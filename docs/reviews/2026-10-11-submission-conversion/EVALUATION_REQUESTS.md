# Evidence and evaluations to request from contributors

Updated 2026-10-11.

## Summary

Please provide the records below for cases selected for conversion. If a record was never captured or cannot be shared, say so and narrow the claim. A documented incident is still useful without a fresh model reproduction. Do not upload raw private histories or run real destructive operations to fill a gap.

The [complete case assessments](CASE_DETAILS.md) contain specific requests for all 84 entries. The original collections are preserved; these are review requests, not assertions that missing results already exist. No contributor has been contacted automatically.

## Establish the original failure

Provide sanitized excerpts showing the applicable request or rule, an earlier correct state or discovered fact, the later action, its observed effect, and recovery or contradictory evidence. Include exact commands or diffs when they determine what happened. Distinguish an issued action from a suggestion, a queued job from a completed run, and a faulty configuration from a measured bad result.

For duration, identify both endpoints and the counting rule: visible assistant messages, tool calls, session or compaction boundaries, elapsed wall time, and intervening work. Do not count recovery after the error as pre-error context. Do not infer time from JSONL line numbers.

| Priority | Case | Critical missing observation |
| --- | --- | --- |
| High | Checkpoint pruning | Cleanup authorization, before/after inventories, merge completion, and proof no recoverable weights remained. |
| High | Allocator setting reintroduced | Scope of the earlier removal instruction and evidence separating the flag from other converter changes. |
| High | Unscoped training glob | Original launcher/request sequence, row order and budget, and saved input identities of affected jobs if available. |
| High | Test data used as validation | Applicable split contract and prepared configuration; keep clear that no tuning sweep actually ran. |
| High | Partial submission retry | Per-job accept events, aggregate error, retries, run/output identifiers, and cancellation chronology. |
| Medium | Ten-step training fallback | Requested production step count, effective launch configuration and actual emitted steps. |
| Medium | Short shell-assignment bug | Exact function, shell version/options, inherited variables and returned error. |

Source: [case-by-case evidence gaps](CASE_DETAILS.md). These priorities concern evidence collection, not measured severity rankings.

## Supply existing evaluation results

If you evaluated an agent on a packaged task, include every actual attempt: successes, target hits, other task failures, invalid runs and development trials. If you only checked handwritten correct/faulty answers, label those records `scripted_check`. If no fresh model ran, report **not run**.

Each fresh attempt should include model and agent versions when exposed, decoding settings, seed if meaningful, context and step budgets, task and judge revisions, stage delivery, available files, tool actions/results, final state and report. Record preconditions, whether the failure opportunity occurred, task success, target failure and any exclusion reason separately. Report the denominator before and after exclusions.

Keep evaluation prompts natural. Give only the current stage's files and instructions to the agent; keep future stages, references, source failures and judging state private to the evaluator. A final prompt that tells the agent the historical repair measures a different task.

## Validate the judge before measuring a model

Use at least a correct implementation, a known faulty implementation, a task failure that is not the target, an unreached opportunity, malformed data and a valid alternative solution. Preserve earlier hit events even if the final state recovers, and report final unresolved failure separately where appropriate. Check actual actions or outputs rather than accepting self-reported flags as evidence.

An empty answer must not become evidence of a deletion, launch, misreport or ignored rule. Protected-state tampering should invalidate the attempt when it destroys the measurement. An ordinary agent-caused product failure should remain judgeable when it is the intended observation.

## Test whether history matters

After the behavioral task works, compare the full staged sequence with a matched fresh-context, explicit-reminder or short-sequence condition. Keep the final request, repository state, available tools, model settings and scoring rules comparable; document every intentional difference. Record actual intervening work and stage eligibility.

Report uncertainty and alternative explanations. A long observed episode, a scripted failing example, and a fresh-model target hit are three different evidence levels. None alone establishes that longer history caused the failure.
