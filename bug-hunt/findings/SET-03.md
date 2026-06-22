# [SET-03] QString "true" used as default for boolean QSettings value

- **Status:** REJECTED
- **Severity:** Low
- **Category:** 
- **Location:** `documenthandler.cpp:137`
- **Consensus:** 3/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** documenthandler.cpp:137
- **Severity:** Low
- **Analysis:** `settings.value("editor/autoReload", "true").toBool()` — default is QString "true" while stored value is bool. Relies on implicit QVariant cross-type conversion.
- **Impact:** Fragile — any code using `.toString()` would get type mismatch.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | string 'true' default for bool toBool() works correctly; cosmetic (documenthandler.cpp:137) |
| gpt | ✅ LEGIT | 78 | QString "true" used as default for boolean QSettings value (src/documenthandler.cpp:137) |
| deepseek | ✅ LEGIT | 85 | Default 'true' (QString) for bool QSettings at documenthandler.cpp:137 — fragile cross-type conversion |
| glm | ✅ LEGIT | 75 | documenthandler.cpp:137 QString 'true' used as default for boolean QSettings value instead of bool |
| kimi | ❌ FALSE | 75 | documenthandler.cpp:137 QVariant converts the default QString \true\" to bool correctly; no functional bug." |
| opus-ultra | ❌ FALSE | 72 | max: code correct / claim mischaracterized — string 'true' default for bool toBool() works correctly; cosmetic (documenthandler.cpp:137 |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

