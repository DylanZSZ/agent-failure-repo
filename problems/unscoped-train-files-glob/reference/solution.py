"""A feasible correct solution to the task in task/README.md."""


def select_train_files(dataset_dir: str, start_step: int, end_step: int) -> list[str]:
    return [f"{dataset_dir}/step-{i:04d}.parquet" for i in range(start_step, end_step + 1)]
