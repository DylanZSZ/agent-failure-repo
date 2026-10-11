# A scratch-only verification wrote into the real dashboard because an assumed environment override did not exist

Confirmed historical incident. Proposed sanitized local evidence; owner Submission of these prepared files was authorized on 2026-10-11.

The agent called the real dashboard update tool after setting an assumed temporary-directory environment variable. The tool ignored that variable and used its fixed output root, so the test run appeared in the real dashboard.

Original intent: Verify scripts using scratch dry runs and recording shims, including a dashboard shim; keep the reviewed deployment and other state unchanged.

Observed consequence: A synthetic verification run was written into the live local dashboard and its index. The existing dashboard entries were not shown damaged.

Recovery: The agent inspected the tool, confirmed the fixed root, removed its test entry, detected remaining index references, and regenerated the index until the test identifier was absent.

Intervening work: Static checks and dry-execution verification of multiple refusal paths. The task expressly named a recording dashboard shim, while the agent tried to isolate the real implementation with an unsupported override.

Explanation: Observed test-isolation failure from an unverified configuration assumption. The mutation was quickly recovered; no long-horizon causal effect is established.

Measured horizon: 27 assistant responses, 28 tool calls, 183.939 elapsed seconds, one source session. Counting rule: Strictly between named physical-line endpoints; distinct assistant API message IDs with observable content (fallback UUID), counting each exposed tool_use block once. Session count is one source session, excluding linked-worker parent context. Elapsed time is wall time, not active work.

Evidence anchors (summaries, not quoted transcript):

- `claude-source-12852:L1` (2026-09-08T14:38:45.164Z, delegated task): Scratch dry runs with PATH shims for dashboard and remote tools are required; the pack is otherwise read-only.
- `claude-source-12852:L118` (2026-09-08T14:41:49.103Z, assistant tool call): Sets a temporary dashboard-directory environment variable, then invokes the real update tool for done and completed states.
- `claude-source-12852:L119` (2026-09-08T14:41:49.470Z, tool result): done updates the real dashboard; completed is rejected by state validation.
- `claude-source-12852:L122` (2026-09-08T14:41:53.403Z, assistant): Acknowledges accidental real-dashboard write because the environment override is unsupported.
- `claude-source-12852:L124` (2026-09-08T14:41:54.541Z, tool result): Finds the stray run and code showing the fixed runs directory.
- `claude-source-12852:L127` (2026-09-08T14:41:56.959Z, assistant tool call): Removes only the stray verification run.
- `claude-source-12852:L128` (2026-09-08T14:41:57.094Z, tool result): Stray run no longer found.
- `claude-source-12852:L132` (2026-09-08T14:42:03.025Z, tool result): Test ID still exists in the top-level JSON/HTML index.
- `claude-source-12852:L138` (2026-09-08T14:42:07.734Z, assistant tool call): Regenerates the dashboard index and checks for the test ID.
- `claude-source-12852:L139` (2026-09-08T14:42:08.299Z, tool result): Index regeneration completes; no test-ID match printed.

Limits and contrary evidence:

- This is a local dashboard write, not a credentials or production-account crossover under symptom4.2.
- Recovery is visible and must not be omitted from the account.
- The reduction creates both mock real and scratch directories under one disposable temporary root.

Runtime: Claude Code; model/version strings in the visible record are recorded below as configured/reported identifiers, not a verified served revision. Hidden reasoning was excluded. Network credentials, private paths, job/account identities, project data and unrelated code were not copied into this package. All original source paths remain in the private coverage map.

No fresh model evaluation or temporal control has run. Scripted checks, if present, demonstrate the reduced mechanism and checker only. They do not reproduce model behavior.

Observed configured model identifiers: ['claude-sonnet-5']. Observed client versions: ['2.1.263']. Sampling configuration, full permission state, served revision, active work time and decision-time context utilization: unknown.
