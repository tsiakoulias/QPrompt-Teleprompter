# [MA-N02] textDragArea missing cursorShape — ArrowCursor over IBeamCursor on editor

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `Prompter.qml:1429-1431`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** Prompter.qml:1429-1431
- **Severity:** Low
- **Analysis:** Topmost MouseArea over editor TextArea defaults to ArrowCursor. MouseArea below it correctly sets IBeamCursor but is concealed.
- **Impact:** Arrow cursor over all editor text instead of I-beam.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 55 | textDragArea missing cursorShape -> arrow over editor (Prompter.qml:1429) |
| gpt | ✅ LEGIT | 78 | textDragArea missing cursorShape - ArrowCursor over IBeamCursor on editor (src/prompter/Prompter.qml:1429) |
| deepseek | ✅ LEGIT | 85 | textDragArea at Prompter.qml:1429 missing cursorShape — defaults to ArrowCursor over editor TextArea |
| glm | ✅ LEGIT | 75 | Prompter.qml:1429-1431 textDragArea missing cursorShape; ArrowCursor over IBeamCursor |
| kimi | ✅ LEGIT | 85 | Prompter.qml:1429 textDragArea covers the editor but sets no cursorShape, so the editor's I-beam cursor is hidden. |
| opus-ultra | ✅ LEGIT | 55 | textDragArea missing cursorShape -> arrow over editor (Prompter.qml:1429) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

