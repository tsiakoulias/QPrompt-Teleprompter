# [INT-N03] 6 qsizetype→int narrowing conversions across models and loops

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `markersmodel.cpp:101,121, promptsession.cpp:88, main.cpp:274, spellchecker.cpp:98,328`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** markersmodel.cpp:101,121, promptsession.cpp:88, main.cpp:274, spellchecker.cpp:98,328
- **Severity:** Low
- **Analysis:** size()/length()/indexOf() return qsizetype (64-bit), narrowed to int (32-bit). Sentinels like -1 fit but values > INT_MAX corrupt.
- **Impact:** Code quality — practical document sizes stay within int range.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 40 | qsizetype->int narrowing 6 sites (markersmodel.cpp:101) |
| gpt | ⚠️ PARTIAL | 58 | observed 6 qsize_type->int narrowing conversions across models and loops (src/markersmodel.cpp:101) |
| deepseek | ✅ LEGIT | 80 | markersmodel.cpp:101/121 promptsession.cpp:88 main.cpp:274 spellchecker.cpp:98/328: qsizetype size()/length()/indexOf() narrowed to int (32-bit); practical docs within range |
| glm | ✅ LEGIT | 70 | markersmodel.cpp:101 121 promptsession.cpp:88 main.cpp:274 spellchecker.cpp:98 328 6 qsizetype→int narrowing conversions |
| kimi | ✅ LEGIT | 70 | markersmodel.cpp:101,121; promptsession.cpp:88; main.cpp:274; spellchecker.cpp:98,328 narrow qsizetype returns to int. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — qsizetype->int narrowing 6 sites (markersmodel.cpp:101) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

