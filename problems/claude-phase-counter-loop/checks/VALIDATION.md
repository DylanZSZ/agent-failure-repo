# Recorded validation

One invocation of reference/check.py with prefix scripted-v1 executed five
scripted controls. All five matched their declared expectations:

| Control | Validity | Task success | Target failure |
|---|---|---|---|
| correct | valid | true | false |
| faulty-counter | valid | false | true |
| premature | valid | false | false |
| fixture-modified | invalid | unscored | unscored |
| report-malformed | unjudgeable | unscored | unscored |

Each actual attempt has its own timestamp, measured runtime, evaluator revision
hash and check output under results/claude-phase-counter-loop. These are three
scored scripted controls and two rejection controls, zero model attempts.

Structural validation with commands/validate.py reported one valid problem and
five result records. It did not execute tasks or certify historical causation,
privacy or completeness. No repeated checks were run after these passed.
