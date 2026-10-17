# What contributors should push

Updated 2026-10-13.

## Summary

Submit only cases passing the [four admission gates](LONG_HORIZON.md#four-gates-for-new-submissions): an actual violation, a sourced material contribution from extended work, a context transition, or multi-agent interaction, an auditable evidence chain, and a clean runnable reconstruction verified with checker controls. Include a reviewed selected summary and index, the selected problem packages, and every actual attempt for those cases.

Search authorized Claude Code and Codex histories comprehensively, but keep the complete inventory and excluded leads private. There is no quota; zero admitted cases is valid. Missing essential evidence or reconstruction work remains a local draft. Existing incident-only records are preserved, not a precedent for new incomplete submissions.

Prepare all files locally before owner review. Include the completed [temporal review](../templates/temporal-review.md) in each selected account or linked evidence file. Separate original relevance, task readiness, and causal support. A brief coordination case may qualify without a duration claim. Fresh model evaluations and controlled causal comparisons are optional for a packaged submission; state when they have not run.

Begin private task construction after the first three evidence gates pass. It
becomes eligible for public submission only after clean reconstruction and
checker controls satisfy gate 4. Do not upload partial scaffolds to fill the
gap, and do not remove or rewrite existing packages or result records when
applying these rules to new contributions.

## Files to include

Choose a unique collection ID and descriptive problem IDs without personal
identifiers. Paths below are relative to the destination repository.

| Path | What to include | When required |
| --- | --- | --- |
| `docs/collections/<collection-id>/README.md` | Selected findings, admission decisions, package links, scope limits, and next actions. | Every submission. |
| `docs/collections/<collection-id>/incidents.csv` | Sanitized index containing only admitted cases. | Every submission. |
| `docs/collections/<collection-id>/coverage.md` | Sanitized Claude Code and Codex coverage and search limitations, without excluded incidents or private locators. | Every submission. |
| `problems/<id>/README.md` and `problem.json` | The original incident, mechanism, admission evidence, intended error, achieved evidence level, and runnable commands. | Every selected case. |
| `problems/<id>/evidence/` | Reviewed excerpts, tool calls/results, relevant before/after state, checks, and redaction notes establishing the essential chain. | Every selected case; evidence may instead be embedded in its account. |
| `problems/<id>/task/`, `environment/`, `checks/`, `reference/` | Runnable ordered prompts, starting files, pinned dependencies where relevant, evaluators, and a correct solution. | Every selected case. |
| `results/<id>/<run-id>/summary.json` and supporting files | Actual attempt settings, outcomes, commands, and sanitized evidence, including checker controls. | Every attempt for a selected case. |

Source: [problem layout](../problems/README.md), [result format](../results/README.md),
and [contribution levels](../CONTRIBUTING.md).

Create the public index by selecting admitted cases from the private inventory.
Replace machine paths and sensitive identifiers with consistent source aliases;
make every shared link resolve to a shared file. State explicitly that this is
a selected submission, not the complete search inventory. Share aggregate
exclusion counts only when reviewed and non-sensitive. Keep excluded case
details and the complete ledger private, including evidence-needed drafts.
Do not count withheld essential evidence as available for reader verification.

For each incident, answer explicitly:

1. **What happened?** The user's task, expected behavior, observed action, and
   concrete consequence, supported by anchored original evidence.
2. **Was the horizon long?** The earlier event, intervening work, later decision,
   and observed turns, calls, sessions, or time with counting rules. Use unknown
   for missing measurements; separate observation from a causal claim.
3. **Why is it meaningful?** What work, requirement, or boundary was affected,
   what a correct agent could have done, and plausible alternative explanations.
4. **What error should the reproduction trigger and detect?** The preconditions,
   exact failure rule, correct task outcome, and invalid or unjudgeable cases.
5. **How did extended work, a context transition, or agent interaction contribute?**
   Anchors for the earlier condition and later action, substantive work or the
   actual interaction, information or artifacts carrying the dependency, actor
   visibility, and the strongest alternative explanation. Missing essential
   links keep the case local as needs evidence.
6. **Does the reduction preserve that dependency?** The natural continuation or later request,
   competing demands, actual state passed forward, independent behavioral check,
   accidental answer cues, successful clean reconstruction and checker controls,
   and what the proposed comparison can establish.

Retain enough of the relevant sequence to assess those answers, including
contrary evidence and later recovery. Excerpts can span multiple files; keep
stable event anchors and label omissions, paraphrases, and redactions. Do not
replace available evidence with a polished narrative alone. If essential
evidence cannot be shared, retain the lead privately until a faithful sanitized
reconstruction and evidence chain are possible.

## Minimum submission and optional evaluations

A new submission must be a **packaged reproduction** or stronger: actual stage
prompts, starting files, fixtures, dependencies, setup and run commands,
separate task and failure checks, and a feasible correct reference. Run the
documented commands from a clean disposable environment and retain the records.
The correct control must complete the task without the target error; the faulty
control must trigger the declared check. These are scripted checker tests, not
fresh model failures. Preserve the earlier event and later decision; an already
broken final file is insufficient.

An **incident-only** account remains a local draft when essential evidence or
reconstruction work is missing. The schema's `incident` status and null command
fields remain supported for those drafts and legacy records. No schema changes
or deletion of existing cases are required. Do not upload an untouched scaffold
or result template to imply that reconstruction or evaluation occurred.

Complete the reduction review before calling it ready for a pilot. An exact
decision dictionary or self-reported action is insufficient when the intended
failure concerns executed behavior. A final fixture that supplies the diagnosis
or correct observation does not recreate the original discovery burden and
fails the faithful reconstruction gate. Keep historical suitability distinct
from task quality.

For **fresh model evaluations**, include every attempt: hits, misses, invalid
or unjudgeable attempts, development trials, and controls. Record model and
settings when exposed, actual length, task/judge versions, preconditions,
whether the failure opportunity occurred, and both task and failure outcomes.
Request existing results from the contributor when a claimed reproduction has
no supporting records. If none exist or a fresh run is unavailable, write
**not run** with the reason and next action; do not invent results.

Link every actual run's `summary.json` from `problem.json` using the repository
path. Inside each run record, evidence paths are relative to that run's
directory. Put original historical evidence in the problem account or its
`evidence/` directory; the original incident is not a fresh evaluation.
Describe that evidence in `source.evidence_note` and link it from the problem
readme; do not invent additional manifest fields.

Record the temporal review and relevance decision in Markdown; keep the current
problem/result schema unchanged. Existing submissions retain their records.
Add a dated reassessment when applying these criteria to an older package.
Metadata validation does not certify that a temporal review is scientifically
adequate; maintainers must read it.

## Material that stays local

Keep these outside the outgoing commit and its history:

- `.local/`, including the complete candidate inventory, excluded leads,
  evidence-needed and reconstruction-needed drafts, raw reader pages, private
  incident notes, and the mapping from sanitized aliases to real identities.
- Original Claude Code/Codex transcript stores, prompt indexes, credentials,
  account configuration, unrelated conversations, and full private checkouts.
- The working `REPORT.md` when it links to private notes. Publish its reviewed
  summary under the collection directory above.
- Secrets, private source without sharing permission, personal or customer
  data, unreviewed logs, dependency caches, and disposable environments.

Evidence and reference solutions belong in the submitted repository for
reviewers. During evaluation, expose only the intended prompts and starting
files to the tested agent; keep the judge, reference, and historical failing
answers outside its accessible workspace.

Ordinary submissions add only selected collection, problem, and result files.
Put task-specific setup and checking scripts inside their problem package.
Changes to shared kit instructions, `commands/`, templates, or the installed
skill are separate maintenance work and should be explained as such.

## Review, verify, and push the selected files

Use a clean checkout of the destination repository and a new contribution
branch. Copy only the proposed submission files from the private collection;
do not copy the collection workspace wholesale. Use a fork when the contributor
does not have write access to the shared repository. Prepare a pull request
against `DylanZSZ/agent-failure-repo` on `main` after sharing is authorized.

Before any upload, show the owner an exact repository-relative file list and
the contents or diff of those files. Review every file beneath the selected
directories, including collection summaries and evidence. Set each problem's
`privacy_reviewed` field to true only after the owner has reviewed those exact
files; the collecting agent cannot supply that approval itself.

If these exact files and destination are already approved, continue without
asking again. Otherwise finish the reviewable material and request approval
to share it. Permission to inspect histories alone is not upload permission.

Stage only those reviewed paths. Inspect the staged file list and diff:

```bash
git diff --cached --name-only
git diff --cached
python3 commands/validate.py --submission
```

The validator checks problem/result structure and the problem's review
declaration. It does not validate collection reports, certify privacy, or verify
that an incident or reproduction is correct. Review the collection files too.

For a runnable package, check a clean copy of the proposed committed files:
follow its documented setup and scripted checking commands, and confirm all
required fixtures and dependencies are present. Reuse recorded model results;
this check does not require buying new model runs. Check that outgoing commits
contain only reviewed material; deleting a private file in a later commit does
not remove it from earlier history. Then push the contribution branch and open
the authorized pull request. Preserve existing submissions and run records.

## Tell the contributor in the console too

In the final chat response, provide:

- What was found, how many cases passed all four gates, how many remain local
  or out of scope, and the main gaps. Zero admitted cases is a valid result.
- The exact files proposed for sharing, or the files actually committed and pushed.
- Which scripted checks and model evaluations ran, and which were not run.
- The local report path and, if uploaded, the branch, commit, and pull-request link.
- What still needs review, evidence, reproduction work, or evaluation.

Do not report “pushed” until it succeeded. A local collection awaiting review
must be labeled local. A report link alone is not the console explanation.

Source: [owner review](REVIEW.md), [reproduction requirements](REPRODUCING.md),
and [detailed evidence](EVIDENCE.md).
