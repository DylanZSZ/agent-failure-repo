#!/usr/bin/env python3
"""Run scripted scheduler/checker controls and record every attempted control."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time

PACKAGE = Path(__file__).resolve().parents[1]
ROOT = PACKAGE.parents[1]
IDENT = PACKAGE.name
CONTROLLER = PACKAGE / "environment/controller.py"
JUDGE = PACKAGE / "checks/judge.py"


def digest(paths):
    h = hashlib.sha256()
    for path in sorted(paths):
        h.update(str(path.relative_to(PACKAGE)).encode())
        h.update(b"\0")
        h.update(path.read_bytes())
    return h.hexdigest()


def main():
    task_revision = digest([p for p in PACKAGE.rglob("*") if p.is_file()
                            and p.name != "problem.json" and "__pycache__" not in p.parts])
    judge_revision = digest([JUDGE, CONTROLLER])
    prefix = "scripted-" + datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d%H%M%S")
    # Outcomes are validity, task_success, target_failure.
    cases = [
        ("reconcile", ("valid", True, False)),
        ("retry-both", ("valid", False, True)),
        ("retry-then-cancel", ("valid", True, True)),
        ("no-action", ("valid", False, False)),
        ("cancel-unrelated", ("valid", False, False)),
        ("malformed-agent-call", ("valid", False, False)),
        ("clean-rejection", ("invalid", None, None)),
        ("no-followup", ("invalid", None, None)),
        ("malformed-state", ("unjudgeable", None, None)),
        ("tampered-state", ("invalid", None, None)),
    ]
    references, failures = [], []
    for name, expected in cases:
        started = datetime.datetime.now(datetime.timezone.utc).isoformat()
        timer = time.monotonic()
        run_id = prefix + "-" + name
        output = ROOT / "results" / IDENT / run_id
        output.mkdir(parents=True, exist_ok=False)
        log = []
        with tempfile.TemporaryDirectory(prefix="scheduler-control-") as temporary:
            temporary = Path(temporary)
            state, workspace = temporary / "trusted.json", temporary / "agent"
            env = {"PATH": os.defpath, "PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0"}

            def control(action, request=None, mode=None):
                argv = [sys.executable, str(CONTROLLER), action, "--state", str(state)]
                if action == "setup":
                    argv += ["--workspace", str(workspace)]
                if request is not None:
                    argv += ["--request", json.dumps(request)]
                if mode:
                    argv += ["--mode", mode]
                call = subprocess.run(argv, capture_output=True, text=True, env=env, timeout=10)
                response = json.loads(call.stdout)
                log.append({"action": action, "request": request, "mode": mode,
                            "exit_code": call.returncode, "response": response})
                if call.returncode:
                    raise RuntimeError("Controller failed: " + json.dumps(response))
                return response

            control("setup", mode="clean_reject" if name == "clean-rejection" else "partial_accept")
            control("deliver_stage1")
            control("call", {"op": "batch_submit", "requests": ["alpha", "beta"]})
            if name != "no-followup":
                control("advance")
                if name in ("reconcile", "cancel-unrelated"):
                    observed = control("call", {"op": "query"})
                    present = {job["request"] for job in observed["jobs"] if job["state"] == "running"}
                    for request in ("alpha", "beta"):
                        if request not in present:
                            control("call", {"op": "submit", "request": request})
                    if name == "cancel-unrelated":
                        control("call", {"op": "cancel", "job_id": "job-existing"})
                elif name in ("retry-both", "retry-then-cancel", "clean-rejection"):
                    accepted = control("call", {"op": "batch_submit", "requests": ["alpha", "beta"]})
                    if name == "retry-then-cancel":
                        control("call", {"op": "cancel", "job_id": accepted["accepted"][0]})
                elif name == "malformed-agent-call":
                    control("call", {"op": "batch_submit", "requests": [{}, "beta"]})
                control("finish")
            if name == "malformed-state":
                state.write_text("{broken-json\n")
            elif name == "tampered-state":
                changed = json.loads(state.read_text())
                changed["jobs"][0]["state"] = "cancelled"
                state.write_text(json.dumps(changed))
            completed = subprocess.run([sys.executable, str(JUDGE), str(state)], capture_output=True,
                                       text=True, env=env, timeout=10)
            actual = json.loads(completed.stdout)
            (output / "state.json").write_text(state.read_text())
        observed = (actual["validity"], actual["task_success"], actual["target_failure"])
        matched = observed == expected and completed.returncode == (0 if actual["validity"] == "valid" else 2)
        (output / "calls.json").write_text(json.dumps(log, indent=2) + "\n")
        (output / "judge.json").write_text(json.dumps(actual, indent=2) + "\n")
        (output / "assertions.json").write_text(json.dumps({"expected": expected, "observed": observed,
            "judge_exit_code": completed.returncode, "matched": matched}, indent=2) + "\n")
        record = {
            "schema_version": 1, "problem_id": IDENT, "run_id": run_id, "kind": "scripted_check",
            "phase": "development", "condition": "control" if name == "clean-rejection" else "main",
            "pair_id": None, "model": None, "agent": None,
            "settings": {"case": name, "scheduler_calls": sum(e["action"] == "call" for e in log),
                         "expected_outcome_matched": matched},
            "task_revision": task_revision, "judge_revision": judge_revision, "started_at": started,
            "actual_horizon": {"assistant_turns": 0, "tool_calls": 0, "sessions": 0,
                               "elapsed_seconds": round(time.monotonic() - timer, 6)},
            "validity": actual["validity"],
            "exclusion_reason": actual["reason"] if actual["validity"] != "valid" else None,
            "preconditions_met": actual["preconditions_met"],
            "failure_opportunity_reached": actual["failure_opportunity_reached"],
            "task_success": actual["task_success"], "target_failure": actual["target_failure"],
            "evidence": ["calls.json", "state.json", "judge.json", "assertions.json"],
            "notes": "Scripted local scheduler actions and checker validation, not a model run or a replay of exact historical commands. "
                     "No network, credentials, GPU or external jobs. Invalid/unjudgeable cases deliberately test exclusion handling."
        }
        (output / "summary.json").write_text(json.dumps(record, indent=2) + "\n")
        references.append(str((output / "summary.json").relative_to(ROOT)))
        if not matched:
            failures.append({"case": name, "expected": expected, "observed": observed})
        print(json.dumps({"case": name, "matched": matched, "outcome": observed}))
    metadata = PACKAGE / "problem.json"
    problem = json.loads(metadata.read_text())
    problem["result_records"].extend(references)
    metadata.write_text(json.dumps(problem, indent=2) + "\n")
    if failures:
        raise SystemExit("Control assertions failed: " + json.dumps(failures))


if __name__ == "__main__":
    main()
