# Independent review of the staged shared-cache task

The derived task now executes the behavior that the original decision reduction omitted. An initially correct launcher is written while only the first four shards exist. A trusted transition grows the same cache, and a later request must scope training to a new range. The evaluator records selected and consumed row identities independently of the agent's final report.

I inspected the stage prompts, visible helper files, evaluator service, transitions, judge, reference launchers and control runner. The prompts do not name the failure, reveal the oracle or supply the repair. The package honestly describes a three-request synthetic reconstruction, not a reproduction of weeks of model history. Fresh-model execution still requires a restricted tool adapter or container; the local service alone is not a sandbox.

One review finding was fixed before the final audit: task success originally checked only selected/consumed rows, allowing an incorrect larger row budget when eight rows happened to be selected. The judge now also requires the requested eight-row budget. The author retained earlier result records and added revised ones.

A clean copy passed all 11 scripted controls: explicit selection, filtered glob and copied selection; the exact whole-cache prefix error; a different wrong subset; error then recovery; changed protected data; bad initial behavior; no later action; trainer request error; wrong row budget. Nine additional independent probes checked correct behavior, wrong budget/subset, malformed request, missing job, action in the wrong stage, forged answer JSON, protected-helper modification followed by restoration, and malformed trusted receipts. Outcomes matched the documented validity and failure boundaries.

The audit found no remaining blocking issue. It does not establish an agent failure rate. There were zero model calls and no network or GPU operations. Receipts: `glob-independent-clean-copy.json`, `glob-independent-probes.json`. The compact receipts contain every independent probe outcome; working control directories remain local.
