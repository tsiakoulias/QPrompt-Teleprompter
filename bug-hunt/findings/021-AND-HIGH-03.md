# [021-AND-HIGH-03] factoryReset() quits Android app without restarting

- **Status:** OPEN
- **Severity:** High
- **Category:** 
- **Location:** `qmlutil.hpp:97-103`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** qmlutil.hpp:97-103
- **Severity:** High
- **Analysis:** restartApplication() skip QProcess on Android → only quit(). Factory reset silently kills app; user must manually reopen.
- **Impact:** Factory reset exits app with no restart or feedback on Android.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ✅ LEGIT | 65 | restartApplication startDetached is #if !ANDROID -> Android quits, no restart (qmlutil.hpp:97) |
| gpt-5.5-xhigh | ✅ LEGIT | 84 | factoryReset() quits Android app without restarting (src/qmlutil.hpp:97) |
| deepseek-v4-pro-max | ✅ LEGIT | 95 | qmlutil.hpp:97-103: QProcess::startDetached() preprocessor-guarded out on Android; only QCoreApplication::quit() executes — factory reset just kills app with no restart |
| glm-5.2-xhigh | ✅ LEGIT | 80 | qmlutil.hpp:97-103 factoryReset() quits Android app without restarting; startDetached excluded by platform guard |
| kimi-k2.7-code | ✅ LEGIT | 95 | qmlutil.hpp:99-102 restartApplication on Android only calls QCoreApplication::quit; factoryReset exits app. |
| opus-4.8-ultra | ✅ LEGIT | 65 | restartApplication startDetached is #if !ANDROID -> Android quits |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

