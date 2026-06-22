# [FINAL-10] Two animations target same `position` property — conflict

- **Status:** OPEN
- **Severity:** High
- **Category:** QML/UI
- **Location:** `src/prompter/Prompter.qml:839,909`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** src/prompter/Prompter.qml:839,909
- **Severity:** High
- **Category:** QML/UI
- **Analysis:** `Behavior on position` and `NumberAnimation on position` both target `prompter.position`. On reset, both fire simultaneously with different durations.
- **Impact:** Animation jitter/jump on rewind-to-start; one animation overrides the other mid-flight.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 55 | Behavior + NumberAnimation both on position (Prompter.qml:839,909) |
| gpt | ⚠️ PARTIAL | 58 | observed Two animations target same position property - conflict (src/prompter/Prompter.qml:839) |
| deepseek | ✅ LEGIT | 90 | Prompter.qml:839 Behavior on position AND line 909 NumberAnimation on position both target prompter.position — conflicting animations |
| glm | ✅ LEGIT | 80 | Prompter.qml:839 909 Behavior on position and NumberAnimation on position both target position property |
| kimi | ✅ LEGIT | 90 | Prompter.qml:839 Behavior on position and line 909 NumberAnimation on position both target prompter.position, causing conflicting animations. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — Behavior + NumberAnimation both on position (Prompter.qml:839 |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

