# [EDGE-11] m_reply dereference without null check in loadFromNetworkFinihed()

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `src/documenthandler.cpp:890`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** src/documenthandler.cpp:890
- **Severity:** Medium
- **Code:**
  ```cpp
  auto document = m_reply->readAll();  // m_reply not checked
  ```
- **Analysis:** `m_reply` is not initialized in the constructor. While practically set before the signal fires, the signal carries the reply pointer as its argument — should use that directly.
- **Impact:** Null dereference if network state machine reaches unexpected state.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 60 | m_reply->readAll no null check; fires after get() (documenthandler.cpp:890) |
| gpt | ⚠️ PARTIAL | 58 | observed m_reply dereference without null check in loadFromNetworkFinihed() (src/documenthandler.cpp:890) |
| deepseek | ✅ LEGIT | 85 | m_reply->readAll() at doc.cpp:890 w/o null check; m_reply uninitialized in constructor; signal-carried reply pointer ignored — null deref risk |
| glm | ✅ LEGIT | 85 | documenthandler.cpp:890 m_reply->readAll() without null check; m_reply could be null if request never started |
| kimi | ✅ LEGIT | 80 | documenthandler.cpp:890 m_reply->readAll() without null check. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — m_reply->readAll no null check; fires after get() (documenthandler.cpp:890) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

