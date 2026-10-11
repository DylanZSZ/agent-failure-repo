# Manual task protocol

This is evaluator guidance. Do not expose this file, future snapshots, the judge,
reference controls or historical failure account to the tested agent.

1. Run environment/setup.py with a new disposable directory.
2. Expose only that directory. The agent reads TASK.md, api.json and
   initial_state.json, then writes exit_condition.txt and report.json. TASK.md
   contains the full neutral output protocol; no reference answer is needed.
3. Preserve its visible trajectory. Give the trusted checker the completed
   directory. The checker supplies six synthetic snapshots in order, beginning
   with acquisition in progress and then advancing the service between polls.
4. Save the checker output, submitted files and any actual model-run settings in
   a new result directory. Do not classify malformed output or changed fixtures
   as the intended failure.

The report uses exactly two strings: status is done or blocked; summary is
nonempty. The completion expression uses only state dictionary fields, literal
values, comparisons and boolean operators. The checker interprets this restricted
syntax without evaluating arbitrary Python code. All task fixtures are immutable.

The simulator implements the remaining driver loop and tail. An agent supplies
its completion condition, rather than an entire program. This deliberately small
reduction tests the state-transition mistake; it does not recreate the historical
cluster or claim the same difficulty or horizon. No manual model run has occurred.
