# [R3-MAIN-07] XDG_CURRENT_DESKTOP unconditionally forced to "KDE" on all Linux

- **Status:** OPEN
- **Severity:** Medium
- **Category:** Platform/Build
- **Location:** `src/main.cpp:86-87`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/main.cpp:86-87
- **Severity:** Medium
- **Category:** Platform/Build
- **Analysis:** qputenv("XDG_CURRENT_DESKTOP", "KDE") on every Linux system regardless of actual desktop. Qt picks KDE platform theme, icon theme, font rendering.
- **Impact:** On GNOME/XFCE/Sway: blank icons if Breeze not installed, visual clash with native desktop, wrong widget styling.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 90 | XDG_CURRENT_DESKTOP=KDE forced all Linux (main.cpp:86) |
| gpt | ✅ LEGIT | 78 | XDG_CURRENT_DESKTOP unconditionally forced to "KDE" on all Linux (src/main.cpp:86) |
| deepseek | ✅ LEGIT | 98 | main.cpp:86-87 qputenv('XDG_CURRENT_DESKTOP' 'KDE') unconditional on ALL Linux — breaks GNOME/XFCE/Sway icon themes and widget styling |
| glm | ✅ LEGIT | 85 | main.cpp:86-87 XDG_CURRENT_DESKTOP unconditionally set to KDE on all Linux including GNOME/XFCE |
| kimi | ✅ LEGIT | 80 | main.cpp:86-87 unconditionally sets XDG_CURRENT_DESKTOP=KDE on every Linux build, overriding the user actual desktop session. |
| opus-ultra | ✅ LEGIT | 90 | XDG_CURRENT_DESKTOP=KDE forced all Linux (main.cpp:86) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

