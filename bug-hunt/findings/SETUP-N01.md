# [SETUP-N01] setup.sh uses windeployqt.exe (Qt 5) — should be windeployqt6.exe (Qt 6)

- **Status:** NEEDS-INFO
- **Severity:** Medium
- **Category:** 
- **Location:** `setup.sh:233`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** setup.sh:233
- **Severity:** Medium
- **Analysis:** Qt 6 ships windeployqt6.exe. Qt 5 tool doesn't exist on Qt 6-only machines. Mixed Qt 5+6 machines deploy wrong DLLs.
- **Impact:** Windows deployment packaging broken on Qt 6-only systems.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❔ UNSURE | 40 | setup.sh windeployqt; Qt6 tool is still 'windeployqt' not '6' (setup.sh:233) |
| gpt | ❔ UNSURE | 39 | Qt 6 still ships windeployqt, so the tool name alone is not wrong (setup.sh:233) |
| deepseek | ✅ LEGIT | 95 | setup.sh:233: windeployqt.exe is Qt5 tool; Qt6 ships windeployqt6.exe — on Qt6-only machines tool not found mixed Qt5+6 deploys wrong DLLs |
| glm | ✅ LEGIT | 75 | setup.sh:233 uses windeployqt.exe (Qt 5) instead of windeployqt6.exe (Qt 6) |
| kimi | ✅ LEGIT | 90 | setup.sh:235 invokes windeployqt.exe but Qt6 project should use windeployqt6.exe. |
| opus-ultra | ❔ UNSURE | 40 | max: unverifiable statically (runtime/semantic) — setup.sh windeployqt; Qt6 tool is still 'windeployqt' not '6' (setup.sh:233) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

