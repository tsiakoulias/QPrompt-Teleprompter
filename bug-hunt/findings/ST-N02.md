# [ST-N02] Dead overlay.state PropertyChanges — overlay has no states array

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `ReadRegionOverlay.qml:34-37, Prompter.qml:2899-3032`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** ReadRegionOverlay.qml:34-37, Prompter.qml:2899-3032
- **Severity:** Medium
- **Analysis:** ReadRegionOverlay defines enum States but has no states: array. Sub-components manage own states independently. All 4 PropertyChanges setting overlay.state in Prompter.qml change no properties — dead code.
- **Impact:** Dead enum + dead PropertyChanges. States either never implemented or should be removed.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 50 | dead overlay.state PropertyChanges; overlay has no states (ReadRegionOverlay.qml:34) |
| gpt | ⚠️ PARTIAL | 58 | observed Dead overlay.state PropertyChanges - overlay has no states array (src/prompter/ReadRegionOverlay.qml:34) |
| deepseek | ✅ LEGIT | 95 | ReadRegionOverlay.qml:34-37 has enum States but no states: array; Prompter.qml:2899 overlay.state PropertyChanges is dead property assignment |
| glm | ✅ LEGIT | 70 | ReadRegionOverlay.qml:34-37 Prompter.qml:2899-3032 dead overlay.state PropertyChanges; overlay has no states array |
| kimi | ✅ LEGIT | 85 | ReadRegionOverlay.qml:34 defines States enum but no `states:` array; Prompter.qml:2899-2900/2934 PropertyChanges target overlay.state are no-ops. |
| opus-ultra | ✅ LEGIT | 50 | dead overlay.state PropertyChanges; overlay has no states (ReadRegionOverlay.qml:34) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

