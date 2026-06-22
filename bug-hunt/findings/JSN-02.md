# [JSN-02] ws.sendTextMessage() called without checking WebSocket status

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `Prompter.qml:383,413`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** Prompter.qml:383,413
- **Severity:** Medium
- **Analysis:** No check for ws.status === WebSocket.Open before sending. Non-Open socket silently discards messages.
- **Impact:** OBS commands silently lost if connection dropped.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | sendTextMessage without checking ws.status (Prompter.qml:383) |
| gpt | ✅ LEGIT | 78 | ws.sendTextMessage() called without checking WebSocket status (src/prompter/Prompter.qml:383) |
| deepseek | ✅ LEGIT | 90 | ws.sendTextMessage() at Prompter.qml:383 413 without ws.status===WebSocket.Open guard |
| glm | ✅ LEGIT | 80 | Prompter.qml:383 413 ws.sendTextMessage() called without checking WebSocket active status |
| kimi | ✅ LEGIT | 85 | Prompter.qml:383 and :413 call ws.sendTextMessage without verifying ws.status === WebSocket.Open. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — sendTextMessage without checking ws.status (Prompter.qml:383) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

