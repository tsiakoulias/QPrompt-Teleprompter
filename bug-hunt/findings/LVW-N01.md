# [LVW-N01] InputsOverlay.qml ListView currentIndex: PointerSettings.States.Arrow — copy-paste error

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `InputsOverlay.qml:77`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** InputsOverlay.qml:77
- **Severity:** Low
- **Analysis:** `currentIndex: PointerSettings.States.Arrow` — copy-paste from PointerSettings.qml. InputsOverlay has 2 tabs, not 4 pointer types. Works accidentally (resolves to 0). Binding breaks on first TabBar click.
- **Impact:** TabBar highlight desyncs after first user interaction.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | ListView currentIndex copy-paste PointerSettings.States.Arrow (InputsOverlay.qml:77) |
| gpt | ⚠️ PARTIAL | 58 | observed InputsOverlay.qml ListView currentIndex: PointerSettings.States.Arrow - copy-paste error (src/kirigami_ui/InputsOverlay.qml:77) |
| deepseek | ✅ LEGIT | 85 | InputsOverlay.qml:77: currentIndex: PointerSettings.States.Arrow — copy-paste from PointerSettings.qml; resolves to 0 accidentally but semantically wrong for 2-tab InputsOverlay |
| glm | ✅ LEGIT | 70 | InputsOverlay.qml:77 ListView currentIndex: PointerSettings.States.Arrow; copy-paste error from PointerSettings |
| kimi | ✅ LEGIT | 70 | InputsOverlay.qml:77 sets ListView currentIndex to PointerSettings.States.Arrow instead of first tab index. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — ListView currentIndex copy-paste PointerSettings.States.Arrow (InputsOverlay.qml:77) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

