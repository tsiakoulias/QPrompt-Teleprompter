# [HDR-N02] telemetry.h not in CMakeLists.txt — Telemetry dead code

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `src/telemetry.h, src/telemetry.cpp, src/CMakeLists.txt`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** src/telemetry.h, src/telemetry.cpp, src/CMakeLists.txt
- **Severity:** Low
- **Analysis:** Same as HDR-N01. Telemetry Q_OBJECT class never MOC-processed. All methods already commented out; source still exists on disk.
- **Impact:** Build hygiene — orphaned .h/.cpp create false expectations of functionality.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 60 | telemetry.h not in CMakeLists; Telemetry dead code (telemetry.h) |
| gpt | ⚠️ PARTIAL | 58 | observed telemetry.h not in CMakeLists.txt - Telemetry dead code (src/telemetry.h:1) |
| deepseek | ✅ LEGIT | 95 | telemetry.h/cpp not in src/CMakeLists.txt — Q_OBJECT class never compiled dead code |
| glm | ✅ LEGIT | 80 | telemetry.h/telemetry.cpp not in CMakeLists.txt; Telemetry dead code |
| kimi | ✅ LEGIT | 80 | telemetry.h/cpp exist but are absent from src/CMakeLists.txt source lists; class is never compiled. |
| opus-ultra | ✅ LEGIT | 60 | telemetry.h not in CMakeLists; Telemetry dead code (telemetry.h) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

