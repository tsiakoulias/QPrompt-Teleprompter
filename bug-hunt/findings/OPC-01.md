# [OPC-01] Right-click toggle desynchronizes velocityIndicator visible/opacity

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `PrompterPage.qml:906,979-980`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** PrompterPage.qml:906,979-980
- **Severity:** Medium
- **Analysis:** Right-click toggles only opacity (0 ↔ 1), leaving visible=true. When opacity=0 but visible=true: middle-click reactivation blocked, full-screen MouseArea consumes input, auto-dismiss Connection fires inconsistently.
- **Impact:** Velocity indicator stuck in invisible-but-interactive state; requires second right-click to recover.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | right-click toggle desyncs indicator visible/opacity (PrompterPage.qml:906) |
| gpt | ✅ LEGIT | 78 | Right-click toggle desynchronizes velocityIndicator visible/opacity (src/kirigami_ui/PrompterPage.qml:906) |
| deepseek | ✅ LEGIT | 90 | Only opacity toggled at PrompterPage.qml:906; visible stays true — breaks middle-click reactivation |
| glm | ✅ LEGIT | 80 | PrompterPage.qml:906 979-980 right-click toggle desynchronizes velocityIndicator visible/opacity |
| kimi | ✅ LEGIT | 85 | PrompterPage.qml:906 right-click only flips velocityIndicator.opacity; visible stays true so velocityDragOverlay keeps capturing input. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — right-click toggle desyncs indicator visible/opacity (PrompterPage.qml:906) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

