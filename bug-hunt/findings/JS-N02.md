# [JS-N02] markerCompare() per-frame JSON.stringify() over OBS marker — 60 allocs/sec

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `Prompter.qml:401-413`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** Prompter.qml:401-413
- **Severity:** Medium
- **Analysis:** Creates new object literal + JSON.stringify() EVERY FRAME (60fps) over OBS marker in read region. Same scene name stringified repeatedly. No guard to fire only on marker entry.
- **Impact:** Severe GC pressure — 180+ heap allocs/sec during OBS-connected prompting.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | per-frame JSON.stringify over OBS marker; allocations (Prompter.qml:401) |
| gpt | ⚠️ PARTIAL | 58 | observed markerCompare() per-frame JSON.stringify() over OBS marker - 60 allocs/sec (src/prompter/Prompter.qml:401) |
| deepseek | ✅ LEGIT | 85 | Prompter.qml:401-413: markerCompare fires every frame; JSON.stringify + object creation 60fps; severe GC pressure during OBS prompting |
| glm | ✅ LEGIT | 75 | Prompter.qml:401-413 markerCompare() per-frame JSON.stringify() over OBS marker; 60 allocs/sec |
| kimi | ✅ LEGIT | 90 | Prompter.qml:413 calls JSON.stringify(req) each frame while an OBS scene marker is in the read region |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — per-frame JSON.stringify over OBS marker; allocations (Prompter.qml:401) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

