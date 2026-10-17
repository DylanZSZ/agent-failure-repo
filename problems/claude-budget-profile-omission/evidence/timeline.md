# Original evidence: Budget constants changed, but the runtime profile was left stale

Source alias: history-campaign-a. These are paraphrases except the explicitly quoted phrases. Original paths, person identifiers, and unrelated cluster details are withheld. The private source map preserves exact file and line anchors.

- L7432, 2026-09-03T08:39:48.596Z, user: observable message. Relevant role documented in the incident account below.
- L7438, 2026-09-03T08:40:40.531Z, assistant: observable tool call/result. Relevant role documented in the incident account below.
- L7454, 2026-09-03T08:44:31.350Z, assistant: observable tool call/result. Relevant role documented in the incident account below.
- L7455, 2026-09-03T08:44:31.688Z, user: observable tool call/result. Relevant role documented in the incident account below.
- L7465, 2026-09-03T08:45:32.213Z, assistant: observable tool call/result. Relevant role documented in the incident account below.
- L7466, 2026-09-03T08:45:32.495Z, user: observable tool call/result. Relevant role documented in the incident account below.
- L7618, 2026-09-03T08:59:25.918Z, assistant: observable message. Relevant role documented in the incident account below.
- L7842, 2026-09-03T09:36:16.150Z, user: observable tool call/result. Relevant role documented in the incident account below.
- L7869, 2026-09-03T09:38:12.941Z, assistant: observable message. Relevant role documented in the incident account below.
- L7884, 2026-09-03T09:39:16.297Z, assistant: observable message. Relevant role documented in the incident account below.
- L7921, 2026-09-03T09:42:21.236Z, user: observable tool call/result. Relevant role documented in the incident account below.
- L7926, 2026-09-03T09:42:46.885Z, user: observable tool call/result. Relevant role documented in the incident account below.
- L7935, 2026-09-03T09:43:26.471Z, assistant: observable message. Relevant role documented in the incident account below.

## Account

The agent changed two budget constants and reported the new ceiling done and deployed. The runtime profile still held the old ceiling; a later plan build refused with an authority mismatch.

The agent later searched the whole checkout, updated the profile, verified 18,000,000 effective seconds, and rebuilt. The error is historical and recovered, not still present.

## Limitations

Full source windows and exact selected events are retained privately and excluded from this submission. This file is an evidence map and paraphrased account, not a substitute for raw event text.

Selected original visible lines are available in [excerpts.md](excerpts.md). Omitted lines and complete source events remain private.
