# [MEM-02] Memory Leak: `_fileSystemWatcher` allocated without parent, never deleted

- **Status:** OPEN
- **Severity:** High
- **Category:** 
- **Location:** `src/documenthandler.cpp:140, src/documenthandler.h:344`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/documenthandler.cpp:140, src/documenthandler.h:344
- **Severity:** High
- **Code:**
  ```cpp
  _fileSystemWatcher = new QFileSystemWatcher();   // no parent
  DocumentHandler::~DocumentHandler() = default;   // no explicit delete
  ```
- **Analysis:** Identical pattern to MEM-01. `QFileSystemWatcher` (QObject) heap-allocated, no parent, never deleted.
- **Impact:** Memory leak on every `DocumentHandler` destruction.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 100 | new QFileSystemWatcher w/o parent (documenthandler.cpp:140) |
| gpt | ✅ LEGIT | 88 | parentless allocation has no destructor cleanup (src/documenthandler.cpp:140) |
| deepseek | ✅ LEGIT | 90 | _fileSystemWatcher=new QFileSystemWatcher() w/o parent at doc.cpp:140; same default dtor — confirmed leak |
| glm | ✅ LEGIT | 90 | documenthandler.cpp:140 _fileSystemWatcher=new QFileSystemWatcher() no parent; default destructor at :160 never deletes it |
| kimi | ✅ LEGIT | 95 | documenthandler.cpp:140 allocates _fileSystemWatcher without parent; default destructor never deletes it. |
| opus-ultra | ✅ LEGIT | 100 | new QFileSystemWatcher w/o parent (documenthandler.cpp:140) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

