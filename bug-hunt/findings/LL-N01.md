# [LL-N01] 10 EditorToolbar MouseArea/TextField width-depends-on-width binding loops

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `EditorToolbar.qml (10 instances, lines 924-2053)`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** EditorToolbar.qml (10 instances, lines 924-2053)
- **Severity:** Medium
- **Analysis:** MouseArea.width → TextField.width → (anchors.fill: parent) → MouseArea.width. QML detects and breaks cycle. TextField width resolves to 0 in edit mode.
- **Impact:** Direct numeric input fields invisible/unusable when entering edit mode.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | width-depends-on-width MouseArea/TextField binding-loop risk (EditorToolbar.qml) |
| gpt | ⚠️ PARTIAL | 58 | observed 10 EditorToolbar MouseArea/TextField width-depends-on-width binding loops (src/kirigami_ui/EditorToolbar.qml:924) |
| deepseek | ✅ LEGIT | 80 | MouseArea.width->TextField.width(anchors.fill:parent)->MouseArea.width binding loop; QML engine breaks loop->TextField width=0 |
| glm | ✅ LEGIT | 65 | EditorToolbar.qml 10 instances of width-depends-on-width binding loops lines 924-2053 |
| kimi | ✅ LEGIT | 75 | EditorToolbar.qml:923/1039/1198 direct-input MouseAreas bind width to child widths, creating circular width dependencies |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — width-depends-on-width MouseArea/TextField binding-loop risk (EditorToolbar.qml) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

