# [WARN-N02] SpellChecker::addWord() — dead public API, never called

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `spellchecker.h:48, spellchecker.cpp:134-140`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** spellchecker.h:48, spellchecker.cpp:134-140
- **Severity:** Low
- **Analysis:** Full implementation but never invoked. DocumentHandler uses addCustomWord() instead.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 60 | addWord() is dead public API never called (spellchecker.h:48) |
| gpt | ⚠️ PARTIAL | 58 | observed SpellChecker::addWord() - dead public API, never called (src/spellchecker.h:48) |
| deepseek | ✅ LEGIT | 85 | spellchecker.h:48 / spellchecker.cpp:134-140: addWord() full implementation exists but never invoked; DocumentHandler uses addCustomWord() instead — dead public API |
| glm | ✅ LEGIT | 75 | spellchecker.h:48 spellchecker.cpp:134-140 addWord() dead public API never called from DocumentHandler |
| kimi | ✅ LEGIT | 70 | spellchecker.h:48 / spellchecker.cpp:134-140 addWord() is fully implemented but never called; addCustomWord() is used instead. |
| opus-ultra | ✅ LEGIT | 60 | addWord() is dead public API never called (spellchecker.h:48) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

