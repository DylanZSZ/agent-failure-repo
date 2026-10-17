# Review the exact files before sharing

Updated 2026-10-13.

## Summary

The contributor should review the private collection and exact selected files before an agent uploads anything. Search comprehensively, then admit only cases passing the [four submission gates](LONG_HORIZON.md#four-gates-for-new-submissions). The public submission contains selected cases, evidence, and runnable reconstructions; the complete lead inventory stays private. A valid file layout is only the first check, and zero admitted cases is a valid result.

## Collection coverage review

- The [collection report](../templates/collection-report.md) lists the exact authorized sources, inspected portions, search passes, unavailable material, and unread gaps.
- Coverage is recorded for [all 20 symptoms](SYMPTOMS.md) and unmatched modes. “No supported incident found” is used only for reviewed material; missing or unread material is not counted as absence.
- The [incident index](../templates/incident-index.csv) includes every distinct candidate, including uncertain, rejected, duplicate, and deferred cases with reasons.
- Repeated references to one event are deduplicated. Different incidents in one symptom class remain separate. Multiple symptom labels on one incident do not inflate the unique incident count.
- Search did not stop after one example, a preferred handful, or one hit per class. Any actual constraint has an explicit continuation point; completeness is not claimed across an unread gap.
- Every private lead has a disposition: admitted, needs evidence, needs reconstruction, out of scope, duplicate, or rejected non-failure. Deferred work names the missing prerequisite and next action. Only admitted cases receive public packages.
- The public index lists only selected cases. Counts reconcile with the private inventory without exposing excluded incidents; any shared aggregate or coverage description has been reviewed for privacy. Do not claim that the public index is the complete search inventory.

## Owner review

- **Submission files:** follow [what to push](SUBMITTING.md). Review the sanitized selected summary, index, and coverage statement as well as every selected problem, evidence file, and actual run record. A problem's review flag does not approve those other files automatically.
- **Scope:** the agent inspected only the histories and project copies you authorized. It states which sources were unavailable.
- **Permission:** you are entitled to share the included code, messages, and other material. Other people's private messages are omitted unless you have permission to include them.
- **Privacy:** inspect all proposed files, including logs, patches, screenshots, filenames, metadata, and test fixtures. Remove credentials, personal details, private repository addresses, customer data, and private home paths. Use stable fake names where relationships matter.
- **Private working files:** raw exports and unreviewed notes stay in `.local/` or your chosen private location. Check the actual staged diff, file list, and commits being shared; an ignore rule does not remove already tracked files or their history.
- **Faithfulness:** quotations and paraphrases are distinguished. Redactions and changes to the original environment are disclosed. Sanitization has not silently removed the reason the failure happened.
- **Publication:** approve the specific files that will be shared. Authorization to inspect history or prepare a task does not by itself authorize uploading that history.

## Task and evidence review

- The account passes all four admission gates with source anchors and a narrow mechanism claim. The actual violation and material contribution of extended work, a context transition, or agent interaction can be checked from shared evidence.
- Multi-agent cases reconstruct assignments, shared or isolated state, event order, visibility, and a consequential interaction. The mere presence of subagents is insufficient. Brief coordination cases make no unsupported duration claim.
- The task states what the sources support and whether fresh model attempts or controlled comparisons were performed. A runnable checker does not imply a model failure or causal proof.
- The actual observed length is separate from the configured maximum. Missing measurements are marked unknown.
- The reduced task preserves the relevant sequence and information available to the agent. It gives the agent a feasible correct path.
- The documented setup and checking commands were actually run in a fresh disposable environment. Dependencies, network effects, starting state, and cleanup are explicit; records identify the tested task and judge versions.
- At every stage, the agent workspace excludes hidden checks, reference solutions, historical failing answers, and descriptions that reveal the target failure. Future prompts and the reset or teammate-change schedule remain outside that workspace.
- The correct reference passes the task check and avoids the intended error. A deliberately faulty control triggers the declared failure check; both controls are recorded and never presented as fresh model failures. The checker accepts valid alternative implementations.
- Task completion and the intended error have separate checks. Preconditions and reaching the failure opportunity are recorded explicitly. Invalid runs, misses, and missing evidence are handled consistently.
- Infrastructure failures are distinguished from agent-caused product failures. A product crash is neither automatically excluded nor automatically counted as the target error.
- Every evaluation attempt is accounted for. Reported denominators exclude invalid or unjudgeable attempts openly, with reasons.
- Original incidents, replays, synthetic examples, fresh model attempts, and temporal comparisons are clearly distinguished.
- A claimed reproduction links to the actual sanitized trace and outcome. A claimed temporal effect includes the control and its limitations.

## Maintainer decision

Apply the [four submission gates](LONG_HORIZON.md#four-gates-for-new-submissions)
and require the completed review in each new account or linked evidence file.
Admit only cases with an observed violation, a sourced material contribution
from an eligible mechanism, auditable evidence, and a verified runnable
reconstruction. Keep original relevance, task readiness, and causal evidence
separate. A narrow supported mechanism is sufficient; controlled model
experiments may remain unrun.

Request a task revision when the final prompt supplies the diagnosis, the
fixture supplies a previously missing observation, or setup overwrites earlier
agent work with a fixed answer-bearing state. Preserve clear requirements and
accessible remedies. Assess whether actual actions and their effects are checked,
whether a legitimate correct path exists, and whether the proposed comparison
changes history rather than quietly making the final task easier.

Keep missing essential evidence or reconstruction work as a local draft with a specific next action. Ordinary local errors are out of scope, even when consequential. Preserve the complete inventory privately; review its coverage without requiring excluded histories to be published. Do not accept a new incident-only package as a substitute for the runnable gate. Existing incident-only submissions remain historical records and can receive a dated reassessment.

Ask for the complete attempt list and existing evaluation records whenever a contribution claims a fresh model failure or a causal comparison. If these have not run, require that explicit limitation rather than invented evidence. Scripted controls suffice to verify a packaged task; they do not establish an error rate or causal effect.

Request revision if the task depends on an undisclosed rule, starts after the crucial mistake, has no feasible correct solution, confuses ordinary task failure with the named error, or claims a fresh model failure from a scripted example. Ask for a narrower claim when privacy or unavailable logs prevents verification.

Record the decision, the evidence level accepted, its main limitation, and the specific work needed next. Preserve the submitted results when interpretations change; add a dated review rather than silently rewriting the run.

Source: [Contribution process](../CONTRIBUTING.md), [history review](FINDING_FAILURES.md), and [reproduction requirements](REPRODUCING.md).
