# [MEM-03] Memory Leak: `m_fontDialog` allocated without parent, never deleted

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `src/documenthandler.cpp:148, src/documenthandler.h:347`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/documenthandler.cpp:148, src/documenthandler.h:347
- **Severity:** Medium
- **Code:**
  ```cpp
  m_fontDialog = new SystemFontChooserDialog();   // no parent, no WA_DeleteOnClose
  DocumentHandler::~DocumentHandler() = default;  // no explicit delete
  ```
- **Analysis:** `SystemFontChooserDialog` (QDialog) heap-allocated with no parent and no `WA_DeleteOnClose`. User-closing merely hides it. Default destructor never deletes it.
- **Impact:** Memory leak of dialog and all child widgets on destruction.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 100 | new dialog w/o parent/WA_DeleteOnClose (documenthandler.cpp:148) |
| gpt | ✅ LEGIT | 88 | parentless allocation has no destructor cleanup (src/documenthandler.cpp:148) |
| deepseek | ✅ LEGIT | 85 | m_fontDialog=new SystemFontChooserDialog() w/o parent/doc.cpp:148; no WA_DeleteOnClose; dtor=default leaks dialog |
| glm | ✅ LEGIT | 85 | documenthandler.cpp:148 m_fontDialog=new SystemFontChooserDialog() no parent; default destructor never deletes it (desktop only) |
| kimi | ✅ LEGIT | 90 | documenthandler.cpp:148 allocates m_fontDialog with no parent and no WA_DeleteOnClose; dialog leaks on destruction. |
| opus-ultra | ✅ LEGIT | 100 | new dialog w/o parent/WA_DeleteOnClose (documenthandler.cpp:148) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

