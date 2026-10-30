# Collect sessions and assess long-horizon task candidates

For the current local review, see [workflow explanation, task catalog, and results](docs/collections/workflow-evaluation-20261030/README.md). It separates collection evidence from task construction and model outcomes.

The [English evaluation report](docs/collections/workflow-evaluation-20261030/RESULTS.md) explains target-hit counts, denominators, unresolved tasks, and the limits of the current evidence.

Collect observable agent behavior from authorized Claude Code and Codex history, then assess which observations support a long-horizon task. A selected observation is not automatically a validated task or a reproduced failure. Current rules: [AGENTS.md](AGENTS.md), revision 2026-10-28.

## Copy this message

> Read the current checkout's AGENTS.md. Collect task-design reference sessions from my authorized project history in a stated batch, grouping by actual task. First record directly observed actions with original evidence and read/unread ranges; defensive-coding observations do not require damage, product failure, or causal proof. Distinguish the coordinator/reviewer from the tested agent and verify the latter's native trace when available. For proposed long-horizon tasks, link a task-candidate card naming the work setting, concrete mechanism, source difficulty and state dependency retained in the new task; distinguish observed from constructed elements and reused carriers from adaptations or new tasks. Keep selection, task suitability, run completeness, and product outcome separate. Keep histories local and report evidence, gaps, and the next unread scope. This collection request does not authorize paid runs or publication.

## Collect a batch

1. Inventory authorized sources by project metadata and state the batch boundary before selection. Keep source IDs, paths, fingerprints, and relationships in the private index.
2. Group by actual objective, including related children and continuations. Browse requests, actions/results, and handoffs, then expand candidate windows to reconstruct the full task arc. Check original events for assignments omitted by the human navigation view. Read remaining ranges before claiming comprehensive coverage.
3. Record selected, needs-evidence, or not-selected in .local/session-selection.csv. Write observed facts before design uses. Keep missing continuations explicit; an unavailable decisive original is needs-evidence for that claim. A normal reference must name the target behavior it contrasts.
4. For proposed long-horizon tasks, use [templates/task-candidate.md](templates/task-candidate.md). Link the private card in the existing design_use_or_reason column. Retain the five-column ledger format. The card separates observation evidence, state dependency, observed versus constructed elements, carrier origin, and actual run results.
5. Deliver REPORT.md linked to the session list, candidate cards, and coverage ledger. Report unresolved evidence and the next unread scope. Completed batches are progress units when a broader search was requested.

Run from this checkout or create/resume a workspace with python3 commands/start.py. Its response identifies current workflow rules and a content fingerprint; use those rules even when a workspace has an older AGENTS.md. Evidence files are preserved.

    python3 commands/history.py inventory --project /path/to/project --output .local/history-index.json
    python3 commands/history.py read --index .local/history-index.json --source SOURCE_ID --start-line 1 --max-lines 200

The reader supplies anchors and omissions, not judgments. Use next_start_line to expand context. Consult [docs/HISTORY.md](docs/HISTORY.md) for format issues and coverage mechanics.

## Check whether selection works

Freeze source IDs, hashes, and allowed reading scope before an independent check. Reader-facing manifests must not reveal expected labels, previous selections, or explanatory titles. Inspect selected and unselected sources independently before comparing. Material already used to edit rules is a development replay, not independent validation. Report supported choices, missed useful sessions, evidence usability, and reading cost only within that pool.

Iterate for a concrete missed/weak selection, missing original, wrong grouping, or repeated work. Apply the smallest relevant change and a targeted check, then return to collection. A runnable reused carrier does not by itself validate the selector or establish new task design.

Full reconstruction and public submission have separate contracts in docs/LONG_HORIZON.md and docs/REPRODUCING.md. Their admission gates do not suppress direct defensive-behavior observations. Collection alone authorizes neither paid model calls nor sharing raw histories.
