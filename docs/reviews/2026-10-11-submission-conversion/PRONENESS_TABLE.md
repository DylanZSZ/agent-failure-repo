# Which submitted tasks still need work?

Updated 2026-10-11.

## Summary

This table covers all historical entries (n=101): 84 incoming and 17 from the laptop collection. The decision concerns readiness for long-horizon evaluation, not whether an incident was serious or a model could ever fail a simple task. Each case links to evidence, the intended error, the role of history, and a proposed discriminating test.

Source: [complete structured review](proneness-review.json).

“Redesign” means the reduction removes the natural difficulty or scores a declaration instead of behavior. “Clarify the evidence” means the original error or consequence needs confirmation. A short control can be useful but is not a primary long-horizon test. Priority ranks follow-up work, not measured error probability.

## Incoming submissions

| Case | What to do next | Priority |
| --- | --- | --- |
| [Analysis command selects a parent without checkpoint configuration](PRONENESS_DETAILS.md#analysis-parent-checkpoint) | Redesign the task | Medium |
| [Archive extraction completion is reported without checking the live process](PRONENESS_DETAILS.md#archive-success-before-process-exit) | Clarify the evidence | Low |
| [Strict unset-variable checking aborts Aurora module initialization](PRONENESS_DETAILS.md#aurora-nounset-before-module) | Keep as a short control | Low |
| [Automatic monitoring is dropped despite an available exact session ID](PRONENESS_DETAILS.md#available-session-id-ignored-for-monitoring) | Clarify the evidence | Medium |
| [Later timing probe reuses prior run ID and resumes an already completed probe](PRONENESS_DETAILS.md#benchmark-resumes-prior-probe) | Redesign the task | High |
| [A queue switch retains the previous queue-only interpreter](PRONENESS_DETAILS.md#capacity-switch-retains-next-eval-venv) | Redesign the task | High |
| [Attention backend is selected on wrapper but misses composite text model](PRONENESS_DETAILS.md#composite-attention-dispatch) | Redesign the task | Medium |
| [Delivered multi-device merger stacks router rows before staging them](PRONENESS_DETAILS.md#connector-router-cross-device-stack) | Keep as a short control | Medium |
| [A result row combines metrics from two different models](PRONENESS_DETAILS.md#cross-model-metric-row) | Redesign the task | High |
| [Analysis defaults omit dense checkpoint decoder keys](PRONENESS_DETAILS.md#dense-decoder-group-mismatch) | Keep as a short control | Low |
| [Directional Fisher loader uses model parameter keys against differently named stored tensors](PRONENESS_DETAILS.md#directional-checkpoint-key-mismatch) | Keep as a short control | Low |
| [A submission duplicates the launcher directory in its path](PRONENESS_DETAILS.md#duplicated-launcher-path) | Keep as a short control | Low |
| [Endpoint-logit interpolation is proposed for a control that must preserve initial Fisher](PRONENESS_DETAILS.md#endpoint-logit-control) | Keep as a short control | Low |
| [EvoGM evaluation wrapper supplies a JSON array to a JSONL reader](PRONENESS_DETAILS.md#evolutionary-evaluation-jsonl-contract-missed) | Redesign the task | Medium |
| [Repair writes the same exclusive-create provenance file twice](PRONENESS_DETAILS.md#exclusive-provenance-written-twice) | Redesign the task | Medium |
| [Known incompatible allocator setting is reintroduced during checkpoint conversion](PRONENESS_DETAILS.md#expandable-allocator-reintroduced) | Clarify the evidence | High |
| [Expert Merging++ fitting compares incompatible checkpoint and loaded-model parameter names](PRONENESS_DETAILS.md#fitting-checkpoint-key-conversion-omitted) | Redesign the task | Medium |
| [FLAT benchmark retains COMPOSITE-only affinity wrapper](PRONENESS_DETAILS.md#flat-mode-composite-wrapper) | Keep as a short control | Low |
| [One of three capacity jobs keeps the next-eval environment][capacity-environment] | Redesign the task | Medium |
| [A documented first-run cache workaround is lost when creating an Aurora launch script](PRONENESS_DETAILS.md#fresh-vllm-cache-workaround-omitted) | Redesign the task | High |
| [Resubmission reuses shards whose manifest the changed runner rejects](PRONENESS_DETAILS.md#incompatible-fisher-resume) | Clarify the evidence | Medium |
| [Failed in-place substitution empties a launcher and still passes validation](PRONENESS_DETAILS.md#inplace-launcher-truncation) | Redesign the task | High |
| [The vLLM rendering adapter sends instruction prompts as raw completions](PRONENESS_DETAILS.md#instruction-model-chat-template-omitted) | Redesign the task | Medium |
| [Learning carryover reads an absent knowledge-state attribute](PRONENESS_DETAILS.md#learning-carryover-missing-field) | Keep as a short control | Low |
| [Login shell redirects implementation to a neighboring repository](PRONENESS_DETAILS.md#login-shell-misdirects-implementation) | Redesign the task | Medium |
| [Routing submission uses a malformed sample-count environment variable](PRONENESS_DETAILS.md#malformed-routing-sample-variable) | Keep as a short control | Low |
| [Restart requests queue maximum rather than estimating remaining training](PRONENESS_DETAILS.md#maximum-walltime-instead-of-estimate) | Clarify the evidence | Low |
| [An answer parser accepts a lowercase ambiguous choice as a valid MC answer](PRONENESS_DETAILS.md#mc-parser-lowercase-ambiguity-accepted) | Keep as a short control | Low |
| [Fisher calibration interpretation compares different model precision and record sets](PRONENESS_DETAILS.md#mismatched-fisher-kl-protocol) | Redesign the task | High |
| [Resume submission retains explicit auto-resume false](PRONENESS_DETAILS.md#missed-resume-flag) | Redesign the task | Medium |
| [Training skip_eval is misreported as no evaluation result](PRONENESS_DETAILS.md#missed-separate-evaluation) | Redesign the task | High |
| [Environment migration retains module export that previously caused startup failure](PRONENESS_DETAILS.md#module-export-fix-omitted) | Redesign the task | High |
| [Parent checkpoint path leads to incorrect text-only diagnosis](PRONENESS_DETAILS.md#nested-vl-checkpoint) | Keep as a short control | Low |
| [Unconditional next-eval interpreter change breaks the shared capacity launcher](PRONENESS_DETAILS.md#next-eval-interpreter-leaks-into-capacity) | Redesign the task | High |
| [Discovered shared cache workaround is omitted from one related launcher](PRONENESS_DETAILS.md#offline-cache-protection-omitted) | Clarify the evidence | High |
| [An explicit one-job evaluation is submitted as separate suite jobs](PRONENESS_DETAILS.md#one-job-evaluation-split) | Redesign the task | High |
| [Trainer import initializes compute-only MPI on the login host](PRONENESS_DETAILS.md#opd-import-time-mpi-init) | Keep as a short control | Low |
| [Submission wrapper receives a nested qsub executable](PRONENESS_DETAILS.md#opd-nested-qsub-wrapper) | Keep as a short control | Low |
| [New OPD launcher enables nounset before module initialization](PRONENESS_DETAILS.md#opd-strict-shell-module-init) | Clarify the evidence | Low |
| [Additional finite-difference GPU work is attempted while the authorized derivative run is active](PRONENESS_DETAILS.md#overlapping-finite-difference-attempt) | Clarify the evidence | Medium |
| [Proxy fan-out uses interpreter handoff that bypasses its evaluation virtualenv](PRONENESS_DETAILS.md#packed-proxy-environment-preflight) | Redesign the task | Medium |
| [Partial scheduler submission is retried without reconciliation](PRONENESS_DETAILS.md#partial-submit-duplicate) | Redesign the task | High |
| [Default evaluation batch omits the required PathMMU suite][omitted-evaluation] | Redesign the task | Medium |
| [PathMMU proxy participation is dropped during configuration review](PRONENESS_DETAILS.md#pathmmu-proxy-obligation-lost) | Redesign the task | High |
| [Collection stops after screening despite required chronological review](PRONENESS_DETAILS.md#premature-collection-wrapup) | Redesign the task | Medium |
| [Queued debug allocation is canceled before the requested work runs](PRONENESS_DETAILS.md#premature-debug-cancellation) | Redesign the task | Medium |
| [A generation probe leaves output that blocks the full submission](PRONENESS_DETAILS.md#probe-output-blocks-full-generation) | Redesign the task | High |
| [Proxy restart preserves a partial ReXVQA directory but cannot resume it](PRONENESS_DETAILS.md#proxy-partial-output-retry) | Redesign the task | High |
| [A healthy queued GPU verification is canceled before it starts](PRONENESS_DETAILS.md#queued-debug-verification-abandoned) | Redesign the task | Medium |
| [Normal queue wait ends an announced GPU memory check prematurely](PRONENESS_DETAILS.md#queued-memory-probe-abandoned) | Redesign the task | Medium |
| [Recovered model delivery omits tokenizer and processor runtime files](PRONENESS_DETAILS.md#recovered-model-runtime-assets) | Redesign the task | Medium |
| [Submission wrapper receives a nested qsub executable](PRONENESS_DETAILS.md#regmean-nested-qsub-wrapper) | Keep as a short control | Low |
| [Healthy queued RegMean canary canceled before required GPU verification](PRONENESS_DETAILS.md#regmean-queued-canary-cancellation) | Redesign the task | Medium |
| [Missing local cache shards are reported as absent remote weights](PRONENESS_DETAILS.md#remote-weights-misdiagnosed-from-cache) | Redesign the task | Medium |
| [Five successive malformed orchestration programs fail before inspection](PRONENESS_DETAILS.md#repeated-malformed-tool-programs) | Keep as a short control | Low |
| [Changing resume accumulation while saved microbatch overrides CLI trains zero steps](PRONENESS_DETAILS.md#resume-batch-state-mismatch) | Redesign the task | High |
| [Editing a running shell launcher corrupts its trailing command](PRONENESS_DETAILS.md#running-launcher-edited) | Redesign the task | High |
| [Same-settings evaluation drops the operative random-sampling wrapper](PRONENESS_DETAILS.md#sampled-eval-wrapper-dropped) | Redesign the task | High |
| [Skill default overrides an explicit CPU scoring instruction](PRONENESS_DETAILS.md#skill-overrides-scoring-request) | Clarify the evidence | Medium |
| [Live inference runner starts spawn workers during module import](PRONENESS_DETAILS.md#spawn-runner-missing-main-guard) | Keep as a short control | Low |
| [Stopped watcher snapshots misreport failed jobs as still queued](PRONENESS_DETAILS.md#stale-queued-training-status) | Redesign the task | High |
| [A completed job is reported as not yet started from stale watcher state](PRONENESS_DETAILS.md#stale-queued-watcher-status) | Redesign the task | High |
| [Stale watcher state is reported despite complete evaluation artifacts](PRONENESS_DETAILS.md#stale-watcher-status) | Redesign the task | Medium |
| [Strict merge validation is dropped after detecting unequal shared weights](PRONENESS_DETAILS.md#strict-merge-validation-bypassed) | Redesign the task | High |
| [Conversion launcher repeats unset-variable checks before module initialization](PRONENESS_DETAILS.md#strict-shell-before-conversion-setup) | Keep as a short control | Low |
| [New probe wrapper enables unset-variable checks before Lmod setup](PRONENESS_DETAILS.md#strict-shell-before-module-setup) | Keep as a short control | Low |
| [Failed runtime patch is followed by unconditional job submission](PRONENESS_DETAILS.md#submission-after-failed-patch) | Keep as a short control | Medium |
| [Benchmark result columns are swapped in the report](PRONENESS_DETAILS.md#swapped-benchmark-labels) | Keep as a short control | Low |
| [Synthetic generator loses profile conditioning during simplification](PRONENESS_DETAILS.md#synthetic-profile-omission) | Clarify the evidence | Medium |
| [Table formatting omits the two models just reported](PRONENESS_DETAILS.md#table-omits-prior-models) | Keep as a short control | Low |
| [Teacher naturalization violates the diagnostic-only classroom invariant](PRONENESS_DETAILS.md#teacher-naturalization-leaks-solution) | Redesign the task | Medium |
| [PathMMU test partitions are configured as validation tuning inputs](PRONENESS_DETAILS.md#test-partitions-used-as-validation) | Redesign the task | High |
| [Text-only support omits distributed unused-branch handling](PRONENESS_DETAILS.md#text-only-ddp-unused-branches) | Redesign the task | Medium |
| [Directory existence check misses nested model checkpoints in three evaluations](PRONENESS_DETAILS.md#three-parent-checkpoints-submitted) | Redesign the task | Medium |
| [Next-eval wrapper is used for two capacity jobs](PRONENESS_DETAILS.md#two-capacity-wrapper-mismatches) | Redesign the task | Medium |
| [Evaluation submission accepts a training parent without model configuration](PRONENESS_DETAILS.md#unloadable-training-parent-submission) | Redesign the task | Medium |
| [False one-job limit causes unnecessary dependency holds](PRONENESS_DETAILS.md#unnecessary-job-dependencies) | Redesign the task | Medium |
| [A question about existing decoder results launches a new GPU allocation](PRONENESS_DETAILS.md#unrequested-decoder-debug-job) | Redesign the task | Medium |
| [Mocked delivery tests miss incompatible live Codex CLI arguments](PRONENESS_DETAILS.md#watcher-cli-contract-unvalidated) | Redesign the task | Medium |
| [Login shell changes directory and wrong repository becomes a redirect claim](PRONENESS_DETAILS.md#wrong-repository-redirect-claim) | Keep as a short control | Medium |
| [Unscoped file-selection glob silently ignores a requested sub-range when the directory holds extra files](PRONENESS_DETAILS.md#unscoped-train-files-glob) | Keep as a short control | High for staged derivative |
| [Production jobs inherit a ten-step smoke-test default](PRONENESS_DETAILS.md#missing-total-training-steps-fallback) | Clarify the evidence | Medium |
| [Checkpoint pruning removes the only recoverable weights](PRONENESS_DETAILS.md#premature-fsdp-deletion-unverified-merge-assumption) | Clarify the evidence | High evidence request |
| [A dependent bash local assignment breaks a verification step](PRONENESS_DETAILS.md#bash-local-combined-assignment-bug) | Keep as a short control | Low |

Source: [per-case assessments](PRONENESS_DETAILS.md) and [structured review](proneness-review.json).

## Our laptop collection

| Case | What to do next | Priority |
| --- | --- | --- |
| [Budget constants changed, but the runtime profile was left stale](PRONENESS_DETAILS.md#claude-budget-profile-omission) | Redesign the task | High |
| [Scheduler activity was reported as progress in a blocked run](PRONENESS_DETAILS.md#claude-unverified-training-progress) | Redesign the task | High |
| [A completion loop keeps waiting after its phase counter resets](PRONENESS_DETAILS.md#claude-phase-counter-loop) | Keep as a short control | Medium |
| [A no-op commit skipped the directory change and wrote the ledger into the code repository](PRONENESS_DETAILS.md#claude-ledger-wrong-directory) | Keep as a short control | Medium |
| [A stale output file was treated as proof that a productive worker had stalled](PRONENESS_DETAILS.md#claude-stopped-productive-worker) | Redesign the task | High |
| [A crashed collection was reported as advancing because a stale counter and a live endpoint were mistaken for job progress](PRONENESS_DETAILS.md#claude-stale-collection-progress) | Redesign the task | High |
| [Training-batch accuracy was presented as benchmark evidence that model quality had declined](PRONENESS_DETAILS.md#claude-training-metric-as-benchmark) | Keep as a short control | Medium |
| [A resumed worker reset a shared job cache and erased the records it needed to harvest a teammate’s jobs](PRONENESS_DETAILS.md#claude-shared-job-cache-reset) | Redesign the task | High |
| [The changed training stack was declared proven before fresh-stage failures caused repeated full-job retries](PRONENESS_DETAILS.md#claude-smoke-skipped-changed-stage) | Redesign the task | High |
| [A failed file transfer was described as checksum-verified and left the next executor without its input](PRONENESS_DETAILS.md#claude-unverified-file-transfer) | Keep as a short control | Medium |
| [A strictly read-only storage survey included a remote temporary-file write](PRONENESS_DETAILS.md#claude-readonly-survey-write) | Keep as a short control | Medium |
| [An independent verifier used gold-label length as a prediction feature and obtained a spurious perfect score](PRONENESS_DETAILS.md#claude-verifier-gold-feature) | Redesign the task | Medium |
| [A scratch-only verification wrote into the real dashboard because an assumed environment override did not exist](PRONENESS_DETAILS.md#claude-scratch-dashboard-escape) | Redesign the task | Medium |
| [An ARM follow-up dispatches generation jobs during a training task](PRONENESS_DETAILS.md#codex-training-request-generation) | Keep as a short control | High |
| [A current status report omits a parallel campaign after an explicit reminder](PRONENESS_DETAILS.md#codex-parallel-campaign-omission) | Keep as a short control | Medium |
| [Model-specific thinking allowance is copied onto the actor](PRONENESS_DETAILS.md#codex-model-policy-scope) | Keep as a short control | Medium |
| [Deployment reviewer approves a launcher that rejects its supported deployed layout](PRONENESS_DETAILS.md#deployment-layout-false-pass) | Keep as a short control | Medium |

Source: [per-case assessments](PRONENESS_DETAILS.md) and [structured review](proneness-review.json).

## Sources

- [Full assessments and exact file-line excerpts](PRONENESS_DETAILS.md).
- [Machine-readable review](proneness-review.json) and [complete CSV](proneness-cases.csv).
- [Summary, derivative review and pilot limitations](PRONENESS.md).

[capacity-environment]: PRONENESS_DETAILS.md#fp32-capacity-environment
[omitted-evaluation]: PRONENESS_DETAILS.md#pathmmu-omitted-from-stage2-evaluation
