# [COMP-N02] Case-sensitive suffix check misses mixed-case extensions — silent format loss

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.cpp:1154`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** documenthandler.cpp:1154
- **Severity:** Medium
- **Analysis:** saveAs() only checks lowercase and UPPERCASE extensions ("html", "html", "HTML", "HTM" etc). Extensions like "Html", "Htm" on case-preserving filesystems (Windows/macOS) slip through — file saved as plain text, silently destroying all formatting.
- **Impact:** Silent formatting loss when saving files with mixed-case extensions.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 50 | suffix check misses mixed-case ext like .Html (documenthandler.cpp:1154) |
| gpt | ✅ LEGIT | 78 | Case-sensitive suffix check misses mixed-case extensions - silent format loss (src/documenthandler.cpp:1154) |
| deepseek | ✅ LEGIT | 90 | documenthandler.cpp:1154-1156: only checks lowercase and UPPERCASE html/htm/xhtml; mixed-case like Html/Htm slip through — saved as plain text losing formatting |
| glm | ✅ LEGIT | 80 | documenthandler.cpp:1154 case-sensitive suffix check; .HTML and .htm not matched consistently |
| kimi | ✅ LEGIT | 85 | documenthandler.cpp:1154 suffix check only covers lower/upper html/htm; mixed-case 'Html' slips through and saves as plain text. |
| opus-ultra | ✅ LEGIT | 50 | suffix check misses mixed-case ext like .Html (documenthandler.cpp:1154) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

