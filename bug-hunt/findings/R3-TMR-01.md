# [R3-TMR-01] TimerClock ETA uses __iDefault instead of actual __i during reverse scroll

- **Status:** NEEDS-INFO
- **Severity:** Medium
- **Category:** Logic
- **Location:** `src/prompter/TimerClock.qml:66`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** src/prompter/TimerClock.qml:66
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** Fallback uses Math.pow(Math.abs(__iDefault), curvature) instead of __i. __iDefault frozen at session-start; if user changes velocity mid-session, ETA uses wrong speed.
- **Impact:** ETA displays incorrect remaining time by factor of (actualSpeed/defaultSpeed)^curvature.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❔ UNSURE | 45 | __iDefault vs __i in ETA fallback; domain call (TimerClock.qml:66) |
| gpt | ❔ UNSURE | 39 | runtime/platform behavior is not decidable from the cited snippet (src/prompter/TimerClock.qml:66) |
| deepseek | ✅ LEGIT | 80 | TimerClock.qml:66 ETA fallback uses prompter.__iDefault(static default) instead of actual __i — wrong ETA after mid-session velocity change |
| glm | ✅ LEGIT | 85 | TimerClock.qml:66 ETA uses __iDefault instead of actual __i during reverse scroll; wrong ETA when reversed |
| kimi | ✅ LEGIT | 95 | ETA fallback uses prompter.__iDefault instead of actual __i for reverse scroll at TimerClock.qml:66 |
| opus-ultra | ❔ UNSURE | 45 | max: unverifiable statically (runtime/semantic) — __iDefault vs __i in ETA fallback; domain call (TimerClock.qml:66) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

