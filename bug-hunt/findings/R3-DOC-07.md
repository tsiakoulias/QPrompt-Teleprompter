# [R3-DOC-07] Inverted selection state after failed search()

- **Status:** OPEN
- **Severity:** High
- **Category:** Logic
- **Location:** `src/documenthandler.cpp:1574-1579`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/documenthandler.cpp:1574-1579
- **Severity:** High
- **Category:** Logic
- **Analysis:** Failed search sets selectionEnd=-1 while selectionStart retains old value (e.g., 42). Creates inverted selection (42 > -1). textCursor() constructs cursor at position 42 with KeepAnchor to -1, creating spurious selection from start to 42.
- **Impact:** Accidental text overwrite if user types after failed search.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 85 | inverted selection after failed search (documenthandler.cpp:1574) |
| gpt | ✅ LEGIT | 84 | Inverted selection state after failed search() (src/documenthandler.cpp:1574) |
| deepseek | ✅ LEGIT | 90 | documenthandler.cpp:1575-1579 failed search sets selectionEnd=-1 while selectionStart retains old value(eg42) — inverted selection spurious next-keystroke overwrite |
| glm | ✅ LEGIT | 85 | documenthandler.cpp:1574-1579 search sets selectionEnd even when cursor is null (selectionStart==-1); inverted selection state |
| kimi | ✅ LEGIT | 85 | documenthandler.cpp:1574-1579 skips setCursorPosition/setSelectionStart when search fails but still calls setSelectionEnd(cursor.selectionEnd()), likely setting end=-1 and inverting selection. |
| opus-ultra | ✅ LEGIT | 85 | inverted selection after failed search (documenthandler.cpp:1574) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

