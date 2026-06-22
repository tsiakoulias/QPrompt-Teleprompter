# [EDGE-05] Null pointer dereference: `textDocument()` unchecked in `search()`

- **Status:** OPEN
- **Severity:** Critical
- **Category:** 
- **Location:** `src/documenthandler.cpp:1546,1548,1550,1555,1557,1561,1563,1565,1569,1571`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/documenthandler.cpp:1546,1548,1550,1555,1557,1561,1563,1565,1569,1571
- **Severity:** Critical
- **Code:**
  ```cpp
  cursor = this->textDocument()->find(searchRegEx, this->selectionStart(), ...);
  ```
- **Analysis:** `textDocument()` returns `nullptr` when `m_document` is null. Called from `replaceAll()` which is QML-invokable. No null guard.
- **Impact:** Null pointer dereference crash when search/replace is invoked with no document loaded.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 90 | textDocument()->find unchecked (documenthandler.cpp:1546) |
| gpt | ✅ LEGIT | 88 | Null pointer dereference: textDocument() unchecked in search() (src/documenthandler.cpp:1546) |
| deepseek | ✅ LEGIT | 92 | this->textDocument()->find(...) at doc.cpp:1546-1571; textDocument() returns nullptr when m_document null; search() is QML-callable — crash confirmed |
| glm | ✅ LEGIT | 90 | documenthandler.cpp:1546+ textDocument() not checked for null before find() calls in regex search path |
| kimi | ✅ LEGIT | 95 | documenthandler.cpp:1546-1571 search() calls this->textDocument() without null guard. |
| opus-ultra | ✅ LEGIT | 90 | textDocument()->find unchecked (documenthandler.cpp:1546) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

