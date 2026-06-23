# [298-HSCROLL-N01] InputsOverlay Flickables use contentWidth: width instead of implicitWidth — horizontal overflow clipped

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `InputsOverlay.qml:95,552`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** InputsOverlay.qml:95,552
- **Severity:** Medium
- **Analysis:** Both Keyboard Inputs and Global Hotkeys Flickables set `contentWidth: buttonGrid.width` which equals Flickable's own width. contentHeight correctly uses implicitHeight. Long key labels silently clipped horizontally with no scroll.
- **Impact:** Content clipped unreachable on narrow windows or with long translation strings.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | Flickable contentWidth:width vs implicitWidth (InputsOverlay.qml:95) |
| gpt | ⚠️ PARTIAL | 58 | observed InputsOverlay Flickables use contentWidth: width instead of implicitWidth - horizontal overflow (src/kirigami_ui/InputsOverlay.qml:95) |
| deepseek | ✅ LEGIT | 95 | InputsOverlay.qml:95 552: contentWidth set to Flickable's own width via buttonGrid.width/hotkeyGrid.width; horizontal overflow clipped |
| glm | ✅ LEGIT | 70 | InputsOverlay.qml:95 552 Flickables use contentWidth: width instead of implicitWidth; horizontal overflow clipped |
| kimi | ✅ LEGIT | 90 | InputsOverlay.qml:95/552 set contentWidth to grid.width (== Flickable width), preventing horizontal scroll |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — Flickable contentWidth:width vs implicitWidth (InputsOverlay.qml:95) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

