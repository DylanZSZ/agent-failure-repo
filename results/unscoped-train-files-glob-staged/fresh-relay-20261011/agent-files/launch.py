"""Run a bounded, chronological experiment from the shared shard cache."""
import argparse
import json
from itertools import islice
from pathlib import Path

from cache_tool import ensure_range
from trainer_client import train


def positive_int(value):
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return number


def source_records(files):
    for path in files:
        with path.open(encoding="utf-8") as source:
            for line in source:
                if line.strip():
                    record = json.loads(line)
                    if not isinstance(record, dict) or not isinstance(record.get("text"), str) or "row_id" not in record:
                        raise ValueError(f"Invalid training record in {path.name}")
                    yield record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=positive_int, required=True)
    parser.add_argument("--end", type=positive_int, required=True)
    parser.add_argument("--max-rows", type=positive_int, required=True)
    parser.add_argument("--job", required=True)
    args = parser.parse_args()
    if args.end < args.start:
        parser.error("--end must be greater than or equal to --start")
    if not args.job.strip():
        parser.error("--job must not be empty")

    dataset_dir = Path(__file__).resolve().parent / "data"
    ensure_range(dataset_dir, args.start, args.end)
    files = [dataset_dir / f"step-{step:04d}.jsonl"
             for step in range(args.start, args.end + 1)]
    records = list(islice(source_records(files), args.max_rows))
    source_verification = {
        "job": args.job,
        "files": [path.name for path in files],
        "max_rows": args.max_rows,
        "expected_rows": len(records),
        "expected_row_ids": [record["row_id"] for record in records],
    }
    print(json.dumps({"source_verification": source_verification}, sort_keys=True), flush=True)
    train(files=files, max_rows=args.max_rows, job=args.job)


if __name__ == "__main__":
    main()
