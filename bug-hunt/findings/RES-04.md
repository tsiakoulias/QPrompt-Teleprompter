# [RES-04] IosSaveDialog::s_instance same singleton dangling pattern

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `src/iossavedialog.cpp:24,29`
- **Consensus:** 2/6 agents LEGIT · split

## Original report claim

- **File:** src/iossavedialog.cpp:24,29
- **Severity:** Low
- **Code:** Identical pattern to RES-03.
- **Impact:** Same use-after-free risk as ShakeDetector.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 65 | same singleton pattern (iossavedialog.cpp:24) |
| gpt | ⚠️ PARTIAL | 58 | observed IosSaveDialog::s_instance same singleton dangling pattern (src/iossavedialog.cpp:24) |
| deepseek | ✅ LEGIT | 85 | Identical s_instance dangling pattern at iossavedialog.cpp:29; never reset to nullptr; use-after-free risk on singleton destruction |
| glm | ⚠️ PARTIAL | 60 | iossavedialog.cpp:24 same singleton pattern as RES-03; dangling pointer on destruction but benign for QML singleton |
| kimi | ✅ LEGIT | 80 | iossavedialog.cpp:24,29 sets s_instance in ctor but no dtor resets it; same dangling pattern. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — same singleton pattern (iossavedialog.cpp:24) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

