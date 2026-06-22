# [THM-SYS] Complete theme deadlock — 50+ Material.theme: Dark hardcoded, theme toggle commented out

- **Status:** OPEN
- **Severity:** High
- **Category:** 
- **Location:** `14 QML files`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **Files:** 14 QML files
- **Severity:** High
- **Analysis:** ~50 `Material.theme: Material.Dark` hardcoded across all controls. Theme toggle button commented out in all main.qml variants ("This is correct, but it isn't working, likely because of Kirigami"). No theme change handler. Single `Material.theme: Material.Light` inconsistency on one Button (Prompter.qml:1272). Countdown, TimerClock, scrollbar all hardcoded dark. Separators, borders, selection colors all hardcoded. PrompterPage `Kirigami.Theme.inherit: false` blocks theme propagation.
- **Impact:** App permanently in dark mode regardless of system preference. Light-theme users see broken visuals.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 55 | 50+ hardcoded Material.theme:Dark means runtime theme toggle is effectively dead (multi-file) |
| gpt | ⚠️ PARTIAL | 58 | visual issue is plausible but depends on theme or device (src/kirigami_ui/main.qml:122) |
| deepseek | ✅ LEGIT | 90 | Material.theme: Material.Dark hardcoded across ~50 controls in 14+ QML files; theme toggle commented out; no light mode support |
| glm | ✅ LEGIT | 70 | 14 QML files have Material.theme: Dark hardcoded; theme toggle commented out |
| kimi | ✅ LEGIT | 85 | Dozens of `Material.theme: Material.Dark` are hardcoded across QML files; theme toggle is commented out |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — 50+ hardcoded Material.theme:Dark means runtime theme toggle is effectively dead (multi-fi |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

