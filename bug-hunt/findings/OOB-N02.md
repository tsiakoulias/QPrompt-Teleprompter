# [OOB-N02] SessionModel::data() — same missing row bounds guard

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `promptsession.cpp:40-43`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** promptsession.cpp:40-43
- **Severity:** Medium
- **Analysis:** Identical to OOB-N01. `isValid()` does not enforce row < m_data.size().
- **Impact:** Crash on out-of-range index access.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | SessionModel::data missing bounds guard; dead code (promptsession.cpp:40) |
| gpt | ✅ LEGIT | 78 | SessionModel::data() - same missing row bounds guard (src/promptsession.cpp:40) |
| deepseek | ✅ LEGIT | 90 | m_data.at(row) at promptsession.cpp:43 — same missing rowCount guard as OOB-N01 |
| glm | ✅ LEGIT | 80 | promptsession.cpp:40-43 m_data.at(index.row()) without row bounds guard |
| kimi | ✅ LEGIT | 85 | promptsession.cpp:40-43 has the same missing row-bound guard as OOB-N01 (though the file is dead code). |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — SessionModel::data missing bounds guard; dead code (promptsession.cpp:40) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

