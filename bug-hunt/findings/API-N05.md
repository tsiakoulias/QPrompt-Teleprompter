# [API-N05] fileName()/fileType() return fabricated defaults — can't distinguish "no file" from "untitled.html"

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `documenthandler.cpp:838-850`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp:838-850
- **Severity:** Low
- **Analysis:** When m_fileUrl empty, fileName() returns "untitled.html" and fileType() returns "html". No way to distinguish from an actual file named "untitled.html". fileUrlChanged fires when fileName() changes even though fileUrl may not.
- **Impact:** QML can't distinguish "no file loaded" from a real file. Misleading signals.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | fileName/fileType return 'untitled.html' default; can't signal no-file (documenthandler.cpp:838) |
| gpt | ✅ LEGIT | 78 | fileName()/fileType() return fabricated defaults - can't distinguish "no file" from "untitled.html" (src/documenthandler.cpp:838) |
| deepseek | ✅ LEGIT | 70 | fileName returns 'untitled.html' default; no way to distinguish no-file state (documenthandler.cpp:838-843) |
| glm | ✅ LEGIT | 70 | documenthandler.cpp:838-850 fileName()/fileType() return fabricated defaults; can't distinguish no-file from untitled.html |
| kimi | ✅ LEGIT | 70 | documenthandler.cpp:838-850 fileName()/fileType() return 'untitled.html'/'html' defaults, indistinguishable from a real untitled.html file. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — fileName/fileType return 'untitled.html' default; can't signal no-file (documenthandler.cp |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

