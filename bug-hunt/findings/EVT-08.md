# [EVT-08] Two additional checkable ToolButton binding breakage instances

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `EditorToolbar.qml:913-918,1541-1556`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** EditorToolbar.qml:913-918,1541-1556
- **Severity:** Medium
- **Analysis:** opacity toggle and overlay bars toggle not in R2-EDT-03 list but suffer same binding-breakage pattern.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 60 | two more checkable ToolButton binding-break instances (R2-EDT-03 family) (EditorToolbar.qml:913) |
| gpt | ✅ LEGIT | 78 | Two additional checkable ToolButton binding breakage instances (src/kirigami_ui/EditorToolbar.qml:913) |
| deepseek | ✅ LEGIT | 88 | checkable ToolButton checked binding broken on click; showOpacityOptions+overlayBar desync (EditorToolbar.qml:913-918 1541-1556) |
| glm | ✅ LEGIT | 80 | EditorToolbar.qml:913-918 1541-1556 additional checkable ToolButton binding breakage |
| kimi | ✅ LEGIT | 85 | EditorToolbar.qml:1541-1556 ToolButton binds checked to an expression and mutates external state in onToggled, breaking the checked binding. |
| opus-ultra | ✅ LEGIT | 60 | two more checkable ToolButton binding-break instances (R2-EDT-03 family) (EditorToolbar.qml:913) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

