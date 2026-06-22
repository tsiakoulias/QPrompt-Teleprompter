# [FOC-N01] focus: true is JS label in atEndLoopDelay SpinBox

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `Prompter.qml:1311`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** Prompter.qml:1311
- **Severity:** Low
- **Analysis:** onValueModified uses colon instead of =. SpinBox never gets focus after value change.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 65 | focus: true JS label in atEndLoopDelay SpinBox (Prompter.qml:1311) |
| gpt | ✅ LEGIT | 78 | focus: true is JS label in atEndLoopDelay SpinBox (src/prompter/Prompter.qml:1311) |
| deepseek | ✅ LEGIT | 88 | focus:true is JS labelled statement not assignment; SpinBox focus never set after value change (Prompter.qml:1311) |
| glm | ✅ LEGIT | 80 | Prompter.qml:1311 focus: true inside onValueModified is JS label not assignment |
| kimi | ✅ LEGIT | 95 | Prompter.qml:1311 `focus: true` inside onValueModified is a JavaScript label, not an assignment, so focus is never set. |
| opus-ultra | ✅ LEGIT | 65 | focus: true JS label in atEndLoopDelay SpinBox (Prompter.qml:1311) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

