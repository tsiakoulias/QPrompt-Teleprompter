# [TRL-N03] About-dialog credit roles not translatable

- **Status:** OPEN
- **Severity:** Medium
- **Category:** I18N
- **Location:** `src/main.cpp:194,202,205-206`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** src/main.cpp:194,202,205-206
- **Severity:** Medium
- **Category:** I18N
- **Analysis:** "Author", "Software Tester", credit descriptions use QLatin1String instead of tr().
- **Impact:** Credit roles always English in About dialog.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | About credit roles not translatable (main.cpp:194) |
| gpt | ✅ LEGIT | 78 | About-dialog credit roles not translatable (src/main.cpp:194) |
| deepseek | ✅ LEGIT | 90 | credit roles use QLatin1String not tr(); About dialog always English (main.cpp:194 202 205-206) |
| glm | ✅ LEGIT | 80 | main.cpp:194 202 205-206 About dialog credit roles ('Author' 'Software Tester') not wrapped in tr() |
| kimi | ✅ LEGIT | 85 | main.cpp:194/202/205-206 use QStringLiteral for About-dialog credit roles/descriptions, not tr(). |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — About credit roles not translatable (main.cpp:194) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

