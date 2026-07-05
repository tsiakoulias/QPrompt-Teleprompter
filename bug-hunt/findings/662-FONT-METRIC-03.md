# [662-FONT-METRIC-03] fontFamily() returns resolved-family not requested-family — substitution invisible

- **Status:** REJECTED
- **Severity:** Low
- **Category:** 
- **Location:** `documenthandler.cpp:493-501`
- **Consensus:** 2/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** documenthandler.cpp:493-501
- **Severity:** Low
- **Analysis:** QFont::families() returns post-substitution resolved list. If user selects unavailable font, getter returns substitution name, not original selection.
- **Impact:** Silent font substitution; user sees different font name than selected.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ❔ UNSURE | 40 | fontFamily returns the format's family list; resolved-vs-requested unclear (documenthandler.cpp:500) |
| gpt-5.5-xhigh | ❔ UNSURE | 39 | runtime/platform behavior is not decidable from the cited snippet (src/documenthandler.cpp:493) |
| deepseek-v4-pro-max | ✅ LEGIT | 85 | documenthandler.cpp:493-501: fontFamilies() returns resolved-family list; if user selects unavailable font getter returns substitution name |
| glm-5.2-xhigh | ✅ LEGIT | 70 | documenthandler.cpp:493-501 fontFamily() returns resolved-family not requested-family; substitution invisible |
| kimi-k2.7-code | ❌ FALSE | 70 | documenthandler.cpp:493-501 returns font.families() first if set, which is the requested family, not resolved |
| opus-4.8-ultra | ❌ FALSE | 72 | max: code correct / claim mischaracterized — fontFamily returns the format's family list; resolved-vs-requested unclear (documenthandle |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

