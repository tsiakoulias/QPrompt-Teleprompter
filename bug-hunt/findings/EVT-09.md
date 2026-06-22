# [EVT-09] Flow ToolSeparator visibility compares y of potentially invisible rows

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `EditorToolbar.qml:246-249,284-287,309-312,347-350,433-437,549-552,710-713,774-777`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** EditorToolbar.qml:246-249,284-287,309-312,347-350,433-437,549-552,710-713,774-777
- **Severity:** Low
- **Analysis:** Separator visibility uses row.y when row may be invisible (y=0), matching visible row at y=0 → false positive separator.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | Flow ToolSeparator visibility compares y of invisible rows (EditorToolbar.qml:246) |
| gpt | ⚠️ PARTIAL | 52 | observed Flow ToolSeparator visibility compares y of potentially invisible rows (src/kirigami_ui/EditorToolbar.qml:246) |
| deepseek | ✅ LEGIT | 78 | ToolSeparator visibility compares row.y when row may be invisible(y=0); false positive match (EditorToolbar.qml:246-249) |
| glm | ⚠️ PARTIAL | 60 | EditorToolbar.qml:246+ ToolSeparator visibility compares y of potentially invisible rows; cosmetic |
| kimi | ✅ LEGIT | 70 | EditorToolbar.qml:246-249 ToolSeparator visibility compares anchorsRow.y to playbackRow.y even when a row may be invisible at y=0. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — Flow ToolSeparator visibility compares y of invisible rows (EditorToolbar.qml:246) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

