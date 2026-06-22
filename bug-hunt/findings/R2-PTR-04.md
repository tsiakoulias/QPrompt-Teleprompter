# [R2-PTR-04] Inverted indexOf truthiness in platform check for ColorDialog

- **Status:** OPEN
- **Severity:** Medium
- **Category:** Type Safety
- **Location:** `src/prompter/PointerSettings.qml:653`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** src/prompter/PointerSettings.qml:653
- **Severity:** Medium
- **Category:** Type Safety
- **Analysis:** `["ios","osx"].indexOf(Qt.platform.os) ? 0 : ColorDialog.DontUseNativeDialog`. indexOf returns -1 for non-iOS/macOS — in JS, -1 is truthy. Non-Apple platforms get `0` (native dialog) instead of `DontUseNativeDialog`. iOS gets `DontUseNativeDialog` instead of `0` (indexOf returns 0, which is falsy). Only macOS gets correct result. Fix: `!== -1 ? 0 : DontUseNativeDialog`.
- **Impact:** Linux/Windows use native color dialog (unreliable/missing features). iOS uses non-native dialog (degraded UX).

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 85 | indexOf truthiness bug (PointerSettings.qml:653) |
| gpt | ✅ LEGIT | 78 | Inverted indexOf truthiness in platform check for ColorDialog (src/prompter/PointerSettings.qml:653) |
| deepseek | ❔ UNSURE | 35 | indexOf truthiness inversion at PointerSettings.qml:653; JS logic analysis correct on paper but need to verify actual runtime context |
| glm | ✅ LEGIT | 85 | PointerSettings.qml:653 indexOf returns -1 for not found which is truthy; logic inverted for platform check |
| kimi | ✅ LEGIT | 90 | PointerSettings.qml:653 inverted indexOf truthiness flips ColorDialog.DontUseNativeDialog logic on non-macOS/iOS. |
| opus-ultra | ✅ LEGIT | 85 | indexOf truthiness bug (PointerSettings.qml:653) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

