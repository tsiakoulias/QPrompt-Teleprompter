# [R3-SPL-04] Corrupt cached dictionary file persists permanently after failed copy

- **Status:** OPEN
- **Severity:** Medium
- **Category:** Edge Case
- **Location:** `src/spellchecker.cpp:198-201`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/spellchecker.cpp:198-201
- **Severity:** Medium
- **Category:** Edge Case
- **Analysis:** QFile::copy() return value unchecked. If copy fails partway (disk full, I/O error), truncated corrupt file passes QFile::exists() check forever. No atomic write (write-to-temp-then-rename) or checksum verification.
- **Impact:** Hunspell loads corrupt .aff/.dic file. Language appears permanently missing until user manually deletes cache directory.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 75 | failed QFile::copy leaves corrupt cache that passes exists() (spellchecker.cpp:198) |
| gpt | ✅ LEGIT | 78 | Corrupt cached dictionary file persists permanently after failed copy (src/spellchecker.cpp:198) |
| deepseek | ✅ LEGIT | 90 | spellchecker.cpp:198-199 QFile::copy() return value unchecked; failed partial copy leaves truncated file passing QFile::exists() check forever |
| glm | ✅ LEGIT | 80 | spellchecker.cpp:198-201 if copy fails cached file is corrupt and persists; no cleanup or retry |
| kimi | ✅ LEGIT | 70 | spellchecker.cpp:198-201 ignores QFile::copy() result; a partially-written outPath persists and future loads skip re-copy, leaving corrupt cache. |
| opus-ultra | ✅ LEGIT | 75 | failed QFile::copy leaves corrupt cache that passes exists() (spellchecker.cpp:198) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

