# [R2-AND-02] Android missing restartDialog crashes LanguageSettingsOverlay and LayoutDirectionSettingsOverlay

- **Status:** OPEN
- **Severity:** Critical
- **Category:** QML/UI
- **Location:** `src/kirigami_ui/+android/main.qml (absent object)`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** src/kirigami_ui/+android/main.qml (absent object)
- **Severity:** Critical
- **Category:** QML/UI
- **Analysis:** Both overlays unconditionally access `restartDialog.visible = true` in onClosed handlers when settings are dirty. `restartDialog` is defined in Windows (line 751-769) and base (line 1083-1098) but absent from +android/main.qml.
- **Impact:** Changing UI language or layout direction on Android crashes app when overlay is dismissed.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 90 | no restartDialog -> overlay crash (+android) |
| gpt | ✅ LEGIT | 84 | Android missing restartDialog crashes LanguageSettingsOverlay and LayoutDirectionSettingsOverlay (src/kirigami_ui/+android/main.qml:1) |
| deepseek | ❔ UNSURE | 35 | Android restartDialog absence — same inheritance question as R2-AND-01 |
| glm | ✅ LEGIT | 80 | +android/main.qml references restartDialog but no MessageDialog with that id declared in android variant |
| kimi | ✅ LEGIT | 95 | +android/main.qml has no restartDialog; LanguageSettingsOverlay.qml:48 / LayoutDirectionSettingsOverlay.qml:47 require it. |
| opus-ultra | ✅ LEGIT | 90 | no restartDialog -> overlay crash (+android) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

