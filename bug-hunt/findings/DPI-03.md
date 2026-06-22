# [DPI-03] Find.qml:38 searchBarWidth:724 hardcoded in px

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `Find.qml:38`
- **Consensus:** 3/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** Find.qml:38
- **Severity:** Low
- **Analysis:** Hardcoded pixel width ignores DPI scaling.
- **Impact:** Search bar width wrong on non-default scaling.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | searchBarWidth:724 hardcoded px (Find.qml:38) |
| gpt | ⚠️ PARTIAL | 58 | visual issue is plausible but depends on theme or device (src/prompter/Find.qml:38) |
| deepseek | ✅ LEGIT | 90 | Hardcoded 724px searchBarWidth at Find.qml:38 — ignores DPI |
| glm | ✅ LEGIT | 75 | Find.qml:38 searchBarWidth:724 hardcoded in px |
| kimi | ❌ FALSE | 75 | Find.qml:38 width 724 is logical pixels; claim of DPI corruption mischaracterizes QML coordinate system. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — searchBarWidth:724 hardcoded px (Find.qml:38) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

