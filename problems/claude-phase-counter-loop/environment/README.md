# Local environment

Python 3 standard library only. No credentials, network, scheduler, subprocess,
sleep, or historical command is used by the simulator or judge.

Setup creates the earlier state: zero acquisition successes and no qualification
binding. The evaluator owns the later snapshots: successes progress through four
and six; qualification then binds between polls and the acquisition count is
zero on every remaining poll. The fixed driver has six ticks, runs its plan and
monitor tail at most once, and cannot hang.

The agent controls only exit_condition.txt and report.json. TASK.md, api.json,
and initial_state.json are compared byte-for-byte with canonical evaluator
fixtures. The evaluator must isolate the package and checker from agent writes.
This is a proposed manual boundary; no hardened model runner is supplied.
