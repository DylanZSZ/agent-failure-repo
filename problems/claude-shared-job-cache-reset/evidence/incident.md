# A resumed worker reset a shared job cache and erased the records it needed to harvest a teammate’s jobs

Confirmed historical incident. Proposed sanitized local evidence; owner Submission of these prepared files was authorized on 2026-10-11.

After receiving explicit fork-job identifiers, the resumed worker restored a tracked shared runtime cache from HEAD during Git synchronization. The cache then lacked the job identifiers; polling required the erased identifier-to-cluster mapping, so a completed evaluation was not harvested.

Original intent: Resume a lane, harvest the replication jobs already submitted by a fork, and confirm the result before broader evaluation.

Observed consequence: Two live job mappings had to be reconstructed before the backend could poll and harvest them. Output files remained intact and harvesting succeeded after repair.

Recovery: The worker reconstructed full job specifications from the goal and lane state, appended them to the cache, verified their presence, and reran harvest successfully.

Intervening work: The worker had paused for about eleven hours; a fork advanced the same lane during that interval. On resume, the coordinator explicitly described the new jobs. Git stash/rebase synchronization was attempted before harvesting.

Explanation: Observed destructive cleanup of shared runtime state at a resume boundary. The explicit handoff named the teammate jobs immediately before the reset, so this also has a short-distance explanation; long-context causation is untested.

Measured horizon: 1 assistant responses, 0 tool calls, 16.306 elapsed seconds, one source session. Counting rule: Strictly between named physical-line endpoints; distinct assistant API message IDs with observable content (fallback UUID), counting each exposed tool_use block once. Session count is one source session, excluding linked-worker parent context. Elapsed time is wall time, not active work.

Evidence anchors (summaries, not quoted transcript):

- `claude-linked-worker-cache:L810` (2026-07-14T19:56:51.373Z, coordinator message): A fork already submitted a replication draw; harvest it and confirm the winner.
- `claude-linked-worker-cache:L812` (2026-07-14T19:57:07.679Z, assistant tool call): git stash/pull/pop followed by git checkout HEAD -- campaigns/slurm_jobs.jsonl.
- `claude-linked-worker-cache:L813` (2026-07-14T19:57:11.248Z, tool result): Lane rows still refer to the two fork job IDs; the completed job exists.
- `claude-linked-worker-cache:L816` (2026-07-14T19:57:32.865Z, assistant tool call): Again restores the shared cache from HEAD before a harvest tick.
- `claude-linked-worker-cache:L817` (2026-07-14T19:58:03.486Z, tool result): Evaluation output exists, but harvested is empty.
- `claude-linked-worker-cache:L821` (2026-07-14T19:58:20.227Z, tool result): The lane row retains the job ID; grep count in the shared cache is 0.
- `claude-linked-worker-cache:L827` (2026-07-14T19:58:54.560Z, tool result): Backend polling requires a cached job-to-cluster mapping; unknown IDs remain unpolled.
- `claude-linked-worker-cache:L839` (2026-07-14T20:00:00.978Z, assistant tool call): Reconstruct and append two full job records.
- `claude-linked-worker-cache:L840` (2026-07-14T20:00:01.086Z, tool result): Both reconstructed IDs have count 1.
- `claude-linked-worker-cache:L843` (2026-07-14T20:00:39.027Z, tool result): Harvest now processes both evaluations.
- `claude-linked-worker-cache:L853` (2026-07-14T20:01:57.561Z, assistant): Reports its own reset erased the fork records and flags shared-writer coordination.

Limits and contrary evidence:

- The direct transcript has no before-reset dump of the complete cache, but the executed reset, missing-ID check, backend read, reconstruction and successful harvest support the state-loss chain.
- No permanent loss of evaluation outputs observed.
- The parent coordinator’s ownership explanation is supporting context, not proof of its internal reasoning.

Runtime: Claude Code; model/version strings in the visible record are recorded below as configured/reported identifiers, not a verified served revision. Hidden reasoning was excluded. Network credentials, private paths, job/account identities, project data and unrelated code were not copied into this package. All original source paths remain in the private coverage map.

No fresh model evaluation or temporal control has run. Scripted checks, if present, demonstrate the reduced mechanism and checker only. They do not reproduce model behavior.

Observed configured model identifiers: ['claude-opus-4-8']. Observed client versions: ['2.1.207']. Sampling configuration, full permission state, served revision, active work time and decision-time context utilization: unknown.

Taxonomy boundary: Related to 3.3 resume-time deletion, but the erased additions are runtime job records, not code or tests; 3.2 committed-work category does not apply.
