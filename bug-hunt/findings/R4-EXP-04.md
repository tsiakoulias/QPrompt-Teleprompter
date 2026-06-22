# [R4-EXP-04] AutoText inserts plain text as HTML — content corruption

- **Status:** OPEN
- **Severity:** High
- **Category:** Logic
- **Location:** `src/documenthandler.cpp:1104-1123`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/documenthandler.cpp:1104-1123
- **Severity:** High
- **Category:** Logic
- **Analysis:** For Qt::AutoText, falls through Qt::RichText to cursor.insertHtml(). If QTextDocument::find() auto-detects as plain text, <script> disappears, entities cause parse errors, angle brackets silently swallowed.
- **Impact:** Plain-text files with <, >, & lose content segments when opened via AutoText path.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 80 | AutoText -> insertHtml for plain text (documenthandler.cpp:1118) |
| gpt | ✅ LEGIT | 84 | AutoText inserts plain text as HTML - content corruption (src/documenthandler.cpp:1104) |
| deepseek | ✅ LEGIT | 90 | documenthandler.cpp:1104-1122 Qt::AutoText falls through to cursor.insertHtml(text) — plain text < > & parsed as HTML causing content loss |
| glm | ✅ LEGIT | 80 | documenthandler.cpp:1104-1123 AutoText path calls insertHtml with plain text; HTML metacharacters in text get interpreted |
| kimi | ✅ LEGIT | 90 | updateContents AutoText case falls through to cursor.insertHtml; documenthandler.cpp:1118-1120 |
| opus-ultra | ✅ LEGIT | 80 | AutoText -> insertHtml for plain text (documenthandler.cpp:1118) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

