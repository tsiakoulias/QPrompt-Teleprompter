# [RES-05] QTextStream left unflushed before QFile destruction

- **Status:** REJECTED
- **Severity:** Low
- **Category:** 
- **Location:** `src/spellchecker.cpp:390-397`
- **Consensus:** 0/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/spellchecker.cpp:390-397
- **Severity:** Low
- **Code:**
  ```cpp
  QTextStream out(&file);
  for (const QString &w : m_customWords)
      out << w << '\n';
  // QTextStream and QFile destructors handle flush/close
  ```
- **Analysis:** `QTextStream` is never explicitly flushed. While RAII (destructor ordering) makes this safe in normal operation, explicit `flush()` would be more robust. Compare with `documenthandler.cpp:1164-1166` which calls `file.flush()`.
- **Impact:** Low risk on abnormal termination; data-at-rest consistency depends on destructor ordering.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❌ FALSE | 80 | RAII flushes; report admits safe (spellchecker.cpp:390) |
| gpt | ❌ FALSE | 76 | QTextStream/QFile destruction flushes this path (src/spellchecker.cpp:390) |
| deepseek | ❌ FALSE | 75 | QTextStream+QFile RAII handles flush/close on destruction at spellchecker.cpp:390-397; Qt guarantees QFile dtor after stream dtor in stack order — benign |
| glm | ❌ FALSE | 80 | spellchecker.cpp:390-397 QTextStream is flushed on QFile destruction via RAII; explicit flush at :396 also present |
| kimi | ❌ FALSE | 70 | spellchecker.cpp:390-397 QTextStream destructor flushes buffered data before QFile destructor; RAII is safe. |
| opus-ultra | ❌ FALSE | 80 | RAII flushes; report admits safe (spellchecker.cpp:390) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

