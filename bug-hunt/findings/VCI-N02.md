# [VCI-N02] upperControls and bottomControls fade to different opacity levels during Prompting

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `PrompterView.qml:70 vs 120`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** PrompterView.qml:70 vs 120
- **Severity:** Low
- **Analysis:** Top controls fade to 0.1, bottom controls to 0.2 during Prompting. Identical purpose, different opacity target.
- **Impact:** Asymmetric fade — top controls nearly invisible while bottom controls remain twice as visible.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 40 | upper/bottom controls fade to different opacity (PrompterView.qml:70) |
| gpt | ⚠️ PARTIAL | 48 | visual issue is plausible but depends on theme or device (src/prompter/PrompterView.qml:70) |
| deepseek | ✅ LEGIT | 95 | PrompterView.qml:70 vs 120: upperControls fades to 0.1 during Prompting; bottomControls to 0.2 — top controls nearly invisible while bottom twice as visible |
| glm | ✅ LEGIT | 70 | PrompterView.qml:70 vs 120 upperControls and bottomControls fade to different opacity levels |
| kimi | ✅ LEGIT | 70 | PrompterView.qml:70 fades upperControls to opacity 0.1 during Prompting while line 120 fades bottomControls to 0.2. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — upper/bottom controls fade to different opacity (PrompterView.qml:70) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

