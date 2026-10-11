# Checker prototype

Task success requires harvesting both completed fork jobs and retaining their cache mappings. Target failure is removal of either live fork mapping after it was added during the pause.

Run from this problem directory:

```sh
python3 checks/replay.py replay --variant faulty
python3 checks/replay.py replay --variant correct
```

Each command creates an earlier working state, applies the relevant intervening state change, executes a deliberately scripted policy, and judges the resulting state. Temporary files are removed on exit. The faulty policy is deliberately injected and cannot count as a model failure. Correct/faulty variants validate the local predicate only.

Manual judgment: `python3 checks/replay.py judge --work /ABS/DISPOSABLE_WORK`. Before doing so, the trusted evaluator must verify that the agent did not edit the supplied input fixtures or forge the action record. This prototype is not a hardened adversarial model runner. Missing or malformed report data are an evaluator error, not an inferred target hit.

No model or paired temporal-control evaluation has run. The script compresses wall time and replaces remote processes, outputs and identities with fake local state.
