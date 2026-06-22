# [LOG-01] SessionModel::rowCount returns m_data.size() for both valid and invalid parents

- **Status:** OPEN
- **Severity:** High
- **Category:** 
- **Location:** `src/promptsession.cpp:31-36`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/promptsession.cpp:31-36
- **Severity:** High
- **Code:**
  ```cpp
  int SessionModel::rowCount(const QModelIndex &parent) const
  {
      if (!parent.isValid())
          return m_data.size();
          //return 0;         // <-- commented-out correct code
      return m_data.size();   // <-- should return 0 for valid parent
  }
  ```
- **Analysis:** For a flat list model, a valid parent should return 0 children. Both branches return `m_data.size()`, making the if/else meaningless. The commented-out `//return 0;` confirms the developer's intent.
- **Impact:** QML ListView/Repeater may attempt to recurse into list items, causing corrupted display or infinite recursion.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 100 | both branches return m_data.size() (promptsession.cpp:31-36) |
| gpt | ✅ LEGIT | 92 | rowCount returns the same size for valid and invalid parents (src/promptsession.cpp:31) |
| deepseek | ✅ LEGIT | 95 | rowCount returns m_data.size() for valid parent at promptsess.cpp:35; should be 0 for flat list; commented-out return 0 confirms |
| glm | ✅ LEGIT | 90 | promptsession.cpp:31-36 rowCount returns m_data.size() for both valid and invalid parents; should return 0 for valid parent in flat list model |
| kimi | ✅ LEGIT | 95 | promptsession.cpp:31-36 returns m_data.size() for both valid and invalid parents; flat model should return 0 for valid parent. |
| opus-ultra | ✅ LEGIT | 100 | both branches return m_data.size() (promptsession.cpp:31-36) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

