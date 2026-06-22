# [R2-FONT-01] RichText label renders unescaped plain text — HTML metacharacters break display

- **Status:** OPEN
- **Severity:** Medium
- **Category:** Type Safety
- **Location:** `src/systemfontchooserdialog.ui:44, src/systemfontchooserdialog.cpp:55`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/systemfontchooserdialog.ui:44, src/systemfontchooserdialog.cpp:55
- **Severity:** Medium
- **Category:** Type Safety
- **Analysis:** textPreviewLabel configured as RichText in UI file. show() calls setText(text) with raw user text. `<`, `>`, `&` chars parsed as HTML, causing text to disappear or render garbled.
- **Impact:** Font preview shows broken/missing text whenever script contains angle brackets or ampersands. Should use Qt::convertFromPlainText() or switch to PlainText.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 85 | RichText label + raw setText breaks on </&> (systemfontchooserdialog.ui:44) |
| gpt | ✅ LEGIT | 78 | RichText label renders unescaped plain text - HTML metacharacters break display (src/systemfontchooserdialog.ui:44) |
| deepseek | ✅ LEGIT | 75 | RichText label renders unescaped plain text at systemfontchooserdialog.cpp:55/ui:44; < > & parsed as HTML in RichText mode — confirmed; should use PlainText or convertFromPlainText |
| glm | ✅ LEGIT | 80 | systemfontchooserdialog.cpp:55 setText on preview label with unescaped text; RichText label could interpret HTML metacharacters |
| kimi | ✅ LEGIT | 75 | systemfontchooserdialog.ui:44 textFormat=RichText and cpp:55 setText(text) with unescaped input; HTML metacharacters can break preview or alter rendering. |
| opus-ultra | ✅ LEGIT | 85 | RichText label + raw setText breaks on </&> (systemfontchooserdialog.ui:44) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

