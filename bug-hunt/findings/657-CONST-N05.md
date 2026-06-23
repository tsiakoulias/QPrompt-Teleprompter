# [657-CONST-N05] Unnecessary copy via const auto instead of const auto& in extendLastMarker

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `markersmodel.cpp:111`
- **Consensus:** 2/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** markersmodel.cpp:111
- **Severity:** Low
- **Analysis:** `const auto last = m_data.last()` — QList::last() returns T&. const auto deduces to const Marker (strips reference), causing full struct copy. Only .text.length() read then discarded.
- **Impact:** Unnecessary heap copy on every marker extension during document parse.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 40 | const auto copy vs const auto& in extendLastMarker (markersmodel.cpp:111) |
| gpt | ⚠️ PARTIAL | 58 | observed Unnecessary copy via const auto instead of const auto& in extendLastMarker (src/markersmodel.cpp:111) |
| deepseek | ✅ LEGIT | 65 | const auto copies Marker object; should be const auto& to avoid copy (markersmodel.cpp:111) |
| glm | ✅ LEGIT | 70 | markersmodel.cpp:111 const auto instead of const auto& in extendLastMarker; unnecessary copy |
| kimi | ❌ FALSE | 65 | extendLastMarker copies last element (const auto); this is a minor inefficiency, not a correctness bug. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — const auto copy vs const auto& in extendLastMarker (markersmodel.cpp:111) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

