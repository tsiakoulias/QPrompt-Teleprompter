# [ACT-N07] namedBookmarkButton: checkable button opens dialog — stale indicator after first click

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `EditorToolbar.qml:225-236`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** EditorToolbar.qml:225-236
- **Severity:** Medium
- **Analysis:** checkable with checked binding to document.namedMarker. onClicked opens dialog instead of toggling property. Binding breaks on first click; indicator never re-syncs. Worse than R2-EDT-03 because formatting buttons re-sync each click — this one permanently desyncs.
- **Impact:** Named-marker button shows stale checkmark after first use.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 60 | namedBookmarkButton checkable opens dialog -> stale indicator (R2-EDT-03 family) (EditorToolbar.qml:225) |
| gpt | ⚠️ PARTIAL | 58 | observed namedBookmarkButton: checkable button opens dialog - stale indicator after first click (src/kirigami_ui/EditorToolbar.qml:225) |
| deepseek | ✅ LEGIT | 65 | checkable button opens dialog instead of toggling; checked binding desyncs after first click (EditorToolbar.qml:225-236) |
| glm | ✅ LEGIT | 75 | EditorToolbar.qml:225-236 namedBookmarkButton checkable button opens dialog; stale checked indicator after first click |
| kimi | ✅ LEGIT | 90 | EditorToolbar.qml:225-236 makes namedBookmarkButton checkable with checked bound to document.namedMarker, but onClicked only opens namedMarkerConfiguration, never toggling the property so the binding breaks. |
| opus-ultra | ✅ LEGIT | 60 | namedBookmarkButton checkable opens dialog -> stale indicator (R2-EDT-03 family) (EditorToolbar.qml:225) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

