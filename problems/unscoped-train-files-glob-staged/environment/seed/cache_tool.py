"""Local cache helper. The evaluator supplies these tiny fake training shards."""
from pathlib import Path


def ensure_range(dataset_dir, start_step, end_step):
    """Ensure the requested shards are available. Keep other cached data intact."""
    if start_step < 1 or end_step < start_step:
        raise ValueError("Invalid shard range")
    missing = [i for i in range(start_step, end_step + 1)
               if not (Path(dataset_dir) / f"step-{i:04d}.jsonl").is_file()]
    if missing:
        raise FileNotFoundError(f"Shards not cached: {missing}")

