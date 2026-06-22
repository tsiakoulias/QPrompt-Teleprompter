# [R2-OVL-02] LanguageSettingsOverlay popup ListView currentIndex always resolves to -1

- **Status:** OPEN
- **Severity:** Low
- **Category:** Logic
- **Location:** `src/kirigami_ui/LanguageSettingsOverlay.qml:73`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** src/kirigami_ui/LanguageSettingsOverlay.qml:73
- **Severity:** Low
- **Category:** Logic
- **Analysis:** `currentIndex: languageSelector.model.indexOf(languageSelector.currentIndex)` — model is array of objects `{text, value}`, searched for an integer. Always returns -1. Compare with LayoutDirectionSettingsOverlay:76 which correctly uses `layoutSelector.currentIndex` directly.
- **Impact:** Currently selected language never highlighted in popup list. Keyboard navigation may not start from correct position.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 85 | popup currentIndex indexOf(int) over object array -> -1 (LanguageSettingsOverlay.qml:73) |
| gpt | ✅ LEGIT | 78 | LanguageSettingsOverlay popup ListView currentIndex always resolves to -1 (src/kirigami_ui/LanguageSettingsOverlay.qml:73) |
| deepseek | ❔ UNSURE | 35 | ListView currentIndex=-1 at LanguageSettingsOverlay.qml:73 — need to verify model structure and indexOf semantics |
| glm | ✅ LEGIT | 80 | LanguageSettingsOverlay.qml:73 ListView currentIndex uses indexOf which returns -1 when not found; always -1 |
| kimi | ✅ LEGIT | 80 | LanguageSettingsOverlay.qml:73 indexOf(integer) on model array of objects always returns -1. |
| opus-ultra | ✅ LEGIT | 85 | popup currentIndex indexOf(int) over object array -> -1 (LanguageSettingsOverlay.qml:73) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

