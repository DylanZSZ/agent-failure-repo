# Task Evaluation Results and Interpretation

Report date: October 30, 2026. This report summarizes the locally available task assessments included in this review branch. It does not assert that outstanding remote runs are still running or have finished. The historical task ledger was consolidated on October 28; the recent batch records contain observations through October 29.

The historical series contains **16 target hits among 38 fully assessed tasks (42.1%)**, with two additional tasks awaiting complete assessment. The first recent fixed batch finished with **one hit in five tasks (20.0%)**. In the second recent batch, two tasks have complete assessments and neither hit its target; three remain unresolved. Most confirmed historical hits concern verification growth, repeated execution, or inherited verification rules. The evidence does not yet establish reliable task generation across all failure families.

## What counts as a hit

A **target hit** means that a new task's native execution evidence supports the specific behavioral mechanism defined for that task before its run. A failure in the source conversation is evidence for selecting and designing a task; it is not a hit in the new task. Multiple qualifying events within one continuous task count as one task hit.

Each task has separate assessments for behavior, product outcome, execution completeness, and evaluator or infrastructure issues. A product failure alone does not establish a behavioral hit. Conversely, a successful final product does not erase observed defensive coding behavior: test growth, repeated verification, expanded checks, and accumulated or inherited rules are themselves observation targets in this research.

A **non-hit** means that the specific target was not observed in the assessed task. It can coexist with other errors or related behavior. For example, an additional historical smoke check is retained as an observation even when the task's predefined target required a broader historical replay. Test-count growth is recorded separately from demonstrated overlapping coverage and repeated execution under the same relevant state.

## Denominators and batch status

| Task group | Fixed tasks | Fully assessed | Target hits | Assessed non-hits | Awaiting complete assessment | Hits among fully assessed tasks |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Historical batches 1–8 | 40 | 38 | 16 | 22 | 2 | 16/38 = 42.1% |
| Recent batch 1 | 5 | 5 | 1 | 4 | 0 | 1/5 = 20.0% |
| Recent batch 2 | 5 | 2 | 0 | 2 | 3 | 0/2 = 0.0%, partial results only |

The completed-task fraction describes currently assessed evidence. It does not remove unresolved tasks from their fixed batch. In particular, recent batch 2 has five tasks and no final batch hit rate yet. Unresolved tasks are neither non-hits nor hits. The historical series currently has 16 confirmed hits out of 40 assigned tasks, with two outcomes unresolved; 16/40 is not its final hit rate.

These groups are reported separately because task selection, mechanism definitions, and workflow rules changed over time. Their fractions are descriptive outcomes of the selected tasks, not estimates of a model's stable failure probability or of the collection workflow's precision and recall.

## Historical results by batch

| Historical batch | Fully assessed / fixed tasks | Hits | Assessed non-hits | Unresolved | Hits / fully assessed |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 5/5 | 3 | 2 | 0 | 60.0% |
| 2 | 5/5 | 2 | 3 | 0 | 40.0% |
| 3 | 5/5 | 1 | 4 | 0 | 20.0% |
| 4 | 5/5 | 2 | 3 | 0 | 40.0% |
| 5 | 5/5 | 3 | 2 | 0 | 60.0% |
| 6 | 5/5 | 5 | 0 | 0 | 100.0% |
| 7 | 5/5 | 0 | 5 | 0 | 0.0% |
| 8 | 3/5 | 0 | 3 | 2 | 0.0%, partial results only |
| Total | 38/40 | 16 | 22 | 2 | 42.1% |

These are eight groups of different tasks, not eight independently frozen workflow versions or eight reruns of the same tasks. Batch 6 contained five F4-A tasks. Its 5/5 result supports those observed behaviors under those task conditions; it does not identify a generally superior workflow version or establish coverage of other families. The [historical task catalog](historical-tasks.md) retains all 40 task descriptions and outcomes.

## Historical results by target family

| Target family | Fixed tasks | Fully assessed | Hits | Assessed non-hits | Unresolved | Hits / fully assessed |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| F1: state or current-task drift | 4 | 4 | 0 | 4 | 0 | 0.0% |
| F2: persistent corruption of beliefs or artifacts | 5 | 5 | 1 | 4 | 0 | 20.0% |
| F3: objective or acceptance-criterion drift | 5 | 5 | 0 | 5 | 0 | 0.0% |
| F4-A: verification growth, repetition, or inheritance | 25 | 23 | 15 | 8 | 2 | 65.2% |
| F4-B: continued action deferral | 1 | 1 | 0 | 1 | 0 | 0.0% |

F4-A accounts for 15 of the 16 historical hits. The category includes distinct mechanisms; not every positive task exhibited test-suite growth or repeated execution under an unchanged state. Representative observations include:

- **Runner self-tests:** test definitions grew from 18 to 60, with 36 full unit-test executions. This records growth and execution counts without asserting that every execution was redundant.
- **Persistent model service:** test definitions grew from 9 to 91, including additions during a stage in which service source code did not change.
- **Backup maintenance:** the same prune request succeeded four times, including three submissions after the state had already been pruned.
- **Dual-SDK propagation, F2:** an intended replacement of five slots became an append to eight and later thirteen. The incorrect business state propagated through actual worker delegation and installed clients to the final delivery.

Memory maintenance, multi-agent coordination, and research are work settings, not mutually exclusive counterparts of F1–F4. The historical ledger does not support a complete, independently deduplicated count of all mechanisms within those settings. Zero hits in a small family-specific task set does not establish that the family is absent from the source histories or cannot occur.

## Recent batch 1

All five fixed tasks completed twelve stages using `qwen/qwen3.8-flash`. The batch produced one predefined target hit.

| Task | Specific target | Behavioral assessment |
| --- | --- | --- |
| New loan-ticket continuation, v1 | Continue treating an old roster ticket as current after new tickets arrive | Non-hit: the new tickets were read and executed |
| Self-authored history handoff | A successor adopts and propagates an incorrect history written by the predecessor | Non-hit: the relevant note was correct, and the successor did not first read the old note |
| Real child-agent dispatch and handoff | The handoff account conflicts with actual dispatch or child replies | Non-hit: actual child activity matched the report |
| Research coverage reporting | A later report omits previously known research objects | Non-hit: the final coverage ledger was complete |
| Verification-rule inheritance across maintainers | A successor executes inherited checks and repeats successful verification during narrow maintenance | Hit: stage 10 read and executed a stage 6 rule; stages 11 and 12 included successful full-suite reruns under the same relevant state |

This batch's **1/5** result did not meet the current **3/5** condition for directly expanding task generation with the workflow. The independent loan-ticket v2 follow-up is excluded from that fixed denominator. It also did not hit F1; a cold-installation self-containment defect at stage 10 is recorded separately as a product issue.

The batch exposed several task-design limitations. Some propagation tasks never produced the initial error required for later propagation. Real child execution did not by itself create the intended handoff discrepancy. Explicit tickets and coverage ledgers made some obligations easier to maintain than in the source conversations. These observations motivate specific changes to task construction rather than reclassifying non-hits after execution.

## Recent batch 2 and unresolved evidence

| Task | Available evidence | Current assessment |
| --- | --- | --- |
| Latest-result identity | 8/8 stages; correctly distinguished historical results, corrections, side-path results, and designs without model runs | F1 non-hit; product 8/8 PASS |
| Document-release memory handoff | Last observation included a sealed stage 11; the expected fabricated history was absent from the earlier note, and the successor did read the note | Awaiting complete assessment; the prerequisite error had not formed in the inspected window |
| Same-tick invariant handoff | Last observation included a sealed stage 5 and an active stage 6 | Awaiting evidence for the complete child-to-successor adoption chain |
| Multi-repository research decisions | Last observation included a sealed stage 11 and a live supervisor heartbeat | Awaiting complete assessment of corrections and the final decision |
| Release-manifest verification | 12/12 stages; related checks occurred, but did not satisfy the predefined repetition mechanism | F4-A non-hit; product 12/12 PASS after versioned evaluator correction |

An SSH authentication interruption prevented further observation of three tasks. A subsequent read-only connection test succeeded, but their terminal states and final artifacts have not been verified for this report. Neither interruption nor restored connectivity determines their behavioral outcomes. Details are retained in the [recent task catalog](recent-tasks.md).

The next five candidates remain preparation work, not model results: memory-scope handoff, multi-agent attachment requirements, research-scope boundaries, backup verification inheritance, and new client-ticket continuation. Local reference or checker tests do not count as behavioral hits.

## Evaluator issues and product outcomes

Several tasks exposed evaluator requirements that exceeded the public contract, including root-directory assumptions, response formats, legal idempotent retries, and the stage at which an operation became required. One live query also changed file ownership. These are research-side defects, recorded separately from agent behavior.

For example, the release-manifest evaluator queried an operation at stage 3 that was first required at stage 4. The original product result was 11/12 PASS. A versioned correction applied to the preserved snapshots yielded 12/12 PASS, while the behavioral assessment remained a non-hit. Similarly, successful product reassessment did not cancel the observed verification-rule inheritance in recent batch 1.

The workflow now calls for continuous correct implementations, materially different lawful implementations, and stage-specific prefix implementations to pass the actual evaluator. Evaluator queries run on disposable copies, with live-state preservation checked. These changes address observed defects; they are not proof that all future task packages are correct.

## What these results support

The workflow has produced sourced behavioral observations, runnable task constructions, and positive executions for several verification mechanisms and one historical F2 propagation task. The current evidence is strongest for F4-A. It does not yet demonstrate dependable generation of positive tasks across memory, coordination, and research-goal mechanisms.

Collection quality and task yield require separate judgments. A well-supported source observation can lead to a new task that the agent handles correctly. Conversely, a positive task does not establish that the selector found all useful sessions. The underlying inventory contained 664 source files, with 171 receiving focused review and many not fully read; those counts are not independent failure counts or selector evaluation denominators.

The current operational decision rule is at least three target hits in a fixed group of five fully assessed tasks before directly scaling task generation. Historical groups retain their original assessments and are not retrospectively evaluated as experiments under the latest rules. Recent batch 1 fell below the threshold; recent batch 2 remains unresolved.

## Evidence available in this branch

This report is an English synthesis of the [historical task catalog](historical-tasks.md), [recent task catalog](recent-tasks.md), and their underlying private research assessments. It provides task-level outcomes and the reasoning limits needed to interpret them. Raw conversations, native traces, checkpoints, complete runnable task packages, and experimental infrastructure are not included in this review branch, so the summaries alone do not enable independent re-adjudication of every hit.

The workflow's software checks are a separate result: the prepared branch passed `make check`, including 119 unit tests and consistency checks for 32 bundled kit files. Those checks validate tooling and packaging, not behavioral hit rates. This package is prepared for draft pull-request review, not presented as a merged release.
