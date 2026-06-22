# [CMT-N08] Entire Telemetry class is dead commented-out shell across 4 files

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `telemetry.h, telemetry.cpp, promptsession.h, promptsession.cpp`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** telemetry.h, telemetry.cpp, promptsession.h, promptsession.cpp
- **Severity:** Medium
- **Analysis:** All methods commented out. Class compiles to nothing. Should be removed or clearly marked as planned.
- **Impact:** Dead files create false expectation of telemetry functionality.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 50 | Telemetry class is dead commented-out shell (telemetry.h) |
| gpt | ⚠️ PARTIAL | 48 | comment problem observed, but defect impact is limited (src/telemetry.h:1) |
| deepseek | ✅ LEGIT | 90 | All Telemetry methods commented out across 4 files — dead shell creates false expectations |
| glm | ✅ LEGIT | 75 | telemetry.h telemetry.cpp promptsession.h promptsession.cpp Telemetry class is dead commented-out shell |
| kimi | ✅ LEGIT | 75 | telemetry.h/cpp and promptsession.h/cpp are largely commented-out shells and are not compiled. |
| opus-ultra | ✅ LEGIT | 50 | Telemetry class is dead commented-out shell (telemetry.h) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

