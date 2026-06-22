# [URL-N03] Network-loaded HTML lacks base URL — relative resources broken

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.cpp:888-901`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp:888-901
- **Severity:** Medium
- **Analysis:** loadFromNetworkFinihed never calls doc->setBaseUrl(). Original network URL discarded. Relative URLs in HTML (`<img src="images/photo.jpg">`) can't resolve. May resolve against stale base URL from prior local file.
- **Impact:** Images, stylesheets in network-loaded HTML fail to load.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 55 | network HTML lacks base URL; relative resources break (documenthandler.cpp:888) |
| gpt | ⚠️ PARTIAL | 58 | observed Network-loaded HTML lacks base URL - relative resources broken (src/documenthandler.cpp:888) |
| deepseek | ✅ LEGIT | 90 | documenthandler.cpp:888-901: loadFromNetworkFinihed never calls doc->setBaseUrl(); original network URL discarded — relative resources (images/stylesheets) in HTML cannot resolve |
| glm | ✅ LEGIT | 80 | documenthandler.cpp:888-901 network-loaded HTML lacks base URL; relative resources broken |
| kimi | ✅ LEGIT | 80 | documenthandler.cpp:888-901 loadFromNetworkFinihed never calls doc->setBaseUrl(), so relative resources in network HTML fail. |
| opus-ultra | ✅ LEGIT | 55 | network HTML lacks base URL; relative resources break (documenthandler.cpp:888) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

