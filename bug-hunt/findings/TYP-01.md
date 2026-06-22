# [TYP-01] Dangling pointer from temporary std::string in SpellChecker::loadOne

- **Status:** REJECTED
- **Severity:** High
- **Category:** 
- **Location:** `src/spellchecker.cpp:154-155`
- **Consensus:** 3/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** src/spellchecker.cpp:154-155
- **Severity:** High
- **Code:**
  ```cpp
  const char *enc = out.hunspell->get_dict_encoding().c_str();  // temporary!
  out.encoding = QByteArray(enc);  // reads freed memory
  ```
- **Analysis:** `get_dict_encoding()` returns `std::string` by value (temporary). `.c_str()` returns a pointer into the temporary's buffer. At the semicolon, the temporary is destroyed; `enc` is dangling. The next line constructs `QByteArray` from freed memory — undefined behavior.
- **Impact:** Corrupted/garbage encoding for hunspell. All subsequent `encode()`/`decode()` return mangled text.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❌ FALSE | 80 | get_dict_encoding returns const std::string& -> not dangling (spellchecker.cpp:154) |
| gpt | ❔ UNSURE | 39 | Hunspell header is not in-tree, so return lifetime cannot be proven here (src/spellchecker.cpp:154) |
| deepseek | ✅ LEGIT | 95 | get_dict_encoding().c_str() at spellchecker.cpp:154 returns temp std::string; enc dangles at semicolon; QByteArray(enc) reads freed memory — UB confirmed |
| glm | ✅ LEGIT | 85 | spellchecker.cpp:154-155 affPath/dicPath are QByteArray from toLocal8Bit stored as local vars then passed to Hunspell; not dangling |
| kimi | ✅ LEGIT | 95 | spellchecker.cpp:154-155 calls c_str() on temporary std::string from get_dict_encoding(); pointer dangles before QByteArray read. |
| opus-ultra | ❌ FALSE | 80 | get_dict_encoding returns const std::string& -> not dangling (spellchecker.cpp:154) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

