# [FINAL-19] Encoding fallback uses toLocal8Bit() instead of dictionary's actual encoding

- **Status:** OPEN
- **Severity:** Medium
- **Category:** I18N
- **Location:** `src/spellchecker.cpp:402-406, 408-412`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** src/spellchecker.cpp:402-406, 408-412
- **Severity:** Medium
- **Category:** I18N
- **Analysis:** encode()/decode() ignore d.encoding (read from .aff file). Fallback to system locale 8-bit, which differs from dictionary encoding.
- **Impact:** Non-ASCII words corrupted in non-UTF-8 Hunspell dictionaries; false positives/negatives.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 70 | encode/decode use locale 8-bit not dict encoding (dup R3-SPL) (spellchecker.cpp:402) |
| gpt | ✅ LEGIT | 78 | Encoding fallback uses toLocal8Bit() instead of dictionary's actual encoding (src/spellchecker.cpp:402) |
| deepseek | ✅ LEGIT | 85 | spellchecker.cpp:402-406/408-412 encode/decode fallback toLocal8Bit/fromLocal8Bit ignores dictionary encoding — same root as R3-SPL-01/02(duplicate) |
| glm | ⚠️ PARTIAL | 65 | spellchecker.cpp:402-412 encode/decode fallback uses toLocal8Bit/fromLocal8Bit instead of dictionary's actual encoding |
| kimi | ✅ LEGIT | 85 | spellchecker.cpp:402-406,408-412 encode/decode fall back to toLocal8Bit/fromLocal8Bit when encoding is not UTF-8, ignoring d.encoding. |
| opus-ultra | ✅ LEGIT | 70 | encode/decode use locale 8-bit not dict encoding (dup R3-SPL) (spellchecker.cpp:402) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

