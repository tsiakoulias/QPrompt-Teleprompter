# [STC-N04] Projection window CursorAutoHide not reset on close — cursor permanently hidden

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `ProjectionsManager.qml:202-206,196-200`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** ProjectionsManager.qml:202-206,196-200
- **Severity:** Medium
- **Analysis:** onClosing never calls cursorAutoHide.reset(). If cursor was hidden by auto-hide timer, system cursor stays hidden after window destruction.
- **Impact:** Cursor permanently invisible until user moves mouse or opens another overlay.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | projection CursorAutoHide not reset on close (ProjectionsManager.qml:202) |
| gpt | ⚠️ PARTIAL | 58 | observed Projection window CursorAutoHide not reset on close - cursor permanently hidden (src/prompter/ProjectionsManager.qml:202) |
| deepseek | ✅ LEGIT | 85 | ProjectionsManager.qml:202-206 196-200: onClosing never calls cursorAutoHide.reset(); cursor stays hidden system-wide after window destruction |
| glm | ✅ LEGIT | 70 | ProjectionsManager.qml:202-206 196-200 projection window CursorAutoHide not reset on close; cursor permanently hidden |
| kimi | ✅ LEGIT | 75 | ProjectionsManager.qml:196-206 onClosing removes window without cursorAutoHide.reset(); hidden cursor may persist |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — projection CursorAutoHide not reset on close (ProjectionsManager.qml:202) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

