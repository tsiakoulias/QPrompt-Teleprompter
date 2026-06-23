# [256-RENDER-01] ShaderEffectSource prompterShadowSource runs unconditionally — wastes GPU capture when shadows disabled

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `PrompterView.qml:230-233`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** PrompterView.qml:230-233
- **Severity:** Medium
- **Analysis:** `live` defaults to true. Captures entire prompter Flickable to texture every frame. Downstream shadow chain gated by `layer.enabled: root.shadows` in Prompter.qml:744, but shadowSource has no `live: root.shadows` guard. When shadows off (default), every frame incurs full off-screen render + GPU texture copy.
- **Impact:** Unnecessary GPU bandwidth and frame-time increase on every frame during prompting.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | prompterShadowSource runs unconditionally; GPU waste (PrompterView.qml:230) |
| gpt | ✅ LEGIT | 78 | ShaderEffectSource prompterShadowSource runs unconditionally - wastes GPU capture when shadows disabled (src/prompter/PrompterView.qml:230) |
| deepseek | ✅ LEGIT | 70 | ShaderEffectSource unconditionally captures GPU regardless of shadows setting (PrompterView.qml:230-233) |
| glm | ✅ LEGIT | 75 | PrompterView.qml:230-233 prompterShadowSource ShaderEffectSource runs unconditionally even when shadows disabled |
| kimi | ✅ LEGIT | 80 | PrompterView.qml:230-233 instantiates prompterShadowSource with default live=true and no guard; Prompter.qml:744 only enables the consuming layer when root.shadows, so capture continues while shadows are disabled. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — prompterShadowSource runs unconditionally; GPU waste (PrompterView.qml:230) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

