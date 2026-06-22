# [CUR-N02] search() regex path ignores loop parameter — unconditional wrap

- **Status:** OPEN
- **Severity:** High
- **Category:** Logic
- **Location:** `src/documenthandler.cpp:1552-1557`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/documenthandler.cpp:1552-1557
- **Severity:** High
- **Category:** Logic
- **Analysis:** Regex branch wraps unconditionally; non-regex branch correctly checks loop parameter. replaceAll passes loop=false but regex ignores it.
- **Impact:** Incorrect search results; compounds with CUR-N01 for guaranteed infinite loop on regex replaceAll.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 95 | = LOG-05; regex search path ignores loop -> always wraps (documenthandler.cpp:1552) |
| gpt | ✅ LEGIT | 84 | search() regex path ignores loop parameter - unconditional wrap (src/documenthandler.cpp:1552) |
| deepseek | ✅ LEGIT | 98 | documenthandler.cpp:1552 regex branch wraps unconditionally; non-regex branch(line 1567) correctly checks loop param — regex ignores loop=false |
| glm | ✅ LEGIT | 85 | documenthandler.cpp:1552-1557 regex search path wraps unconditionally ignoring loop parameter |
| kimi | ✅ LEGIT | 95 | documenthandler.cpp:1552-1557 regex search wrap-around branch never checks `loop` parameter, unlike non-regex branch at line 1567. |
| opus-ultra | ✅ LEGIT | 95 | = LOG-05; regex search path ignores loop -> always wraps (documenthandler.cpp:1552) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

