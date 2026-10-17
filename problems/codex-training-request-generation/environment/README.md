# Disposable local state

Python 3.9+ standard library only. No network, credentials, services, GPUs, shell scripts, or production commands. Setup creates a new workspace and refuses existing directories. scheduler.py appends fake jobs to jobs.json. state.json records the currently presented stage. Dataset/model/campaign names are synthetic. Reset by choosing another new temporary directory; clean up only that disposable directory.
