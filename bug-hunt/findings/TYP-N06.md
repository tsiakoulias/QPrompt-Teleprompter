# [TYP-N06] 9 getters copy-paste double-textCursor() pattern — null check on stale cursor

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `documenthandler.cpp: alignment(548), bold(565), italic(581), underline(597), strike(613), subscript(629), superscript(648), fontCapitalization(669), regularMarker(694)`
- **Consensus:** 2/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp: alignment(548), bold(565), italic(581), underline(597), strike(613), subscript(629), superscript(648), fontCapitalization(669), regularMarker(694)
- **Severity:** Low
- **Analysis:** LOG-07 flags namedMarker() double-textCursor(). Same pattern in 9 more getters: null-check local QTextCursor, then read from fresh textCursor() call. Null check meaningless — cursor may have changed.
- **Impact:** Rare stale formatting state. Formatting toolbar may show wrong indicator.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | 9 getters share the double-textCursor() pattern (LOG-07 family) |
| gpt | ⚠️ PARTIAL | 58 | observed 9 getters copy-paste double-textCursor() pattern - null check on stale cursor (src/documenthandler.cpp:1) |
| deepseek | ✅ LEGIT | 65 | alignment() null-checks first textCursor() but reads second stale textCursor() (documenthandler.cpp:548-550) |
| glm | ⚠️ PARTIAL | 65 | documenthandler.cpp:548+ 9 getters call textCursor() twice; second call may return stale cursor |
| kimi | ✅ LEGIT | 85 | documenthandler.cpp:545-696 repeats the double-textCursor() pattern in alignment,bold,italic,underline,strike,subscript,superscript,fontCapitalization,regularMarker: null-checking one cursor then reading from a fresh textCursor(). |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — 9 getters share the double-textCursor() pattern (LOG-07 family) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

