# Historical evidence and limits

Confirmed local historical incident. These are sanitized investigator summaries,
not reconstructed transcript quotations. The source alias maps to the original
privately. Hidden reasoning and private paths, identifiers and commands are not
included. Owner authorized submission of the prepared file set on 2026-10-11.

The driver was intended to complete acquisition and automatically run the
plan-building and monitoring tail. The original code and later observed stalled
state establish the failure independently of the later admission. The task's
exact original user wording is not reproduced in this selected evidence.

- `claude-phase-source:L7734` (2026-09-03T09:12:00.453Z, assistant tool call): The agent writes a driver whose acquisition loop exits only when terminal_success is at least eight; the downstream plan-building tail follows the loop.
- `claude-phase-source:L7738` (2026-09-03T09:12:10.868Z, assistant tool call): The agent issues the launch command for that driver. This anchor is a command, not proof of successful startup by itself.
- `claude-phase-source:L7807` (2026-09-03T09:31:00.244Z, tool result): Live inspection shows the driver session, qualification already bound, acquisition successes zero, and the downstream plan not yet built.
- `claude-phase-source:L7810` (2026-09-03T09:32:06.467Z, assistant): The agent identifies the counter reset and diagnoses continued waiting in the acquisition loop.
- `claude-phase-source:L7811` (2026-09-03T09:32:16.920Z, assistant tool call): The agent writes a stop-and-inspect script. This is a prepared action; this anchor alone does not prove that it executed.
- `claude-phase-source:L7959` (2026-09-03T09:48:12.077Z, assistant): The agent announces a repair that uses the persistent qualification-stage binding.
- `claude-phase-source:L7960` (2026-09-03T09:48:21.910Z, assistant tool call): The agent writes the revised tail generator; this anchor is not the revised completion-condition implementation itself.
- `claude-phase-source:L7980` (2026-09-03T09:49:11.038Z, assistant): The agent reports the repaired driver running. This is a reported recovery, not proof that the downstream plan or training completed.

The measured interval is L7734 to L7807: 1,139.791 seconds, with 11 distinct
visible assistant message IDs and nine tool-use blocks strictly between those
endpoints, one source session. Wall time includes waiting and is not active work.
These counts were established in the root incident review; this package preserves
them rather than inferring duration from transcript length.

Consequence: the plan tail had not run when the later state was inspected. The
extra delay attributable to this bug is unknown. Repair was announced and the
replacement driver was reported running, but final downstream completion is not
proven by these anchors. A short state-machine error is a sufficient alternative
to memory loss or long-horizon degradation.

The local reduction uses fake identifiers and bounded in-memory snapshots. It
compresses the observed time span and supplies the loop machinery. All recorded
controls are scripted checks, not fresh model runs or causal comparisons.
