# [HTK-06] Pause (Ctrl+Space) and Stop (Meta+Space) conflict — Meta+Space captured by OS

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `globalhotkeys.cpp:581,586`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** globalhotkeys.cpp:581,586
- **Severity:** Medium
- **Analysis:** Stop uses Meta/Win+Space. On Windows (Start menu), GNOME (input source), macOS (Spotlight) — captured by OS. Never reaches QPrompt.
- **Impact:** Stop hotkey non-functional by default on all 3 major platforms.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | Ctrl/Meta+Space shortcut OS-conflict; environment (globalhotkeys.cpp:581) |
| gpt | ⚠️ PARTIAL | 58 | observed Pause (Ctrl+Space) and Stop (Meta+Space) conflict - Meta+Space captured by OS (src/globalhotkeys.cpp:581) |
| deepseek | ✅ LEGIT | 90 | Stop uses Meta/Win+Space captured by Windows Start Menu/GNOME/macOS Spotlight (globalhotkeys.cpp:581 586) |
| glm | ✅ LEGIT | 80 | globalhotkeys.cpp:581 586 Pause=Ctrl+Space and Stop=Meta+Space; Meta+Space captured by OS on many platforms |
| kimi | ✅ LEGIT | 85 | globalhotkeys.cpp:581/586 default Stop shortcut is Meta+Space, captured by Windows Start/GNOME input/macOS Spotlight. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — Ctrl/Meta+Space shortcut OS-conflict; environment (globalhotkeys.cpp:581) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

