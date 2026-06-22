# [RND-N03] Missing smooth: true on projection Image — aliased text on external displays

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `ProjectionsManager.qml:284-304`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** ProjectionsManager.qml:284-304
- **Severity:** Low
- **Analysis:** Projection Image frequently re-scaled for different screen sizes. Nearest-neighbor filtering makes text jagged on large external monitors/projectors.
- **Impact:** Pixelated prompter content on external projection screens.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | missing smooth:true on projection Image; aliased (ProjectionsManager.qml:284) |
| gpt | ⚠️ PARTIAL | 58 | observed Missing smooth: true on projection Image - aliased text on external displays (src/prompter/ProjectionsManager.qml:284) |
| deepseek | ✅ LEGIT | 85 | ProjectionsManager.qml:284-304: projection Image lacks smooth:true; text aliased on scaled external displays |
| glm | ✅ LEGIT | 70 | ProjectionsManager.qml:284-304 missing smooth: true on projection Image; aliased text |
| kimi | ✅ LEGIT | 80 | ProjectionsManager.qml:284-304 projection Image lacks `smooth: true`; scaling with nearest filter causes aliasing. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — missing smooth:true on projection Image; aliased (ProjectionsManager.qml:284) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

