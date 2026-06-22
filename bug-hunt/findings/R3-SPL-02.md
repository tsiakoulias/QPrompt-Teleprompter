# [R3-SPL-02] decode() uses fromLocal8Bit() — suggestions show as mojibake

- **Status:** OPEN
- **Severity:** Medium
- **Category:** Type Safety
- **Location:** `src/spellchecker.cpp:408-413`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** src/spellchecker.cpp:408-413
- **Severity:** Medium
- **Category:** Type Safety
- **Analysis:** Same encoding mismatch as encode(). Hunspell suggestions from non-UTF-8 dictionary interpreted with system local 8-bit codec instead of dictionary encoding.
- **Impact:** Spelling suggestions with non-ASCII characters appear as garbled text.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 70 | decode() fromLocal8Bit ignores dict encoding (spellchecker.cpp:408) |
| gpt | ✅ LEGIT | 78 | decode() uses fromLocal8Bit() - suggestions show as mojibake (src/spellchecker.cpp:408) |
| deepseek | ✅ LEGIT | 80 | spellchecker.cpp:408-412 decode() fallback fromLocal8Bit() same encoding mismatch as encode() — non-UTF-8 dictionary suggestions garbled |
| glm | ⚠️ PARTIAL | 65 | spellchecker.cpp:408-413 decode uses fromLocal8Bit; correct for legacy encodings but may produce mojibake if system locale differs |
| kimi | ✅ LEGIT | 75 | spellchecker.cpp:408-413 decode falls back to fromLocal8Bit() ignoring d.encoding; suggestions from non-UTF-8 dictionaries become mojibake. |
| opus-ultra | ✅ LEGIT | 70 | decode() fromLocal8Bit ignores dict encoding (spellchecker.cpp:408) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

