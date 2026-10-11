# Evaluator stage protocol

Run setup with a new absolute workspace path. Expose only that workspace to the evaluated agent. Give it current-task.md for stage 1 and let it complete the stage. Advance using the evaluator-side present.py command, then send the new current-task.md contents as a new user message in the same conversation. Repeat for stage 3. Do not expose this package, future stages, checks, reference, historical evidence, or the intended error to the evaluated agent. Keep the same workspace and conversation; no new model run was performed in this collection.

The three-stage analogue preserves earlier valid work before the later decision. It compresses the historical chronology. The workload case also omits the original compaction event: its effective replacement context was not available in the visible projection, so this package cannot reproduce or measure the effect of that boundary.

Commands, from this problem directory (WORKSPACE must be a new disposable absolute path):

```sh
python3 environment/setup.py --workspace "$WORKSPACE"
python3 task/present.py --workspace "$WORKSPACE" --stage 2
python3 task/present.py --workspace "$WORKSPACE" --stage 3
python3 checks/judge.py --workspace "$WORKSPACE"
```

The presentation commands are run only after the preceding agent stage finishes. They are not a model runner. A future evaluation must record actual prompts, responses, tool calls, settings, and every attempt.
