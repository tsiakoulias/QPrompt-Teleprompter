# [NOTIFY-01] setAutoReload doesn't emit autoReloadChanged NOTIFY signal

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.cpp:909-919, documenthandler.h:120,300`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** documenthandler.cpp:909-919, documenthandler.h:120,300
- **Severity:** Medium
- **Analysis:** Q_PROPERTY declares NOTIFY autoReloadChanged. Signal exists. `setAutoReload()` sets `m_autoReload` but never emits. Every other WRITE method in DocumentHandler emits its NOTIFY — this is the single exception. QML bindings reading `document.autoReload` become stale after any C++ write.
- **Impact:** QML bindings never update when autoReload changed from C++.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 75 | setAutoReload never emits autoReloadChanged (documenthandler.cpp:909) |
| gpt | ✅ LEGIT | 78 | setAutoReload doesn't emit autoReloadChanged NOTIFY signal (src/documenthandler.cpp:909) |
| deepseek | ✅ LEGIT | 95 | setAutoReload at documenthandler.cpp:909 sets m_autoReload but never emits autoReloadChanged |
| glm | ✅ LEGIT | 80 | documenthandler.cpp:909-919 setAutoReload doesn't emit autoReloadChanged NOTIFY signal |
| kimi | ✅ LEGIT | 95 | documenthandler.cpp:909-919 sets m_autoReload but never emits autoReloadChanged despite the Q_PROPERTY NOTIFY declaration. |
| opus-ultra | ✅ LEGIT | 75 | setAutoReload never emits autoReloadChanged (documenthandler.cpp:909) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

