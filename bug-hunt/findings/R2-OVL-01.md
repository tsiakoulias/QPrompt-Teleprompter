# [R2-OVL-01] InputsOverlay onOpened calls cursorAutoHide.restart() instead of reset()

- **Status:** OPEN
- **Severity:** Medium
- **Category:** Logic
- **Location:** `src/kirigami_ui/InputsOverlay.qml:41`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** src/kirigami_ui/InputsOverlay.qml:41
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** All other overlays consistently call `cursorAutoHide.reset()` on open (LanguageSettingsOverlay:40, LayoutDirectionSettingsOverlay:39, WheelSettingsOverlay:36, countdownConfiguration in PrompterPage:1072) to prevent cursor auto-hide. InputsOverlay calls `cursorAutoHide.restart()` which re-enables the auto-hide timer.
- **Impact:** Cursor vanishes during key binding configuration; user forced to move mouse repeatedly.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 65 | cursorAutoHide.restart() on open vs reset() elsewhere (InputsOverlay.qml:41) |
| gpt | ⚠️ PARTIAL | 58 | observed InputsOverlay onOpened calls cursorAutoHide.restart() instead of reset() (src/kirigami_ui/InputsOverlay.qml:41) |
| deepseek | ❔ UNSURE | 35 | restart vs reset at InputsOverlay.qml:41 — need to verify Timer API and intended behavior |
| glm | ✅ LEGIT | 85 | InputsOverlay.qml:41 cursorAutoHide.restart() called on open; should be reset() per the pattern used elsewhere |
| kimi | ✅ LEGIT | 85 | InputsOverlay.qml:41 calls cursorAutoHide.restart() while other overlays call reset(); cursor hides during config. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — cursorAutoHide.restart() on open vs reset() elsewhere (InputsOverlay.qml:41) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

