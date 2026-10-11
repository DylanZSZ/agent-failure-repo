# Local environment

Python 3.9+ standard library only. No network, model, cluster, credentials, or private histories. Setup exclusively creates the named new workspace; it fails if the path already exists. Agent-visible inputs are config.json, plan.md, stage.json, current-task.md and later-created task artifacts. Future stage prompts remain outside the workspace. The stage presenter snapshots completed stage 1 as evidence. Run in a disposable temporary directory with limited permissions; remove only that disposable directory for cleanup/reset. Setup does not mutate historical files.
