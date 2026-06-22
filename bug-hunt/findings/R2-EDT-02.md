# [R2-EDT-02] wheelThrottleSettingsButton checked bound to completely unrelated document property

- **Status:** OPEN
- **Severity:** High
- **Category:** QML/UI
- **Location:** `src/kirigami_ui/EditorToolbar.qml:790`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** src/kirigami_ui/EditorToolbar.qml:790
- **Severity:** High
- **Category:** QML/UI
- **Analysis:** `checked: viewport.prompter.document.namedMarker` and `onClicked: wheelSettings.open()`. Button opens wheel/scroll settings but checked state bound to named marker property — a copy-paste error from namedBookmarkButton (line 233).
- **Impact:** Wheel settings button toggle state controlled by whether a named marker exists, semantically unrelated to wheel settings.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 85 | wheel button checked bound to document.namedMarker (EditorToolbar.qml:790) |
| gpt | ✅ LEGIT | 84 | wheelThrottleSettingsButton checked bound to completely unrelated document property (src/kirigami_ui/EditorToolbar.qml:790) |
| deepseek | ❔ UNSURE | 35 | wheelThrottleSettingsButton checked bound to namedMarker at EditorToolbar.qml:790; need full QML to verify if this is intentional or copy-paste |
| glm | ✅ LEGIT | 90 | EditorToolbar.qml:790 wheelThrottleSettingsButton checked bound to document.namedMarker (unrelated property) |
| kimi | ✅ LEGIT | 90 | EditorToolbar.qml:790 wheelThrottleSettingsButton checked bound to document.namedMarker instead of wheel setting. |
| opus-ultra | ✅ LEGIT | 85 | wheel button checked bound to document.namedMarker (EditorToolbar.qml:790) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

