# [R4-ROOT-01] Qt.openUrlExternally called with translation context string instead of URL

- **Status:** OPEN
- **Severity:** High
- **Category:** QML/UI
- **Location:** `src/kirigami_ui/main.qml:899`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/kirigami_ui/main.qml:899
- **Severity:** High
- **Category:** QML/UI
- **Analysis:** Qt.openUrlExternally("Global menu actions", "https://feedback.qprompt.app") — first arg is the qsTr disambiguation string copy-pasted from previous line. "Global menu actions" treated as URL; real URL ignored/triggers warning.
- **Impact:** "Report Bug" menu item opens nothing. Users cannot reach feedback page.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 90 | openUrlExternally first arg is the URL (main.qml:898) |
| gpt | ✅ LEGIT | 84 | Qt.openUrlExternally called with translation context string instead of URL (src/kirigami_ui/main.qml:899) |
| deepseek | ✅ LEGIT | 95 | main.qml:898 Qt.openUrlExternally('Global menu actions' 'https://...') — first arg is qsTr disambiguation string not URL; real URL ignored |
| glm | ✅ LEGIT | 85 | main.qml:899 Qt.openUrlExternally('Global menu actions' 'https://...') passes disambiguation string as first arg |
| kimi | ✅ LEGIT | 95 | Qt.openUrlExternally called with translation context string first and URL second; URL ignored; main.qml:898 |
| opus-ultra | ✅ LEGIT | 90 | openUrlExternally first arg is the URL (main.qml:898) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

