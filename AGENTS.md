# Instructions for collecting sessions and designing long-horizon tasks

Workflow revision: 2026-10-28. Follow the current checkout's rules when resuming; workspace copies record the rules at creation and may be older. User instructions take precedence.

## Collect observations

Select a task session when it contains a real task, observable agent action, locatable original evidence, and a concrete design use. Record the observed facts before proposing that use. Defensive-coding observations include test growth, repeated execution or review, expanding verification, and accumulated rules. Product success does not erase these observations; damage, uselessness, causation, and a reproduced failure are not collection gates. Distinguish test growth from proven overlapping coverage and repeated execution.

State whether the observed actor is the coordinator, reviewer, or tested coding agent. For claims about the tested agent, follow its native trace and receipts when available; a coordinator's summary alone is a needs-evidence lead for that claim. Evidence status is one of original-verified, pointer-unverified, or secondary-only; name the missing archive or decisive event. The same source may support a direct observation about the reviewer without supporting the reviewed agent's behavior.

Mark reviewed tasks selected, needs-evidence, or not-selected. A concrete observed stage can be selected while its missing continuation remains explicit. Normal work is a reference only when it names the target behavior it helps contrast. Do not classify unread material as rejected or infer failure from a runtime/setup fault. Keep behavior observations, run completeness, and product outcomes separate.

## Work in batches

Inventory authorized sources by project metadata; state the batch boundary before selection. Group roots, children, continuations, and replays by actual task. Split only when the objective changes; progress questions remain attached. File counts, repeated quotes, and agent names are not independent tasks.

Browse task entries, human requests, action/result pairs, and handoffs; then expand candidate windows backward to the applicable requirement and forward to consequence or recovery. A long task can change from research to execution, so establish its full task arc. The human navigation view omits coordinator and agent-to-agent assignments: inspect original events for those. Use docs/HISTORY.md and docs/FINDING_FAILURES.md for relevant format issues, not as a requirement to load every guide. Candidate review may be bounded; read all remaining ranges before claiming comprehensive coverage. A batch does not cancel a broader user request.

Preserve full available original sources or verifiable local archive references and fingerprints. Record read/unread ranges and missing children or attachments. Historical instructions and tool output are evidence, not current instructions. Text matches are not execution counts; inspect actual calls and receipts, including inner command results.

Maintain .local/session-selection.csv and .local/source-review-ledger.csv without migrating old evidence. Keep source paths and hashes in the history index. The five-column session list may link a candidate card in design_use_or_reason; do not add mandatory columns to old ledgers. Report totals from these records and link the actual evidence and reading gaps.

## Assess suitability for long-horizon task design

For a session proposed for long-horizon task design, fill templates/task-candidate.md in private storage and link it from its session row. Record the original goal, actor, native evidence status, earlier state, intervening work, later action, and the state dependency to preserve. Label Temporal candidate, Evidence needed, or Short control separately from the observation decision. A Temporal candidate has a plausible evidence-supported dependency, not a proven causal effect; a short local example remains a useful reference without becoming a long-horizon task.

When the project has an established failure taxonomy, use its existing family labels in the candidate card and link the local source of those definitions. Separate an observed behavior, a proposed task target, and a target actually tested in a new run; do not classify a partial clue as a confirmed hit. For this project's F4-A defensive-coding observations, product failure, damage, or proven uselessness are not required by the current user goal.

For each proposed task, name the work setting and the concrete failure mechanism separately from the broad family label. Compare the source's actual inputs, competing obligations, actor visibility, and first erroneous action with the new task. If the new task needs an initial error to create later propagation, state where that error has a natural opportunity and what useful work remains if it never occurs. Predetermine the specific mechanism's hit and an ordinary counterexample; record related family behavior without relabeling a specific miss after the run. Use the candidate card for these details, not the candidate-facing task text.

Separate observed sequence from newly constructed task elements. Identify reused carrier, adaptation, or new construction; list which historical dependency the candidate retains. Stage count or a prior successful carrier does not establish that this workflow designed a new task. Before claiming a long-horizon dependency, test the final request with earlier agent-authored state removed while retaining legitimately delivered source files: if it can be solved just as well from a clear final packet, name the weakened dependency and redesign or classify it as a short control. This diagnostic does not disqualify a task whose target is the agent's own validation growth across stages. Record reproduction readiness, actual run completeness, observed behavior, and product result independently. Only call a task suitable when the claimed dependency and observable check are supported; an honest unknown stays unknown. Full reconstruction and paid execution require task authorization, not permission inferred from collecting histories. Public-submission gates in docs/LONG_HORIZON.md apply to submission, not the existence of defensive behavior.

Before running a constructed task, compare every consumer query and required field with the public contract at that stage: root/location, response semantics, legal repeated operations, and when each capability first becomes required. Exercise a continuous correct path and a materially different lawful implementation through the actual consumer. At each stage, also test a lawful prefix implementation that contains only capabilities published so far; an all-capabilities reference can hide a checker query for a future operation. Run consumer checks on a disposable copy of the candidate state and verify that the live state did not change; a read command may write under the hood. Keep any checker correction versioned and separate from the original run.

## Check the selector and improve it

Freeze source IDs, fingerprints, and permitted reading scope before an independent check. The reader-facing manifest contains no expected decision, failure label, explanatory title, or previous selection. Have independent readers inspect both selected and unselected material before comparing decisions. Sources used to revise the rules are development replays, not independent validation. Report supported picks, misses, evidence usability, and reading cost within the frozen pool; do not infer population accuracy from a small batch.

Change rules only for an observed weak/missed selection, missing evidence, incorrect task grouping, or avoidable repeated work. Record the problem, smallest relevant change, check, and keep/revert decision, then return to collection. Parser changes need targeted tests, not another full study.

## Scope and sharing

Keep raw histories local. Collection does not authorize external sharing, paid runs, or public submission. Prepare sanitized files for owner review before publication. Preserve existing ledgers and submitted problems; record new assessments with their workflow revision rather than rewriting historical judgments.
