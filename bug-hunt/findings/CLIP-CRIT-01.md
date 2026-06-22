# [CLIP-CRIT-01] Paste via toolbar button and File menu bypasses HTML sanitization

- **Status:** FIXED  (routed toolbar+menu paste through document.paste(); commit 9da5d07 on fix/toolbar-menu-paste-filtering)
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

## Patch

- **Severity correction:** The "Critical RCE/XSS" framing is **misdiagnosed**. `filterHtml()`
  (`documenthandler.cpp:1246`) is a *formatting* cleanup (removes non-scaling font-sizes and forced
  office text colours), not a security sanitizer — it does not strip scripts/event-handlers/`javascript:`.
  And `paste()` inserts via `QTextDocument::insertHtml` (`documenthandler.cpp:1351`), a Qt rich-text
  engine that does **not** execute scripts. So there is no XSS/RCE. The real defect is **paste
  inconsistency** (a formatting bug, ~Medium): toolbar/menu paste keeps hardcoded font sizes that then
  don't scale with the prompter, and office colours that break on dark backgrounds.
- **Root cause:** The toolbar Paste button (`EditorToolbar.qml:345`) and the global File-menu Paste
  (`main.qml:686`) called the editor's raw `editor.paste()`, while the other four paste paths (Ctrl+V,
  context menu) use `document.paste()` → `DocumentHandler::paste()` → `filterHtml()`. The two outliers
  bypassed the filter.
- **Fix:** Routed both through `document.paste()`, mirroring the existing context-menu pattern
  (`enabled: editor.canPaste; onTriggered: document.paste()`, `Prompter.qml:2564`). `canPaste` stays on
  the editor. Two-line change, no new code.
- **Files changed:** `src/kirigami_ui/EditorToolbar.qml` (+1/−1), `src/kirigami_ui/main.qml` (+1/−1).
- **Verification:** `document` resolves in both contexts via existing aliases already used in the same
  files (`viewport.prompter.document` at EditorToolbar.qml:221; `root.pageStack.currentItem.document` at
  main.qml:76,153). Change is identical to the four working call sites. No C++ to compile; full Qt build
  not run on this host (no toolchain) — QML reference change verified against established usages.
- **Commit / PR:** `9da5d07` on branch `fix/toolbar-menu-paste-filtering` (cut from `main`).

