# [ARC-02] Arc-03 Search/replace state machine fully in QML (50+ lines)

- **Status:** OPEN
- **Severity:** 
- **Category:** 
- **Location:** `Find.qml:112-161`
- **Consensus:** 1/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** Find.qml:112-161
- **Analysis:** Mode dispatch, replace-next/replace-previous/replace-all orchestration, wrap detection, cursor math all in QML. Should be in C++ for testability.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 35 | search state machine in QML; architectural (Find.qml:112) |
| gpt | ⚠️ PARTIAL | 48 | maintainability issue observed, but no direct runtime bug shown (src/prompter/Find.qml:112) |
| deepseek | ❌ FALSE | 50 | architectural observation; state machine in QML is a valid Qt design pattern |
| glm | ⚠️ PARTIAL | 55 | Find.qml:112-161 search/replace state machine in QML; architectural concern |
| kimi | ✅ LEGIT | 60 | Find.qml:112-161 search/replace orchestration, wrap detection and cursor math implemented fully in QML. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — search state machine in QML; architectural (Find.qml:112) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

