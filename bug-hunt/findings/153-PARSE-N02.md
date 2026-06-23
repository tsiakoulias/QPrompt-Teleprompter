# [153-PARSE-N02] MarkersModel::keySearch() hits=1 limits search to first marker only

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `markersmodel.cpp:120`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** markersmodel.cpp:120
- **Severity:** Medium
- **Analysis:** `match(index(0), KeyRole, key, 1, ...)` — hits=1 returns only first match. Variable name is plural (`markersThatMatchShortcut`). Multiple markers with same key at different positions: only first found, second unreachable.
- **Impact:** Key-based marker navigation (Ctrl+key) misses markers beyond first match.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 60 | keySearch match maxHits=1 finds only first same-key marker (markersmodel.cpp:120) |
| gpt | ✅ LEGIT | 78 | MarkersModel::keySearch() hits=1 limits search to first marker only (src/markersmodel.cpp:120) |
| deepseek | ✅ LEGIT | 85 | match(hits=1) at markersmodel.cpp:120 — only first marker found later markers with same key unreachable |
| glm | ✅ LEGIT | 80 | markersmodel.cpp:120 keySearch match() with hits=1 limits search to first matching marker only |
| kimi | ✅ LEGIT | 95 | markersmodel.cpp:120 keySearch calls match(...,1,...); variable implies plural results but only the first matching marker is returned |
| opus-ultra | ✅ LEGIT | 60 | keySearch match maxHits=1 finds only first same-key marker (markersmodel.cpp:120) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

