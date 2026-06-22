# [WYS-N01] Internal drag-and-drop copy inserts HTML as plain text — tags become visible

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `Prompter.qml:1362-1363`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** Prompter.qml:1362-1363
- **Severity:** Medium
- **Analysis:** TextArea.insert() always plain text. Internal Ctrl+drag inserts HTML string verbatim — angle brackets/tags visible. External drops correctly use insertHtmlAt().
- **Impact:** Visible HTML tag pollution on every internal copy-drag.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 60 | internal drag inserts HTML as plain text -> tags visible (Prompter.qml:1362) |
| gpt | ✅ LEGIT | 78 | Internal drag-and-drop copy inserts HTML as plain text - tags become visible (src/prompter/Prompter.qml:1362) |
| deepseek | ✅ LEGIT | 90 | Prompter.qml:1362-1363: editor.insert() inserts plain text; internal Ctrl+drag HTML verbatim renders tags visible |
| glm | ✅ LEGIT | 75 | Prompter.qml:1362-1363 internal drag-and-drop copy inserts HTML as plain text; tags become visible |
| kimi | ✅ LEGIT | 85 | Prompter.qml:1362-1365 internal drag with hasHtml uses editor.insert(position,...) which inserts plain text; HTML tags become visible. |
| opus-ultra | ✅ LEGIT | 60 | internal drag inserts HTML as plain text -> tags visible (Prompter.qml:1362) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

