# [CFG-N02] v1.1.3 release date "2022-1-16" breaks chronological order — should be 2023-01-16

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `appdata.xml line 202`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** appdata.xml line 202
- **Severity:** Low
- **Impact:** Software centers may display releases in wrong order.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 55 | appdata v1.1.3 date 2022-1-16 breaks chronological order (appdata.xml) |
| gpt | ⚠️ PARTIAL | 58 | observed v1.1.3 release date "2022-1-16" breaks chronological order - should be 2023-01-16 (com.cuperino.qprompt.appdata.xml:202) |
| deepseek | ❔ UNSURE | 40 | 'appdata.xml:202 date "2022-1-16"; cannot independently verify correct year from source alone' |
| glm | ✅ LEGIT | 70 | appdata.xml line 202 v1.1.3 release date '2022-1-16' breaks chronological order; should be 2023-01-16 |
| kimi | ✅ LEGIT | 95 | com.cuperino.qprompt.appdata.xml:202 release 1.1.3 has date='2022-1-16'; chronology broken. |
| opus-ultra | ✅ LEGIT | 55 | appdata v1.1.3 date 2022-1-16 breaks chronological order (appdata.xml) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

