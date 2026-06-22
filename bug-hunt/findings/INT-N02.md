# [INT-N02] replaceAll() returns long — 32-bit overflow on Windows x64

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.h:228, documenthandler.cpp:1494`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.h:228, documenthandler.cpp:1494
- **Severity:** Medium
- **Analysis:** long is 32-bit on Windows x64 (LLP64). Replacement counter silently overflows at 2^31 matches. Should be qlonglong/qint64.
- **Impact:** Replace-all count silently wrong on Windows with >2B matches.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 40 | replaceAll long is 32-bit on Win64; overflow practically impossible (documenthandler.cpp:1494) |
| gpt | ✅ LEGIT | 78 | replaceAll() returns long - 32-bit overflow on Windows x64 (src/documenthandler.h:228) |
| deepseek | ✅ LEGIT | 90 | documenthandler.h:228 / cpp:1494: replaceAll() returns long which is 32-bit on Windows x64 (LLP64); replacement counter overflows at 2^31 matches — use qlonglong |
| glm | ⚠️ PARTIAL | 60 | documenthandler.h:228 1494 replaceAll returns long; 32-bit overflow on Windows x64 where long is 32-bit |
| kimi | ✅ LEGIT | 85 | documenthandler.h:228 / documenthandler.cpp:1494 replaceAll returns long, which is 32-bit on Windows LLP64, overflowing past 2^31. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — replaceAll long is 32-bit on Win64; overflow practically impossible (documenthandler.cpp:1 |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

