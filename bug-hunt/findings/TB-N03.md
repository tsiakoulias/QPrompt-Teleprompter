# [TB-N03] Collapsible toolbar rows animate height but adjacent rows snap — no y-position animation

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `EditorToolbar.qml:1175-1906 (8 collapsible rows)`
- **Consensus:** 2/6 agents LEGIT · split

## Original report claim

- **File:** EditorToolbar.qml:1175-1906 (8 collapsible rows)
- **Severity:** Low
- **Analysis:** Behavior on height smooth, but Flow recalculates sibling positions immediately — rows below jump to new position without animation.
- **Impact:** Jarring visual — half animations smooth, half teleport.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | collapsible rows animate height but neighbors snap (EditorToolbar.qml:1175) |
| gpt | ⚠️ PARTIAL | 58 | observed Collapsible toolbar rows animate height but adjacent rows snap - no y-position animation (src/kirigami_ui/EditorToolbar.qml:1175) |
| deepseek | ✅ LEGIT | 70 | EditorToolbar.qml: collapsible rows have Behavior on height but Flow recalculates siblings immediately; rows below snap without animation |
| glm | ⚠️ PARTIAL | 55 | EditorToolbar.qml:1175-1906 8 collapsible rows animate height but adjacent rows snap; no y-position animation |
| kimi | ✅ LEGIT | 65 | EditorToolbar collapsible rows animate height only; adjacent rows snap because no y-position animation is applied |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — collapsible rows animate height but neighbors snap (EditorToolbar.qml:1175) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

