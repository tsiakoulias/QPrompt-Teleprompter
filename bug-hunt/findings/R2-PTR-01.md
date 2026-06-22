# [R2-PTR-01] Type mismatch: textVerticalOffset declared int but fed a real

- **Status:** REJECTED
- **Severity:** Medium
- **Category:** Type Safety
- **Location:** `src/prompter/pointers/pointer_1.qml:33`
- **Consensus:** 2/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** src/prompter/pointers/pointer_1.qml:33
- **Severity:** Medium
- **Category:** Type Safety
- **Analysis:** `property int textVerticalOffset` receives value from PointerSettings real slider (-1.0 to 1.0 at stepSize 0.01). `int` truncation: -0.05→0, 0.75→0, -0.99→0. Only ±1.0 survives. Default -0.05 rounds to zero.
- **Impact:** Text pointer vertical-offset slider non-responsive for most of its range. Only extreme ends register change. Default offset silently lost.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❌ FALSE | 75 | int gets scaled readRegion.height*offset/2 not raw slider (pointer_1.qml:33) |
| gpt | ❌ FALSE | 76 | value is scaled before assignment; int truncation is minor (src/prompter/pointers/pointer_1.qml:33) |
| deepseek | ✅ LEGIT | 80 | textVerticalOffset declared int at pointer_1.qml:33; fed real from slider -1.0..1.0 step 0.01; truncation means only +/-1 survive — confirmed type mismatch |
| glm | ⚠️ PARTIAL | 60 | pointer_1.qml:33 textVerticalOffset declared int but QML bindings may assign real; type coercion handles this |
| kimi | ✅ LEGIT | 90 | pointer_1.qml:33 property int textVerticalOffset truncates real slider values from PointerSettings. |
| opus-ultra | ❌ FALSE | 75 | int gets scaled readRegion.height*offset/2 not raw slider (pointer_1.qml:33) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

