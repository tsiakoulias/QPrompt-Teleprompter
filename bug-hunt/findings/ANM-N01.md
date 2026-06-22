# [ANM-N01] Easing.EaseOut is not a valid Qt Quick easing type (2 instances)

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `PrompterView.qml:88,140`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** PrompterView.qml:88,140
- **Severity:** Medium
- **Analysis:** `Easing.EaseOut` is CSS convention, not valid QML. Valid: Easing.OutQuad, Easing.OutCubic, etc. Falls back to Easing.Linear silently.
- **Impact:** Margin animations run abruptly instead of smoothly easing.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 70 | Easing.EaseOut is not a valid Qt Quick easing type (PrompterView.qml:88) |
| gpt | ✅ LEGIT | 78 | Easing.EaseOut is not a valid Qt Quick easing type (2 instances) (src/prompter/PrompterView.qml:88) |
| deepseek | ✅ LEGIT | 92 | Easing.EaseOut is CSS convention not valid Qt Quick type; falls back to Easing.Linear silently (PrompterView.qml:88 140) |
| glm | ✅ LEGIT | 80 | PrompterView.qml:88 140 Easing.EaseOut is not valid Qt Quick easing type; should be Easing.OutQuad or similar |
| kimi | ✅ LEGIT | 90 | PrompterView.qml:88 uses Easing.EaseOut, which is not a valid Qt Quick easing type; it falls back to Easing.Linear. |
| opus-ultra | ✅ LEGIT | 70 | Easing.EaseOut is not a valid Qt Quick easing type (PrompterView.qml:88) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

