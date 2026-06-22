# [SET-01] macOS/iOS: QSettings split across two preference domains

- **Status:** OPEN
- **Severity:** High
- **Category:** 
- **Location:** `documenthandler.cpp, globalhotkeys.cpp`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **Files:** documenthandler.cpp, globalhotkeys.cpp
- **Severity:** High
- **Analysis:** C++ uses `QSettings(organizationDomain(), applicationName())` → domain `com.cuperino.qprompt`. QML Settings and default `QSettings()` → domain `Cuperino/qprompt`. Two separate preference files on macOS/iOS. C++ keys (autoReload, hotkeys, paths) stored in different domain than QML keys (background, prompter, scroll, editor, etc.).
- **Impact:** Settings written by C++ invisible to QML and vice versa.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | macOS/iOS QSettings uses different domain combo but consistent within platform |
| gpt | ✅ LEGIT | 84 | macOS/iOS: QSettings split across two preference domains (src/documenthandler.cpp:132) |
| deepseek | ✅ LEGIT | 90 | C++ QSettings uses organizationDomain() (com.cuperino.qprompt) QML uses default (Cuperino/qprompt) — split domains |
| glm | ⚠️ PARTIAL | 65 | documenthandler.cpp globalhotkeys.cpp macOS/iOS QSettings split across organizationDomain vs organizationName |
| kimi | ✅ LEGIT | 90 | main.cpp sets orgDomain=com.cuperino.qprompt; C++ uses organizationDomain on macOS/iOS while QML Settings use organizationName, splitting domains. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — macOS/iOS QSettings uses different domain combo but consistent within platform |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

