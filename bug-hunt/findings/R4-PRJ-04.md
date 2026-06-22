# [R4-PRJ-04] Division by zero in projection image height

- **Status:** OPEN
- **Severity:** Medium
- **Category:** Edge Case
- **Location:** `src/prompter/ProjectionsManager.qml:298`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/prompter/ProjectionsManager.qml:298
- **Severity:** Medium
- **Category:** Edge Case
- **Analysis:** height calculation divides by forwardTo.width/height which may be 0 before main prompter layout. Produces Infinity/NaN → broken Image geometry.
- **Impact:** Projection windows show degenerate/stretched image at startup until main window first paints.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 55 | div by zero parent.width/forwardTo.width at startup (ProjectionsManager.qml:298) |
| gpt | ✅ LEGIT | 78 | Division by zero in projection image height (src/prompter/ProjectionsManager.qml:298) |
| deepseek | ✅ LEGIT | 85 | ProjectionsManager.qml:298 divides by forwardTo.width which may be 0 before main prompter layout — Infinity/NaN leading to degenerate Image geometry |
| glm | ✅ LEGIT | 80 | ProjectionsManager.qml:298 division by zero in projection image height when forwardTo.width is 0 |
| kimi | ✅ LEGIT | 90 | Image height divides by projectionManager.forwardTo.width in reScale path; division by zero possible; ProjectionsManager.qml:298 |
| opus-ultra | ✅ LEGIT | 55 | div by zero parent.width/forwardTo.width at startup (ProjectionsManager.qml:298) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

