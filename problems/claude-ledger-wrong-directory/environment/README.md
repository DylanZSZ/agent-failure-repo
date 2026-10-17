# Local environment

Requires Python 3 standard library and, for ledger/cache cases, Git. No network, service accounts, GPU, credentials, original private code or histories are required. The trusted fixture creates only a new disposable directory, initializes fake Git metadata where relevant, and uses subprocesses only for Git or tiny local Python imports. It never runs historical commands.

Paths, job IDs, project labels and data are replaced by fake values. The ledger reduction preserves shell short-circuit behavior in explicit Python control flow around a real no-op Git commit. Worker and progress cases use deterministic process-state records. Metric values are simplified while retaining distinct provenance and missing held-out observations. Cache reset uses a real throwaway Git index. The smoke reduction uses a missing local import symbol instead of GPU libraries. The transfer case uses an injected compatibility error and real local file comparison, with no rsync/SSH execution.

Cleanup: replay cleans its temporary directory. For manual work, remove only the exact disposable directory you created after preserving its trajectory and result.
