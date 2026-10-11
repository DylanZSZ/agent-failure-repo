# Deliberately scripted controls

The correct condition observes the persistent next-stage binding. The faulty
condition waits for the old phase counter to reach eight. Both receive exactly
the same bounded service sequence. Three additional controls check premature
completion, immutable-fixture validation and strict report types.

Run from the collection root:

```sh
python3 problems/claude-phase-counter-loop/reference/check.py --record-prefix scripted-v1
```

The script records every attempted case under results/claude-phase-counter-loop
and appends those exact paths to problem.json. Reusing an existing prefix is
refused; choose a new lowercase prefix for any later run. It does not invoke a
model, network or remote command. A faulty reference is intentionally injected,
not a historical replay or a fresh agent failure.
