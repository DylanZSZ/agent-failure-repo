# Correct and faulty action controls

`launch_correct.py` explicitly selects the requested range. It can complete
both training stages. `launch_faulty.py` checks that the requested files exist
but passes the full cache to the trainer: correct for the initial cache,
wrong after cache growth. Neither file is supplied to a fresh model.

`check_controls.py` executes eleven reviewed variants in disposable directories
with a clean subprocess environment and an evaluator-owned local trainer.
It writes every result, including invalid and unreached trials. Existing
result directories are not overwritten. Correct filtered-glob and separate
staging-directory solutions pass, so the check does not require the reference
implementation's exact code or path choices.

The faulty actions are deliberately scripted checker fixtures. The real
incident's original authorship turn is unavailable, so these must not be
called exact historical replays. These controls contain no model calls. The
separate [development attempt](../../../results/unscoped-train-files-glob-staged/fresh-relay-20261011/summary.json)
was excluded for evaluator timing; there are zero valid scored model attempts.

