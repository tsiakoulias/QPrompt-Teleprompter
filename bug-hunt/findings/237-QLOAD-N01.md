# [237-QLOAD-N01] InputsOverlay toggleButtonsOff() null-check bypass — crash on slow async Loaders

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `InputsOverlay.qml:107,564`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** InputsOverlay.qml:107,564
- **Severity:** Medium
- **Analysis:** All 48 Loaders are async. `typeof children[i].item !== "undefined"` passes for null (typeof null === "object"). If one Loader finishes before others, `null.checked = false` throws TypeError crash.
- **Impact:** Crash on first-open of key-configuration overlay on slow systems.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ⚠️ PARTIAL | 50 | toggleButtonsOff null-check bypass on slow async Loader (InputsOverlay.qml:107) |
| gpt-5.5-xhigh | ✅ LEGIT | 78 | InputsOverlay toggleButtonsOff() null-check bypass - crash on slow async Loaders (src/kirigami_ui/InputsOverlay.qml:107) |
| deepseek-v4-pro-max | ✅ LEGIT | 95 | InputsOverlay.qml:107 564: typeof null==='object' bypasses guard; null.checked=false throws TypeError on slow async Loader completion |
| glm-5.2-xhigh | ✅ LEGIT | 75 | InputsOverlay.qml:107 564 toggleButtonsOff() null-check bypass; crash on slow async Loaders |
| kimi-k2.7-code | ✅ LEGIT | 85 | InputsOverlay.qml:107,564 guard `typeof children[i].item !== 'undefined'` passes for null; null.checked TypeError. |
| opus-4.8-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — toggleButtonsOff null-check bypass on slow async Loader (InputsOverlay.qml:107) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

