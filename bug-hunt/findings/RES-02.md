# [RES-02] loadFromNetworkFinihed ignores the QNetworkReply* signal parameter

- **Status:** OPEN
- **Severity:** High
- **Category:** 
- **Location:** `src/documenthandler.cpp:145,888-901`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/documenthandler.cpp:145,888-901
- **Severity:** High
- **Code:**
  ```cpp
  connect(m_network, &QNetworkAccessManager::finished, this, &DocumentHandler::loadFromNetworkFinihed);

  void DocumentHandler::loadFromNetworkFinihed() {
      auto document = m_reply->readAll();   // uses member, not the reply that actually finished
  }
  ```
- **Analysis:** `QNetworkAccessManager::finished(QNetworkReply *)` provides the exact reply that completed. The slot ignores this parameter and uses `m_reply` instead. Combined with RES-01, this can read from the wrong reply.
- **Impact:** Wrong document content loaded; stale replies processed as current request.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 95 | slot ignores QNetworkReply* param (documenthandler.cpp:888) |
| gpt | ✅ LEGIT | 84 | loadFromNetworkFinihed ignores the QNetworkReply signal parameter (src/documenthandler.cpp:145) |
| deepseek | ✅ LEGIT | 92 | loadFromNetworkFinihed() ignores QNetworkReply* signal param at doc.cpp:145/888; reads m_reply member instead — wrong reply if overwritten by RES-01 |
| glm | ✅ LEGIT | 90 | documenthandler.cpp:145 connect finished to loadFromNetworkFinihed() which takes no args; the QNetworkReply* parameter from finished signal is ignored |
| kimi | ✅ LEGIT | 90 | documenthandler.cpp:145 connects QNetworkAccessManager::finished to loadFromNetworkFinihed() which ignores the reply argument at :888-890. |
| opus-ultra | ✅ LEGIT | 95 | slot ignores QNetworkReply* param (documenthandler.cpp:888) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

