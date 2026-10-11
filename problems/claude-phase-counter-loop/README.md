# A completion loop keeps waiting after its phase counter resets

The historical agent wrote and launched a phase driver that waited for eight
acquisition successes. The service advanced to qualification between polls and
reset the phase counter to zero. Its next-stage binding persisted, but the driver
continued waiting and never reached the downstream plan-building section.

This blocked an automatic transition and required intervention. The anchored
write-to-observed-failure span is 19 minutes: 11 assistant responses and nine tool
calls strictly between endpoints. An ordinary state-machine bug explains the
incident; history length is not established as its cause. Exact additional delay
and eventual downstream completion are unknown.

This package is an **incident with a local reduced prototype**. The evaluator
feeds synthetic states to a fixed driver with an agent-supplied completion
expression. It preserves earlier acquisition states, the transition, and the
later waiting decision. It omits real services, long waits, and production work.
There is no automatic model adapter or fresh model evaluation.

Read [evidence](evidence/timeline.md), [manual task procedure](task/RUN.md),
[environment](environment/README.md), [checks](checks/README.md), and
[scripted references](reference/README.md). Results are linked from problem.json.
The complete original history remains private. Owner review is required before
publishing these proposed sanitized derivatives.
