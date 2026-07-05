# [444-STATE-N03] Countdown Running restarts dissolveIn unnecessarily — visual dim-to-bright flash

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `Countdown.qml:289`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** Countdown.qml:289
- **Severity:** Low
- **Analysis:** Entering Running sets `dissolveIn.running = true`. Exiting Ready reverts dissolveIn to default `running: false`. Running then restarts from 0→1 even though countdown already fully visible.
- **Impact:** Brief dim-to-bright flash when countdown begins.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ⚠️ PARTIAL | 50 | Running re-runs dissolveIn; visual flash (Countdown.qml:289) |
| gpt-5.5-xhigh | ✅ LEGIT | 78 | Countdown Running restarts dissolveIn unnecessarily - visual dim-to-bright flash (src/prompter/Countdown.qml:289) |
| deepseek-v4-pro-max | ✅ LEGIT | 65 | Running state always restarts dissolveIn when re-entered causing visual flash (Countdown.qml:289) |
| glm-5.2-xhigh | ⚠️ PARTIAL | 60 | Countdown.qml:289 Running restarts dissolveIn unnecessarily; visual dim-to-bright flash |
| kimi-k2.7-code | ✅ LEGIT | 80 | Countdown.qml:289 sets dissolveIn.running=true after Ready state already set it; causes a 1->0->1 opacity flicker. |
| opus-4.8-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — Running re-runs dissolveIn; visual flash (Countdown.qml:289) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

