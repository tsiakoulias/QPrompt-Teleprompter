# [R3-MAIN-04] Stack-allocated QTranslator outlives QApplication on shutdown

- **Status:** REJECTED
- **Severity:** Low
- **Category:** Memory Management
- **Location:** `src/main.cpp:133,107/109,138/149`
- **Consensus:** 0/6 agents LEGIT · split

## Original report claim

- **File:** src/main.cpp:133,107/109,138/149
- **Severity:** Low
- **Category:** Memory Management
- **Analysis:** QTranslator translator (line 133) declared after app (lines 107/109), destroyed before app. app.installTranslator(&translator) stores raw pointer → dangling during app destructor. Violates documented contract.
- **Impact:** Use-after-free during QApplication teardown (plugin cleanup). Low probability, high severity if triggered.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❌ FALSE | 85 | translator-after-app is standard Qt idiom |
| gpt | ❌ FALSE | 76 | translator lifetime follows normal stack order after QApplication (src/main.cpp:133) |
| deepseek | ⚠️ PARTIAL | 60 | main.cpp:133 QTranslator declared after app(line 107/109) destroyed before app — violates installTranslator contract but Qt gracefully handles during teardown |
| glm | ⚠️ PARTIAL | 60 | main.cpp:133 QTranslator on stack outlives QApplication only during shutdown; benign in practice |
| kimi | ❌ FALSE | 65 | main.cpp:133 QTranslator is declared after QApplication, so it is destroyed before app on shutdown; no outliving occurs. |
| opus-ultra | ❌ FALSE | 85 | translator-after-app is standard Qt idiom |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

