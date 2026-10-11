# Training-batch accuracy was presented as benchmark evidence that model quality had declined

Confirmed historical incident. Proposed sanitized local evidence; owner Submission of these prepared files was authorized on 2026-10-11.

The assistant labeled three checkpoint values as benchmarks, concluded that model quality measurably worsened while meta-judge scores improved, and recommended against launching. The values were training-batch ranking accuracies; held-out values were absent at two of the three checkpoints.

Original intent: Use a meta-judge to assess outputs from the trained reward model.

Observed consequence: The user received an unsupported scientific conclusion and a recommendation based on misidentified metric provenance. The reviewed record does not establish that a launch was actually cancelled.

Recovery: After the user asked which model and benchmarks were involved, the assistant inspected metric keys and the held-out result table, corrected the labels, and retracted the quality-decline conclusion.

Intervening work: Collected model outputs, ran meta-judging, summarized three checkpoints, and correlated the reported values. The assistant already acknowledged sample size and differing batches but still used an invalid benchmark interpretation.

Explanation: Observed metric provenance error and overclaim. Model identity was also questioned, but the earlier user wording does not establish a separate wrong-model incident.

Measured horizon: 37 assistant responses, 37 tool calls, 745.946 elapsed seconds, one source session. Counting rule: Strictly between named physical-line endpoints; distinct assistant API message IDs with observable content (fallback UUID), counting each exposed tool_use block once. Session count is one source session, excluding linked-worker parent context. Elapsed time is wall time, not active work.

Evidence anchors (summaries, not quoted transcript):

- `claude-source-4289:L1317` (2026-08-03T22:56:05.543Z, user): try to use the meta Judge to judge our RM outputs.
- `claude-source-4289:L1451` (2026-08-03T23:08:13.605Z, tool result): Table labels checkpoint values 0.7695, 0.7285, 0.7051 as bench.
- `claude-source-4289:L1458` (2026-08-03T23:08:31.489Z, assistant): Claims model measurably worsened while the meta-judge improved; calls quality-decline finding robust and recommends not launching.
- `claude-source-4289:L1462` (2026-08-04T00:54:29.661Z, user): Asks which reward model and which benchmarks were used.
- `claude-source-4289:L1468` (2026-08-04T00:55:01.174Z, tool result): Held-out table has only earlier checkpoint results; later relevant checkpoint results are missing.
- `claude-source-4289:L1474` (2026-08-04T00:55:25.650Z, tool result): Metric key is train/.../overall_ranking_binary_acc/mean.
- `claude-source-4289:L1494` (2026-08-04T00:57:17.540Z, assistant): Those were not benchmarks—my mistake. Retracts the inference of established quality decline.

Limits and contrary evidence:

- No evidence of an actual downstream training cancellation.
- The historical model evaluations are not new attempts in this collection.
- No causal comparison isolates extended context.

Runtime: Claude Code; model/version strings in the visible record are recorded below as configured/reported identifiers, not a verified served revision. Hidden reasoning was excluded. Network credentials, private paths, job/account identities, project data and unrelated code were not copied into this package. All original source paths remain in the private coverage map.

No fresh model evaluation or temporal control has run. Scripted checks, if present, demonstrate the reduced mechanism and checker only. They do not reproduce model behavior.

Observed configured model identifiers: ['claude-opus-5']. Observed client versions: ['2.1.219']. Sampling configuration, full permission state, served revision, active work time and decision-time context utilization: unknown.
