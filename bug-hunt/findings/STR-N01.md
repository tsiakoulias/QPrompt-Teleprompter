# [STR-N01] main.cpp:158 QLatin1String iterator-pair UB from two unrelated string literals

- **Status:** OPEN
- **Severity:** High
- **Category:** 
- **Location:** `main.cpp:158`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** main.cpp:158
- **Severity:** High
- **Analysis:** `QLatin1String("file", "File to copy.")` matches the iterator-pair constructor `QLatin1StringView(const char *first, const char *last)`. Pointer subtraction between two unrelated string literals is undefined behavior. Resulting QLatin1StringView has arbitrary m_size — garbage content.
- **Impact:** `--help` output contains garbage or crashes during argument parsing.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 70 | QLatin1String(const char*,const char*) two-pointer ctor on unrelated literals = UB (main.cpp:158) |
| gpt | ✅ LEGIT | 84 | main.cpp:158 QLatin1String iterator-pair UB from two unrelated string literals (src/main.cpp:158) |
| deepseek | ✅ LEGIT | 90 | QLatin1String('file' 'File to copy.') at main.cpp:158 — iterator-pair ctor from unrelated literals = UB |
| glm | ✅ LEGIT | 85 | main.cpp:158 QLatin1String iterator pair from two unrelated string literals; UB |
| kimi | ✅ LEGIT | 95 | main.cpp:158 QLatin1String(\source\" |
| opus-ultra | ✅ LEGIT | 70 | QLatin1String(const char* |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

