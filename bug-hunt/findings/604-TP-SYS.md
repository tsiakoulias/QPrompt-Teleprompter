# [604-TP-SYS] Systemic absence of ToolTip on ~60+ controls across entire application

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `Find.qml (8 buttons), EditorToolbar.qml (~28 buttons), PrompterView.qml (4 buttons), Prompter.qml (4 at-end buttons), MarkersDrawer (pin button), KeyInputButton (clear button), PrompterPage (~18 drawer actions)`
- **Consensus:** 2/6 agents LEGIT · split

## Original report claim

- **Files:** Find.qml (8 buttons), EditorToolbar.qml (~28 buttons), PrompterView.qml (4 buttons), Prompter.qml (4 at-end buttons), MarkersDrawer (pin button), KeyInputButton (clear button), PrompterPage (~18 drawer actions)
- **Severity:** Medium
- **Analysis:** Dozens of buttons use unicode/cryptic icons with zero ToolTip text. Only ~12 of ~30 context drawer actions have tooltips. Zero Accessible properties anywhere — app invisible to screen readers.
- **Impact:** Poor discoverability. Keyboard-only and assistive-technology users cannot identify controls.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ⚠️ PARTIAL | 40 | systemic absence of ToolTips; UX |
| gpt-5.5-xhigh | ⚠️ PARTIAL | 58 | missing tooltip is a UX gap, not a functional failure (src/prompter/Find.qml:1) |
| deepseek-v4-pro-max | ⚠️ PARTIAL | 70 | Systemic absence of ToolTip across ~60 controls is accurate observation but subjective; some buttons use text labels; not a code defect per se |
| glm-5.2-xhigh | ✅ LEGIT | 70 | ~60+ controls across entire application missing ToolTip; systemic absence |
| kimi-k2.7-code | ✅ LEGIT | 75 | Source files show many ToolButtons/Actions with no tooltip; verified in Find.qml, EditorToolbar.qml, PrompterView.qml, PrompterPage.qml. |
| opus-4.8-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — systemic absence of ToolTips; UX |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

