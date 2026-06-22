# [R2-TEL-01] Telemetry sub-toggles permanently disconnect from master toggle on click

- **Status:** OPEN
- **Severity:** Medium
- **Category:** Logic
- **Location:** `src/kirigami_ui/TelemetryPage.qml:80-88,101-110,123-132,149-158`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** src/kirigami_ui/TelemetryPage.qml:80-88,101-110,123-132,149-158
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** Each sub-toggle has `checked: root.__telemetry` as initial binding + `checkable: true`. Clicking any sub-toggle breaks the binding. After that, toggling master switch no longer controls that sub-option. Value persisted via QSettings but orphaned.
- **Impact:** After interacting with individual telemetry option, master toggle no longer controls it. UI state inconsistent.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 80 | telemetry sub-toggles break from master on click (TelemetryPage.qml:80) |
| gpt | ✅ LEGIT | 78 | Telemetry sub-toggles permanently disconnect from master toggle on click (src/kirigami_ui/TelemetryPage.qml:80) |
| deepseek | ❔ UNSURE | 35 | Telemetry sub-toggles disconnect from master — commented-out code; need verification of active code paths |
| glm | ✅ LEGIT | 85 | TelemetryPage.qml:80+ sub-toggles disconnect from master toggle on click due to imperative assignment breaking binding |
| kimi | ✅ LEGIT | 85 | TelemetryPage.qml:80-88,101-110,123-132,149-158 sub-toggles checked: root.__telemetry break binding when toggled individually. |
| opus-ultra | ✅ LEGIT | 80 | telemetry sub-toggles break from master on click (TelemetryPage.qml:80) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

