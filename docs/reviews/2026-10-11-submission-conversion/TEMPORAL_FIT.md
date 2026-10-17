# Which incidents should we pursue as failures from long-running work?

Updated 2026-10-11.

## Summary

**Prioritize five historical candidates with documented intervening work; do not treat all submitted bugs as long-running failures.** Reviewing every historical entry (n=101) found 28 plausible dependencies on earlier work or state. Within those 28, five describe substantial intervening work, 13 currently demonstrate only a short mechanism, and ten lack enough evidence about the intervening work. None establishes that extended running caused the error.

The [complete table][table] covers every entry. The [individual assessments][details] explain the expected behavior, earlier and later anchors, actual work or missing evidence, alternative explanation, current reproduction limits, and next action. The [reference-branch comparison][branches] explains the intended behaviors behind the revised collection instructions.

## What the collection should target

The desired sequence is **earlier work → meaningful continued work or change → a later decision that mishandles what came before**. An earlier rule can be forgotten or overgeneralized. Previously correct notes, tests, or outputs can become stale. Compatible work can be overwritten. An initial mistake can spread through dependent actions, or competing tasks can displace a still-active goal.

Both reference branches contain such designs and ordinary reliability cases. Their strongest lesson is to preserve the actual dependency and competing demands. The collecting agent should not turn a historical mistake into a small question that already supplies the diagnosis, live state, or correct answer. A short reproduction can demonstrate a useful mechanism, but it does not measure the contribution of prolonged work.

Source: [comparison of both pinned branches][branches] and [revised submission criteria][criteria].

## How the current entries are classified

These are review judgments from shared evidence, not model error rates. The two derived task packages are versions of existing incidents and are not counted again.

| Original-incident relevance | Incoming entries | Our laptop entries | Total |
| --- | ---: | ---: | ---: |
| Plausible dependency on earlier work or state | 21 | 7 | 28 |
| Evidence needed to establish the error or dependency | 16 | 0 | 16 |
| Short reliability control | 47 | 10 | 57 |
| Total | 84 | 17 | 101 |

Source: [all per-case decisions][data].

A dependency on an earlier action is not sufficient to call an incident long-running. The 28 candidates therefore have a separate assessment of the original work exposure:

| Evidence of intervening work among the 28 candidates | Count | Treatment |
| --- | ---: | --- |
| Substantial engineering work described | 5 | Prioritize faithful reconstruction and then evaluation |
| Only a short mechanism currently shown | 13 | Retain separately; do not claim long-running exposure |
| Insufficient detail about the intervening work | 10 | Recover the missing middle of the sequence |

Source: the exposure decision and reason in each [case record][data]. This is a conservative assessment of available evidence, not a fixed turn-count threshold.

For example, accepting some jobs and immediately retrying all of them can cause duplicates. That is meaningful compounding state, but it can happen in a short exchange. A cached status becoming stale during hours of waiting also does not establish hours of agent reasoning. These remain useful mechanisms without being counted as observed long-running failures.

## Five priorities and the intended errors

All five still need work before a credible long-running pilot. Four original reductions need redesign; the offline-cache case needs an additional check of the delivered wrapper's effective behavior. Its work history is visible, but the claimed final omission may be supplied by another script.

| Historical candidate | Work that connects earlier and later events | Intended error to detect |
| --- | --- | --- |
| [Earlier environment repair omitted][module] | Diagnose a working environment, then migrate wrappers and interpreter selection | The later executed launch loses the earlier required module cleanup |
| [Offline-cache protection omitted][offline] | Diagnose cache behavior, run a successful benchmark, then prepare full launches | A later launch actually loses the required protection; inspect inherited settings first |
| [Proxy-stage obligation lost][proxy] | Implement evaluation stages and parsing, then normalize configuration and documentation | A still-required proxy stage is absent from effective generated work |
| [Test data used as validation][holdout] | Accept a holdout plan, build evaluation infrastructure, then integrate another benchmark | Prepared tuning configuration selects test data contrary to the earlier plan |
| [Old smoke success reused after dependencies change][smoke] | Perform thirteen smoke/debug iterations while dependencies and validation coverage change | Claim the training stage is ready without validating that stage under the changed environment |

Source: linked per-case assessments and their submitted evidence. The holdout configuration was caught before a sweep; do not invent contaminated scores. The smoke case's later retry/wait interval is a consequence, not additional pre-error exposure.

These priorities concern evidence quality and fit, not predicted failure probability. Longer numeric windows alone did not qualify allocator reintroduction, the timing probe, training-to-generation substitution, or the growing data cache. Their broader mechanisms may be worthwhile, but the shared evidence does not sufficiently anchor the intervening activity.

## What needs revisiting in the reproductions

The earlier audit judged the quality of the current tasks: 56 needed redesign, 12 needed evidence, and 33 were short controls. Those figures answer a different question from original historical relevance. Among the 28 temporal candidates, the original reductions were rated 22 needing redesign, two needing evidence, and four short controls. Neither classification replaces the other.

Source: [prior task-readiness audit][readiness] and its preserved per-case classifications in [this review][data].

The revision should restore the missing decision. Let the agent make or discover the earlier artifact, keep the actual state it creates, introduce only the historical kind of legitimate continued work, and test its later actions independently. Do not overwrite the first stage with a fixed final fixture. Do not supply the live job inventory or a prejoined metric row when discovering or joining those facts was the original burden.

A task can remain useful when all required information is discoverable in the final repository. That tests handling accumulated state; it does not automatically test retaining conversational memory. Keep the correct path accessible and compare the proposed mechanisms explicitly. Do not hide requirements, remove real warnings, or pad a short mistake with unrelated work until the agent fails.

## Next steps and evaluation requests

For the five priorities, collect the exact original requirement, the earlier successful or committed state, the intervening edits and tool results, the first wrong action, and the final outcome after any repair. For the ten candidates with unknown exposure, recover the missing activity between the anchors before designing a long-running version. For the 16 evidence-needed leads, resolve the specific scope, attribution, or consequence gap recorded in the full table.

For anyone claiming reproduction, request all fresh-agent attempts, not only hits: exact task and judge versions, prompts and tool definitions, available model settings, starting and delivered state, visible action traces, independent checks, corrections, exclusions, and comparison results. If these do not exist, record **not run**. A scripted bad example verifies the checker; it is not evidence that an agent is prone to the error.

There are still only two fresh attempts in the existing derived-task records: one valid scheduler attempt avoided the target error, and one data-selection attempt was excluded for evaluator timing. This revision adds no benchmark attempts. Neither the original incident counts nor those two attempts estimate a long-running effect.

Source: [existing pilot outcomes and limitations][pilots].

## Changes to the collection workflow

The one-message prompt, agent instructions, installable skill, evidence forms, reproduction guide, and submission review now require an earlier-to-later account and an alternative explanation. They separate original relevance, observed work exposure, task readiness, and causal evidence. They preserve all credible leads while reporting short mechanisms, local controls, and uncertain records separately.

Contributors can still submit incident-only evidence. Rejected leads remain in the private inventory with reasons. An approved change of goal, a justified changed scientific conclusion, or honest blocking is not a failure by itself. The revised workflow requests missing results rather than inventing stronger evidence or rejecting a useful lead for lacking a model run.

The standalone skill was rebuilt and validated. Repository checks passed: 100 unit tests, metadata validation for 100 packages and 409 existing result records, the synthetic example, and distribution consistency. An independent instruction review and five invented history snippets checked the wording; those snippets are skill tests, not collected incidents or benchmark results.

Source: [verification record](criteria-checks.json). The [exact changed-file list][files] separates this maintenance revision from the earlier submissions.

## Limitations

This pass used submitted public evidence, prior task inspections, and current reference-branch specifications. It did not reopen private raw histories, rerun reference benchmarks, or modify contributors' original packages and result records. Some original anchor labels point to requests or recovery rather than the exact first error; those limitations remain in every affected record.

The initial reference comparison concerned design intent; detailed cleanup results were unavailable during that pass. A subsequent read-only review of the results-contract collection and publication repository informed the additional evaluator and evidence requirements in [the submission criteria][criteria]. It did not reopen contributors' private histories or change the 101 incident classifications above. The [reference comparison][branches] records the follow-up scope and lessons.

Even a persuasive observed sequence does not isolate whether duration, changing state, conflicting requirements, local skill, or a context boundary caused the error. That needs a defensible comparison with actual agent attempts.

## Sources

[table]: TEMPORAL_FIT_TABLE.md

[details]: TEMPORAL_FIT_DETAILS.md

[data]: temporal-fit.json

[branches]: REFERENCE_BRANCHES.md

[criteria]: ../../LONG_HORIZON.md

[readiness]: PRONENESS.md

[pilots]: PRONENESS.md#what-happened-in-the-fresh-pilots

[module]: TEMPORAL_FIT_DETAILS.md#module-export-fix-omitted

[offline]: TEMPORAL_FIT_DETAILS.md#offline-cache-protection-omitted

[proxy]: TEMPORAL_FIT_DETAILS.md#pathmmu-proxy-obligation-lost

[holdout]: TEMPORAL_FIT_DETAILS.md#test-partitions-used-as-validation

[smoke]: TEMPORAL_FIT_DETAILS.md#claude-smoke-skipped-changed-stage

[files]: TEMPORAL_FIT_FILES.txt

- [Download the review as CSV](temporal-fit.csv).
- [Submission file contract](../../SUBMITTING.md).
- Reference branch hashes and source line links are recorded in the branch comparison.
- Reviewed submission baseline: `c054c1ed7f5b96ec1ffd6e56cdf1f80dc919bb95`.
- Verification commands: `make check`; skill-creator `quick_validate.py`; readable `readable_lint.py --strict` on the criteria and new reports.
