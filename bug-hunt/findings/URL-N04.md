# [URL-N04] loadFromNetwork() validates wrong URL instance

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `documenthandler.cpp:881`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp:881
- **Severity:** Low
- **Analysis:** `if (url.isValid())` checks original URL, not constructed resultingUrl. Valid relative URL can produce invalid resultingUrl that passes unchecked.
- **Impact:** Invalid network requests silently initiated.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 60 | validates wrong URL instance (dup NET-N06) (documenthandler.cpp:881) |
| gpt | ⚠️ PARTIAL | 58 | observed loadFromNetwork() validates wrong URL instance (src/documenthandler.cpp:881) |
| deepseek | ✅ LEGIT | 90 | documenthandler.cpp:881: url.isValid() validates original url not constructed resultingUrl; valid relative URL can produce invalid resultingUrl that passes unchecked |
| glm | ✅ LEGIT | 75 | documenthandler.cpp:881 loadFromNetwork validates original url not constructed resultingUrl |
| kimi | ✅ LEGIT | 85 | documenthandler.cpp:881 validates original 'url' parameter, not the constructed 'resultingUrl', allowing invalid requests. |
| opus-ultra | ✅ LEGIT | 60 | validates wrong URL instance (dup NET-N06) (documenthandler.cpp:881) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

