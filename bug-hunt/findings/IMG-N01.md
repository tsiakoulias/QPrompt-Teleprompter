# [IMG-N01] Missing go-previous-symbolic.svg — back-navigation icon blank on Android/Windows

- **Status:** NEEDS-INFO
- **Severity:** Medium
- **Category:** 
- **Location:** `+android/main.qml:575, +windows/main.qml:631`
- **Consensus:** 2/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp:1733-1764
- **Severity:** High
- **Analysis:** QImage ctor doesn't parse data URIs. image.isNull() → true. Scheme check misses "data". Falls to return with zero effect. insertHtmlAt() correctly handles data: URIs.
- **Impact:** Data URI images dropped/pasted via QML handler silently do nothing.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❔ UNSURE | 45 | go-previous-symbolic.svg may be absent from breeze subset; needs icon check (main.qml:575) |
| gpt | ❔ UNSURE | 39 | runtime/platform behavior is not decidable from the cited snippet (src/kirigami_ui/+android/main.qml:575) |
| deepseek | ❔ UNSURE | 30 | icon presence depends on breeze-internal subset bundling; DUPLICATE-ID per csv |
| glm | ✅ LEGIT | 80 | +android/main.qml:575 +windows/main.qml:631 reference go-previous-symbolic.svg; icon exists in Breeze subset |
| kimi | ✅ LEGIT | 95 | +android/main.qml:575 and +windows/main.qml:631 source qrc:/.../go-previous-symbolic.svg, but the file does not exist anywhere in the repository. |
| opus-ultra | ❔ UNSURE | 45 | max: unverifiable statically (runtime/semantic) — go-previous-symbolic.svg may be absent from breeze subset; needs icon check (main.qml:575) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

