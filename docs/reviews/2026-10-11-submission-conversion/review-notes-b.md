# Review of submitted failures: group B

Reviewed all 40 assigned manifests and narratives, task-facing prompts/fixtures, checker definitions, selected published historical evidence, common setup/advance scripts and all 156 result metadata records. Original private transcripts were unavailable. No contributor files were modified; no submitted script, historical command, remote job or model call was executed.

39 packages are decision exercises and one is incident-only. All 156 results are `scripted_check`; none measures a fresh agent run. Shared setup only copies a JSON fixture and advance replaces it. That is useful for checking a scoring rule, but it does not reproduce the original action or preserve original duration. These distinctions are usually disclosed honestly in the READMEs.

Verdicts mean:

- **convert_now**: the evidence and mechanism support building an action-based local environment now; the existing reduction is not thereby validated.
- **needs_rework**: revise the task/predicate or share a common scenario implementation before evaluation.
- **needs_evidence**: settle an original requirement, authority or provenance ambiguity before presenting an unambiguous benchmark failure.
- **short_control**: keep as a useful short test/control, not primary evidence of long-horizon failure.

## Main findings

1. `test-partitions-used-as-validation` is the strongest temporal candidate here: 316,989.89 seconds (~3.67 days), 29 visible assistant messages and 139 calls between anchors. The actual consequence was a prepared configuration that would tune on test; no sweep ran. A miniature real tuning pipeline can verify which row IDs are accessed.
2. `sampled-eval-wrapper-dropped` retains an earlier successful implementation and a later same-settings request. Verify actual sample IDs/counts through wrapper execution. The current judge misses an incorrect full-data run when the agent still claims to use uniform sampling.
3. `partial-submit-duplicate` is a strong practical failure with a compact local simulation: accept one side effect, lose its response, then score reconciliation versus duplicate live submissions. This tests uncertainty about action outcomes directly.
4. `strict-merge-validation-bypassed` has a clear strict flag, real mismatch and actual weakening. Tiny numerical files and a merge CLI suffice. Honest disclosure of a non-strict fallback must not be confused with an authorized waiver.
5. The active-launcher edit, probe-to-full-generation transition, stale watcher report and interrupted-output retry all support real file/stateful conversions with no GPU or external service.

## Common revisions

- Stop judging declarations such as `same_examples`, `config_checked`, `diagnostic_only` and `submit` as if they were observed behavior. Read actual files, outputs and evaluator-owned action logs. In `test-partitions-used-as-validation`, test categories plus `same_examples:false` evade the present target predicate.
- Exact dictionary equality rejects harmless extra fields, different orderings and valid alternative implementations. Judge semantic invariants. The text-only DDP fixture itself permits freezing the unused branch, but its exact reference rejects that solution.
- Several final prompts are historical conclusions, not tasks: queue-memory recovery, corrected checkpoint paths, watcher CLI diagnosis, and wrong-repository diagnosis. Supply a natural current request with enough discoverable evidence, not the repair answer.
- The conversion-shell incident copies the five-update probe prompt and fixture. Its actual task was model conversion. Correct task fidelity before merging scenarios.
- Preserve earlier correct state and add meaningful intervening work where history dependence is the question. Do not repeat the answer as a new final-stage instruction. Do not infer duration from source line numbers or include recovery hours in a pre-error horizon.
- Define eligibility from trusted stage-delivery records; a JSON dictionary cannot prove that both stages occurred. Add matched short/fresh-context controls and report all attempts. None has been run yet.

## Shared families

Keep distinct original incidents, but avoid counting near-identical reductions as independent task mechanisms:

- Queue persistence: premature-debug-cancellation, queued-debug-verification-abandoned, queued-memory-probe-abandoned, regmean-queued-canary-cancellation.
- Status authority: stale-queued-training-status, stale-queued-watcher-status, stale-watcher-status.
- Checkpoint root preflight: three-parent-checkpoints-submitted, unloadable-training-parent-submission.
- Shell initialization: strict-shell-before-module-setup, strict-shell-before-conversion-setup.
- Evaluation obligation retention: sampled-eval-wrapper-dropped, pathmmu-proxy-obligation-lost, pathmmu-omitted-from-stage2-evaluation. Partition leakage is related context but a distinct data-boundary mechanism.
- Interrupted artifact handling: probe-output-blocks-full-generation and proxy-partial-output-retry.

## Evidence to request

For every converted task request the original applicable contract, earlier correct state, actual faulty action and outcome, recovery/contrary evidence, plus a defined requirement-to-decision horizon. Fresh model traces/results need exact task/judge revisions and explicit run denominators. Selective public excerpts support a narrower claim than access to the full original trace. All model revisions here are unspecified. Cases involving unclear standalone delivery, a prior design proposal, a terse table request, or whether a skill embodied an independent site rule need those authority gaps resolved first.

The full per-incident assessments and concrete conversion/checker designs are in `review.json`.

Disposition counts: convert_now: 13, needs_evidence: 4, needs_rework: 9, short_control: 14.
