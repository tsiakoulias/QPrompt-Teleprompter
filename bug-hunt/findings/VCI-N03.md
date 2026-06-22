# [VCI-N03] Hardcoded divider/separator/border colors (#292929, #606060, #808080) break theme adaptation

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `PointerSettings.qml, InputsOverlay.qml, Find.qml, PrompterPage.qml, ProgressIndicator.qml`
- **Consensus:** 2/6 agents LEGIT · split

## Original report claim

- **Files:** PointerSettings.qml, InputsOverlay.qml, Find.qml, PrompterPage.qml, ProgressIndicator.qml
- **Severity:** Low
- **Analysis:** Fixed gray values never adapt to theme. Dark themes render dividers near-invisible; light themes produce harsh dark borders.
- **Impact:** Divider lines invisible on dark themes, jarring on light themes.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 40 | hardcoded divider/border colors break theming (PointerSettings.qml) |
| gpt | ⚠️ PARTIAL | 48 | visual issue is plausible but depends on theme or device (src/prompter/PointerSettings.qml:1) |
| deepseek | ⚠️ PARTIAL | 70 | PointerSettings/InputsOverlay/Find/PrompterPage/ProgressIndicator: hardcoded colors (#292929 at PointerSettings.qml:260 verified); others not all checked but pattern consistent |
| glm | ⚠️ PARTIAL | 55 | PointerSettings.qml etc hardcoded divider/separator/border colors break theme adaptation |
| kimi | ✅ LEGIT | 90 | Hardcoded #292929/#606060/#808080 in PointerSettings.qml:240/260 InputsOverlay.qml:69 Find.qml:83 PrompterPage.qml:817 ProgressIndicator.qml:52 break theme adaptation. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — hardcoded divider/border colors break theming (PointerSettings.qml) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

