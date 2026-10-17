# Original evidence: Scheduler activity was reported as progress in a blocked run

Source alias: history-campaign-a. These are paraphrases except the explicitly quoted phrases. Original paths, person identifiers, and unrelated cluster details are withheld. The private source map preserves exact file and line anchors.

- L8159, 2026-09-03T11:21:48.248Z, assistant: observable message. Relevant role documented in the incident account below.
- L8228, 2026-09-03T13:20:14.463Z, assistant: observable message. Relevant role documented in the incident account below.
- L8280, 2026-09-03T15:19:46.794Z, assistant: observable message. Relevant role documented in the incident account below.
- L8296, 2026-09-03T16:19:13.448Z, user: observable tool call/result. Relevant role documented in the incident account below.
- L8299, 2026-09-03T16:19:39.318Z, assistant: observable message. Relevant role documented in the incident account below.
- L8303, 2026-09-03T16:19:50.640Z, assistant: observable tool call/result. Relevant role documented in the incident account below.
- L8306, 2026-09-03T16:19:56.942Z, assistant: observable message. Relevant role documented in the incident account below.
- L8345, 2026-09-03T17:20:30.730Z, assistant: observable message. Relevant role documented in the incident account below.
- L8361, 2026-09-03T18:19:19.463Z, user: observable tool call/result. Relevant role documented in the incident account below.
- L8371, 2026-09-03T18:19:52.525Z, assistant: observable message. Relevant role documented in the incident account below.
- L8546, 2026-09-03T19:22:03.125Z, user: observable tool call/result. Relevant role documented in the incident account below.
- L8561, 2026-09-03T19:23:24.529Z, user: observable tool call/result. Relevant role documented in the incident account below.
- L8588, 2026-09-03T19:25:42.530Z, assistant: observable tool call/result. Relevant role documented in the incident account below.
- L8598, 2026-09-03T19:26:21.690Z, assistant: observable message. Relevant role documented in the incident account below.
- L8729, 2026-09-03T20:51:57.699Z, assistant: observable message. Relevant role documented in the incident account below.

## Account

The agent correctly said the gate had not passed, then later reported the gate passed and consumer training active based on scheduler names. The same check still showed consumer lanes at REVIEWED. Later detailed receipts showed the specified run was blocked with zero harvested gate results.

At L8598 the agent explicitly corrected its reports and escalated the stuck gate. L8729 still reports the block and respects the no-second-writer rule. That later escalation is correct behavior.

## Limitations

Full source windows and exact selected events are retained privately and excluded from this submission. This file is an evidence map and paraphrased account, not a substitute for raw event text.

Selected original visible lines are available in [excerpts.md](excerpts.md). Omitted lines and complete source events remain private.
