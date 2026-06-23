# [149-MODEL-N01] MarkersModel::rowCount ignores parent.isValid() — returns full size for child probe

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `markersmodel.cpp:32-36`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** markersmodel.cpp:32-36
- **Severity:** Medium
- **Analysis:** Flat QAbstractListModel should return 0 when parent.isValid(). Unconditionally returns m_data.size(). QML views probing children get wrong count. LOG-01 covers SessionModel only.
- **Impact:** Wrong row count reported for child indices.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 60 | rowCount ignores parent.isValid(); returns size for child (markersmodel.cpp:32) |
| gpt | ✅ LEGIT | 78 | MarkersModel::rowCount ignores parent.isValid() - returns full size for child probe (src/markersmodel.cpp:32) |
| deepseek | ✅ LEGIT | 90 | markersmodel.cpp:32-36: rowCount ignores parent.isValid(); returns full size for child index probes on flat list model |
| glm | ✅ LEGIT | 75 | markersmodel.cpp:32-36 rowCount ignores parent.isValid(); returns full size for child probe |
| kimi | ✅ LEGIT | 80 | markersmodel.cpp:32-36 rowCount ignores parent.isValid() and always returns m_data.size(); flat model should return 0 for valid parent. |
| opus-ultra | ✅ LEGIT | 60 | rowCount ignores parent.isValid(); returns size for child (markersmodel.cpp:32) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

