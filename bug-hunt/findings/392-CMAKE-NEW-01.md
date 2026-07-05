# [392-CMAKE-NEW-01] Remote.qml exists on disk but never listed in QML_FILES

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `src/CMakeLists.txt, src/prompter/Remote.qml`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** src/CMakeLists.txt, src/prompter/Remote.qml
- **Severity:** Low
- **Analysis:** Remote.qml not in any CMake source list. Orphaned dead code.
- **Impact:** Runtime "not installed" error if Remote component ever referenced.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ⚠️ PARTIAL | 45 | Remote.qml on disk but not in QML_FILES (CMakeLists.txt) |
| gpt-5.5-xhigh | ✅ LEGIT | 78 | Remote.qml exists on disk but never listed in QMLFILES (src/CMakeLists.txt:260) |
| deepseek-v4-pro-max | ✅ LEGIT | 90 | Remote.qml on disk but not in any CMake QML_FILES — orphaned dead code |
| glm-5.2-xhigh | ✅ LEGIT | 75 | src/CMakeLists.txt Remote.qml exists on disk but not listed in QML_FILES (but is in WASM list at :132) |
| kimi-k2.7-code | ✅ LEGIT | 80 | src/prompter/Remote.qml exists but is not listed in any CMakeLists.txt QML_FILES/source list. |
| opus-4.8-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — Remote.qml on disk but not in QML_FILES (CMakeLists.txt) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

