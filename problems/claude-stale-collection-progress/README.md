# A crashed collection was reported as advancing because a stale counter and a live endpoint were mistaken for job progress

After reading a counter of 6,600 and seeing the teacher endpoint up, the assistant later reported that collection was still advancing at about 100 episodes per minute without a fresh collection-state check. The collector had exited with a context-length error; a waiter checked for a failure marker that was written to a different destination.

The crash went undiagnosed for approximately 73 minutes. A later live inspection found idle GPUs, unchanged logs, and the error. The assistant reported losing the unsaved 6,600 episodes; that loss is an agent-reported estimate, not an independently audited storage count.

See [historical evidence](evidence/incident.md) and [line anchors](evidence/anchors.json). Source identifiers are sanitized aliases mapped privately. Owner authorized submission of the prepared file set on 2026-10-11.

Evidence level: incident with a local staged checker prototype. No fresh model run, rate estimate or temporal causal comparison. The reduction removes production systems and compresses the observed time span. See [task procedure](task/README.md), [environment](environment/README.md), [checks](checks/README.md), and [reference](reference/README.md).
