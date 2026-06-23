# [409-NOTIFY-02] availableDictionariesChanged NOTIFY signal never emitted

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `documenthandler.h:137,318`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.h:137,318
- **Severity:** Low
- **Analysis:** Q_PROPERTY `availableDictionaries` declares NOTIFY. Signal declared but zero emits in entire codebase. Underlying `SpellChecker::availableDictionaries()` is a static disk-scan — results can't change at runtime — so signal is semantically dead.
- **Impact:** No current impact. Future dynamic dictionary loading would fail to notify QML.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 55 | availableDictionariesChanged NOTIFY never emitted (documenthandler.h:137) |
| gpt | ✅ LEGIT | 78 | availableDictionariesChanged NOTIFY signal never emitted (src/documenthandler.h:137) |
| deepseek | ⚠️ PARTIAL | 85 | availableDictionariesChanged at documenthandler.h:137 never emitted; but method is static disk-scan can't change |
| glm | ✅ LEGIT | 80 | documenthandler.h:137 318 availableDictionariesChanged signal never emitted |
| kimi | ✅ LEGIT | 85 | documenthandler.h:137 declares availableDictionariesChanged but no code emits it; list is static. |
| opus-ultra | ✅ LEGIT | 55 | availableDictionariesChanged NOTIFY never emitted (documenthandler.h:137) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

