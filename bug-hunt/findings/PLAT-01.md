# [PLAT-01] KF6Crash_FOUND never defined as C preprocessor macro — KCrash support dead code

- **Status:** OPEN
- **Severity:** High
- **Category:** 
- **Location:** `src/main.cpp:50, CMakeLists.txt:316`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** src/main.cpp:50, CMakeLists.txt:316
- **Severity:** High
- **Code:**
  ```cmake
  find_package(KF6Crash ...)   # sets CMake variable, NOT C++ preprocessor macro
  ```
  ```cpp
  #if defined(KF6Crash_FOUND)   // always false — never #defined
  ```
- **Analysis:** CMake's `find_package` sets the CMake variable `KF6Crash_FOUND`, but this is never translated to a C++ preprocessor macro via `target_compile_definitions`. No `add_definitions(-DKF6Crash_FOUND)` or similar. Also, `KF6::Crash` is never linked. Compare with `QHotkey_FOUND` which IS correctly added at `src/CMakeLists.txt:496`.
- **Impact:** KCrash (crash handling, DrKonqi, auto-restart) is never compiled into the binary on any platform. Entire `#include <KCrash>` and `KCrash::initialize()` blocks are dead code.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 90 | KF6Crash_FOUND never -D; KF6::Crash never linked (main.cpp:50) |
| gpt | ⚠️ PARTIAL | 58 | observed KF6Crash_FOUND never defined as C preprocessor macro - KCrash support dead code (src/main.cpp:50) |
| deepseek | ✅ LEGIT | 90 | KF6Crash_FOUND at main.cpp:50 checked via #if defined but CMake never adds compile definition; KCrash code dead; confirmed at CMakeLists.txt:316 — find_package sets CMake var not C++ macro |
| glm | ⚠️ PARTIAL | 65 | main.cpp:50 uses KF6Crash_FOUND but CMakeLists.txt:316 uses find_package without add_compile_definitions; KCrash block dead |
| kimi | ✅ LEGIT | 90 | main.cpp:50 #if defined(KF6Crash_FOUND) never true; CMakeLists.txt:316 find_package sets CMake var not compile definition. |
| opus-ultra | ✅ LEGIT | 90 | KF6Crash_FOUND never -D; KF6::Crash never linked (main.cpp:50) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

