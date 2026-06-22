# [COMP-N01] Case-sensitive duplicate detection in setLanguages()

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `spellchecker.cpp:83`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** spellchecker.cpp:83
- **Severity:** Low
- **Analysis:** `seen.contains(lang)` is case-sensitive. `{"en_US", "EN_US"}` loaded as separate dictionaries. Same root cause as SPL2-12 but different code site.
- **Impact:** Duplicate dictionary loading on case-different language inputs.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 55 | case-sensitive duplicate detection in setLanguages (spellchecker.cpp:83) |
| gpt | ✅ LEGIT | 92 | Case-sensitive duplicate detection in setLanguages() (src/spellchecker.cpp:83) |
| deepseek | ✅ LEGIT | 95 | spellchecker.cpp:83: QStringList::contains() is case-sensitive; en_US and EN_US treated as distinct — duplicate dictionaries loaded |
| glm | ✅ LEGIT | 75 | spellchecker.cpp:83 case-sensitive duplicate detection in setLanguages(); allows 'en_US' and 'EN_US' |
| kimi | ✅ LEGIT | 80 | spellchecker.cpp:83 seen.contains(lang) is case-sensitive; 'en_US' and 'EN_US' load as separate dictionaries. |
| opus-ultra | ✅ LEGIT | 55 | case-sensitive duplicate detection in setLanguages (spellchecker.cpp:83) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

