# [111-CMAKE-NEW-02] Duplicate install() of appdata.xml/desktop in root and src/CMakeLists.txt

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `CMakeLists.txt:408-409, src/CMakeLists.txt:524-525`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** CMakeLists.txt:408-409, src/CMakeLists.txt:524-525
- **Severity:** Medium
- **Analysis:** Both root and src CMakeLists install same files to same destinations. CMake 3.27+ CMP0177 hard-errors on duplicate install.
- **Impact:** Build configure failure on CMake 3.27+.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ✅ LEGIT | 55 | duplicate install() of appdata/desktop in root+src (CMakeLists.txt:408) |
| gpt-5.5-xhigh | ✅ LEGIT | 92 | Duplicate install() of appdata.xml/desktop in root and src/CMakeLists.txt (CMakeLists.txt:408) |
| deepseek-v4-pro-max | ✅ LEGIT | 90 | appdata.xml/desktop installed at CMakeLists.txt:408 AND src/CMakeLists.txt:524 — duplicate CMP0177 error on 3.27+ |
| glm-5.2-xhigh | ✅ LEGIT | 80 | CMakeLists.txt:408-409 and src/CMakeLists.txt:524-525 both install appdata.xml/desktop; duplicate install |
| kimi-k2.7-code | ✅ LEGIT | 90 | CMakeLists.txt:408-409 and src/CMakeLists.txt:524-525 both install appdata.xml/desktop to the same destinations. |
| opus-4.8-ultra | ✅ LEGIT | 55 | duplicate install() of appdata/desktop in root+src (CMakeLists.txt:408) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

