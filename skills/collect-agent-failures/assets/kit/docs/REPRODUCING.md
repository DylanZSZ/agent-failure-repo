# Build a faithful task without removing the temporal mechanism

Updated 2026-10-13.

## Summary

A reproduction should let a new agent face the decision that produced the original failure. Begin private task construction after the first three [admission gates](LONG_HORIZON.md#four-gates-for-new-submissions) pass. These establish the violation, relevant mechanism, and auditable evidence. Clean execution and checker verification then satisfy the fourth gate. Preserve the earlier event and later decision; an already broken fixture only demonstrates a bug.

Apply [the temporal criteria and reduction checks](LONG_HORIZON.md) first.
Minimize infrastructure and private data, not the dependency or legitimate
competing demands. A long task may need to remain long. If only a short
mechanism survives, state that limitation instead of calling it a reproduction
of extended exposure. Keep ordinary local bugs and unsupported leads in the
private inventory. A short coordination failure can qualify on multi-agent
evidence; it must not be described as evidence of long duration.

## Account for the whole collection

Use the [incident index](../templates/incident-index.csv) to track each distinct candidate and the [collection report](../templates/collection-report.md) to track overall coverage. Begin with the [history search](FINDING_FAILURES.md) and [all symptom classes](SYMPTOMS.md). Feasibility can determine work order, but it should not silently determine which incidents appear in the report.

For each candidate, record selection or deferral and the reason. Selected new
submissions need a runnable package with the clean-environment checks below.
An incident-only account remains a local draft when evidence or reproduction is
incomplete. Link every actual attempt from the index. Do not fabricate
reproductions to satisfy completeness; unavailable dependencies or restricted
sources justify deferral. An unavailable model prevents a fresh agent attempt,
but need not prevent building and checking a faithful package.

## Keep the temporal mechanism

Write the sequence before implementing the environment:

1. Establish the relevant rule, completed behavior, discovery, ownership boundary, or initial mistake whose propagation is being studied.
2. Include the intervening work or state change that might make it hard to retain or apply.
3. Continue the existing work or give a natural later request that creates an opportunity for the error.
4. Check whether the setup was valid, the agent reached that opportunity, the user's task was completed, and the intended error occurred.

For example, to study a rule lost after a session reset, first let the agent complete work under that rule. Keep the durable reminder available in the same way it was available originally. Then reset the conversation and give the next task. Starting with “ignore the old rule” or handing the agent a broken implementation would change the question.

Remove unrelated dependencies, data, and setup. Keep details that could explain the failure, including an accessible reminder, conflicting local examples, a teammate's edit, the correct stopping option, or the originally available budget. Document every material change from the original incident. If a reduction removes the long span, explain what temporal claim remains testable.

The earlier agent action should affect the later workspace, memory, or external
state. Do not replace it with the same final fixture regardless of what the
agent did. Before a pilot, complete [the temporal review](../templates/temporal-review.md),
including whether the final prompt and fixture make earlier stages unnecessary.
Keep the legitimate requirement clear while leaving its discovery or application
to the agent. Supplying a resolved status query or explicit repair removes the
decision that many historical incidents need.

For error propagation, distinguish the origin of the first mistake from its
later amplification. A seeded defect can test whether subsequent work detects,
repairs, or compounds it; it cannot show that long-running created that defect.
Similarly, fixing current code while leaving earlier delivered data stale is
a separate outcome from fixing neither. Check the older artifact's downstream
consumer when that is the proposed mechanism.

## Package the task

Create a starter with `python3 commands/new_problem.py <slug>`. Document the following in the problem's description and metadata:

- A short account of the original incident, its evidence, and what can be shared.
- The intended failure, its concrete consequence, and the reason earlier work may matter.
- The exact starting state, pinned software versions or image digest, prerequisites, environment variables, and any network needs; identify versions not recoverable from the history.
- The sequence of prompts, session resets, teammate changes, and context carried between stages.
- Exact commands for setup, task execution, checking, reset, and cleanup; state what each creates or changes.
- The agent-visible files and instructions, with checks and reference material kept outside that workspace.
- An executable correct reference or another runnable demonstration that the requested task can be completed, plus a deliberately faulty case for testing the checker.
- The proposed comparison, known limitations, and the strongest evidence level currently supported.

Put requests in `task/`, local setup and fixtures in `environment/`, checks in `checks/`, and the correct implementation or walkthrough in `reference/`. Shared repository commands belong in `commands/`; commands specific to one task belong with that task. The repository does not supply a universal model runner: document the exact adapter or manual procedure, and distinguish planned execution from what you actually ran.

Define visibility separately for every stage. Present only the current stage's permitted message and files, plus the history or memory that should carry forward. Future requests, reset schedules, and simulated teammate changes are evaluator instructions. Keep them outside the evaluated workspace rather than copying the entire `task/` directory into it.

### Specify multi-agent order and visibility

Use this table in the existing problem readme when multiple actors matter.
Define observable transitions, not just an instruction to “run two agents.”
Write the planned schedule before a run and record actual order and receipts
for attempts that occurred; leave unperformed model attempts marked not run.

| Stage and release condition | Actor/session | Visible messages and file versions | Shared state or isolated copy | Action and output | Evidence the next actor received it |
| --- | --- | --- | --- | --- | --- |
| Example: resume B after A commits a compatible addition and its check passes | B, resumed session | B's retained conversation and the updated shared file | Shared checkout | Continue B's existing task | Commit ID, actual read, and tool result |

For each actor, label the execution as a **live agent**, **historical replay**,
or **scripted teammate change**. A scripted change can recreate a documented
collaboration condition; it is not a fresh multi-agent result. Keep per-actor
prompts, roles, histories, permissions, and action records. State which messages
are merely discoverable and which were actually delivered or read.

For a known ordering, use an observable barrier such as a committed artifact or
completed check. If concurrency itself matters, document the scheduler or
interleaving rule and record the order that occurred. A sleep interval alone
does not establish which file version an actor saw. Do not wait for the target
mistake and then choose a favorable schedule after the fact.

Preserve ownership rules and show that both legitimate tasks could succeed, or
describe the allowed conflict-resolution path. If a live teammate does not
produce the necessary state, record the absent opportunity. Do not silently
substitute a scripted contribution or overwrite the agent's actual work.

### Meet the clean-environment contract

Another contributor must be able to use only the submitted revision and declared
dependencies. The procedure must not depend on the author's transcript store,
private checkout, laptop cache, undeclared fixture, or live private service.
Write one command or a short exact command sequence in the existing problem
readme, with working directories, inputs, expected output artifacts, and exit-code
meaning for each operation:

| Operation | Required evidence |
| --- | --- |
| Setup from a new disposable workspace | Complete starting files, declared dependencies, and a check that the required baseline exists |
| Execute the staged task | Exact adapter invocation or manual agent procedure, current-stage inputs, transition conditions, and where actions and delivered artifacts are saved |
| Judge the delivered state | Independent task and target-failure outcomes, including invalid or unjudgeable cases |
| Check the judge | Correct reference accepted; intended faulty behavior detected; unrelated error and invalid setup not mislabeled as target hits |
| Reset and cleanup | A new attempt does not inherit a previous attempt's conversation, files, service state, or receipts unless the declared design requires it |

Run setup, reference/checker controls, and reset from a clean copy of the proposed
submitted files. Save the actual commands, outputs, exit codes, and tested
revision. Inspect that copy for missing ignored or untracked inputs. A fresh
model run is optional for a packaged submission; its execution procedure must
still be complete. Mark unperformed model or causal comparisons **not run**.
If the mandatory clean checks cannot run, the case remains a local draft.

Use disposable directories, fake identities, and local mock services. Do not mount real credentials, personal histories, or unrelated source trees into an agent workspace. Keep model-provider credentials with the trusted caller rather than exposing them to the tested agent. Run both the task and the evaluator with limited permissions; a check that imports task code can execute it.

## Define two separate checks

**Task check:** did the delivered work satisfy the user's request? Prefer observable behavior, a clean-checkout test, or another independent acceptance check. A model saying “done” is not task completion.

**Failure check:** did the specified erroneous action occur? Define the exact evidence required. For “calls its own regression pre-existing,” require evidence that the test passed initially, the agent caused the later failure, and its report assigned the wrong origin. A failed final test alone is insufficient.

Prefer observed actions and effects over self-reported flags or exact answer
dictionaries. Accept behaviorally equivalent correct solutions. Capture first
wrong action, any correction, and final delivery separately; recovery does not
erase an action, but an intermediate error is not automatically a failed final
delivery. Protect action receipts from agent modification where they determine
the result.

Record preconditions such as a correct earlier implementation, a successful teammate change, and a visible reminder. Record arrival at the later decision separately using the result form:

- `preconditions_met` — whether the required starting conditions were established.
- `failure_opportunity_reached` — whether the agent reached the situation in which the intended mistake could occur.

Fill both from evidence, using null for unknown, rather than inferring them from the final answer. Use explicit outcomes:

- **Hit:** a valid, judgeable attempt meets the failure rule.
- **Miss:** a valid, judgeable attempt reaches the opportunity and does not meet it.
- **Invalid or unjudgeable:** a prerequisite fails, the agent never reaches the opportunity, evidence is missing, or the checker cannot decide.

Keep task success separate from these outcomes. An agent can fail the task without exhibiting the target failure, or finish the requested feature while deleting someone else's work.

A broken runner, missing setup dependency, or infrastructure crash can make an attempt invalid or unjudgeable. An agent-caused product crash is different: it can be the specified failure if the preconditions, opportunity, and evidence satisfy the declared rule. Do not exclude crashes categorically or count every crash as a hit.

Check the checker against a correct reference and a deliberately faulty version. Label those as checker tests; neither is a model reproduction. If text judgment is needed, record the rubric, evaluator, and uncertainty rather than disguising a subjective decision as an objective test.

## Separate kinds of evidence

| Evidence | What actually happened |
|---|---|
| Original incident | An authorized historical record shows the observed failure |
| Historical reconstruction or scripted replay | Source-anchored states or recorded actions were recreated to check their effects; substitutions and gaps are declared |
| Deliberately faulty version | A human or script inserted the suspected defect |
| Fresh model attempt | A model received the task and chose its own actions |
| Causal comparison | Fresh attempts differ in a declared history, context, or coordination condition; remaining differences are assessed |

A reconstruction or replay helps verify a consequence; it does not recreate an
unrecorded model decision. A faulty version helps test a checker. Only a fresh
model attempt can show the model making the mistake again. A fresh hit alone
does not show that duration or coordination caused it. Synthetic teaching
examples must remain labeled synthetic and must not enter crowdsourced failure counts.

## Evaluate the explanation, when feasible

Start with a fresh model attempt. Predeclare the conditions, model settings, number of attempts or stopping rule, and judging rule before examining outcomes. Preserve every attempt, including timeouts and service errors. Keep model name, version if available, prompts, tool definitions, context handling, budget, and actual observed run length in the run record.

Enforce declared time and tool limits in the runner and record deviations.
Do not revise exclusions, subtract delays, or restart to replace an inconvenient
attempt after seeing it. Lack of an automated runner does not justify claiming
an unperformed evaluation.

Then change one plausible cause while keeping the final task and its difficulty as comparable as possible. Options include removing the intervening work, keeping the session continuous, replacing stale notes with current ones, or restoring an earlier reminder. Explain what else that change affects. If the control hands over the solution or makes the final task easier, it cannot isolate the effect of a long history.

Name the factor being tested. Duration, session reset, stale memory, environment
change, and an explicit reminder are different interventions. A fresh agent
with the same accumulated artifacts is useful for testing conversational carryover;
removing those artifacts changes the state dependency too. Preserve the final
task's resources and relevant available facts as far as possible.

For multi-agent cases, serializing edits, changing handoff visibility, replacing
a live teammate with a script, and removing shared state test different factors.
Name the intervention and record the actual schedule and state each actor saw.
Do not describe a coordination comparison as isolating long duration.

Use multiple attempts when estimating rates. Match seeds when the provider supports them, but do not assume a shared seed makes two runs identical. Report the hit count and eligible denominator for each condition, plus all excluded attempts and reasons. State the main limitation: a single matching pair supports a case study; it does not establish a reliable causal effect.

Save sanitized evidence and `summary.json` in `results/<slug>/<run-id>/`. Retain the original record when adding a later review. If no model evaluation was run, say “not run” and list what is needed. Do not substitute checker tests or synthetic transcripts for unavailable model results. Return to the incident index after each package or evaluation and update the remaining work for that incident.

## Validate before owner review

Run `python3 commands/validate.py` to check the submission structure. It does not
check scientific eligibility or reproducibility. Apply the clean-environment
contract above and link its actual records. Reconcile each candidate with a
selected package or a local deferral reason and next action. Finish with
[the owner review](REVIEW.md) before uploading selected material.

Source: [Evidence levels](../CONTRIBUTING.md), [finding the temporal mechanism](FINDING_FAILURES.md), and [agent operating rules](../AGENTS.md).
