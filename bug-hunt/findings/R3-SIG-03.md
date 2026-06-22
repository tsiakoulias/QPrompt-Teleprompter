# [R3-SIG-03] IosSaveDialog accepted/rejected signals declared but never emitted

- **Status:** REJECTED
- **Severity:** Medium
- **Category:** Logic
- **Location:** `src/iossavedialog.h:44-45, iossavedialog.cpp:44-47`
- **Consensus:** 2/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** src/iossavedialog.h:44-45, iossavedialog.cpp:44-47
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** Both signals declared, saveDocument() has empty body with no emits. Zero emits anywhere.
- **Impact:** On iOS, QML waiting for accepted()/rejected() hangs indefinitely. Save-as flow broken.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❌ FALSE | 90 | accepted/rejected emitted in iossavedialog.mm:43,51 |
| gpt | ❌ FALSE | 90 | iOS .mm emits accepted and rejected (src/iossavedialog.h:44) |
| deepseek | ✅ LEGIT | 75 | iossavedialog.cpp:44-47 saveDocument no-op with zero emits of accepted()/rejected() signals — iOS save-as flow broken |
| glm | ✅ LEGIT | 85 | iossavedialog.h:44-45 accepted/rejected signals declared but never emitted in non-iOS iossavedialog.cpp |
| kimi | ❌ FALSE | 85 | accepted/rejected signals are emitted in iOS implementation at iossavedialog.mm:42-51; not dead |
| opus-ultra | ❌ FALSE | 90 | accepted/rejected emitted in iossavedialog.mm:43 |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

