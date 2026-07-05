# [356-CMAKE-N05] foreach(file IN LISTS icon_files doc) — "doc" never defined

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `src/CMakeLists.txt:243`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** CMakeLists.txt:332,407
- **Severity:** Medium
- **Analysis:** `UNIX` true for Android. `# AND NOT ANDROID` comments confirm exclusion intended but not implemented. KDE flags may inject incompatible linker flags into Android builds.
- **Impact:** Potentially broken Android builds from KDE compiler/linker flags.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ✅ LEGIT | 55 | foreach IN LISTS icon_files doc; 'doc' never defined (CMakeLists.txt:243) |
| gpt-5.5-xhigh | ✅ LEGIT | 78 | foreach(file IN LISTS iconfiles doc) - "doc" never defined (src/CMakeLists.txt:243) |
| deepseek-v4-pro-max | ✅ LEGIT | 85 | src/CMakeLists.txt:243: foreach(file IN LISTS icon_files doc) — variable doc never defined; CMake treats as empty (no-op) but likely typo for document_files; DUPLICATE-ID |
| glm-5.2-xhigh | ✅ LEGIT | 75 | src/CMakeLists.txt:243 foreach(file IN LISTS icon_files doc) - 'doc' never defined as a variable |
| kimi-k2.7-code | ✅ LEGIT | 80 | src/CMakeLists.txt:243 foreach(file IN LISTS icon_files doc) iterates over undefined variable 'doc'. |
| opus-4.8-ultra | ✅ LEGIT | 55 | foreach IN LISTS icon_files doc; 'doc' never defined (CMakeLists.txt:243) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

