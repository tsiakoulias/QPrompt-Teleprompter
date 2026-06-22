# [RESP-N03] +android/main.qml omits all size declarations — transient zero-size layout on startup

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `+android/main.qml`
- **Consensus:** 3/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** +android/main.qml
- **Severity:** Low
- **Analysis:** No width/height/minimum declarations. Child bindings dependent on root.width evaluate against 0/undefined before window sized. Toolbars flash as window resizes from zero to full screen.
- **Impact:** Transient layout collapse on Android startup.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | +android omits size declarations; transient zero-size (main.qml) |
| gpt | ⚠️ PARTIAL | 58 | observed +android/main.qml omits all size declarations - transient zero-size layout on startup (src/kirigami_ui/+android/main.qml:1) |
| deepseek | ❌ FALSE | 85 | +android/main.qml is dead code (QML file selectors never instantiated per QT-LC-N01); base main.qml always loads with proper width/height |
| glm | ✅ LEGIT | 65 | +android/main.qml omits all size declarations; transient zero-size layout on startup |
| kimi | ✅ LEGIT | 70 | +android/main.qml lacks explicit width/height/minimumWidth; relies only on Settings aliases |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — +android omits size declarations; transient zero-size (main.qml) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

