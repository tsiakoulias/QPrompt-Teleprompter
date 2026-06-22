# [R3-MAIN-02] Invalid locale string constructed for short language codes

- **Status:** OPEN
- **Severity:** High
- **Category:** Platform/Build
- **Location:** `src/main.cpp:141-143`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** src/main.cpp:141-143
- **Severity:** High
- **Category:** Platform/Build
- **Analysis:** language.toUtf8() + ".UTF-8" produces e.g., "es.UTF-8" — not a valid POSIX locale. setlocale() silently fails; C library uses "C" locale.
- **Impact:** Wrong date/number formatting, sorting, character classification throughout the app.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 55 | language+.UTF-8 invalid only for 2-letter codes (main.cpp:141) |
| gpt | ⚠️ PARTIAL | 58 | observed Invalid locale string constructed for short language codes (src/main.cpp:141) |
| deepseek | ✅ LEGIT | 90 | main.cpp:141 language.toUtf8()+'.UTF-8' for short codes like 'es' produces 'es.UTF-8' — not valid POSIX locale; setlocale silently fails |
| glm | ✅ LEGIT | 85 | main.cpp:141-143 for short language codes like 'en' QLocale name produces 'en' not 'en_US'; translator.load may fail |
| kimi | ✅ LEGIT | 75 | main.cpp:141 appends .UTF-8 to the user language string; short codes like en become invalid locale names (e.g. en.UTF-8). |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — language+.UTF-8 invalid only for 2-letter codes (main.cpp:141) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

