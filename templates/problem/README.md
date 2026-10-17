# Describe the failure in one sentence

Template updated 2026-10-13.

Status: incident; local draft, reproduction not yet attempted.
Submission decision: selected / local draft only; selection evidence or missing prerequisite.

Symptom labels: choose all that fit from docs/SYMPTOMS.md, or use other.
One incident may have multiple labels; do not count it as multiple incidents.

## What happened and why it matters

Describe the user's legitimate task, the expected behavior, the agent's actual
action, and the concrete consequence. Explain whether this is a meaningful
workflow error or an ordinary local bug. A report that the agent merely seemed
confused is not enough.

## Evidence from the original history

Complete the collection's templates/incident-evidence.md in private working
storage for this candidate. Use its checklist to capture relevant detail before
writing this public-facing summary. Include a sanitized evidence attachment
only after owner review; do not copy private originals here.

Record the agent/model if known and the date. Link reviewed evidence with stable
event or artifact anchors for the complete chain: applicable requirement,
earlier state or interaction, substantive intervening process, wrong action
(with its matching tool result when applicable), and consequence. Include contrary evidence,
later recovery, and the last inspected event. A narrative alone is insufficient.
Label paraphrases, source gaps, and redactions. Never paste raw secrets.

Distinguish original recorded state from later reconstruction and inference.
For reconstructed state, identify the base, source-anchored edits, substitutions,
and checks run later; do not present them as original agent actions. An unknown
model revision can be acceptable; a missing essential link keeps this a local draft.

## Why the earlier work matters

Original relevance: temporal candidate / evidence needed / short control.
Original work exposure: substantial intervening work observed / short mechanism only / unknown; evidence:
Current task readiness: faithful enough for a pilot / needs redesign /
short mechanism demonstration / not built. Explain these separately from status.

Complete the collection's templates/temporal-review.md in the private evidence
record. Include its reviewed answers here or link a sanitized evidence document.
Apply docs/LONG_HORIZON.md; a symptom or a long log alone does not establish fit.
Select only a source-supported contribution from extended work, a context
transition, or real interaction between agents. Name the mechanism; a brief
coordination failure is not automatically a long-running failure.

Describe the earlier event, intervening work, and later decision. What needed
to persist: a rule, a fact, a file change, a boundary, or a status? Could the
agent recover it from current files? Did it actually read the relevant evidence?

Record observed turns, tool calls, session changes, and elapsed time when known.
Define the counting unit and endpoints. Distinguish configured budgets from
actual execution. Explain plausible alternative causes; a long session alone
does not establish causation.

Distinguish a correct earlier state from a provisional mistake whose later
propagation is the target. Identify the natural competing demand and what
observation would weaken the temporal explanation. Separate the pre-error span
from idle time and recovery; measure a propagation interval separately.

## Intended failure and how to identify it

Write the specific wrong action or output the check should catch. Define the
preconditions, the observable failure predicate, and evidence required. Define
correct task completion separately. Explain how unrelated errors, missing
exposure, invalid setup, and unjudgeable runs are classified.

## Minimal reproduction

State what the agent receives at every stage, which files persist, what resets,
and what simulates a teammate or environment change. Keep judge, reference, and
incident narrative outside the evaluated workspace. List changes from the real
incident, what mechanism each preserves, and what the reduction loses.

For multi-agent cases, include the schedule from docs/REPRODUCING.md: each actor's
session and live/replay/scripted role, shared or isolated workspace, visible
messages and file versions, release condition, actual action, and receipt by
the next actor. Record uncertain ordering and demonstrate that the legitimate
tasks were compatible or had an allowed conflict-resolution path.

Explain whether the final prompt and fixture can solve the task without the
earlier stages. Preserve the agent's actual earlier state. Identify any diagnosis,
resolved observation, correct path, or answer inadvertently supplied during
reduction. Describe the actual behavior checked and why an agent-written action
flag alone would be insufficient. Label a short mechanism demonstration honestly.

Describe pinned dependencies or image identity, supported operating systems,
installation, network use, expected cost, and safe disposable execution. Use fake
data and local services. Give copyable setup, staged agent-run, judge,
reference-check, reset, and cleanup commands with working directories, expected
output artifacts, and exit-code meaning. Describe any causal-control command or
mark it not implemented. Nothing required may exist only on the author's laptop.

Link the actual clean-copy command log and tested revision: setup, reference and
checker controls, and reset must work from the proposed submitted files alone.
Follow docs/REPRODUCING.md's clean-environment contract. If it is unverified,
keep this as a local draft. A fresh model attempt is optional for a packaged
submission; an executable procedure for attempting it is required.

## Correct solution and judge checks

Show that a correct solution is feasible and passes. Show that a deliberately
faulty solution is rejected for the intended reason. Test an unrelated error
and a broken setup so they are not mistaken for the target failure. These are
scripted checks, not fresh agent reproduction.

## Fresh evaluations and comparison

Link every result record, including misses and excluded attempts. Record exact
model/settings and task/judge revision. Report hits over eligible attempts,
total attempts, and reasons for exclusions. Report development trials separately
from any evaluation after the task and judge were frozen.

Compare with a condition that changes the relevant history, context, or coordination factor,
while preserving the final task, environment, model settings, and budget as far
as possible. Name all other changes, including edit order, handoff visibility,
and shared state. Specify the comparison before running it. Describe uncertainty;
one pair is not a reliable frequency estimate. If not run, say not run. Keep
historical reconstruction, scripted checker tests, fresh model attempts, and
causal comparisons separate; none substitutes for the others.

## Limits and review

State what is observed, inferred, or untested. Note sanitization changes that
may change the mechanism. The owner must review the exact staged files before
sharing. Record permissions for any third-party material or use a rewrite you
are allowed to share.
