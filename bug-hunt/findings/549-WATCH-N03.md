# [549-WATCH-N03] Watcher not refreshed after fileChanged — stale inotify on Linux atomic saves

- **Status:** NEEDS-INFO
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.cpp:857-864,1020-1027`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp:857-864,1020-1027
- **Severity:** Medium
- **Analysis:** Editors using write-to-temp+rename (atomic save) replace file inode. Inotify watch stays on old inode. Qt fires fileChanged once but watcher not re-added. Standard fix: removePath+addPath after each fileChanged.
- **Impact:** Subsequent external edits after first atomic save undetected on Linux.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ❔ UNSURE | 45 | watcher stale after atomic-save inotify swap; Linux-specific (documenthandler.cpp:857) |
| gpt-5.5-xhigh | ✅ LEGIT | 78 | Watcher not refreshed after fileChanged - stale inotify on Linux atomic saves (src/documenthandler.cpp:857) |
| deepseek-v4-pro-max | ✅ LEGIT | 90 | documenthandler.cpp:857-864: reload() loads document but watcher not re-added after fileChanged; next atomic save undetected |
| glm-5.2-xhigh | ✅ LEGIT | 75 | documenthandler.cpp:857-864 1020-1027 watcher not refreshed after fileChanged; stale inotify on Linux atomic saves |
| kimi-k2.7-code | ✅ LEGIT | 70 | documenthandler.cpp reload() / load() calls removePath/addPath on new path but fileChanged handler does not re-add; atomic-save inode change can lose events. |
| opus-4.8-ultra | ❔ UNSURE | 45 | max: unverifiable statically (runtime/semantic) — watcher stale after atomic-save inotify swap; Linux-specific (documenthandler.cpp:857) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

