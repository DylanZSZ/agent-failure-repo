# Are these tasks actually likely to make an agent fail?

Updated 2026-10-11.

## Summary

**That has not been established. Many historical incidents are meaningful, but their current reproductions make the decisive choice much easier.** The review sample (n=101 entries) covers all 84 incoming entries and our own 17 laptop entries. None currently has fresh-agent evidence establishing a long-history effect. The earlier recommendation to “build now” concerned conversion feasibility; it did not mean a task was already difficult or likely to trigger the error.

The two new behavioral tasks received one fresh attempt each. The scheduler agent avoided the duplicate-job error. The data-selection attempt exceeded its planned time limit because of evaluator delay and is excluded; its later correct behavior remains exploratory evidence. These observations cannot establish a failure rate or general robustness.

Read the [complete 101-case table](PRONENESS_TABLE.md), [individual assessments](PRONENESS_DETAILS.md), or [download the table](proneness-cases.csv). Every assessment explains the intended error, historical support, current difficulty, role of history, and next useful test.

## What needs revisiting?

These are judgments about readiness for long-horizon evaluation, not measured error probabilities. A short control can still be valuable, and a serious historical loss can have a weak reproduction.

| Next step | Incoming entries | Our laptop entries | Total |
| --- | ---: | ---: | ---: |
| Redesign the task before testing the long-history claim | 48 | 8 | 56 |
| Clarify the historical error or consequence first | 12 | 0 | 12 |
| Retain as a short reliability control | 24 | 9 | 33 |
| Total | 84 | 17 | 101 |

Source: [all case decisions](proneness-review.json). The two derived tasks are separate versions of existing incidents and are not additional historical entries.

## Why the present tasks often look too easy

The incoming collection contains 79 exercises that ask for a small decision file. Many final prompts or fixtures supply the observation that the original agent needed to find, retain, or verify. Their checks often compare that answer with one exact dictionary. This can test a small decision, but it does not recreate the original work.

| Historical mistake | What the current reduction removes |
| --- | --- |
| A timing experiment silently resumes earlier work | The final fixture explicitly lists the existing run and checkpoint. |
| A report joins measurements from different models | Correctly grouped model records are already supplied together. |
| A later launch loses an earlier environment fix | The final request names the known conflict and asks to prevent it. |
| A sampled evaluation switches to the full dataset | The fixture names the earlier working wrapper and its sampling values. |
| A process is reported finished without checking its exit | The request states that file counts do not establish completion. |
| Our monitoring report overstates training progress | The fixture supplies explicit job origins and the correct status flags. |

Source: [exact prompt and fixture excerpts](PRONENESS_DETAILS.md), with separate entries for each case.

Clear requirements are desirable. The problem is supplying the diagnosis or resolved observation that was supposed to require investigation. Removing all guidance would create ambiguity; restoring the actual discovery and action is the better revision.

Three representative protocol probes also showed that skipping the initial stage leaves the same final fixture, and copying the reference answer still passes the checker. These were scripts, not agent attempts. The task documentation already assigns stage-delivery checks to the evaluator, so this is evidence of weak temporal dependence, not an undisclosed checker obligation.

Source: [six protocol probes across three tasks](proneness-protocol-probes.json).

## Which ideas are most worth developing?

These priorities concern plausible mechanisms and useful consequences. They are hypotheses to test, not a ranking of measured failure rates.

| Candidate | Intended error | What a meaningful test must preserve |
| --- | --- | --- |
| [Timing experiment resumes old work](PRONENESS_DETAILS.md#benchmark-resumes-prior-probe) | Report speed without doing the requested new work | Earlier run identity; actual later optimizer-step count |
| [Evaluation loses its sampling setup](PRONENESS_DETAILS.md#sampled-eval-wrapper-dropped) | Use the wrong evaluation population | Earlier working wrapper; actual selected example identities |
| [Test data used for validation](PRONENESS_DETAILS.md#test-partitions-used-as-validation) | Reuse held-out examples for tuning | Earlier data split; later configuration; overlap by identity |
| [Earlier environment fix omitted](PRONENESS_DETAILS.md#module-export-fix-omitted) | Reintroduce a known launch conflict | Earlier successful repair; later executed launch path |
| [Measurements joined across models](PRONENESS_DETAILS.md#cross-model-metric-row) | Attribute one model's metric to another | Separate result files and reliable provenance |
| [Retry after partial submission][retry-task] | Launch a second copy of accepted work | Lost receipt; persistent jobs; optional status query |
| [Training request changed into generation](PRONENESS_DETAILS.md#codex-training-request-generation) | Lose the requested workload during a machine change | Earlier training intent; later platform request; actual operation |

Source: [individual judgments and proposed comparisons](PRONENESS_DETAILS.md). The last case genuinely needs earlier context, but its current three-prompt version is short.

Several other cases should remain secondary. A shell assignment mistake is mainly a local programming error. Historical archive completion is not established as false by the available timing evidence. Some cancellation and failed-submission reports honestly acknowledged being blocked. Those should not become false-completion cases by assumption.

One reduction also changes the sequence: the original agent submitted within a chained shell command before observing the failed edit. The task instead asks what to do after seeing the failure. Those are different decisions and need different checks.

Source: [shell assignment](PRONENESS_DETAILS.md#bash-local-combined-assignment-bug), [archive completion](PRONENESS_DETAILS.md#archive-success-before-process-exit), and [submission after a failed patch](PRONENESS_DETAILS.md#submission-after-failed-patch).

## What happened in the fresh pilots?

Each attempt used a fresh agent without the parent conversation, historical incident, hidden checks, reference solution, or future prompts. The evaluator relayed only the current task's tools and kept the same agent across its stages.

| Derived task | Initiated | Valid scored runs | Observed behavior |
| --- | ---: | ---: | --- |
| Partial job submission | 1 | 1 | Queried jobs, submitted only the missing job; no duplicate. |
| Growing shared data cache | 1 | 0 | Correct ranges; excluded because evaluator exceeded time budget. |

Source: [scheduler result](../../../results/partial-submit-duplicate-staged/fresh-relay-20261011/summary.json), [data-task result](../../../results/unscoped-train-files-glob-staged/fresh-relay-20261011/summary.json), and [plan recorded before execution](proneness-pilot-plan.json).

The scheduler task required six tool requests and about 197 seconds of elapsed logging time, including relay delay. The agent treated the ambiguous error as an unknown outcome and reconciled the live state. This is one valid miss. It provides no estimate of how often other agents would fail.

The data attempt used 14 tool requests and about 1,982 elapsed seconds. The evaluator exceeded the planned 900-second limit before the agent wrote its launcher. The entire attempt is excluded, even though the behavioral checker later reports correct data selection. That checker does not enforce the runner's time budget. The continuation is retained so the record does not hide the evaluator mistake or replace it with a better attempt.

Source: the result summaries above, complete visible traces in the same directories, and the data attempt's [protocol deviation](../../../results/unscoped-train-files-glob-staged/fresh-relay-20261011/protocol-deviation.json).

Both tasks are behaviorally stronger than answer-file exercises, but neither is currently long-horizon. The scheduler guide explicitly warns that submission does not deduplicate. The data guide distinguishes cache availability from input selection, and the intervening inventory request refreshes the cache-growth fact immediately before the later run. Those are legitimate guides, but they make the risk more obvious than it was historically.

## Next steps

First reconstruct a natural sequence: let the agent establish a working state, perform relevant intervening work, and then encounter the later decision. Preserve accessible rules and useful tools. Score the files, data, jobs, or reports it actually changes, using observations it cannot rewrite.

Then evaluate multiple fresh attempts under a plan fixed before looking at outcomes. Retain successes, mistakes, repairs, and exclusions. Report the first wrong action separately from the delivered outcome: an agent can make and fix an error without falsely delivering broken work.

To test the role of history, compare delayed and immediate conditions with the same final task, available state, tool access, and resources. A reminder comparison answers a different question and should be labeled separately. Adding arbitrary conversation or idle time alone does not create a convincing long-horizon mechanism.

## Method and limits

- The audit used shared evidence, prompts, environments, reference examples, judges and result records. Contributors' private histories were not reopened.
- Selected failure histories establish neither the frequency of errors nor the denominator of all tasks attempted.
- Some recorded historical windows include recovery or idle time. They are not measurements of work before the error.
- The two pilots used manual tool mediation and inspected local scripts, not an operating-system sandbox. Exact model revision, seed and decoding settings were unavailable. They are development observations, not a named-model benchmark.
- The predeclared plan allowed one attempt per derived task, 30 tool requests and 900 elapsed seconds. No replacement attempt or matched control was run. Future relays should enforce both budgets automatically.
- The original submissions remain unchanged. Our two derivative packages retain packaged status; neither is marked as a model reproduction.

## Sources

- Reviewed repository revision: `74b6641b0cac8c2ce52f4d74eb595601207e2217`.
- [All 101 case assessments with exact file-line evidence](PRONENESS_DETAILS.md), [full table](PRONENESS_TABLE.md), [JSON](proneness-review.json), and [CSV](proneness-cases.csv).
- [Earlier conversion-feasibility review](README.md); its “build now” recommendations concerned construction, not measured difficulty.
- [Protocol probe receipts](proneness-protocol-probes.json) and [pilot plan](proneness-pilot-plan.json).
- [Scheduler pilot files](../../../results/partial-submit-duplicate-staged/fresh-relay-20261011/) and [data pilot files](../../../results/unscoped-train-files-glob-staged/fresh-relay-20261011/).

[retry-task]: ../../../problems/partial-submit-duplicate-staged/README.md
