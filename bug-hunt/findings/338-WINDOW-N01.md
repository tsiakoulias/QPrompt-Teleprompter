# [338-WINDOW-N01] Projection windows not closed on main window close — orphaned on Linux

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `main.qml:159-165, +windows:154-160, +android:144-150`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** main.qml:159-165, +windows:154-160, +android:144-150
- **Severity:** Medium
- **Analysis:** onClosing opens save dialog if modified but never calls projectionManager.closeAll() or sets isEnabled=false. Projection Windows with transientParent:root: on Windows/macOS may auto-hide but on Linux/X11, transient children not guaranteed to close when parent closes.
- **Impact:** Orphaned projection windows remain on-screen after app exits on Linux.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | projection windows may orphan on main-window close; lifecycle (main.qml:159) |
| gpt | ⚠️ PARTIAL | 58 | observed Projection windows not closed on main window close - orphaned on Linux (src/kirigami_ui/main.qml:159) |
| deepseek | ✅ LEGIT | 85 | main.qml:159-165/+android:144-150/+windows:154-160: onClosing only handles save dialog; no projectionManager.closeAll() or isEnabled=false — orphaned projection windows on Linux |
| glm | ✅ LEGIT | 75 | main.qml:159-165 projection windows not closed on main window close; orphaned on Linux |
| kimi | ✅ LEGIT | 85 | main.qml/+windows/+android onClosing handlers never close projectionManager windows. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — projection windows may orphan on main-window close; lifecycle (main.qml:159) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

