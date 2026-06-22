# [LYR-N01] InputsOverlay calls cursorAutoHide.restart() on open instead of reset()

- **Status:** OPEN
- **Severity:** High
- **Category:** Logic
- **Location:** `src/kirigami_ui/InputsOverlay.qml:41`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** src/kirigami_ui/InputsOverlay.qml:41
- **Severity:** High
- **Category:** Logic
- **Analysis:** All other overlays call reset() on open (stop timer, show cursor). InputsOverlay calls restart() (re-enables auto-hide). Cursor hides after 1 second while user configuring key bindings.
- **Impact:** Cursor vanishes during key binding configuration. User locked out of overlay.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 60 | cursorAutoHide.restart() on open vs reset() elsewhere (dup R2-OVL-01) (InputsOverlay.qml:41) |
| gpt | ✅ LEGIT | 84 | InputsOverlay calls cursorAutoHide.restart() on open instead of reset() (src/kirigami_ui/InputsOverlay.qml:41) |
| deepseek | ✅ LEGIT | 85 | InputsOverlay.qml:41 onOpened calls cursorAutoHide.restart() instead of reset() — cursor auto-hides after 1s during key binding configuration |
| glm | ✅ LEGIT | 85 | InputsOverlay.qml:41 cursorAutoHide.restart() on open instead of reset(); restart re-triggers hide timer |
| kimi | ✅ LEGIT | 90 | InputsOverlay.qml:41 calls cursorAutoHide.restart(); other overlays call reset(), so cursor auto-hides during key binding. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — cursorAutoHide.restart() on open vs reset() elsewhere (dup R2-OVL-01) (InputsOverlay.qml:4 |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

