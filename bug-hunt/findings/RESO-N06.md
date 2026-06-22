# [RESO-N06] ReadRegionOverlay pointer margin 3dp — overlap with text at large fonts

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `ReadRegionOverlay.qml:260,267`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** ReadRegionOverlay.qml:260,267
- **Severity:** Low
- **Impact:** Pointer icons collide with text at large prompter font sizes.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 40 | pointer margin 3dp overlap at large fonts (ReadRegionOverlay.qml:260) |
| gpt | ⚠️ PARTIAL | 48 | visual issue is plausible but depends on theme or device (src/prompter/ReadRegionOverlay.qml:260) |
| deepseek | ✅ LEGIT | 80 | ReadRegionOverlay.qml:260 267: pointer margin 3dp; overlaps text at large font sizes |
| glm | ⚠️ PARTIAL | 55 | ReadRegionOverlay.qml:260 267 pointer margin 3dp; overlap with text at large fonts |
| kimi | ✅ LEGIT | 70 | ReadRegionOverlay.qml:260/267 set pointer margins to 3, causing overlap at large font sizes |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — pointer margin 3dp overlap at large fonts (ReadRegionOverlay.qml:260) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

