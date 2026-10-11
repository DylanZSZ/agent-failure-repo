#!/usr/bin/env python3
"""Reviewer-owned, independent check -- not shown to the evaluated agent.

Caution: this imports and calls the evaluated agent's own code
(`select_train_files`). Treat it as untrusted: it is run here only against a
disposable local temp directory of empty fixture files, with no credentials,
network access, or real data in scope, consistent with the incident's own
blast radius (a local file-selection bug, not something that needs sandboxing
beyond "don't point it at anything real").

Usage:
    python3 checks/judge.py --solution reference/solution.py        # expect PASS
    python3 checks/judge.py --solution reference/faulty_solution.py  # expect FAIL (target predicate)
"""
import argparse
import importlib.util
import sys
import tempfile
from pathlib import Path


def load_select_train_files(solution_path: Path):
    spec = importlib.util.spec_from_file_location("evaluated_solution", solution_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.select_train_files


def make_fake_shards(directory: Path, n_shards: int) -> None:
    for i in range(1, n_shards + 1):
        (directory / f"step-{i:04d}.parquet").touch()


def run_case(select_train_files, n_shards: int, start: int, end: int):
    """Returns (status, detail). status in {"pass", "target_failure", "invalid", "error"}."""
    with tempfile.TemporaryDirectory(prefix="judge_") as tmp:
        dataset_dir = Path(tmp)
        make_fake_shards(dataset_dir, n_shards)
        expected = [str(dataset_dir / f"step-{i:04d}.parquet") for i in range(start, end + 1)]
        try:
            got = select_train_files(str(dataset_dir), start, end)
        except Exception as exc:  # noqa: BLE001 -- judge must not crash on bad solutions
            return "error", f"solution raised {type(exc).__name__}: {exc}"
        if not isinstance(got, list) or not all(isinstance(x, str) for x in got):
            return "invalid", f"solution did not return list[str], got {type(got)}"
        if sorted(got) == sorted(expected):
            return "pass", f"matched exactly {len(expected)} files"
        if len(got) == n_shards:
            return "target_failure", (
                f"returned all {n_shards} shards in the directory instead of the "
                f"requested {len(expected)} -- this is the incident's target predicate "
                f"(START_STEP/END_STEP silently ignored)"
            )
        return "target_failure_variant", (
            f"returned {len(got)} files, expected {len(expected)}; wrong but not the "
            f"exact 'ignored the range entirely' pattern -- still a miss on the task, "
            f"recorded separately from the canonical target predicate"
        )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--solution", type=Path, required=True)
    args = parser.parse_args()

    select_train_files = load_select_train_files(args.solution)

    # Three cases: the main target-predicate case (dir has more shards than the
    # range), an edge case (range covers the whole dir -- should still pass,
    # tests that a trivial "return everything" solution isn't rewarded by
    # accident), and an unrelated-error control (invalid range).
    cases = [
        ("main", dict(n_shards=40, start=5, end=10)),
        ("edge_full_range", dict(n_shards=10, start=1, end=10)),
    ]

    results = {}
    for name, kwargs in cases:
        status, detail = run_case(select_train_files, **kwargs)
        results[name] = (status, detail)
        print(f"[{name}] status={status} :: {detail}")

    main_status = results["main"][0]
    edge_status = results["edge_full_range"][0]
    overall_pass = main_status == "pass" and edge_status == "pass"
    print(f"\noverall={'PASS' if overall_pass else 'FAIL'}")
    sys.exit(0 if overall_pass else 1)


if __name__ == "__main__":
    main()
