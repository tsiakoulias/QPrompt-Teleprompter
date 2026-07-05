# [255-REGEX-N04] ReDoS — user-supplied regex has no length limit, timeout, or backtracking guard

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.cpp:1543-1557`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp:1543-1557
- **Severity:** Medium
- **Analysis:** subString from QML user input. No QRegularExpression::optimize(), MatchTimeout, or pattern-length cap. Evil regex like `(a+)+b` causes exponential backtracking in replaceAll() loop. Combined with LOG-05/LOG-06 infinite loop risk.
- **Impact:** Application hang with 100% CPU during Search/Replace All with malicious regex.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ⚠️ PARTIAL | 50 | ReDoS: user regex no length/timeout guard; user's own input (documenthandler.cpp:1543) |
| gpt-5.5-xhigh | ✅ LEGIT | 78 | ReDoS - user-supplied regex has no length limit, timeout, or backtracking guard (src/documenthandler.cpp:1543) |
| deepseek-v4-pro-max | ✅ LEGIT | 90 | documenthandler.cpp:1543-1557: user-supplied regex has no length limit no MatchTimeout no optimize(); evil regex like (a+)+b causes exponential backtracking — 100% CPU hang |
| glm-5.2-xhigh | ✅ LEGIT | 80 | documenthandler.cpp:1543-1557 user-supplied regex has no length limit timeout or backtracking guard; ReDoS risk |
| kimi-k2.7-code | ✅ LEGIT | 85 | documenthandler.cpp:1543-1557 accepts arbitrary user regex with no length limit, timeout or optimize(); malicious input can ReDoS. |
| opus-4.8-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — ReDoS: user regex no length/timeout guard; user's own input (documenthandler.cpp:1543) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

