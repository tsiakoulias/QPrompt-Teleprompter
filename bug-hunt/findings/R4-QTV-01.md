# [R4-QTV-01] QtQuick 2.13 import does not exist in Qt 6.5

- **Status:** REJECTED
- **Severity:** Critical
- **Category:** QML/UI
- **Location:** `src/prompter/ProjectionsManager.qml:22`
- **Consensus:** 2/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** src/prompter/ProjectionsManager.qml:22
- **Severity:** Critical
- **Category:** QML/UI
- **Analysis:** Qt 6 registers QtQuick as 6.x and 2.15 for backward compat. Version 2.13 not registered. QML engine finds no module with major=2 and minor≤13 (2.15 > 2.13 excluded). Module-not-found error at runtime.
- **Impact:** ProjectionsManager.qml fails to load; all external display/projector mirroring completely non-functional.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❌ FALSE | 90 | QtQuick 2.13 valid on Qt 6; target 6.8.2 |
| gpt | ❌ FALSE | 76 | QtQuick 2.x import remains valid on Qt 6.8.2 (src/prompter/ProjectionsManager.qml:22) |
| deepseek | ✅ LEGIT | 95 | ProjectionsManager.qml:22 imports QtQuick 2.13 — Qt 6 registers QtQuick only as 6.x and 2.15 backward compat; 2.13 not registered |
| glm | ❌ FALSE | 80 | ProjectionsManager.qml:22 import QtQuick 2.13 is a minimum version; valid in Qt 6.8.2 |
| kimi | ✅ LEGIT | 80 | ProjectionsManager.qml:22 imports QtQuick 2.13 |
| opus-ultra | ❌ FALSE | 90 | QtQuick 2.13 valid on Qt 6; target 6.8.2 |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

