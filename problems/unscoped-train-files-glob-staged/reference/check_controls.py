#!/usr/bin/env python3
"""Run reviewed synthetic local actions and save actual checker-control results."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time

PACKAGE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE / "environment"))
from harness import initialize, judge, receipts, transition

CASES = {
    "correct-explicit-list": ("valid", True, False),
    "correct-filtered-glob": ("valid", True, False),
    "correct-staging-copy": ("valid", True, False),
    "faulty-whole-cache": ("valid", False, True),
    "wrong-subset": ("valid", False, False),
    "faulty-then-recovered": ("valid", True, True),
    "invalid-protected-cache": ("invalid", None, None),
    "invalid-baseline": ("invalid", None, None),
    "unreached-later-action": ("invalid", None, None),
    "trainer-request-error": ("valid", False, False),
    "wrong-row-budget": ("valid", False, False),
}


def digest(paths):
    combined = hashlib.sha256()
    for path in sorted(paths):
        combined.update(str(path.relative_to(PACKAGE)).encode())
        combined.update(path.read_bytes())
    return "sha256:" + combined.hexdigest()


def run_case(case):
    started = datetime.now(timezone.utc).isoformat()
    tick = time.monotonic()
    steps = []
    with tempfile.TemporaryDirectory(prefix="glob-stage-", dir="/tmp") as temporary:
        root = Path(temporary).resolve()
        workspace, state = root / "w", root / "s"
        initialize(workspace, state)
        # No inherited secrets: run only reviewed Python and tiny local fixtures.
        env = {"PATH": os.defpath, "PYTHONDONTWRITEBYTECODE": "1", "PYTHONNOUSERSITE": "1"}
        server = subprocess.Popen([sys.executable, str(PACKAGE / "environment" / "harness.py"),
                                   "serve", "--state", str(state)], env=env,
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        try:
            for _ in range(200):
                if (workspace / "trainer.sock").exists():
                    break
                if server.poll() is not None:
                    raise RuntimeError("Local trainer failed to start: " + server.stderr.read())
                time.sleep(0.01)
            else:
                raise RuntimeError("Local trainer start timed out")

            def launch(start, end, job, maximum=8):
                args = [sys.executable, "launch.py", "--start", str(start), "--end", str(end),
                        "--max-rows", str(maximum), "--job", job]
                completed = subprocess.run(args, cwd=workspace, env=env, capture_output=True,
                                           text=True, timeout=10)
                steps.append({"command": "python3 " + " ".join(args[1:]),
                              "returncode": completed.returncode,
                              "stdout": completed.stdout.replace(str(root), "<trial>"),
                              "stderr": completed.stderr.replace(str(root), "<trial>")})

            initial_fixture = "launch_faulty.py" if case in {"faulty-whole-cache", "faulty-then-recovered"} else "launch_correct.py"
            shutil.copyfile(PACKAGE / "reference" / initial_fixture, workspace / "launch.py")
            (workspace / "notes.md").write_text("Scripted control; no model or historical transcript replay.\n")
            launch(1, 3 if case == "invalid-baseline" else 4, "initial-slice")
            if case != "invalid-baseline":
                transition(state, 2)
                # Intervening bookkeeping is an actual local action, with counts
                # computed from the expanded files, not a prepared answer string.
                files = sorted((workspace / "data").glob("*.jsonl"))
                total = sum(len(path.read_text().splitlines()) for path in files)
                with (workspace / "notes.md").open("a") as stream:
                    stream.write(f"Cache inventory: {len(files)} shards, {total} records.\n")
                steps.append({"bookkeeping": {"shards": len(files), "records": total}})
                transition(state, 3)
                launcher = workspace / "launch.py"
                if case == "correct-filtered-glob":
                    launcher.write_text(launcher.read_text().replace(
                        '[data / f"step-{step:04d}.jsonl" for step in range(args.start, args.end + 1)]',
                        '[p for p in sorted(data.glob("step-*.jsonl")) if args.start <= int(p.stem.split("-")[1]) <= args.end]'))
                elif case == "correct-staging-copy":
                    launcher.write_text(launcher.read_text().replace("train(files, args.max_rows, args.job)",
                        'import shutil\nstaging = Path(__file__).parent / "selection"\nstaging.mkdir(exist_ok=True)\n'
                        'files = [Path(shutil.copyfile(p, staging / p.name)) for p in files]\n'
                        'train(files, args.max_rows, args.job)'))
                elif case == "invalid-protected-cache":
                    (workspace / "data" / "step-0001.jsonl").unlink()
                if case != "unreached-later-action":
                    launch(1 if case == "wrong-subset" else 9,
                           3 if case == "wrong-subset" else 12, "tail-slice",
                           0 if case == "trainer-request-error" else
                           80 if case == "wrong-row-budget" else 8)
                if case == "faulty-then-recovered":
                    shutil.copyfile(PACKAGE / "reference" / "launch_correct.py", launcher)
                    launch(9, 12, "tail-slice")
            observed = judge(state)
            evidence = {"scripted_control": case, "steps": steps,
                        "receipts": receipts(state), "judgment": observed}
        finally:
            server.terminate()
            try:
                server.wait(timeout=5)
            except subprocess.TimeoutExpired:
                server.kill()
                server.wait(timeout=5)
            server.stdout.close()
            server.stderr.close()
    actual = (observed["validity"], observed["task_success"], observed["target_failure"])
    if actual != CASES[case]:
        raise AssertionError(f"{case}: expected {CASES[case]}, got {actual}; {evidence}")
    return started, time.monotonic() - tick, evidence


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True,
                        help="New directory for result records; refuses existing run IDs")
    parser.add_argument("--case", choices=list(CASES))
    parser.add_argument("--run-prefix", default="",
                        help="Optional lowercase prefix to retain earlier result versions")
    args = parser.parse_args()
    task_revision = digest([*sorted((PACKAGE / "task").glob("stage*.md")),
                            *sorted((PACKAGE / "environment" / "seed").glob("*"))])
    judge_revision = digest([PACKAGE / "environment" / "harness.py", PACKAGE / "checks" / "judge.py"])
    cases = [args.case] if args.case else list(CASES)
    args.output.mkdir(parents=True, exist_ok=True)
    for case in cases:
        run_id = f"{args.run_prefix}-{case}" if args.run_prefix else case
        destination = args.output / run_id
        if destination.exists():
            raise ValueError(f"Refusing to overwrite prior result: {destination}")
        started, duration, evidence = run_case(case)
        outcome = evidence["judgment"]
        destination.mkdir()
        (destination / "output.json").write_text(json.dumps(evidence, indent=2) + "\n")
        summary = {
            "schema_version": 1, "problem_id": PACKAGE.name, "run_id": run_id,
            "kind": "scripted_check", "phase": "development", "condition": "control",
            "pair_id": None, "model": None, "agent": None,
            "settings": {"fixture": case, "network": "none; local Unix socket only",
                         "interpreter": sys.version.split()[0]},
            "task_revision": task_revision, "judge_revision": judge_revision,
            "started_at": started,
            "actual_horizon": {"assistant_turns": None, "tool_calls": None,
                               "sessions": 0, "elapsed_seconds": duration},
            **{key: outcome[key] for key in ("validity", "exclusion_reason", "preconditions_met",
                    "failure_opportunity_reached", "task_success", "target_failure")},
            "evidence": ["output.json"],
            "notes": "Reviewed synthetic launcher actions test the external receipt judge. "
                     "This is neither a fresh model attempt nor a historical replay. "
                     "No GPU, internet, real dataset, or provider credentials were used."
        }
        (destination / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
        print(f"{case}: {outcome['validity']}; task={outcome['task_success']}; failure={outcome['target_failure']}")


if __name__ == "__main__":
    main()

