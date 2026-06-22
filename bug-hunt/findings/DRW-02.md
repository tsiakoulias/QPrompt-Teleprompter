# [DRW-02] globalDrawer and contextDrawer missing from ESC dismiss chain

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `main.qml:481-504, +windows:452-487, +android:391-426`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** main.qml:481-504, +windows:452-487, +android:391-426
- **Severity:** Medium
- **Analysis:** ESC handler checks markersDrawer + 8 sheets but never checks contextDrawer.drawerOpen or globalMenu.drawerOpen. ESC falls through, drawer stays open.
- **Impact:** ESC does not close global/context drawer; user must manually tap outside.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | globalDrawer/contextDrawer not in ESC dismiss chain (main.qml:481) |
| gpt | ⚠️ PARTIAL | 58 | observed globalDrawer and contextDrawer missing from ESC dismiss chain (src/kirigami_ui/main.qml:481) |
| deepseek | ✅ LEGIT | 88 | ESC handler checks 8 sheets but not contextDrawer.drawerOpen nor globalMenu.drawerOpen; drawer stays (main.qml:481-504) |
| glm | ⚠️ PARTIAL | 65 | main.qml:481-504 ESC handler missing globalDrawer and contextDrawer from dismiss chain |
| kimi | ✅ LEGIT | 85 | main.qml:481-504 closes markersDrawer and overlay sheets but never checks contextDrawer.drawerOpen or globalMenu.drawerOpen. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — globalDrawer/contextDrawer not in ESC dismiss chain (main.qml:481) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

