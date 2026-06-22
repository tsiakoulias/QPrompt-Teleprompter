# [PLAT-07] Incorrect macro syntax: `#define Use_GlobalAccel = 1`

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `src/globalhotkeys.cpp:29`
- **Consensus:** 4/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** src/globalhotkeys.cpp:29
- **Severity:** Low
- **Code:**
  ```cpp
  #define Use_GlobalAccel = 1  // defines macro to "= 1", not to "1"
  ```
- **Analysis:** Currently benign (only `#ifdef` tested), but any value-check (`#if Use_GlobalAccel`) would produce syntax error.
- **Impact:** Latent compile error if value-check is ever added.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 95 | #define Use_GlobalAccel = 1 malformed (dup TYP-06) (globalhotkeys.cpp:29) |
| gpt | ⚠️ PARTIAL | 58 | bad macro expansion is latent; existing preprocessor tests are presence-only (src/globalhotkeys.cpp:29) |
| deepseek | ✅ LEGIT | 85 | Same as TYP-06; #define Use_GlobalAccel = 1 at globalhotkeys.cpp:29 defines to = 1 not 1; latent compile error if #if value-check used |
| glm | ❌ FALSE | 75 | globalhotkeys.cpp:29 #define Use_GlobalAccel = 1 works as existence-only macro; #ifdef checks pass |
| kimi | ✅ LEGIT | 90 | globalhotkeys.cpp:29 malformed #define Use_GlobalAccel = 1 (same as TYP-06). |
| opus-ultra | ✅ LEGIT | 95 | #define Use_GlobalAccel = 1 malformed (dup TYP-06) (globalhotkeys.cpp:29) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

