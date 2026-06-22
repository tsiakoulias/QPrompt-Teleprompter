# [TXT-N04] goToNextMarker() temporarily sets cursorPosition=-1 — corrupts cursor state

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `Prompter.qml:656-659`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** Prompter.qml:656-659
- **Severity:** Medium
- **Analysis:** When no markers exist, nextMarker() returns Marker(-1) with position=-1. editor.cursorPosition set to -1 fires onChange signals; cursorRectangle.y read from invalid state before guard corrects position. Qt may assert-fail in debug.
- **Impact:** Visual jitter/flash on "next marker" with empty markers list. Debug assertion failures.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | goToNextMarker temporarily sets cursorPosition=-1 (Prompter.qml:656) |
| gpt | ⚠️ PARTIAL | 58 | observed goToNextMarker() temporarily sets cursorPosition=-1 - corrupts cursor state (src/prompter/Prompter.qml:656) |
| deepseek | ✅ LEGIT | 85 | Prompter.qml:656-659: editor.cursorPosition set to nextMarker().position which is -1 when no markers exist; cursorPosition=-1 fires onChange signals before guard corrects |
| glm | ✅ LEGIT | 75 | Prompter.qml:656-659 goToNextMarker temporarily sets cursorPosition=-1; corrupts cursor state |
| kimi | ✅ LEGIT | 80 | Prompter.qml:656-659 goToNextMarker sets editor.cursorPosition from nextMarker(-1) when no markers exist, corrupting cursor before fallback. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — goToNextMarker temporarily sets cursorPosition=-1 (Prompter.qml:656) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

