# [IMP-N02] import QtWebSockets 1.10 — wrong version for Qt 6.5

- **Status:** REJECTED
- **Severity:** Critical
- **Category:** QML/UI
- **Location:** `src/prompter/Prompter.qml:80`
- **Consensus:** 2/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** src/prompter/Prompter.qml:80
- **Severity:** Critical
- **Category:** QML/UI
- **Analysis:** In Qt 6.x, QML WebSocket module uses Qt version number (6.5) not 1.x. Version 1.10 doesn't exist.
- **Impact:** OBS WebSocket remote control integration completely non-functional.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❌ FALSE | 65 | QtWebSockets 1.x import resolves on Qt6 target; OBS feature ships (Prompter.qml:80) |
| gpt | ❌ FALSE | 76 | QtWebSockets QML import version is not the project Qt version (src/prompter/Prompter.qml:80) |
| deepseek | ✅ LEGIT | 80 | Prompter.qml:80 imports QtWebSockets 1.10 — Qt6 registers WebSocket under 6.x only; 1.10 not registered per Qt6 module versioning |
| glm | ⚠️ PARTIAL | 60 | Prompter.qml:80 import QtWebSockets 1.10; versioned import works as minimum in Qt 6.5+ |
| kimi | ✅ LEGIT | 95 | Prompter.qml:80 imports QtWebSockets 1.10; Qt 6 modules use Qt version numbers (e.g., 6.8), so 1.10 is invalid. |
| opus-ultra | ❌ FALSE | 65 | QtWebSockets 1.x import resolves on Qt6 target; OBS feature ships (Prompter.qml:80) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

