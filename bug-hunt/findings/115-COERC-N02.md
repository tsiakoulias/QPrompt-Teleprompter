# [115-COERC-N02] Unvalidated string-to-number injects NaN into root.__opacity — all opacity dead

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `EditorToolbar.qml:953-958`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** EditorToolbar.qml:953-958
- **Severity:** Medium
- **Analysis:** Non-numeric TextField input ("abc") passes !="" guard, both numeric comparisons produce NaN→false, falls through to `"abc"/100 → NaN`. Propagates to PrompterBackground opacity, toolbar opacity, overlay calculations. No recovery — only app restart fixes it.
- **Impact:** Typing non-numeric text in opacity field silently breaks all opacity-dependent visuals.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ✅ LEGIT | 55 | unvalidated string->number injects NaN into root.__opacity (EditorToolbar.qml:953) |
| gpt-5.5-xhigh | ✅ LEGIT | 78 | Unvalidated string-to-number injects NaN into root.__opacity - all opacity dead (src/kirigami_ui/EditorToolbar.qml:953) |
| deepseek-v4-pro-max | ✅ LEGIT | 95 | EditorToolbar.qml:953-958: non-numeric text passes !== guard; 'abc'/100=NaN injected into root.__opacity; all opacity visuals break |
| glm-5.2-xhigh | ✅ LEGIT | 75 | EditorToolbar.qml:953-958 unvalidated string-to-number injects NaN into root.__opacity |
| kimi-k2.7-code | ✅ LEGIT | 85 | EditorToolbar.qml:951-958 non-numeric input reaches `root.__opacity = text/100` producing NaN; no validation. |
| opus-4.8-ultra | ✅ LEGIT | 55 | unvalidated string->number injects NaN into root.__opacity (EditorToolbar.qml:953) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

