# Evaluator-owned environment

`harness.py` seeds fake data, advances one stage at a time and serves a local
Unix-socket trainer. It reads the requested files itself, verifies that each
record belongs to the synthetic dataset, records selected/consumed row IDs
outside the workspace, and reports ordinary counts to the client.

Only files in `seed/` are copied initially, plus initial synthetic data and
the runtime socket location. The agent authors `launch.py`. Protected inputs
are hashed before each launch and stage transition and again at judgment.
For a fresh model, use the required read-only mounts and restricted adapter
in [RUN.md](../task/RUN.md); hash checks are not a substitute for isolation.

Valid copied staging selections are accepted. The broker permits only small
regular input files resolved inside the disposable workspace and exact
synthetic rows. It never imports or executes the agent's launcher. The agent
executes that launcher through its restricted task tools.

