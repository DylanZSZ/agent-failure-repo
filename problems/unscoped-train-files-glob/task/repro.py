#!/usr/bin/env python3
"""Minimal, disposable reproduction of the unscoped-train-files-glob incident.

Does not touch any real dataset, GPU, or network resource. Creates a small
directory of empty placeholder shard files, then shows that a wildcard glob
over that directory ignores a requested (start, end) sub-range, while an
explicit file list built from that range does not.

This isolates exactly the mechanism implicated in the incident -- it does not
reproduce the full SFT trainer, the real rollout dataset, or any model.
"""
import argparse
import glob as glob_mod
import tempfile
from pathlib import Path


def make_fake_shards(directory: Path, n_shards: int = 40) -> None:
    for i in range(1, n_shards + 1):
        (directory / f"step-{i:04d}.parquet").touch()


def buggy_train_files(dataset_dir: Path, start: int, end: int) -> list[str]:
    """Mirrors the pre-fix run_rollout_sft.sh: an unscoped wildcard glob.
    START_STEP/END_STEP are accepted as arguments (mirroring how the real
    script accepted them) but never actually used to build the glob -- this
    is the bug."""
    del start, end  # accepted, matching the real signature, but unused: the bug
    return sorted(glob_mod.glob(str(dataset_dir / "step-*.parquet")))


def fixed_train_files(dataset_dir: Path, start: int, end: int) -> list[str]:
    """Mirrors the post-fix run_rollout_sft.sh: an explicit file list built
    from the requested range."""
    return [str(dataset_dir / f"step-{i:04d}.parquet") for i in range(start, end + 1)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["buggy", "fixed"], required=True)
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--end", type=int, required=True)
    parser.add_argument("--n-shards", type=int, default=40,
                         help="Total fake shards present in the directory (simulates a "
                              "shared DATASET_DIR already populated by an earlier, "
                              "unrelated full-range job).")
    args = parser.parse_args()

    with tempfile.TemporaryDirectory(prefix="unscoped_glob_repro_") as tmp:
        dataset_dir = Path(tmp)
        make_fake_shards(dataset_dir, args.n_shards)

        fn = buggy_train_files if args.mode == "buggy" else fixed_train_files
        matched = fn(dataset_dir, args.start, args.end)
        expected_count = args.end - args.start + 1

        print(f"mode={args.mode} requested_range={args.start}-{args.end} "
              f"(expected {expected_count} files) directory_has={args.n_shards} shards")
        print(f"matched_count={len(matched)}")
        print(f"matched_ok={'YES' if len(matched) == expected_count else 'NO (BUG REPRODUCED)'}")


if __name__ == "__main__":
    main()
