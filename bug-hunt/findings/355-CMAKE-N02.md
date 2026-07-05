# [355-CMAKE-N02] INTERFACE_LINK_LIBRARIES on executable target — no-op

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `src/CMakeLists.txt:285`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/CMakeLists.txt:285
- **Severity:** Low
- **Analysis:** INTERFACE_LINK_LIBRARIES is no-op on executable — nothing links against an executable's interface.
- **Impact:** Dead code.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ✅ LEGIT | 55 | INTERFACE_LINK_LIBRARIES on executable target is a no-op (CMakeLists.txt:285) |
| gpt-5.5-xhigh | ✅ LEGIT | 78 | INTERFACE_LINK_LIBRARIES on executable target - no-op (src/CMakeLists.txt:285) |
| deepseek-v4-pro-max | ✅ LEGIT | 95 | src/CMakeLists.txt:285: INTERFACE_LINK_LIBRARIES on executable target is no-op; nothing links against an executable's interface — dead code |
| glm-5.2-xhigh | ✅ LEGIT | 70 | src/CMakeLists.txt:285 INTERFACE_LINK_LIBRARIES on executable target; no-op |
| kimi-k2.7-code | ✅ LEGIT | 90 | src/CMakeLists.txt:285 sets INTERFACE_LINK_LIBRARIES on executable target where it has no effect. |
| opus-4.8-ultra | ✅ LEGIT | 55 | INTERFACE_LINK_LIBRARIES on executable target is a no-op (CMakeLists.txt:285) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

