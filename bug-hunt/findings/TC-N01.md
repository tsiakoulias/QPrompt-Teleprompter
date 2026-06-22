# [TC-N01] Image.source assigned boolean false instead of empty string

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `ProjectionsManager.qml:287`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** ProjectionsManager.qml:287
- **Severity:** Low
- **Analysis:** `source: model.flip ? model.p : false` — false (boolean) on empty, not "". QML coerces to "". Should be `model.flip ? model.p : ""`.
- **Impact:** Type muddling. Silent coercion.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 60 | Image.source assigned boolean false instead of '' (ProjectionsManager.qml:287) |
| gpt | ✅ LEGIT | 78 | Image.source assigned boolean false instead of empty string (src/prompter/ProjectionsManager.qml:287) |
| deepseek | ✅ LEGIT | 80 | ProjectionsManager.qml:287: source: model.flip ? model.p : false; boolean false silently coerced to ''; should be empty string |
| glm | ✅ LEGIT | 65 | ProjectionsManager.qml:287 Image.source assigned boolean false instead of empty string |
| kimi | ✅ LEGIT | 60 | ProjectionsManager.qml:287 assigns bool false to Image.source when not flipped; source type is url |
| opus-ultra | ✅ LEGIT | 60 | Image.source assigned boolean false instead of '' (ProjectionsManager.qml:287) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

