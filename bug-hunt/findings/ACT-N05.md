# [ACT-N05] +windows main.qml Controls Settings submenu missing OBS Settings action

- **Status:** NEEDS-INFO
- **Severity:** Medium
- **Category:** 
- **Location:** `+windows/main.qml vs main.qml:261-270`
- **Consensus:** 2/6 agents LEGIT · split

## Original report claim

- **File:** +windows/main.qml vs main.qml:261-270
- **Severity:** Medium
- **Analysis:** Base main.qml includes OBS Settings in Controls Settings. +windows omits it. Since +windows has no Labs.MenuBar (dead code per IMP-N01), Windows users have zero menu access to OBS configuration.
- **Impact:** Windows users cannot reach OBS WebSocket settings.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❔ UNSURE | 45 | +windows Controls submenu missing OBS Settings action; menu-specific (main.qml:261) |
| gpt | ⚠️ PARTIAL | 58 | observed +windows main.qml Controls Settings submenu missing OBS Settings action (src/kirigami_ui/main.qml:261) |
| deepseek | ⚠️ PARTIAL | 45 | missing OBS Settings action in +windows may be intentional per-platform feature gating |
| glm | ✅ LEGIT | 80 | +windows/main.qml Controls Settings submenu missing OBS Settings action present in base main.qml:261-270 |
| kimi | ✅ LEGIT | 85 | base main.qml:261-270 adds an OBS Settings action in Controls Settings; +windows/main.qml:244-298 Controls Settings omits it and +windows has no Labs.MenuBar. |
| opus-ultra | ❔ UNSURE | 45 | max: unverifiable statically (runtime/semantic) — +windows Controls submenu missing OBS Settings action; menu-specific (main.qml:261) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

