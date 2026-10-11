# Correct path and checker fixtures

Run `python3 reference/check_reference.py --workspace /absolute/new/temp/workspace` for a scripted correct sequence. Add `--faulty` for a deliberately faulty final-stage action/report. Both execute only the local fake scheduler. The correct sequence must yield task_success=true,target_failure=false; the faulty sequence must yield task_success=false,target_failure=true. No model is called.

The correct agent retains the current workload when the platform changes, or reports both distinct active campaigns despite a naming alias. No temporal comparison is claimed. A future control could remove the earlier unrelated workload/naming alias, but that also changes task difficulty and needs explicit evaluation design.
