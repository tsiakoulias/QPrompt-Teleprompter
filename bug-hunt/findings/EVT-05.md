# [EVT-05] Drag breaks positionHandler.x declarative binding permanently

- **Status:** OPEN
- **Severity:** High
- **Category:** 
- **Location:** `Prompter.qml:2018,926`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** Prompter.qml:2018,926
- **Severity:** High
- **Analysis:** Same pattern. drag.target breaks x binding; coordinate system becomes inconsistent.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | drag.target positionHandler may break its x binding (Prompter.qml:2018) |
| gpt | ⚠️ PARTIAL | 58 | observed Drag breaks positionHandler.x declarative binding permanently (src/prompter/Prompter.qml:2018) |
| deepseek | ✅ LEGIT | 92 | drag.target:positionHandler writes x imperatively breaking declarative x binding (Prompter.qml:2018 926) |
| glm | ✅ LEGIT | 80 | Prompter.qml:2018 926 Drag breaks positionHandler.x declarative binding permanently |
| kimi | ✅ LEGIT | 85 | Prompter.qml:2018 sets drag.target: positionHandler, which imperatively writes x and breaks the declarative x binding at Prompter.qml:926. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — drag.target positionHandler may break its x binding (Prompter.qml:2018) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

