# [PATH-N02] reload() constructs file:// URL via raw string concat — #/? in filenames break URL

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.cpp:860`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** documenthandler.cpp:860
- **Severity:** Medium
- **Analysis:** `QUrl("file://" + fileUrl)` — no URL-encoding. `#` parsed as fragment delimiter, `?` as query delimiter. Spaces produce invalid URL. Root cause of R3-DOC-06 m_reloading permanently stuck. Should be `QUrl::fromLocalFile(fileUrl)`.
- **Impact:** File-watcher reload silently fails for files with #, ?, or space in path.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 60 | reload builds file:// URL via string concat; #/? break it (documenthandler.cpp:860) |
| gpt | ✅ LEGIT | 78 | reload() constructs file:// URL via raw string concat - #/? in filenames break URL (src/documenthandler.cpp:860) |
| deepseek | ✅ LEGIT | 95 | documenthandler.cpp:860: QUrl('file://'+fileUrl) — raw string concat without URL-encoding; # parsed as fragment ? as query space breaks URL |
| glm | ✅ LEGIT | 80 | documenthandler.cpp:860 reload() constructs file:// URL via raw string concat; #/? in filenames break URL |
| kimi | ✅ LEGIT | 85 | documenthandler.cpp:860 reload() builds QUrl('file://'+fileUrl) without encoding; #, ?, or spaces break the URL. |
| opus-ultra | ✅ LEGIT | 60 | reload builds file:// URL via string concat; #/? break it (documenthandler.cpp:860) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

