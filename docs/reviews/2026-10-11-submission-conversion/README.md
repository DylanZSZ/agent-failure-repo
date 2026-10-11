# Submitted failures: what can become a useful benchmark?

Updated 2026-10-11. Scope: both newly merged contributor collections (n=84 entries).

## Summary

**Research-scope review: [Which incidents depend on earlier work?](TEMPORAL_FIT.md)** The full 101-entry reassessment separates original historical relevance from the reproduction-quality judgments below. It also links the [reference-branch comparison](REFERENCE_BRANCHES.md) that informs the revised submission criteria.

**Follow-up: [Are these tasks actually error-prone?](PRONENESS.md)** The stricter pass reviews all 84 incoming and 17 laptop entries, plus the two derivatives. Its [complete table](PRONENESS_TABLE.md) separates historical importance from current task difficulty. The “build now” label below means feasible to construct; it does not mean ready as a long-horizon benchmark.

**Many incidents are worth converting, but the current decision-file exercises are not yet strong tests of agent behavior.** We reviewed all 84 entries from the two incoming collections: 81 problem packages and three deferred reports. The complete [84-row table](TABLE.md) links to an individual assessment of each case; [CSV](cases.csv) and [JSON](review.json) are also available.

| Recommendation | Entries | Meaning |
| --- | ---: | --- |
| Build now | 29 | Evidence and mechanism support constructing an action-based task. |
| Redesign first | 18 | The task, scoring rule, or scenario family needs revision. |
| Evidence first | 11 | Clarify the original requirement, action, or consequence first. |
| Short control | 26 | Useful reliability tests, but weak primary examples of long-horizon failure. |

Source: [per-case review](review.json). These mutually exclusive recommendations are judgments about the next step, not measured success rates. A short control can also need additional evidence.

The review uses the contributors' shared excerpts, task files, checkers and result records. We did not access their private histories. Both collections disclose limitations; their reduced examples do not constitute fresh model evaluations. The incoming 322 result records are scripted checks. No fresh model evaluation was performed in this initial conversion pass. The later [proneness review](PRONENESS.md) records two fresh attempts: one valid miss and one excluded for evaluator timing.

## Is the horizon actually long?

Several histories have substantial measured spans. Other incidents happen within seconds, and many have no measured interval. Of the 80 entries in the larger collection, 29 supply numeric horizon metadata and 51 do not. Some measured windows include diagnosis or recovery, which cannot be counted as work before the mistake. Elapsed wall time also includes idle time.

| Incident | Recorded span | Why it matters; what remains uncertain |
| --- | --- | --- |
| [Test partitions used as validation](CASE_DETAILS.md#test-partitions-used-as-validation) | 29 replies, 139 calls, 3.67 days | Prepared tuning configuration reused test data. No sweep ran, so actual score contamination was prevented. |
| [Allocator setting reintroduced](CASE_DETAILS.md#expandable-allocator-reintroduced) | 96 replies, 230 calls, 21.5 hours | Earlier removal was later reversed. The original rule's scope and the flag's causal role need clarification. |
| [Timing probe resumes earlier work](CASE_DETAILS.md#benchmark-resumes-prior-probe) | 23 replies, 72 calls, 2.05 hours | Reused run identity can invalidate a throughput measurement. The bad measurement was caught. |
| [Earlier module fix omitted](CASE_DETAILS.md#module-export-fix-omitted) | 32 replies, 117 calls, 70 minutes | A known environment fix failed to carry into a later workflow. |
| [Unscoped training glob](CASE_DETAILS.md#unscoped-train-files-glob) | About two weeks reported; unmeasured | Cache growth changes the data selected by a reused launcher. Original authorship and exact chronology are missing. |
| [Submit after failed patch](CASE_DETAILS.md#submission-after-failed-patch) | 0 intervening replies, 1 call, 3.9 seconds | A meaningful unchecked-action failure, but a short control. |

Sources: linked case assessments and their original evidence references. None of these spans establishes that extended history caused the error. Test that claim with matched fresh-context or reminder conditions, while retaining the same final task and available facts.

## What needs to change in the current packages?

The larger collection has 79 packaged decision exercises and one incident-only entry. The exercises generally ask the agent to write `decision.json`, then compare it with one exact dictionary. They are useful scoring prototypes, but a correct declaration does not show that an agent edited the right file, launched the right job, preserved data, or verified a claim. Some prompts also state the repair directly.

The review inspected the judges and ran 124 isolated synthetic probes across 40 packages. All 80 supplied correct/faulty examples scored as recorded, but additional inputs exposed important gaps:

- Six judges classify `{}` as a valid target failure despite no demonstrated action or opportunity.
- Two judges crash on nested values of the wrong type instead of returning an excluded result.
- An attention-dispatch judge rejects an explicitly permitted alternative configuration.
- A walltime judge requires exactly 60 hours and rejects a reasonable 64-hour estimate; the historical instruction does not justify its numerical cutoff.

Source: [all 124 inputs, judge hashes and outcomes](checker-review-a.json). These are checker findings, not additional historical incidents. [Reproduce the probes](reproduce-checker-review-a.py) after inspecting the referenced judges:

```sh
python3 docs/reviews/2026-10-11-submission-conversion/reproduce-checker-review-a.py \
  . docs/reviews/2026-10-11-submission-conversion/checker-review-a.json \
  /tmp/checker-review-rerun.json
```

Build the replacement tasks around observable actions: files actually edited, row IDs actually consumed, jobs actually accepted, artifacts actually preserved, and reports checked against those facts. Score task completion separately from the intended failure. Missing evidence, an unreached stage, and a malformed action are not automatically hits.

## Two concrete conversions

| Derived task | What the agent does | What identifies the error |
| --- | --- | --- |
| [Growing data cache][glob-task] | Creates a working launcher, does intervening bookkeeping, then runs a later cohort after the shared cache grows. | An evaluator-owned trainer records actual selected and consumed row IDs. Wrong cohort, recovery, and invalid state are distinct outcomes. |
| [Partial submission and retry][retry-task] | Submits two local mock jobs, receives an ambiguous batch error, and completes the original request. | An evaluator-owned event ledger records accepted jobs and whether two copies of one logical run overlap. |

Independent review passed all 21 current control scenarios across the two packages and 18 additional probes. A row-budget gap found during review was fixed; earlier development records were preserved. See the [data-selection audit](glob-independent-review.md) and [retry audit](partial-independent-review.md).

These are derivatives of existing incidents, not two additional incidents. They replace expensive systems with small local services. Their documentation keeps future prompts, reference policies and judging state outside the tested agent's access. The repository does not supply an operating-system sandbox or an automatic paid-model runner; the evaluator must enforce the documented access boundary. Both tasks compress the original sequence and therefore do not reproduce its historical duration.

## How to organize further conversions

Keep every historical incident and its provenance, while sharing reusable environment machinery. Queue/interpreter selection, shell initialization, checkpoint discovery, checkpoint conversion, status reporting and interrupted-output recovery recur across the collection. Group related histories and task templates when making evaluation splits; otherwise near-duplicate tasks can make coverage appear broader than it is.

Use the existing separation: `docs/` for collection and review records, `problems/<id>/` for each task and its local setup/checking code, and `results/<id>/<run>/` for actual attempts. Preserve the submitted originals. Give a behavioral derivative its own ID, link its source incident, and never count it as a new historical observation. Keep short controls alongside longer sequences with explicit labels.

Before claiming reproduction, request [the evaluation and evidence checklist](EVALUATION_REQUESTS.md). The [individual assessments](CASE_DETAILS.md) specify what each contributor needs to supply. Requests are documented here; no messages were sent to contributors.

## Laptop collection included with this submission

The separately prepared [laptop collection][laptop] adds 17 supported historical incidents: 13 from Claude Code and four from Codex. Five have packaged tasks; 12 remain incidents with checker prototypes. Its 54 recorded scripted checks are separate from this review's probes and from fresh model evaluations. Full semantic review remains incomplete; 97 unresolved lead records remain in its index.

Only the previously presented 333-file collection manifest was copied. Publication-status notes were updated after the owner's instruction to pull and push. Raw histories, source mappings, search databases and the private working report remain local. The five packaged tasks passed their documented reference controls in a clean copy containing only those proposed files; see the [verification receipt](laptop-clean-verification.json).

The [initial submission file list](SUBMISSION_FILES.txt) records the original contribution. The later [proneness follow-up file list](PRONENESS_FILES.txt) records the separate audit and pilot changes. Existing contributor files are preserved.

## Next steps

Use the later [proneness review](PRONENESS.md) to revise task designs and plan further evaluation. Retain every attempt and build longer sequences only where the historical mechanism warrants them. Request the specific missing evidence before promoting ambiguous incidents.

## Sources

Reviewed repository revision: `9209e6f`. Evidence is linked per case in [the detailed assessments](CASE_DETAILS.md). Scripted outcomes from the initial review are linked above; subsequent fresh attempts and their limitations are in the [proneness review](PRONENESS.md).

[glob-task]: ../../../problems/unscoped-train-files-glob-staged/README.md
[retry-task]: ../../../problems/partial-submit-duplicate-staged/README.md
[laptop]: ../../collections/laptop-20261011/README.md
