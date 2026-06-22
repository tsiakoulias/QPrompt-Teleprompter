# [GSW-N01] MarkersDrawer SwipeListItem navigates on swipe — gesture conflict on touch

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `MarkersDrawer.qml:70-74`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** MarkersDrawer.qml:70-74
- **Severity:** Medium
- **Analysis:** `onPressed` fires at start of every touch including swipe. Swiping to reveal edit action first triggers navigation to marker position + drawer close. Should use `onClicked` which only fires on press-release without exceeding swipe threshold.
- **Impact:** Swipe-to-reveal-edit non-functional on touchscreens; every swipe navigates away first.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | SwipeListItem navigates on swipe; gesture conflict (MarkersDrawer.qml:70) |
| gpt | ⚠️ PARTIAL | 58 | observed MarkersDrawer SwipeListItem navigates on swipe - gesture conflict on touch (src/kirigami_ui/MarkersDrawer.qml:70) |
| deepseek | ✅ LEGIT | 90 | MarkersDrawer.qml:70-74: SwipeListItem onPressed fires at start of every touch including swipe; navigating to marker+closing drawer on swipe-to-reveal gesture conflict |
| glm | ✅ LEGIT | 70 | MarkersDrawer.qml:70-74 SwipeListItem navigates on swipe; gesture conflict on touch |
| kimi | ✅ LEGIT | 80 | MarkersDrawer.qml:70-74 SwipeListItem onPressed navigates and conflicts with swipe gesture. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — SwipeListItem navigates on swipe; gesture conflict (MarkersDrawer.qml:70) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

