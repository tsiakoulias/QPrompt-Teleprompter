# [R4-BKG-01] Flip transform origin stays at (0,0) when Flip stored as property

- **Status:** OPEN
- **Severity:** Medium
- **Category:** QML/UI
- **Location:** `src/prompter/PrompterBackground.qml:89-90 (also ReadRegionOverlay:65,90)`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** src/prompter/PrompterBackground.qml:89-90 (also ReadRegionOverlay:65,90)
- **Severity:** Medium
- **Category:** QML/UI
- **Analysis:** readonly property Scale __flips: Flip{} — Scale item whose origin.x: width/2, origin.y: height/2 bind to Scale's own width/height, always 0. Flip occurs around top-left corner.
- **Impact:** Background image and overlay flips visibly off-center; mirrored content jumps to one side.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 85 | Scale has no width; origin.x: width/2=0 (Flip.qml:27) |
| gpt | ✅ LEGIT | 78 | Flip transform origin stays at (0,0) when Flip stored as property (src/prompter/PrompterBackground.qml:89) |
| deepseek | ✅ LEGIT | 85 | PrompterBackground.qml:89-90 Scale Flip{} without explicit origin — default (0 0) causes flip around top-left not center |
| glm | ⚠️ PARTIAL | 60 | PrompterBackground.qml:89-90 Flip transform origin at (0 0) when Flip is property; cosmetic issue |
| kimi | ✅ LEGIT | 90 | PrompterBackground.qml:89-90 Flip{} Scale binds origin.x/y to its own zero width/height, so flips occur around (0,0). |
| opus-ultra | ✅ LEGIT | 85 | Scale has no width; origin.x: width/2=0 (Flip.qml:27) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

