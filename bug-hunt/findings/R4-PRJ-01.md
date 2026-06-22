# [R4-PRJ-01] flip variable spuriously reset in project() inner loop else-branch

- **Status:** REJECTED
- **Severity:** High
- **Category:** Logic
- **Location:** `src/prompter/ProjectionsManager.qml:108-114`
- **Consensus:** 0/6 agents LEGIT · split

## Original report claim

- **File:** src/prompter/ProjectionsManager.qml:108-114
- **Severity:** High
- **Category:** Logic
- **Analysis:** Inner for loop sets flip on match, but else runs for EVERY non-matching iteration, unconditionally resetting flip to defaultDisplayMode. First match silently discarded.
- **Impact:** Screens configured for projection (flip>0) get no projection window if any non-matching display entry follows.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❌ FALSE | 80 | break preserves match (ProjectionsManager.qml:108) |
| gpt | ❌ FALSE | 76 | the inner break exits after a match; it does not discard it (src/prompter/ProjectionsManager.qml:108) |
| deepseek | ❌ FALSE | 85 | ProjectionsManager.qml:108-114 break exits immediately on match before else runs for that iteration — flip correctly set by match; no spurious reset |
| glm | ⚠️ PARTIAL | 60 | ProjectionsManager.qml:108-114 flip variable reset in else-branch; may cause visual glitch but not critical |
| kimi | ❌ FALSE | 90 | Inner loop breaks on match; non-matching else resets default but does not discard the actual match; ProjectionsManager.qml:108-114 |
| opus-ultra | ❌ FALSE | 80 | break preserves match (ProjectionsManager.qml:108) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

