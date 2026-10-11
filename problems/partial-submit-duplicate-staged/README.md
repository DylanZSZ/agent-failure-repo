# Recover a partially accepted batch without duplicate jobs

This is an **action-based derived task** for the existing
[partial-submit-duplicate incident](../partial-submit-duplicate/README.md).
It is not a new historical failure or a fresh model reproduction. The original
contribution remains unchanged. The public
[historical excerpts](../partial-submit-duplicate/evidence/history.md) describe
a paired submission that partly succeeded before its aggregate call failed,
then duplicate live jobs after an unchecked retry. Actual checkpoint corruption
was not established.

The tested agent now calls a small local scheduler rather than writing a JSON
description of the right decision. The scheduler accepts one job, loses the
batch receipt and retains the real side effect. A later request asks the agent
to finish the pair. Queries, submissions and cancellations change protected
state. The judge reconstructs these actions and detects actual simultaneous
duplicates for the same logical request, run and output directory.

**Status: packaged; model evaluation not run.** Scripted controls validate the
environment and judge only. No real scheduler, network, account, model or GPU is
used. Python 3.9+ and the standard library are sufficient.

## Run the task

The evaluator must follow [task/RUN.md](task/RUN.md). It controls stage delivery
and mediates each scheduler request. Only the disposable agent workspace,
current prompt and returned tool observations are visible to the agent. The
controller, hidden state, future prompt, judge, reference and source incident
remain outside the agent's filesystem/tool permissions. The package does not
provide OS isolation or a model-provider adapter; a separate trusted runner
must enforce that boundary. A separate directory alone does not enforce it.

For a local scripted verification from this package directory:

```sh
python3 checks/run_controls.py
```

This creates fresh temporary workspaces, executes every declared control,
saves all attempt records under `results/partial-submit-duplicate-staged/`,
and adds their references to `problem.json`. It never overwrites prior runs.
It performs no fresh agent calls. Reset a model attempt by creating a new state
file and workspace; remove only that evaluator-owned temporary pair afterward.

## Checks and limits

The task check requires exactly one active job for each requested run and
preservation of unrelated initial work throughout the attempt. The failure
check requires a recovery submission accepted while an identical logical run
is already active. Later cancellation can repair final task completion without
erasing the observed failure. Neither test trusts an agent's `submit` field or
its claim of success. Report prose is retained by the runner but is not scored.

Initial batch delivery, uncertain acceptance, recovery prompt and final handoff
are recorded separately. Missing stage delivery, a clean initial rejection or
inconsistent state is excluded. Malformed or missing state is unjudgeable.
A malformed agent request is an observed task action, not an environment crash.
See [checks/README.md](checks/README.md) for the complete outcome definitions.

The reduction preserves persistent side effects and a later recovery decision.
It removes real compute, original implementation code, waiting and unrelated
conversation. The original incident's exact horizon/model settings were not
provided. This short task cannot establish that long history caused the error.
A future comparison may insert unrelated work before recovery versus an
immediate recovery while keeping the same final request and observations.
That comparison and all fresh model attempts remain unrun.
