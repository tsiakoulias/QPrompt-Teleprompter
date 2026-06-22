# [FONT-METRIC-02] FontLoader status never checked — font substitution silently fails

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `Prompter.qml:995-998`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** Prompter.qml:995-998
- **Severity:** Medium
- **Analysis:** If bundled DejaVuSans.ttf missing/corrupt, .name is empty → font.family feeds empty string → Qt falls back to system default. No status check, no fallback, no error.
- **Impact:** Wrong font silently used; layout scroll timing and visual appearance shift unpredictably.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | FontLoader status never checked; substitution silent (Prompter.qml:995) |
| gpt | ⚠️ PARTIAL | 58 | observed FontLoader status never checked - font substitution silently fails (src/prompter/Prompter.qml:995) |
| deepseek | ✅ LEGIT | 85 | Prompter.qml:995-998: FontLoader source set but status never checked; corrupted/missing font silently substituted with no error |
| glm | ✅ LEGIT | 70 | Prompter.qml:995-998 FontLoader status never checked; font substitution silently fails |
| kimi | ✅ LEGIT | 90 | Prompter.qml:995-998 FontLoader has no status handling; font substitution failures are silent |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — FontLoader status never checked; substitution silent (Prompter.qml:995) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

