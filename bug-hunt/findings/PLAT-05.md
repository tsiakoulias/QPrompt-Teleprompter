# [PLAT-05] DBINARY_ICONS_RESOURCE is a typo — should be BINARY_ICONS_RESOURCE

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `CMakeLists.txt:110`
- **Consensus:** 5/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** CMakeLists.txt:110
- **Severity:** Medium
- **Code:**
  ```cmake
  set(DBINARY_ICONS_RESOURCE ON)   # extra "D" prefix
  ```
- **Analysis:** ECM's `ecm_install_icons` module uses `BINARY_ICONS_RESOURCE`. The `D` prefix means the variable never matches what ECM looks for. Likely a typo from deleting `//` comment prefix.
- **Impact:** Non-Android binary icon resources never enabled despite explicit intent.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 85 | DBINARY_ICONS_RESOURCE typo (CMakeLists.txt:110) |
| gpt | ✅ LEGIT | 92 | DBINARY_ICONS_RESOURCE is a typo - should be BINARY_ICONS_RESOURCE (CMakeLists.txt:110) |
| deepseek | ✅ LEGIT | 85 | DBINARY_ICONS_RESOURCE at CMakeLists.txt:110 should be BINARY_ICONS_RESOURCE; ECM expects BINARY_ICONS_RESOURCE — typo confirmed; D prefix makes ECM miss it |
| glm | ❌ FALSE | 85 | CMakeLists.txt:110 sets DBINARY_ICONS_RESOURCE which is a custom variable name not a typo; used consistently |
| kimi | ✅ LEGIT | 85 | CMakeLists.txt:110 sets DBINARY_ICONS_RESOURCE; ECM ecm_install_icons expects BINARY_ICONS_RESOURCE. |
| opus-ultra | ✅ LEGIT | 85 | DBINARY_ICONS_RESOURCE typo (CMakeLists.txt:110) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

