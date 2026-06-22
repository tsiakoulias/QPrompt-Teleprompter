# [WARN-N03] quint64→int implicit narrowing in nextMarker()/previousMarker()

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `documenthandler.cpp:1713,1721`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp:1713,1721
- **Severity:** Low
- **Analysis:** Q_INVOKABLE accepts quint64 but calls MarkersModel methods taking int. 64→32 bit unsigned→signed truncation. Compiler warning on some toolchains.
- **Impact:** Code quality — practical document sizes stay within int range.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | quint64->int narrowing (dup INT-N01) (documenthandler.cpp:1713) |
| gpt | ⚠️ PARTIAL | 58 | observed quint64->int implicit narrowing in nextMarker()/previousMarker() (src/documenthandler.cpp:1713) |
| deepseek | ✅ LEGIT | 90 | documenthandler.cpp:1713/1721: Q_INVOKABLE takes quint64 position but MarkersModel::nextMarker/previousMarker accept int (markersmodel.h:62-63); 64->32 bit unsigned->signed truncation |
| glm | ✅ LEGIT | 70 | documenthandler.cpp:1713 1721 quint64→int implicit narrowing in nextMarker()/previousMarker() |
| kimi | ✅ LEGIT | 70 | documenthandler.cpp:1713,1721 pass quint64 position to MarkersModel methods taking int, causing 64->32 narrowing. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — quint64->int narrowing (dup INT-N01) (documenthandler.cpp:1713) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

