# [DLG-N08] 3 save-completion passive notifications lack passiveNotifications guard

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `Prompter.qml:2294,2296,2474,2499`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** Prompter.qml:2294,2296,2474,2499
- **Severity:** Low
- **Analysis:** Save completion notifications fire even when user disabled notifications. Six other call sites in same file correctly guard with `if(root.passiveNotifications)`.
- **Impact:** Inconsistent notification behavior.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | save notifications lack passiveNotifications guard (Prompter.qml:2294) |
| gpt | ✅ LEGIT | 78 | 3 save-completion passive notifications lack passiveNotifications guard (src/prompter/Prompter.qml:2294) |
| deepseek | ✅ LEGIT | 85 | Save notifications at Prompter.qml:2294 2296 2474 2499 lack passiveNotifications guard |
| glm | ✅ LEGIT | 75 | Prompter.qml:2294+ 3 save-completion passive notifications lack passiveNotifications guard |
| kimi | ✅ LEGIT | 80 | Prompter.qml:2294/2296 save-completion notifications are not guarded by root.passiveNotifications unlike other call sites. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — save notifications lack passiveNotifications guard (Prompter.qml:2294) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

