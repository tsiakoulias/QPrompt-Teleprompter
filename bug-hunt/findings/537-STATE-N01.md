# [537-STATE-N01] Shadowed Prompting→Editing transition — velocity default never saved

- **Status:** NEEDS-INFO
- **Severity:** High
- **Category:** 
- **Location:** `Prompter.qml:3119-3137`
- **Consensus:** 2/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** Prompter.qml:3119-3137
- **Severity:** High
- **Analysis:** Two transitions target `to: Editing`. First (line 3119) matches and runs only `timer.stopTimer()`. Second (line 3127, guarded by `from: Prompting`) saves `__iDefault = prompter.__i` and calls `cursorAutoHide.reset()` — but QML selects first matching transition. Velocity-save code is dead.
- **Impact:** User's last prompting velocity never saved as new default. __iDefault stays at initial value forever.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ❔ UNSURE | 45 | shadowed Prompting->Editing transition claim; needs state-machine trace (Prompter.qml:3119) |
| gpt-5.5-xhigh | ✅ LEGIT | 84 | Shadowed Prompting->Editing transition - velocity default never saved (src/prompter/Prompter.qml:3119) |
| deepseek-v4-pro-max | ⚠️ PARTIAL | 50 | specific Prompting->Editing transition(line 3129) takes priority over general(line 3119) per QML rules (Prompter.qml:3119-3137) |
| glm-5.2-xhigh | ✅ LEGIT | 80 | Prompter.qml:3119-3137 Shadowed Prompting→Editing transition; velocity default never saved |
| kimi-k2.7-code | ❌ FALSE | 70 | Transition from Prompting to Editing at Prompter.qml:3127-3137 sets __iDefault when __i>0; generic to-Editing transition is not shadowed. |
| opus-4.8-ultra | ❔ UNSURE | 45 | max: unverifiable statically (runtime/semantic) — shadowed Prompting->Editing transition claim; needs state-machine trace (Prompter.qml:3119 |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

