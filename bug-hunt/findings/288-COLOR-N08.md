# [288-COLOR-N08] textBackground() returns invalid QColor for body/paragraph text

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.cpp:528-534`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp:528-534
- **Severity:** Medium
- **Analysis:** Default stylesheet has no background-color on body/p. QBrush::color() returns invalid QColor (isValid()=false) for NoBrush. QML color swatch indicator receives invalid color → renders as transparent black.
- **Impact:** Text-background color swatch invisible for body/paragraph text.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ⚠️ PARTIAL | 45 | textBackground().color() yields black for unset bg, not 'invalid' (documenthandler.cpp:534) |
| gpt-5.5-xhigh | ⚠️ PARTIAL | 58 | visual issue is plausible but depends on theme or device (src/documenthandler.cpp:528) |
| deepseek-v4-pro-max | ✅ LEGIT | 90 | documenthandler.cpp:528-534: textBackground() returns format.background().color(); QBrush::color() on NoBrush returns invalid QColor |
| glm-5.2-xhigh | ✅ LEGIT | 70 | documenthandler.cpp:528-534 textBackground() returns invalid QColor for body/paragraph text |
| kimi-k2.7-code | ✅ LEGIT | 85 | documenthandler.cpp:534 returns format.background().color(), which is invalid when no background-color is set |
| opus-4.8-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — textBackground().color() yields black for unset bg |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

