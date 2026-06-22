# [SHDR-N01] Math.cos/Math.sin used with degrees value — shadow offset diagonal instead of horizontal

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `Prompter.qml:749, ReadRegionOverlay.qml:151-155`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** Prompter.qml:749, ReadRegionOverlay.qml:151-155
- **Severity:** Medium
- **Analysis:** `readonly property real angle: 180` then `offset = Qt.point(Math.cos(angle), Math.sin(angle))`. QML Math.cos/sin operate in radians. 180 rad ≈ 28.65 rotations; cos≈-0.598, sin≈-0.801 — diagonal up-left offset instead of intended horizontal-left (−1, 0) for 180°. Math.PI never used.
- **Impact:** Text/read-region drop shadows are offset diagonally. Should multiply by Math.PI/180 for degree conversion.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 65 | Math.cos/sin(angle=180) treats degrees as radians (Prompter.qml:749) |
| gpt | ✅ LEGIT | 78 | Math.cos/Math.sin used with degrees value - shadow offset diagonal instead of horizontal (src/prompter/Prompter.qml:749) |
| deepseek | ✅ LEGIT | 85 | Math.cos/sin(angle=180) takes radians; offset becomes diagonal not horizontal (Prompter.qml:749) |
| glm | ✅ LEGIT | 75 | Prompter.qml:749 ReadRegionOverlay.qml:151-155 Math.cos/Math.sin used with degrees; shadow offset diagonal |
| kimi | ✅ LEGIT | 90 | Shadow offset uses Math.cos/sin with angle in degrees at Prompter.qml:749 and ReadRegionOverlay.qml:151-155; JS trig expects radians. |
| opus-ultra | ✅ LEGIT | 65 | Math.cos/sin(angle=180) treats degrees as radians (Prompter.qml:749) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

