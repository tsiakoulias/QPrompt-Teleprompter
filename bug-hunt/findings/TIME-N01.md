# [TIME-N01] copyrightYear computed then discarded — stale "2020-2026" in About after 2026

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `main.cpp:176-179`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** main.cpp:176-179
- **Severity:** Low
- **Analysis:** `QDate::currentDate().year()` computed into `copyrightYear` but never interpolated into `copyrightStatement2` which hardcodes "2026". The `(currentYear <= 2020)` branch is dead code. Missing `#include <QDate>` (works only via transitive includes).
- **Impact:** About dialog shows stale copyright range starting 2027.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 60 | copyrightYear computed then discarded; hardcoded 2026 (main.cpp:176) |
| gpt | ✅ LEGIT | 78 | copyrightYear computed then discarded - stale "2020-2026" in About after 2026 (src/main.cpp:176) |
| deepseek | ✅ LEGIT | 85 | copyrightYear computed at line 177 but hardcoded '2020-2026' used at line 179 (main.cpp:176-179) |
| glm | ✅ LEGIT | 70 | main.cpp:176-179 copyrightYear computed then discarded; stale '2020-2026' in About after 2026 |
| kimi | ✅ LEGIT | 90 | main.cpp:177 computes currentYear but :179 hardcodes '2020-2026'; after 2026 the copyright string remains stale. |
| opus-ultra | ✅ LEGIT | 60 | copyrightYear computed then discarded; hardcoded 2026 (main.cpp:176) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

