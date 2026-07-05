# [664-IMP-NEW-03] main.cpp:38-39 redundant #include \<QtQml/qqml.h\> + #include \<QtQml\>

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `main.cpp:38-39`
- **Consensus:** 2/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** main.cpp:38-39
- **Severity:** Low
- **Analysis:** `<QtQml>` umbrella already pulls in `qqml.h`. Sub-include is redundant.
- **Impact:** Code clarity only.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ⚠️ PARTIAL | 40 | redundant QtQml/qqml.h + QtQml includes (main.cpp:38) |
| gpt-5.5-xhigh | ⚠️ PARTIAL | 58 | observed main.cpp:38-39 redundant #include \QtQml/qqml.h\ + #include \QtQml\ (src/main.cpp:38) |
| deepseek-v4-pro-max | ✅ LEGIT | 95 | <QtQml/qqml.h> at main.cpp:38 redundant with <QtQml> at line 39 — umbrella already includes it |
| glm-5.2-xhigh | ✅ LEGIT | 75 | main.cpp:38-39 redundant #include <QtQml/qqml.h> + #include <QtQml>; both not needed |
| kimi-k2.7-code | ❌ FALSE | 70 | main.cpp:38-39 duplicate include is redundant, not a functional bug. |
| opus-4.8-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — redundant QtQml/qqml.h + QtQml includes (main.cpp:38) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

