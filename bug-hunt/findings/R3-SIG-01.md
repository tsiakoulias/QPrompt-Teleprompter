# [R3-SIG-01] textChanged() signal declared but never emitted

- **Status:** OPEN
- **Severity:** Low
- **Category:** Logic
- **Location:** `src/documenthandler.h:307`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/documenthandler.h:307
- **Severity:** Low
- **Category:** Logic
- **Analysis:** Signal `void textChanged()` declared in Q_SIGNALS but zero emits in entire codebase. Not used as NOTIFY for any Q_PROPERTY.
- **Impact:** Dead code. Any connection to this signal silently never fires.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 85 | textChanged declared never emitted (documenthandler.h:307) |
| gpt | ✅ LEGIT | 78 | textChanged() signal declared but never emitted (src/documenthandler.h:307) |
| deepseek | ✅ LEGIT | 90 | documenthandler.h:307 textChanged() signal declared but zero emits in entire codebase — dead signal any connection silently never fires |
| glm | ✅ LEGIT | 80 | documenthandler.h:307 textChanged() signal declared but never emitted anywhere in documenthandler.cpp |
| kimi | ✅ LEGIT | 95 | textChanged declared at documenthandler.h:307 but no Q_EMIT found anywhere in source |
| opus-ultra | ✅ LEGIT | 85 | textChanged declared never emitted (documenthandler.h:307) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

