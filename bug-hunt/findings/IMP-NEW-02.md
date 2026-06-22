# [IMP-NEW-02] main.cpp:22 #include "qglobal.h" uses quotes + Qt5-era name

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `main.cpp:22`
- **Consensus:** 0/6 agents LEGIT · split

## Original report claim

- **File:** main.cpp:22
- **Severity:** Low
- **Analysis:** Double-quotes search local dir first; `qglobal.h` is pre-Qt6 header name. Qt 6 canonical: `<QtGlobal>`. Local file named `qglobal.h` would shadow system header.
- **Impact:** Fragile include — harmless currently.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | #include \qglobal.h\" quotes + Qt5-era name; works (main.cpp:22)" |
| gpt | ⚠️ PARTIAL | 58 | observed main.cpp:22 #include "qglobal.h" uses quotes + Qt5-era name (src/main.cpp:22) |
| deepseek | ⚠️ PARTIAL | 80 | #include 'qglobal.h' at main.cpp:22 — quotes + Qt5 name; Qt6 canonical is <QtGlobal> harmless currently |
| glm | ⚠️ PARTIAL | 60 | main.cpp:22 #include 'qglobal.h' uses quotes and Qt5-era name; works but non-idiomatic |
| kimi | ❌ FALSE | 80 | main.cpp:22 #include \qglobal.h\" works because Qt still provides the header; it is non-canonical but not broken." |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — #include \qglobal.h\" quotes + Qt5-era name; works (main.cpp:22)" |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

