# [EDGE-01] QString::arg() called on string with no placeholder — program name silently dropped

- **Status:** OPEN
- **Severity:** High
- **Category:** 
- **Location:** `src/documenthandler.cpp:1086-1089`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/documenthandler.cpp:1086-1089
- **Severity:** High
- **Code:**
  ```cpp
  return tr("An error occurred while attempting to open file in a third party format..."
            "to make sure a corresponding import tool is properly configured.")
      .arg(program);
  ```
- **Analysis:** The tr() string has no `%1` placeholder, but `.arg(program)` is called. In Qt 6, `arg()` on a string with no placeholder silently does nothing. The program name intended for the error message is never included.
- **Impact:** Users troubleshooting import failures never see which program path was attempted. Error message is misleading.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 95 | arg() on string w/o %1 (documenthandler.cpp:1086) |
| gpt | ✅ LEGIT | 84 | QString::arg() called on string with no placeholder - program name silently dropped (src/documenthandler.cpp:1086) |
| deepseek | ✅ LEGIT | 95 | tr() string has no %1 at doc.cpp:1087-1089; arg(program) silently no-ops in Qt6; program name dropped from error message — confirmed |
| glm | ✅ LEGIT | 85 | documenthandler.cpp:1086-1089 tr(...).arg(program) but the tr string has no %1 placeholder; program name silently dropped |
| kimi | ✅ LEGIT | 90 | documenthandler.cpp:1086-1089 .arg(program) on tr() string lacking %1 placeholder; program name not shown. |
| opus-ultra | ✅ LEGIT | 95 | arg() on string w/o %1 (documenthandler.cpp:1086) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

