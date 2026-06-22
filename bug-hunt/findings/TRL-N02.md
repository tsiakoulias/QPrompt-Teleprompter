# [TRL-N02] Application --help description not translatable

- **Status:** OPEN
- **Severity:** Medium
- **Category:** I18N
- **Location:** `src/main.cpp:154-155`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/main.cpp:154-155
- **Severity:** Medium
- **Category:** I18N
- **Analysis:** setApplicationDescription uses QLatin1String instead of tr(). User-visible in --help output.
- **Impact:** App description never translated. Non-English users see English in --help.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 50 | --help description not wrapped in tr() (main.cpp:154) |
| gpt | ✅ LEGIT | 78 | Application --help description not translatable (src/main.cpp:154) |
| deepseek | ✅ LEGIT | 90 | QLatin1String not tr() in setApplicationDescription; --help always English (main.cpp:154-155) |
| glm | ✅ LEGIT | 80 | main.cpp:154-155 application description passed to setApplicationDescription is not wrapped in tr() |
| kimi | ✅ LEGIT | 90 | main.cpp:154-155 passes QLatin1String to setApplicationDescription, not tr(), so --help text is untranslatable. |
| opus-ultra | ✅ LEGIT | 50 | --help description not wrapped in tr() (main.cpp:154) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

