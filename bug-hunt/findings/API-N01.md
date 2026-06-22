# [API-N01] setAlignment() missing null-cursor guard — crash risk with no document

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.cpp:557-558`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp:557-558
- **Severity:** Medium
- **Analysis:** Unlike all other format setters, setAlignment() creates a QTextCursor and calls mergeBlockFormat() without checking cursor.isNull(). Dereferences null QTextDocument if no document loaded.
- **Impact:** Crash if alignment changed before document loaded.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | setAlignment no null guard; null-cursor ops are Qt no-ops, crash unlikely (documenthandler.cpp:557) |
| gpt | ✅ LEGIT | 78 | setAlignment() missing null-cursor guard - crash risk with no document (src/documenthandler.cpp:557) |
| deepseek | ✅ LEGIT | 65 | setAlignment lacks null-cursor guard unlike alignment() getter (documenthandler.cpp:557-558) |
| glm | ✅ LEGIT | 75 | documenthandler.cpp:557-558 setAlignment() missing null-cursor guard; crash risk with no document |
| kimi | ✅ LEGIT | 80 | setAlignment() at documenthandler.cpp:553-559 calls mergeBlockFormat on textCursor without isNull() guard; crash risk if no document loaded. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — setAlignment no null guard; null-cursor ops are Qt no-ops |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

