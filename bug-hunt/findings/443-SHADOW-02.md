# [443-SHADOW-02] id: flow shadows Flow.flow property

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `EditorToolbar.qml:184`
- **Consensus:** 4/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** EditorToolbar.qml:184
- **Severity:** Low
- **Analysis:** Flow layout has id: flow. Flow.flow is direction enum. Bare flow resolves to Flow item. Reading flow direction requires awkward flow.flow.
- **Impact:** Error-prone property access.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ✅ LEGIT | 55 | id: flow shadows Flow.flow property (EditorToolbar.qml:184) |
| gpt-5.5-xhigh | ✅ LEGIT | 78 | id: flow shadows Flow.flow property (src/kirigami_ui/EditorToolbar.qml:184) |
| deepseek-v4-pro-max | ✅ LEGIT | 85 | Flow id:flow shadows Flow.flow enum; accessing flow direction requires awkward flow.flow (EditorToolbar.qml:184) |
| glm-5.2-xhigh | ⚠️ PARTIAL | 60 | EditorToolbar.qml:184 id: flow shadows Flow.flow property; ambiguous in context |
| kimi-k2.7-code | ❌ FALSE | 80 | id:flow names the Flow item; no current use of the Flow.flow enum conflicts, so this is only a naming smell. |
| opus-4.8-ultra | ✅ LEGIT | 55 | id: flow shadows Flow.flow property (EditorToolbar.qml:184) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

