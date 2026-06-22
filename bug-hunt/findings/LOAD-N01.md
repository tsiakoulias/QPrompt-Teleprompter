# [LOAD-N01] TOCTOU race between QFile::exists() and file.open() in load()

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.cpp:944-947`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp:944-947
- **Severity:** Medium
- **Analysis:** File can be deleted/replaced between exists() check and open() call. If vanishes: open fails, content block skipped, but m_fileUrl set and fileUrlChanged emitted anyway. clearUndoRedoStacks() called despite nothing loaded. No error emitted.
- **Impact:** Silent empty document with wrong file URL after race. Undo history lost for no reason.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | TOCTOU between exists() and open(); minor for desktop (documenthandler.cpp:944) |
| gpt | ✅ LEGIT | 78 | TOCTOU race between QFile::exists() and file.open() in load() (src/documenthandler.cpp:944) |
| deepseek | ✅ LEGIT | 65 | classic TOCTOU race between QFile::exists and file.open (documenthandler.cpp:944-947) |
| glm | ✅ LEGIT | 75 | documenthandler.cpp:944-947 TOCTOU race between QFile::exists() and file.open() in load() |
| kimi | ✅ LEGIT | 70 | load() checks QFile::exists at documenthandler.cpp:944 before opening at :947; file can vanish between check and open. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — TOCTOU between exists() and open(); minor for desktop (documenthandler.cpp:944) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

