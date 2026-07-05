# [659-DETACH-N01] 4 non-const operator[] on QList in keySearch() — unnecessary implicit sharing detach

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `markersmodel.cpp:126,133,137,144`
- **Consensus:** 2/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** markersmodel.cpp:126,133,137,144
- **Severity:** Low
- **Analysis:** QModelIndexList is implicitly shared. Non-const operator[] returns T& forcing deep copy. All 4 sites only read — should use .at() or declare const.
- **Impact:** Wasteful heap allocation per keySearch() call. Minor performance.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ⚠️ PARTIAL | 40 | non-const operator[] detaches QList (markersmodel.cpp:126) |
| gpt-5.5-xhigh | ⚠️ PARTIAL | 58 | observed 4 non-const operator[] on QList in keySearch() - unnecessary implicit sharing detach (src/markersmodel.cpp:126) |
| deepseek-v4-pro-max | ✅ LEGIT | 75 | markersmodel.cpp:126 133 137 144: non-const operator[] on QModelIndexList forces implicit sharing detach; all uses read-only |
| glm-5.2-xhigh | ✅ LEGIT | 70 | markersmodel.cpp:126 133 137 144 4 non-const operator[] on QList in keySearch; unnecessary implicit sharing detach |
| kimi-k2.7-code | ❌ FALSE | 60 | markersmodel.cpp:126,133,137,144 use non-const operator[] on QModelIndexList; in Qt 6 QModelIndexList is QList with reference stability but claim of implicit-sharing detach is speculative and not a verified bug. |
| opus-4.8-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — non-const operator[] detaches QList (markersmodel.cpp:126) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

