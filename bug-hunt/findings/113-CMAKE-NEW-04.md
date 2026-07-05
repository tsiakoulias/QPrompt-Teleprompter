# [113-CMAKE-NEW-04] execute_process uses CMAKE_PREFIX_PATH (list) as scalar — broken command

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `src/CMakeLists.txt:512`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/CMakeLists.txt:512
- **Severity:** Medium
- **Analysis:** `${CMAKE_PREFIX_PATH}/bin/lconvert` — semicolon-separated list produces broken multi-path string. No RESULT_VARIABLE (silent failure). Redundant with qt_add_translations on line 345. Runs on all platforms including WASM where host binaries don't exist.
- **Impact:** Non-functional command, wasted configure time.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ✅ LEGIT | 60 | execute_process uses CMAKE_PREFIX_PATH list as scalar (CMakeLists.txt:512) |
| gpt-5.5-xhigh | ✅ LEGIT | 78 | executeprocess uses CMAKEPREFIXPATH (list) as scalar - broken command (src/CMakeLists.txt:512) |
| deepseek-v4-pro-max | ✅ LEGIT | 90 | ${CMAKE_PREFIX_PATH}/bin at src/CMakeLists.txt:512 — semicolon list used as scalar broken command |
| glm-5.2-xhigh | ✅ LEGIT | 80 | src/CMakeLists.txt:512 execute_process uses CMAKE_PREFIX_PATH (a list) as scalar path for lconvert |
| kimi-k2.7-code | ✅ LEGIT | 85 | src/CMakeLists.txt:512 uses ${CMAKE_PREFIX_PATH}/bin/lconvert as a scalar path despite CMAKE_PREFIX_PATH being a list. |
| opus-4.8-ultra | ✅ LEGIT | 60 | execute_process uses CMAKE_PREFIX_PATH list as scalar (CMakeLists.txt:512) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

