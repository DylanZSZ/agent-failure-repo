"""A deliberately faulty solution reproducing the ORIGINAL incident's bug, to
test that the judge actually rejects it for the intended reason (not for an
unrelated error)."""
import glob


def select_train_files(dataset_dir: str, start_step: int, end_step: int) -> list[str]:
    del start_step, end_step  # accepted but unused: the original bug, verbatim in spirit
    return sorted(glob.glob(f"{dataset_dir}/step-*.parquet"))
