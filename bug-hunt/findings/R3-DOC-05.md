# [R3-DOC-05] updateContents() produces two separate undo entries — undo destroys document

- **Status:** OPEN
- **Severity:** High
- **Category:** Edge Case
- **Location:** `src/documenthandler.cpp:1104-1122`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/documenthandler.cpp:1104-1122
- **Severity:** High
- **Category:** Edge Case
- **Analysis:** No beginEditBlock/endEditBlock wrapping removeSelectedText + insertText/insertHtml. Two independent undo entries created. Undo after file load: only insertion reversed, leaving permanently empty document.
- **Impact:** Undo after file load irreversibly destroys document content.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 85 | updateContents no editblock; undo empties doc (documenthandler.cpp:1104) |
| gpt | ✅ LEGIT | 84 | updateContents() produces two separate undo entries - undo destroys document (src/documenthandler.cpp:1104) |
| deepseek | ✅ LEGIT | 90 | documenthandler.cpp:1104-1122 updateContents has no beginEditBlock/endEditBlock wrapping removeSelectedText+insertText — two undo entries undo destroys doc |
| glm | ✅ LEGIT | 80 | documenthandler.cpp:1104-1122 updateContents does select all + remove + insert; creates separate undo entry |
| kimi | ✅ LEGIT | 80 | documenthandler.cpp:1104-1121 removes all text then inserts new text without an edit block; two undo steps result, leaving an empty-document intermediate on first undo. |
| opus-ultra | ✅ LEGIT | 85 | updateContents no editblock; undo empties doc (documenthandler.cpp:1104) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

