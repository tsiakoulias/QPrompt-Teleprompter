# [RND-N01] forceQtTextRenderer dead on Apple platforms — unconditionally uses NativeRendering

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `Prompter.qml:994`
- **Consensus:** 3/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** Prompter.qml:994
- **Severity:** Low
- **Analysis:** `Qt.platform.os==="ios" || Qt.platform.os==="osx"` short-circuits to NativeRendering before `root.forceQtTextRenderer` is evaluated.
- **Impact:** "Force Qt Text Renderer" toggle has no effect on macOS/iOS.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | forceQtTextRenderer dead on Apple (always NativeRendering) (Prompter.qml:994) |
| gpt | ⚠️ PARTIAL | 58 | observed forceQtTextRenderer dead on Apple platforms - unconditionally uses NativeRendering (src/prompter/Prompter.qml:994) |
| deepseek | ✅ LEGIT | 95 | Prompter.qml:994: iOS/osx short-circuit to NativeRendering unconditionally before evaluating root.forceQtTextRenderer |
| glm | ✅ LEGIT | 70 | Prompter.qml:994 forceQtTextRenderer dead on Apple platforms; unconditionally uses NativeRendering |
| kimi | ❌ FALSE | 70 | Prompter.qml:994 does evaluate `root.forceQtTextRenderer` on non-Apple; claim says Apple branch dead. Conditional is valid; toggle works on other platforms; not solely a code bug. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — forceQtTextRenderer dead on Apple (always NativeRendering) (Prompter.qml:994) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

