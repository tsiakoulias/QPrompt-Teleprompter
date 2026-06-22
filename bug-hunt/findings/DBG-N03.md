# [DBG-N03] Latent debug state leak: pointers/debug Setting persists Guides checkbox

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `PointerSettings.qml:94, ReadRegionOverlay.qml:239`
- **Consensus:** 1/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** PointerSettings.qml:94, ReadRegionOverlay.qml:239
- **Severity:** Low
- **Analysis:** After QML-01 fixed, users who checked "Guides" will see red debug rectangles appear with no way to disable (cross-file reference still broken).
- **Impact:** Debug rectangles appear in production after fixing QML-01.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | debug Setting persists Guides checkbox (PointerSettings.qml:94) |
| gpt | ⚠️ PARTIAL | 52 | observed Latent debug state leak: pointers/debug Setting persists Guides checkbox (src/prompter/PointerSettings.qml:94) |
| deepseek | ⚠️ PARTIAL | 60 | PointerSettings.qml:94: debug alias persists; ReadRegionOverlay.qml:239 binding uses !pointerSettings.debug but cross-file reference may be broken after QML-01 fix — depends on other bug status |
| glm | ⚠️ PARTIAL | 60 | PointerSettings.qml:94 ReadRegionOverlay.qml:239 latent debug state leak; pointers/debug Setting persists |
| kimi | ❌ FALSE | 60 | PointerSettings.qml:94 persists debug, but ReadRegionOverlay.qml:239 currently cannot resolve pointerSettings (QML-01), so no production effect. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — debug Setting persists Guides checkbox (PointerSettings.qml:94) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

