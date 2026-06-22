# [DECL-N01] MarkersModel::keySearch — default params in definition but not declaration

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `markersmodel.h:64 vs markersmodel.cpp:117`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** markersmodel.h:64 vs markersmodel.cpp:117
- **Severity:** Low
- **Analysis:** Same DCL pattern as DCL-N01/DCL-N02. Defaults `currentPosition = 0, reverse = false, wrap = true` in definition invisible to MOC and QML. Currently always called with all 4 args, masked.
- **Impact:** Latent — any direct QML invocation with fewer args fails.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | keySearch default params in def not decl (markersmodel.h:64) |
| gpt | ✅ LEGIT | 78 | MarkersModel::keySearch - default params in definition but not declaration (src/markersmodel.h:64) |
| deepseek | ✅ LEGIT | 75 | keySearch has default params in definition but not declaration (markersmodel.h:64 vs markersmodel.cpp:117) |
| glm | ✅ LEGIT | 75 | markersmodel.h:64 vs markersmodel.cpp:117 keySearch default params in definition but not declaration |
| kimi | ✅ LEGIT | 95 | markersmodel.h:64 declares keySearch(int key,int currentPosition,bool reverse,bool wrap) without defaults; markersmodel.cpp:117 defines defaults (0,false,true) invisible to MOC and QML callers. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — keySearch default params in def not decl (markersmodel.h:64) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

