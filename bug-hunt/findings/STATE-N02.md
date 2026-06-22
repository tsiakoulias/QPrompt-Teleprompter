# [STATE-N02] Find.toggle() uses !visible instead of !isOpen — can't close during Prompting

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `Find.qml:51`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** Find.qml:51
- **Severity:** Medium
- **Analysis:** `toggle()` computes `isOpen = !visible` but `visible` is bound to `height>0` which is false during Prompting/Countdown regardless of `isOpen`. When isOpen=true and state=Prompting: `isOpen = !false = true` — no change. Find stays logically open.
- **Impact:** Find bar reappears unexpectedly when returning to Editing after pressing close shortcut during prompting.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | toggle() uses !visible vs !isOpen; can desync (Find.qml:51) |
| gpt | ✅ LEGIT | 78 | Find.toggle() uses !visible instead of !isOpen - can't close during Prompting (src/prompter/Find.qml:51) |
| deepseek | ✅ LEGIT | 75 | toggle() uses !visible which desyncs from isOpen state machine flag (Find.qml:51) |
| glm | ✅ LEGIT | 80 | Find.qml:51 toggle() uses !visible instead of !isOpen; can't close during Prompting |
| kimi | ✅ LEGIT | 80 | Find.toggle() uses visible (derived from height) instead of isOpen; during Prompting height is forced 0 so toggle cannot close the bar. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — toggle() uses !visible vs !isOpen; can desync (Find.qml:51) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

