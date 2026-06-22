# [DBG-N01] OBS WebSocket auth challenge+salt logged to console in release builds

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `Prompter.qml:364,372,386`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** Prompter.qml:364,372,386
- **Severity:** Medium
- **Analysis:** `console.log(m)` logs full WebSocket Hello message including authentication challenge and salt on every connection. `console.info(m)` at line 386 maps to qInfo() — never suppressed. No debug guard.
- **Impact:** Security-sensitive material leaked to console/logs in production.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 60 | console.log(m) logs OBS auth challenge+salt in release (Prompter.qml:372) |
| gpt | ⚠️ PARTIAL | 58 | observed OBS WebSocket auth challenge+salt logged to console in release builds (src/prompter/Prompter.qml:364) |
| deepseek | ✅ LEGIT | 95 | Prompter.qml:364 372 386: console.log(status) + console.log(m) logs full WebSocket Hello including auth challenge+salt; console.info maps to unsuppressed qInfo() |
| glm | ✅ LEGIT | 75 | Prompter.qml:364 372 386 OBS WebSocket auth challenge+salt logged to console in release builds |
| kimi | ✅ LEGIT | 90 | Prompter.qml:364,372 log full WebSocket Hello including authentication challenge and salt; line 386 console.info also logs. |
| opus-ultra | ✅ LEGIT | 60 | console.log(m) logs OBS auth challenge+salt in release (Prompter.qml:372) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

