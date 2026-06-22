# [FINAL-11] onFrameSwapped calls grabToImage every frame — severe performance hit

- **Status:** OPEN
- **Severity:** High
- **Category:** QML/UI
- **Location:** `src/kirigami_ui/main.qml:1041-1045`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/kirigami_ui/main.qml:1041-1045
- **Severity:** High
- **Category:** QML/UI
- **Analysis:** Every frame, when projections enabled, `viewport.grabToImage()` triggers offscreen render + GPU readback.
- **Impact:** Major frame rate degradation during screen projections.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 85 | grabToImage every onFrameSwapped (main.qml:1041) |
| gpt | ✅ LEGIT | 84 | onFrameSwapped calls grabToImage every frame - severe performance hit (src/kirigami_ui/main.qml:1041) |
| deepseek | ✅ LEGIT | 95 | main.qml:1041-1045 onFrameSwapped calls grabToImage() every frame when projections enabled — GPU readback per frame severe perf hit |
| glm | ✅ LEGIT | 85 | main.qml:1041-1045 onFrameSwapped calls grabToImage every frame for projection updates; severe performance hit |
| kimi | ✅ LEGIT | 95 | main.qml:1041-1045 calls viewport.grabToImage every frame inside onFrameSwapped whenever projections are enabled. |
| opus-ultra | ✅ LEGIT | 85 | grabToImage every onFrameSwapped (main.qml:1041) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

