# [QP-N01] restartApplication() quits even when startDetached fails — app dies with no replacement

- **Status:** OPEN
- **Severity:** High
- **Category:** 
- **Location:** `qmlutil.hpp:97-102`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** qmlutil.hpp:97-102
- **Severity:** High
- **Analysis:** startDetached() returns bool — discarded. quit() fires unconditionally. If binary inaccessible (macOS bundle moved, AppImage mount expired), app terminates permanently.
- **Impact:** Factory reset or language change kills app with no restart.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 65 | restartApplication quits even if startDetached fails (return ignored) (qmlutil.hpp:97) |
| gpt | ⚠️ PARTIAL | 58 | observed restartApplication() quits even when startDetached fails - app dies with no replacement (src/qmlutil.hpp:97) |
| deepseek | ✅ LEGIT | 95 | qmlutil.hpp:97-102: QProcess::startDetached return bool discarded; quit() fires unconditionally; app dies if restart fails |
| glm | ✅ LEGIT | 80 | qmlutil.hpp:97-102 restartApplication() quits even when startDetached fails; app dies with no replacement |
| kimi | ✅ LEGIT | 95 | qmlutil.hpp:100-102 discards startDetached() return and calls quit() unconditionally |
| opus-ultra | ✅ LEGIT | 65 | restartApplication quits even if startDetached fails (return ignored) (qmlutil.hpp:97) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

