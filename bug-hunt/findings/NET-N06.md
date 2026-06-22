# [NET-N06] loadFromNetwork() validates original URL, not constructed resultingUrl

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `documenthandler.cpp:881`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp:881
- **Severity:** Low
- **Analysis:** `if (url.isValid())` checks input URL, not the constructed `resultingUrl`. If construction produces malformed URL (beyond already-documented R4-EXP-03 host/path swap), guard passes, bad request issued.
- **Impact:** Masked URL construction errors reach network layer.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 65 | if(url.isValid()) validates original url not resultingUrl (documenthandler.cpp:881) |
| gpt | ⚠️ PARTIAL | 58 | observed loadFromNetwork() validates original URL, not constructed resultingUrl (src/documenthandler.cpp:881) |
| deepseek | ✅ LEGIT | 85 | url.isValid() at documenthandler.cpp:881 checks input URL not constructed resultingUrl — masked construction errors |
| glm | ✅ LEGIT | 80 | documenthandler.cpp:881 loadFromNetwork validates original url not constructed resultingUrl |
| kimi | ✅ LEGIT | 95 | documenthandler.cpp:881 tests url.isValid() (the original argument) instead of resultingUrl.isValid() after URL construction |
| opus-ultra | ✅ LEGIT | 65 | if(url.isValid()) validates original url not resultingUrl (documenthandler.cpp:881) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

