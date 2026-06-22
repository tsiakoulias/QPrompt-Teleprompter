# [SAVE-N02] iOS save flow never updates C++ m_fileUrl — file URL perpetually stale

- **Status:** OPEN
- **Severity:** High
- **Category:** 
- **Location:** `Prompter.qml:2493-2506, iossavedialog.mm:36-46`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** Prompter.qml:2493-2506, iossavedialog.mm:36-46
- **Severity:** High
- **Analysis:** iOS saves entirely outside C++ DocumentHandler. accepted(fileUrl) received in QML but never calls `document.saveAs(fileUrl)`. fileUrl is READ-only Q_PROPERTY (no WRITE). Can't update m_fileUrl. editor.lastDocument records stale URL.
- **Impact:** After iOS save, Ctrl+S/auto-save writes to wrong location. Title bar and recent docs show wrong URL.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | iOS onAccepted doesn't refresh C++ m_fileUrl; domain (Prompter.qml:2493) |
| gpt | ✅ LEGIT | 84 | iOS save flow never updates C++ m_fileUrl - file URL perpetually stale (src/prompter/Prompter.qml:2493) |
| deepseek | ✅ LEGIT | 75 | iOS save flow in QML never calls C++ method to update m_fileUrl (Prompter.qml:2493-2506) |
| glm | ✅ LEGIT | 80 | Prompter.qml:2493-2506 iOS save flow never updates C++ m_fileUrl; file URL perpetually stale |
| kimi | ✅ LEGIT | 85 | iOS save Connections onAccepted (Prompter.qml:2493-2506) never assigns the returned fileUrl back to document; m_fileUrl stays stale. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — iOS onAccepted doesn't refresh C++ m_fileUrl; domain (Prompter.qml:2493) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

