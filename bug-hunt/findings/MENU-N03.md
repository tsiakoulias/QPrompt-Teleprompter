# [MENU-N03] Text alignment menu RTL swap: labels swap but actions don't

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `EditorToolbar.qml:362-374`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** EditorToolbar.qml:362-374
- **Severity:** Medium
- **Analysis:** `text` and `enabled` bindings swap for RTL, but `onTriggered` unconditionally sets AlignLeft/AlignRight. In RTL, clicking "Right" sets AlignLeft. Global Format menu correctly swaps both text and action.
- **Impact:** Alignment menu produces opposite of label in RTL mode.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 55 | RTL alignment menu: labels swap but actions don't (EditorToolbar.qml:362) |
| gpt | ⚠️ PARTIAL | 58 | observed Text alignment menu RTL swap: labels swap but actions don't (src/kirigami_ui/EditorToolbar.qml:362) |
| deepseek | ✅ LEGIT | 95 | EditorToolbar.qml:362-374: text labels swap for RTL (Left<->Right) but onTriggered actions hardcoded AlignLeft/AlignRight unconditionally; RTL clicking Right sets AlignLeft |
| glm | ✅ LEGIT | 75 | EditorToolbar.qml:362-374 text alignment menu RTL swap: labels swap but actions don't |
| kimi | ✅ LEGIT | 85 | EditorToolbar.qml:362-374 RTL swaps menu labels but onTriggered always sets AlignLeft/AlignRight regardless of layout direction. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — RTL alignment menu: labels swap but actions don't (EditorToolbar.qml:362) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

