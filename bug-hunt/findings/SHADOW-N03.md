# [SHADOW-N03] id: stopwatch shadows property bool stopwatch — timersEnabled always true

- **Status:** OPEN
- **Severity:** High
- **Category:** 
- **Location:** `TimerClock.qml:38,122,100`
- **Consensus:** 5/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** TimerClock.qml:38,122,100
- **Severity:** High
- **Analysis:** `id: stopwatch` (Item child) shadows `property bool stopwatch: true` in same scope. Line 100 `timersEnabled: enabled && (stopwatch || eta)` — bare `stopwatch` resolves to Item (always truthy), never to bool. timersEnabled always returns `enabled && true`, permanently ignoring both stopwatch and eta toggles.
- **Impact:** 9 consumers of viewport.timer.timersEnabled across main.qml, +windows, +android, PrompterPage ALL receive wrong values. Timer display always enabled regardless of toggles.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 70 | id: stopwatch (Item) shadows property bool stopwatch -> timersEnabled always true (TimerClock.qml:38) |
| gpt | ✅ LEGIT | 84 | id: stopwatch shadows property bool stopwatch - timersEnabled always true (src/prompter/TimerClock.qml:38) |
| deepseek | ❌ FALSE | 75 | property bool stopwatch resolves before child Item id; timersEnabled correctly depends on property (TimerClock.qml:38 100 122) |
| glm | ✅ LEGIT | 75 | TimerClock.qml:38 122 100 id: stopwatch shadows property bool stopwatch; timersEnabled always true |
| kimi | ✅ LEGIT | 95 | TimerClock.qml:122 id stopwatch shadows property bool stopwatch; line 100 stopwatch\|\|eta resolves to Item (truthy), ignoring toggles. |
| opus-ultra | ✅ LEGIT | 70 | id: stopwatch (Item) shadows property bool stopwatch -> timersEnabled always true (TimerClock.qml:38) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

