# [PLAT-N01] qmlutil.hpp incorrectly excludes QNX from QProcess — run()/restartApplication() silently no-op

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `qmlutil.hpp:35,86,99`
- **Consensus:** 3/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** qmlutil.hpp:35,86,99
- **Severity:** Medium
- **Analysis:** Three guards omit Q_OS_QNX despite QNX being a POSIX RTOS with full QProcess support in Qt. main.cpp:23,42,106 correctly include QNX in similar guards. run() becomes Q_UNUSED, restartApplication() only calls quit() without spawning replacement.
- **Impact:** sys:// URL handler, app restart on language/layout change, factory reset all broken on QNX.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | qmlutil excludes QNX from QProcess; exotic (qmlutil.hpp:35) |
| gpt | ✅ LEGIT | 78 | qmlutil.hpp incorrectly excludes QNX from QProcess - run()/restartApplication() silently no-op (src/qmlutil.hpp:35) |
| deepseek | ❌ FALSE | 85 | QNX NOT excluded from QProcess guard at line 35; QProcess included for QNX (qmlutil.hpp:35) |
| glm | ✅ LEGIT | 80 | qmlutil.hpp:35 86 99 incorrectly excludes QNX from QProcess; run()/restartApplication() silently no-op |
| kimi | ✅ LEGIT | 75 | qmlutil.hpp:35,86,99 excludes Q_OS_QNX from QProcess, so run() and restartApplication() become no-ops on QNX, contradicting Qt's POSIX QProcess support. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — qmlutil excludes QNX from QProcess; exotic (qmlutil.hpp:35) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

