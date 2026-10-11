# Collection: sft-rollout-pipeline-2026-10

Collection date: 2026-10-10/11. Agent: Claude Code (Sonnet 5), single session,
self-collected (the collecting assistant is also the agent whose failure is
recorded). Contributor identity withheld; referred to as "the contributor."

## Scope actually covered

Authorized source: a single long Claude Code conversation, covering ongoing
work on an HPC ML research project (an SFT training pipeline built on `verl`).
The contributor authorized this conversation, "the available past agent
sessions for my current project," and any history exports they might supply.
No history exports were supplied. The newly-added `commands/history.py`
project-scoped historical-session reader was not run in this pass — inventorying
and reading other past Claude Code/Codex sessions for this project is deferred
to a later pass if the contributor wants it (see `coverage.md`).

Inspected range: the full raw (non-summarized) portion of the authorized
conversation. An earlier portion of the same conversation exists only as an
auto-generated prose summary (a context-compaction boundary); it was not
re-scanned for additional incidents in this pass, since a prose summary is not
reliable enough to extract verifiable incident evidence from.

A full, explicit pass against all 20 symptoms, individually, across the entire
inspected range, was not performed as a formal checklist exercise; candidates
were found via chronological re-reading and mapped to symptom IDs afterward.

## Findings summary

- Distinct candidates recorded: 4
- Distinct incidents supported by direct evidence: 4
- Packaged reproductions (full evidence record, working minimal repro, judge,
  verified by direct execution): 1 — `unscoped-train-files-glob`
- Condensed/candidate records (root cause and evidence identified, full
  evidence template and reproduction not yet built): 3
- Fresh model reproductions run: 0
- Rejected or duplicate candidates: 0

This collection pass ran as a side task inside a session simultaneously
responsible for monitoring the contributor's real, actively-running,
budget-constrained GPU training jobs. One incident was developed deeply and
verified by direct execution rather than four developed shallowly.

## Packaged incident: `unscoped-train-files-glob`

A training-launch script's data-file selection used an unscoped shell glob
over a shared directory, while separate `START_STEP`/`END_STEP` variables
(intended to scope the training range) were wired only into a download-range
check, never into the actual file selection. Every sub-range training job
that didn't happen to start at the first available shard silently trained on
the wrong data for roughly two weeks of real work before an anomalous job
runtime led to discovery and a verified fix.

Consequence, in the contributor's own words after the scope of the problem was
established (quoted with the contributor's explicit review and approval to
share): *"This is devastating. and this really is 90% of what was done over
the past 2 weeks. I don't think I have enough gpu hours left to redo them."*

Full details, evidence, and a working, directly-executed minimal reproduction:
[`problems/unscoped-train-files-glob/`](../../../problems/unscoped-train-files-glob/).

## Deferred candidates (incident-only; not packaged in this pass)

| ID | One-line description | Consequence | Why deferred |
| --- | --- | --- | --- |
| `missing-total-training-steps-fallback` | Two launch scripts omitted a step-count override and silently fell back to a 10-step smoketest default instead of hundreds of steps. | Two completed jobs had to be identified as wrong, deleted, and relaunched; a third instance was caught before launch. | Time; condensed evidence only, no reproduction built. |
| `premature-fsdp-deletion-unverified-merge-assumption` | An automated checkpoint-pruning watcher deleted raw model weights for 8 checkpoints based on an unverified generalization (from a small, non-representative sample of prior checkpoints) that a separate merge step ran automatically. It did not. | Entire 8-checkpoint, multi-hour training chain had to be fully rerun from scratch — irreversible loss of the original weights. | Time; recommended as the next candidate for full packaging given the irreversible-deletion severity class. |
| `bash-local-combined-assignment-bug` | A combined `local a=x b=$a` shell assignment doesn't chain in bash; crashed a verification step (under `set -u`) immediately after the real work it was checking had already completed correctly. | Minor: one-turn delay, no data loss. | Low severity; lower priority. |

Full private evidence notes for all three (not included in this public
submission): retained in the contributor's local, git-ignored collection
workspace.

## What was NOT done in this pass

- No fresh-model-attempt evaluation condition was run against the packaged
  reproduction. `problem.json`'s `result_records` include only scripted
  checks (a mechanism replay, a reference-solution check, and a
  faulty-solution control), not a fresh model being asked to solve the task.
- The three deferred candidates have no reproduction package, no judge, and
  no `problems/` directory.
- `commands/history.py` was not run; only the current conversation was
  inspected.

## Next action / continuation point

1. If useful, run `commands/history.py` against this same project's other
   local Claude Code/Codex sessions, if the contributor authorizes that for a
   future pass.
2. Develop `premature-fsdp-deletion-unverified-merge-assumption` into a full
   package next — it is the highest-severity deferred candidate.
3. Run a fresh-model-attempt evaluation condition against
   `unscoped-train-files-glob`'s existing task/judge.
