# [AND-HIGH-01] Android back button doesn't dismiss overlays/drawers before close

- **Status:** OPEN
- **Severity:** High
- **Category:** 
- **Location:** `+android/main.qml:144-150, PrompterPage.qml:64`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** +android/main.qml:144-150, PrompterPage.qml:64
- **Severity:** High
- **Analysis:** PrompterPage.onBackRequested triggers close() directly. ESC key cascade (dismiss layers→drawers→overlays→find→exit prompting) absent from back button. Any open overlay/drawer triggers save-before-close instead of dismiss.
- **Impact:** Broken Android UX — cannot dismiss overlays with back button.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | Android back button overlay-dismissal claim; domain (main.qml:144) |
| gpt | ⚠️ PARTIAL | 58 | observed Android back button doesn't dismiss overlays/drawers before close (src/kirigami_ui/+android/main.qml:144) |
| deepseek | ✅ LEGIT | 80 | +android/main.qml:144-150: onClosing only handles save dialog (modified check); ESC dismiss cascades (layers->drawers->overlays->find) absent from back button — cannot dismiss overlays |
| glm | ✅ LEGIT | 80 | +android/main.qml:144-150 back button doesn't dismiss overlays/drawers before close |
| kimi | ✅ LEGIT | 80 | +android/main.qml:144-150 onClosing checks modified only; PrompterPage.qml:64 onBackRequested closes without dismissing overlays/drawers. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — Android back button overlay-dismissal claim; domain (main.qml:144) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

