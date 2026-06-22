# [BLK-N01] alignment() returns Qt::AlignCenter (includes vertical bit 0x0080) on null cursor

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.cpp:549`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp:549
- **Severity:** Medium
- **Analysis:** Qt::AlignCenter = AlignHCenter | AlignVCenter. AlignVCenter has no meaning in QTextBlockFormat context — only applies to table cells/frames. QTextDocument default is AlignLeft.
- **Impact:** Alignment toolbar shows "centered" with bogus vertical-flag pollution when no document.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 70 | null-cursor returns Qt::AlignCenter incl vertical bit 0x80 (documenthandler.cpp:549) |
| gpt | ⚠️ PARTIAL | 58 | observed alignment() returns Qt::AlignCenter (includes vertical bit 0x0080) on null cursor (src/documenthandler.cpp:549) |
| deepseek | ✅ LEGIT | 85 | documenthandler.cpp:549: alignment() returns Qt::AlignCenter(AlignHCenter\|AlignVCenter) on null cursor; AlignVCenter meaningless for blocks |
| glm | ✅ LEGIT | 70 | documenthandler.cpp:549 alignment() returns Qt::AlignCenter (includes vertical bit 0x0080) on null cursor |
| kimi | ❔ UNSURE | 55 | documenthandler.cpp:548-549 returns Qt::AlignCenter on null cursor; impact depends on whether another default is expected |
| opus-ultra | ✅ LEGIT | 70 | null-cursor returns Qt::AlignCenter incl vertical bit 0x80 (documenthandler.cpp:549) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

