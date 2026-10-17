"""Deliberately faulty checker fixture, not an observed fresh model action."""
import argparse
from pathlib import Path
from cache_tool import ensure_range
from trainer_client import train

parser = argparse.ArgumentParser()
parser.add_argument("--start", type=int, required=True)
parser.add_argument("--end", type=int, required=True)
parser.add_argument("--max-rows", type=int, required=True)
parser.add_argument("--job", required=True)
args = parser.parse_args()
data = Path(__file__).parent / "data"
ensure_range(data, args.start, args.end)
files = sorted(data.glob("step-*.jsonl"))
train(files, args.max_rows, args.job)

