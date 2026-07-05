# [285-CMAKE-N03] qt_wrap_ui conflicts with global AUTOUIC — double UI processing

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `src/CMakeLists.txt:43-46 vs CMakeLists.txt:45`
- **Consensus:** 4/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** src/CMakeLists.txt:43-46 vs CMakeLists.txt:45
- **Severity:** Medium
- **Analysis:** Both mechanisms process systemfontchooserdialog.ui. Redundant code generation, race in parallel builds.
- **Impact:** Build failures or duplicate symbols in parallel builds.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ⚠️ PARTIAL | 50 | qt_wrap_ui + AUTOUIC may double-process .ui (CMakeLists.txt:43) |
| gpt-5.5-xhigh | ❌ FALSE | 76 | AUTOUIC can coexist with qt_wrap_ui; duplicate processing is not shown (src/CMakeLists.txt:43) |
| deepseek-v4-pro-max | ✅ LEGIT | 85 | src/CMakeLists.txt:43-46 vs CMakeLists.txt:45: qt_wrap_ui + AUTOUIC both process systemfontchooserdialog.ui; double code generation — race in parallel builds |
| glm-5.2-xhigh | ✅ LEGIT | 75 | src/CMakeLists.txt:43-46 qt_wrap_ui conflicts with global AUTOUIC at CMakeLists.txt:45; double UI processing |
| kimi-k2.7-code | ✅ LEGIT | 80 | CMakeLists.txt:45 enables CMAKE_AUTOUIC and src/CMakeLists.txt:43-46 also calls qt_wrap_ui causing duplicate processing. |
| opus-4.8-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — qt_wrap_ui + AUTOUIC may double-process .ui (CMakeLists.txt:43) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

