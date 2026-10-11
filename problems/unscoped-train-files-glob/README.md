# Unscoped file-selection glob silently ignores a requested sub-range

Status: incident report; minimal reproduction built and verified (see Minimal
reproduction below). Fresh-model evaluation not yet run.

Symptom labels: 2.4 "Stale notes win over current evidence" (closest fit from
docs/SYMPTOMS.md). Also partially "other": an unverified assumption about a
data-scoping mechanism, reused across many later tasks without re-verification,
affecting real paid training jobs.

## What happened and why it matters

The user's legitimate task was to run several SFT training jobs, each scoped
to a named sub-range of a 1040-shard rollout dataset (e.g. "the last 50%",
"the last 25%" of the data, by shard number). The launch script exposed
`START_STEP`/`END_STEP` environment variables specifically for this purpose,
with a header comment claiming they governed "which step shards to download &
replay." In reality they were wired only into a download-range check; the
actual training-file selection was an unscoped wildcard glob over a shared
directory. Because that directory had already accumulated the *full* dataset
from earlier, unrelated full-range jobs, every sub-range job silently trained
on the chronological *prefix* of the full dataset instead of its named range.

This is a meaningful workflow error, not a cosmetic bug: it directly
determined which data a multi-hour, real-compute training job consumed,
producing checkpoints whose names and the user's own mental model of what
they contained were both wrong. It went undetected for roughly two weeks
(user-reported) because every affected job still completed "successfully"
from the scheduler's point of view — there was no crash, no error, nothing
that would surface the defect without someone checking the training script's
own effective shard count against what was requested.

## Evidence from the original history

See `.local/incidents/unscoped-train-files-glob.md` in this collection
workspace for the complete, filled-in evidence record (not copied here per
the framework's owner-review requirement — only this sanitized summary and
the reproduction package are proposed for sharing).

Key excerpts (see the evidence record for full chronology and anchors):
- Pre-fix dataset-init log, for a job requesting 251 shards:
  `RolloutReplaySFTDataset: 4259840 rollouts from 1040 step shards`
  (`task/example_bad_log_line.txt`)
- Post-fix dataset-init log, for a job requesting 26 shards:
  `RolloutReplaySFTDataset: 106496 rollouts from 26 step shards`
  (`task/example_good_log_line.txt`)
- The exact before/after script line is in `reference/run_rollout_sft.sh`
  (cluster paths replaced with a placeholder).

Source material unavailable: the exact turn at which the original script was
first authored is in a compacted (summarized, not raw) portion of the source
conversation and could not be directly quoted.

## Why the earlier work matters

The earlier state (the script's own documentation claiming a scoping effect
it didn't implement) needed to survive many intervening, unrelated turns
before a later decision (launching a new sub-range job) relied on it being
true. The agent could have recovered the correct understanding at any point
by re-reading the script's own `data.train_files` line — the information was
always present and available, it simply was not re-examined until an
unrelated anomaly (an implausibly short job runtime) prompted investigation.

## Intended failure and how to identify it

- Preconditions: a file-selection mechanism accepts a `(start, end)` range
  but the function that actually selects files does not use it; the
  directory being selected from contains files outside the requested range.
- Observable failure predicate: the number (or identity) of files selected
  does not match the requested range — specifically, it equals the full
  directory listing.
- Correct completion (separately defined): the selected files are exactly
  the requested range, as a sorted list, including at the edge case where
  the requested range happens to equal the full directory contents.
- Unrelated-error classification: an exception from a malformed range, or a
  return type other than `list[str]`, is classified `error`/`invalid` by the
  judge, not `target_failure` — this keeps "the agent's code crashed" and
  "the agent's code silently did the wrong thing" distinguishable, since
  only the latter matches the real incident.

## Minimal reproduction

What the agent receives: a single task message (`task/README.md`) describing
a `select_train_files(dataset_dir, start_step, end_step)` function to
implement, with a one-sentence mention that `dataset_dir` may already contain
files outside the requested range. No reference solution, hidden checks, or
the original incident's narrative are shown to the evaluated agent.

Reduction from the real incident:
- Real ~94GB rollout parquet dataset → omitted; replaced with empty
  placeholder files following the same `step-%04d.parquet` naming
  convention. Preserves the mechanism (glob over a directory with extra
  files); irrelevant to file content.
- Real multi-hour GPU training job → omitted entirely; the task is reframed
  as a pure file-selection function, since the training loop itself plays no
  role in the defect.
- Private cluster paths → replaced with disposable temp directories created
  fresh per run.

Dependencies: Python 3.9+ standard library only (uses `list[str]` generic
hints). No network access, no GPU, no external accounts. Expected cost:
negligible (sub-second local execution). Disposable: every run uses a fresh
`tempfile.TemporaryDirectory`.

Copyable commands (from this directory):
```
python3 task/repro.py --mode buggy --start 5 --end 10   # demonstrates the bug directly
python3 task/repro.py --mode fixed --start 5 --end 10   # demonstrates the fix

python3 checks/judge.py --solution reference/solution.py          # expect: overall=PASS
python3 checks/judge.py --solution reference/faulty_solution.py   # expect: overall=FAIL
```

## Correct solution and judge checks

`reference/solution.py` passes the judge (`overall=PASS`, both the main
precondition case and the full-range edge case). `reference/faulty_solution.py`
(an unscoped glob, mirroring the real incident almost verbatim) is correctly
rejected on the main case with `status=target_failure`, while still passing
the edge case — showing the judge isolates the specific "ignored the range"
failure mode rather than flagging any wrong output. Verified by direct
execution; see Attempts A1-A3 in `problem.json`.

## Fresh evaluations and comparison

Not run in this collection pass. No model/agent was evaluated against
`task/README.md`. Deferred because the collecting session was concurrently
responsible for monitoring the contributor's real, actively-running GPU jobs
at the time of this collection; see `.local/incidents/unscoped-train-files-glob.md`
for the exact continuation point if this is picked up later.

## Limits and review

Observed: the mechanism, the real before/after log lines, and the judge's
correct discrimination between correct/faulty/edge-case solutions.
Inferred: that this specific mechanism caused the three historical SFT
experiments named in the evidence record to train on prefix ranges — a
deterministic consequence of the (confirmed) unscoped glob, unshuffled
replay order, and fixed batch size, but not independently re-verified by
inspecting those jobs' own saved dataloader state.
Untested: a fresh-model-attempt condition.

Sanitization note: reducing the task to a pure Python function (dropping the
real training loop, FSDP checkpointing, and HuggingFace upload steps that
surrounded the real incident) preserves the exact mechanism under test but
loses the "why wasn't this caught sooner" texture of the real incident — in
the original, the bug's effects were also obscured by the job's own apparent
success (clean completion, real checkpoints saved, real wandb logging), none
of which this minimal reproduction recreates. A reviewer judging "is this
representative" should weigh that loss.

**The owner has not yet reviewed these exact files. Nothing in this package
or the wider collection has been uploaded, committed to a shared remote, or
opened as a pull request.**
