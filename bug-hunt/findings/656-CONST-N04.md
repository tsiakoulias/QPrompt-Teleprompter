# [656-CONST-N04] GlobalHotkeys::globalShortcutKey(Action) not const — Q_INVOKABLE pure query

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `globalhotkeys.h:147, globalhotkeys.cpp:108`
- **Consensus:** 2/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** globalhotkeys.h:147, globalhotkeys.cpp:108
- **Severity:** Low
- **Analysis:** Queries QHotkey::shortcut() (const) and KGlobalAccel::shortcut() (const). No mutation. Called from QML via AppController.
- **Impact:** Blocks const-correct usage.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 40 | globalShortcutKey not const; Q_INVOKABLE query (globalhotkeys.h:147) |
| gpt | ⚠️ PARTIAL | 58 | observed GlobalHotkeys::globalShortcutKey(Action) not const - Q_INVOKABLE pure query (src/globalhotkeys.h:147) |
| deepseek | ✅ LEGIT | 60 | Q_INVOKABLE globalShortcutKey pure query method missing const (globalhotkeys.cpp:108) |
| glm | ✅ LEGIT | 70 | globalhotkeys.h:147 108 globalShortcutKey not const; Q_INVOKABLE pure query |
| kimi | ❌ FALSE | 70 | globalShortcutKey() is a query method without const; this is a style issue, not a functional defect. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — globalShortcutKey not const; Q_INVOKABLE query (globalhotkeys.h:147) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

