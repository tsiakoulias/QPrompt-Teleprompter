# [449-VIS-FB-N01] bookmarkListButton and searchButton missing checkable: true — no checked background

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `EditorToolbar.qml:188,202`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** EditorToolbar.qml:188,202
- **Severity:** Low
- **Analysis:** Both declare checked binding but omit checkable: true. Material style checked background only renders when checkable && checked. Text color feedback works but background never highlights.
- **Impact:** Checked state visually diminished — harder to tell if markers drawer or find panel is open.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | bookmarkListButton/searchButton missing checkable:true (EditorToolbar.qml:188) |
| gpt | ⚠️ PARTIAL | 58 | observed bookmarkListButton and searchButton missing checkable: true - no checked background (src/kirigami_ui/EditorToolbar.qml:188) |
| deepseek | ✅ LEGIT | 90 | EditorToolbar.qml:188 202: bookmarkListButton.searchButton declare checked binding but omit checkable:true; no Material checked background |
| glm | ✅ LEGIT | 70 | EditorToolbar.qml:188 202 bookmarkListButton and searchButton missing checkable: true; no checked background |
| kimi | ✅ LEGIT | 90 | EditorToolbar.qml:188/202 set `checked` on bookmarkListButton/searchButton but omit `checkable: true` |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — bookmarkListButton/searchButton missing checkable:true (EditorToolbar.qml:188) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

