# [HDR-N01] promptsession.h not in CMakeLists.txt — SessionModel/DataPoint dead code

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `src/promptsession.h, src/promptsess.cpp, src/CMakeLists.txt`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** src/promptsession.h, src/promptsess.cpp, src/CMakeLists.txt
- **Severity:** Low
- **Analysis:** promptsession.h/cpp exist on disk but are not listed in any CMakeLists.txt. No other file includes promptsession.h. The entire file is never MOC-processed, never compiled. LOG-01/LOG-02 bugs have zero runtime impact.
- **Impact:** Orphaned dead code clutters tree; bugs in this file can't manifest.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 60 | promptsession.h/cpp not in CMakeLists; SessionModel dead code (promptsession.h) |
| gpt | ⚠️ PARTIAL | 58 | observed promptsession.h not in CMakeLists.txt - SessionModel/DataPoint dead code (src/promptsession.h:1) |
| deepseek | ✅ LEGIT | 95 | prompsession.h/cpp not in src/CMakeLists.txt — never MOC-processed never compiled dead code |
| glm | ✅ LEGIT | 80 | promptsession.h not in CMakeLists.txt; SessionModel/DataPoint are dead code |
| kimi | ✅ LEGIT | 80 | promptsession.h/cpp exist but are absent from src/CMakeLists.txt source lists; the code is never compiled. |
| opus-ultra | ✅ LEGIT | 60 | promptsession.h/cpp not in CMakeLists; SessionModel dead code (promptsession.h) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

