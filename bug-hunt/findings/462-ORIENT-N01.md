# [462-ORIENT-N01] TimerClock binary width>height orientation creates sharp 2x font jump at 1:1

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `TimerClock.qml:127`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** TimerClock.qml:127
- **Severity:** Low
- **Analysis:** `root.width/root.height>1 ? 2 : 1` divides font by 2 when width > height. At near-square window (800x798→800x802), timer font size abruptly doubles/halves at the 1:1 boundary. Smooth ratio-based formula would avoid discontinuity.
- **Impact:** Timer text doubles/halves in size when window crosses near-square aspect ratio.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ⚠️ PARTIAL | 45 | binary width>height -> 2x font jump at 1:1 (TimerClock.qml:127) |
| gpt-5.5-xhigh | ⚠️ PARTIAL | 58 | observed TimerClock binary widthheight orientation creates sharp 2x font jump at 1:1 (src/prompter/TimerClock.qml:127) |
| deepseek-v4-pro-max | ✅ LEGIT | 60 | binary width>height check creates 2x font size jump at exact square 1:1 aspect (TimerClock.qml:127) |
| glm-5.2-xhigh | ⚠️ PARTIAL | 55 | TimerClock.qml:127 binary width>height orientation creates sharp 2x font jump at 1:1 |
| kimi-k2.7-code | ✅ LEGIT | 70 | TimerClock.qml:127 uses binary width/height>1 ratio, causing abrupt 2x font jump when window crosses near-square aspect. |
| opus-4.8-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — binary width>height -> 2x font jump at 1:1 (TimerClock.qml:127) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

