# Copy these forms, then replace uncertainty with evidence

`problem/` is copied by the scaffolder. `result.json` describes one attempted
run and is copied manually into `results/<problem-id>/<run-id>/summary.json`.
Null values mean unknown or not yet available. They are not measured zeros.

The problem status is one of `incident`, `packaged`, `model_reproduced`, or
`temporal_supported`. These mark progressively stronger evidence, not a score.
The guides explain their meaning. `incident` is available for local drafts and
legacy records. New submissions need the admission requirements in
`docs/LONG_HORIZON.md`, including clean verification of a runnable task. A fresh
model hit or the final status is not required for a packaged submission.

`privacy_reviewed` starts false. Only change it after the owner reviews the
exact files intended for sharing. The validator cannot perform that review.
Do not copy private originals into these templates.

Start a private collection ledger by copying `collection-report.md` and
`incident-index.csv` into `.local/` or another private directory. Inspect all
authorized sources and all symptom categories, then log every distinct candidate.
Use semicolons between multiple symptom IDs in the CSV cell. Each source label
must refer to the collection report; event references stay local until reviewed.
Do not equate several labels with several independent incidents.

Use `symptoms` in each problem manifest to record the existing IDs or `other`.
Unknown categories can remain empty in a draft. The metadata checker does not
check the completeness of your search; the collection report makes its limits
reviewable.

Use `incident-evidence.md` for a detailed record of each candidate in private
working storage. Follow `docs/EVIDENCE.md` for relevant source material, execution
context, chronology, contradictions, impact, and reasons information is missing.
Summarize only after preserving the available evidence.

Complete `temporal-review.md` alongside each incident record, following
`docs/LONG_HORIZON.md`. Include a sanitized version in the problem account or
linked reviewed evidence. Record original relevance separately from task
readiness and contribution status. The existing index's `temporal_evidence`
column can carry the relevance decision and explanation; the complete review
belongs in the linked incident record. No new problem manifest fields are needed.
