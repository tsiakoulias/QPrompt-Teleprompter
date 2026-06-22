# [FINAL-20] Dangling pointer from temporary QByteArray in marker anchor parsing

- **Status:** REJECTED
- **Severity:** High
- **Category:** Type Safety
- **Location:** `src/documenthandler.cpp:1664`
- **Consensus:** 2/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** src/documenthandler.cpp:1664
- **Severity:** High
- **Category:** Type Safety
- **Analysis:** `(*constIterator).toUtf8().constData()` — stores pointer to temporary QByteArray buffer. Temporary destroyed at end of expression; pointer dangles.
- **Impact:** Memory corruption when parsing markers with non-ASCII anchor names.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❌ FALSE | 80 | temporary QByteArray alive during QString ctor; no dangling (documenthandler.cpp:1664) |
| gpt | ❌ FALSE | 76 | temporary QByteArray lives through the QString constructor call (src/documenthandler.cpp:1664) |
| deepseek | ❌ FALSE | 90 | documenthandler.cpp:1664 (*constIterator).toUtf8().constData() — temporary QByteArray lives until semicolon; constData() valid for QString construction |
| glm | ✅ LEGIT | 85 | documenthandler.cpp:1664 (*constIterator).toUtf8().constData() returns pointer to temporary QByteArray; dangling |
| kimi | ✅ LEGIT | 90 | documenthandler.cpp:1664 assigns QString from (*constIterator).toUtf8().constData(); temporary QByteArray destroyed, pointer dangles. |
| opus-ultra | ❌ FALSE | 80 | temporary QByteArray alive during QString ctor; no dangling (documenthandler.cpp:1664) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

