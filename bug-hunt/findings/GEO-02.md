# [GEO-02] main.qml persists x/y/width/height with zero validation

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `main.qml:85-91, +windows/main.qml`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** main.qml:85-91, +windows/main.qml
- **Severity:** Medium
- **Analysis:** Settings save/restore window geometry without screen-bounds validation. Remove external monitor → restart places window off-screen. No recovery mechanism.
- **Impact:** Unreachable window requiring manual settings reset.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | persists x/y/w/h with no on-restore validation; can restore off-screen (main.qml:85) |
| gpt | ⚠️ PARTIAL | 58 | observed main.qml persists x/y/width/height with zero validation (src/kirigami_ui/main.qml:85) |
| deepseek | ✅ LEGIT | 90 | Settings alias x/y/width/height at main.qml:87-90 — no screen bounds validation on restore |
| glm | ✅ LEGIT | 80 | main.qml:85-91 persists x/y/width/height with zero validation; could restore off-screen |
| kimi | ✅ LEGIT | 85 | main.qml:85-91 persists window geometry without clamping to available screen geometry; can place window off-screen. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — persists x/y/w/h with no on-restore validation; can restore off-screen (main.qml:85) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

