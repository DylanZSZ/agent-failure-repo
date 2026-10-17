# Submit failures that depend on earlier work or agent interaction

Updated 2026-10-13.

## Summary

Our goal is to find failures to which extended work, context transitions, or multi-agent interaction materially contributed. Search the full authorized history and keep a private inventory of leads, but submit only cases that pass all four gates below. A bug appearing late in a transcript, or in a task delegated to a subagent, is not enough. Zero qualifying submissions is a valid outcome.

Read this guide before choosing which incidents to reproduce. Use the [symptom catalog](SYMPTOMS.md) to find observable errors; use the criteria here to decide whether they fit the research question. A symptom label, a large token count, a runnable task, or a checker rejecting a planted defect cannot establish a long-running failure.

## The sequence we want

A useful candidate has a traceable sequence:

1. **Something earlier matters.** A requirement, discovery, completed implementation, scoped convention, commitment, ownership boundary, or provisional assumption is established. An earlier mistake can also matter when the target is its later propagation.
2. **Real work changes the situation.** Features accumulate, artifacts evolve, another task competes for attention, a teammate edits the workspace, context is compressed, or work crosses a session or project boundary. Identify the actual work or transition.
3. **A later decision tests continuity.** During the same ongoing request, or a legitimate follow-up request, the agent must retain, rediscover, update, revoke, correctly scope, or verify something from that earlier work. State what an acceptable action would be with the information and tools available then.
4. **An observable action mishandles it.** Identify the first wrong action, its effect, any repair, and the delivered outcome separately. A plausible causal explanation still needs testing.

Explain the dependency in one sentence: “After doing ___, the agent encountered ___; it needed to carry forward or revise ___, but instead ___.” Fill this from evidence. If the missing part is only a guess, keep it as an evidence-needed lead.

There is no universal minimum turn count. A brief coordination failure can qualify when actual interaction between actors contributed; do not call it a duration effect. A short reproduction can preserve a mechanism supported by an extended historical sequence, but does not measure extended exposure. Long idle waits, simulator ticks, repeated “continue” messages, and difficult debugging after the error do not by themselves establish a long-running cause.

## Four gates for new submissions

All four gates must pass before a new case belongs in the public submission. After the first three evidence gates pass, build and verify the reconstruction privately to satisfy gate 4. Record the decision and evidence in the [temporal review](../templates/temporal-review.md); no new manifest fields are needed.

1. **An actual violation.** Identify a still-applicable requirement, an executed action or delivered state, and an observed violation with a concrete consequence or explicit failure predicate. Include contrary evidence and later repair.

   Keep an ambiguous case local as **needs evidence**; reject a demonstrated non-failure.

2. **A material contribution from extended work, a context transition, or agent interaction.** Anchor the earlier and later events, identify the state or information connecting them, and explain how the work or interaction contributed. Address the strongest local-error alternative and identify a feasible comparison.

   Keep a missing dependency local as **needs evidence**. An ordinary local bug is **out of scope**, even in a long or multi-agent run.

3. **An auditable evidence chain.** Provide sanitized source excerpts, relevant instructions, tool results, before/after state, event order, and actor visibility sufficient for another person to check gates 1 and 2. Label reconstruction, inference, omissions, and recovery.

   Keep the case local as **needs evidence** if essential links are missing or cannot be shared. A polished narrative cannot replace them.

4. **A faithful runnable reconstruction.** Provide clean setup, staged tasks, exact commands, dependencies, independent task and failure checks, and a feasible correct path. Run the documented commands in a fresh disposable environment. Record a passing correct control and a deliberately faulty control detected by the checker. Check valid alternatives and preserve the mechanism.

   Keep the case local as **needs reconstruction** until the task and checks work. A plan or already broken final fixture is insufficient.

Gate 2 requires a narrow, source-supported mechanism, not a claim about an agent's hidden reasoning. For example, a colleague's compatible addition was present before another agent rewrote the file, and the rewrite removed it. That can support a lost-work interaction without establishing that multiple agents generally raise error rates. Mere sequence—“a long run, then a bug”—does not establish material contribution. Missing model revision or exact token count can remain unknown; missing essential instruction, action, state, or interaction evidence cannot pass the relevant gate.

Fresh blind model attempts and controlled comparisons are valuable but are **not mandatory for packaged submission**. The checker controls establish that the task is runnable and its checker distinguishes the declared outcomes. They do not demonstrate a fresh model failure or establish a causal effect. State which stronger tests have not run, what comparison would distinguish the proposed mechanism from alternatives, and what that comparison could actually establish.

For multi-agent cases, reconstruct each actor's assignment, session, base revision, shared or isolated workspace, messages, relevant reads and writes, commits or merges, and the resulting delivered state. Identify what each actor could see at the decision and what it actually read. Preserve observed order; do not infer concurrency from unordered timestamps or assume isolated worktrees share uncommitted changes. Show a permitted way to satisfy the compatible assignments. A delegated syntax error does not qualify without evidence that coordination contributed.

The complete lead inventory stays private. Preserve ordinary errors, duplicates, rejected cases, and missing-evidence leads there with reasons and next actions; do not package them for public submission by default. The public index contains only admitted cases and their actual attempts. Existing incident-only records remain valid historical records; apply a dated review rather than deleting or rewriting them.

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

## Record relevance, admission, and evidence separately

First confirm an observable failure against a still-applicable requirement.
Legitimate reprioritization, a justified revised conclusion, and an honest
blocked report are not failures by themselves. Keep such leads as rejected
with the reason; mark temporal relevance not applicable rather than forcing
them into a failure category.

Retain the following relevance labels for the private inventory and legacy records. A relevance label alone does not pass the submission gates:

- **Temporal candidate:** the available sequence supports a plausible dependency on earlier work or state. Identify the anchors, competing explanation, and what remains untested. This does not mean causation is established.
- **Evidence needed:** the earlier obligation, later action, scope, or consequence is too incomplete or ambiguous to establish that dependency. Name the missing evidence and a specific next step.
- **Short control:** the supported error is mainly local, or the current record shows no relevant earlier-work dependency. Retain it privately as out of scope for this collection. Do not submit it as an independent problem merely because its checker is useful.

For a temporal candidate, also state whether the original evidence shows
substantial intervening work, only a short mechanism, or unknown exposure.
Describe the work; do not infer it from elapsed time. A two-turn retry after
partial submission can demonstrate compounding state, but it is not an
observed long-running failure. Without a supported context-transition or actual
multi-agent mechanism, it remains a local lead outside the submission target.
Do not add filler stages to promote it. A qualifying coordination case can be
brief; identify that mechanism explicitly and make no duration claim.

Also assess the **current reproduction** independently: faithful enough for a pilot, needs redesign, short mechanism demonstration, or not built. A strong historical candidate may have a poor task. A short task can have a good behavioral checker. Neither should change the original incident's classification automatically.

Keep these judgments separate from the existing contribution statuses: incident, packaged, model reproduced, and temporal evidence supported. The incident status remains available for local drafts and legacy records; new submissions must satisfy the runnable reconstruction gate. Do not relabel a packaged case as causally supported because its checker works. A controlled model experiment is not required to submit a case that passes all four gates.

## Minimum account for a primary candidate

Complete [the temporal review form](../templates/temporal-review.md) in the private incident record. Put a reviewed version in the problem account or a linked evidence document for each admitted submission. Every answer needs an anchor or an explicit unknown. Unknown essential links keep a case in the private evidence-needed inventory; optional metadata may remain unknown in a submitted case.

1. **Original goal and consequence:** what still-applicable requirement failed, why it mattered, and whether the damage persisted after correction.
2. **Earlier anchor and later action:** the actual instruction, artifact, discovery, or action that connects them. Distinguish a correct baseline from an earlier mistake being propagated.
3. **Intervening work:** concrete tasks and state transitions. Separate the span before the target error, the whole session, idle time, and recovery. If studying propagation, define the later consequence and measure that separate interval.
4. **Information at the decision:** what was in context, automatically loaded, discoverable, unavailable, or actually read. Do not invent forgetting or a reset from a wrong answer alone.
5. **Natural pressure toward the mistake:** a nearby conflicting example, stale successful artifact, similar task with different scope, compatible teammate change, accumulated partial action, or another evidenced demand. Do not invent a trap absent from the history.
6. **Alternative explanation:** local skill gap, ambiguity, bad setup, external change, missing authority, or insufficient budget. State what would distinguish it from the proposed temporal mechanism.
7. **Reduction and comparison:** what must survive minimization, what is removed, the clean reconstruction and checker-control results, and a feasible comparison that would change the inference. If fresh model evaluation or a comparison has not run, say so.

Missing controlled causal results limit the claim; they do not justify inventing results. Missing essential historical evidence or a working reconstruction prevents admission, while the lead remains private. A consequential local error without an eligible dependency is out of scope.

## Reject reductions that remove the decision we want to study

Before calling a task ready for a pilot, ask:

- **Could the final message and fixture solve it without the earlier stages?** If so, explain what dependency remains. A static state-reconciliation test can be useful, but it does not test retaining history merely because setup has two stages.
- **Did minimization supply the diagnosis?** Do not automatically reveal the live job query, correct file path, model-to-metric join, stale-note correction, or missing validation that the original agent needed to discover. Keep legitimate specifications and accessible remedies.
- **Does the agent actually perform the relevant work?** Judge executed jobs, loaded inputs, file changes, data provenance, or claims against trusted observations. A decision file is appropriate only when making that decision is the real task; self-reported action flags cannot establish that an action ran.
- **Does the earlier action affect the later state?** Keep the agent's actual implementation, note, artifact, or side effect. Do not overwrite it with a fixed final fixture and call the sequence an agent-created trajectory.
- **Is the later request natural?** Preserve ordinary feature work, continuation, refactoring, reporting, or handoff. “Find and fix this exact failure” tests diagnosis after disclosure, not the original temptation to make it.
- **Is a correct path feasible and permitted?** No secret requirement, forced permission violation, incompatible teammate edit, impossible deadline, or manufactured ambiguity. Honest blocked delivery is acceptable where it was acceptable originally.

Minimize infrastructure and sensitive data, not the dependency or competing demands. If those demands cannot be reconstructed faithfully, retain the historical account privately as needs reconstruction. Do not keep making prompts more misleading until an agent fails.

Discoverable repository evidence is desirable. Its availability does not
disqualify a task: some failures concern accumulated artifact state rather
than conversational memory. Explain how the earlier work created that state,
what the later agent must reconcile, and which comparison tests that claim.

## Evaluation evidence and limitations

Scripted correct and faulty controls check the environment and judge. Fresh blind agent attempts test whether the reduction elicits the behavior. Multiple attempts under a predeclared plan are needed to estimate error rates; keep every hit, miss, repair, and exclusion.

For each attempt, also answer these questions before counting a hit:

- **Did the intended opportunity actually occur?** Record the earlier state the agent really created, the later request it received, and the relevant state when it acted. If it completed a deliberately partial job early, the later partial-state opportunity may no longer exist. Record that early scope violation separately.

- **Was the observed error the intended error?** Name both. A task designed to test forgotten journal state may instead reveal an omitted request or a broken CLI. Preserve the useful unexpected failure without claiming the intended mechanism occurred.

- **Does the check accept valid alternatives?** Test another lawful implementation, extra fields where permitted, equivalent artifact layouts, honest blocked delivery, and a successful run. A reference implementation's private filenames or JSON layout are not requirements unless the task publishes them.

- **What actually reached the next consumer?** Inspect the installed package, loaded implementation, downloaded report, committed files, or durable service effects. A correct working tree or an `active` filename does not establish that the delivered path used it.

- **Did later success repair the earlier damage?** Compare identities and history, not only current totals. A compensating transaction can restore a balance while leaving the original transaction wrong; later authorization can make current state valid without repairing an earlier unauthorized action or historical snapshot.

Keep **actor actions** separate from **product capability**. A consumer that
executes a missed operation on the delivered program can establish that the
program supports it; it cannot establish that the original agent performed it.
Likewise, a cold replay may expose a product bug in a valid state that the
original trajectory never reached. Record both findings and their different
contexts.

Retain successful attempts and corrected mistakes as comparison evidence.
Repeated checks, a large test suite, a temporary wrong thought followed by a
correct action, and waiting for a teammate to finish are not failures by
themselves. For unnecessary work, identify the violated priority, missed
deadline, or demonstrated avoidable cost. State whether a report defect changes
the answer, its interpretation, or only a label; do not imply a larger impact
than the evidence shows.

To test the role of extended work, compare natural intervening work with a shorter condition while keeping the final task, available evidence, tools, and final-task resources comparable. Distinguish this from experiments that change memory content, session reset, reminders, or environmental drift. Those can test useful mechanisms, but do not isolate duration.

A fresh agent given the same accumulated workspace tests dependence on conversational history versus artifacts. Removing the workspace state tests a different question. A control that gives the correct answer changes task difficulty; it is not a clean history comparison. Name all material differences and limit the conclusion accordingly.

Declare model/settings when exposed, task and judge versions, run count or stopping rule, budgets, comparison, and exclusion rules before inspecting outcomes. Enforce tool and time limits in the runner; log deviations and retain affected attempts. Do not silently subtract evaluator delays or replace unsuccessful attempts. No causal claim follows automatically from a single pair.

Request existing evaluation artifacts when a contributor claims reproduction: all attempts, visible action traces, exact prompts and tool definitions, starting and delivered state, authoritative checks, exclusions, repairs, and comparison results. If unavailable, record **not run** or the specific gap. Do not request hidden model reasoning.

## Next steps for collectors and reviewers

Search the whole authorized history and retain all candidates privately. Submit only cases passing the four gates, with their evidence and every actual attempt. Report admitted cases separately from local deferrals and out-of-scope findings; zero admitted cases is valid. Use the [submission guide](SUBMITTING.md) for the exact file contract and [reproduction guide](REPRODUCING.md) for execution details.

## Sources

- [Symptom search and evidence requirements](SYMPTOMS.md).
- [Evidence collection](EVIDENCE.md), [task design](REPRODUCING.md), and [submission requirements](SUBMITTING.md).
- [Temporal review form](../templates/temporal-review.md), used alongside the detailed incident record.
