# [SAVE-N05] save() broken on Android content:// URIs — empty filename

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `documenthandler.cpp:1181-1184`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** documenthandler.cpp:1181-1184
- **Severity:** Low
- **Analysis:** `QQmlFile::urlToLocalFileOrQrc()` can't resolve content:// URIs, returns empty string. Propagates through encoding to saveAs("") → open fails with confusing empty-path error.
- **Impact:** Ctrl+S always fails on Android for files from FileDialog.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 50 | save() breaks on Android content:// URIs (empty filename) (documenthandler.cpp:1181) |
| gpt | ✅ LEGIT | 78 | save() broken on Android content:// URIs - empty filename (src/documenthandler.cpp:1181) |
| deepseek | ✅ LEGIT | 70 | Android content:// URIs return empty string from urlToLocalFileOrQrc (documenthandler.cpp:1181) |
| glm | ✅ LEGIT | 80 | documenthandler.cpp:1181-1184 save() broken on Android content:// URIs; empty filename |
| kimi | ✅ LEGIT | 80 | save() takes urlToLocalFileOrQrc(m_fileUrl), empty for Android content:// URIs; empty path propagates to saveAs. |
| opus-ultra | ✅ LEGIT | 50 | save() breaks on Android content:// URIs (empty filename) (documenthandler.cpp:1181) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

