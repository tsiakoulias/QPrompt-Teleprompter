# [276-WATCH-N02] removePath() return never checked — stale path causes double-watch

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.cpp:1024`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp:1024
- **Severity:** Medium
- **Analysis:** If removePath fails, old path stays watched alongside new path. fileChanged on old file invokes reload() with wrong URL — m_reloading stuck at true (R3-DOC-06).
- **Impact:** Double-watch causing stale content reload on old file change.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ⚠️ PARTIAL | 50 | removePath() return value unchecked (documenthandler.cpp:1024) |
| gpt-5.5-xhigh | ✅ LEGIT | 78 | removePath() return never checked - stale path causes double-watch (src/documenthandler.cpp:1024) |
| deepseek-v4-pro-max | ✅ LEGIT | 90 | documenthandler.cpp:1024: removePath() return unchecked; stale path stays watched causing double-watch on fileChanged |
| glm-5.2-xhigh | ✅ LEGIT | 70 | documenthandler.cpp:1024 removePath() return never checked; stale path causes double-watch |
| kimi-k2.7-code | ✅ LEGIT | 80 | documenthandler.cpp:1024 calls removePath(...) with no return check; stale watch possible. |
| opus-4.8-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — removePath() return value unchecked (documenthandler.cpp:1024) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

