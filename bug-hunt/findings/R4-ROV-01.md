# [R4-ROV-01] Division by zero in __customPlacement when overlay full

- **Status:** OPEN
- **Severity:** High
- **Category:** Edge Case
- **Location:** `src/prompter/ReadRegionOverlay.qml:189`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** src/prompter/ReadRegionOverlay.qml:189
- **Severity:** High
- **Category:** Edge Case
- **Analysis:** readRegion.y / (overlay.height - readRegion.height) — when read region fills full overlay (equal heights), denominator 0 → Infinity → NaN propagation.
- **Impact:** Read region position corrupted; overlay unusable until value reset externally.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 60 | div-by-zero only when readRegion fills overlay (ReadRegionOverlay.qml:189) |
| gpt | ⚠️ PARTIAL | 58 | observed Division by zero in __customPlacement when overlay full (src/prompter/ReadRegionOverlay.qml:189) |
| deepseek | ✅ LEGIT | 90 | ReadRegionOverlay.qml:189 readRegion.y/(overlay.height-readRegion.height) — when readRegion fills overlay denominator=0 — Infinity/NaN |
| glm | ✅ LEGIT | 80 | ReadRegionOverlay.qml:189 division by zero in __customPlacement when overlay.height equals readRegion.height |
| kimi | ✅ LEGIT | 95 | ReadRegionOverlay.qml:189 divides readRegion.y by (overlay.height-readRegion.height); denominator 0 when heights equal, yielding Infinity/NaN. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — div-by-zero only when readRegion fills overlay (ReadRegionOverlay.qml:189) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

