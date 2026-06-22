# [SAVE-N04] save() unnecessary QString→std::string→QString round-trip through locale encoding

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `documenthandler.cpp:1183`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp:1183
- **Severity:** Low
- **Analysis:** `QString::fromStdString(QUrl::toPercentEncoding(...).toStdString())` — useless conversion. Qt 5: locale-dependent encoding corrupts non-ASCII paths.
- **Impact:** Non-ASCII file paths corrupted during save under Qt 5.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | save() needless QString->std::string->QString round-trip (documenthandler.cpp:1183) |
| gpt | ✅ LEGIT | 78 | save() unnecessary QString->std::string->QString round-trip through locale encoding (src/documenthandler.cpp:1183) |
| deepseek | ✅ LEGIT | 65 | unnecessary QString->std::string->QString round-trip via locale encoding (documenthandler.cpp:1183) |
| glm | ✅ LEGIT | 75 | documenthandler.cpp:1183 unnecessary QString→std::string→QString round-trip through locale encoding |
| kimi | ✅ LEGIT | 70 | save() at documenthandler.cpp:1183 round-trips the percent-encoded path through toStdString/fromStdString; redundant and encoding-risky. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — save() needless QString->std::string->QString round-trip (documenthandler.cpp:1183) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

