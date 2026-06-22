# [BLK-N03] setLineHeight/setParagraphHeight apply document-wide — destroy per-block customization

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.cpp:1597,1611`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp:1597,1611
- **Severity:** Medium
- **Analysis:** Both select entire document and merge block format to ALL blocks. Every other formatting setter respects selection scope. These two force destructive global scope.
- **Impact:** Any per-block line-height or paragraph-spacing customization silently destroyed. Names suggest property setters but behavior is document-level overwrite.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 60 | setLineHeight/setParagraphHeight select Document -> apply to all blocks (documenthandler.cpp:1597) |
| gpt | ⚠️ PARTIAL | 58 | observed setLineHeight/setParagraphHeight apply document-wide - destroy per-block customization (src/documenthandler.cpp:1597) |
| deepseek | ✅ LEGIT | 90 | documenthandler.cpp:1597 1611: setLineHeight/setParagraphHeight select entire document via cursor.select(Document); destroy per-block customization |
| glm | ✅ LEGIT | 70 | documenthandler.cpp:1597 1611 setLineHeight/setParagraphHeight apply document-wide; destroy per-block customization |
| kimi | ✅ LEGIT | 90 | documenthandler.cpp:1597/1611 select the whole document then mergeBlockFormat, applying height to all blocks |
| opus-ultra | ✅ LEGIT | 60 | setLineHeight/setParagraphHeight select Document -> apply to all blocks (documenthandler.cpp:1597) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

