# [TMR-02] timer.updateTimer() runs before timer.startTimer() on Prompting entry

- **Status:** NEEDS-INFO
- **Severity:** Medium
- **Category:** 
- **Location:** `Prompter.qml:3093 vs :3113`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** Prompter.qml:3093 vs :3113
- **Severity:** Medium
- **Analysis:** onStateChanged fires before transitions. updateTimer() computes elapsedMilliseconds with stale startTime. Then startTimer() uses corrupted elapsed value.
- **Impact:** First 333ms tick shows bogus elapsed time (~tens of seconds phantom).

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❔ UNSURE | 45 | updateTimer before startTimer on Prompting entry; domain (Prompter.qml:3093) |
| gpt | ❔ UNSURE | 39 | runtime/platform behavior is not decidable from the cited snippet (src/prompter/Prompter.qml:3093) |
| deepseek | ✅ LEGIT | 80 | updateTimer runs before startTimer in Prompting transition; computes elapsed with stale startTime (Prompter.qml:3093 vs 3113) |
| glm | ✅ LEGIT | 80 | Prompter.qml:3093 vs :3113 timer.updateTimer() runs before timer.startTimer() on Prompting entry |
| kimi | ✅ LEGIT | 85 | Prompter.qml:3093 timer.updateTimer() runs in onStateChanged before the Transition at :3113 calls timer.startTimer(). |
| opus-ultra | ❔ UNSURE | 45 | max: unverifiable statically (runtime/semantic) — updateTimer before startTimer on Prompting entry; domain (Prompter.qml:3093) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

