# Read historical Claude Code and Codex runs

Updated 2026-10-10.

## Summary

Review past runs from **both Claude Code and Codex** for the authorized project.
Either agent can collect from both tools when it has local file access. The
current conversation is supplementary evidence. Search all available matching
transcripts, preserve the sequence of actions, and account for missing records.

The helper below only inventories and reads local files. The collecting agent
reviews the relevant task and action records to decide whether a session is
useful for task design. Failure adjudication and reproduction are optional
follow-up work. The helper never starts or resumes historical agents or
executes recorded commands.

## Find the project's transcripts

Record the target project's absolute path before switching into the collection
workspace. From that workspace, run:

```bash
python3 commands/history.py inventory --project /path/to/target-project --output .local/history-index.json
```

The command checks both providers. It selects sources using recorded working
directories, not a guess from an encoded folder name. A working directory must
equal the authorized project path or be inside it. Unrelated sessions are
excluded from content review. Sessions with missing or conflicting project
metadata require scope resolution; do not silently count them as reviewed.

| Tool | Default local transcript location | Custom root |
| --- | --- | --- |
| Claude Code | `~/.claude/projects/` transcripts, including subagents and saved alternative versions | `CLAUDE_CONFIG_DIR` or `--claude-home` |
| Codex | `~/.codex/sessions/**/*.jsonl` and `~/.codex/archived_sessions/**/*.jsonl` | `CODEX_HOME` or `--codex-home` |

Sources: [Claude Code session storage](https://code.claude.com/docs/en/claude-directory#application-data), [Claude Code environment variables](https://code.claude.com/docs/en/env-vars), and [Codex transcript locations](https://learn.chatgpt.com/docs/reference/troubleshooting).
Storage formats can change; the helper supports the record shapes described below.

`CLAUDE_CONFIG_DIR` is the environment variable for Claude Code's storage root.
`CODEX_HOME` is the equivalent root variable for Codex. The explicit command
options override those variables for this read without changing your settings.

Use an explicit root when the contributor has identified a different local
installation or a copied transcript store:

```bash
python3 commands/history.py inventory --project /path/to/target-project --claude-home /path/to/claude-store --codex-home /path/to/codex-store --output .local/history-index-custom.json
```

For a moved checkout or another authorized worktree, repeat `--project` with
the exact additional path. Do not broaden it to the entire home directory to
make matches appear. Older path aliases and external projects need explicit
scope. The helper does not discover other accounts, remote machines, or cloud
histories. Supplied exports can be reviewed separately and listed in coverage.

The helper filters by project, not by date or named conversation. If permission
is narrower than a whole project's history, select only authorized sources and
ranges before reading content; use a scoped export when metadata cannot establish
those boundaries. Do not treat the helper's eligibility flag as broader permission.

The index records checked locations, access problems, matching sources, parse
problems, and source fingerprints. It contains no transcript message bodies,
but its paths and identifiers are private. Output files are created with owner
read/write permissions and never overwritten. Use a new filename to refresh
an inventory. Keep old fingerprints with existing evidence references.

## Prioritize large histories without changing the coverage claim

When hundreds of files match, first link root sessions, subagents, forks,
resumptions, and replayed events using the recorded relationships. Rank task
families for **reading order** using recent activity, observed user/task turns,
tool work, context or handoff boundaries, and explicit human corrections.
File bytes, JSONL line counts, and repeated message copies describe reading
cost; they do not measure task length or count separate failures. A long idle
period does not establish that useful work occurred.

An early pass may extract a compact event timeline and candidate windows.
It is screening, not complete review. Read the full relevant earlier and later
sequence before confirming a candidate, and keep each source's unread ranges
and next line in the coverage ledger. Continue the remaining authorized
history as resources allow. Never turn a screened source or a keyword miss into
"reviewed, no failure."

For a Codex child that may have received several tasks under one agent name,
list its visible task boundaries before counting repeated reviews:

```bash
python3 commands/history.py turns --index .local/history-index.json --source CHILD_SOURCE_ID
```

This private navigation output lists `NEW_TASK` line ranges, bounded previews
of each turn's first and last visible assistant messages, tool-call counts,
and bounded line/type anchors for parse errors or unsupported records.
It counts the original agent message, not its completion mirror. A call count
does not prove review, completion, or redundancy; inspect the request, actions,
target version, and artifact within each range. Encrypted task text and parse
gaps remain unresolved. If a child source changed since inventory, refresh
the index or preserve a complete point-in-time copy before further review.

When a long source needs an initial page sample, reserve some of the fixed page
budget for messages with verified human-origin metadata. Inspect nearby actions
within the selected pages and mark any continuation outside them for follow-up.
First run `python3 commands/history.py human --index .local/history-index.json
--source SOURCE_ID` to list ordinary human-message candidates and explicit
human-origin queued prompts across the **whole source** with their original
line numbers. The command suppresses known automated goal/Stop-hook text,
Claude records with explicit non-human `origin.kind`, `promptSource=system`, or
`scheduledTaskId`, and tool results; long messages retain a length and hash
instead of their body. A scheduled task may contain user-authored instructions,
but its firing is not a fresh typed human correction.
It is a private navigation manifest, not proof of human authorship, delivery,
agent error, or complete history. Inspect any hidden long message at its line
before calling the human timeline complete. Record manifest coverage separately
from the later assistant/tool page sample. A fixed page sample alone cannot
support a full-source claim that no human correction occurred.
Use correction words only to rank those pages for reading; they are navigation
clues, not evidence that the agent erred. Keep the first and last pages and
spread the remaining pages across the timeline. Freeze the page rule and source
fingerprint before reading message bodies, and record how many human-message
pages were selected and left unread. A sample can miss important corrections
even when two reviewers read identical pages. Follow selected corrections
backward to the applicable task and forward to recovery; retain all unselected
pages as unread, including pages displaced by the human-message sample.
For the anchor list, inspect all candidate line positions rather than a stored
first-ten preview. Exclude automated goal check-ins, local-command output,
stop-hook notices, repeated `Stop hook feedback:` and continuation summaries
even when exported as `user`;
keep human-origin queued commands. Rank pages containing explicit human
corrections ahead of generic repeated goal text, and record any human-origin
correction pages that the fixed budget leaves out.
For a frozen-page comparison, use `commands/frozen_pages.py` with a private
freeze JSON containing `source_path_private`, `sha256`, `physical_lines`,
`page_size`, and sorted `page_starts`. Its `--check` verifies the source without
printing bodies; `--summary START` inventories visible event types and long
fields without their bodies; `--page START` and `--line NUMBER` reject requests outside
the frozen ranges. Keep that freeze private because it contains a source path.
For a comparison with a strict long-field exposure budget, set
`bounded_page_char_limit` to `4000` in the freeze. Then `--page` replaces
projected strings of at least that length with their character count;
`--summary` still lists each field's original line and path, and only an
allowed `--line NUMBER` returns its full content. Record every full-line read
as an expansion. Older freezes without this key retain full page output.
Use the guarded reader rather than manually expanding line intervals: a
mistyped range can expose an unselected page and invalidate the comparison.
It shares `history.py`'s visible-event projection, with physical line numbers,
omissions, and schema gaps retained. Do not treat omitted bodies as reviewed.
If original records are required for adjudication, read them only in a
separately labeled follow-up after the fixed-page reports are frozen.

Identify the origin of a `role=user` message before treating it as a user
correction. Scheduled reminders, injected context, replayed copies, and actual
human replies can share that role in exports. Codex goal-continuation or
environment-context messages and Claude task notifications are examples of
non-human records that may appear near real user messages. Preserve their
source and event anchors and do not infer a human complaint or new permission
from an automated notification. In Claude, check `origin.kind`, `promptSource`,
`scheduledTaskId`, and `isMeta` before using text or role as a fallback; a
monitor prompt can be worded like a user request while carrying system source.

Also check for human instructions outside ordinary `user` messages. Claude can
store a mid-turn human prompt as an `attachment` with
`attachment.type=queued_command` and `attachment.origin.kind=human`; a nearby
`queue-operation` may record that the prompt was absorbed into the current
turn. Inspect both records before asserting that no user instruction intervened.
The queued command and its queue operation are one delivery sequence, not two
separate human requests. Keep the recorded file order and event timestamps;
they can differ when a prompt arrives during an ongoing tool call.
Do not treat `queue-operation: remove` as proof that the human withdrew the
request or the assistant never received it. A `queued_command` attachment may
follow `remove` in file order while retaining the earlier enqueue timestamp;
inspect that attachment and the assistant's next visible action. Distinguish
when the human entered a prompt from when it became available to the assistant.
Each `history.py read` page and frozen-page read returns
`human_queued_command_lines`. Reconcile every listed line with the nearby
queue operation and the assistant's next visible action before closing that
page's instruction timeline. An empty list covers only the returned page or
line, not the unread source. Do not count the summary line as another request.

## Complete remaining reading before claiming full coverage

Candidate triage starts with task entries and relevant windows; expand backward
and forward to check requirements, actions, and recovery. Do not infer an entire
task from its opening. Bounded review is permitted when its gaps are recorded.
Only a claim of comprehensive coverage requires completing every eligible source.
For that remaining coverage, substitute each source `id` below:

```bash
python3 commands/history.py read --index .local/history-index.json --source SOURCE_ID --start-line 1 --max-lines 200
```

Before reading a large page, add `--summary` to this command to see projected
event types and long fields without printing their bodies. Record long-field
line numbers, projected paths, and character lengths, then read the page or a
smaller window. The summary is subject to the same source and project checks
as the normal read. It describes only the selected window; it cannot establish
that the rest of the source lacks an event.

Read the returned events in order. Each has an original source line anchor.
`next_start_line` is the starting line for the next page; `eof` means the end
of the file. When completing comprehensive coverage, continue until `eof` is true. The page size controls
one read, not how much of the source to inspect. There is no newest-only filter
or maximum number of sessions. If a tool truncates output, reduce the page
size and revisit that page; for a single oversized record, save the page in
private storage and read its visible fields in smaller pieces.

Save reviewed line ranges, remaining ranges, requirements carried forward,
and open candidates in `.local/collection-report.md`. A file in the index has
only been discovered. It is reviewed only after its available content has
been read and its omissions accounted for. Read the middle of long sessions
as carefully as their beginnings and endings.

The reader checks file identity, size, modification time, and project metadata
against the index. If those changed, it asks for a fresh inventory. It records
a full content hash during inventory and uses line checkpoints for fast page
reads. For an active run, make a new inventory and reconcile the changed ranges
without overwriting old evidence. Do not restart a past run to inspect it: that would create new actions
instead of reading the original record.

Reader output is **private, unredacted evidence** and may contain credentials,
code, or personal information from ordinary messages and tools. Keep saved
pages under `.local/`; it is not a sanitizer. Never paste raw pages into a
public issue or commit them. Follow [the sharing review](REVIEW.md).

## Preserve actions, relationships, and gaps

| Source detail | How to use it |
| --- | --- |
| Claude user and assistant records | Read ordinary text, tool requests, and tool results. Keep message and parent IDs, model metadata, timestamps, and original line anchors where recorded. |
| Claude queued commands | Include `queued_command` attachments and queue operations in the instruction timeline. Check `origin_kind`, prompt, queue operation, and tool order before deciding whether a human authorized an action. |
| Claude bridge sessions | Retain bridge session ID and sequence number as relationship evidence; do not equate a bridge record with a new human message or an independent task. |
| Claude subagent records | Inspect files under a matched parent's `subagents/` directory too. Some versions omit their own project or timestamp; retain the parent link and mark missing timing unknown. |
| Claude saved versions | Treat saved alternatives as versions, not independent runs. |
| Separate large outputs | Follow relevant `tool-results/` references; account for missing files. |
| Codex response items | Read visible messages, function/custom/shell calls, and their outputs. Preserve call IDs so actions can be paired with results. |
| Codex inter-agent messages | `response_item.type=agent_message` carries author, recipient, ID, and visible content. Read it when checking handoffs; omit encrypted content. |
| Codex event messages | Some mirror response items. Retain provenance and distinguish duplicate representations from new actions before counting turns or incidents. |
| Codex completed UI items | `event_msg.type=item_completed` can carry visible commands, edits, agent messages, subagent activity, and collaboration calls. Match item IDs and action details to response items before counting; hidden reasoning remains omitted. |
| Resumed or forked histories | Preserve file identity and ancestry; reconcile replayed events before counting. |
| Compaction or reset | Record the boundary and any available summary. It does not reconstruct removed messages or prove which earlier information remained in the model's context. |
| Unsupported or malformed records | Record their line anchors and types. Resolve using an authorized export or a reader adapted to that version; retain an explicit gap if unresolved. |

Source: [the local reader](../commands/history.py), whose supported formats are
tested with synthetic records. These are format-handling rules, not a claim
that every historical version uses an identical schema.

Source: Claude Code's [application-data layout](https://code.claude.com/docs/en/claude-directory#application-data) documents saved alternatives and separate large tool outputs.
Include `.orphaned-…jsonl` and `.jsonl.superseded-…` records as alternative
versions. A referenced history does not grant access to another project.
The JSON reader does not automatically open those separate output files. Read
relevant referenced outputs privately, preserve their file anchors, and record
missing files. Avoid scanning unrelated session folders for extra material.

The reader deliberately omits private thinking/reasoning blocks and binary
attachments. It reports omissions and unknown shapes instead of dumping
arbitrary record bodies. Use observable messages, actions, outputs, code, and
tests as evidence. Missing attachments or unhandled tool-output formats can
limit a finding; identify them. Do not request hidden reasoning to fill a gap.

Never treat JSON lines, transcript files, or replayed messages as independent
agent turns or runs. State the counting rule and verified endpoints for the
observed horizon. Preserve raw anchors even when combining related histories.
Do not discard identical actions merely because their text repeats: an agent
may actually have retried the same command.

## Report coverage and limitations for both tools

Keep a Claude Code row and a Codex row in the coverage report. For each, record
the checked root, access status, matching files, logical sessions where known,
reviewed ranges, and remaining work. Distinguish these outcomes:

- **Reviewed:** identify the exact sources and ranges, with unresolved omissions.
- **No matching project:** the checked records have no verified match; confirm
  an authorized old path or worktree if the contributor expects more.
- **Missing or inaccessible:** state which store could not be read. Continue
  with the other tool and request a selected export only if needed.
- **Unknown or unsupported:** record the metadata or parsing problem and the
  next action; do not label the session empty.

Histories may have been deleted, retained elsewhere, or never persisted.
Prompt indexes such as `history.jsonl`, session titles, and Git logs are leads
or corroboration; they cannot substitute for an agent's complete interaction
record. Record unavailable evidence honestly. Absence of logs is not evidence
of absence of failures.

Continue with [the failure-search passes](FINDING_FAILURES.md),
[all 20 symptoms](SYMPTOMS.md), and [the evidence checklist](EVIDENCE.md).
The final report must say what was actually reviewed from each tool.
