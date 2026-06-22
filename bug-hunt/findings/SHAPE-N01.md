# [SHAPE-N01] pointer_0.qml PathLine parent.width resolves to undefined (ShapePath has no width) — arrow collapsed

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `pointer_0.qml:60-67`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** pointer_0.qml:60-67
- **Severity:** Medium
- **Analysis:** parent inside PathLine is ShapePath (non-Item QObject, no width). parent.width = undefined → 0. Both PathLines collapse to (0,0). Arrow renders as single point instead of chevron.
- **Impact:** Arrow pointer shape never renders correctly.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 60 | PathLine parent.width = ShapePath.width (no width) -> undefined (pointer_0.qml:60) |
| gpt | ✅ LEGIT | 92 | pointer_0.qml PathLine parent.width resolves to undefined (ShapePath has no width) - arrow collapsed (src/prompter/pointers/pointer_0.qml:60) |
| deepseek | ✅ LEGIT | 80 | PathLine parent=ShapePath(QObject non-Item); parent.width=undefined->arrow coordinates degenerate at pointer_0.qml:60-67 |
| glm | ✅ LEGIT | 70 | pointer_0.qml:60-67 PathLine parent.width resolves to undefined (ShapePath has no width); arrow collapsed |
| kimi | ✅ LEGIT | 85 | pointer_0.qml:57/61/66 uses parent.width inside ShapePath, which has no width; x resolves as undefined |
| opus-ultra | ✅ LEGIT | 60 | PathLine parent.width = ShapePath.width (no width) -> undefined (pointer_0.qml:60) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

