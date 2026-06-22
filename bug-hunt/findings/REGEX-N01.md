# [REGEX-N01] All 13 QRegularExpression objects lack isValid() checks

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.cpp, spellhighlighter.cpp (13 regex objects)`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp, spellhighlighter.cpp (13 regex objects)
- **Severity:** Medium
- **Analysis:** Every regex constructed without validating. Pattern typo → silent no-match instead of error. searchRegEx (line 1543) receives user input — invalid user regex like `[` silently matches nothing.
- **Impact:** Regex bugs silently break filtering/search/highlighting.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | 13 regexes lack isValid(); all but search are author-literal (always valid) |
| gpt | ✅ LEGIT | 78 | All 13 QRegularExpression objects lack isValid() checks (src/documenthandler.cpp:893) |
| deepseek | ✅ LEGIT | 85 | 13 QRegularExpression objects lack isValid() checks — pattern typo silently matches nothing |
| glm | ✅ LEGIT | 75 | 13 QRegularExpression objects across documenthandler.cpp and spellhighlighter.cpp lack isValid() checks |
| kimi | ✅ LEGIT | 95 | documenthandler.cpp has 12 QRegularExpression objects (regex_0..regex_8, imgSrcRegex, searchRegEx) and spellhighlighter.cpp has 1 (wordRe); none call isValid() |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — 13 regexes lack isValid(); all but search are author-literal (always valid) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

