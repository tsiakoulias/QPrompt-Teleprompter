# [R2-PTR-03] Casing error: Units.longDuration should be Units.LongDuration

- **Status:** OPEN
- **Severity:** Medium
- **Category:** Logic
- **Location:** `src/prompter/ProjectionsManager.qml:329`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** src/prompter/ProjectionsManager.qml:329
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** All other animations use PascalCase (`Units.ShortDuration`, `Units.VeryLongDuration`). This is the only active use of lowercase `Units.longDuration`. QML property access is case-sensitive; resolves to undefined.
- **Impact:** Projection window button grid opacity animation gets `duration: undefined`, snaps to 20% opacity instantly instead of fading smoothly.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 80 | Units.longDuration casing (ProjectionsManager.qml:329) |
| gpt | ✅ LEGIT | 78 | Casing error: Units.longDuration should be Units.LongDuration (src/prompter/ProjectionsManager.qml:329) |
| deepseek | ❔ UNSURE | 40 | Units.longDuration lowercase vs LongDuration at ProjectionsManager.qml:329; depends on Kirigami Units property case — need API reference |
| glm | ✅ LEGIT | 85 | ProjectionsManager.qml:329 Units.longDuration should be Units.LongDuration; casing error |
| kimi | ✅ LEGIT | 85 | ProjectionsManager.qml:329 uses Units.longDuration (lowercase) and file does not import Kirigami; undefined. |
| opus-ultra | ✅ LEGIT | 80 | Units.longDuration casing (ProjectionsManager.qml:329) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

