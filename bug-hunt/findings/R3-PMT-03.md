# [R3-PMT-03] goToNextMarker fallback desynchronizes cursor from viewport

- **Status:** OPEN
- **Severity:** Medium
- **Category:** Logic
- **Location:** `src/prompter/Prompter.qml:658-659`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** src/prompter/Prompter.qml:658-659
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** Fallback scrolls viewport to document end but doesn't update editor.cursorPosition. Cursor stays where document.nextMarker() placed it (possibly stale).
- **Impact:** Editor cursor and viewport out of sync. Subsequent marker lookups use wrong position.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | goToNextMarker fallback desyncs cursor/viewport; domain (Prompter.qml:658) |
| gpt | ⚠️ PARTIAL | 58 | observed goToNextMarker fallback desynchronizes cursor from viewport (src/prompter/Prompter.qml:658) |
| deepseek | ✅ LEGIT | 85 | Prompter.qml:658-659 fallback scrolls viewport to document end but does NOT update editor.cursorPosition — cursor/viewport desynchronized |
| glm | ✅ LEGIT | 75 | Prompter.qml:658-659 goToNextMarker sets cursorPosition then reads cursorRectangle.y which may not have updated yet |
| kimi | ✅ LEGIT | 90 | goToNextMarker fallback jumps prompter.position to end without updating editor.cursorPosition at Prompter.qml:658-659 |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — goToNextMarker fallback desyncs cursor/viewport; domain (Prompter.qml:658) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

