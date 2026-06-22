# [WATCH-N04] unblockFileWatcher() dereferences _fileSystemWatcher without null guard

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `documenthandler.cpp:1125-1128`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp:1125-1128
- **Severity:** Low
- **Analysis:** No null check. Reachable via QTimer::singleShot from saveAs().

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | _fileSystemWatcher always constructed in ctor; null-deref unlikely (documenthandler.cpp:1125) |
| gpt | ✅ LEGIT | 78 | unblockFileWatcher() dereferences _fileSystemWatcher without null guard (src/documenthandler.cpp:1125) |
| deepseek | ✅ LEGIT | 85 | documenthandler.cpp:1125-1128: _fileSystemWatcher dereferenced without null guard; reachable via QTimer::singleShot from saveAs() |
| glm | ✅ LEGIT | 70 | documenthandler.cpp:1125-1128 unblockFileWatcher() dereferences _fileSystemWatcher without null guard |
| kimi | ✅ LEGIT | 85 | documenthandler.cpp:1125-1127 unblockFileWatcher derefs _fileSystemWatcher without null check. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — _fileSystemWatcher always constructed in ctor; null-deref unlikely (documenthandler.cpp:11 |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

