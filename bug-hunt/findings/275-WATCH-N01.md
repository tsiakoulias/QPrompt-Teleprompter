# [275-WATCH-N01] addPath() return never checked — silent watch failure

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.cpp:1026`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp:1026
- **Severity:** Medium
- **Analysis:** QFileSystemWatcher::addPath() returns false on unsupported filesystems, network drives, or exceeded system watch limits. No diagnostic, no fallback.
- **Impact:** Auto-reload silently non-functional for files on network/unsupported filesystems.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ⚠️ PARTIAL | 50 | addPath() return value unchecked (documenthandler.cpp:1026) |
| gpt-5.5-xhigh | ✅ LEGIT | 78 | addPath() return never checked - silent watch failure (src/documenthandler.cpp:1026) |
| deepseek-v4-pro-max | ✅ LEGIT | 95 | documenthandler.cpp:1026: addPath() bool return discarded; silent failure on unsupported filesystems |
| glm-5.2-xhigh | ✅ LEGIT | 70 | documenthandler.cpp:1026 addPath() return never checked; silent watch failure |
| kimi-k2.7-code | ✅ LEGIT | 80 | documenthandler.cpp:1026 calls _fileSystemWatcher->addPath(fileName) without checking bool return. |
| opus-4.8-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — addPath() return value unchecked (documenthandler.cpp:1026) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

