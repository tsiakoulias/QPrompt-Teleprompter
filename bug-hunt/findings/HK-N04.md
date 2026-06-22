# [HK-N04] No auto-repeat guard in key-binding configuration Keys.onPressed

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `KeyInputButton.qml:103`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** KeyInputButton.qml:103
- **Severity:** Medium
- **Analysis:** Auto-repeat races with toggleButtonsOff() mitigation. Signal-chain latency can allow second event before checked clears.
- **Impact:** Double-assignment during key re-binding.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | no auto-repeat guard in key-binding Keys.onPressed (KeyInputButton.qml:103) |
| gpt | ⚠️ PARTIAL | 58 | observed No auto-repeat guard in key-binding configuration Keys.onPressed (src/kirigami_ui/KeyInputButton.qml:103) |
| deepseek | ✅ LEGIT | 85 | Keys.onPressed at KeyInputButton.qml:103 — no auto-repeat guard races with toggleButtonsOff |
| glm | ✅ LEGIT | 80 | KeyInputButton.qml:103 key-binding configuration Keys.onPressed has no auto-repeat guard |
| kimi | ✅ LEGIT | 90 | KeyInputButton.qml:103 Keys.onPressed lacks event.isAutoRepeat guard, allowing double-assignment while rebinding keys |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — no auto-repeat guard in key-binding Keys.onPressed (KeyInputButton.qml:103) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

