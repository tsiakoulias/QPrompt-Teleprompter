# [DPI-02] MarkersDrawer.qml:37 drawer minimumWidth hardcoded to 260px

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `MarkersDrawer.qml:37`
- **Consensus:** 3/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** MarkersDrawer.qml:37
- **Severity:** Low
- **Analysis:** `minimumWidth: 260` in px. On 200% DPI this is 130 logical px — drawer too narrow to read marker labels.
- **Impact:** Unusable drawer on high DPI.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | drawer minimumWidth hardcoded 260px (MarkersDrawer.qml:37) |
| gpt | ⚠️ PARTIAL | 58 | visual issue is plausible but depends on theme or device (src/kirigami_ui/MarkersDrawer.qml:37) |
| deepseek | ✅ LEGIT | 85 | Hardcoded 260px width at MarkersDrawer.qml:37 — ignores DPI scaling |
| glm | ✅ LEGIT | 75 | MarkersDrawer.qml:37 drawer minimumWidth hardcoded to 260px |
| kimi | ❌ FALSE | 75 | MarkersDrawer.qml:37 width is in QML logical pixels, not raw pixels; high-DPR does not halve it. Layout width concern is overstated. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — drawer minimumWidth hardcoded 260px (MarkersDrawer.qml:37) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

