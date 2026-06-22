# [HSCROLL-N02] Inner Flickables missing flickableDirection: VerticalFlick — conflict with parent horizontal ListView

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `InputsOverlay.qml:92,549`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** InputsOverlay.qml:92,549
- **Severity:** Medium
- **Analysis:** Both Flickables are delegates in horizontal ListView for tab switching. Neither sets flickableDirection, defaulting to AutoFlickDirection which may intercept horizontal swipes, blocking tab switching on touch.
- **Impact:** Tab switching stutters/fails on touch when swiping from within Flickable area.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | inner Flickables missing flickableDirection (InputsOverlay.qml:92) |
| gpt | ⚠️ PARTIAL | 58 | observed Inner Flickables missing flickableDirection: VerticalFlick - conflict with parent horizontal Li (src/kirigami_ui/InputsOverlay.qml:92) |
| deepseek | ✅ LEGIT | 90 | InputsOverlay.qml:92 549: inner Flickables lack flickableDirection:VerticalFlick; default AutoFlickDirection intercepts horizontal tab swipes |
| glm | ✅ LEGIT | 70 | InputsOverlay.qml:92 549 inner Flickables missing flickableDirection: VerticalFlick; conflict with parent |
| kimi | ✅ LEGIT | 80 | InputsOverlay.qml:92/549 Flickables inside a horizontal ListView lack flickableDirection: VerticalFlick |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — inner Flickables missing flickableDirection (InputsOverlay.qml:92) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

