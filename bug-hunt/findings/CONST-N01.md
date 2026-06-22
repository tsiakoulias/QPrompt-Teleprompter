# [CONST-N01] getMarkerKey() not const — pure reader without side effects

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `documenthandler.h:214, documenthandler.cpp:746`
- **Consensus:** 2/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** documenthandler.h:214, documenthandler.cpp:746
- **Severity:** Low
- **Analysis:** Reads cursor anchor names, converts to display string. Zero member mutation. Should be const.
- **Impact:** Cannot be called on const DocumentHandler&.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 40 | getMarkerKey not const; style only (documenthandler.cpp:746) |
| gpt | ⚠️ PARTIAL | 58 | observed getMarkerKey() not const - pure reader without side effects (src/documenthandler.h:214) |
| deepseek | ✅ LEGIT | 60 | getMarkerKey pure reader method missing const qualifier (documenthandler.cpp:746) |
| glm | ✅ LEGIT | 70 | documenthandler.h:214 746 getMarkerKey() not const; pure reader without side effects |
| kimi | ❌ FALSE | 75 | getMarkerKey() is a non-const reader, but its const-correctness is a style issue with no observable misbehavior. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — getMarkerKey not const; style only (documenthandler.cpp:746) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

