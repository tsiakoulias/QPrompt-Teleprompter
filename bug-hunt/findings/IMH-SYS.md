# [IMH-SYS] Systemic absence of inputMethodHints on ALL TextFields (16 sites)

- **Status:** REJECTED
- **Severity:** Medium
- **Category:** 
- **Location:** `EditorToolbar.qml (10 numeric TextFields), PrompterPage.qml (openUrl, wsUrlField, markerHrefField), PathsPage.qml (sofficePathField), PointerSettings.qml (3 color hex, 4 path TextFields), Find.qml (replaceField)`
- **Consensus:** 2/6 agents LEGIT · CONFLICT

## Original report claim

- **Files:** EditorToolbar.qml (10 numeric TextFields), PrompterPage.qml (openUrl, wsUrlField, markerHrefField), PathsPage.qml (sofficePathField), PointerSettings.qml (3 color hex, 4 path TextFields), Find.qml (replaceField)
- **Severity:** Medium
- **Analysis:** Zero `inputMethodHints` set on any TextField. No `ImhFormattedNumbersOnly` on 10 numeric fields, no `ImhUrlCharactersOnly` on URL/path fields, no `ImhNoAutoUppercase` on dictionary word field, no `ImhNoPredictiveText` on replace field.
- **Impact:** Full QWERTY with auto-correct/auto-cap on all mobile fields. Numeric fields get wrong keyboard. URLs get auto-correct corruption. Dictionary words get forced capitalization. Paths get predictive text mangling.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 40 | no inputMethodHints on TextFields = ImhNone default; IME still works (EditorToolbar.qml) |
| gpt | ⚠️ PARTIAL | 58 | observed Systemic absence of inputMethodHints on ALL TextFields (16 sites) (src/kirigami_ui/EditorToolbar.qml:1) |
| deepseek | ⚠️ PARTIAL | 65 | IMH-SYS: systemic absence of inputMethodHints on TextFields is a mobile UX concern but design choice not bug; not all 16 sites individually verified |
| glm | ✅ LEGIT | 75 | 16+ TextFields across EditorToolbar.qml PrompterPage.qml PathsPage.qml PointerSettings.qml Find.qml have no inputMethodHints |
| kimi | ✅ LEGIT | 95 | No inputMethodHints anywhere in src QML; numeric/URL TextFields lack proper IME hints. |
| opus-ultra | ❌ FALSE | 72 | max: code correct / claim mischaracterized — no inputMethodHints on TextFields = ImhNone default; IME still works (EditorToolbar.qml) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

