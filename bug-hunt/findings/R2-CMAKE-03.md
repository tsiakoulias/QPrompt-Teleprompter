# [R2-CMAKE-03] WORKING_DIRECTORY and COMMENT not parseable by callers of sphinx_add_docs

- **Status:** OPEN
- **Severity:** Medium
- **Category:** Platform/Build
- **Location:** `cmake/FindSphinx.cmake:67,72`
- **Consensus:** 5/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** cmake/FindSphinx.cmake:67,72
- **Severity:** Medium
- **Category:** Platform/Build
- **Analysis:** Function reads `${_WORKING_DIRECTORY}` and `${_COMMENT}` but neither keyword appears in cmake_parse_arguments spec. These variables are never populated from function arguments; callers cannot override working directory or build comment.
- **Impact:** After fixing CMAKE-01, WORKING_DIRECTORY and COMMENT still won't work unless added to one_value_keywords list.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 80 | WORKING_DIRECTORY/COMMENT absent from keyword lists (FindSphinx.cmake:67) |
| gpt | ✅ LEGIT | 78 | WORKING_DIRECTORY and COMMENT not parseable by callers of sphinx_add_docs (cmake/FindSphinx.cmake:67) |
| deepseek | ✅ LEGIT | 85 | WORKING_DIRECTORY and COMMENT not in cmake_parse_arguments spec at FindSphinx.cmake:67/72; callers cannot set these — affirmed |
| glm | ❌ FALSE | 80 | cmake/FindSphinx.cmake:67 72 WORKING_DIRECTORY and COMMENT are used in add_custom_target; parseable by callers |
| kimi | ✅ LEGIT | 85 | cmake/FindSphinx.cmake:67,72 reads _WORKING_DIRECTORY/_COMMENT but those keywords are absent from :56-58 spec. |
| opus-ultra | ✅ LEGIT | 80 | WORKING_DIRECTORY/COMMENT absent from keyword lists (FindSphinx.cmake:67) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

