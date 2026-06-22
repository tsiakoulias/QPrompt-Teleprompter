# [EVT-07] TabBar currentIndex binding broken on first TabButton click

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `PointerSettings.qml:266,248`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** PointerSettings.qml:266,248
- **Severity:** Medium
- **Analysis:** TabBar sets currentIndex imperatively, breaking binding to pointerSettings.pointerKind. Two-way sync dead after first click.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 60 | TabBar currentIndex binding broken on first TabButton click (PointerSettings.qml:266) |
| gpt | ✅ LEGIT | 78 | TabBar currentIndex binding broken on first TabButton click (src/prompter/PointerSettings.qml:266) |
| deepseek | ✅ LEGIT | 90 | TabBar sets currentIndex imperatively on click breaking binding to pointerSettings.pointerKind (PointerSettings.qml:266 248) |
| glm | ✅ LEGIT | 80 | PointerSettings.qml:266 248 TabBar currentIndex binding broken on first TabButton click |
| kimi | ✅ LEGIT | 85 | PointerSettings.qml:266 binds TabBar.currentIndex to pointerSettings.pointerKind; TabButton clicks set currentIndex imperatively and break the binding. |
| opus-ultra | ✅ LEGIT | 60 | TabBar currentIndex binding broken on first TabButton click (PointerSettings.qml:266) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

