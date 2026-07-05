# [407-MODEL-N02] SessionModel::clearDataPoints lacks empty-model guard before beginRemoveRows

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `promptsession.cpp:79-84`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** promptsession.cpp:79-84
- **Severity:** Low
- **Analysis:** beginRemoveRows(0, 0) on empty model signals removal of 1 row from empty model — contract violation. MarkersModel::clearMarkers correctly guards with isEmpty() check. LOG-02 covers off-by-one only.
- **Impact:** Model/view consistency violation on clearing empty session model.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ✅ LEGIT | 55 | clearDataPoints no empty guard before beginRemoveRows; dead code (promptsession.cpp:79) |
| gpt-5.5-xhigh | ⚠️ PARTIAL | 58 | observed SessionModel::clearDataPoints lacks empty-model guard before beginRemoveRows (src/promptsession.cpp:79) |
| deepseek-v4-pro-max | ✅ LEGIT | 85 | promptsession.cpp:79-84: clearDataPoints calls beginRemoveRows(0 rowCount()) without empty-model guard; signals removal from empty model |
| glm-5.2-xhigh | ✅ LEGIT | 70 | promptsession.cpp:79-84 clearDataPoints lacks empty-model guard before beginRemoveRows |
| kimi-k2.7-code | ✅ LEGIT | 85 | promptsession.cpp:79-84 clearDataPoints calls beginRemoveRows(0,rowCount()) even when rowCount()=0; contract violation. |
| opus-4.8-ultra | ✅ LEGIT | 55 | clearDataPoints no empty guard before beginRemoveRows; dead code (promptsession.cpp:79) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

