# [R4-QTV-02] QtQuick.Window 2.0 import does not exist in Qt 6.5

- **Status:** REJECTED
- **Severity:** Critical
- **Category:** QML/UI
- **Location:** `src/prompter/ReadRegionOverlay.qml:25`
- **Consensus:** 1/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** src/prompter/ReadRegionOverlay.qml:25
- **Severity:** Critical
- **Category:** QML/UI
- **Analysis:** QtQuick.Window 2.0 from Qt 5.0 era. Qt 6 merged it into QtQuick; only provides backward compat at 2.15 and 6.x. Module-not-found at runtime.
- **Impact:** ReadRegionOverlay.qml fails to load; reading region overlay (bars, pointers, controls) completely broken.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❌ FALSE | 90 | QtQuick.Window 2.0 valid on Qt 6.8.2 |
| gpt | ❌ FALSE | 76 | QtQuick.Window 2.0 is valid with the 6.8.2 target (src/prompter/ReadRegionOverlay.qml:25) |
| deepseek | ❔ UNSURE | 60 | ReadRegionOverlay.qml:25 imports QtQuick.Window 2.0 — Qt6 may provide version-mapping for 2.x imports but 2.0 predates 2.15 compat; cannot confirm |
| glm | ❌ FALSE | 80 | ReadRegionOverlay.qml:25 import QtQuick.Window 2.0 is minimum; valid in Qt 6 |
| kimi | ✅ LEGIT | 80 | ReadRegionOverlay.qml:25 imports QtQuick.Window 2.0 |
| opus-ultra | ❌ FALSE | 90 | QtQuick.Window 2.0 valid on Qt 6.8.2 |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

