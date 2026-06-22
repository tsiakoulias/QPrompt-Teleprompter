# [BIND-N01] contentWidth undefined for Shape/Image pointer types — transform origin silently wrong

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `ReadRegionOverlay.qml:396`
- **Consensus:** 3/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** ReadRegionOverlay.qml:396
- **Severity:** Low
- **Analysis:** `(rightPointer.item.width | rightPointer.item.contentWidth) / 2` — contentWidth is Text-only property. For pointer_0 (Shape) and pointer_2 (Image), contentWidth is undefined. `number | undefined` → `ToInt32(undefined)` → 0. Origin depends on low-bit coincidence rather than intended center.
- **Impact:** Right-pointer transform origin silently wrong for Arrow and Image pointer kinds.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | contentWidth undefined for Shape/Image pointer (R4-ROV-03 family) (ReadRegionOverlay.qml:396) |
| gpt | ✅ LEGIT | 92 | contentWidth undefined for Shape/Image pointer types - transform origin silently wrong (src/prompter/ReadRegionOverlay.qml:396) |
| deepseek | ✅ LEGIT | 65 | contentWidth undefined for Shape/Image pointer types; transform origin silently wrong (ReadRegionOverlay.qml:396) |
| glm | ⚠️ PARTIAL | 55 | ReadRegionOverlay.qml:396 contentWidth undefined for Shape/Image pointer types; transform origin wrong |
| kimi | ❌ FALSE | 70 | ReadRegionOverlay.qml:396 uses bitwise OR with contentWidth; JS coerces undefined to 0, so origin falls back to width/2, not arbitrary. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — contentWidth undefined for Shape/Image pointer (R4-ROV-03 family) (ReadRegionOverlay.qml:3 |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

