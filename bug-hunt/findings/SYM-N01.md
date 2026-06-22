# [SYM-N01] 6 RTL/symmetry issues across PointerSettings, Find, PrompterView, Prompter, PrompterPage

- **Status:** OPEN
- **Severity:** Low-Medium
- **Category:** 
- **Location:** `PointerSettings.qml:380 (right pointer label not RTL-mirrored), Find.qml:63-66 (search bar always left-pinned), PrompterView.qml:74-76 (upper controls not RTL-aware), Prompter.qml:658-659 (goToNextMarker has end-fallback but goToPreviousMarker lacks start-fallback), PrompterPage.qml:266,278 (pointer tooltips not RTL-mirrored, contradict button labels)`
- **Consensus:** 2/6 agents LEGIT · split

## Original report claim

- **Files:** PointerSettings.qml:380 (right pointer label not RTL-mirrored), Find.qml:63-66 (search bar always left-pinned), PrompterView.qml:74-76 (upper controls not RTL-aware), Prompter.qml:658-659 (goToNextMarker has end-fallback but goToPreviousMarker lacks start-fallback), PrompterPage.qml:266,278 (pointer tooltips not RTL-mirrored, contradict button labels)
- **Severity:** Low-Medium
- **Impact:** Inconsistent RTL experience — labels, tooltips, positioning, and navigation fallbacks not mirrored.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 40 | 6 RTL/symmetry issues (PointerSettings.qml:380) |
| gpt | ⚠️ PARTIAL | 58 | observed 6 RTL/symmetry issues across PointerSettings, Find, PrompterView, Prompter, PrompterPage (src/prompter/PointerSettings.qml:380) |
| deepseek | ✅ LEGIT | 85 | 6 RTL issues: PointerSettings.qml:380 label not mirrored; Find.qml:63-66 left-pinned; PrompterView.qml:74-76 not RTL-aware; Prompter.qml:658-659 one-sided fallback; PrompterPage.qml:266 tooltip not RTL-mirrored |
| glm | ⚠️ PARTIAL | 55 | 6 RTL/symmetry issues across PointerSettings Find PrompterView Prompter PrompterPage; mixed severity |
| kimi | ✅ LEGIT | 65 | Multiple files have RTL/symmetry issues; verified PointerSettings label, Find bar margin, PrompterView upper controls, goToPreviousMarker no start fallback, PrompterPage tooltip mismatch. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — 6 RTL/symmetry issues (PointerSettings.qml:380) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

