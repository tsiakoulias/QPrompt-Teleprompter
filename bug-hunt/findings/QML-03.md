# [QML-03] Undefined `root` ID in WindowDragger.qml

- **Status:** OPEN
- **Severity:** Critical
- **Category:** 
- **Location:** `src/qt/WindowDragger.qml:41,45`
- **Consensus:** 5/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** src/qt/WindowDragger.qml:41,45
- **Severity:** Critical
- **Code:**
  ```qml
  property var window: parent   // declared but ignored
  root.x += deltaX;             // root is NOT an id in this file
  root.y += deltaY;
  ```
- **Analysis:** No `id: root` declared in WindowDragger.qml. The file defines `window` for the drag target but uses `root` instead. `root` exists only in `main.qml` files.
- **Impact:** Window dragging via toolbar silently fails on frameless configurations with ReferenceError.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 95 | root undefined in WindowDragger; should be window (WindowDragger.qml:41) |
| gpt | ✅ LEGIT | 92 | Undefined root ID in WindowDragger.qml (src/qt/WindowDragger.qml:41) |
| deepseek | ✅ LEGIT | 75 | WindowDragger.qml uses root at lines 41,45 but no id:root declared; window property at line 28 exists but never referenced — root is undefined |
| glm | ❌ FALSE | 80 | WindowDragger.qml uses root.x/root.y not an undefined root id; the id root is the Item itself |
| kimi | ✅ LEGIT | 90 | WindowDragger.qml:41,45 uses root.x/root.y but no id root in file; property window is unused. |
| opus-ultra | ✅ LEGIT | 95 | root undefined in WindowDragger; should be window (WindowDragger.qml:41) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

