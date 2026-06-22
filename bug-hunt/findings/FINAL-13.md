# [FINAL-13] Invalid Korean locale code "ko_KO" — should be "ko_KR"

- **Status:** OPEN
- **Severity:** Medium
- **Category:** I18N
- **Location:** `src/kirigami_ui/LanguageSettingsOverlay.qml:127`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/kirigami_ui/LanguageSettingsOverlay.qml:127
- **Severity:** Medium
- **Category:** I18N
- **Analysis:** "KO" is not valid ISO 3166-1 (South Korea = KR). Translation file won't match.
- **Impact:** Korean users get no translation — silently falls back to English.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 90 | ko_KO should be ko_KR (LanguageSettingsOverlay.qml:127) |
| gpt | ✅ LEGIT | 92 | Invalid Korean locale code "koKO" - should be "koKR" (src/kirigami_ui/LanguageSettingsOverlay.qml:127) |
| deepseek | ✅ LEGIT | 95 | LanguageSettingsOverlay.qml:127 'ko_KO' — ISO 3166-1 for South Korea is KR not KO; Korean translation file never matches |
| glm | ✅ LEGIT | 90 | LanguageSettingsOverlay.qml:127 uses 'ko_KO' which is invalid; should be 'ko_KR' |
| kimi | ✅ LEGIT | 95 | LanguageSettingsOverlay.qml:127 uses locale value ko_KO; valid Korean locale is ko_KR, so translation loading fails. |
| opus-ultra | ✅ LEGIT | 90 | ko_KO should be ko_KR (LanguageSettingsOverlay.qml:127) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

