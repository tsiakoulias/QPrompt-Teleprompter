# [R2-PRP-02] Kirigami.Units.SmallSpacing — uppercase S yields undefined

- **Status:** OPEN
- **Severity:** Medium
- **Category:** Logic
- **Location:** `src/kirigami_ui/PrompterPage.qml:1331,1332,1352,1353,1377,1378`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** src/kirigami_ui/PrompterPage.qml:1331,1332,1352,1353,1377,1378
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** QML properties are case-sensitive. Correct property is `Kirigami.Units.smallSpacing` (lowercase 's'), used correctly elsewhere in file. `SmallSpacing` resolves to undefined, setting margins to 0.
- **Impact:** 3 SpinBoxes in network dialog (auto-reload hours/minutes/seconds) have zero horizontal margins, rendering labels cramped.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 85 | Units.SmallSpacing should be smallSpacing (PrompterPage.qml:1331) |
| gpt | ✅ LEGIT | 92 | Kirigami.Units.SmallSpacing - uppercase S yields undefined (src/kirigami_ui/PrompterPage.qml:1331) |
| deepseek | ❔ UNSURE | 40 | Kirigami.Units.SmallSpacing uppercase S claimed undefined; depends on Kirigami 2.x API; need to verify actual property name in Kirigami's Units singleton |
| glm | ✅ LEGIT | 85 | PrompterPage.qml:1331+ uses Kirigami.Units.SmallSpacing with capital S; correct API is kirigamiUnits.smallSpacing or Units.smallSpacing |
| kimi | ✅ LEGIT | 90 | PrompterPage.qml:1331,1332,1352,1353,1377,1378 uses Kirigami.Units.SmallSpacing (undefined); correct is smallSpacing. |
| opus-ultra | ✅ LEGIT | 85 | Units.SmallSpacing should be smallSpacing (PrompterPage.qml:1331) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

