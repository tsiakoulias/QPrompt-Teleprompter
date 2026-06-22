# [WARN-N04] QProcess::startDetached() bool return silently ignored

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `qmlutil.hpp:91`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** qmlutil.hpp:91
- **Severity:** Low
- **Analysis:** `startDetached()` returns bool. Discarded. If program not found, failure invisible — no error logged, no QML notification.
- **Impact:** Silent failure of sys:// URL handler and app restart on missing program.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 55 | startDetached bool return ignored (qmlutil.hpp:91) |
| gpt | ⚠️ PARTIAL | 58 | observed QProcess::startDetached() bool return silently ignored (src/qmlutil.hpp:91) |
| deepseek | ✅ LEGIT | 95 | qmlutil.hpp:91: QProcess::startDetached() returns bool — discarded; if program not found failure is silent with no error log or QML notification |
| glm | ✅ LEGIT | 70 | qmlutil.hpp:91 QProcess::startDetached() bool return silently ignored |
| kimi | ✅ LEGIT | 70 | qmlutil.hpp:91 discards QProcess::startDetached() return value; failure to launch is silent. |
| opus-ultra | ✅ LEGIT | 55 | startDetached bool return ignored (qmlutil.hpp:91) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

