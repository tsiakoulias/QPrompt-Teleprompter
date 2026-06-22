# [DRW-01] interalFocusElsewhere() misses 3 OverlaySheets + 2 Drawers — hotkeys pass through

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `Prompter.qml:283-296`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** Prompter.qml:283-296
- **Severity:** Medium
- **Analysis:** Function blocks hotkeys when overlays open, but omits obsConfiguration, dictionariesSheet, customWordsSheet, contextDrawer, globalMenu. Hotkeys (play/pause/stop) execute through while configuring OBS/dictionaries/words or with drawer open.
- **Impact:** Unexpected prompter state changes while interacting with overlays/drawers.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | interalFocusElsewhere() misses sheets/drawers -> hotkey passthrough (Prompter.qml:283) |
| gpt | ⚠️ PARTIAL | 58 | observed interalFocusElsewhere() misses 3 OverlaySheets + 2 Drawers - hotkeys pass through (src/prompter/Prompter.qml:283) |
| deepseek | ✅ LEGIT | 88 | hotkey guard misses obsConfiguration dictionariesSheet customWordsSheet contextDrawer globalMenu (Prompter.qml:283-296) |
| glm | ⚠️ PARTIAL | 65 | Prompter.qml:283-296 interalFocusElsewhere misses 3 OverlaySheets + 2 Drawers; hotkeys pass through |
| kimi | ✅ LEGIT | 85 | Prompter.qml:283-296 omits obsConfiguration/dictionariesSheet/customWordsSheet/globalMenu/contextDrawer; hotkeys pass through open overlays/drawers. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — interalFocusElsewhere() misses sheets/drawers -> hotkey passthrough (Prompter.qml:283) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

