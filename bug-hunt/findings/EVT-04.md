# [EVT-04] Drag breaks editor.x declarative binding permanently

- **Status:** OPEN
- **Severity:** High
- **Category:** 
- **Location:** `Prompter.qml:1984,958`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** Prompter.qml:1984,958
- **Severity:** High
- **Analysis:** drag.target: editor writes x imperatively, breaks `x: contentsPlacement*(prompter.width) + 20` binding.
- **Impact:** After one drag, editor horizontal position frozen. Resize/orientation changes no-op.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | width-handle drag.target editor may break editor.x binding (Prompter.qml:1984) |
| gpt | ⚠️ PARTIAL | 58 | observed Drag breaks editor.x declarative binding permanently (src/prompter/Prompter.qml:1984) |
| deepseek | ✅ LEGIT | 92 | drag.target:editor writes x imperatively breaking x:contentsPlacement*(prompter.width)+20 binding (Prompter.qml:1984 958) |
| glm | ✅ LEGIT | 80 | Prompter.qml:1984 958 Drag on editor breaks x declarative binding permanently |
| kimi | ✅ LEGIT | 85 | Prompter.qml:1984 sets drag.target: editor, which imperatively writes x and breaks the declarative x binding at Prompter.qml:958. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — width-handle drag.target editor may break editor.x binding (Prompter.qml:1984) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

