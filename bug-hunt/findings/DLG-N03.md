# [DLG-N03] errorDialog MessageDialog has no title

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `Prompter.qml:2510-2513`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** Prompter.qml:2510-2513
- **Severity:** Low
- **Analysis:** Error dialog displayed with blank title bar. closeDialog, restartDialog, factoryResetDialog all set descriptive titles.
- **Impact:** Blank title bar in error dialogs.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | errorDialog MessageDialog has no title (Prompter.qml:2510) |
| gpt | ✅ LEGIT | 78 | errorDialog MessageDialog has no title (src/prompter/Prompter.qml:2510) |
| deepseek | ✅ LEGIT | 90 | errorDialog at Prompter.qml:2510 has no title — blank title bar |
| glm | ✅ LEGIT | 75 | Prompter.qml:2510-2513 errorDialog MessageDialog has no title set |
| kimi | ✅ LEGIT | 80 | Prompter.qml:2510 MessageDialog has no title property, so error dialogs show a blank title bar. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — errorDialog MessageDialog has no title (Prompter.qml:2510) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

