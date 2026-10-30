# Private session collection templates

New collections use collection-report.md, source-review-ledger.csv, and session-selection.csv. The history index supplies source paths, fingerprints, dates, and source relationships; these are not retyped into each row. Record one session decision per actual task, linking related source IDs. Use selected, needs-evidence, or not-selected as the decision. Keep read ranges separate from available source files.

The session list has five columns: task_id_and_source_ids, decision, key_event_anchors, design_use_or_reason, and material_and_reading_gaps. Assign one task ID per actual objective, linking all related source IDs; one source can contribute to several task rows. Selected rows name the natural task, relevant state or handoff, and observable behavior. A needs-evidence row names the exact missing original. A not-selected row gives a short reason; unread sources are represented in the source ledger rather than classified as rejected.

For a proposed long-horizon task, copy task-candidate.md into private storage and link it from design_use_or_reason. This preserves the five-column format and old ledgers. The card separates direct observations, native evidence, state dependency, constructed elements, carrier origin, and execution results.

Legacy incident-index.csv, incident-evidence.md, temporal-review.md, and problem templates remain available for separately requested failure analysis, task packaging, and publication. They are not required for ordinary session selection.
