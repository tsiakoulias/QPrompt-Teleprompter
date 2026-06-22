# [R4-ROOT-03] ESC global shortcut skips single-layer pages — can't dismiss with keyboard

- **Status:** REJECTED
- **Severity:** Medium
- **Category:** Logic
- **Location:** `src/kirigami_ui/main.qml:481`
- **Consensus:** 2/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** src/kirigami_ui/main.qml:481
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** StandardKey.Cancel checks `if (layers.depth > 1)` before clear(). Exactly one layer (common case: About, Paths, Remote pages) → depth===1 → branch skipped → falls through to restoreFocus() leaving layer visible. Should be `depth > 0`.
- **Impact:** On desktop Linux/macOS (no back button), pressing Escape on layer pages does nothing visible.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❌ FALSE | 80 | layers.depth>1 is correct Kirigami idiom (main.qml:481) |
| gpt | ❌ FALSE | 76 | layers.depth > 1 is the expected Kirigami layer-pop guard (src/kirigami_ui/main.qml:481) |
| deepseek | ✅ LEGIT | 90 | main.qml:481 checks layers.depth>1 before clear(); single layer(depth===1) skipped — ESC doesn't dismiss About/Paths/Remote pages |
| glm | ⚠️ PARTIAL | 65 | main.qml:481 ESC handler uses if/else chain; single-layer pages may not dismiss with keyboard |
| kimi | ✅ LEGIT | 90 | ESC handler checks pageStack.layers.depth > 1 so single-layer pages stay open; main.qml:481 |
| opus-ultra | ❌ FALSE | 80 | layers.depth>1 is correct Kirigami idiom (main.qml:481) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

