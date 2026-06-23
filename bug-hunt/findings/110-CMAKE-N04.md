# [110-CMAKE-N04] Relative ../build path in install rules — out-of-tree build failure

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `src/CMakeLists.txt:521-522`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/CMakeLists.txt:521-522
- **Severity:** Medium
- **Analysis:** `install(DIRECTORY ../build/bin/org ...)` assumes build dir named "build" sibling to source. Out-of-tree builds resolve to nonexistent path.
- **Impact:** macOS QML plugin installation empty for out-of-tree builds.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 55 | relative ../build path in install rules breaks out-of-tree (CMakeLists.txt:521) |
| gpt | ✅ LEGIT | 78 | Relative ../build path in install rules - out-of-tree build failure (src/CMakeLists.txt:521) |
| deepseek | ✅ LEGIT | 90 | src/CMakeLists.txt:521-522: install(DIRECTORY ../build/bin/org ...) — relative path assumes build dir named build sibling to source; out-of-tree builds resolve nonexistent path |
| glm | ✅ LEGIT | 75 | src/CMakeLists.txt:521-522 relative ../build path in install rules; out-of-tree build failure |
| kimi | ✅ LEGIT | 90 | src/CMakeLists.txt:521-522 hardcodes ../build/bin/org paths breaking out-of-source builds. |
| opus-ultra | ✅ LEGIT | 55 | relative ../build path in install rules breaks out-of-tree (CMakeLists.txt:521) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

