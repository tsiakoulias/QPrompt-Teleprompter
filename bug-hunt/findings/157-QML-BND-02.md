# [157-QML-BND-02] clock.__iteration binding broken by post-decrement in animation handler

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `Countdown.qml:76,116,121`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** Countdown.qml:76,116,121
- **Severity:** Medium
- **Analysis:** `property int __iteration: countdown.__iterations - 1` (line 76) is a declarative binding. Line 116 (`clock.__iteration--`) and 121 (direct assignment) imperatively write to it, breaking the binding. If `__iterations` changes while countdown is running, clock uses stale value.
- **Impact:** Stale iteration count if config changes mid-countdown.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 55 | clock.__iteration binding broken by -- in handler (Countdown.qml:76) |
| gpt | ✅ LEGIT | 78 | clock.iteration binding broken by post-decrement in animation handler (src/prompter/Countdown.qml:76) |
| deepseek | ✅ LEGIT | 90 | clock.__iteration-- at Countdown.qml:116 breaks declarative binding at line 76 |
| glm | ✅ LEGIT | 80 | Countdown.qml:76 116 121 clock.__iteration binding broken by post-decrement in animation handler |
| kimi | ✅ LEGIT | 85 | Countdown.qml:76 binds clock.__iteration, but lines 116/121 use -- and direct assignment, breaking the binding. |
| opus-ultra | ✅ LEGIT | 55 | clock.__iteration binding broken by -- in handler (Countdown.qml:76) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

