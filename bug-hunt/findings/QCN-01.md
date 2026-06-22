# [QCN-01] O(n²) contains()-in-loop during custom words file load

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `spellchecker.cpp:370-374`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** spellchecker.cpp:370-374
- **Severity:** Low
- **Analysis:** while-loop calls contains() on growing unsorted list. Total cost O(n²). QSet dedup then sort would be O(n log n).
- **Impact:** Quadratic startup time with large custom dictionaries.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 55 | O(n^2) contains()-in-loop during custom-words load (spellchecker.cpp:370) |
| gpt | ✅ LEGIT | 78 | O(n²) contains()-in-loop during custom words file load (src/spellchecker.cpp:370) |
| deepseek | ✅ LEGIT | 90 | O(n^2) contains() on QStringList in loop at spellchecker.cpp:372 — QSet would be O(n log n) |
| glm | ✅ LEGIT | 75 | spellchecker.cpp:370-374 O(n²) contains()-in-loop during custom words file load |
| kimi | ✅ LEGIT | 80 | spellchecker.cpp:372 calls m_customWords.contains(line) while iterating and appending, giving O(n^2) load time. |
| opus-ultra | ✅ LEGIT | 55 | O(n^2) contains()-in-loop during custom-words load (spellchecker.cpp:370) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

