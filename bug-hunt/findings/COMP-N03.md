# [COMP-N03] regularMarker() same double-textCursor anti-pattern as LOG-07

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `documenthandler.cpp:693-696`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp:693-696
- **Severity:** Low
- **Analysis:** Null-check on local QTextCursor (fetch 1), reads anchor properties from 3 independent textCursor() calls (fetches 2-4). LOG-07 documents namedMarker() only — regularMarker() has identical bug.
- **Impact:** Rare stale formatting state on marker toolbar button.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | regularMarker double textCursor() (LOG-07 family) (documenthandler.cpp:693) |
| gpt | ✅ LEGIT | 78 | regularMarker() same double-textCursor anti-pattern as LOG-07 (src/documenthandler.cpp:693) |
| deepseek | ✅ LEGIT | 95 | documenthandler.cpp:693-696: fetches textCursor() 3 extra times after null-checked local copy; same anti-pattern as namedMarker() at 701-704 — stale formatting reads |
| glm | ⚠️ PARTIAL | 60 | documenthandler.cpp:693-696 regularMarker() same double-textCursor anti-pattern; second cursor may be stale |
| kimi | ✅ LEGIT | 70 | documenthandler.cpp:693-696 regularMarker() null-checks one cursor then reads format from fresh textCursor() calls; stale cursor pattern. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — regularMarker double textCursor() (LOG-07 family) (documenthandler.cpp:693) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

