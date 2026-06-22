# [SAFE-02] ReadRegionOverlay screenMiddle ignores notch/status bar height

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `ReadRegionOverlay.qml:132-134`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** ReadRegionOverlay.qml:132-134
- **Severity:** Medium
- **Analysis:** screenMiddle calculation uses raw `screen.height` without subtracting status bar/notch height. On notched devices, reading region "middle" is physically offset downward.
- **Impact:** Read region misaligned on iPhones and notched Android devices.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | screenMiddle ignores notch/status bar (ReadRegionOverlay.qml:132) |
| gpt | ⚠️ PARTIAL | 58 | observed ReadRegionOverlay screenMiddle ignores notch/status bar height (src/prompter/ReadRegionOverlay.qml:132) |
| deepseek | ✅ LEGIT | 80 | screenMiddle at ReadRegionOverlay.qml:132 uses raw screen.height — ignores notch/status bar |
| glm | ✅ LEGIT | 75 | ReadRegionOverlay.qml:132-134 screenMiddle ignores notch/status bar height |
| kimi | ✅ LEGIT | 75 | ReadRegionOverlay.qml:132-134 computes screenMiddle from raw screen.height without accounting for status-bar/notch offset. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — screenMiddle ignores notch/status bar (ReadRegionOverlay.qml:132) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

