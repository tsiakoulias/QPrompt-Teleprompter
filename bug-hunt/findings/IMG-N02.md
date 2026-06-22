# [IMG-N02] insertHtmlAt() silent blocking HTTP load for img src URLs — UI freeze

- **Status:** OPEN
- **Severity:** High
- **Category:** 
- **Location:** `documenthandler.cpp:1451`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** documenthandler.cpp:1451
- **Severity:** High
- **Analysis:** QImage::load() with HTTP URL performs synchronous download on main thread. UI frozen until complete/timed-out. insertImageAt() correctly uses async QNetworkAccessManager for HTTP.
- **Impact:** Multi-second UI freezes when pasting HTML with remote images.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 60 | insertHtmlAt synchronous image.load(src) for http -> UI freeze (documenthandler.cpp:1451) |
| gpt | ✅ LEGIT | 84 | insertHtmlAt() silent blocking HTTP load for img src URLs - UI freeze (src/documenthandler.cpp:1451) |
| deepseek | ✅ LEGIT | 90 | documenthandler.cpp:1451: image.load(src) on HTTP URL performs synchronous network load on main thread; multi-second UI freeze |
| glm | ✅ LEGIT | 80 | documenthandler.cpp:1451 insertHtmlAt silent blocking HTTP load for img src URLs; UI freeze |
| kimi | ✅ LEGIT | 95 | documenthandler.cpp:1451 calls image.load(src) for http/https URLs synchronously on the main thread |
| opus-ultra | ✅ LEGIT | 60 | insertHtmlAt synchronous image.load(src) for http -> UI freeze (documenthandler.cpp:1451) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

