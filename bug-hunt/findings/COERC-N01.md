# [COERC-N01] parseInt("") → NaN state bootstrap — first toggle() bricks state machine

- **Status:** NEEDS-INFO
- **Severity:** High
- **Category:** 
- **Location:** `Prompter.qml:448`
- **Consensus:** 3/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** Prompter.qml:448
- **Severity:** High
- **Analysis:** Flickable.state defaults to empty string "". toggle() reads `parseInt(state)` to compute next state. `parseInt("") = NaN`. `(NaN + 1) % 4 = NaN`. State set to NaN — every subsequent `parseInt(state) === Prompter.States.X` comparison fails silently (NaN ≠ integer). State machine permanently bricked from first toggle.
- **Impact:** If Flickable.state is ever empty when toggle() is called, the app enters unrecoverable undefined state.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❔ UNSURE | 45 | parseInt('') NaN only if initial state unset; depends on default state (Prompter.qml:448) |
| gpt | ✅ LEGIT | 84 | parseInt("") -> NaN state bootstrap - first toggle() bricks state machine (src/prompter/Prompter.qml:448) |
| deepseek | ❌ FALSE | 85 | Prompter.qml:3088 explicitly sets state: Prompter.States.Editing(=0); parseInt('0')=0 not NaN; state is never empty string |
| glm | ✅ LEGIT | 75 | Prompter.qml:448 parseInt(state) when state is non-numeric returns NaN; first toggle() bricks state machine |
| kimi | ✅ LEGIT | 90 | Prompter.qml:448 `parseInt(state)` on empty string yields NaN; `(NaN+1)%4` is NaN and state comparisons fail. |
| opus-ultra | ❔ UNSURE | 45 | max: unverifiable statically (runtime/semantic) — parseInt('') NaN only if initial state unset; depends on default state (Prompter.qml:448) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

