# [STC-N03] velocityIndicator.firstResetDone never cleared on dismiss — second activation broken

- **Status:** NEEDS-INFO
- **Severity:** Medium
- **Category:** 
- **Location:** `PrompterPage.qml:799-872,928-937`
- **Consensus:** 2/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** PrompterPage.qml:799-872,928-937
- **Severity:** Medium
- **Analysis:** velocityDragOverlay.dismiss() never clears firstResetDone, originX/Y, originalVelocity. Next activation: firstResetDone still true → cursor warps to page-middle not indicator-center.
- **Impact:** Velocity indicator mouse tracking broken on second activation.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❔ UNSURE | 45 | velocityIndicator.firstResetDone not cleared on dismiss; domain (PrompterPage.qml:799) |
| gpt | ⚠️ PARTIAL | 58 | observed velocityIndicator.firstResetDone never cleared on dismiss - second activation broken (src/kirigami_ui/PrompterPage.qml:799) |
| deepseek | ✅ LEGIT | 90 | PrompterPage.qml:928-937: dismiss() never clears firstResetDone/originX/Y; second activation cursor warps to page-middle not indicator-center |
| glm | ✅ LEGIT | 70 | PrompterPage.qml:799-872 928-937 velocityIndicator.firstResetDone never cleared on dismiss; second activation broken |
| kimi | ❌ FALSE | 65 | velocityIndicator.firstResetDone is set to false on every activation (PrompterPage.qml:900); stale-on-dismiss not shown |
| opus-ultra | ❔ UNSURE | 45 | max: unverifiable statically (runtime/semantic) — velocityIndicator.firstResetDone not cleared on dismiss; domain (PrompterPage.qml:799) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

