# [R2-PTH-01] FileDialog filter matches all files on Linux due to stray glob

- **Status:** OPEN
- **Severity:** Medium
- **Category:** Type Safety
- **Location:** `src/kirigami_ui/PathsPage.qml:105`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/kirigami_ui/PathsPage.qml:105
- **Severity:** Medium
- **Category:** Type Safety
- **Analysis:** Filter string is `"Executable <bin>(*.bin *.BIN *)"` — space between `*.BIN` and `*` means `*` is a third glob pattern matching every file. Should be `(*.bin *.BIN)` without trailing ` *`.
- **Impact:** Executable file filter shows every file on Linux/Unix, defeating its purpose.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 85 | filter trailing glob matches all files (PathsPage.qml:105) |
| gpt | ✅ LEGIT | 78 | FileDialog filter matches all files on Linux due to stray glob (src/kirigami_ui/PathsPage.qml:105) |
| deepseek | ✅ LEGIT | 80 | Filter string trailing space+* at PathsPage.qml:105 creates wildcard glob; Executable filter matches all files — confirmed string analysis |
| glm | ✅ LEGIT | 80 | PathsPage.qml:105 FileDialog filter has stray glob matching all files on Linux |
| kimi | ✅ LEGIT | 85 | PathsPage.qml:105 executable filter includes stray * glob so it matches all files on Linux/Unix. |
| opus-ultra | ✅ LEGIT | 85 | filter trailing glob matches all files (PathsPage.qml:105) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

