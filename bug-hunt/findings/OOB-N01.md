# [OOB-N01] MarkersModel::data() — m_data.at() without row < rowCount() guard

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `markersmodel.cpp:40-43`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** markersmodel.cpp:40-43
- **Severity:** Medium
- **Analysis:** `index.isValid()` only checks row>=0, column>=0, model!=nullptr. If row >= m_data.size(), `QList::at()` throws or asserts. `removeMarker()` already has the correct guard.
- **Impact:** Crash if QML passes out-of-range row to data().

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | data() m_data.at() relies on isValid() not rowCount bound (markersmodel.cpp:40) |
| gpt | ✅ LEGIT | 78 | MarkersModel::data() - mdata.at() without row rowCount() guard (src/markersmodel.cpp:40) |
| deepseek | ✅ LEGIT | 90 | m_data.at(row) at markersmodel.cpp:43 — isValid() doesn't enforce row<rowCount() |
| glm | ✅ LEGIT | 80 | markersmodel.cpp:40-43 m_data.at(index.row()) without row < rowCount() bounds guard |
| kimi | ✅ LEGIT | 90 | markersmodel.cpp:40-43 only checks index.isValid() before m_data.at(index.row()); missing row<rowCount guard. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — data() m_data.at() relies on isValid() not rowCount bound (markersmodel.cpp:40) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

