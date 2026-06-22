# [RAII-N01] QDrag object never deleteLater'd after exec() — leaks on rejected drags

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.cpp:1486-1489`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp:1486-1489
- **Severity:** Medium
- **Analysis:** `new QDrag(this)` followed by `exec()`. Qt docs: "QDrag object needs to be deleted after exec() returns." Code never calls `deleteLater()`. Rejected/cancelled drags accumulate as zombie children of DocumentHandler. Paired QMimeData also leaked.
- **Impact:** Memory leak on every drag-and-drop operation that is cancelled or rejected.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | QDrag parented to this; accumulates per drag rather than leaks outright (documenthandler.cpp:1486) |
| gpt | ✅ LEGIT | 78 | QDrag object never deleteLater'd after exec() - leaks on rejected drags (src/documenthandler.cpp:1486) |
| deepseek | ✅ LEGIT | 60 | QDrag new'd per drag operation with parent this; accumulates over session (documenthandler.cpp:1486-1489) |
| glm | ✅ LEGIT | 80 | documenthandler.cpp:1486-1489 QDrag never deleteLater'd after exec(); leaks on rejected drags. Actually QDrag(this) has parent so auto-deleted. |
| kimi | ✅ LEGIT | 85 | new QDrag at documenthandler.cpp:1486 is not deleteLater'd after exec() returns; object leaks on rejected drag operations. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — QDrag parented to this; accumulates per drag rather than leaks outright (documenthandler.c |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

