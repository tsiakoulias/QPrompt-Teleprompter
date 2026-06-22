# [FONT-N01] font.family: "Monospace" never resolves — no such font on any OS

- **Status:** REJECTED
- **Severity:** Medium
- **Category:** 
- **Location:** `TimerClock.qml:149,161`
- **Consensus:** 3/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** TimerClock.qml:149,161
- **Severity:** Medium
- **Analysis:** `font.family: "Monospace"` does case-insensitive exact matching. No font named "Monospace" ships on any platform. Should be `font.families: ["monospace"]` (lowercase, plural) — the only API resolving CSS generic family names.
- **Impact:** Timer stopwatch/ETA uses proportional fallback. Digit widths vary, causing visible layout jitter as time increments.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | 'Monospace' resolves via Qt font matching on most OS (TimerClock.qml:149) |
| gpt | ❔ UNSURE | 39 | runtime/platform behavior is not decidable from the cited snippet (src/prompter/TimerClock.qml:149) |
| deepseek | ✅ LEGIT | 95 | TimerClock.qml:149/161: font.family:'Monospace' does exact case-insensitive matching; no font named Monospace on any OS — should use families:['monospace'] for CSS generic resolution |
| glm | ✅ LEGIT | 75 | TimerClock.qml:149 161 font.family 'Monospace' is a generic family; may not resolve to actual font |
| kimi | ✅ LEGIT | 70 | TimerClock.qml:149 |
| opus-ultra | ❌ FALSE | 72 | max: code correct / claim mischaracterized — 'Monospace' resolves via Qt font matching on most OS (TimerClock.qml:149) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

