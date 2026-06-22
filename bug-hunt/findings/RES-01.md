# [RES-01] Network reply overwritten without aborting previous download

- **Status:** OPEN
- **Severity:** High
- **Category:** 
- **Location:** `src/documenthandler.cpp:884`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/documenthandler.cpp:884
- **Severity:** High
- **Code:**
  ```cpp
  m_reply = m_network->get(req);  // old m_reply overwritten, never abort()ed
  ```
- **Analysis:** When `loadFromNetwork()` is called a second time, `m_reply` is reassigned without calling `abort()` or `deleteLater()` on the old reply. Old reply continues downloading; when it completes, the slot reads from the new (possibly incomplete) `m_reply`.
- **Impact:** Stale network traffic, wasted bandwidth/CPU, potential data corruption when stale replies finish and the slot reads wrong data.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 95 | m_reply overwritten w/o abort (documenthandler.cpp:884) |
| gpt | ✅ LEGIT | 84 | Network reply overwritten without aborting previous download (src/documenthandler.cpp:884) |
| deepseek | ✅ LEGIT | 90 | m_reply=m_network->get(req) at doc.cpp:884 overwrites old reply w/o abort()/deleteLater(); old request continues; stale data race confirmed |
| glm | ✅ LEGIT | 85 | documenthandler.cpp:884 m_reply overwritten without aborting previous reply; previous download leaked |
| kimi | ✅ LEGIT | 90 | documenthandler.cpp:884 assigns m_reply from new get() without aborting/deleting previous reply. |
| opus-ultra | ✅ LEGIT | 95 | m_reply overwritten w/o abort (documenthandler.cpp:884) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

