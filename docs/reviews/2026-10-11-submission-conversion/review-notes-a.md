# Group A conversion review

Reviewed all 40 assigned submitted packages. The structured recommendations are in `review.json`: 15 ready to convert into behavioral tasks, 9 needing task/oracle rework, 5 needing historical evidence clarified first, and 11 best retained as short controls. **Convert now means the source incident supports building a task, not that its current package is already an agentic environment.**

Every current package uses two prompts and JSON fixtures. All 40 setup scripts only copy a JSON fixture; all 40 transition scripts replace it; all 40 judges read only the agent's `decision.json`. This is useful incident documentation and checker prototyping, but it does not exercise the historical code edits, launches, artifact discovery, process polling, or reports. Several stage-2 messages explicitly give the repair. An agent can state the correct answer without performing the work, and most short reductions remove the history dependence being studied.

The strongest first conversions are:

- `benchmark-resumes-prior-probe`: a local checkpointing trainer can measure whether a second timing probe performs new work. The historical pre-decision window is 23 visible assistant messages, 72 tool calls, and 7,397.836 seconds; the bad probe was caught before accepting timings.
- `module-export-fix-omitted`: local environment-export and module stubs can preserve an earlier diagnosis then test a later persistent workflow migration. The measured window is 32 messages, 117 calls, and 4,203.113 seconds.
- `cross-model-metric-row`: interleaved result files with durable model/job identifiers can test whether the reported row actually joins one model. Current grouping puts the answer directly under the model name.
- The queue-environment family (`capacity-switch-retains-next-eval-venv`, `fp32-capacity-environment`, `next-eval-interpreter-leaks-into-capacity`) can share fake queue/interpreter infrastructure while retaining three distinct histories.
- `one-job-evaluation-split`: a local submission log can distinguish the direct one-job request from a conflicting workflow default without a real scheduler.
- `fresh-vllm-cache-workaround-omitted` and `offline-cache-protection-omitted`: preserve the earlier discovery, then inspect actual later launcher behavior. Do not make a deterministic fake prove an uncertain production race mechanism.

`expandable-allocator-reintroduced` has the longest clearly measured before-error sequence here: 96 visible assistant messages, 230 calls, and 77,381.755 seconds. The instruction's scope and the flag's role in the later failure still need clarification: the converter changed other mechanisms, and the earlier removal applied to a specific launcher. It is promising, but this is not causal proof from history length.

Several source narratives give counts for a window that includes diagnosis and recovery. Those cannot be relabeled as work before the error. `dense-decoder-group-mismatch` and `next-eval-interpreter-leaks-into-capacity` explicitly use later-session evidence while metadata reports one session. Clarify the unit being counted.

## Checker verification

After inspecting the common wrappers, setup/transition scripts, and every target expression, I ran 124 local checks with Python isolated mode, a temporary working directory, and an environment containing only PATH and LANG. No submitted setup, historical command, GPU task, network operation, or model call was run. The receipt is `checker-review.json`.

- All 80 submitted reference/faulty fixture tests match their recorded outcomes.
- `{}` is reported as `valid` with `target_failure=true` in six packages: archive completion, monitoring registration, JSONL contract, exclusive provenance, fitting key conversion, and wrong working directory. No action or failure opportunity occurred.
- `lookup=[]` crashes directional checkpoint judging; `jobs=["invalid"]` crashes the FP32 queue judge instead of returning unjudgeable.
- The composite attention judge rejects an explicit `text_config` mapping that the fixture itself allows.
- The walltime judge rejects a reasonable 64-hour request, accepts only 60, and uses an unsupported greater-than-100-hours failure cutoff. Historical authorization did not specify that numerical rule.

The 163 contributed result records for these 40 packages are all labeled scripted checks, including one retained invalid trial; none is a fresh model evaluation. New probe receipts likewise provide no model failure rate.

Minimal reproduction after inspecting the referenced judges:

```sh
python3 reproduce-checker-review-a.py /path/to/agent-failure-repo checker-review.json /tmp/checker-review-a-rerun.json
```

The replay script checks each judge's source hash before executing. The receipt contains synthetic decisions and redacted tracebacks only. Repository and temporary absolute paths were removed; no historical transcript, credential, personal home path, or private source value is included. The replay script uses user-provided paths rather than embedding a laptop path.

## What contributors should supply next

For each converted task, request the minimum source command/diff and returned error needed to establish the event, the earliest rule/correct state and later decision anchors, recovery, and precise missing observations listed per row. For model evaluation, record all trials with model/settings, actual stage delivery, available files/context, executed tools, opportunity validity, task success, target failure, and later recovery. Keep no-history or current-rule controls matched to the same final task. Do not count scripted faulty decisions as reproduced agent failures.

The same code family can serve multiple distinct episodes, but train/test splitting should group shared sources, tasks and mechanisms. In particular, combine infrastructure for checkpoint discovery, checkpoint namespace mapping, queue environment selection, shell/module initialization and submission argument composition; retain incident provenance rather than pretending these are independent benchmark environments.

No contributor files were modified by this review.
