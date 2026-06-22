# [DRAG-N02] textDragArea has no cursorShape — no cursor feedback during text drag

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `Prompter.qml:1429-1431`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** Prompter.qml:1429-1431
- **Severity:** Low
- **Analysis:** Manual text drag shows blue drop line but cursor stays as IBeamCursor — no indication drag is in progress.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 55 | textDragArea no cursorShape; no drag cursor feedback (Prompter.qml:1429) |
| gpt | ⚠️ PARTIAL | 58 | observed textDragArea has no cursorShape - no cursor feedback during text drag (src/prompter/Prompter.qml:1429) |
| deepseek | ✅ LEGIT | 80 | textDragArea MouseArea lacks cursorShape at Prompter.qml:1429-1431; no visual cursor change during text drag |
| glm | ✅ LEGIT | 65 | Prompter.qml:1429-1431 textDragArea has no cursorShape; no cursor feedback during text drag |
| kimi | ✅ LEGIT | 70 | Prompter.qml:1429-1431 textDragArea has no cursorShape; no text-drag cursor feedback |
| opus-ultra | ✅ LEGIT | 55 | textDragArea no cursorShape; no drag cursor feedback (Prompter.qml:1429) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

