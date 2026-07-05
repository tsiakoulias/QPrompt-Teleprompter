# [371-REGEX-N03] Unescaped dot in font-size regex — matches any char instead of decimal

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `documenthandler.cpp:894,954,1274`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** documenthandler.cpp:894,954,1274
- **Severity:** Low
- **Analysis:** `(?:.[\\d]+)` uses `.` (any char) instead of `\\.` (literal dot). Works only by coincidence on well-formed HTML.
- **Impact:** Theoretical. No practical impact with well-formed inputs.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ✅ LEGIT | 65 | unescaped dot in font-size regex (dup REGEX-N05) (documenthandler.cpp:894) |
| gpt-5.5-xhigh | ✅ LEGIT | 78 | Unescaped dot in font-size regex - matches any char instead of decimal (src/documenthandler.cpp:894) |
| deepseek-v4-pro-max | ✅ LEGIT | 85 | Unescaped dot in (?:.[\\d]+) at documenthandler.cpp:894 — matches any char instead of literal dot |
| glm-5.2-xhigh | ✅ LEGIT | 75 | documenthandler.cpp:894 954 1274 unescaped dot in font-size regex matches any char instead of decimal point |
| kimi-k2.7-code | ✅ LEGIT | 85 | documenthandler.cpp:894/954/1274 font-size patterns use unescaped '.', matching any character instead of a literal decimal point |
| opus-4.8-ultra | ✅ LEGIT | 65 | unescaped dot in font-size regex (dup REGEX-N05) (documenthandler.cpp:894) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

