# Local scheduler tools

The evaluator supplies a `scheduler` tool. It accepts JSON operations and returns
the local scheduler's response. This task uses no network or real compute.

- `{"op":"query"}` lists jobs, exact job IDs, logical requests, output locations
  and current states.
- `{"op":"batch_submit","requests":["alpha","beta"]}` submits the requested pair.
- During recovery, `{"op":"submit","request":"alpha"}` submits one request.
- During recovery, `{"op":"cancel","job_id":"job-001"}` cancels an exact job.

Submission allocates a running job; it does not deduplicate logical requests.
Cancellation preserves the historical record. Use only the request identifiers
in `requests.json`. Jobs that are already running can be inspected at any time.
State is persistent across calls and stages. The evaluator ends a stage when
the current requested interaction is complete; do not invoke real schedulers.
