# [060-REGEX-CRIT-02] searchRegEx.setPattern() from user input — isValid() never called

- **Status:** OPEN
- **Severity:** High
- **Category:** 
- **Location:** `documenthandler.cpp:1543-1544`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** documenthandler.cpp:1543-1544
- **Severity:** High
- **Analysis:** User input from QML search box passed directly to setPattern(). No isValid() check. Invalid pattern (unbalanced parentheses, malformed quantifiers) → undefined behavior in QTextDocument::find().
- **Impact:** Search/replace crashes or silently misfires on invalid user regex.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ✅ LEGIT | 55 | user search regex isValid() never checked; Qt handles invalid gracefully (documenthandler.cpp:1543) |
| gpt-5.5-xhigh | ✅ LEGIT | 84 | searchRegEx.setPattern() from user input - isValid() never called (src/documenthandler.cpp:1543) |
| deepseek-v4-pro-max | ✅ LEGIT | 95 | documenthandler.cpp:1543-1544: searchRegEx.setPattern(subString) from user QML input; no isValid() check — invalid regex causes undefined behavior in QTextDocument::find() |
| glm-5.2-xhigh | ✅ LEGIT | 85 | documenthandler.cpp:1543-1544 searchRegEx.setPattern() from user input; isValid() never called |
| kimi-k2.7-code | ✅ LEGIT | 90 | documenthandler.cpp:1543-1544 sets user-supplied pattern on searchRegEx without isValid(); invalid regex reaches QTextDocument::find. |
| opus-4.8-ultra | ✅ LEGIT | 55 | user search regex isValid() never checked; Qt handles invalid gracefully (documenthandler.cpp:1543) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

