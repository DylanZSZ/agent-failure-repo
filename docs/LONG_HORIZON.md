# Collect failures that depend on earlier work

Updated 2026-10-11.

## Summary

Our goal is to find failures caused or made more likely by extended agent work: accumulated obligations, changing artifacts, competing task context, repeated repairs, and transitions between sessions or collaborators. A bug appearing late in a transcript is not enough. Collect every credible lead, but distinguish a plausible connection to earlier work from an ordinary short-task error and from demonstrated causation.

Read this guide before choosing which incidents to reproduce. Use the [symptom catalog](SYMPTOMS.md) to find observable errors; use the criteria here to decide whether they fit the research question. A symptom label, a large token count, a runnable task, or a checker rejecting a planted defect cannot establish a long-running failure.

## The sequence we want

A useful candidate has a traceable sequence:

1. **Something earlier matters.** A requirement, discovery, completed implementation, scoped convention, commitment, ownership boundary, or provisional assumption is established. An earlier mistake can also matter when the target is its later propagation.
2. **Real work changes the situation.** Features accumulate, artifacts evolve, another task competes for attention, a teammate edits the workspace, context is compressed, or work crosses a session or project boundary. Identify the actual work or transition.
3. **A later decision tests continuity.** During the same ongoing request, or a legitimate follow-up request, the agent must retain, rediscover, update, revoke, correctly scope, or verify something from that earlier work. State what an acceptable action would be with the information and tools available then.
4. **An observable action mishandles it.** Identify the first wrong action, its effect, any repair, and the delivered outcome separately. A plausible causal explanation still needs testing.

Explain the dependency in one sentence: “After doing ___, the agent encountered ___; it needed to carry forward or revise ___, but instead ___.” Fill this from evidence. If the missing part is only a guess, keep it as an evidence-needed lead.

There is no universal minimum turn count. A short reproduction can preserve a temporal mechanism without measuring extended exposure. Label it accordingly. Long idle waits, simulator ticks, repeated “continue” messages, and difficult debugging after the error do not by themselves establish a long-running cause.

## Behaviors worth looking for

| Earlier work or state | Later behavior of interest | Essential burden to preserve |
| --- | --- | --- |
| Standing rule or accumulated feature | Omission, partial withdrawal, wrong effective edit | Recover all applicable obligations and locations |
| Useful rule learned in one scope | Apply it in the wrong module or project | Distinguish scopes despite similar code or terminology |
| Notes, design assumptions, or old conclusions | Follow them despite changed current evidence | Reconcile earlier knowledge with the present state |
| Completed work or a teammate's compatible edit | Regress, overwrite, or delete it during later work | Preserve behavior beyond the newest request |
| Temporary data or a permission boundary | Carry it into delivery or bypass it during repair | Maintain the boundary while finishing legitimate work |
| Earlier tests, diagnoses, or measurements | Treat them as authority after their basis changes | Recheck validity rather than reuse apparent success |
| A provisional mistake or partial side effect | Compound it through dependent later actions | Inspect accumulated state before trusting or retrying it |
| Original goal across revisions and interruptions | Substitute another goal or lose a commitment | Continue useful work toward the still-applicable request |
| Discoveries and local artifacts at handoff | Lose facts, omit files, or leave no usable report | Transfer the information and state needed by the recipient |

Source: the project's [20 symptom classes](SYMPTOMS.md) and the maintainer's review of the release and cleanup reference suites. These are search directions, not a claim that every example is caused by duration.

## Decide relevance separately from evidence level

First confirm an observable failure against a still-applicable requirement.
Legitimate reprioritization, a justified revised conclusion, and an honest
blocked report are not failures by themselves. Keep such leads as rejected
with the reason; mark temporal relevance not applicable rather than forcing
them into a failure category.

Record one of these relevance decisions in each incident account and the collection report:

- **Temporal candidate:** the available sequence supports a plausible dependency on earlier work or state. Identify the anchors, competing explanation, and what remains untested. This does not mean causation is established.
- **Evidence needed:** the earlier obligation, later action, scope, or consequence is too incomplete or ambiguous to establish that dependency. Name the missing evidence and a specific next step.
- **Short control:** the supported error is mainly local, or the current record shows no relevant earlier-work dependency. Retain it in the inventory and, when useful, as a separately reported reliability test.

For a temporal candidate, also state whether the original evidence shows
substantial intervening work, only a short mechanism, or unknown exposure.
Describe the work; do not infer it from elapsed time. A two-turn retry after
partial submission can demonstrate compounding state, but it is not an
observed long-running failure. Report such short temporal candidates
separately and prioritize those with documented extended work. Do not add
filler stages to promote them.

Also assess the **current reproduction** independently: faithful enough for a pilot, needs redesign, short mechanism demonstration, or not built. A strong historical candidate may have a poor task. A short task can have a good behavioral checker. Neither should change the original incident's classification automatically.

Keep these judgments separate from the existing contribution statuses: incident, packaged, model reproduced, and temporal evidence supported. Do not relabel a packaged case as causally supported because its checker works. Do not require a contributor to run a controlled experiment before submitting a credible historical lead.

## Minimum account for a primary candidate

Complete [the temporal review form](../templates/temporal-review.md) in the private incident record. Put a reviewed version in the problem account or a linked evidence document before submission. Every answer needs an anchor or an explicit unknown; unknown fields are acceptable in an evidence-needed report.

1. **Original goal and consequence:** what still-applicable requirement failed, why it mattered, and whether the damage persisted after correction.
2. **Earlier anchor and later action:** the actual instruction, artifact, discovery, or action that connects them. Distinguish a correct baseline from an earlier mistake being propagated.
3. **Intervening work:** concrete tasks and state transitions. Separate the span before the target error, the whole session, idle time, and recovery. If studying propagation, define the later consequence and measure that separate interval.
4. **Information at the decision:** what was in context, automatically loaded, discoverable, unavailable, or actually read. Do not invent forgetting or a reset from a wrong answer alone.
5. **Natural pressure toward the mistake:** a nearby conflicting example, stale successful artifact, similar task with different scope, compatible teammate change, accumulated partial action, or another evidenced demand. Do not invent a trap absent from the history.
6. **Alternative explanation:** local skill gap, ambiguity, bad setup, external change, missing authority, or insufficient budget. State what would distinguish it from the proposed temporal mechanism.
7. **Reduction and comparison:** what must survive minimization, what is removed, and a feasible comparison that would change the inference. If no reproduction or evaluation exists, say so.

Missing causal results limit the claim; they do not justify inventing results or rejecting the entire lead. A consequential error with no temporal connection belongs in the short-control inventory rather than the primary long-running count.

## Reject reductions that remove the decision we want to study

Before calling a task ready for a pilot, ask:

- **Could the final message and fixture solve it without the earlier stages?** If so, explain what dependency remains. A static state-reconciliation test can be useful, but it does not test retaining history merely because setup has two stages.
- **Did minimization supply the diagnosis?** Do not automatically reveal the live job query, correct file path, model-to-metric join, stale-note correction, or missing validation that the original agent needed to discover. Keep legitimate specifications and accessible remedies.
- **Does the agent actually perform the relevant work?** Judge executed jobs, loaded inputs, file changes, data provenance, or claims against trusted observations. A decision file is appropriate only when making that decision is the real task; self-reported action flags cannot establish that an action ran.
- **Does the earlier action affect the later state?** Keep the agent's actual implementation, note, artifact, or side effect. Do not overwrite it with a fixed final fixture and call the sequence an agent-created trajectory.
- **Is the later request natural?** Preserve ordinary feature work, continuation, refactoring, reporting, or handoff. “Find and fix this exact failure” tests diagnosis after disclosure, not the original temptation to make it.
- **Is a correct path feasible and permitted?** No secret requirement, forced permission violation, incompatible teammate edit, impossible deadline, or manufactured ambiguity. Honest blocked delivery is acceptable where it was acceptable originally.

Minimize infrastructure and sensitive data, not the dependency or competing demands. If those demands cannot be reconstructed faithfully, retain the historical account and mark the task as a limited mechanism demonstration. Do not keep making prompts more misleading until an agent fails.

Discoverable repository evidence is desirable. Its availability does not
disqualify a task: some failures concern accumulated artifact state rather
than conversational memory. Explain how the earlier work created that state,
what the later agent must reconcile, and which comparison tests that claim.

## Evaluation evidence and limitations

Scripted correct and faulty controls check the environment and judge. Fresh blind agent attempts test whether the reduction elicits the behavior. Multiple attempts under a predeclared plan are needed to estimate error rates; keep every hit, miss, repair, and exclusion.

To test the role of extended work, compare natural intervening work with a shorter condition while keeping the final task, available evidence, tools, and final-task resources comparable. Distinguish this from experiments that change memory content, session reset, reminders, or environmental drift. Those can test useful mechanisms, but do not isolate duration.

A fresh agent given the same accumulated workspace tests dependence on conversational history versus artifacts. Removing the workspace state tests a different question. A control that gives the correct answer changes task difficulty; it is not a clean history comparison. Name all material differences and limit the conclusion accordingly.

Declare model/settings when exposed, task and judge versions, run count or stopping rule, budgets, comparison, and exclusion rules before inspecting outcomes. Enforce tool and time limits in the runner; log deviations and retain affected attempts. Do not silently subtract evaluator delays or replace unsuccessful attempts. No causal claim follows automatically from a single pair.

Request existing evaluation artifacts when a contributor claims reproduction: all attempts, visible action traces, exact prompts and tool definitions, starting and delivered state, authoritative checks, exclusions, repairs, and comparison results. If unavailable, record **not run** or the specific gap. Do not request hidden model reasoning.

## Next steps for collectors and reviewers

Search the whole authorized history and retain all candidates. Prioritize faithful reproductions of temporal candidates; preserve short controls and uncertain leads with separate counts. Report both original relevance and task readiness. Use the [submission guide](SUBMITTING.md) for the exact file contract and [reproduction guide](REPRODUCING.md) for execution details.

## Sources

- [Symptom search and evidence requirements](SYMPTOMS.md).
- [Evidence collection](EVIDENCE.md), [task design](REPRODUCING.md), and [submission requirements](SUBMITTING.md).
- [Temporal review form](../templates/temporal-review.md), used alongside the detailed incident record.
