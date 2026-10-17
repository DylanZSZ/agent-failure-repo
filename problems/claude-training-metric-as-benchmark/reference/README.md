# Correct reference

Run `python3 checks/replay.py replay --variant correct` from this problem directory. The output contains each staged state, the reference decision, and the final task/failure verdict. Keep this reference and its implementation outside agent-visible files.

This demonstrates a feasible local success path. It is a scripted check, not a fresh agent attempt and not a temporal comparison.
