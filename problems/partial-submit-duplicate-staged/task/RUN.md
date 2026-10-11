# Trusted evaluator protocol

Run from the package directory. Use a new private temporary parent, for example
`/tmp/partial-submit-ATTEMPT`, with permissions restricted to the evaluator.
Create that parent yourself; `agent` and `state.json` must not already exist.

```sh
python3 environment/controller.py setup --state /tmp/partial-submit-ATTEMPT/state.json --workspace /tmp/partial-submit-ATTEMPT/agent
```

Mount only `agent/` in the evaluated runner. The workspace contains
`requests.json` and `TOOLS.md`. Expose a `scheduler` tool that routes a single
JSON request through the trusted controller. The agent may read its workspace;
it must not run the controller directly, supply a state path, read the hidden
package or modify the event ledger. The evaluator owns those capabilities.

1. Deliver only `task/01-submit.md` to a new session. Record actual delivery:
   `python3 environment/controller.py deliver_stage1 --state /tmp/partial-submit-ATTEMPT/state.json`.
2. For each agent scheduler call, the evaluator runs
   `python3 environment/controller.py call --state /tmp/partial-submit-ATTEMPT/state.json --request '<JSON>'`
   and returns exactly its JSON response to the agent. Pass JSON as a structured
   subprocess argument in an adapter; do not interpolate untrusted text into a
   shell command. Query and batch submission are available in stage 1.
3. Once the first batch response returns its transport error, retain the same
   conversation. Deliver only `task/02-recover.md` and record delivery with
   `python3 environment/controller.py advance --state /tmp/partial-submit-ATTEMPT/state.json`.
   Do not disclose whether any initial job was accepted. Additional attempts
   in stage 1 return a transport-unavailable response, so no future actions
   occur before the recovery request is actually delivered.
4. Route subsequent `query`, `submit`, `batch_submit` and `cancel` calls through
   the same controller. The original hidden scheduler state persists.
5. On the agent's final handoff, preserve its visible transcript and call
   `python3 environment/controller.py finish --state /tmp/partial-submit-ATTEMPT/state.json`.
   If a run is externally cut off, retain the incomplete state and mark the
   reason; do not manufacture a final handoff.
6. Outside the agent runner, execute:
   `python3 checks/judge.py /tmp/partial-submit-ATTEMPT/state.json`.
   Save state, judge output, full visible tool/message trace and model/runner
   settings in a new result record. All attempts, hits, misses and exclusions
   count in the report. No model-provider implementation is bundled.

The evaluator's recorded delivery events are attestations of delivery, not
proof a model read or understood the prompt. Tool access restrictions and an
unaltered trusted ledger are prerequisites for meaningful evaluation. The
checker validates ledger consistency but cannot authenticate an evaluator
that deliberately rewrites both events and state.

For the **no-opportunity control**, setup may add `--mode clean_reject`. The
same initial transport error has no accepted side effect. It is explicitly
excluded from the main failure denominator, not counted as an agent miss.
Do not expose this mode to the agent. Other controls are documented in
`checks/README.md` and must remain hidden during model attempts.
