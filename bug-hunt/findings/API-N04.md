# [API-N04] setMarker(bool) misleadingly named — sets regular marker, not any marker

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `documenthandler.h:123,212`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.h:123,212
- **Severity:** Low
- **Analysis:** Q_PROPERTY `regularMarker` has WRITE `setMarker`. But `setMarker()` exclusively creates regular markers with `href="#"` — name implies it could set any marker type.
- **Impact:** API confusion — caller expecting to set named marker via `setMarker(true)` gets wrong behavior.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 35 | setMarker(bool) naming; cosmetic (documenthandler.h:123) |
| gpt | ✅ LEGIT | 78 | setMarker(bool) misleadingly named - sets regular marker, not any marker (src/documenthandler.h:123) |
| deepseek | ✅ LEGIT | 65 | setMarker(bool) only toggles regular marker despite generic name (documenthandler.h:123 212) |
| glm | ✅ LEGIT | 70 | documenthandler.h:123 212 setMarker(bool) misleadingly named; sets regular marker not any marker |
| kimi | ⚠️ PARTIAL | 50 | documenthandler.h:123 WRITE setMarker only creates regular markers with href='#', an API naming limitation more than a runtime defect. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — setMarker(bool) naming; cosmetic (documenthandler.h:123) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

