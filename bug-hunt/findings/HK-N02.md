# [HK-N02] Typo Qt.Key_VolumeDowm — "Dowm" instead of "Down" — volume-down hardware key dead

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `Prompter.qml:2674`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** Prompter.qml:2674
- **Severity:** Medium
- **Analysis:** 'm' instead of 'n'. Resolves to `undefined`. Volume-down key never works. Volume-up (Key_VolumeUp) correct.
- **Impact:** Volume-down hardware button non-functional.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 80 | Qt.Key_VolumeDowm typo (should be VolumeDown) -> undefined, never matches (Prompter.qml:2674) |
| gpt | ✅ LEGIT | 92 | Typo Qt.KeyVolumeDowm - "Dowm" instead of "Down" - volume-down hardware key dead (src/prompter/Prompter.qml:2674) |
| deepseek | ✅ LEGIT | 95 | Qt.Key_VolumeDowm at Prompter.qml:2674 — typo Dowm->Down resolves to undefined |
| glm | ✅ LEGIT | 85 | Prompter.qml:2674 Qt.Key_VolumeDowm typo; should be VolumeDown; volume-down hardware key dead |
| kimi | ✅ LEGIT | 98 | Prompter.qml:2674 references Qt.Key_VolumeDowm instead of Down; undefined enum means the volume-down hardware key does nothing |
| opus-ultra | ✅ LEGIT | 80 | Qt.Key_VolumeDowm typo (should be VolumeDown) -> undefined |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

