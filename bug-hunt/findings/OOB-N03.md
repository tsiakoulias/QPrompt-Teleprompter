# [OOB-N03] alignment() fetches textCursor() twice — stale cursor race

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `documenthandler.cpp:547-550`
- **Consensus:** 2/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** documenthandler.cpp:547-550
- **Severity:** Low
- **Analysis:** Double textCursor() fetch — first null-checked, second reads alignment from potentially different position if cursorPosition changed between calls.
- **Impact:** Formatting toolbar shows wrong alignment in rare race conditions.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | alignment() double textCursor() fetch; harmless (LOG-07 family) (documenthandler.cpp:547) |
| gpt | ✅ LEGIT | 78 | alignment() fetches textCursor() twice - stale cursor race (src/documenthandler.cpp:547) |
| deepseek | ✅ LEGIT | 85 | textCursor() called twice at documenthandler.cpp:547+550 — second fetch may return different cursor |
| glm | ⚠️ PARTIAL | 60 | documenthandler.cpp:547-550 alignment() fetches textCursor() twice; second call may return stale cursor |
| kimi | ❌ FALSE | 80 | documenthandler.cpp:547-550 fetches textCursor() twice; it is redundant but both calls happen synchronously with no real race. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — alignment() double textCursor() fetch; harmless (LOG-07 family) (documenthandler.cpp:547) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

