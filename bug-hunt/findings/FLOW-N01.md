# [FLOW-N01] setKeyMarker() calls setAnchor("#") — const char*→bool conversion, href never set

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.cpp:716`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** documenthandler.cpp:716
- **Severity:** Medium
- **Analysis:** `format.setAnchor("#")` — `setAnchor(bool)` is only overload. `"#"` decays to const char* → pointer-to-bool → true. setAnchorHref never called. Regular markers (setMarker:798) correctly use `setAnchorHref("#")`. Parse sees key markers with url="" vs regular markers with url="#".
- **Impact:** Inconsistent marker url role; QML consuming url sees wrong classification.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 65 | setAnchor(\#\") -> const char* to bool=true; href never set (documenthandler.cpp:716)" |
| gpt | ✅ LEGIT | 78 | setKeyMarker() calls setAnchor("#") - const char->bool conversion, href never set (src/documenthandler.cpp:716) |
| deepseek | ✅ LEGIT | 90 | documenthandler.cpp:716: format.setAnchor('#') — '#' decays const char*->bool=true; setAnchorHref() never called unlike regular setMarker() at 798 which uses setAnchorHref('#') |
| glm | ✅ LEGIT | 80 | documenthandler.cpp:716 setKeyMarker calls format.setAnchor('#') which takes const char* not bool; href never set properly |
| kimi | ✅ LEGIT | 90 | documenthandler.cpp:716 format.setAnchor('#') converts const char* to bool; setAnchorHref('#') is never called. |
| opus-ultra | ✅ LEGIT | 65 | setAnchor(\#\") -> const char* to bool=true; href never set (documenthandler.cpp:716)" |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

