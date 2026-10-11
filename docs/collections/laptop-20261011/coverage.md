# Coverage of the laptop history collection

Updated 2026-10-11. This is a working evidence ledger, not a model evaluation.

## Summary

Both local history stores were accessible and inventoried. Machine signal scans and selected chronological reviews produced the cases in the incident index. Full semantic review remains incomplete; exact source ranges and remaining leads are retained privately. No fresh model evaluation occurred during collection. The prepared sanitized files were subsequently authorized for submission on 2026-10-11.

## Scope and inventory

The owner requested collection from the local Claude Code and Codex history stores across projects. Original histories were read only. No historical command was executed; only synthetic local fixtures were run. No new model API jobs were launched.

The source files use JSON Lines (JSONL), one structured record per physical line.

| Provider | Canonical files | Physical lines | Bytes | Interpretation |
| --- | ---: | ---: | ---: | --- |
| Claude Code | 14,637 | 1,993,822 | 7,443,508,353 | Includes linked workers and records with unknown project metadata |
| Codex | 3,545 | 38,967,364 | 57,417,442,349 | Includes 4 archived files and substantial parent-history replay |

Source: the private canonical history inventory and provider file receipts.

The inventory snapshot was created at 2026-10-11 06:05 UTC. Source timestamps run from June to October 2026; copied/replayed timestamps may not describe the time of the original work. Live files may change after this snapshot. Provider scan receipts and fingerprints govern the exact ranges actually processed.

## What was scanned and what was read

The Claude base scanner processed cached source paths through the kit’s visible-event normalizer. The supplement reconciled all 14,637 canonical files, adding 556 files absent from the cache. Thirty-eight cached paths through a linked workflow directory were excluded. The supplement also recovered 354 human queued prompts that the standard Claude projection omitted. Other unsupported attachments and external tool-result files remain gaps.

Those 556 additional files were workflow journals. A further allowlisted supplement extracted 9,070 visible final results from their 19,239 physical records. It retained 4,035 signal rows as leads, with duplicate worker responses and quoted task text still requiring scrutiny. This closes a discovery-format gap; it is not a detailed review of all workflow results.

The Codex scanner processes active and archived stores, excluding the collection thread and its detected descendants. It keeps native visible messages and source-anchored tool events, tracks unsupported records, and deduplicates message text for admission review. Parent replay and mirrored message records do not count as independent failures. The scanner’s per-file receipts distinguish completed scans, exclusions, errors and changing inputs.

## Completed scan and excerpt-review accounting

| Layer | Claude Code | Codex |
| --- | --- | --- |
| Physical file pass | 14,637 canonical files | 3,516 historical files; 30 collector files excluded |
| Physical lines scanned | 1,993,822 | 38,950,617 |
| Admission excerpts triaged | 132 | 158 |
| Additional correction excerpts triaged | 66 queued human corrections | 91 ordinary corrections |
| Workflow-return admission excerpts triaged | 14 | Included only when the format is supported |
| Full-source semantic review | Incomplete | Incomplete |

Source: final provider coverage receipts. Counts refer to files, lines and excerpts respectively, not independent agent runs or failure rates.

The Codex discovery pass found 3,546 files: the canonical 3,545 plus one newer collector child. Twenty-nine canonical files and that newer child belong to the collector, leaving 3,516 historical files, including all four archives. Every scanned historical file matched the canonical hash. Three files changed while collection was active, all excluded collector files. No historical read or stat errors were reported.

Claude’s canonical inventory hashes are retained; subsequent passes compared file identity, size and modification time. All canonical sources remained stable during those checks, with no canonical read or JSON parse errors. The rejected 38 symlink aliases are outside that canonical regular-file set.

Across providers, 461 admission, correction or workflow-return excerpts were triaged. These can be duplicates or false alarms; excerpt triage is not full chronology review. Claude retains 23,014 individually unassessed signal hits. Codex retains 198 leads needing chronological investigation, plus its broader symptom-signal database. Unsupported record types, external tool results and source chunks without keywords still require review.

The Codex projection excludes unsupported state/inter-agent record formats, including some top-level agent-message records. Those omissions have exact source-line anchors. Its 35,018,233 normalized event observations include mirrors and replay; they are not unique turns. Both readers exclude hidden reasoning.

Machine scans search the 20 symptom families, corrections and admissions. Detailed verification follows selected leads back to the earlier instruction, action, result and later recovery. Neither keyword matching nor admission-snippet triage is a full chronological review of all source files. Confirmed cases cite their bounded reviewed ranges; no negative conclusion applies to the whole corpus.

## Symptom coverage

“Found” applies to the exact documented variant. “Insufficient evidence” means no strict confirmed match in the assessed cases; it never means the model avoids that behavior. Related operational variants are retained as `other`, including shared runtime state versus committed code and file transfer versus Git delivery.

| Symptom | Status | Confirmed incident IDs |
| --- | --- | --- |
| 1.1 — Standing project rule omitted | Insufficient evidence | — |
| 1.2 — Effective configuration missed | Found | C01 |
| 1.3 — Feature only partly withdrawn | Insufficient evidence | — |
| 2.1 — Rule applied to the wrong module | Insufficient evidence | — |
| 2.2 — Memory overrides current authority | Insufficient evidence | — |
| 2.3 — Project convention crosses scope | Insufficient evidence | — |
| 2.4 — Stale note overrides current evidence | Insufficient evidence | — |
| 3.1 — Earlier working behavior regresses | Insufficient evidence | — |
| 3.2 — Teammate's committed code overwritten | Insufficient evidence | — |
| 3.3 — Resumed agent erases another's additions | Insufficient evidence | — |
| 4.1 — Restricted value copied into a durable file | Insufficient evidence | — |
| 4.2 — Prohibited production access used | Insufficient evidence | — |
| 5.1 — Completion or review pass despite unmet acceptance | Found | C01, C04, C09, C10, C17 |
| 5.2 — Retries mistaken for a repair | Insufficient evidence | — |
| 5.3 — Correct code broken for a wrong test | Insufficient evidence | — |
| 5.4 — New regression accepted into a snapshot | Insufficient evidence | — |
| 5.5 — Self-caused failure blamed on the baseline | Insufficient evidence | — |
| 6.1 — Critical handoff fact omitted or reversed | Insufficient evidence | — |
| 6.2 — Required file omitted from a delivered commit | Insufficient evidence | — |
| 6.3 — Required closing report omitted | Insufficient evidence | — |
| other — Additional symptoms or related variants | Found | C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14, C15, C16 |

Source: consolidated incident records; case numbers also appear in the collection’s incident table. The symptom definitions come from the kit’s symptom guide.

## Results and limitations

There are 17 confirmed cases, 97 unresolved lead records, 4 rejected or duplicate assessed records, 17 task/checker directories and 54 scripted result records. Unresolved lead records may overlap; deduplication is pending. Fresh model runs: zero. The broad signal queues contain additional unassessed candidates; they are not included in these incident counts.

No temporal comparison establishes that long histories caused these failures. Small reductions may preserve the wrong action while losing the cognitive burden of the original sequence. Evaluate those separately. Reported model and client strings come from historical records and are not independent verification of the served model revision.

The current kit schema’s weakest causal label is `suspected`; several packages therefore use it while explicitly stating that causal evidence is absent. Do not read that enum as a positive finding. The local collector feedback file records this and the queued-attachment parsing gap.

Raw source data and working artifacts remain private. The owner authorized submission of the prepared 333-file manifest on 2026-10-11. The submission excludes raw histories, source maps, and private working artifacts.

## Sources and next steps

Source counts come from the canonical inventory; findings come from bounded history excerpts and their case-level evidence notes; check counts come from actual saved result summaries. The private coverage receipts identify excluded, changing and unsupported inputs. Continue with the remaining lead queues, then source chunks without keyword hits. Complete trusted evaluator controls before fresh-model testing.

The detailed source-line ledger, admission dispositions and remaining lead queues are held privately. Full chronological review remains incomplete.
