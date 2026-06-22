# [EVT-N12] velocityDragArea and viewport.mouse share z:5 — wheel dispatch ambiguous

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `PrompterPage.qml:875-877 vs PrompterView.qml:3083`
- **Consensus:** 2/6 agents LEGIT · split

## Original report claim

- **File:** PrompterPage.qml:875-877 vs PrompterView.qml:3083
- **Severity:** Low
- **Analysis:** Same-z siblings in Prompting state. velocityDragArea (no wheel handler) declared later → sits "on top" of viewport.mouse (has wheel handler). Qt version-dependent: may silently consume wheel events even without onWheel.
- **Impact:** Wheel scrolling may fail intermittently during prompting on some Qt builds.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | velocityDragArea/viewport.mouse share z:5; wheel ambiguous (PrompterPage.qml:875) |
| gpt | ⚠️ PARTIAL | 58 | observed velocityDragArea and viewport.mouse share z:5 - wheel dispatch ambiguous (src/kirigami_ui/PrompterPage.qml:875) |
| deepseek | ✅ LEGIT | 60 | velocityDragArea and viewport.mouse share z:5; wheel event dispatch ambiguous (PrompterPage.qml:875-877 vs PrompterView.qml:249) |
| glm | ⚠️ PARTIAL | 60 | PrompterPage.qml:875-877 vs PrompterView.qml:3083 velocityDragArea and viewport.mouse share z:5; wheel dispatch ambiguous |
| kimi | ⚠️ PARTIAL | 50 | velocityDragArea is z:5 but viewport.mouse gets z:5 only in Prompting/Countdown states; real ambiguity not demonstrated. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — velocityDragArea/viewport.mouse share z:5; wheel ambiguous (PrompterPage.qml:875) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

