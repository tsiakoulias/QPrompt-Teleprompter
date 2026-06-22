# [ANM-N02] Standby→Ready countdown opacity flash — PropertyChanges opacity:1 conflicts with dissolveIn

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `Countdown.qml:265-276`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** Countdown.qml:265-276
- **Severity:** Medium
- **Analysis:** Ready state simultaneously sets opacity:1 (PropertyChanges) AND starts dissolveIn (from:0 to:1). QML applies PropertyChanges first (opacity→1), then animation starts (opacity→0→1). Visible 1→0→1 flash.
- **Impact:** Visible flash when entering countdown-ready screen.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | Standby->Ready opacity PropertyChanges flash (Countdown.qml:265) |
| gpt | ⚠️ PARTIAL | 58 | observed Standby->Ready countdown opacity flash - PropertyChanges opacity:1 conflicts with dissolveIn (src/prompter/Countdown.qml:265) |
| deepseek | ✅ LEGIT | 90 | Countdown.qml:265-276: Ready state sets opacity:1 AND starts dissolveIn(0->1); PropertyChanges applied first causes visible 1->0->1 flash |
| glm | ✅ LEGIT | 70 | Countdown.qml:265-276 Standby→Ready countdown opacity flash; PropertyChanges opacity:1 conflicts with dissolveIn |
| kimi | ✅ LEGIT | 85 | Countdown.qml:268 sets opacity:1 while dissolveIn animates opacity from 0 to 1, causing a flash |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — Standby->Ready opacity PropertyChanges flash (Countdown.qml:265) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

