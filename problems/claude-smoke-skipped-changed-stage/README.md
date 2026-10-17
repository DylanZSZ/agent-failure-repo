# The changed training stack was declared proven before fresh-stage failures caused repeated full-job retries

After changing the dependency stack, the assistant treated a successful multi-step RL smoke as proof of the entire SFT-to-RL chain and launched fresh SFT jobs. Those jobs repeatedly failed at a missing imported symbol while their outer launcher reported completion. A monitor resubmitted them without resolving the failure.

Direct monitor output and scheduler records show repeated roughly six-minute attempts without SFT completion or RL checkpoints. The assistant reported about a day lost; the measured full-launch-to-diagnosis interval is about 21 hours, which includes queue time and is not billed GPU time.

See [historical evidence](evidence/incident.md) and [line anchors](evidence/anchors.json). Source identifiers are sanitized aliases mapped privately. Owner authorized submission of the prepared file set on 2026-10-11.

Evidence level: incident with a local staged checker prototype. No fresh model run, rate estimate or temporal causal comparison. The reduction removes production systems and compresses the observed time span. See [task procedure](task/README.md), [environment](environment/README.md), [checks](checks/README.md), and [reference](reference/README.md).

Checkpoint reuse is the assistant’s visible diagnosis. The confirmed account here is the premature readiness claim, fresh-stage import failure, and repeated failed launches; the exact checkpoint-reuse cause is not independently established by the selected smoke output.
