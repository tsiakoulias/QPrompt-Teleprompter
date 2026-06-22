# [R4-ROV-03] Bitwise OR | used for width fallback instead of logical OR

- **Status:** OPEN
- **Severity:** Medium
- **Category:** Logic
- **Location:** `src/prompter/ReadRegionOverlay.qml:396`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** src/prompter/ReadRegionOverlay.qml:396
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** (rightPointer.item.width | rightPointer.item.contentWidth) / 2 — bitwise OR on two non-zero ints produces garbage combination (50|60=62), wrong origin. Meant to be || or ternary.
- **Impact:** Right pointer icon appears off-center when both width and contentWidth have non-zero values.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 90 | bitwise \| for width (ReadRegionOverlay.qml:396) |
| gpt | ✅ LEGIT | 78 | Bitwise OR \| used for width fallback instead of logical OR (src/prompter/ReadRegionOverlay.qml:396) |
| deepseek | ✅ LEGIT | 95 | ReadRegionOverlay.qml:396 bitwise OR \| on two non-zero ints(eg 50\|60=62) instead of logical \|\| or ternary — right pointer origin off-center |
| glm | ⚠️ PARTIAL | 65 | ReadRegionOverlay.qml:396 bitwise \| for width fallback; works but should be logical \|\| |
| kimi | ✅ LEGIT | 95 | ReadRegionOverlay.qml:396 uses bitwise OR (width\|contentWidth)/2 instead of logical OR/ternary, producing wrong transform origin. |
| opus-ultra | ✅ LEGIT | 90 | bitwise \| for width (ReadRegionOverlay.qml:396) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

