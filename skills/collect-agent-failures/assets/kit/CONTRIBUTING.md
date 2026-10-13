# Search broadly and submit supported, reproducible failures

Updated 2026-10-13.

## Summary

Ask your agent to search the full history you authorize, then submit only failures with clear evidence that extended work, a context transition, or actual multi-agent interaction contributed. Use [all 20 symptoms](docs/SYMPTOMS.md) as search directions, including other modes where relevant. There is no quota, and zero qualifying cases is a valid result. Keep the complete lead inventory private.

Apply the [four submission gates](docs/LONG_HORIZON.md#four-gates-for-new-submissions): an actual violation, a sourced contribution from the target mechanism, an auditable evidence chain, and a clean runnable reconstruction verified with checker controls. A long transcript or the presence of subagents does not satisfy those gates. Brief coordination failures can qualify without supporting a claim about duration.

Start with **historical Claude Code and Codex runs** for your selected project.
The collecting agent checks both tools' transcript stores and reports coverage
separately. The current conversation adds context. See [how histories are found
and read](docs/HISTORY.md).

## Choose how far to take your contribution

| Contribution | What it contains | What it supports |
|---|---|---|
| Local incident draft | Available evidence and specific missing evidence or reconstruction work | A lead to investigate; not a new public submission |
| Packaged reproduction | All four gates passed, including a faithful environment and recorded checker controls | Others can attempt the task; a fresh model failure is not yet established |
| Model reproduced | Fresh model attempts with complete run records | The intended failure occurred again in the reduced task |
| Temporal evidence supported | Matched attempts that vary the relevant history | Evidence that the earlier work or boundary affects the failure |

New submissions start at packaged reproduction. Fresh model attempts and controlled causal comparisons are not required for that level; report them as not run when absent. A single fresh failure does not establish a general failure rate or cause, and a scripted replay cannot satisfy the model reproduction level. The existing `incident` status remains available for local drafts and legacy records; preserve existing submissions and add dated reviews when interpretations change.

## Give your agent a clear scope

Point your agent to [AGENTS.md](AGENTS.md) and name the histories it may inspect. For example:

> Read this repository's AGENTS.md, docs/LONG_HORIZON.md, and docs/SYMPTOMS.md. You may inspect the selected exports and project copies. Search the full authorized history for failures to which extended work, context transitions, or actual multi-agent interaction contributed. Reconstruct the applicable instruction, earlier state, intervening work or interaction, actor visibility, executed action, consequence, and recovery with source anchors. Keep every lead in a private inventory, but prepare public packages only for cases passing all four submission gates. Build and verify faithful runnable reconstructions without supplying the diagnosis or removing the dependency. Keep all actual attempts, including misses. Mark missing evidence or reconstruction work as local drafts; ordinary local bugs are out of scope. Zero qualifying submissions is acceptable. Show the exact sanitized contribution before uploading anything.

If the agent cannot access your old conversations, give it a selected export or describe an incident. Do not give it broad access to your accounts simply to fill in missing details.

## Prepare the contribution

1. Copy the [collection report](templates/collection-report.md) and [incident index](templates/incident-index.csv) into private working storage. Inventory the authorized sources, then follow [the multi-pass search guide](docs/FINDING_FAILURES.md).
2. Add every candidate to the index with evidence, symptom labels or an unmatched mode, and its disposition. Deduplicate the same event appearing in multiple records; keep different incidents within the same symptom class.
3. Apply the first three evidence gates. Keep missing-evidence leads and ordinary local errors in the private inventory with their disposition. Once those gates pass, use `python3 commands/new_problem.py <slug>` in the private collection workspace to begin the reconstruction needed for gate 4.
4. Follow [the reproduction guide](docs/REPRODUCING.md). Run clean setup and checker controls, preserving the relevant historical dependency and information available to each actor. If the reconstruction cannot be completed, keep the case local as needs reconstruction with an exact next action.
5. Put sanitized run summaries and evidence under `results/<slug>/<run-id>/`. Include every actual attempt for each selected case, even when the model avoids the failure or the setup breaks. Do not create model run records when no model evaluation occurred.
6. Reconcile the private inventory and coverage with the selected cases. Run `python3 commands/validate.py` and perform the [owner review](docs/REVIEW.md). Validation checks structure; it does not establish scientific admission or reproducibility.
7. Prepare the selected, shareable file set in [what to push](docs/SUBMITTING.md), including a sanitized selected index and summary. Explain the findings, checks, gaps, and reasons for selection in the console. Once the owner has reviewed and authorized those files, push a contribution branch (in a fork if needed) and open a pull request against this repository's `main`. Otherwise deliver the local package for review. Clearly distinguish selected submissions from the complete private search inventory.

## Keep the parts separate

| Location | What belongs there |
|---|---|
| `docs/` | Shared instructions and methodology; reviewed collection summaries in `docs/collections/<collection-id>/` |
| `problems/<slug>/` | One incident and its reproducible task package |
| `results/<slug>/<run-id>/` | Sanitized evidence from one attempt |
| `commands/` | Shared repository tools |
| `templates/` | Starter files copied for a contribution |
| `examples/` | Explicitly labeled teaching examples |
| `.local/` | Ignored, private working material that must not be committed |

Keep hidden checks and reference solutions out of the tested agent's workspace. Expose only the current stage's intended messages and files; keep future prompts and the orchestration schedule outside that workspace. Preserve each original run record when adding a later evaluation; explain any changed interpretation rather than replacing the old evidence.

## Before you share

Only share material you are entitled to contribute. Remove secrets, private code, personal details, and other people's messages that you do not have permission to share. Describe any sanitization that changes the task. Review the actual files and staged changes; an ignored directory or a secret scanner is not a guarantee that a package is safe to publish.

Source: [Agent instructions](AGENTS.md), [reproduction requirements](docs/REPRODUCING.md), and [review checklist](docs/REVIEW.md).
