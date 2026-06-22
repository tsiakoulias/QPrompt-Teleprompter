# [LOG-05] DocumentHandler::search ignores `loop` parameter when `regEx` is true

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `src/documenthandler.cpp:1552-1567`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/documenthandler.cpp:1552-1567
- **Severity:** Medium
- **Code:**
  ```cpp
  // regex branch (line 1552):
  if (cursor.selectionStart() == -1 && cursor.selectionStart() == -1 && cursor.selectionEnd() == -1) {
      // wraps around unconditionally -- loop parameter NOT checked

  // non-regex branch (line 1567):
  if (loop && (cursor.selectionStart() == -1 && cursor.selectionStart() == -1 && cursor.selectionEnd() == -1)) {
      // respects the loop parameter
  ```
- **Analysis:** The `loop` parameter controls wrap-around behavior. When `regEx = true`, the check at line 1552 does not test `loop`, so it always wraps. Also, both branches redundantly check `cursor.selectionStart() == -1` twice instead of checking start AND end.
- **Impact:** `replaceAll()` passes `loop = false` to prevent wrapping, but regex searches still wrap, potentially causing infinite loops.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 100 | regex branch ignores loop; dup selectionStart check (documenthandler.cpp:1552) |
| gpt | ✅ LEGIT | 78 | regex search branch ignores the loop argument (src/documenthandler.cpp:1552) |
| deepseek | ✅ LEGIT | 88 | search() regex branch at doc.cpp:1552 lacks loop param check; non-regex branch at 1567 checks loop — confirmed asymmetry loop always wraps in regex mode |
| glm | ✅ LEGIT | 90 | documenthandler.cpp:1552-1557 regex search path wraps unconditionally without checking the loop parameter |
| kimi | ✅ LEGIT | 90 | documenthandler.cpp:1552 regex branch wraps unconditionally ignoring loop param; non-regex branch at :1567 checks loop. |
| opus-ultra | ✅ LEGIT | 100 | regex branch ignores loop; dup selectionStart check (documenthandler.cpp:1552) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

