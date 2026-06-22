# [PROP-N01] on__FullScreenChanged handler casing mismatch — never fires

- **Status:** OPEN
- **Severity:** High
- **Category:** 
- **Location:** `main.qml:36-37`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** main.qml:36-37
- **Severity:** High
- **Analysis:** Property declared `__fullScreen` (lowercase `f`). Handler written `on__FullScreenChanged` (uppercase `F`). Auto-generated handler name doesn't match. Same bug class as FINAL-09 (`on__IChanged`). `AppController.wasm.toggleBrowserFullscreen()` never called.
- **Impact:** WASM native browser Fullscreen API never invoked; fullscreen only within browser tab frame.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 70 | property is __fullScreen; on__FullScreenChanged caps F -> never fires (main.qml:36) |
| gpt | ✅ LEGIT | 84 | onFullScreenChanged handler casing mismatch - never fires (src/kirigami_ui/main.qml:36) |
| deepseek | ✅ LEGIT | 95 | __fullScreen (lower f) at main.qml:36 vs on__FullScreenChanged (upper F) at :37 — handler never fires |
| glm | ✅ LEGIT | 85 | main.qml:36-37 on__FullScreenChanged handler casing mismatch; property is __fullScreen not __FullScreen |
| kimi | ✅ LEGIT | 90 | main.qml:36 declares __fullScreen (lowercase f) but uses on__FullScreenChanged (uppercase F); handler mismatch means WASM fullscreen API never fires |
| opus-ultra | ✅ LEGIT | 70 | property is __fullScreen; on__FullScreenChanged caps F -> never fires (main.qml:36) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

