# [RENDER-02] ShaderEffectSource pointerShadowSource runs unconditionally — same pattern

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `ReadRegionOverlay.qml:123-126`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** ReadRegionOverlay.qml:123-126
- **Severity:** Medium
- **Analysis:** Identical to RENDER-01. Always captures readRegion to texture. Downstream shadow on readRegion gated by `layer.enabled`, but source never stops when shadows off.
- **Impact:** Wasted texture capture every frame when shadows disabled.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | pointerShadowSource runs unconditionally (ReadRegionOverlay.qml:123) |
| gpt | ✅ LEGIT | 78 | ShaderEffectSource pointerShadowSource runs unconditionally - same pattern (src/prompter/ReadRegionOverlay.qml:123) |
| deepseek | ✅ LEGIT | 70 | pointerShadowSource ShaderEffectSource captures unconditionally (ReadRegionOverlay.qml:123-126) |
| glm | ✅ LEGIT | 75 | ReadRegionOverlay.qml:123-126 pointerShadowSource ShaderEffectSource runs unconditionally |
| kimi | ✅ LEGIT | 80 | ReadRegionOverlay.qml:123-126 instantiates pointerShadowSource with default live=true and no guard; the shadow effect at line 145 is gated by layer.enabled only. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — pointerShadowSource runs unconditionally (ReadRegionOverlay.qml:123) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

