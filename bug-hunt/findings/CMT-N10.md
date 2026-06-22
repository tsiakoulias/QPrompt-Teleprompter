# [CMT-N10] Obsolete Qt 5 qmlRegisterType calls as commented-out cruft

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `main.cpp:68-69,215-223`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** main.cpp:68-69,215-223
- **Severity:** Low
- **Analysis:** Multiple `// qmlRegisterType<...>(...)` and `// #include` from Qt 5 era. Malformed comment nesting at line 219 (`/**/` inside `//`).
- **Impact:** Misleads about current C++ registration mechanism (QML_ELEMENT).

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 35 | commented-out Qt5 qmlRegisterType cruft; cosmetic (main.cpp:68) |
| gpt | ⚠️ PARTIAL | 48 | comment problem observed, but defect impact is limited (src/main.cpp:68) |
| deepseek | ✅ LEGIT | 90 | Qt 5 qmlRegisterType calls commented out at main.cpp — cruft misleads about QML_ELEMENT registration |
| glm | ✅ LEGIT | 75 | main.cpp:68-69 215-223 obsolete Qt 5 qmlRegisterType calls as commented-out cruft |
| kimi | ✅ LEGIT | 90 | main.cpp:68-69,215-223 contain commented-out Qt 5 qmlRegisterType/QObject cruft; misleading with current QML_ELEMENT registration |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — commented-out Qt5 qmlRegisterType cruft; cosmetic (main.cpp:68) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

