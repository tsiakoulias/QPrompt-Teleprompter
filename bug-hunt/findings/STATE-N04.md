# [STATE-N04] loop animation cancel() state change overridden by toggle() due to QML batching

- **Status:** NEEDS-INFO
- **Severity:** Low
- **Category:** 
- **Location:** `Prompter.qml:900-907`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** Prompter.qml:900-907
- **Severity:** Low
- **Analysis:** SequentialAnimation's final ScriptAction calls `prompter.cancel()` (sets state=Editing) then `prompter.toggle()` (overwrites state). QML batches in same JS execution — only toggle()'s final state takes effect. cancel() state transition dead.
- **Impact:** Dead code — cancel() effects never run except side effect `cursorAutoHide.reset()` which gets immediately undone.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❔ UNSURE | 45 | loop cancel() vs toggle() QML batching; domain (Prompter.qml:900) |
| gpt | ✅ LEGIT | 78 | loop animation cancel() state change overridden by toggle() due to QML batching (src/prompter/Prompter.qml:900) |
| deepseek | ✅ LEGIT | 70 | cancel() then toggle() in same ScriptAction batch; QML batching may override cancel (Prompter.qml:900-907) |
| glm | ⚠️ PARTIAL | 55 | Prompter.qml:900-907 loop animation cancel() state change overridden by toggle() due to QML batching |
| kimi | ✅ LEGIT | 75 | Prompter.qml:900-907 ScriptAction calls cancel() then toggle() together, risking QML batching overriding the cancel state. |
| opus-ultra | ❔ UNSURE | 45 | max: unverifiable statically (runtime/semantic) — loop cancel() vs toggle() QML batching; domain (Prompter.qml:900) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

