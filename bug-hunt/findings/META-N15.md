# [META-N15] No StartupWMClass in desktop file — duplicate dock entries, missing icon

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `com.cuperino.qprompt.desktop`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** com.cuperino.qprompt.desktop
- **Severity:** Medium
- **Impact:** App appears as separate generic entry in docks/taskbars on Linux.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | no StartupWMClass in desktop file |
| gpt | ⚠️ PARTIAL | 58 | observed No StartupWMClass in desktop file - duplicate dock entries, missing icon (com.cuperino.qprompt.desktop:1) |
| deepseek | ✅ LEGIT | 90 | com.cuperino.qprompt.desktop (both copies): no StartupWMClass entry; causes duplicate dock entries and missing icon on Linux |
| glm | ✅ LEGIT | 70 | com.cuperino.qprompt.desktop no StartupWMClass; duplicate dock entries missing icon |
| kimi | ✅ LEGIT | 80 | com.cuperino.qprompt.desktop has no StartupWMClass; duplicate dock entries / missing icon can occur |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — no StartupWMClass in desktop file |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

