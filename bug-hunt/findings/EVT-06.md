# [EVT-06] Drag breaks stopwatch.x binding permanently

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `TimerClock.qml:178,130`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** TimerClock.qml:178,130
- **Severity:** Medium
- **Analysis:** Same pattern. After one drag, stopwatch no longer re-centers on resize.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | drag breaks stopwatch.x binding (TimerClock.qml:178) |
| gpt | ⚠️ PARTIAL | 58 | observed Drag breaks stopwatch.x binding permanently (src/prompter/TimerClock.qml:178) |
| deepseek | ✅ LEGIT | 90 | drag.target:parent writes x imperatively; stopwatch no longer re-centers on resize after one drag (TimerClock.qml:178 130) |
| glm | ✅ LEGIT | 80 | TimerClock.qml:178 130 Drag breaks stopwatch.x binding permanently |
| kimi | ✅ LEGIT | 85 | TimerClock.qml:178 sets drag.target: parent (stopwatch), which imperatively writes x and breaks the x binding at TimerClock.qml:130. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — drag breaks stopwatch.x binding (TimerClock.qml:178) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

