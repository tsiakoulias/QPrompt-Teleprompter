# [ARC-03] OBS WebSocket v5 protocol in QML — opcode dispatch, auth, subscription

- **Status:** OPEN
- **Severity:** 
- **Category:** 
- **Location:** `Prompter.qml:366-388`
- **Consensus:** 1/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** Prompter.qml:366-388
- **Analysis:** Complete WebSocket handshake JSON parsed and opcode-dispatched in QML. C++ provides only raw authStr(). Protocol changes require QML edits.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 35 | OBS WS protocol in QML; architectural (Prompter.qml:366) |
| gpt | ⚠️ PARTIAL | 48 | maintainability issue observed, but no direct runtime bug shown (src/prompter/Prompter.qml:366) |
| deepseek | ❌ FALSE | 50 | architectural observation; WebSocket protocol in QML is a valid Qt design pattern |
| glm | ⚠️ PARTIAL | 55 | Prompter.qml:366-388 OBS WebSocket v5 protocol in QML; architectural concern |
| kimi | ✅ LEGIT | 60 | Prompter.qml:366-388 implements OBS WebSocket v5 handshake, opcode dispatch and authentication in QML. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — OBS WS protocol in QML; architectural (Prompter.qml:366) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

