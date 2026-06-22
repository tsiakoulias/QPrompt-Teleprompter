# [TP-N01] "Error loading file..." used as document content, not placeholderText

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `Prompter.qml:969`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** Prompter.qml:969
- **Severity:** Medium
- **Analysis:** `text: qsTr("Error loading file…")` set as TextArea's text property — appears as editable document body on new/empty documents.
- **Impact:** New documents show confusing "Error loading file..." as editable content.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 55 | 'Error loading file' shown as document content not placeholder (Prompter.qml:969) |
| gpt | ⚠️ PARTIAL | 58 | observed "Error loading file..." used as document content, not placeholderText (src/prompter/Prompter.qml:969) |
| deepseek | ✅ LEGIT | 90 | Prompter.qml:969: qsTr('Error loading file...') assigned as TextArea.text content not placeholderText; shows as editable document body |
| glm | ✅ LEGIT | 70 | Prompter.qml:969 'Error loading file...' used as document content not placeholderText |
| kimi | ✅ LEGIT | 80 | Prompter.qml:969 sets TextArea.text: qsTr('Error loading file…') as default initial text instead of placeholder. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — 'Error loading file' shown as document content not placeholder (Prompter.qml:969) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

