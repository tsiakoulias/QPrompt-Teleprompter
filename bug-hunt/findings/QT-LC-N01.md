# [QT-LC-N01] QQmlFileSelector never instantiated — platform QML file selectors dead

- **Status:** REJECTED
- **Severity:** High
- **Category:** 
- **Location:** `main.cpp:33`
- **Consensus:** 1/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** main.cpp:33
- **Severity:** High
- **Analysis:** `#include <QQmlFileSelector>` present but no persistent QQmlFileSelector created and attached to engine. +windows/main.qml and +android/main.qml variants are dead code — base main.qml always loaded on all platforms.
- **Impact:** Platform-specific QML objects (QmlUtil on Windows, RestartDialog) never instantiated. Wrong QML file loaded on all platforms.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❌ FALSE | 70 | QQmlApplicationEngine auto-installs a file selector; +variants demonstrably load (main.cpp:33) |
| gpt | ❌ FALSE | 76 | QQmlApplicationEngine applies file selectors for +android/+windows (src/main.cpp:33) |
| deepseek | ✅ LEGIT | 95 | main.cpp:33: #include <QQmlFileSelector> present but never instantiated/attached; +windows/+android variants dead; base main.qml loads on all platforms |
| glm | ⚠️ PARTIAL | 60 | main.cpp:33 QQmlFileSelector included but never instantiated; platform QML file selectors may not work |
| kimi | ❌ FALSE | 90 | main.cpp:220 uses QQmlApplicationEngine, which Qt 6 docs say automatically installs a QQmlFileSelector |
| opus-ultra | ❌ FALSE | 70 | QQmlApplicationEngine auto-installs a file selector; +variants demonstrably load (main.cpp:33) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

