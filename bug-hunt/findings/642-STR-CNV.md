# [642-STR-CNV] 5 defensive validation gaps: toInt() without ok flag in getMarkerKey, parse(×2), setFontSize, and 32 hotkey reads

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `documenthandler.cpp:757,1667,1675,829, globalhotkeys.cpp:569-698`
- **Consensus:** 3/6 agents LEGIT · CONFLICT

## Original report claim

- **Files:** documenthandler.cpp:757,1667,1675,829, globalhotkeys.cpp:569-698
- **Severity:** Low
- **Analysis:** All rely on `toInt()`/`QVariant::toInt()` returning 0 on failure, which matches desired default (0 = unknown/unset) in every case. No functional behavior incorrect — omission of explicit ok validation and defensive coding.
- **Impact:** None currently. Latent fragility if Qt changes implicit-from-invalid behavior.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ⚠️ PARTIAL | 45 | several toInt() without ok flag; defensive gap (documenthandler.cpp:757) |
| gpt-5.5-xhigh | ✅ LEGIT | 78 | 5 defensive validation gaps: toInt() without ok flag in getMarkerKey, parse(×2), setFontSize, and 32 hotkey reads (src/documenthandler.cpp:757) |
| deepseek-v4-pro-max | ✅ LEGIT | 60 | multiple toInt() calls without ok flag silently discard parse failures (documenthandler.cpp:757 829) |
| glm-5.2-xhigh | ✅ LEGIT | 75 | documenthandler.cpp:757 1667 1675 829 globalhotkeys.cpp:569-698 5 defensive validation gaps: toInt() without ok flag |
| kimi-k2.7-code | ❌ FALSE | 60 | documenthandler.cpp:757/1667/1675 and globalhotkeys.cpp:569-698 use toInt() without ok flag, but 0 default matches intended sentinel; no defect. |
| opus-4.8-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — several toInt() without ok flag; defensive gap (documenthandler.cpp:757) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

