# [SAFE-01] +android/main.qml zero safe area insets

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `+android/main.qml`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** +android/main.qml
- **Severity:** Medium
- **Analysis:** Full-screen Android window lacks safe area margins. Content obscured by camera notch and gesture navigation pill on modern devices (Pixel, Galaxy S).
- **Impact:** UI elements hidden behind notch/pill on modern Android devices.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | +android no safe-area insets; notch handling (main.qml) |
| gpt | ⚠️ PARTIAL | 58 | observed +android/main.qml zero safe area insets (src/kirigami_ui/+android/main.qml:1) |
| deepseek | ✅ LEGIT | 80 | +android/main.qml full-screen — zero safe area margins for notch/gesture pill |
| glm | ✅ LEGIT | 80 | +android/main.qml no safe area insets for notch/status bar |
| kimi | ✅ LEGIT | 75 | +android/main.qml applies no safe-area margins; content can be hidden by notch or gesture bar. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — +android no safe-area insets; notch handling (main.qml) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

