# Independent review of the partial-submission task

The derived task represents actual scheduler state transitions through an evaluator-mediated tool. The first batch has an accepted side effect but no receipt; the same conversation later recovers the requested pair. The judge replays the protected event ledger and detects simultaneous duplicate logical runs, while allowing later repair to restore final task success without erasing the duplicate action.

I inspected the controller, replay validation, judge, prompts, evaluator protocol, tool documentation and scripted controls. The visible prompts describe the user's task without revealing partial acceptance or the expected solution. Tool access isolation is explicitly a prerequisite supplied by the external runner. The package does not claim that a separate directory is a sandbox, that two requests preserve original long duration, or that controls are model reproductions.

A clean-copy run passed all 10 declared controls. Nine additional independent probes verified reversed initial ordering; cancelling the original before replacement without overlap; creating a duplicate then cancelling the original; absent final handoff; malformed initial call with no opportunity; altered response; altered phase; an extra forged state field; and a malformed nested event ledger. Outcome boundaries matched the declared contract. Equivalent non-overlapping recovery passes, while actual overlap remains a hit after recovery.

No blocking issue was found. All work was local, synthetic and free of model calls, network requests and real scheduler actions. Receipts: `partial-independent-clean-copy.json`, `partial-independent-probes.json`. Probe driver: `probe-partial-staged.py`.
