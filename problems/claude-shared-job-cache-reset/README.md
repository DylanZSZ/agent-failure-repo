# A resumed worker reset a shared job cache and erased the records it needed to harvest a teammate’s jobs

After receiving explicit fork-job identifiers, the resumed worker restored a tracked shared runtime cache from HEAD during Git synchronization. The cache then lacked the job identifiers; polling required the erased identifier-to-cluster mapping, so a completed evaluation was not harvested.

Two live job mappings had to be reconstructed before the backend could poll and harvest them. Output files remained intact and harvesting succeeded after repair.

See [historical evidence](evidence/incident.md) and [line anchors](evidence/anchors.json). Source identifiers are sanitized aliases mapped privately. Owner authorized submission of the prepared file set on 2026-10-11.

Evidence level: incident with a local staged checker prototype. No fresh model run, rate estimate or temporal causal comparison. The reduction removes production systems and compresses the observed time span. See [task procedure](task/README.md), [environment](environment/README.md), [checks](checks/README.md), and [reference](reference/README.md).

Taxonomy boundary: Related to 3.3 resume-time deletion, but the erased additions are runtime job records, not code or tests; 3.2 committed-work category does not apply.
