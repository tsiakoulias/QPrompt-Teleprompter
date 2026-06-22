# [TBND-N03] extendLastMarker() doesn't update Marker::length field — stale after appends

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `markersmodel.cpp:109-114`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** markersmodel.cpp:109-114
- **Severity:** Low
- **Analysis:** Only m_data.last().text updated, length field stays at default 1. After extension, text.length() exceeds length. Currently masked because LengthRole already returns position instead of length (LOG-03).
- **Impact:** Latent correctness risk; would manifest if LOG-03 is fixed.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 55 | extendLastMarker doesn't update Marker::length (markersmodel.cpp:109) |
| gpt | ✅ LEGIT | 78 | extendLastMarker() doesn't update Marker::length field - stale after appends (src/markersmodel.cpp:109) |
| deepseek | ✅ LEGIT | 80 | extendLastMarker updates text but not Marker::length field; masked by LOG-03 LengthRole bug at markersmodel.cpp:109-114 |
| glm | ✅ LEGIT | 65 | markersmodel.cpp:109-114 extendLastMarker doesn't update Marker::length field; stale after appends |
| kimi | ✅ LEGIT | 90 | markersmodel.cpp:109-114 extendLastMarker appends text but never updates marker.length; length role is incorrect |
| opus-ultra | ✅ LEGIT | 55 | extendLastMarker doesn't update Marker::length (markersmodel.cpp:109) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

