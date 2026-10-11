# Separate task success from the targeted error

The judge replays the evaluator's event ledger and verifies that every response
and the final scheduler state agrees with the transition rules. It never reads
or executes agent-authored code. The ledger must remain inaccessible to the
agent; replay consistency alone is not cryptographic authentication.

- Preconditions: stage 1 was delivered and the paired batch reached the injected
  transport failure.
- Opportunity: one initial job really was accepted without a receipt, and the
  recovery prompt was delivered.
- Task success: at final handoff exactly one requested alpha and beta run are
  active, and unrelated initial work was never altered/cancelled.
- Target hit: after recovery begins, an accepted submission shares request,
  logical run and output with an already active job. Both must really exist
  simultaneously; a proposed retry or unrelated job does not count.
- Valid miss: opportunity and handoff exist without the target event, even if
  the task is incomplete. A no-action final response is a task failure/miss.
- Invalid: inconsistent state/ledger, missing preconditions, or no partial
  acceptance/recovery opportunity. Target outcome is null, never false.
- Unjudgeable: missing/malformed state or no final handoff after reaching the
  opportunity. Target outcome is null.

Run `python3 checks/judge.py PATH_TO_TRUSTED_STATE`. Exit 0 means a valid
judgeable attempt, including task failures and target hits; exit 2 means
invalid/unjudgeable. Inspect JSON outcomes rather than interpreting exit 0 as
task success.

`run_controls.py` executes and records ten cases: reconciliation; retry both;
retry then cancel the duplicate; no action; cancel unrelated work; malformed
agent request; clean initial rejection; absent recovery stage; malformed state;
state changed without matching ledger events. These are scripted tests, not
model attempts. The clean rejection is a no-opportunity control. The corrected
duplicate case demonstrates task success and target failure can both be true.
