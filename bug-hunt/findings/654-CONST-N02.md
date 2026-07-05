# [654-CONST-N02] getMarkerHref() not const — identical pattern

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `documenthandler.h:216, documenthandler.cpp:779`
- **Consensus:** 2/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** documenthandler.h:216, documenthandler.cpp:779
- **Severity:** Low
- **Analysis:** Same as CONST-N01 — pure reader.
- **Impact:** Same.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ⚠️ PARTIAL | 40 | getMarkerHref not const; style only (documenthandler.cpp:779) |
| gpt-5.5-xhigh | ⚠️ PARTIAL | 58 | observed getMarkerHref() not const - identical pattern (src/documenthandler.h:216) |
| deepseek-v4-pro-max | ✅ LEGIT | 60 | getMarkerHref pure reader method missing const qualifier (documenthandler.cpp:779) |
| glm-5.2-xhigh | ✅ LEGIT | 70 | documenthandler.h:216 779 getMarkerHref() not const; identical pattern |
| kimi-k2.7-code | ❌ FALSE | 75 | getMarkerHref() is a non-const reader; absence of const does not cause a runtime bug. |
| opus-4.8-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — getMarkerHref not const; style only (documenthandler.cpp:779) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

