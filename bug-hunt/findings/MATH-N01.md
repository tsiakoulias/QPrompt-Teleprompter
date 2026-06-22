# [MATH-N01] Division by zero in __timeToArival/__timeToEnd when speed=0

- **Status:** OPEN
- **Severity:** High
- **Category:** Logic
- **Location:** `src/prompter/Prompter.qml:121-123`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/prompter/Prompter.qml:121-123
- **Severity:** High
- **Category:** Logic
- **Analysis:** __relativeSpeed=0 when __speed=0 or fontSize=0 → division by zero → Infinity assigned to NumberAnimation duration. No isFinite guard.
- **Impact:** Teleprompter scrolling freezes permanently when speed slider hits 0.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 65 | speed=0 -> __relativeSpeed=0 -> __timeToEnd = x/0 = Infinity (Prompter.qml:121) |
| gpt | ✅ LEGIT | 84 | Division by zero in timeToArival/timeToEnd when speed=0 (src/prompter/Prompter.qml:121) |
| deepseek | ✅ LEGIT | 95 | Prompter.qml:121-123 __relativeSpeed=0 when __speed=0 or fontSize=0 — division by zero produces Infinity for NumberAnimation duration; no isFinite guard |
| glm | ✅ LEGIT | 85 | Prompter.qml:121-123 __timeToEnd/__timeToArival divide by __relativeSpeed which is 0 when speed=0; division by zero |
| kimi | ✅ LEGIT | 90 | Prompter.qml:122 divides by __relativeSpeed which is zero when speed/fontSize is zero, producing Infinity for animation duration. |
| opus-ultra | ✅ LEGIT | 65 | speed=0 -> __relativeSpeed=0 -> __timeToEnd = x/0 = Infinity (Prompter.qml:121) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

