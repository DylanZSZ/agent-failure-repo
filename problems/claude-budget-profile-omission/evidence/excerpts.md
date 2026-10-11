# Selected historical excerpts

Updated 2026-10-11. Source alias: history-campaign-a. Each block is an exact selection of ordinary visible message/tool-result lines, with unrelated lines omitted. No private reasoning is included. The source file map and complete selected events remain local. Owner authorized submission of this prepared file set on 2026-10-11; full histories remain private.

## Source L7432 — 2026-09-03T08:39:48.596Z — user

```text
            <command-args>increase the total amount of GPU hours allowed to 5000 GPU-hours and run it.</command-args>
```

## Source L7455 — 2026-09-03T08:44:31.688Z — user

```text
authority sum(lanes)=4800.0 + unalloc 200.0 = 5000.0 (OUTER 5000.0)
ops sum(lanes)=4800 (outer 5000)
PATCHED OK
 2 files changed, 15 insertions(+), 15 deletions(-)
```

## Source L7618 — 2026-09-03T08:59:25.918Z — assistant

```text
**Goal 1 — total GPU-hour ceiling → 5000: DONE and deployed.**
- `OUTER_GPU_H` 83.3925 → **5000.0** (both authority + ops, invariant holds), per-lane sub-caps scaled ×60 (720–1320 GPU-h each, up from 12–22).
- Rebuilt as sealed release v12 (`17ec252a`), deployed + verified on nrt, re-commissioned — **init accepted the 5000 budget cleanly**.
```

## Source L7842 — 2026-09-03T09:36:16.150Z — user

```text
ee56c2 plan refused: PlanError: program-accounting authority drifted
```

## Source L7884 — 2026-09-03T09:39:16.297Z — assistant

```text
Root cause found — I missed a **third** place the budget lives. `cluster/profiles.yaml:88` carries a `program_accounting` data field that still has the **old** budget:
I changed `OUTER_GPU_H`/`LANE_GPU_H` in the two code files but not this profiles data — so the loaded config (83.3925) drifts from the constant (5000). I need to update it + recompute `control_config_sha256`. Let me find how that sha is computed:
```

## Source L7926 — 2026-09-03T09:42:46.885Z — user

```text
outer_gpu_seconds: 18000000 (want 18000000)
```

