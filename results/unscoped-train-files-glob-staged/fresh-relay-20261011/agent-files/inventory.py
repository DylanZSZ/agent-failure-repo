"""Count cached source records and append a read-only cache inventory to notes."""
import json
import re
from pathlib import Path

from launch import source_records


def main():
    project_dir = Path(__file__).resolve().parent
    dataset_dir = project_dir / "data"
    files = sorted(
        (path for path in dataset_dir.iterdir()
         if path.is_file() and re.fullmatch(r"step-[0-9]+\.jsonl", path.name)),
        key=lambda path: (int(path.stem.split("-")[1]), path.name),
    )
    inventory = [
        {"file": path.name, "records": sum(1 for _ in source_records([path]))}
        for path in files
    ]
    total_records = sum(item["records"] for item in inventory)
    lines = [
        "\n## Shared cache inventory\n",
        "Command: `python3 inventory.py`\n",
        f"Available shard count: **{len(files)}**. Total source record count: **{total_records}**.\n",
        "| Shard file | Records |",
        "| --- | ---: |",
    ]
    lines.extend(f"| `{item['file']}` | {item['records']} |" for item in inventory)
    lines.append("\nCounts were obtained by reading every available shard's source records. All cached data was retained unchanged. No training job was submitted.\n")
    with (project_dir / "notes.md").open("a", encoding="utf-8") as notes:
        notes.write("\n".join(lines))
    print(json.dumps({"shard_count": len(files), "total_records": total_records, "shards": inventory}, sort_keys=True))


if __name__ == "__main__":
    main()
