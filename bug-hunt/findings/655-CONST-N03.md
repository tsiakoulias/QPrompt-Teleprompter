# [655-CONST-N03] MarkersModel::previousMarker(), nextMarker(), keySearch(), binarySearch() not const

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `markersmodel.h:62,63,64,78, markersmodel.cpp:117,151,205,217`
- **Consensus:** 2/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** markersmodel.h:62,63,64,78, markersmodel.cpp:117,151,205,217
- **Severity:** Low
- **Analysis:** Four pure-read query methods (binarySearch recursive, previous/next/keySearch call binarySearch/data) declared non-const. Transitive — binarySearch non-const forces all callers non-const.
- **Impact:** Cannot be called on const MarkersModel&.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 40 | marker query methods not const (markersmodel.h:62) |
| gpt | ⚠️ PARTIAL | 58 | observed MarkersModel::previousMarker(), nextMarker(), keySearch(), binarySearch() not const (src/markersmodel.h:62) |
| deepseek | ✅ LEGIT | 55 | four marker query methods lack const qualifier (markersmodel.h:62-64 78) |
| glm | ✅ LEGIT | 70 | markersmodel.h:62-64 78 previousMarker/nextMarker/keySearch/binarySearch not const |
| kimi | ❌ FALSE | 70 | MarkersModel query methods lack const, but they are not misused or mutating data incorrectly. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — marker query methods not const (markersmodel.h:62) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

