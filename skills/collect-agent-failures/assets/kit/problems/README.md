# One problem directory per selected failure

Apply [the admission requirements](../docs/LONG_HORIZON.md) before proposing a
submission. Once a case has auditable evidence of a failure contributed to by
earlier work or agent interaction, create its draft in the private collection
with `python3 commands/new_problem.py your-short-name`. Submit only after its
faithful task works from a clean copy and the checker controls pass. Ordinary
bugs, evidence gaps, and unrunnable drafts stay local. Never fabricate a run.

Each package contains:

```text
your-short-name/
  README.md        # incident, meaning, horizon, reduction, limits
  problem.json     # small machine-readable record and commands
  evidence/        # reviewed historical excerpts, state, and check receipts
  task/            # ordered messages and handoff instructions for the agent
  environment/     # initial files and local fixtures
  checks/          # reviewer-owned checks and outcome definitions
  reference/       # one correct solution and, optionally, a known bad fixture
```

The evaluated agent must not receive the reviewer files. Document exactly
which files and messages it receives at each stage, what persists, and how
sessions or compaction are handled. Follow [the reproduction guide](../docs/REPRODUCING.md).

Newly initialized collection kits contain no incidents. Existing repository
contributions remain available with their dated assessments; their presence
does not certify admission under the current requirements.

See [what to push](../docs/SUBMITTING.md) for submission requirements,
collection summaries, evaluation records, and private files to exclude.
