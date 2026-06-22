# [EVT-10] Nested MouseAreas with hoverEnabled steal hover from parent Buttons

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `ProjectionsManager.qml:347-354,376-383,405-412`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** ProjectionsManager.qml:347-354,376-383,405-412
- **Severity:** Low
- **Analysis:** Child MouseArea hoverEnabled:true fills parent Button. Button's hovered property never fires → flat highlight missing.

---

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | nested hoverEnabled MouseAreas steal hover (ProjectionsManager.qml:347) |
| gpt | ⚠️ PARTIAL | 58 | observed Nested MouseAreas with hoverEnabled steal hover from parent Buttons (src/prompter/ProjectionsManager.qml:347) |
| deepseek | ✅ LEGIT | 85 | nested MouseArea hoverEnabled:true fills parent Button; Button.hovered never fires (ProjectionsManager.qml:347-354) |
| glm | ⚠️ PARTIAL | 60 | ProjectionsManager.qml:347+ nested MouseAreas with hoverEnabled steal hover from parent Buttons |
| kimi | ✅ LEGIT | 85 | ProjectionsManager.qml:347-354 places a hover-enabled MouseArea filling a Button, so the Button's hovered state never triggers. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — nested hoverEnabled MouseAreas steal hover (ProjectionsManager.qml:347) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

