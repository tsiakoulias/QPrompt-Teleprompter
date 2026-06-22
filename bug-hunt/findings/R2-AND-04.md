# [R2-AND-04] Android Settings for "background" missing transparency persistence

- **Status:** OPEN
- **Severity:** Low
- **Category:** Platform/Build
- **Location:** `src/kirigami_ui/+android/main.qml:96-100`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** src/kirigami_ui/+android/main.qml:96-100
- **Severity:** Low
- **Category:** Platform/Build
- **Analysis:** "background" Settings persists opacity/shadows but missing `property alias transparency: root.__translucidBackground` (present in Windows line 108, base line 113). Consistent with Android hardcoding transparency as readonly, but forward-compat issue.
- **Impact:** No current user-facing impact (menu item absent). Future issue if transparency toggle enabled.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | +android background Settings missing transparency alias; no current impact (main.qml:96) |
| gpt | ⚠️ PARTIAL | 58 | observed Android Settings for "background" missing transparency persistence (src/kirigami_ui/+android/main.qml:96) |
| deepseek | ❔ UNSURE | 30 | Android transparency persistence — future compat issue minimal current impact |
| glm | ✅ LEGIT | 75 | +android/main.qml:96-100 background Settings missing transparency alias present in base |
| kimi | ✅ LEGIT | 70 | +android/main.qml:96-100 background Settings lacks transparency alias present in base/windows variants. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — +android background Settings missing transparency alias; no current impact (main.qml:96) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

