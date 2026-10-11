# An independent verifier used gold-label length as a prediction feature and obtained a spurious perfect score

The verifier included the length of the gold-label string among features. Because the two label strings have different lengths, the implementation directly encoded the answer and produced cross-validation accuracy 1.0.

The agent produced a transient invalid verification result. It identified the leakage before its final verdict; the record does not show an erroneous final rejection or a production change based on the perfect score.

See [historical evidence](evidence/incident.md) and [line anchors](evidence/anchors.json). Source identifiers are sanitized aliases mapped privately. Owner authorized submission of the prepared file set on 2026-10-11.

Evidence level: incident with a local staged checker prototype. No fresh model run, rate estimate or temporal causal comparison. The reduction removes production systems and compresses the observed time span. See [task procedure](task/README.md), [environment](environment/README.md), [checks](checks/README.md), and [reference](reference/README.md).
