# [R3-MAIN-05] Hardcoded Homebrew version-specific Kirigami import path

- **Status:** OPEN
- **Severity:** Medium
- **Category:** Platform/Build
- **Location:** `src/main.cpp:314`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** src/main.cpp:314
- **Severity:** Medium
- **Category:** Platform/Build
- **Analysis:** /opt/homebrew/Cellar/kf5-kirigami2/5.95.0/lib/qt6/qml — every brew upgrade changes directory → path stale. QQmlEngine::addImportPath silently ignores missing dirs.
- **Impact:** After Homebrew upgrade, Kirigami QML imports fail silently. App starts with blank window.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 80 | hardcoded Homebrew Cellar Kirigami path (main.cpp:314) |
| gpt | ⚠️ PARTIAL | 58 | visual issue is plausible but depends on theme or device (src/main.cpp:314) |
| deepseek | ✅ LEGIT | 98 | main.cpp:314 hardcoded /opt/homebrew/Cellar/kf5-kirigami2/5.95.0/lib/qt6/qml — every brew upgrade breaks path |
| glm | ✅ LEGIT | 80 | main.cpp:314 hardcoded Homebrew version-specific Kirigami import path /opt/homebrew/Cellar/kf5-kirigami2/5.95.0/lib/qt6/qml |
| kimi | ✅ LEGIT | 85 | main.cpp:314 hardcodes /opt/homebrew/Cellar/kf5-kirigami2/5.95.0/lib/qt6/qml; brittle, breaks when Homebrew formula version changes. |
| opus-ultra | ✅ LEGIT | 80 | hardcoded Homebrew Cellar Kirigami path (main.cpp:314) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

