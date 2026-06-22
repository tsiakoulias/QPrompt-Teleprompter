# [R2-PTH-02] File path from file:// URL preserves percent-encoding

- **Status:** OPEN
- **Severity:** Medium
- **Category:** QML/UI
- **Location:** `src/kirigami_ui/PathsPage.qml:113`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/kirigami_ui/PathsPage.qml:113
- **Severity:** Medium
- **Category:** QML/UI
- **Analysis:** `pathsDialog.selectedFile.toString().slice(...)` removes `file://` prefix but does not decode percent-encoding. Path `C:\Program Files\...` becomes `C:/Program%20Files/...` after slicing.
- **Impact:** LibreOffice won't be found if installed in directory with spaces or non-ASCII characters.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 85 | percent-encoding not decoded from file:// (PathsPage.qml:113) |
| gpt | ✅ LEGIT | 78 | File path from file:// URL preserves percent-encoding (src/kirigami_ui/PathsPage.qml:113) |
| deepseek | ✅ LEGIT | 80 | file:// URL percent-encoding not decoded at PathsPage.qml:113; spaces become %20 in path — confirmed; Qt 6 toLocalFile decodes but toString().slice does not |
| glm | ✅ LEGIT | 85 | PathsPage.qml:113 file path from file:// URL preserves percent-encoding; not decoded |
| kimi | ✅ LEGIT | 85 | PathsPage.qml:113 strips file:// prefix but does not decode percent-encoding; spaces remain %20. |
| opus-ultra | ✅ LEGIT | 85 | percent-encoding not decoded from file:// (PathsPage.qml:113) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

