# [HK-N03] platformName() != "wayland" fails on "wayland-egl" — global hotkeys dead

- **Status:** OPEN
- **Severity:** High
- **Category:** 
- **Location:** `globalhotkeys.cpp:16 sites`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** globalhotkeys.cpp:16 sites
- **Severity:** High
- **Analysis:** Qt reports "wayland-egl" on Wayland with EGL backend. `!= "wayland"` passes → QHotkey shortcuts zeroed AND KGlobalAccel defaults zeroed. Zero global hotkeys on Wayland-EGL.
- **Impact:** All global hotkeys non-functional on Wayland-EGL compositors.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | platformName()!='wayland' could miss 'wayland-egl'; Qt usually reports 'wayland' (globalhotkeys.cpp) |
| gpt | ⚠️ PARTIAL | 58 | observed platformName() != "wayland" fails on "wayland-egl" - global hotkeys dead (src/globalhotkeys.cpp:822) |
| deepseek | ✅ LEGIT | 90 | platform!='wayland' at globalhotkeys.cpp:119 fails on 'wayland-egl' — all global hotkeys dead |
| glm | ⚠️ PARTIAL | 65 | globalhotkeys.cpp platformName()!='wayland' fails on 'wayland-egl'; but this is for QHotkey which doesn't support Wayland anyway |
| kimi | ✅ LEGIT | 90 | globalhotkeys.cpp ~16 sites compare platformName() != 'wayland'; on wayland-egl QHotkey path runs and KGlobalAccel is bypassed, breaking global hotkeys |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — platformName()!='wayland' could miss 'wayland-egl'; Qt usually reports 'wayland' (globalho |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

