# [112-CMAKE-NEW-03] find_package(KF6Crash ... COMPONENTS) — COMPONENTS keyword with zero names

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `CMakeLists.txt:316`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** CMakeLists.txt:316
- **Severity:** Medium
- **Analysis:** `find_package(KF6Crash ${REQUIRED_KF6_VERSION} COMPONENTS)` — after expansion, COMPONENTS keyword has no arguments. Syntax error. No QUIET – hard-errors if not found despite TYPE OPTIONAL next line.
- **Impact:** CMake warning/error on configure.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ✅ LEGIT | 55 | find_package KF6Crash COMPONENTS with zero names (CMakeLists.txt:316) |
| gpt-5.5-xhigh | ✅ LEGIT | 78 | findpackage(KF6Crash ... COMPONENTS) - COMPONENTS keyword with zero names (CMakeLists.txt:316) |
| deepseek-v4-pro-max | ✅ LEGIT | 90 | find_package(KF6Crash ... COMPONENTS) at CMakeLists.txt:316 — COMPONENTS keyword with zero args |
| glm-5.2-xhigh | ✅ LEGIT | 80 | CMakeLists.txt:316 find_package(KF6Crash ... COMPONENTS) with COMPONENTS keyword but zero component names |
| kimi-k2.7-code | ✅ LEGIT | 85 | CMakeLists.txt uses find_package(KF6Crash ${REQUIRED_KF6_VERSION} COMPONENTS) with empty COMPONENTS and REQUIRED_KF6_VERSION undefined. |
| opus-4.8-ultra | ✅ LEGIT | 55 | find_package KF6Crash COMPONENTS with zero names (CMakeLists.txt:316) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

