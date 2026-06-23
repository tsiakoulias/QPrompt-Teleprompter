# [442-SHADOW-01] id: rotation shadows Item.rotation property

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `Prompter.qml:1280`
- **Consensus:** 4/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** Prompter.qml:1280
- **Severity:** Low
- **Analysis:** Rotation transform has id: rotation. Flipable inherits Item.rotation (qreal). Bare rotation resolves to Rotation object, not the float.
- **Impact:** Future code reading bare rotation gets wrong type.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 60 | id: rotation shadows Item.rotation property (Prompter.qml:1280) |
| gpt | ✅ LEGIT | 78 | id: rotation shadows Item.rotation property (src/prompter/Prompter.qml:1280) |
| deepseek | ✅ LEGIT | 85 | Rotation id:rotation shadows Item.rotation qreal; bare rotation resolves to Rotation object not float (Prompter.qml:1280) |
| glm | ⚠️ PARTIAL | 60 | Prompter.qml:1280 id: rotation shadows Item.rotation property; ambiguous in context |
| kimi | ❌ FALSE | 80 | id:rotation names the Rotation transform and is correctly used as its target; current code does not confuse it with Item.rotation. |
| opus-ultra | ✅ LEGIT | 60 | id: rotation shadows Item.rotation property (Prompter.qml:1280) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

