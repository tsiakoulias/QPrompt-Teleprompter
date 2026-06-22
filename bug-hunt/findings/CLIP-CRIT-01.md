# [CLIP-CRIT-01] Paste via toolbar button and File menu bypasses HTML sanitization

- **Status:** OPEN
- **Severity:** Critical
- **Category:** 
- **Location:** `EditorToolbar.qml:345, main.qml:686`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** EditorToolbar.qml:345, main.qml:686
- **Severity:** Critical
- **Analysis:** Both invoke editor.paste() (raw Qt built-in) instead of document.paste() (filtered via filterHtml()). Ctrl+V and context menu correctly use document.paste(). Unsanitized HTML with scripts, event handlers, javascript: URLs injected.
- **Impact:** Same RCE/XSS class as SEC-01 and R4-EXP-01. Keyboard shortcuts safe; toolbar and File menu are not.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 85 | toolbar/menu call editor.paste() (unfiltered) vs document.paste() elsewhere (EditorToolbar.qml:345, main.qml:686) |
| gpt | ✅ LEGIT | 84 | Paste via toolbar button and File menu bypasses HTML sanitization (src/kirigami_ui/EditorToolbar.qml:345) |
| deepseek | ✅ LEGIT | 95 | EditorToolbar.qml:345 calls editor.paste() (raw Qt); main.qml:686 same; both bypass filterHtml(); Ctrl+V correctly uses document.paste() |
| glm | ✅ LEGIT | 80 | EditorToolbar.qml:345 main.qml:686 paste via toolbar button and File menu bypasses HTML sanitization |
| kimi | ✅ LEGIT | 90 | EditorToolbar.qml:345 and main.qml:686 call editor.paste() instead of document.paste()/filterHtml; bypasses sanitization. |
| opus-ultra | ✅ LEGIT | 85 | toolbar/menu call editor.paste() (unfiltered) vs document.paste() elsewhere (EditorToolbar.qml:345 |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

