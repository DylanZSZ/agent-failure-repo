# Find every supported failure within the authorized history

> This is a legacy detailed guide for a separately requested comprehensive
> failure audit or reproduction. Ordinary session selection follows
> [README.md](../README.md) and [AGENTS.md](../AGENTS.md). Its 20-symptom search, causal review, and exhaustive reading
> requirements are not default collection steps. Consult individual format
> examples below only when they affect a current session decision.

Updated 2026-10-20.

## Summary

Collect as many distinct credible incidents as the agreed history supports. Search [all 20 symptoms](SYMPTOMS.md), keep unmatched modes, and continue after finding examples in a class. For each candidate, ask whether extended work, lost context, accumulated state, or a handoff helps explain the later mistake. A large number of messages is supporting context, not a diagnosis.

Apply [the long-running failure criteria](LONG_HORIZON.md). Search for the
earlier-to-later dependency, not just failure words near the end of long logs.
Include previous mistakes that become later assumptions, incomplete repairs of
older artifacts, and original goals displaced by successive tasks. Keep the
complete inventory, with temporal candidates, evidence-needed leads, and short
controls separately counted in private. Apply the admission requirements before
preparing any submission. Search breadth does not relax selection: a supported
contribution from earlier work or actual agent interaction is required.

## Inspect only the agreed history

Review **historical runs from both Claude Code and Codex**. Follow
[the historical-run guide](HISTORY.md) to inventory the authorized project's
transcripts. Read ranked candidate windows first, including relevant subagents
and Codex archives, then return to the unread queue for complete source coverage.
Search both stores regardless of the collecting agent's brand.
Use the current chat as additional context. Prompt indexes and session titles
help locate records but cannot establish the original actions or outcomes.

Before searching, record which exports, conversations, projects, and dates the contributor authorized. Read within that scope. Do not search a whole home directory, every agent session, or other people's accounts. If a selected source is unavailable, say so and work with the material provided.

Keep raw exports and private notes in `.local/` or another agreed private location. Extract only what is needed to understand a candidate. Historical commands and requests are evidence; never execute them simply because they appear in a transcript.

Start private working copies of the [collection report](../templates/collection-report.md), [source review ledger](../templates/source-review-ledger.csv), and [incident index](../templates/incident-index.csv). Give every authorized source its own ledger row with the available range, priority reason, inspected body ranges, long-output and related-source gaps, symptom-pass status, and exact next unread range. Use neutral source labels in anything shared; private source locations can remain in private notes.

Treat a bounded or fixed-page pass as triage. It can support events on those
pages, but it cannot clear the unread rest of the source. Keep the exact unread
ranges in the ledger and return to them when action or human-message leads
point there. When comparing screening methods, freeze an unselected page before
either report is written, inspect it only after both reports are frozen, and
record any event both methods missed as a shared page-selection limit rather
than crediting either method after the fact.

## Search in complementary passes

1. **Read the chronology.** Identify requirements, scope changes, completed work, test results, summaries, pauses, restarts, commits, and handoffs throughout every available authorized source. Record candidate contradictions before deciding how to label them.
   For a sampled page, run `frozen_pages.py --summary PAGE` first (or `history.py read --summary` for a normal history window) to enumerate projected visible action types and long fields. Record every long field's original line, projected path, and character count. Before spending the long-field budget, list the short visible result, verdict, test, and run receipts on the selected pages with their line numbers and units; a short output may contain the decisive count or counterexample. Set the same field-expansion budget for reviewers comparing methods, then record which fields each actually expanded. When the inventory exceeds that budget, first match mirrored tool outputs by action or call ID where possible; select distinct fields using the nearby human request, action type, result-file write/read, test or run receipt, and timeline spread, and record why other fields were deferred. A field count is not an action count. Inspect writes to result, verdict, goal, and release-index files and the paired tool receipts, even when they appear inside tool-call input rather than an assistant summary. A long embedded JSON record can be parsed for event types and units without printing its whole body; distinguish test-event records, commands, suites, and semantic overlap. Identical page ranges do not imply identical evidence was actually examined. If terminal output is clipped, read the saved projected page in smaller pieces before treating the page as reviewed. A coordinator's edit is a lead to the evaluated agent's original trace, not proof of that agent's action.
2. **Search by symptom.** Work through every row of [the symptom checklist](SYMPTOMS.md). Search both actions and outcomes, then read the surrounding context. An exact keyword match is not a requirement; an exact keyword search with no results is not a completed review.
   Build a separate **visible-action reading queue** for long histories even when
   human correction keywords are absent. Index original tool calls by source
   line and call ID; nominate repeated test commands, test/edit/test sequences,
   repeated review commands, and additions to test or rule files. Pair calls
   with results and avoid counting UI completion mirrors as new actions. Keep
   source fingerprints and parse gaps beside the queue. A command string is a
   navigation hint: inspect its execution context, working directory, target
   version, test-set changes, and result before calling two runs redundant.
   A zero count of visible edit events between matching command strings does
   not establish an unchanged test target. The same shell call can copy or
   modify a workspace before testing; a later call can recreate a clean copy
   or repair remote state before testing. Pair each invocation with its own
   working directory, in-call mutations, pre/post state and inner test output.
   A piped test may report failures even when the outer tool says success.
   The converse also matters: an earlier test in a compound call can pass
   before a later syntax or setup check fails. Read the whole call and each
   subcommand receipt before marking the test failed or its rerun redundant.
   One shell call can run the same verifier several times, including inside a
   loop. Count reached inner invocations from their separate receipts, and
   record which invocations followed an edit or state change. An unchanged
   verification-report hash supports an unchanged report, not an unchanged
   input state: a manifest rewrite or another in-call mutation may intervene.
   When matching verifier text appears several times in one background launch,
   map each occurrence to its working tree and follow the named job log. The
   launch receipt establishes scheduling; a later test summary establishes
   what ran. Identical commands against buggy, patched, and fixed trees are
   different comparison arms. If a test is piped through `tail` or `grep`, an
   echoed `$?` may be the filter's status; use the inner runner output or
   preserved `PIPESTATUS` to classify the test result.
   A test runner can start and collect zero tests, especially from the wrong
   working directory. Record collection count separately from invocation and
   executed tests; a later run with discovered cases is the first tested run.
   Aggregate these nominations by root and linked child histories before
   ranking a family. A root's human-message manifest gives the task boundary;
   child call IDs and receipts may carry the actual tests. Keep each child's
   reviewed ranges and parser gaps separate. A root-only zero does not clear
   its children, and several child files are not several independent tasks.
   If a parser extracts test-looking text from a compound shell call, keep it
   as a candidate and prioritize it with the **full original command**. A
   `pytest` string inside `rg`/`grep` over an old trace is data, even when it
   resembles a complete test command. `pytest --version` checks an installation,
   and a Python filename containing `test` may name a reporting or audit script.
   For a same-line repeat queue, first separate search patterns, here-doc or
   static evidence text, and reachable test subcommands. Then group reached
   subcommands by working tree and intervening edits before comparing results.
   Raw occurrences in one source line are a reading priority, not executed or
   redundant run counts; keep incomplete background receipts unresolved.
   Read the invoked script's purpose when its name is ambiguous. A priority
   score never establishes execution; preserve lower-priority candidates and
   the parser's unresolved calls for later review.
   For repeated review, follow one review task across `spawn_agent`, later
   `followup_task`/`send_message` calls, child history, and the resulting
   artifact. A review-like agent name or repeated `git diff/status/show`
   string only nominates a window. Read the human request and compare the
   reviewed target, version, scope, findings, and changes before deciding
   whether the same review was repeated or its scope grew. Delegation text
   and child replies may be encrypted in the parent history; inspect the
    authorized child source or mark the task details unread.
   A child can receive several `NEW_TASK` turns under one unchanged agent
   name. Split its chronology at those turn boundaries and label each turn
   from its visible request, actions and artifact. An audit-named child may
   move from read-only inspection to building or repairing another task;
   count the later work by its actual object, not by the original name.
   Adjacent turns may also continue one experiment through design, run and
   checkpoint recovery; link those turns by task packet, state and artifact
   before counting independent tasks or repeated review.
   When a queue starts from audit/review names, reconcile four counts:
   parent starts, child sources actually found, child task turns, and turns
   confirmed to review a particular object/version. Preserve missing children
   and turns with encrypted or insufficient scope as unknown, and snapshot a
   changed child source before comparing it with an older parent index. For
   Codex children, `history.py turns` can list visible `NEW_TASK` boundaries
   and bounded first/last messages; its call counts are reading leads only.
   For each shell
   inspection, check its own working directory and inner result: a command
   may fail outside the repository even when a later command or outer wrapper
   exits successfully. A rule-file path in `git status` establishes neither
   who edited it nor when it became visible; pair the write/diff with the
   subsequent load or read before claiming rule accumulation or inheritance.
   Index explicit edits to `AGENTS.md`, `CLAUDE.md`, skills, and memory files
   as **write attempts**. Pair each target path with its tool result; a failed
   patch is not a confirmed write, and a multi-file patch needs target-level
   checking if partial effects are possible. Read the actual old and new text:
   a full `Write` can prune instructions, a memory directory can hold a
   literature index or task summary, and a series of edits can replace the
   same rule instead of adding new ones. Record addition, revision, pruning,
   reference, and unresolved content separately. Compare file versions and
   count units directly when available, rather than copying counts stated in
   a header. To claim inheritance, identify the later task and verify that
   this version was accessible and actually loaded before the relevant action.
   For a full-file write and later read, compare normalized content hashes
   when both complete texts are available. In a batched tool call, pair the
   specific inner command with its indexed result and exit status; another
   result in the same outer response may be clipped or concern a different
   file. An exact later read establishes exposure to that version, not that
   the agent followed every rule in it. Check the subsequent action separately.
   For memory stores, classify the visible material: a filename in `rg --files`
   is only a path lead; an attached index line exposes its short summary; a
   full note read exposes the note text. An assistant citation shows use of
   the idea but does not upgrade an index summary to a full-note read. Pair
   later launch, stop, or review actions with their own receipts and process
   state. A Claude `user`-role tool result can mirror an assistant write; it
   is not another human request or another memory load.
   Also date the rule's status. A later read from a backup or archive proves
   exposure to historical text, not that the text was still active guidance.
   Check the replacement write, old-file removal, active index update, their
   receipts, and their order before attributing a later action to a rule.
   When notes conflict or one says it supersedes another, preserve both
   versions and use the version available at the action time. If the active
   state cannot be established, leave compliance unresolved.
   Both old and replacement titles in one source are still only search leads:
   one may be an archived filename and the other a citation inside source
   code. Trace each title to its own call, returned object, and any completion
   mirror before saying either memory note was loaded or compared.
   Count a test written in a shell command separately from a tool call that
   reached the shell and a test process whose output or receipt confirms it
   ran. A failed SSH connection, failed `cd`, or earlier `&&` gate can prevent
   later test text from executing. A wrapper's `is_error=false` or exit code
   may describe only its outer pipeline; inspect the inner command's result.
   One compound call may deliberately test the same target in separate
   workspaces; a read-only search can mention a test without running it.
   A grep pattern, here-doc program, or printed historical trace can contain
   `pytest` or another test command as data. Attribute the action to the
   current caller only when the command actually invokes that test; otherwise
   follow the source trace and its actor before counting a historical run.
   For a here-doc that writes a helper script, inspect commands after its
   terminator and the paired receipt. If the same call then runs that script,
   the helper's test invocation can be a current test even though the extracted
   fragment appears only inside the written program. If only the file write is
   visible, retain it as an unconfirmed candidate.
   Include `unittest.main()` and `pytest.main()` in this check. A helper may
   run a verification probe without assertions; record that executed probe
   separately from a passing test suite, especially when `grep` or `tail`
   filters away the runner's result summary. A script named `*test*.py` can
   likewise perform an unrelated audit or network check.
   Also inspect path-linked helpers without a framework call for handwritten
   invariant checks, such as explicit failure branches and a final pass/fail
   result. Keep this as a reading lane: a linked helper may instead download
   data, summarize old traces, or fail in shell parsing before Python starts.
   A static parser that recognizes only some here-doc forms must report its
   parse gaps; no nomination is not evidence of no verification.
   A background task's "completed" notice may cover an outer pipeline while
   the test output lives in a separate file. Follow that file or a later test
   receipt before reporting its pass, fail, or executed case count. If the
   output is unavailable, retain the attempted command and the missing result
   as separate facts.
   Conversely, different wrappers can execute the same suite. A queue with no
   hits is not evidence that the behavior did not occur.
   Before reporting an absence or a rate from search results, check the search boundary and alternate forms of the action: subdirectories and artifact names for files, direct test scripts and other command forms for tests, and the surrounding message for what the agent actually claimed. Inspect examples on both sides of the proposed classification; provisional hit counts are leads, not failure rates.
3. **Compare earlier and later state.** Check omitted edits, stale defaults, changed tests, deleted work, uncommitted fixtures, permission use, and completion claims against the available code, outputs, or version history. For a claimed lost requirement, read the pre-edit text or diff for equivalent wording; an exact keyword search with zero matches and the agent's own admission do not prove semantic absence. Include quiet omissions and mistakes the agent later corrected; label whether the failure survived delivery.
   For a numerical completion claim, reconcile the initial candidate set, exclusions or skipped items, actually changed objects, and final reported total. Preserve the unit at every stage: candidate names, edited occurrences, changed files, remaining registry entries, and accepted outputs may have different counts. Check the contemporaneous diff or artifact when available; a final summary or commit title is not proof that every candidate was changed.
   For a summary spanning multiple batches, recalculate its opening table, later additions, repeat runs, and concluding count from the same document version. Keep research-complete runs, valid calibration runs, and formal assessment qualifications separate; a corrected tail sentence does not establish the status of each underlying run.
4. **Follow boundaries.** Inspect transitions between tasks, projects, sessions, compressed contexts, teammates, and final handoffs. Carry the earlier requirements across reading chunks so an event at the end of one chunk is not separated from its consequence in the next.
   When a report names a failed case as a new requirement, trace that case ID back through its ledger or test definition and later edits. Record its expected value, originating feature stage, current active or retired status, and whether it is inherited regression coverage. Compare those facts with the case-level verifier result and the report's description. A failed aggregate window, or a passing aggregate regression flag, does not by itself classify every case in that window.
   For an aggregate consumer or verifier failure, read the check implementation and locate the first failing assertion or condition on the frozen artifact. A group name such as `working_tree`, an empty observed-results object, or a nonzero exit code does not identify which obligation was reached. Run earlier stages separately when the checker permits, and distinguish an unmodified checker result from a diagnostic copy used to expose the failing line.
Check both sides of a verifier. A failed result may enforce a condition introduced after the relevant task stage or absent from its public contract. A passing result may come from an alternate path that bypasses the required artifact or dependency. Compare each requirement with the stage when it became active, and run a targeted negative case that bypasses the claimed dependency while preserving the visible output. Record the original frozen result, diagnostic result, and any later checker revision separately.
5. **Reconcile the inventory.** Revisit uncertain candidates, deduplicate repeated references, and check every symptom row plus unmatched modes against the inspected scope. Record unreviewed material explicitly and name where to resume.

Record the method and scope for each pass. If the history is too large for one session, process it in explicit chunks with a private ledger of carried-forward requirements and unresolved candidates. Complete all available authorized chunks; if a real constraint prevents completion, report the remaining ranges rather than claiming an exhaustive search.

Before declaring an instruction absent, inspect other event shapes in the same
window. In Claude exports a mid-turn human prompt can appear as a queued-command
attachment, with a separate queue operation recording delivery, rather than an
ordinary `user` message. Check its human origin and delivery, and count the
pair as one instruction. `queue-operation: remove` alone does not prove that
a prompt was withdrawn; look for a later `queued_command` attachment and the
assistant's response. A tool permission denial does not prove that a human
instruction was absent elsewhere in the record.
For ordinary Claude `user` records, prefer explicit provenance over prompt
wording: `origin.kind` other than `human`, `promptSource=system`, or a
`scheduledTaskId` identifies automatic continuations or monitor firings.
Keep those records as task context, not fresh human corrections.
For Codex multi-agent work, check `agent_message` response items and completed
UI items for the sender, recipient, delivery, tool result, and child session.
Some completed items mirror response items; preserve both anchors but count one
underlying action only after matching their IDs or content.
Before closing a source review, reconcile every projected human-origin queued
command with the human-instruction timeline and the next visible assistant
action. A reader can expose the record correctly while the reviewer still
omits it from the written chronology.

For explicit human corrections, read backward to the last applicable request
and forward through recovery. Separate an agent's proposal, an executed launch,
partial progress, completion of the full task, and whether the intended failure
opportunity was actually reached. "No experiment ran" can refer to zero
launches, zero complete tasks, or zero valid observations; check commands,
receipts, results, and the user's wording before choosing one. Record a newly
clarified or changed user goal separately from a still-applicable earlier one.
If the user explicitly excludes an analysis or attribution step during
exploration, track whether the coordinator later makes that step a launch gate.
Record the exact user instruction, the gate's first rejecting condition, each
revision and audit result, the next user correction, and the first real launch.
Separate optional explanatory checks from conditions needed to run a valid
task, such as keeping future requirements out of a verifier or preserving one
session. Do not infer that every review was redundant or that no experiment
ran from a blocked version of one task.
When the complaint is that the agent stopped after an initial batch, read the
then-current task and planning document before calling the stop premature.
Distinguish a stated milestone or minimum batch from an unconditional promise
to finish later items in that same stage. Verify the actual goal-status tool
call and its receipt, the work already completed, the human's later instruction,
and the launches after the correction. The human's dissatisfaction establishes
a correction and a new scope boundary; it does not by itself prove the earlier
milestone violated an unambiguous prior requirement.
As a navigation pass on Codex histories, locate `update_goal(status=complete)`
calls and any later human message even when correction keywords have no hits.
Compare the **earlier objective** with the completed milestone: a goal that
explicitly requires continued iteration cannot be closed solely because its
first calibration batch passed. A later human message may be a new task rather
than a correction, so inspect its content before labeling the closure wrong.
A request to organize results, explain how runs worked, or change report format
is not by itself a reversal of the completed goal. Require a same-goal bridge
from the earlier acceptance boundary to the later human challenge or resumed
work; leave substantive task completion unverified if run artifacts were not
checked.
Count completion calls as events before grouping them by source file: one root
can contain several completed goals. Record a same-goal quality correction
separately from a proven premature closure when the earlier acceptance
boundary or original run evidence remains unclear.
For complaints about parallel or delayed experiments, compute launch intervals
from run receipts rather than relying on the agent's retrospective count. Keep
batch starts, model starts, completed runs, usable observations, concurrent
runtime, and idle gaps as separate units; a batch start need not contain a
completed model task.
Also audit what the coordinator **reported at the time**. Reconstruct the
human's current request and later changes to parallelism or worker ownership;
then compare the available repository/chain/run ledger with the summary and
table actually shown to the human. Record omitted carriers and results, missing
table delivery, and later corrections separately from under-running. A later
complete report does not make an earlier incomplete report complete. If a
contemporaneous estimate and a later detailed ledger disagree, retain both
versions and their units until original launch receipts resolve the count. A
human's "only two experiments?" question is a lead about both work and
visibility, not proof that only two model runs started.
Match background job names, result-directory names, and renamed run labels to
the same session or launch receipt before treating them as separate runs.
When the human asks why real experiments have not started, inspect the paid-run
authorization and the agent's question about missing limits before calling the
wait unjustified. Assess work that did not require paid calls separately:
whether independent task directions could be prepared, delegated, or mechanically
checked in parallel. A reference replay, local calibration, or cloud dry run is
not a model episode; a spawned worker is not a launch. If the agent already
reported zero model starts accurately, do not label the case a hidden-progress
or missing-table error. Repeated checks need their own necessity and outcome
evidence before being called redundant defensive coding.
For a reported local side effect such as recurring CLI windows or high memory,
record the report, nearby commands and process identity, the agent's causal
claim, each stop request and receipt, and any later report separately. A local
test process can violate a cloud-only execution constraint without proving it
caused the reported window or memory problem. A missing PID or closed helper
session does not prove the user's symptom stopped; seek direct confirmation
or leave the cause unresolved.
For repeated interruption complaints, maintain separate timelines for the
assistant turn, tool session handle, local child PID and exit receipt, remote
supervisor, and the user's visible symptom. A `turn_aborted` event establishes a
turn interruption, not why a child process exited or what produced a desktop
window. A PID disappearing without an exit code does not prove natural exit;
an empty or failed OOM-log query does not exclude OOM outside the checked scope.
Do not turn temporal proximity between `exec_command` or a file edit and a
popup into a direct-cause finding without window-to-process evidence.
When the same complaint appears in several root sessions, first link it as
one user concern, then distinguish each agent's task and tool actions. Similar
wording does not establish independent incidents or a shared actor. For data
transfer, separate verified remote asset bytes, retries and protocol traffic,
whole-adapter upload/download counters, and the time interval. Check whether
the original user request permitted the destination or set a volume limit
before treating a later objection as a prior-instruction violation. Trace
rollback through local restoration, remote deletion receipts, and any current
state that was actually checked.
For every correction, preserve the agent's concrete pre-correction claim or
action, the evidence available for it then, the correcting evidence, and the
recovery. A sound final conclusion does not erase a wrong interim claim made
to the user. Conversely, a provisional hypothesis that was never asserted or
acted on is not automatically an incident.
When a human corrects the same artifact several times, connect each request
to the artifact version or edit it addresses, the next revision, and the
later correction. In a taxonomy or summary, check whether the requested
classification level is a research direction, a failure behavior, a carrier,
or a concrete technique before calling the revision compliant. Group this as
one correction chain unless the user clearly opens a separate task; do not
turn every message or apology into an independent failure. Record a requested
pause and later authorization as distinct scope boundaries.
For a missing stage receipt, inspect the delivery record, workspace changes,
the evaluated agent's reads, and the natural stop separately. No receipt does
not establish that the stage was never delivered, and a delivered stage does
not establish completion. In concurrent work, reconcile process exits against
all actors' PID-verified stop actions and archived receipts before saying a
process exited on its own. An agent's statement that it did not stop a run
only describes that agent's actions.
For a coordinator-managed stop, trace the stop command, monitor's state,
notification time, and the monitor's subsequent diagnosis. A monitor report
of an unexplained exit may be a delayed handoff after an intentional stop;
count each proved stop-and-notification sequence, not the coordinator's
retrospective claim of how many times it happened.
For a run stopped by a budget or gate, identify who authorized that stopping
condition, which run version used it, and whether a checkpoint continuation
actually occurred. Count real launches and completed tasks independently.
Keep response, task, and aggregate token caps in separate units. For each cap,
record prior usage, the added allowance, its saved configuration, authorization
flag, model-call evidence, and terminal stop receipt. A proposed or prepared
cap is not an observed budget stop, even if an earlier run hit a different cap.
When a validation rule created for one task blocks another task, inspect the
rule's origin and scope, the second task's current public contract, and the
first rejecting condition in the original gate log. Check whether a model
request began, whether a narrow rule repair passed a positive and a negative
case, and whether the affected task later launched. A global gate rejection
is a coordinator or harness event until the evaluated agent's own actions are
independently shown; a later full-repository scan may still contain unrelated
red entries after the affected task's gate is repaired.

Retain direct process observations such as repeated test execution, review
expansion, and rules that accumulate across stages in the private inventory.
Capture the objects, versions, inputs, actors, and sequence. A successful
product result does not erase those actions. Process observation alone does
not satisfy the public admission requirements for a long-running failure.
When a coordinator summarizes an evaluated agent's trace, mark it as a
secondary lead until the original calls are checked. Keep counts with their
units: post-edit tool calls, test invocations, distinct tests, repeated runs,
and idle or driver-prompted turns are different measures.
When counting test execution, inspect wrapper commands such as `make test`
and `make all`, their dependency targets, and the actual tool output and exit
status. A search for literal `pytest` or `unittest` calls can miss tests run
through a wrapper. Do not count every shell command mentioning `make` as a
separate test invocation or infer semantic duplication from test growth.
For compound shell commands, count tool calls, test command executions, and
reported test results separately. Check `$(...)`, pipelines, `;`, and `&&`
before equating one tool call with one test run; a pipeline can also hide the
test process's exit status. When only a command and output tail survive,
state which counts are observed and which remain uncertain.

Finding one example does not complete a symptom search. There is no one-per-class rule, target quota, or arbitrary cap. Equally, a symptom need not appear: “reviewed, no supported incident found” is a valid coverage result. “Unavailable,” “unread,” and “not checked” are different results and must not become zeroes.

## Keep every distinct candidate in the index

Add a candidate as soon as there is a concrete suspected event. Give it a stable local identifier, source span, short consequence, any matching symptom labels, evidence status, and current disposition. A single event may match several symptoms; keep one incident with multiple labels. Different events in the same class remain separate incidents, even when they share a project or a likely mechanism.

In the private index, use `observation_kind` to distinguish a supported
failure, directly observed process, evidence-needed lead, runtime/carrier
issue, or rejected control;
use `observation_subject` to name the actor whose behavior is at issue. These
are working classifications, not publication eligibility. For an observed
process without an established failure, record what happened in `consequence`
without inventing damage.

Fill the index's five short conclusion fields independently and link the detailed
evidence in `evidence_path`: `behavior_observation` states the observed action
or `unknown`; `task_or_product_outcome` states success, failure, incomplete, or
unknown with scope; `long_horizon_link` states supported, plausible, absent in
reviewed scope, or unknown; `reproduction_status` distinguishes not built,
packaged, fresh model tested, or unknown; `public_admission` states selected,
deferred, or out of scope and why. These are concise summaries, not substitutes
for source anchors. A process observation can coexist with a successful task,
and a packaged task can remain untested by a fresh model.

Keep duplicate rows linked to the canonical incident, and keep rejected or uncertain candidates with reasons. Do not delete them to make the collection look cleaner. Unmatched modes should have a plain-language name and the same evidence review as known modes. The taxonomy guides discovery; it must not hide new failures or force an unsupported label.

The private index must reconcile every candidate to a selected package, local draft, duplicate, rejection, or explicit deferral. The shareable index contains only selected cases; summarize other dispositions as reviewed aggregate counts. Distinguish unique incidents from symptom labels and evaluation attempts.

## Capture detailed evidence, then summarize

First use [the detailed evidence guide](EVIDENCE.md) and a private copy of
[the incident form](../templates/incident-evidence.md). Preserve the full relevant
sequence, original source anchors, supporting and contrary evidence, and explicit
unknowns. The questions below guide the readable summary; they do not replace
the detailed record or limit how much useful evidence to collect.

For each candidate, answer the following in plain English:

1. **Task and consequence.** What did the user want, what did the agent do, and what concrete requirement or behavior failed?
2. **Earlier event.** Where was the relevant rule, successful state, or discovery established? Cite the message, file revision, test output, or handoff.
3. **Later decision.** Which action first violated it? Cite the tool call or edit and the resulting state, not only the agent's final summary.
4. **Intervening work.** What happened between the two? Count messages, model turns, tool calls, elapsed time, or task stages only when the record supports them. Name the unit and state missing measurements.
5. **Information still available.** At the later decision, could the agent see the original instruction, a project file, a current test, or a status report? Was context truncated, summarized, reset, or unavailable? Separate observed facts from guesses about memory.
   For a rule carried across sessions, keep three claims separate: the earlier human instruction existed; the rule was accessible in a file or memory store at decision time; the deciding agent actually received or read it before acting. A file read after a user correction, or the agent's later admission that it "remembered" the rule, does not by itself prove pre-decision exposure. Check file versions and delivery or load events in order. A memory file's origin-session ID can identify its creation, not every later revision or human instruction quoted in it.
6. **A feasible correct action.** What could the agent have done using the permitted tools and information? Was enough budget left to do it? If unknown, say so.
7. **Alternative explanations.** Could an ambiguous request, broken setup, insufficient skill, missing access, contradictory instructions, or exhausted budget explain the result?

Preserve the smallest sanitized excerpts that show the earlier event, later action, and consequence. Keep original ordering and distinguish quotations, omissions, redactions, and your interpretation. If exact quotations cannot be shared, label a paraphrase as a paraphrase. Do not reconstruct missing messages as if they were a transcript.

## Decide whether the example is meaningful

A compact task can expose a consequential failure. Conversely, an agent can spend a long time on an ordinary bug. Describe what depends on time: remembering a prior rule, reconciling a changed environment, preserving another contributor's work, or passing information across a boundary.

Be cautious when the only evidence is “the answer was wrong after many turns.” Also be cautious when success requires a hidden rule that the agent never received, when the correct task cannot be completed, or when the error exists before the agent starts. Those cases may still be useful incidents, but they need revision or a different claim.

There is no universal turn count that makes a task long. Record both the total task length and the span between the earlier event and the later decision. A configured maximum is not an observed run length. A long real incident reduced to a short toy task must be described as a reduction, with the removed work made explicit.

## Apply the admission requirements before packaging

Complete [the temporal review](../templates/temporal-review.md) before task
construction. A reproduction that supplies the exact missing observation is a
different task from the original. Record that loss explicitly; do not promote
an easy final decision exercise because the original transcript was long.

For each relevant case with auditable evidence, attempt a faithful task using [the reproduction guide](REPRODUCING.md). A candidate must show an actual violation and how earlier work or coordination contributed. Record unknown critical links as needs evidence, and ordinary local bugs as out of scope. Multiple agents qualify only when an actual interaction contributed; a delegated syntax error does not suffice. Do not silently drop difficult candidates from the private ledger.

If a faithful environment cannot be built and verified from a clean copy, keep the draft local as needs reconstruction. State the missing prerequisite and next action. A fresh model evaluation may remain not run after setup and checker verification; never replace it with an invented result. End with private coverage and the full inventory, selected runnable packages, and exact remaining work. Zero selected cases is a valid result.

Source: [Contribution levels](../CONTRIBUTING.md) and [agent scope rules](../AGENTS.md).
