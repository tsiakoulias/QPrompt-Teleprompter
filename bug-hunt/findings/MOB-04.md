# [MOB-04] Android: restartApplication() quits without restart

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `qmlutil.hpp:97-103`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** qmlutil.hpp:97-103
- **Severity:** Low
- **Analysis:** On Android/iOS/WASM/WatchOS, QProcess guard skips startDetached, leaving only quit(). Factory reset just closes app without relaunching.
- **Impact:** User must manually reopen app after factory reset.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 65 | restartApplication quits without restart on Android (dup AND-HIGH-03) (qmlutil.hpp:97) |
| gpt | ✅ LEGIT | 78 | Android: restartApplication() quits without restart (src/qmlutil.hpp:97) |
| deepseek | ✅ LEGIT | 95 | qmlutil.hpp:97-103: Android/iOS/WASM skip QProcess::startDetached via preprocessor guard; only QCoreApplication::quit() executes — restart never happens |
| glm | ✅ LEGIT | 75 | qmlutil.hpp:97-103 Android: restartApplication() quits without restart; startDetached excluded by platform guard |
| kimi | ✅ LEGIT | 90 | qmlutil.hpp:97-103 restartApplication on Android/iOS/WASM/WatchOS falls through to QCoreApplication::quit() without restarting. |
| opus-ultra | ✅ LEGIT | 65 | restartApplication quits without restart on Android (dup AND-HIGH-03) (qmlutil.hpp:97) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

