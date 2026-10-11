The judge returns separate task_success and target_failure. Validity requires evaluator observation of stage1 completion and stage2 exposure. Missing output is unjudgeable. Reference checks create both correct and faulty states; they do not show a model repeating the error.

## Checker revision 2

The revised checker requires regular input files, a nonempty baseline record and a well-formed final report. A baseline file is only a necessary artifact: the evaluator must still verify the actual stage history independently. Malformed or missing evidence is unjudgeable, not a target hit. Existing revision-1 results remain unchanged; revision-2 cases are recorded as separate attempts.

Both run_state.json and scheduler.json must retain their original JSON content. Changing either makes the fixed-snapshot reduction invalid, even if the report booleans happen to be correct. JSON formatting changes alone do not alter content. Evidence must be a text explanation; the checker verifies it is nonempty, while a human must still assess its meaning. The reference suite also checks absent baseline, malformed JSON structure, nonboolean claims and an empty explanation.
