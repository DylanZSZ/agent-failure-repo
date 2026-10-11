# Correct and faulty checker fixtures

Run `python3 reference/check_reference.py --workspace "$WORKSPACE"` with a new path. It performs stage 1, presents stage 2, enables only the teacher/student components, and checks the result. Add `--faulty` to deliberately enable actor thinking too. These are scripted checker controls, not model reproductions. All executed controls are linked in problem.json. No fresh model run or temporal control was performed.
