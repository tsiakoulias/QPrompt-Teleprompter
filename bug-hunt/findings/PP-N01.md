# [PP-N01] Q_OS_APPLE is not a Qt macro — KGlobalAccel block compiles on all Unix including macOS

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `globalhotkeys.cpp:26`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** globalhotkeys.cpp:26
- **Severity:** Medium
- **Analysis:** `!defined(Q_OS_APPLE)` — Qt does not define Q_OS_APPLE. Correct macro is Q_OS_DARWIN. Since never defined, `!defined(Q_OS_APPLE)` always true. KGlobalAccel include and macro compiled on all Unix platforms — macOS, FreeBSD, etc. — contrary to "KDE Plasma only" intent.
- **Impact:** On macOS with KF6 via Homebrew, enables KDE global shortcut infrastructure on non-KDE platform. Hard compile error if KF6 unavailable.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 55 | Q_OS_APPLE not a Qt macro; should be Q_OS_DARWIN/defined check (globalhotkeys.cpp:26) |
| gpt | ⚠️ PARTIAL | 58 | observed Q_OS_APPLE is not a Qt macro - KGlobalAccel block compiles on all Unix including macOS (src/globalhotkeys.cpp:26) |
| deepseek | ✅ LEGIT | 95 | globalhotkeys.cpp:26: Q_OS_APPLE not defined by Qt (correct macro: Q_OS_DARWIN); !defined always true; KGlobalAccel compiles on all Unix |
| glm | ✅ LEGIT | 75 | globalhotkeys.cpp:26 Q_OS_APPLE is not a Qt macro; KGlobalAccel block compiles on all Unix including macOS |
| kimi | ✅ LEGIT | 95 | globalhotkeys.cpp:26 uses !defined(Q_OS_APPLE); Q_OS_APPLE is not a Qt macro so the guard is always true |
| opus-ultra | ✅ LEGIT | 55 | Q_OS_APPLE not a Qt macro; should be Q_OS_DARWIN/defined check (globalhotkeys.cpp:26) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

