# What the two reference branches tell us to collect

Updated 2026-10-11.

## Summary

**We want failures in which earlier work changes a later decision or its consequences.** The strongest reference tasks make an agent establish a useful rule, create an artifact, verify a result, or accept a commitment; later legitimate work changes what that earlier state means. The error occurs when the agent fails to retain, revise, revoke, correctly scope, or independently verify it.

The release branch supplies concrete observable symptoms. The cleanup branch develops deeper sequences: an earlier correction becomes a permanent rule; code is repaired while old delivered data remains wrong; a self-written test becomes an obstacle to a new requirement; or a provisional interpretation gradually displaces the original goal. These are promising **designs**, not proof that running longer causes the observed errors.

Use [the submission criteria](../../LONG_HORIZON.md) to assess new contributions. Preserve the relevant history when reducing an incident. Do not replace that history with a final prompt containing the diagnosis and correct answer.

## Reviewed versions and limitations

| Reference | Pinned revision | Reviewed material |
| --- | --- | --- |
| `release/benchmark` | [Release snapshot][release-commit] | All 20 current mode READMEs; representative task specifications and drivers |
| `chore/workspace-cleanup-20261001` | [Cleanup snapshot][cleanup-commit] | Current documentation, runner checks, and representative top-level task sources, including the newer temporal chains |

Source: the pinned branch snapshots above; exact commit identifiers are listed under Sources.

Archived problems were excluded. No reference task was rerun, and the recorded results were not independently reproduced in this review. Cleanup has 159 top-level `envs/z*.py` source modules, including unverified, blocked, retired, and short-control designs: **this census is not a validated benchmark count**. Its README points to a separate analysis repository for detailed results. Source links below are pinned to the reviewed commits and require access to the reference repository. [Cleanup scope][cleanup-readme]

## Shared behavioral families

The correspondence below groups related mechanisms; it does not claim that the branches contain identical tasks.

| Behavior we want to study | Release examples | Cleanup examples | What a faithful reproduction must retain |
| --- | --- | --- | --- |
| Earlier obligations stop reaching the right output | [1.1 standing rules][r11], [1.2 effective defaults][r12], [1.3 incomplete withdrawal][r13] | [Publishing state used by later outputs][c-zqn] | Earlier obligations, multiple real consumers, a later change, and a check of actual output—not a supplied impact checklist |
| A previously useful rule outlives its scope | [2.1 module scope][r21], [2.2 memory versus contract][r22], [2.3 project scope][r23] | [Correction reused after scope change and retirement][c-zcr] | The earlier rule must genuinely have been useful; later work must require distinguishing its scope or retiring it |
| Earlier knowledge conflicts with present state | [2.4 stale design note][r24] | [Historical rule table versus changed implementation][c-zdf]; [new local repair versus old authoritative record][c-zqn] | Provenance of the old belief, a real change, accessible contradictory evidence, and a later consumer of the old representation |
| Correct new code still loses earlier work | [3.1 regressions][r31], [3.2 colleague overwrite][r32], [3.3 overwrite after pause][r33] | [Previously delivered baselines and ledgers retain obsolete ownership][c-zpv] | An independently verified earlier state, compatible later work, and checks of both old obligations and new behavior |
| Self-checking becomes an authority of its own | [5.3 correct code changed for a wrong test][r53], [5.4 regression written into a snapshot][r54] | [Old acceptance assumptions resist new requirements][c-zsv]; [registered expectations rewritten to match output][c-zvk] | Agent-created checks or records with history; later conflict; independent product truth; the option to report an unresolved conflict honestly |
| Small mistakes accumulate through dependent work | [2.4 stale notes][r24], [5.2 accepting a lucky rerun][r52] are related symptoms, not equivalent accumulation tests | [Increasing irreversible archive loss][c-zye]; [old review tools reused on later counterexamples][c-zwh] | Actual downstream consumption and growing consequences, rather than repeating an unchanged wrong answer several times |
| Prior commitments or interpretations disappear under competing work | [6.1 handoff loss][r61], [6.3 missed wrap-up][r63] | [Interrupted research lines][c-znx]; [conflicting framings arriving over time][c-zrj]; [tentative statements quoted back as settled][c-zrh] | Legitimate intervening requests, the still-applicable goal, evidence of displacement, and a distinction between silent loss and acknowledged reprioritization |
| Boundaries and delivery facts are lost while finishing | [4.1 secret persistence][r41], [4.2 prohibited credentials][r42], [5.5 false attribution][r55], [6.2 omitted files][r62] | [Stale teammate completeness republished downstream][c-zcw] | The earlier boundary or verified fact, later action, and independently observed effect. These remain adjacent reliability cases until their dependence on earlier work is supported |

Source: each row links the relevant release specification and cleanup design.

## Why the strongest cleanup designs matter

**A correction can become the source of the later error.** In the configuration chain, relaxing a comparison is correct when requested. After several uses, strict release checks and retirement of the original exception make that same rule inappropriate. The interesting choice is whether the agent can revise a once-successful rule and its tests. This preserves a natural conflict between maintaining a previous fix and applying the new requirement. [Correction chain][c-zcr]

**Recognizing a contradiction and repairing its lasting representation are different actions.** The publishing redesign gives the agent a new reference page where a quick local repair resolves the immediate warning. Future builds still consume a separate, older publication record. Its predecessor was too easy because the prompt enumerated the consequences and practically directed the agent to the only relevant record. [Publishing redesign][c-zqn]

**Persistent data creates a real dependency even when code is well factored.** An ownership-rule predecessor used one shared function, so changing it automatically fixed several supposedly independent interfaces. Its successor instead checks approvals, baselines, and ledgers written before the rule changed. Correct code plus unchanged old files is now an actual possible failure. [Delivered-data redesign][c-zpv]

**Accumulation and drift need their own evidence.** The archive design measures increasing lost payload as later batches reuse an inherited processing error. That supports a compounding-damage mechanism; it does not show that long context caused the initial bug. The research designs permit legitimate changes of method and priorities. A different scientific conclusion is not itself a failure: unsupported claims, abandoned commitments, and the evidence connecting them to prior work must be assessed separately. [Archive mechanism][c-zye], [research limits][c-zrj], [commitment tracking][c-znx]

## Complete release-mode mapping

**Temporal candidate** means the design contains a meaningful dependency on earlier work. **Plausible** means such a dependency is possible but a local explanation remains prominent. **Adjacent** means the current task can test a useful reliability problem without establishing extended-work dependence. None of these labels establishes a duration effect or a reproduced failure rate.

| Mode | Intended observable error | Earlier work that must matter | Fit and principal limit |
| --- | --- | --- | --- |
| [1.1 Standing rule omitted][r11] | New setting works but misses required validation or worker serialization | Earlier rule and correct implementation must be recovered from the repository in a later session | **Temporal candidate.** Repository persistence and local imitation; many recorded outcomes occur at a step cap |
| [1.2 Effective layer missed][r12] | Changed constants do not change runtime defaults | Agent-authored defaults are superseded by a maintainer’s effective configuration | **Temporal candidate.** Search difficulty and budget remain alternatives to a history effect |
| [1.3 Incomplete withdrawal][r13] | One representation of a revoked feature remains in output | Multiple earlier feature deliveries encode the same concept under different names | **Temporal candidate.** Naming every field demonstrates solvability, not a pure horizon effect |
| [2.1 Rule leaks across modules][r21] | Blob retries adopt the HTTP status policy despite a behavior-preserving refactor request | Recently implemented HTTP policy competes with an earlier, different blob rule | **Temporal candidate.** The final ticket itself emphasizes status-bearing errors |
| [2.2 Memory overrides current contract][r22] | Old milliseconds convention replaces the current seconds contract | Self-written memory comes from successful work on earlier packages | **Temporal candidate.** Narrow matching-API copying; the reported memory comparison is inconclusive |
| [2.3 Convention crosses projects][r23] | Internal license marker or ticket format enters an unrelated upstream project | Rules learned and enforced in a fork are carried through personal notes | **Temporal candidate.** Repository identity confusion is an alternative mechanism |
| [2.4 Stale design note][r24] | Current behavior contradicts a note, but the dependent function follows the note | A once-correct invariant survives an intervening teammate change | **Temporal candidate.** No-note controls also fail; memory loading may affect perceived authority |
| [3.1 Delivered feature regresses][r31] | Later work breaks independently verified earlier functionality | Features and obligations accumulate across deliveries | **Temporal candidate.** Ordinary implementation difficulty and budgets can also cause regressions |
| [3.2 Colleague commit overwritten][r32] | Rewriting a file removes a colleague’s compatible committed behavior | Agent’s earlier conception of its file predates another author’s additions | **Temporal candidate.** Some runs include imposed compaction; others directly read the added code |
| [3.3 Resume overwrites another agent][r33] | Resumed work deletes intervening functionality and its tests | A pauses after writing; B adds compatible work; A resumes its existing context | **Temporal candidate.** Interleaving is demonstrated by design; a longer pause is not itself causal |
| [4.1 Test secret persisted][r41] | Restricted test token enters durable documentation | Legitimate earlier token use precedes documentation | **Adjacent.** The persistence opportunity is local; writing docs versus not writing docs does not isolate horizon |
| [4.2 Production credential used][r42] | Verification crosses an explicit credential boundary | Earlier staging-only policy must survive repeated unsuccessful attempts | **Plausible.** Allowed credentials cannot complete the task; honest BLOCKED is a valid outcome |
| [5.1 Incorrect DONE claim][r51] | Green visible tests accompany incorrect specified behavior | Related feature rounds create interacting requirements | **Plausible.** Current explicit requirements and incomplete sample coverage can explain the error locally |
| [5.2 Rerun until green][r52] | An unchanged remaining defect is declared fixed after a lucky pass | Earlier failures are displaced by later success during investigation | **Adjacent.** A short debugging episode can produce the same failure |
| [5.3 Wrong test changes correct code][r53] | Tests-only work regresses an already correct implementation | The agent previously implemented, verified, and delivered the module | **Temporal candidate.** Two short rounds establish the dependency, not a long-context effect |
| [5.4 Regression enters snapshot][r54] | Updated expected output hides an unrelated regression | Product edits precede adoption of current output as the new oracle | **Adjacent.** The one-session snapshot layout tests observability, not duration |
| [5.5 Own regression blamed elsewhere][r55] | A newly caused failure is called pre-existing | Prior baseline checks and existing failures must be distinguished at final attribution | **Plausible.** Mixed-red baselines can cause immediate attribution bias |
| [6.1 Handoff loses discovered rules][r61] | Brief omits or reverses a condition and misleads the recipient | Earlier tool-discovered rules were correctly implemented, then their temporary source disappears | **Temporal candidate.** Cross-session persistence is relevant; compaction causation is not established |
| [6.2 Required file omitted][r62] | Local tests pass but the committed checkout lacks a dependency | Inherited local or ignored artifacts are relied on before delivery | **Plausible.** A short session and gitignore visibility alone can explain it |
| [6.3 Wrap-up not delivered][r63] | Continued editing consumes the remaining budget without a handoff report | Unfinished feature work must give way to an explicit handoff obligation | **Temporal candidate.** Missing report, budget cutoff, and a successor’s false claim are separate outcomes |

Source: the 20 linked release mode specifications. Fit assessments are this review’s interpretation, not the source’s measured causal conclusions.

## Reproduction lessons and next steps

1. **Show the dependency before naming the symptom.** Identify the earlier anchor, intervening work or change, later action, effect, and recovery. State what would be lost if the earlier portion were removed.
2. **Reduce setup without solving the task for the agent.** Retain legitimate requirements and discoverable evidence. Remove diagnosis, answer summaries, evaluator labels, and added reminders from the tested agent’s view.
3. **Preserve real competing demands.** A later feature, migration, test request, retry, or handoff should make sense as ordinary work. Do not add filler tickets or artificial waits merely to increase the count.
4. **Verify that the opportunity occurred.** A stale artifact must actually exist and be consumed; a colleague’s change must actually be present; an old test must actually constrain later work. Judge eligibility separately from success and failure.
5. **Check effects independently.** Test product behavior, actions, durable files, or claims against external state. Preserve valid uncertainty, honest blocking, recovery, and legitimate reprioritization as distinct outcomes.
6. **Separate evidence levels.** Historical incidents, checker self-tests, fresh-agent attempts, and matched causal comparisons answer different questions. Keep untested but credible incidents; request missing evidence and evaluation results instead of inventing runs.

The cleanup branch itself warns that elapsed time, repeated stops, and large mechanical edits can exaggerate apparent horizon. It also records that the two- and three-stage `zxi`/`zxj` designs are short calibration probes. Its numerical stop threshold is a local development rule, not a universal admission threshold for this collection. Preserve real session boundaries: a continuous-context experiment, a fresh-session handoff, and a shared-workspace pause test different mechanisms. [Horizon checks][cleanup-horizon], [short controls][cleanup-controls], [continuity checks][cleanup-continuity]

For a causal claim, specify a comparison that removes the suspected historical interference while preserving the legitimate task, tools, authority, and comparable opportunity to succeed. A proposed comparison is enough to retain a candidate; claiming a causal effect requires actual results and a defensible comparison.

## Sources

Release commit: `201294fedc5d1fa7051dd857e6a6876697753fef`.

Cleanup commit: `7dcd0243a991b23114cfbb7a1c6ba6b3397bbcb8`.

Reference definitions pin each link to a source file and line range.

[release-commit]: https://github.com/memory-abstraction-collapse/agent-collapse/tree/201294fedc5d1fa7051dd857e6a6876697753fef

[cleanup-commit]: https://github.com/memory-abstraction-collapse/agent-collapse/tree/7dcd0243a991b23114cfbb7a1c6ba6b3397bbcb8

[cleanup-readme]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/7dcd0243a991b23114cfbb7a1c6ba6b3397bbcb8/README.md#L3-L31

[cleanup-horizon]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/7dcd0243a991b23114cfbb7a1c6ba6b3397bbcb8/runner/precheck.py#L854-L894

[cleanup-controls]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/7dcd0243a991b23114cfbb7a1c6ba6b3397bbcb8/runner/selfevolve_supervisor_plan.json#L22-L43

[cleanup-continuity]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/7dcd0243a991b23114cfbb7a1c6ba6b3397bbcb8/runner/chain_gates.py#L21-L43

[c-zcr]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/7dcd0243a991b23114cfbb7a1c6ba6b3397bbcb8/envs/zcr.py#L15-L68

[c-zdf]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/7dcd0243a991b23114cfbb7a1c6ba6b3397bbcb8/envs/zdf.py#L10-L42

[c-zqn]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/7dcd0243a991b23114cfbb7a1c6ba6b3397bbcb8/envs/zqn.py#L9-L46

[c-zpv]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/7dcd0243a991b23114cfbb7a1c6ba6b3397bbcb8/envs/zpv.py#L11-L46

[c-zsv]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/7dcd0243a991b23114cfbb7a1c6ba6b3397bbcb8/envs/zsv.py#L17-L45

[c-zvk]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/7dcd0243a991b23114cfbb7a1c6ba6b3397bbcb8/envs/zvk.py#L8-L45

[c-zye]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/7dcd0243a991b23114cfbb7a1c6ba6b3397bbcb8/envs/zye.py#L13-L67

[c-zwh]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/7dcd0243a991b23114cfbb7a1c6ba6b3397bbcb8/envs/zwh.py#L45-L68

[c-znx]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/7dcd0243a991b23114cfbb7a1c6ba6b3397bbcb8/envs/znx.py#L47-L85

[c-zrj]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/7dcd0243a991b23114cfbb7a1c6ba6b3397bbcb8/envs/zrj.py#L5-L44

[c-zrh]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/7dcd0243a991b23114cfbb7a1c6ba6b3397bbcb8/envs/zrh.py#L150-L159

[c-zcw]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/7dcd0243a991b23114cfbb7a1c6ba6b3397bbcb8/envs/zcw.py#L6-L26

[r11]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/201294fedc5d1fa7051dd857e6a6876697753fef/suite/modes/1.1-standing-rule-dropped/README.md#L10-L41

[r12]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/201294fedc5d1fa7051dd857e6a6876697753fef/suite/modes/1.2-effective-layer-missed/README.md#L10-L35

[r13]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/201294fedc5d1fa7051dd857e6a6876697753fef/suite/modes/1.3-revocation-incomplete/README.md#L10-L33

[r21]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/201294fedc5d1fa7051dd857e6a6876697753fef/suite/modes/2.1-rule-scope-leak/README.md#L10-L45

[r22]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/201294fedc5d1fa7051dd857e6a6876697753fef/suite/modes/2.2-memory-over-instruction/README.md#L10-L46

[r23]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/201294fedc5d1fa7051dd857e6a6876697753fef/suite/modes/2.3-convention-carried-across-projects/README.md#L10-L39

[r24]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/201294fedc5d1fa7051dd857e6a6876697753fef/suite/modes/2.4-stale-design-note/README.md#L10-L42

[r31]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/201294fedc5d1fa7051dd857e6a6876697753fef/suite/modes/3.1-delivered-feature-broken/README.md#L10-L38

[r32]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/201294fedc5d1fa7051dd857e6a6876697753fef/suite/modes/3.2-colleague-commit-overwritten/README.md#L12-L44

[r33]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/201294fedc5d1fa7051dd857e6a6876697753fef/suite/modes/3.3-rewrite-after-pause/README.md#L10-L43

[r41]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/201294fedc5d1fa7051dd857e6a6876697753fef/suite/modes/4.1-test-secret-persisted/README.md#L10-L26

[r42]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/201294fedc5d1fa7051dd857e6a6876697753fef/suite/modes/4.2-production-credential-used/README.md#L10-L27

[r51]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/201294fedc5d1fa7051dd857e6a6876697753fef/suite/modes/5.1-done-claim-unverified/README.md#L10-L27

[r52]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/201294fedc5d1fa7051dd857e6a6876697753fef/suite/modes/5.2-rerun-until-green/README.md#L10-L23

[r53]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/201294fedc5d1fa7051dd857e6a6876697753fef/suite/modes/5.3-rework-correct-code/README.md#L10-L27

[r54]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/201294fedc5d1fa7051dd857e6a6876697753fef/suite/modes/5.4-regression-into-snapshot/README.md#L10-L25

[r55]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/201294fedc5d1fa7051dd857e6a6876697753fef/suite/modes/5.5-self-break-misattributed/README.md#L10-L28

[r61]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/201294fedc5d1fa7051dd857e6a6876697753fef/suite/modes/6.1-handover-condition-wrong/README.md#L66-L73

[r62]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/201294fedc5d1fa7051dd857e6a6876697753fef/suite/modes/6.2-file-left-out-of-commit/README.md#L74-L81

[r63]: https://github.com/memory-abstraction-collapse/agent-collapse/blob/201294fedc5d1fa7051dd857e6a6876697753fef/suite/modes/6.3-wrapup-notice-ignored/README.md#L77-L84
