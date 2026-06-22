# [VCI-N01] At-end action buttons use inconsistent font scaling (1/1.5 vs 1/1.75) in same group

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `Prompter.qml:1158,1185,1212 vs 1256,1269,1309`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** Prompter.qml:1158,1185,1212 vs 1256,1269,1309
- **Severity:** Low
- **Analysis:** Stop/Exit/Loop buttons scale by 1/1.5; adjacent Flipable buttons and SpinBox scale by 1/1.75. Buttons visibly 16.7% larger than neighbors.
- **Impact:** Visible size mismatch between button rows in same footer control.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 40 | at-end buttons inconsistent font scaling (Prompter.qml:1158) |
| gpt | ⚠️ PARTIAL | 48 | visual issue is plausible but depends on theme or device (src/prompter/Prompter.qml:1158) |
| deepseek | ✅ LEGIT | 95 | Prompter.qml:1158/1185/1212 vs 1256/1269/1309: Stop/Exit/Loop buttons scale font /1.5 while adjacent Flipable/SpinBox scale /1.75 — visible 16.7% size mismatch |
| glm | ✅ LEGIT | 70 | Prompter.qml:1158+ at-end action buttons use inconsistent font scaling 1/1.5 vs 1/1.75 |
| kimi | ✅ LEGIT | 70 | Prompter.qml:1158-1212 at-end Stop/Exit/Loop buttons scale font by 1/1.5 while adjacent Flipable/SpinBox at ~1256-1309 scale by 1/1.75. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — at-end buttons inconsistent font scaling (Prompter.qml:1158) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

