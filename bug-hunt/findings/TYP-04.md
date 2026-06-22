# [TYP-04] Bitwise AND on bools hides dead code in preventSleep

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `src/documenthandler.cpp:1928,1931`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** src/documenthandler.cpp:1928,1931
- **Severity:** Medium
- **Code:**
  ```cpp
  return false & prevent;
  ```
- **Analysis:** `&` on bools: `false & prevent` → `0 & (0|1)` → always `0` (false). The `prevent` parameter is dead code — has zero effect. Should be `&&` or just `return false;`.
- **Impact:** On iOS/non-Android, the `prevent` parameter is silently ignored; function always returns false.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 95 | false & prevent -> prevent dead (documenthandler.cpp:1928) |
| gpt | ⚠️ PARTIAL | 58 | observed Bitwise AND on bools hides dead code in preventSleep (src/documenthandler.cpp:1928) |
| deepseek | ✅ LEGIT | 90 | return false & prevent at doc.cpp:1928/1931; bitwise & on bool always 0(false) — prevent param dead code; should be && or just return false |
| glm | ✅ LEGIT | 85 | documenthandler.cpp:1928 1931 uses false & prevent which is bitwise AND on bools; both branches return false making iOS preventSleep always return false |
| kimi | ✅ LEGIT | 90 | documenthandler.cpp:1928,1931 return false & prevent; result is always false so prevent parameter is ignored. |
| opus-ultra | ✅ LEGIT | 95 | false & prevent -> prevent dead (documenthandler.cpp:1928) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

