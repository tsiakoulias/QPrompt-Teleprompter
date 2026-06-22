# [DLG-N06] import() error strings passed as document content via updateContents()

- **Status:** OPEN
- **Severity:** High
- **Category:** 
- **Location:** `documenthandler.cpp:1000,1087`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** documenthandler.cpp:1000,1087
- **Severity:** High
- **Analysis:** ALL import formats depending on external tools (ODT, DOCX, DOC, RTF, ABW, PAGESX, PAGES) — if LibreOffice unavailable/crashes/times out, the error description becomes document content. No notification distinguishes error-text-as-content from successful import.
- **Impact:** User's document silently replaced with error message text.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 65 | import() error string replaces document via updateContents (documenthandler.cpp:1000) |
| gpt | ✅ LEGIT | 84 | import() error strings passed as document content via updateContents() (src/documenthandler.cpp:1000) |
| deepseek | ✅ LEGIT | 90 | import() error strings passed to updateContents at documenthandler.cpp:1000 — doc replaced with error text |
| glm | ✅ LEGIT | 80 | documenthandler.cpp:1000 1087 import() error strings passed as document content via updateContents() |
| kimi | ✅ LEGIT | 90 | documenthandler.cpp:1000/1087 passes import() error strings through updateContents(html, Qt::RichText), replacing document content. |
| opus-ultra | ✅ LEGIT | 65 | import() error string replaces document via updateContents (documenthandler.cpp:1000) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

