The judge returns separate task_success and target_failure. Validity requires evaluator observation of stage1 completion and stage2 exposure. Missing output is unjudgeable. Reference checks create both correct and faulty states; they do not show a model repeating the error.

## Checker revision 2

The revised checker requires regular input files, a nonempty baseline record and a well-formed final report. A baseline file is only a necessary artifact: the evaluator must still verify the actual stage history independently. Malformed or missing evidence is unjudgeable, not a target hit. Existing revision-1 results remain unchanged; revision-2 cases are recorded as separate attempts.

The fixed builder must remain byte-identical. If it changes, this reduction becomes invalid and cannot pass the task or score the omission. Configuration Python is checked statically and must contain one finite literal LIMIT assignment; arbitrary rewritten modules need manual evaluation. The judge never executes submitted code. The reference suite verifies the original planner output, then tests correct, faulty, changed-builder, absent-baseline, malformed-report, honest-blocked and executable-config cases.
