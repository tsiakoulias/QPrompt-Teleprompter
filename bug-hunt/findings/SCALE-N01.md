# [SCALE-N01] Right pointer xScale: -1 mirrors text pointers — backwards/unreadable text

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `ReadRegionOverlay.qml:391-398`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** ReadRegionOverlay.qml:391-398
- **Severity:** Medium
- **Analysis:** `Scale { xScale: -1 }` applied when sameAsLeftPointer or pointerKind is Arrow. For pointer_0 (arrow Shape), mirroring correct — arrow points inward. For pointer_1 (text pointer), text rendered backwards/unreadable.
- **Impact:** Right-side text pointers display mirrored, unreadable text (masked by broken pointerSettings refs).

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | right pointer xScale:-1 mirrors text; domain (ReadRegionOverlay.qml:391) |
| gpt | ✅ LEGIT | 78 | Right pointer xScale: -1 mirrors text pointers - backwards/unreadable text (src/prompter/ReadRegionOverlay.qml:391) |
| deepseek | ✅ LEGIT | 65 | right pointer xScale:-1 mirrors Arrow/sameAsLeft text making it backwards (ReadRegionOverlay.qml:391-398) |
| glm | ✅ LEGIT | 75 | ReadRegionOverlay.qml:391-398 right pointer xScale:-1 mirrors text; backwards/unreadable text |
| kimi | ✅ LEGIT | 80 | ReadRegionOverlay.qml:391-398 applies Scale xScale:-1 to Text pointers, mirroring text and making it unreadable. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — right pointer xScale:-1 mirrors text; domain (ReadRegionOverlay.qml:391) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

