# [R2-CMAKE-01] sphinx_add_docs silently ignores all keyword arguments due to empty cmake_parse_arguments prefix

- **Status:** REJECTED
- **Severity:** Critical
- **Category:** Platform/Build
- **Location:** `cmake/FindSphinx.cmake:54-56`
- **Consensus:** 3/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** cmake/FindSphinx.cmake:54-56
- **Severity:** Critical
- **Category:** Platform/Build
- **Analysis:** `cmake_parse_arguments(PARSE_ARGV 1 "" ...)` uses empty prefix `""` so parsed variables are named literally (`${ALL}`, `${BUILDER}`, etc.). But every access uses `_`-prefixed names (`${_ALL}`, `${_BUILDER}`). All keyword arguments from callers are silently ignored; documentation builds with wrong configuration.
- **Impact:** Any project using sphinx_add_docs() with parameters gets default behavior instead of configured behavior. ALL never adds to default target, BUILDER always defaults to "html", all boolean flags and options ignored.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❌ FALSE | 80 | empty prefix yields _ALL matching access (FindSphinx.cmake:55) |
| gpt | ❌ FALSE | 76 | empty cmake_parse_arguments prefix intentionally creates _ALL etc. (cmake/FindSphinx.cmake:54) |
| deepseek | ✅ LEGIT | 90 | cmake_parse_arguments empty prefix '' at FindSphinx.cmake:54; all accesses use _ prefixed vars; ALL/BUILDER etc parsed to unprefixed name — all args silently ignored |
| glm | ✅ LEGIT | 85 | cmake/FindSphinx.cmake:54-56 cmake_parse_arguments with empty prefix ''; keyword args parsed correctly actually—this works as intended |
| kimi | ✅ LEGIT | 95 | cmake/FindSphinx.cmake:54-56 cmake_parse_arguments prefix empty; parsed vars ALL/BUILDER not the accessed _ALL/_BUILDER. |
| opus-ultra | ❌ FALSE | 80 | empty prefix yields _ALL matching access (FindSphinx.cmake:55) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

