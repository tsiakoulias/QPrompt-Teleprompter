# [372-REGEX-N05] regex_0 and regex_3 use . (any-char) instead of \. (literal dot) in decimal matching

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `documenthandler.cpp:893-894,1274-1275`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** documenthandler.cpp:893-894,1274-1275
- **Severity:** Low
- **Analysis:** `(?:.[\d]+)*` intended as `(?:\.[\d]+)*` for decimal points. Unescaped `.` matches any character, potentially over-matching on malformed CSS.
- **Impact:** Minor. Works by coincidence on well-formed inputs.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ✅ LEGIT | 70 | regex_0/regex_3 use unescaped . in decimal match (any char) (documenthandler.cpp:893) |
| gpt-5.5-xhigh | ✅ LEGIT | 78 | regex0 and regex3 use . (any-char) instead of \. (literal dot) in decimal matching (src/documenthandler.cpp:893) |
| deepseek-v4-pro-max | ✅ LEGIT | 85 | documenthandler.cpp:893-894/1274-1275: regex_0 and regex_3 use . (any-char) instead of \. (literal dot) in decimal matching; over-matches on malformed CSS but works by coincidence on well-formed input |
| glm-5.2-xhigh | ✅ LEGIT | 70 | documenthandler.cpp:893-894 1274-1275 regex_0 and regex_3 use . instead of \. for decimal matching |
| kimi-k2.7-code | ✅ LEGIT | 80 | documenthandler.cpp:893-894,1274-1275 regex_0 and regex_3 use unescaped '.' for decimal point, matching any character. |
| opus-4.8-ultra | ✅ LEGIT | 70 | regex_0/regex_3 use unescaped . in decimal match (any char) (documenthandler.cpp:893) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

