# [QTD-01] m_spellHighlighter not detached when setDocument(nullptr)

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.cpp:183-199`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** documenthandler.cpp:183-199
- **Severity:** Medium
- **Analysis:** m_spellHighlighter.reset() inside if(m_document) block. When new doc is nullptr, old highlighter remains attached to orphaned QTextDocument. Document destroyed → highlighter holds dangling pointer → use-after-free at DocumentHandler destructor.
- **Impact:** Use-after-free on QTextDocument/SpellHighlighter cleanup.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 65 | m_spellHighlighter.reset() inside if(m_document); skipped on setDocument(nullptr) (documenthandler.cpp:193) |
| gpt | ✅ LEGIT | 78 | mspellHighlighter not detached when setDocument(nullptr) (src/documenthandler.cpp:183) |
| deepseek | ✅ LEGIT | 85 | m_spellHighlighter.reset() inside if(m_document) block at documenthandler.cpp:193 — not detached on nullptr |
| glm | ✅ LEGIT | 80 | documenthandler.cpp:183-199 m_spellHighlighter not detached when setDocument(nullptr); old document pointer retained |
| kimi | ✅ LEGIT | 85 | documenthandler.cpp:183-199 resets m_spellHighlighter only inside if(m_document); setDocument(nullptr) leaves old highlighter attached to orphaned doc. |
| opus-ultra | ✅ LEGIT | 65 | m_spellHighlighter.reset() inside if(m_document); skipped on setDocument(nullptr) (documenthandler.cpp:193) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

