# [R4-ROOT-02] Invalid QML color value "initial"

- **Status:** OPEN
- **Severity:** Medium
- **Category:** QML/UI
- **Location:** `src/kirigami_ui/main.qml:126 (also +windows:121, ProjectionsManager:195)`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/kirigami_ui/main.qml:126 (also +windows:121, ProjectionsManager:195)
- **Severity:** Medium
- **Category:** QML/UI
- **Analysis:** color: root.__translucidBackground ? "transparent" : "initial" — "initial" is CSS keyword, not SVG named color. Not valid in QML color type. Falls back to default (likely black) with runtime warning.
- **Impact:** Disabling background transparency renders window background black instead of system-theme color.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 85 | color initial invalid QML color (main.qml:126) |
| gpt | ✅ LEGIT | 92 | Invalid QML color value "initial" (src/kirigami_ui/main.qml:126) |
| deepseek | ✅ LEGIT | 95 | main.qml:126 color:'initial' is CSS keyword not valid QML color type — falls back to default black with runtime warning |
| glm | ✅ LEGIT | 85 | main.qml:126 color 'initial' is not valid QML color; CSS keyword not supported in QML |
| kimi | ✅ LEGIT | 90 | Window color uses invalid value "initial"; main.qml:126/ProjectionsManager.qml:195/+windows/main.qml:121 |
| opus-ultra | ✅ LEGIT | 85 | color initial invalid QML color (main.qml:126) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

