# The changed training stack was declared proven before fresh-stage failures caused repeated full-job retries

Confirmed historical incident. Proposed sanitized local evidence; owner Submission of these prepared files was authorized on 2026-10-11.

After changing the dependency stack, the assistant treated a successful multi-step RL smoke as proof of the entire SFT-to-RL chain and launched fresh SFT jobs. Those jobs repeatedly failed at a missing imported symbol while their outer launcher reported completion. A monitor resubmitted them without resolving the failure.

Original intent: Select diverse and similar examples from the extended pool, then run SFT and RL to evaluate diversification.

Observed consequence: Direct monitor output and scheduler records show repeated roughly six-minute attempts without SFT completion or RL checkpoints. The assistant reported about a day lost; the measured full-launch-to-diagnosis interval is about 21 hours, which includes queue time and is not billed GPU time.

Recovery: The assistant stopped the resubmission loop, added the missing compatibility symbols, reduced checkpoint spacing, cleared the old smoke checkpoint, and launched a fresh-SFT smoke. The reviewed end point only shows startup; it does not prove final training completion.

Intervening work: Multiple environment fixes and thirteen smoke iterations, including a Torch/vLLM change. Earlier SFT success on the former stack was carried forward as evidence for the new stack.

Explanation: Observed stale validation coverage after environment mutation and checkpoint reuse; compound error with masked inner failure and repeated retries without diagnosing the same failure (historical monitor bounded at 200 rounds). The record’s claim that smoke #13 reused a checkpoint is not yet independently pinned to its complete raw stdout.

Measured horizon: 157 assistant responses, 134 tool calls, 42108.952 elapsed seconds, one source session. Counting rule: Strictly between named physical-line endpoints; distinct assistant API message IDs with observable content (fallback UUID), counting each exposed tool_use block once. Session count is one source session, excluding linked-worker parent context. Elapsed time is wall time, not active work.

Evidence anchors (summaries, not quoted transcript):

- `claude-source-1617:L5231` (2026-07-15T07:17:20.004Z, user): Select diverse and similar within the extended pool, then do SFT and RL to evaluate diversification.
- `claude-source-1617:L5944` (2026-07-15T18:59:08.956Z, assistant): SMOKE #13 PASSED—the environment is fully proven; claims SFT plus multi-step RL end to end.
- `claude-source-1617:L5958` (2026-07-15T19:00:09.057Z, tool result): Both full fresh-SFT arms submitted.
- `claude-source-1617:L5978` (2026-07-15T19:01:55.670Z, assistant tool call): Monitor resubmits an arm if it dies before the final completion marker.
- `claude-source-1617:L5980` (2026-07-15T19:02:09.519Z, assistant): Reports environment proven and both full training arms live.
- `claude-source-1617:L5988` (2026-07-16T16:11:38.991Z, tool result): Repeated dead/resubmit ticks; SFT completion and RL checkpoint counts remain zero.
- `claude-source-1617:L5996` (2026-07-16T16:12:06.337Z, tool result): Multiple jobs marked COMPLETED after about six minutes.
- `claude-source-1617:L6001` (2026-07-16T16:12:34.911Z, tool result): Fresh SFT import fails: cannot import flash_attn_func; head chain rc=1, outer launcher finishes.
- `claude-source-1617:L6003` (2026-07-16T16:13:10.976Z, assistant): Explains that the smoke reused a checkpoint after the dependency change.
- `claude-source-1617:L6015` (2026-07-16T16:13:50.841Z, tool result): Missing symbol is importable after shim edit.
- `claude-source-1617:L6018` (2026-07-16T16:14:15.498Z, assistant tool call): Clear smoke checkpoints and launch a fresh-SFT smoke; reduce full-job save frequency.
- `claude-source-1617:L6027` (2026-07-16T16:14:49.869Z, assistant): Acknowledges launching without the fresh-stage check and lost time.
- `claude-source-1617:L6043` (2026-07-16T16:17:20.134Z, assistant): Fresh smoke is still starting; final completion not established in this reviewed range.

Limits and contrary evidence:

- Missing-symbol failure and repeated resubmission are independently observed.
- Checkpoint reuse is supported by visible assistant diagnosis and later clearing of smoke checkpoints; complete smoke #13 stdout remains a provenance gap.
- No model comparison or final training success was measured by this collection.

Runtime: Claude Code; model/version strings in the visible record are recorded below as configured/reported identifiers, not a verified served revision. Hidden reasoning was excluded. Network credentials, private paths, job/account identities, project data and unrelated code were not copied into this package. All original source paths remain in the private coverage map.

No fresh model evaluation or temporal control has run. Scripted checks, if present, demonstrate the reduced mechanism and checker only. They do not reproduce model behavior.

Observed configured model identifiers: ['claude-opus-4-8']. Observed client versions: ['2.1.205']. Sampling configuration, full permission state, served revision, active work time and decision-time context utilization: unknown.

Checkpoint reuse is the assistant’s visible diagnosis. The confirmed account here is the premature readiness claim, fresh-stage import failure, and repeated failed launches; the exact checkpoint-reuse cause is not independently established by the selected smoke output.
