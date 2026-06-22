# [ARC-01] Velocity physics engine entirely in QML (~20 readonly property bindings)

- **Status:** OPEN
- **Severity:** 
- **Category:** 
- **Location:** `Prompter.qml:113-129`
- **Consensus:** 1/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** Prompter.qml:113-129
- **Analysis:** Core teleprompter behavior — `__speed`, `__velocity`, `__relativeSpeed`, `__timeToEnd`, `__destination`, `__jitterMargin`, `__speedLimit` — all in QML bindings with Math.pow, division, branching. Cannot be unit-tested; fragile to QML engine behavioral changes.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 35 | velocity physics in QML; architectural (Prompter.qml:113) |
| gpt | ⚠️ PARTIAL | 48 | maintainability issue observed, but no direct runtime bug shown (src/prompter/Prompter.qml:113) |
| deepseek | ❌ FALSE | 50 | architectural observation; readonly property bindings are a valid QML design pattern |
| glm | ⚠️ PARTIAL | 55 | Prompter.qml:113-129 velocity physics in QML with ~20 readonly property bindings; architectural concern not a bug |
| kimi | ✅ LEGIT | 60 | Prompter.qml:113-129 velocity physics (__speed,__velocity,__timeToEnd,etc.) implemented entirely in QML readonly bindings. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — velocity physics in QML; architectural (Prompter.qml:113) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

