# [TXT-FMT-N01] setMarkerHref("") fails to clear QTextFormat::AnchorHref — stale href persists

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.cpp:769-774`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp:769-774
- **Severity:** Medium
- **Analysis:** When href is empty, format.setAnchor(false) only; clearProperty(AnchorHref) skipped. After clearing, getMarkerHref() still returns old href. setMarker(false) correctly clears both.
- **Impact:** Orphaned href data attached to deactivated anchors.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 65 | setMarkerHref('') doesn't clear AnchorHref via mergeCharFormat (FINAL-21 family) (documenthandler.cpp:769) |
| gpt | ⚠️ PARTIAL | 58 | observed setMarkerHref("") fails to clear QTextFormat::AnchorHref - stale href persists (src/documenthandler.cpp:769) |
| deepseek | ✅ LEGIT | 80 | setMarkerHref('') sets setAnchor(false) but skips clearProperty(AnchorHref) at documenthandler.cpp:769-774; stale href persists |
| glm | ✅ LEGIT | 70 | documenthandler.cpp:769-774 setMarkerHref('') fails to clear QTextFormat::AnchorHref; stale href persists |
| kimi | ✅ LEGIT | 90 | documenthandler.cpp:765-774 setMarkerHref('') never calls clearProperty(QTextFormat::AnchorHref); stale href remains |
| opus-ultra | ✅ LEGIT | 65 | setMarkerHref('') doesn't clear AnchorHref via mergeCharFormat (FINAL-21 family) (documenthandler.cpp:769) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

