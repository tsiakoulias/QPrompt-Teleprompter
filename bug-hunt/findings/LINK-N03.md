# [LINK-N03] Qt::WebSockets found as REQUIRED but never explicitly linked

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `CMakeLists.txt:145, all target_link_libraries blocks`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** CMakeLists.txt:145, all target_link_libraries blocks
- **Severity:** Medium
- **Analysis:** find_package REQUIRED ensures module installed but no target_link_libraries entry on any platform. Works on dynamic-link via QML plugin; breaks on static if qmlimportscanner misses it.
- **Impact:** OBS WebSocket integration broken on static builds if auto-scan fails.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | Qt::WebSockets found REQUIRED but not explicitly linked; QML plugin pulls it (CMakeLists.txt:145) |
| gpt | ✅ LEGIT | 78 | Qt::WebSockets found as REQUIRED but never explicitly linked (CMakeLists.txt:145) |
| deepseek | ✅ LEGIT | 85 | src/CMakeLists.txt: all target_link_libraries blocks lack Qt6::WebSockets; find_package REQUIRED but never linked — breaks static builds if qmlimportscanner misses it |
| glm | ✅ LEGIT | 75 | CMakeLists.txt:145 Qt::WebSockets found as REQUIRED but never explicitly linked in target_link_libraries |
| kimi | ✅ LEGIT | 80 | CMakeLists.txt:145 finds Qt::WebSockets REQUIRED but src/CMakeLists.txt target_link_libraries blocks never link it. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — Qt::WebSockets found REQUIRED but not explicitly linked; QML plugin pulls it (CMakeLists.t |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

