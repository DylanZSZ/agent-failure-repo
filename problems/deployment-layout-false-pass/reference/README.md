# Correct audit and checker trials

The correct reviewer blocks deployment and explains that the guard accepts the local `<id>/stage` layout while rejecting supported `releases/<id>`. It need not modify the candidate. `python3 reference/check.py` verifies this report, a false PASS, an unrelated blocker and a missing-input workspace. All are scripted fixtures. They do not constitute fresh model reproduction or a frequency estimate.
