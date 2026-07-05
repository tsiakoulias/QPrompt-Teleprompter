# [661-EKA-SYS] Systemic absence of EnterKeyAction on ALL TextFields (7 sites)

- **Status:** REJECTED
- **Severity:** Low
- **Category:** 
- **Location:** `PrompterPage.qml (openUrl, wsUrlField, markerHrefField, newWordField), Find.qml (searchField, replaceField), PathsPage.qml (sofficePathField)`
- **Consensus:** 2/6 agents LEGIT · CONFLICT

## Original report claim

- **Files:** PrompterPage.qml (openUrl, wsUrlField, markerHrefField, newWordField), Find.qml (searchField, replaceField), PathsPage.qml (sofficePathField)
- **Severity:** Low
- **Analysis:** Fields with onAccepted/onEditingFinished/ReturnPressed handlers lack EnterKeyAction. Virtual keyboard shows default "Return" instead of contextual "Go"/"Search"/"Done".
- **Impact:** Mobile keyboard enter-key label wrong — no visual cue for action. 10 EditorToolbar numeric fields also affected.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ⚠️ PARTIAL | 40 | no EnterKeyAction on TextFields; minor UX (PrompterPage.qml) |
| gpt-5.5-xhigh | ⚠️ PARTIAL | 58 | observed Systemic absence of EnterKeyAction on ALL TextFields (7 sites) (src/kirigami_ui/PrompterPage.qml:1) |
| deepseek-v4-pro-max | ⚠️ PARTIAL | 65 | EKA-SYS: absence of EnterKeyAction is mobile UX polish not defect; virtual keyboard enter-key label defaults to Return — not all 7 sites verified |
| glm-5.2-xhigh | ✅ LEGIT | 70 | 7 TextFields across PrompterPage.qml Find.qml PathsPage.qml have no EnterKeyAction |
| kimi-k2.7-code | ✅ LEGIT | 90 | No EnterKey attached property in src QML; TextFields lack mobile return-key actions. |
| opus-4.8-ultra | ❌ FALSE | 72 | max: code correct / claim mischaracterized — no EnterKeyAction on TextFields; minor UX (PrompterPage.qml) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

