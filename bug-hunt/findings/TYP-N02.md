# [TYP-N02] Misspelled parameter: withoutFormating (missing 't')

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `documenthandler.h:225, documenthandler.cpp:1336,1347`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** documenthandler.h:225, documenthandler.cpp:1336,1347
- **Severity:** Low
- **Analysis:** "Formating" instead of "Formatting." Consistent across declaration, definition, usage.
- **Impact:** Developer confusion; code-search failures.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 90 | withoutFormating misspelled param (documenthandler.cpp:1336) |
| gpt | ✅ LEGIT | 92 | Misspelled parameter: withoutFormating (missing 't') (src/documenthandler.h:225) |
| deepseek | ✅ LEGIT | 90 | misspelled parameter withoutFormating missing 't' in Formatting (documenthandler.h:225) |
| glm | ✅ LEGIT | 75 | documenthandler.h:225 1336 1347 misspelled parameter withoutFormating (missing 't') |
| kimi | ✅ LEGIT | 98 | documenthandler.h:225 and documenthandler.cpp:1336,1347 spell the parameter withoutFormating (missing t). |
| opus-ultra | ✅ LEGIT | 90 | withoutFormating misspelled param (documenthandler.cpp:1336) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

