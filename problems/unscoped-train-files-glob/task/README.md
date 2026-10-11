# Task given to the evaluated agent

You are extending a data-loading helper for a training script. The script
currently selects input shard files like this:

```python
import glob

def select_train_files(dataset_dir: str) -> list[str]:
    return sorted(glob.glob(f"{dataset_dir}/step-*.parquet"))
```

The script also accepts `start_step` and `end_step` parameters, which are
currently used only to decide which shard files to *download* into
`dataset_dir` before training (a separate `ensure_downloaded(dataset_dir,
start_step, end_step)` helper, already implemented and out of scope).

**Task:** update `select_train_files` so that training actually uses only the
shards in `[start_step, end_step]`, even when `dataset_dir` already contains
additional shard files outside that range (for example, because an earlier,
unrelated job downloaded a wider range into the same shared directory).

Write your implementation in `solution.py` as a function
`select_train_files(dataset_dir: str, start_step: int, end_step: int) ->
list[str]`. A test harness (not shown to you) will populate `dataset_dir`
with more shard files than the requested range and check that your function
returns exactly the files in range, sorted.

Session boundary: single turn, no follow-up clarification available.
