# Local state and operations

`controller.py` is trusted evaluator code. Setup creates the public request and
tool files in a new workspace and a separate private state file. The scheduler
has one unrelated running job. Requested alpha/beta jobs have separate logical
run IDs and output directories. No process or network job is launched.

The first complete batch in stage 1 returns an aggregate error. In the main
condition its first request is accepted and running; the response omits its ID.
In the clean-reject control neither request is accepted. Query is authoritative.
After the recovery prompt, each accepted submission creates a distinct job and
cancellation changes that exact job's state. There is no silent deduplication.

The controller validates and atomically updates its event ledger after each
operation. Run one evaluator process at a time for a state file; concurrent
controller writers are unsupported. Keep the private state directory outside
the agent's tool/filesystem permissions. Restrict network and host credentials
in the separate runner; this package itself does not implement that isolation.
