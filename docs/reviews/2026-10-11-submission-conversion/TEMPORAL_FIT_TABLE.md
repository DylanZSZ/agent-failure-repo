# Which submitted incidents fit failures from extended work?

Updated 2026-10-11.

## Summary

This table covers every historical entry (n=101): 84 incoming and 17 from our laptop. It separates original incident relevance from the quality of the current reproduction. **The 28 temporal candidates are leads, not 28 demonstrated long-running failures.** The other entries comprise 16 needing evidence and 57 short controls.

Read the [interpretation and priorities](TEMPORAL_FIT.md), [full case records][details], or [download the data](temporal-fit.csv). Each linked record explains the expected action, earlier and later evidence, actual intervening work or its absence, competing explanation, and next step.

## How to read the table

“Recorded interval” reproduces the submitted endpoint measurements; it is not a measurement of uninterrupted work. Some windows include waiting or recovery. The separate work-exposure column assesses the described activity. “Current task” retains the prior audit of the original reduction; it does not assess the two later derived tasks or change historical evidence.

## Temporal candidates: incoming (21)

| Incident and full assessment | Recorded interval | Original work exposure | Current task |
| --- | --- | --- | --- |
| [Later timing probe reuses prior run ID and resumes an already completed probe][case-5] | 23 replies; 72 calls; 2.05 hours | Exposure unknown | Redesign before pilot |
| [A queue switch retains the previous queue-only interpreter][case-6] | Not measured | Short mechanism only | Redesign before pilot |
| [A result row combines metrics from two different models][case-9] | Not measured | Exposure unknown | Redesign before pilot |
| [Known incompatible allocator setting is reintroduced during checkpoint conversion][case-16] | 96 replies; 230 calls; 21.49 hours | Exposure unknown | Evidence before pilot |
| [A documented first-run cache workaround is lost when creating an Aurora launch script][case-20] | Not measured | Short mechanism only | Redesign before pilot |
| [Environment migration retains module export that previously caused startup failure][case-32] | 32 replies; 117 calls; 1.17 hours | Substantial work observed | Redesign before pilot |
| [Unconditional next-eval interpreter change breaks the shared capacity launcher][case-34] | 9 replies; 41 calls; 11.8 minutes | Exposure unknown | Redesign before pilot |
| [Discovered shared cache workaround is omitted from one related launcher][case-35] | 17 replies; 66 calls; 26.6 minutes | Substantial work observed | Evidence before pilot |
| [An explicit one-job evaluation is submitted as separate suite jobs][case-36] | Not measured | Short mechanism only | Redesign before pilot |
| [Partial scheduler submission is retried without reconciliation][case-42] | Not measured | Short mechanism only | Redesign before pilot |
| [PathMMU proxy participation is dropped during configuration review][case-44] | 6 replies; 20 calls; 1.82 hours | Substantial work observed | Redesign before pilot |
| [A generation probe leaves output that blocks the full submission][case-47] | Not measured | Short mechanism only | Redesign before pilot |
| [Proxy restart preserves a partial ReXVQA directory but cannot resume it][case-48] | Not measured | Exposure unknown | Redesign before pilot |
| [Changing resume accumulation while saved microbatch overrides CLI trains zero steps][case-56] | 3 replies; 5 calls; 2.3 minutes | Short mechanism only | Redesign before pilot |
| [Editing a running shell launcher corrupts its trailing command][case-57] | 12 replies; 54 calls; 22.5 minutes | Exposure unknown | Redesign before pilot |
| [Same-settings evaluation drops the operative random-sampling wrapper][case-58] | Not measured | Short mechanism only | Redesign before pilot |
| [Stopped watcher snapshots misreport failed jobs as still queued][case-61] | 3 replies; 3 calls; 6.01 hours | Short mechanism only | Redesign before pilot |
| [A completed job is reported as not yet started from stale watcher state][case-62] | Not measured | Short mechanism only | Redesign before pilot |
| [Strict merge validation is dropped after detecting unequal shared weights][case-64] | 11 replies; 75 calls; 26.1 minutes | Exposure unknown | Redesign before pilot |
| [PathMMU test partitions are configured as validation tuning inputs][case-72] | 29 replies; 139 calls; 3.67 days | Substantial work observed | Redesign before pilot |
| [Unscoped file-selection glob silently ignores a requested sub-range when the directory holds extra files][case-81] | Not measured | Exposure unknown | Short control only |

Source: [per-case review data](temporal-fit.json), including original source references and exposure reasons.

## Temporal candidates: our laptop (7)

| Incident and full assessment | Recorded interval | Original work exposure | Current task |
| --- | --- | --- | --- |
| [Scheduler activity was reported as progress in a blocked run][case-86] | 21 replies; 17 calls; 4.97 hours | Exposure unknown | Redesign before pilot |
| [A crashed collection was reported as advancing because a stale counter and a live endpoint were mistaken for job progress][case-90] | 2 replies; 1 calls; 42.0 minutes | Short mechanism only | Redesign before pilot |
| [A resumed worker reset a shared job cache and erased the records it needed to harvest a teammate’s jobs][case-92] | 1 replies; 0 calls; 16.3 seconds | Short mechanism only | Redesign before pilot |
| [The changed training stack was declared proven before fresh-stage failures caused repeated full-job retries][case-93] | 157 replies; 134 calls; 11.70 hours | Substantial work observed | Redesign before pilot |
| [A strictly read-only storage survey included a remote temporary-file write][case-95] | 12 replies; 19 calls; 11.5 minutes | Short mechanism only | Short control only |
| [An ARM follow-up dispatches generation jobs during a training task][case-98] | 27 replies; 90 calls; 10.7 minutes | Exposure unknown | Short control only |
| [A current status report omits a parallel campaign after an explicit reminder][case-99] | 7 replies; 17 calls; 2.7 minutes | Short mechanism only | Short control only |

Source: [per-case review data](temporal-fit.json), including original source references and exposure reasons.

## Evidence needed: incoming (16)

| Incident and full assessment | Recorded interval | Original work exposure | Current task |
| --- | --- | --- | --- |
| [Archive extraction completion is reported without checking the live process][case-2] | 3 replies; 7 calls; 1.6 minutes | Exposure unknown | Evidence before pilot |
| [Automatic monitoring is dropped despite an available exact session ID][case-4] | 2 replies; 3 calls; 1.0 minutes | Exposure unknown | Evidence before pilot |
| [Resubmission reuses shards whose manifest the changed runner rejects][case-21] | Not measured | Exposure unknown | Evidence before pilot |
| [Restart requests queue maximum rather than estimating remaining training][case-27] | 3 replies; 3 calls; 2.1 minutes | Exposure unknown | Evidence before pilot |
| [Fisher calibration interpretation compares different model precision and record sets][case-29] | Not measured | Exposure unknown | Redesign before pilot |
| [Additional finite-difference GPU work is attempted while the authorized derivative run is active][case-40] | Not measured | Exposure unknown | Evidence before pilot |
| [Collection stops after screening despite required chronological review][case-45] | Not measured | Exposure unknown | Redesign before pilot |
| [Recovered model delivery omits tokenizer and processor runtime files][case-51] | 22 replies; 111 calls; 49.0 minutes | Exposure unknown | Redesign before pilot |
| [Skill default overrides an explicit CPU scoring instruction][case-59] | Not measured | Exposure unknown | Evidence before pilot |
| [Stale watcher state is reported despite complete evaluation artifacts][case-63] | Not measured | Exposure unknown | Redesign before pilot |
| [Synthetic generator loses profile conditioning during simplification][case-69] | Not measured | Exposure unknown | Evidence before pilot |
| [Table formatting omits the two models just reported][case-70] | Not measured | Exposure unknown | Short control only |
| [False one-job limit causes unnecessary dependency holds][case-77] | Not measured | Exposure unknown | Redesign before pilot |
| [Production jobs inherit a ten-step smoke-test default][case-82] | Not measured | Exposure unknown | Evidence before pilot |
| [Checkpoint pruning removes the only recoverable weights][case-83] | Not measured | Exposure unknown | Evidence before pilot |
| [A dependent bash local assignment breaks a verification step][case-84] | Not measured | Exposure unknown | Short control only |

Source: [per-case review data](temporal-fit.json), including original source references and exposure reasons.

## Short controls: incoming (47)

| Incident and full assessment | Recorded interval | Original work exposure | Current task |
| --- | --- | --- | --- |
| [Analysis command selects a parent without checkpoint configuration][case-1] | Not measured | Exposure unknown | Redesign before pilot |
| [Strict unset-variable checking aborts Aurora module initialization][case-3] | Not measured | Exposure unknown | Short control only |
| [Attention backend is selected on wrapper but misses composite text model][case-7] | 5 replies; 13 calls; 2.9 minutes | Exposure unknown | Redesign before pilot |
| [Delivered multi-device merger stacks router rows before staging them][case-8] | Not measured | Exposure unknown | Short control only |
| [Analysis defaults omit dense checkpoint decoder keys][case-10] | Not measured | Exposure unknown | Short control only |
| [Directional Fisher loader uses model parameter keys against differently named stored tensors][case-11] | Not measured | Exposure unknown | Short control only |
| [A submission duplicates the launcher directory in its path][case-12] | Not measured | Exposure unknown | Short control only |
| [Endpoint-logit interpolation is proposed for a control that must preserve initial Fisher][case-13] | Not measured | Exposure unknown | Short control only |
| [EvoGM evaluation wrapper supplies a JSON array to a JSONL reader][case-14] | 24 replies; 62 calls; 1.70 hours | Exposure unknown | Redesign before pilot |
| [Repair writes the same exclusive-create provenance file twice][case-15] | 2 replies; 4 calls; 3.7 minutes | Exposure unknown | Redesign before pilot |
| [Expert Merging++ fitting compares incompatible checkpoint and loaded-model parameter names][case-17] | 18 replies; 46 calls; 1.27 hours | Exposure unknown | Redesign before pilot |
| [FLAT benchmark retains COMPOSITE-only affinity wrapper][case-18] | 5 replies; 22 calls; 4.8 minutes | Exposure unknown | Short control only |
| [One of three capacity jobs keeps the next-eval environment][case-19] | Not measured | Exposure unknown | Redesign before pilot |
| [Failed in-place substitution empties a launcher and still passes validation][case-22] | Not measured | Exposure unknown | Redesign before pilot |
| [The vLLM rendering adapter sends instruction prompts as raw completions][case-23] | Not measured | Exposure unknown | Redesign before pilot |
| [Learning carryover reads an absent knowledge-state attribute][case-24] | Not measured | Exposure unknown | Short control only |
| [Login shell redirects implementation to a neighboring repository][case-25] | Not measured | Exposure unknown | Redesign before pilot |
| [Routing submission uses a malformed sample-count environment variable][case-26] | Not measured | Exposure unknown | Short control only |
| [An answer parser accepts a lowercase ambiguous choice as a valid MC answer][case-28] | Not measured | Exposure unknown | Short control only |
| [Resume submission retains explicit auto-resume false][case-30] | 2 replies; 10 calls; 3.5 minutes | Exposure unknown | Redesign before pilot |
| [Training skip_eval is misreported as no evaluation result][case-31] | Not measured | Exposure unknown | Redesign before pilot |
| [Parent checkpoint path leads to incorrect text-only diagnosis][case-33] | Not measured | Exposure unknown | Short control only |
| [Trainer import initializes compute-only MPI on the login host][case-37] | Not measured | Exposure unknown | Short control only |
| [Submission wrapper receives a nested qsub executable][case-38] | Not measured | Exposure unknown | Short control only |
| [New OPD launcher enables nounset before module initialization][case-39] | Not measured | Exposure unknown | Evidence before pilot |
| [Proxy fan-out uses interpreter handoff that bypasses its evaluation virtualenv][case-41] | Not measured | Exposure unknown | Redesign before pilot |
| [Default evaluation batch omits the required PathMMU suite][case-43] | 3 replies; 4 calls; 1.3 minutes | Exposure unknown | Redesign before pilot |
| [Queued debug allocation is canceled before the requested work runs][case-46] | Not measured | Exposure unknown | Redesign before pilot |
| [A healthy queued GPU verification is canceled before it starts][case-49] | Not measured | Exposure unknown | Redesign before pilot |
| [Normal queue wait ends an announced GPU memory check prematurely][case-50] | 4 replies; 10 calls; 5.0 minutes | Exposure unknown | Redesign before pilot |
| [Submission wrapper receives a nested qsub executable][case-52] | Not measured | Exposure unknown | Short control only |
| [Healthy queued RegMean canary canceled before required GPU verification][case-53] | Not measured | Exposure unknown | Redesign before pilot |
| [Missing local cache shards are reported as absent remote weights][case-54] | Not measured | Exposure unknown | Redesign before pilot |
| [Five successive malformed orchestration programs fail before inspection][case-55] | 0 replies; 3 calls; 15.7 seconds | Exposure unknown | Short control only |
| [Live inference runner starts spawn workers during module import][case-60] | Not measured | Exposure unknown | Short control only |
| [Conversion launcher repeats unset-variable checks before module initialization][case-65] | Not measured | Exposure unknown | Short control only |
| [New probe wrapper enables unset-variable checks before Lmod setup][case-66] | Not measured | Exposure unknown | Short control only |
| [Failed runtime patch is followed by unconditional job submission][case-67] | 0 replies; 1 calls; 3.9 seconds | Exposure unknown | Short control only |
| [Benchmark result columns are swapped in the report][case-68] | Not measured | Exposure unknown | Short control only |
| [Teacher naturalization violates the diagnostic-only classroom invariant][case-71] | Not measured | Exposure unknown | Redesign before pilot |
| [Text-only support omits distributed unused-branch handling][case-73] | Not measured | Exposure unknown | Redesign before pilot |
| [Directory existence check misses nested model checkpoints in three evaluations][case-74] | 3 replies; 9 calls; 1.8 minutes | Exposure unknown | Redesign before pilot |
| [Next-eval wrapper is used for two capacity jobs][case-75] | Not measured | Exposure unknown | Redesign before pilot |
| [Evaluation submission accepts a training parent without model configuration][case-76] | 1 replies; 4 calls; 45.7 seconds | Exposure unknown | Redesign before pilot |
| [A question about existing decoder results launches a new GPU allocation][case-78] | Not measured | Exposure unknown | Redesign before pilot |
| [Mocked delivery tests miss incompatible live Codex CLI arguments][case-79] | 15 replies; 66 calls; 44.7 minutes | Exposure unknown | Redesign before pilot |
| [Login shell changes directory and wrong repository becomes a redirect claim][case-80] | 2 replies; 9 calls; 1.4 minutes | Exposure unknown | Short control only |

Source: [per-case review data](temporal-fit.json), including original source references and exposure reasons.

## Short controls: our laptop (10)

| Incident and full assessment | Recorded interval | Original work exposure | Current task |
| --- | --- | --- | --- |
| [Budget constants changed, but the runtime profile was left stale][case-85] | 26 replies; 25 calls; 19.6 minutes | Exposure unknown | Redesign before pilot |
| [A completion loop keeps waiting after its phase counter resets][case-87] | 11 replies; 9 calls; 19.0 minutes | Exposure unknown | Short control only |
| [A no-op commit skipped the directory change and wrote the ledger into the code repository][case-88] | 3 replies; 3 calls; 1.9 minutes | Exposure unknown | Short control only |
| [A stale output file was treated as proof that a productive worker had stalled][case-89] | 7 replies; 6 calls; 7.3 minutes | Exposure unknown | Redesign before pilot |
| [Training-batch accuracy was presented as benchmark evidence that model quality had declined][case-91] | 37 replies; 37 calls; 12.4 minutes | Exposure unknown | Short control only |
| [A failed file transfer was described as checksum-verified and left the next executor without its input][case-94] | 7 replies; 7 calls; 3.7 minutes | Exposure unknown | Short control only |
| [An independent verifier used gold-label length as a prediction feature and obtained a spurious perfect score][case-96] | 19 replies; 18 calls; 10.1 minutes | Exposure unknown | Redesign before pilot |
| [A scratch-only verification wrote into the real dashboard because an assumed environment override did not exist][case-97] | 27 replies; 28 calls; 3.1 minutes | Exposure unknown | Redesign before pilot |
| [Model-specific thinking allowance is copied onto the actor][case-100] | 7 replies; 14 calls; 2.2 minutes | Exposure unknown | Short control only |
| [Deployment reviewer approves a launcher that rejects its supported deployed layout][case-101] | 14 calls; 2.9 minutes | Exposure unknown | Short control only |

Source: [per-case review data](temporal-fit.json), including original source references and exposure reasons.

## Next steps

Prioritize the five candidates with documented substantial work. Rebuild their missing decisions before model pilots. For the remaining leads, collect the specific evidence requested in each assessment or retain the demonstrated short mechanism without adding artificial length.

Source: [candidate exposure assessments](temporal-fit.json).

## Limitations

This is a qualitative review of shared evidence, not fresh model testing. Private source histories were not reopened. Unknown causal sequences and ambiguous scopes remain explicit. A short observed gap does not rule out a broader history, but the review does not invent one. Original packages and historical result records were preserved.

## Sources

[details]: TEMPORAL_FIT_DETAILS.md

### Case record links 1–34

[case-1]: TEMPORAL_FIT_DETAILS.md#analysis-parent-checkpoint

[case-2]: TEMPORAL_FIT_DETAILS.md#archive-success-before-process-exit

[case-3]: TEMPORAL_FIT_DETAILS.md#aurora-nounset-before-module

[case-4]: TEMPORAL_FIT_DETAILS.md#available-session-id-ignored-for-monitoring

[case-5]: TEMPORAL_FIT_DETAILS.md#benchmark-resumes-prior-probe

[case-6]: TEMPORAL_FIT_DETAILS.md#capacity-switch-retains-next-eval-venv

[case-7]: TEMPORAL_FIT_DETAILS.md#composite-attention-dispatch

[case-8]: TEMPORAL_FIT_DETAILS.md#connector-router-cross-device-stack

[case-9]: TEMPORAL_FIT_DETAILS.md#cross-model-metric-row

[case-10]: TEMPORAL_FIT_DETAILS.md#dense-decoder-group-mismatch

[case-11]: TEMPORAL_FIT_DETAILS.md#directional-checkpoint-key-mismatch

[case-12]: TEMPORAL_FIT_DETAILS.md#duplicated-launcher-path

[case-13]: TEMPORAL_FIT_DETAILS.md#endpoint-logit-control

[case-14]: TEMPORAL_FIT_DETAILS.md#evolutionary-evaluation-jsonl-contract-missed

[case-15]: TEMPORAL_FIT_DETAILS.md#exclusive-provenance-written-twice

[case-16]: TEMPORAL_FIT_DETAILS.md#expandable-allocator-reintroduced

[case-17]: TEMPORAL_FIT_DETAILS.md#fitting-checkpoint-key-conversion-omitted

[case-18]: TEMPORAL_FIT_DETAILS.md#flat-mode-composite-wrapper

[case-19]: TEMPORAL_FIT_DETAILS.md#fp32-capacity-environment

[case-20]: TEMPORAL_FIT_DETAILS.md#fresh-vllm-cache-workaround-omitted

[case-21]: TEMPORAL_FIT_DETAILS.md#incompatible-fisher-resume

[case-22]: TEMPORAL_FIT_DETAILS.md#inplace-launcher-truncation

[case-23]: TEMPORAL_FIT_DETAILS.md#instruction-model-chat-template-omitted

[case-24]: TEMPORAL_FIT_DETAILS.md#learning-carryover-missing-field

[case-25]: TEMPORAL_FIT_DETAILS.md#login-shell-misdirects-implementation

[case-26]: TEMPORAL_FIT_DETAILS.md#malformed-routing-sample-variable

[case-27]: TEMPORAL_FIT_DETAILS.md#maximum-walltime-instead-of-estimate

[case-28]: TEMPORAL_FIT_DETAILS.md#mc-parser-lowercase-ambiguity-accepted

[case-29]: TEMPORAL_FIT_DETAILS.md#mismatched-fisher-kl-protocol

[case-30]: TEMPORAL_FIT_DETAILS.md#missed-resume-flag

[case-31]: TEMPORAL_FIT_DETAILS.md#missed-separate-evaluation

[case-32]: TEMPORAL_FIT_DETAILS.md#module-export-fix-omitted

[case-33]: TEMPORAL_FIT_DETAILS.md#nested-vl-checkpoint

[case-34]: TEMPORAL_FIT_DETAILS.md#next-eval-interpreter-leaks-into-capacity

### Case record links 35–68

[case-35]: TEMPORAL_FIT_DETAILS.md#offline-cache-protection-omitted

[case-36]: TEMPORAL_FIT_DETAILS.md#one-job-evaluation-split

[case-37]: TEMPORAL_FIT_DETAILS.md#opd-import-time-mpi-init

[case-38]: TEMPORAL_FIT_DETAILS.md#opd-nested-qsub-wrapper

[case-39]: TEMPORAL_FIT_DETAILS.md#opd-strict-shell-module-init

[case-40]: TEMPORAL_FIT_DETAILS.md#overlapping-finite-difference-attempt

[case-41]: TEMPORAL_FIT_DETAILS.md#packed-proxy-environment-preflight

[case-42]: TEMPORAL_FIT_DETAILS.md#partial-submit-duplicate

[case-43]: TEMPORAL_FIT_DETAILS.md#pathmmu-omitted-from-stage2-evaluation

[case-44]: TEMPORAL_FIT_DETAILS.md#pathmmu-proxy-obligation-lost

[case-45]: TEMPORAL_FIT_DETAILS.md#premature-collection-wrapup

[case-46]: TEMPORAL_FIT_DETAILS.md#premature-debug-cancellation

[case-47]: TEMPORAL_FIT_DETAILS.md#probe-output-blocks-full-generation

[case-48]: TEMPORAL_FIT_DETAILS.md#proxy-partial-output-retry

[case-49]: TEMPORAL_FIT_DETAILS.md#queued-debug-verification-abandoned

[case-50]: TEMPORAL_FIT_DETAILS.md#queued-memory-probe-abandoned

[case-51]: TEMPORAL_FIT_DETAILS.md#recovered-model-runtime-assets

[case-52]: TEMPORAL_FIT_DETAILS.md#regmean-nested-qsub-wrapper

[case-53]: TEMPORAL_FIT_DETAILS.md#regmean-queued-canary-cancellation

[case-54]: TEMPORAL_FIT_DETAILS.md#remote-weights-misdiagnosed-from-cache

[case-55]: TEMPORAL_FIT_DETAILS.md#repeated-malformed-tool-programs

[case-56]: TEMPORAL_FIT_DETAILS.md#resume-batch-state-mismatch

[case-57]: TEMPORAL_FIT_DETAILS.md#running-launcher-edited

[case-58]: TEMPORAL_FIT_DETAILS.md#sampled-eval-wrapper-dropped

[case-59]: TEMPORAL_FIT_DETAILS.md#skill-overrides-scoring-request

[case-60]: TEMPORAL_FIT_DETAILS.md#spawn-runner-missing-main-guard

[case-61]: TEMPORAL_FIT_DETAILS.md#stale-queued-training-status

[case-62]: TEMPORAL_FIT_DETAILS.md#stale-queued-watcher-status

[case-63]: TEMPORAL_FIT_DETAILS.md#stale-watcher-status

[case-64]: TEMPORAL_FIT_DETAILS.md#strict-merge-validation-bypassed

[case-65]: TEMPORAL_FIT_DETAILS.md#strict-shell-before-conversion-setup

[case-66]: TEMPORAL_FIT_DETAILS.md#strict-shell-before-module-setup

[case-67]: TEMPORAL_FIT_DETAILS.md#submission-after-failed-patch

[case-68]: TEMPORAL_FIT_DETAILS.md#swapped-benchmark-labels

### Case record links 69–101

[case-69]: TEMPORAL_FIT_DETAILS.md#synthetic-profile-omission

[case-70]: TEMPORAL_FIT_DETAILS.md#table-omits-prior-models

[case-71]: TEMPORAL_FIT_DETAILS.md#teacher-naturalization-leaks-solution

[case-72]: TEMPORAL_FIT_DETAILS.md#test-partitions-used-as-validation

[case-73]: TEMPORAL_FIT_DETAILS.md#text-only-ddp-unused-branches

[case-74]: TEMPORAL_FIT_DETAILS.md#three-parent-checkpoints-submitted

[case-75]: TEMPORAL_FIT_DETAILS.md#two-capacity-wrapper-mismatches

[case-76]: TEMPORAL_FIT_DETAILS.md#unloadable-training-parent-submission

[case-77]: TEMPORAL_FIT_DETAILS.md#unnecessary-job-dependencies

[case-78]: TEMPORAL_FIT_DETAILS.md#unrequested-decoder-debug-job

[case-79]: TEMPORAL_FIT_DETAILS.md#watcher-cli-contract-unvalidated

[case-80]: TEMPORAL_FIT_DETAILS.md#wrong-repository-redirect-claim

[case-81]: TEMPORAL_FIT_DETAILS.md#unscoped-train-files-glob

[case-82]: TEMPORAL_FIT_DETAILS.md#missing-total-training-steps-fallback

[case-83]: TEMPORAL_FIT_DETAILS.md#premature-fsdp-deletion-unverified-merge-assumption

[case-84]: TEMPORAL_FIT_DETAILS.md#bash-local-combined-assignment-bug

[case-85]: TEMPORAL_FIT_DETAILS.md#claude-budget-profile-omission

[case-86]: TEMPORAL_FIT_DETAILS.md#claude-unverified-training-progress

[case-87]: TEMPORAL_FIT_DETAILS.md#claude-phase-counter-loop

[case-88]: TEMPORAL_FIT_DETAILS.md#claude-ledger-wrong-directory

[case-89]: TEMPORAL_FIT_DETAILS.md#claude-stopped-productive-worker

[case-90]: TEMPORAL_FIT_DETAILS.md#claude-stale-collection-progress

[case-91]: TEMPORAL_FIT_DETAILS.md#claude-training-metric-as-benchmark

[case-92]: TEMPORAL_FIT_DETAILS.md#claude-shared-job-cache-reset

[case-93]: TEMPORAL_FIT_DETAILS.md#claude-smoke-skipped-changed-stage

[case-94]: TEMPORAL_FIT_DETAILS.md#claude-unverified-file-transfer

[case-95]: TEMPORAL_FIT_DETAILS.md#claude-readonly-survey-write

[case-96]: TEMPORAL_FIT_DETAILS.md#claude-verifier-gold-feature

[case-97]: TEMPORAL_FIT_DETAILS.md#claude-scratch-dashboard-escape

[case-98]: TEMPORAL_FIT_DETAILS.md#codex-training-request-generation

[case-99]: TEMPORAL_FIT_DETAILS.md#codex-parallel-campaign-omission

[case-100]: TEMPORAL_FIT_DETAILS.md#codex-model-policy-scope

[case-101]: TEMPORAL_FIT_DETAILS.md#deployment-layout-false-pass


- [Machine-readable review](temporal-fit.json).
- [Prior reproduction audit](PRONENESS.md).
- [Reference branch comparison](REFERENCE_BRANCHES.md).
