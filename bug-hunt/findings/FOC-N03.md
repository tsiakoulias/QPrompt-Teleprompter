# [FOC-N03] Tab/Backtab asymmetry — Backtab silently unhandled

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `Prompter.qml:2170-2173`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** Prompter.qml:2170-2173
- **Severity:** Low
- **Analysis:** Keys.onPressed handles Qt.Key_Tab but not Qt.Key_Backtab. Users can Tab forward but cannot Shift+Tab backward to return.
- **Impact:** One-directional keyboard accessibility navigation.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | Tab/Backtab asymmetry; Backtab unhandled (Prompter.qml:2170) |
| gpt | ✅ LEGIT | 78 | Tab/Backtab asymmetry - Backtab silently unhandled (src/prompter/Prompter.qml:2170) |
| deepseek | ✅ LEGIT | 85 | Keys.onPressed handles Qt.Key_Tab but not Qt.Key_Backtab; Shift+Tab silently unhandled (Prompter.qml:2170-2173) |
| glm | ⚠️ PARTIAL | 60 | Prompter.qml:2170-2173 Tab handled but Backtab silently unhandled; minor asymmetry |
| kimi | ✅ LEGIT | 85 | Prompter.qml:2170-2173 handles Qt.Key_Tab but has no Qt.Key_Backtab case, breaking Shift+Tab navigation. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — Tab/Backtab asymmetry; Backtab unhandled (Prompter.qml:2170) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

