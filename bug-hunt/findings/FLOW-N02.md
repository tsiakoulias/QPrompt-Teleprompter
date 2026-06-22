# [FLOW-N02] increaseVelocity()/decreaseVelocity() skip velocity change when paused

- **Status:** NEEDS-INFO
- **Severity:** Medium
- **Category:** 
- **Location:** `Prompter.qml:494-497,510-513`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** Prompter.qml:494-497,510-513
- **Severity:** Medium
- **Analysis:** `if (this.__play) this.__i++` — __i modification gated on play. When paused, functions only resume at existing velocity + trigger animated jump to document end. Contrast with setVelocity() which always modifies __i.
- **Impact:** "Increase/Decrease Velocity" buttons do nothing to velocity when paused — behavioral inconsistency.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❔ UNSURE | 45 | increase/decreaseVelocity skip change when paused; domain (Prompter.qml:494) |
| gpt | ⚠️ PARTIAL | 58 | observed increaseVelocity()/decreaseVelocity() skip velocity change when paused (src/prompter/Prompter.qml:494) |
| deepseek | ✅ LEGIT | 90 | Prompter.qml:494-497/510-513: increaseVelocity/decreaseVelocity gate __i modification on this.__play; when paused __i never changes but __play=true & position updated — behavioral inconsistency |
| glm | ✅ LEGIT | 75 | Prompter.qml:494-497 510-513 increaseVelocity/decreaseVelocity skip velocity change when paused (__play false) |
| kimi | ✅ LEGIT | 85 | Prompter.qml:494-497,510-513 increase/decreaseVelocity only modify __i when __play is true, so paused adjustments do nothing to velocity. |
| opus-ultra | ❔ UNSURE | 45 | max: unverifiable statically (runtime/semantic) — increase/decreaseVelocity skip change when paused; domain (Prompter.qml:494) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

