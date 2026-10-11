# Coverage: sft-rollout-pipeline-2026-10

## Scope and access

- Collection date: 2026-10-10/11. Responsible contributor: the project owner (identity withheld).
- Authorized projects, sessions, exports, and date ranges: one Claude Code conversation, covering an HPC ML research project's SFT training pipeline work. "The available past agent sessions for my current project" was also authorized, but not inventoried in this pass (see Historical runs table below). No history exports were supplied.
- Sources actually available and inspected: the full raw (non-summarized) portion of the authorized conversation.
- Unavailable sources, truncated exports, or inaccessible tools: an earlier portion of the same conversation exists only as an auto-generated prose summary (context-compaction boundary); not independently verifiable as raw evidence, so not scanned for additional incidents in this pass. No Claude Code/Codex session-store inventory was run.
- Search method and counting units: chronological re-reading of the raw transcript, followed by mapping found candidates to the closest-fitting symptom IDs from `docs/SYMPTOMS.md`. Not a formal per-symptom checklist pass across the entire scope.

## Historical runs from both tools

| Tool | Access status and checked roots | Matching files / logical sessions | Reviewed ranges | Gaps and next action |
| --- | --- | --- | --- | --- |
| Claude Code | **Not checked.** `commands/history.py` (newly available as of this collection's pull of upstream changes) was not run in this pass. | Unknown | None | Run `commands/history.py inventory --project <project-path>` in a future pass if the contributor authorizes it. |
| Codex | **Not checked.** Same reason as Claude Code. | Unknown | None | Same as Claude Code. |

Absence of a Claude Code/Codex session-store scan is not evidence of absence
of further incidents in this project's other sessions.

## Symptom coverage

Not performed as a formal per-symptom pass in this collection round; the four
recorded candidates were found by chronological reading, not systematic
per-symptom search. All 20 symptoms are therefore **unsearched** as a formal
matter, even though the recorded candidates happen to touch on 2.4 and
"other." A dedicated per-symptom pass against the same scope is recommended
before treating this collection as a complete search of the authorized
history.

## Limitations

- This collection reflects one conversation only; the contributor's broader
  authorization (past sessions for this project) has not yet been exercised.
- One incident was developed to full evidence/reproduction depth; three were
  recorded with condensed evidence only, due to the collecting session's
  concurrent responsibility for monitoring real, active GPU jobs.
- No fresh-model-attempt evaluations were run against any candidate.
