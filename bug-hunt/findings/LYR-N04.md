# [LYR-N04] ESC handler uses activeFocus in base but focus in platform variants — inconsistent

- **Status:** OPEN
- **Severity:** Medium
- **Category:** Logic
- **Location:** `src/kirigami_ui/main.qml:512 vs +windows:483 vs +android:422`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** src/kirigami_ui/main.qml:512 vs +windows:483 vs +android:422
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** Base checks `prompter.activeFocus`, platform variants check `prompter.focus`. If prompter is FocusScope delegating to child, activeFocus=false while focus=true. Platform divergence.
- **Impact:** Linux/macOS ESC may fail to cancel prompting; Windows/Android work correctly.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | ESC uses activeFocus in base vs focus in variants; inconsistent (main.qml:512) |
| gpt | ✅ LEGIT | 78 | ESC handler uses activeFocus in base but focus in platform variants - inconsistent (src/kirigami_ui/main.qml:512) |
| deepseek | ✅ LEGIT | 85 | base uses prompter.activeFocus(512) windows/android use .focus(483/422); FocusScope activeFocus vs focus divergence (main.qml:512 +windows:483 +android:422) |
| glm | ✅ LEGIT | 80 | main.qml:512 uses activeFocus; +windows:483 and +android:422 use .focus; inconsistent focus checking |
| kimi | ✅ LEGIT | 90 | main.qml:512 checks prompter.activeFocus, but +windows/main.qml:483 and +android/main.qml:422 check prompter.focus only. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — ESC uses activeFocus in base vs focus in variants; inconsistent (main.qml:512) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

