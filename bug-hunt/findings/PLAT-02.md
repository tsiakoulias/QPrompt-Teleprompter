# [PLAT-02] REQUIRED_KF6_VERSION variable referenced but never defined

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `CMakeLists.txt:309,316`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** CMakeLists.txt:309,316
- **Severity:** Medium
- **Code:**
  ```cmake
  find_package(KF${QT_VERSION_MAJOR}Crash ${REQUIRED_KF${QT_VERSION_MAJOR}_VERSION} ...)
  ```
- **Analysis:** `REQUIRED_KF6_VERSION` is never set. Expands to empty string in `find_package`, dropping the version requirement silently.
- **Impact:** KF6Crash found without version constraint; incompatible versions may be accepted.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 90 | REQUIRED_KF6_VERSION never set (CMakeLists.txt:309) |
| gpt | ✅ LEGIT | 78 | REQUIRED_KF6_VERSION variable referenced but never defined (CMakeLists.txt:309) |
| deepseek | ✅ LEGIT | 85 | REQUIRED_KF6_VERSION never defined; expands to empty at CMakeLists.txt:309; KF6Crash version constraint silently dropped |
| glm | ✅ LEGIT | 85 | CMakeLists.txt:309 316 reference REQUIRED_KF6_VERSION but variable never defined anywhere in build files |
| kimi | ✅ LEGIT | 85 | CMakeLists.txt:309,316 uses REQUIRED_KF6_VERSION variable that is never set; version constraint silently dropped. |
| opus-ultra | ✅ LEGIT | 90 | REQUIRED_KF6_VERSION never set (CMakeLists.txt:309) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

