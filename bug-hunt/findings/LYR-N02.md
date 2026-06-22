# [LYR-N02] Three OverlaySheets missing from ESC dismiss chain

- **Status:** OPEN
- **Severity:** Medium
- **Category:** Logic
- **Location:** `src/kirigami_ui/main.qml:489-504`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** src/kirigami_ui/main.qml:489-504
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** obsConfiguration, dictionariesSheet, customWordsSheet added to PrompterPage after ESC handler. Not in the if-else chain. ESC falls through without closing them.
- **Impact:** ESC doesn't close OBS/dictionary/custom-words sheets. User must click close button.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | three OverlaySheets missing from ESC dismiss chain (main.qml:489) |
| gpt | ✅ LEGIT | 78 | Three OverlaySheets missing from ESC dismiss chain (src/kirigami_ui/main.qml:489) |
| deepseek | ✅ LEGIT | 75 | main.qml:489-504 ESC if-else chain missing obsConfiguration/dictionariesSheet/customWordsSheet — these 3 sheets never dismissed by ESC |
| glm | ⚠️ PARTIAL | 65 | main.qml:489-504 ESC handler chain missing three OverlaySheets from dismiss chain |
| kimi | ✅ LEGIT | 90 | main.qml:489-504 ESC handler omits obsConfiguration, dictionariesSheet and customWordsSheet defined in PrompterPage. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — three OverlaySheets missing from ESC dismiss chain (main.qml:489) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

