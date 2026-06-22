# [VIS-N04] Countdown crosshair frame renders orphan lines when enabled=false

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `Countdown.qml:151-178`
- **Consensus:** 2/6 agents LEGIT · split

## Original report claim

- **File:** Countdown.qml:151-178
- **Severity:** Low
- **Analysis:** `Shape { id: frame }` (crosshair lines) has no visible binding. All other countdown elements guard with `visible: countdown.enabled`. When disabled but Prompter in Standby, only orphan crosshair lines render.
- **Impact:** Meaningless hairline crosshairs visible during standby with countdown disabled.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | crosshair frame orphan lines when enabled=false (Countdown.qml:151) |
| gpt | ⚠️ PARTIAL | 58 | observed Countdown crosshair frame renders orphan lines when enabled=false (src/prompter/Countdown.qml:151) |
| deepseek | ⚠️ PARTIAL | 45 | Shape lines lack visible binding to frame property; render independent of toggle (Countdown.qml:151-178) |
| glm | ⚠️ PARTIAL | 60 | Countdown.qml:151-178 crosshair frame renders orphan lines when enabled=false |
| kimi | ✅ LEGIT | 85 | Countdown.qml:151-178 frame Shape has no visible:countdown.enabled binding; if countdown becomes visible while enabled=false, hairline crosshairs still render |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — crosshair frame orphan lines when enabled=false (Countdown.qml:151) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

