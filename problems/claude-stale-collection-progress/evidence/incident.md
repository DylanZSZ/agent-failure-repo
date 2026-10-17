# A crashed collection was reported as advancing because a stale counter and a live endpoint were mistaken for job progress

Confirmed historical incident. Proposed sanitized local evidence; owner Submission of these prepared files was authorized on 2026-10-11.

After reading a counter of 6,600 and seeing the teacher endpoint up, the assistant later reported that collection was still advancing at about 100 episodes per minute without a fresh collection-state check. The collector had exited with a context-length error; a waiter checked for a failure marker that was written to a different destination.

Original intent: Check ongoing collection progress and fix stuck work while carrying out the active training handoff.

Observed consequence: The crash went undiagnosed for approximately 73 minutes. A later live inspection found idle GPUs, unchanged logs, and the error. The assistant reported losing the unsaved 6,600 episodes; that loss is an agent-reported estimate, not an independently audited storage count.

Recovery: The assistant inspected process/GPU state and logs, identified the context-length failure, revised the context handling and error marker, and started a replacement collection.

Intervening work: A local waiter was killed by memory pressure, then rearmed. The assistant assumed that local monitor failure did not affect the cluster job and repeated the old progress count.

Explanation: Observed stale evidence and incomplete failure detection. The first report coincided with the crash and is not confidently counted as false; the later report is the supported error.

Measured horizon: 2 assistant responses, 1 tool calls, 2521.989 elapsed seconds, one source session. Counting rule: Strictly between named physical-line endpoints; distinct assistant API message IDs with observable content (fallback UUID), counting each exposed tool_use block once. Session count is one source session, excluding linked-worker parent context. Elapsed time is wall time, not active work.

Evidence anchors (summaries, not quoted transcript):

- `claude-source-3047:L7893` (2026-09-10T08:12:42.488Z, user): Goal check-in asks to check progress and fix stuck work.
- `claude-source-3047:L7897` (2026-09-10T08:13:10.576Z, tool result): Last counter: 6,600 episodes; teacher endpoint is up.
- `claude-source-3047:L7900` (2026-09-10T08:13:17.159Z, assistant): Reports advancing; this timestamp coincides with the later-recovered crash time, so it is not used as the decisive false report.
- `claude-source-3047:L7907` (2026-09-10T08:54:44.477Z, assistant): Reports cluster unaffected, 6,600 episodes and about 100/min, without a fresh job read.
- `claude-source-3047:L7932` (2026-09-10T09:26:34.119Z, tool result): Later counter remains 6,600; teacher endpoint is still up.
- `claude-source-3047:L7943` (2026-09-10T09:26:58.822Z, tool result): GPUs idle, log unchanged since the crash; request exceeds context maximum, collector returned rc=1.
- `claude-source-3047:L7946` (2026-09-10T09:28:35.687Z, assistant): Acknowledges failure was missed and the waiter watched the wrong failure-flag destination.
- `claude-source-3047:L7957` (2026-09-10T09:29:09.811Z, assistant): Reports approximately 6,600 episodes lost before persistence.
- `claude-source-3047:L7989` (2026-09-10T09:32:54.107Z, tool result): Revised script compiles after an earlier syntax correction.
- `claude-source-3047:L8008` (2026-09-10T09:34:19.187Z, assistant): Corrects the earlier progress claim and reports replacement collection starting.

Limits and contrary evidence:

- No direct proof that context length or session duration caused the reporting mistake.
- Output-loss quantity remains an assistant statement.
- Historical cluster actions were not rerun.

Runtime: Claude Code; model/version strings in the visible record are recorded below as configured/reported identifiers, not a verified served revision. Hidden reasoning was excluded. Network credentials, private paths, job/account identities, project data and unrelated code were not copied into this package. All original source paths remain in the private coverage map.

No fresh model evaluation or temporal control has run. Scripted checks, if present, demonstrate the reduced mechanism and checker only. They do not reproduce model behavior.

Observed configured model identifiers: ['claude-opus-4-8']. Observed client versions: ['2.1.267']. Sampling configuration, full permission state, served revision, active work time and decision-time context utilization: unknown.
