# [SAVE-N01] loadFromNetworkFinihed sets m_fileUrl to phantom QTemporaryFile path

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.cpp:897,144`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp:897,144
- **Severity:** Medium
- **Analysis:** m_cache is new QTemporaryFile(this) never opened. `m_cache->fileName()` returns auto-generated temp name with no file on disk. m_fileUrl set to this phantom path. Title bar shows garbage; save() constructs broken URL.
- **Impact:** Corrupted file URL after every network load. Save-in-place broken.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 55 | network doc m_fileUrl set to QTemporaryFile path (documenthandler.cpp:897) |
| gpt | ✅ LEGIT | 78 | loadFromNetworkFinihed sets m_fileUrl to phantom QTemporaryFile path (src/documenthandler.cpp:897) |
| deepseek | ✅ LEGIT | 70 | network docs set m_fileUrl to QTemporaryFile path not source network URL (documenthandler.cpp:897) |
| glm | ✅ LEGIT | 80 | documenthandler.cpp:897 144 loadFromNetworkFinihed sets m_fileUrl to m_cache->fileName() (QTemporaryFile path) |
| kimi | ✅ LEGIT | 80 | loadFromNetworkFinihed assigns m_cache->fileName() to m_fileUrl at documenthandler.cpp:897, so fileUrl points to a temporary cache. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — network doc m_fileUrl set to QTemporaryFile path (documenthandler.cpp:897) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

