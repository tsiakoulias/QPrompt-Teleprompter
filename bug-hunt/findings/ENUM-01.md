# [ENUM-01] documenthandler.cpp:1108 updateContents switch no default — silent data loss

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.cpp:1108`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp:1108
- **Severity:** Medium
- **Analysis:** updateContents unconditionally clears document via `cursor.removeSelectedText()` before switch on format. No default case. If format is Qt::UnknownText (-1) or future value, document destroyed with zero content inserted.
- **Impact:** Silent data loss if unexpected format value reaches the function.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | updateContents switch has no default but covers all TextFormat values (documenthandler.cpp:1108) |
| gpt | ✅ LEGIT | 78 | documenthandler.cpp:1108 updateContents switch no default - silent data loss (src/documenthandler.cpp:1108) |
| deepseek | ✅ LEGIT | 90 | No default case in switch(format) at documenthandler.cpp:1108 — doc cleared with zero content inserted |
| glm | ✅ LEGIT | 80 | documenthandler.cpp:1108 updateContents switch has no default case; silent data loss for unknown format |
| kimi | ✅ LEGIT | 85 | documenthandler.cpp:1108 updateContents switch has no default; an unknown format value clears the document without inserting content. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — updateContents switch has no default but covers all TextFormat values (documenthandler.cpp |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

