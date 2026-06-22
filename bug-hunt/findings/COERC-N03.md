# [COERC-N03] real→int truncation in WindowDragger position compounds drift

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `WindowDragger.qml:28-34`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** WindowDragger.qml:28-34
- **Severity:** Low
- **Analysis:** mouse.x (qreal/double) stored to prevX (int) — loses ~0.5px mean error per drag start. Compounds with FINAL-05 algebraic accumulation.
- **Impact:** Window position drift larger than documented in FINAL-05 alone.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | real->int truncation in WindowDragger compounds drift (FINAL-05 family) (WindowDragger.qml:28) |
| gpt | ⚠️ PARTIAL | 58 | observed real->int truncation in WindowDragger position compounds drift (src/qt/WindowDragger.qml:28) |
| deepseek | ✅ LEGIT | 80 | WindowDragger.qml:28-34: mouse.x (qreal) stored to prevX (int) losing fractional precision; compounds drift on each drag start |
| glm | ✅ LEGIT | 70 | WindowDragger.qml:28-34 real→int truncation in position compounds drift |
| kimi | ✅ LEGIT | 80 | WindowDragger.qml:28 prevX/prevY declared int; mouse.x qreal truncated each press; compounds drift. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — real->int truncation in WindowDragger compounds drift (FINAL-05 family) (WindowDragger.qml |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

