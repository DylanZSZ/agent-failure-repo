#!/usr/bin/env python3
"""Read independent trainer receipts; never import the evaluated launcher."""
from pathlib import Path
import argparse
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "environment"))
from harness import judge

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--state", type=Path, required=True)
args = parser.parse_args()
result = judge(args.state)
print(json.dumps(result, indent=2, sort_keys=True))
raise SystemExit(0 if result["validity"] == "valid" and result["task_success"] else 1)

