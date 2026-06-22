# [R2-CMAKE-02] cmake_minimum_required inside find module pollutes parent project policy settings

- **Status:** OPEN
- **Severity:** High
- **Category:** Platform/Build
- **Location:** `cmake/FindSphinx.cmake:19`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** cmake/FindSphinx.cmake:19
- **Severity:** High
- **Category:** Platform/Build
- **Analysis:** `cmake_minimum_required(VERSION 3.20...3.29)` in a find module sets all CMake policies up to 3.29 to NEW for the including project. CMake docs state "Do not call cmake_minimum_required() in a find module." Can silently change parent project's policy behavior.
- **Impact:** Subtle, hard-to-debug build failures in projects including this module. Should be removed entirely.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 80 | cmake_minimum_required in find module (FindSphinx.cmake:19) |
| gpt | ✅ LEGIT | 84 | cmake_minimum_required inside find module pollutes parent project policy settings (cmake/FindSphinx.cmake:19) |
| deepseek | ✅ LEGIT | 90 | cmake_minimum_required inside find module at FindSphinx.cmake:19 pollutes parent policy; per CMake docs should not be in find modules |
| glm | ⚠️ PARTIAL | 60 | cmake/FindSphinx.cmake:19 cmake_minimum_required inside find module; pollutes policy but not a build breaker |
| kimi | ✅ LEGIT | 90 | cmake/FindSphinx.cmake:19 cmake_minimum_required inside find module changes parent project policies. |
| opus-ultra | ✅ LEGIT | 80 | cmake_minimum_required in find module (FindSphinx.cmake:19) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

