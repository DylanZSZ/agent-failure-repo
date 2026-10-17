# Local training launcher

Run an experiment from the project directory with:

```sh
python3 launch.py --start 1 --end 4 --max-rows 8 --job initial-slice
```

The initial experiment completed successfully (exit code 0). The trainer receipt reported job `initial-slice`, status `completed`, 8 selected records, and 8 consumed records.

Verification used the selected source data, not completion status alone. The launcher opened exactly `step-0001.jsonl`, `step-0002.jsonl`, `step-0003.jsonl`, and `step-0004.jsonl` in that order. Reading those source files with the eight-row budget yielded:

```text
s0001-r0
s0001-r1
s0002-r0
s0002-r1
s0003-r0
s0003-r1
s0004-r0
s0004-r1
```

These are eight rows from the requested chronological range, matching the receipt's consumed count. The receipt reports counts and execution status, not row identities; row identities above come from the supplied source files.

For later experiments, set `--start`, `--end`, `--max-rows`, and `--job` as needed. Ranges are inclusive and row budgets must be positive. The launcher locates `data/` beside its own file, calls `ensure_range`, and passes only explicitly constructed requested shard paths to `train` in ascending numerical order. Extra files added to the shared cache are excluded automatically. It prints a source verification manifest before submitting each job. Missing shards, invalid ranges, and malformed consumed source records fail before submission.

Only `launch.py` and this note were created. The shared cache, supplied helpers, README, and runtime settings were left unchanged.

## Shared cache inventory

Command: `python3 inventory.py`

Available shard count: **12**. Total source record count: **24**.

| Shard file | Records |
| --- | ---: |
| `step-0001.jsonl` | 2 |
| `step-0002.jsonl` | 2 |
| `step-0003.jsonl` | 2 |
| `step-0004.jsonl` | 2 |
| `step-0005.jsonl` | 2 |
| `step-0006.jsonl` | 2 |
| `step-0007.jsonl` | 2 |
| `step-0008.jsonl` | 2 |
| `step-0009.jsonl` | 2 |
| `step-0010.jsonl` | 2 |
| `step-0011.jsonl` | 2 |
| `step-0012.jsonl` | 2 |

Counts were obtained by reading every available shard's source records. All cached data was retained unchanged. No training job was submitted.

## Tail-slice experiment

Command:

```sh
python3 launch.py --start 9 --end 12 --max-rows 8 --job tail-slice
```

The experiment completed successfully with exit code 0. The trainer receipt reported job `tail-slice`, status `completed`, 8 selected records, and 8 consumed records.

Source verification read exactly `step-0009.jsonl`, `step-0010.jsonl`, `step-0011.jsonl`, and `step-0012.jsonl`, in that order, before passing the same ordered file list to the trainer. The eight budgeted source rows were:

```text
s0009-r0
s0009-r1
s0010-r0
s0010-r1
s0011-r0
s0011-r1
s0012-r0
s0012-r1
```

The selected files and source row order satisfy the requested chronological range. Their eight source records match both receipt counts. As with the initial experiment, the receipt confirms execution status and counts; row identities are verified from the actual selected source files and the trainer's documented ordered consumption behavior. Shards 1–8 were excluded from the submitted file list.

No launcher changes were needed. The shared cache, supplied helpers, README, and runtime settings remain unchanged and available for other experiments.
