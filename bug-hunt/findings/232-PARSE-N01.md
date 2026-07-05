# [232-PARSE-N01] insertImageAt() stores image resource with file:// key but looks up via plain path

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.cpp:1766-1769`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp:1766-1769
- **Severity:** Medium
- **Analysis:** `addResource(ImageResource, imageUrl, image)` uses full file:// QUrl. `imageFormat.setName(imageUrl.toLocalFile())` stores plain path. Later `imageAt()`/`imageRect()` lookup via `QUrl(imgFmt.name())` misses because plain-path QUrl != file:// QUrl. Remote image path (line 1753) correctly uses `.toString()` for both.
- **Impact:** Image dimension retrieval broken for locally inserted images (drag-and-drop from filesystem).

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ⚠️ PARTIAL | 50 | image resource keyed by QUrl but format name=path string; possible mismatch (documenthandler.cpp:1766) |
| gpt-5.5-xhigh | ✅ LEGIT | 78 | insertImageAt() stores image resource with file:// key but looks up via plain path (src/documenthandler.cpp:1766) |
| deepseek-v4-pro-max | ✅ LEGIT | 85 | addResource with file:// QUrl at documenthandler.cpp:1766 but imageFormat.setName uses plain path at 1769 |
| glm-5.2-xhigh | ✅ LEGIT | 80 | documenthandler.cpp:1766-1769 insertImageAt stores image resource with file:// key but looks up via plain path |
| kimi-k2.7-code | ✅ LEGIT | 95 | documenthandler.cpp:1766-1769 stores local image under file:// key but sets imageFormat.name to toLocalFile(); imageAt/imageRect lookup via QUrl(name) misses |
| opus-4.8-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — image resource keyed by QUrl but format name=path string; possible mismatch (documenthandl |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

