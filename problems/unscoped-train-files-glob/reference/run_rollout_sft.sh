#!/bin/bash
# Sanitized excerpt of the real fix applied in the source incident. Private
# cluster paths replaced with <DATASET_DIR> placeholders. Included for
# comparison against the task's minimal Python reframing above -- this is
# the actual shell-level fix, not the thing the evaluated agent is asked to
# write.

# BEFORE (the bug): an unscoped wildcard glob, with START_STEP/END_STEP fed
# only into a separate download-range check, never into this line.
#   data.train_files="<DATASET_DIR>/step-*.parquet"

# AFTER (the fix): an explicit file list built from the requested range.
TRAIN_FILES="[$(seq -f "<DATASET_DIR>/step-%04g.parquet" "$START_STEP" "$END_STEP" | paste -sd, -)]"
# ... then passed as: "data.train_files=${TRAIN_FILES}"
