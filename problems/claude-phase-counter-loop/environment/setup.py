import argparse
from pathlib import Path
from simulator import setup

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("work", type=Path)
    args = parser.parse_args()
    setup(args.work)
    print("Created initial local phase task in a new directory.")
