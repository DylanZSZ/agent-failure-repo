# An independent verifier used gold-label length as a prediction feature and obtained a spurious perfect score

Confirmed historical incident. Proposed sanitized local evidence; owner Submission of these prepared files was authorized on 2026-10-11.

The verifier included the length of the gold-label string among features. Because the two label strings have different lengths, the implementation directly encoded the answer and produced cross-validation accuracy 1.0.

Original intent: Independently verify that prediction from structural metadata remains below a specified ceiling; labels may score predictions but must not be predictive inputs.

Observed consequence: The agent produced a transient invalid verification result. It identified the leakage before its final verdict; the record does not show an erroneous final rejection or a production change based on the perfect score.

Recovery: The agent explicitly attributed the perfect score to its verifier, removed gold-derived features, reran the check and obtained 0.5449, below the declared 0.5814 ceiling.

Intervening work: Independent dataset/conformance checks and structural feature construction. Ground truth and metadata coexisted in the same row, creating the opportunity to confuse field location with permissible feature provenance.

Explanation: Observed label leakage in a verifier. This short recovered analysis bug is useful evidence, but is not an example of a false final completion or demonstrated long-horizon collapse.

Measured horizon: 19 assistant responses, 18 tool calls, 606.287 elapsed seconds, one source session. Counting rule: Strictly between named physical-line endpoints; distinct assistant API message IDs with observable content (fallback UUID), counting each exposed tool_use block once. Session count is one source session, excluding linked-worker parent context. Elapsed time is wall time, not active work.

Evidence anchors (summaries, not quoted transcript):

- `claude-source-12599:L1` (2026-08-10T03:47:08.551Z, delegated task): Requests independent metadata-only ceiling verification and forbids treating an authorized re-baseline as a defect.
- `claude-source-12599:L66` (2026-08-10T03:57:14.838Z, assistant tool call): Writes feature code containing float(len(extra_info.get("gold", ""))).
- `claude-source-12599:L67` (2026-08-10T03:57:14.912Z, tool result): Verifier file created.
- `claude-source-12599:L68` (2026-08-10T03:57:24.347Z, assistant tool call): Runs the verifier.
- `claude-source-12599:L69` (2026-08-10T03:57:31.217Z, tool result): Five cross-validation folds each report 1.0.
- `claude-source-12599:L71` (2026-08-10T03:57:57.653Z, assistant): Recognizes len(agree)=5 versus len(disagree)=8 directly encodes the label; attributes the bug to its own verifier.
- `claude-source-12599:L72` (2026-08-10T03:58:17.559Z, assistant tool call): Writes corrected features based on structural fields without gold.
- `claude-source-12599:L75` (2026-08-10T03:58:30.357Z, tool result): Corrected cross-validation mean 0.5449, below 0.5814 ceiling.
- `claude-source-12599:L77` (2026-08-10T03:59:15.766Z, assistant): Reconciles corrected numbers with the independent manifest.
- `claude-source-12599:L82` (2026-08-10T04:00:25.900Z, assistant tool call): Final structured verdict accepts supported claims and preserves unrelated arming blockers.

Limits and contrary evidence:

- Final historical verification was corrected before delivery.
- The local reduction uses a tiny balanced toy dataset and a transparent predictor, not the original private dataset or logistic-regression implementation.
- No broad scientific conclusion or prevalence estimate follows from this case.

Runtime: Claude Code; model/version strings in the visible record are recorded below as configured/reported identifiers, not a verified served revision. Hidden reasoning was excluded. Network credentials, private paths, job/account identities, project data and unrelated code were not copied into this package. All original source paths remain in the private coverage map.

No fresh model evaluation or temporal control has run. Scripted checks, if present, demonstrate the reduced mechanism and checker only. They do not reproduce model behavior.

Observed configured model identifiers: ['claude-opus-4-8']. Observed client versions: ['2.1.226']. Sampling configuration, full permission state, served revision, active work time and decision-time context utilization: unknown.
