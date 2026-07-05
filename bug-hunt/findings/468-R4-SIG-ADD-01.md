# [468-R4-SIG-ADD-01] SessionModel::appendDataPoint declared public slot but never connected

- **Status:** OPEN
- **Severity:** Low
- **Category:** Logic
- **Location:** `src/prompsession.h:71`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** src/prompsession.h:71
- **Severity:** Low
- **Category:** Logic
- **Analysis:** Declared as public slot but no connect() call anywhere connects any signal to it. Not marked Q_INVOKABLE. If intended as signal-driven telemetry, silently broken.
- **Impact:** Likely low. If QML invokes via slot mechanism it works, but signal-driven recording is dead.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ⚠️ PARTIAL | 45 | appendDataPoint public slot never connected; dead-code area (promptsession.h:71) |
| gpt-5.5-xhigh | ⚠️ PARTIAL | 58 | observed SessionModel::appendDataPoint declared public slot but never connected (src/prompsession.h:71) |
| deepseek-v4-pro-max | ⚠️ PARTIAL | 60 | promptsession.h:71 appendDataPoint in public slots never connected to any signal; but QML can still invoke slots directly — signal-driven recording dead |
| glm-5.2-xhigh | ✅ LEGIT | 75 | promptsession.h:71 appendDataPoint declared as public slot but never connected via signal/slot |
| kimi-k2.7-code | ✅ LEGIT | 70 | promptsession.h:71 appendDataPoint is a slot but not connected externally; signal-driven path dead, yet callable from QML. |
| opus-4.8-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — appendDataPoint public slot never connected; dead-code area (promptsession.h:71) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

