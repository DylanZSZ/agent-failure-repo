# A failed file transfer was described as checksum-verified and left the next executor without its input

A transfer used an unsupported option and its shell pipeline ended successfully despite the transfer error. The handoff stated that required files were already checksum-verified on the destination. Later executor evidence and a checksum dry run showed that the main files were still absent.

The downstream executor was blocked at the data-filtering stage because the selection file was absent. One separately transferred view file did arrive; this partial success does not establish delivery of the package.

See [historical evidence](evidence/incident.md) and [line anchors](evidence/anchors.json). Source identifiers are sanitized aliases mapped privately. Owner authorized submission of the prepared file set on 2026-10-11.

Evidence level: incident with a local staged checker prototype. No fresh model run, rate estimate or temporal causal comparison. The reduction removes production systems and compresses the observed time span. See [task procedure](task/README.md), [environment](environment/README.md), [checks](checks/README.md), and [reference](reference/README.md).

Taxonomy boundary: This is file transfer and false delivery reporting, not missing files in a Git commit (6.2); no earlier recognized failure was omitted from the handoff, so strict 6.1 is not asserted.
