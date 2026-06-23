# [020-AND-HIGH-02] Android screen never sleeps after prompter use

- **Status:** OPEN
- **Severity:** High
- **Category:** 
- **Location:** `Prompter.qml:465`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** Prompter.qml:465
- **Severity:** High
- **Analysis:** `document.preventSleep(false)` on entering Editing is commented out. `preventSleep(true)` active for Prompting/Standby/Countdown. Combined with `keepScreenOn="true"`, screen stays on permanently after first session.
- **Impact:** Severe battery drain — screen never times out after using prompter once.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 60 | preventSleep(false) commented out at stop -> Android screen stays awake (Prompter.qml:465) |
| gpt | ✅ LEGIT | 84 | Android screen never sleeps after prompter use (src/prompter/Prompter.qml:465) |
| deepseek | ✅ LEGIT | 90 | Prompter.qml:465: document.preventSleep(false) commented out; only preventSleep(true) active + AndroidManifest.xml:24 keepScreenOn=true — screen never times out after prompter |
| glm | ✅ LEGIT | 80 | Prompter.qml:465 Android screen never sleeps after prompter use; preventSleep not implemented for Android |
| kimi | ✅ LEGIT | 90 | Prompter.qml:465 preventSleep(false) is commented; combined with keepScreenOn screen never sleeps. |
| opus-ultra | ✅ LEGIT | 60 | preventSleep(false) commented out at stop -> Android screen stays awake (Prompter.qml:465) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

