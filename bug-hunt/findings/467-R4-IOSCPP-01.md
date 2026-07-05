# [467-R4-IOSCPP-01] QTemporaryDir created on all platforms including non-iOS where unused

- **Status:** OPEN
- **Severity:** Low
- **Category:** Resource Management
- **Location:** `src/iossavedialog.h:49`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** src/iossavedialog.h:49
- **Severity:** Low
- **Category:** Resource Management
- **Analysis:** QTemporaryDir m_tempDir by-value member — default constructor creates real temp directory on disk immediately. Non-iOS platforms: saveDocument no-op but directory still created.
- **Impact:** Unnecessary filesystem I/O and temporary directory creation on Windows, Linux, macOS, Android, WASM at every app start.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ⚠️ PARTIAL | 50 | QTemporaryDir by-value member on all platforms (iossavedialog.h:49) |
| gpt-5.5-xhigh | ⚠️ PARTIAL | 58 | observed QTemporaryDir created on all platforms including non-iOS where unused (src/iossavedialog.h:49) |
| deepseek-v4-pro-max | ✅ LEGIT | 90 | iossavedialog.h:49 QTemporaryDir m_tempDir by-value member — default constructor creates temp dir on ALL platforms even non-iOS |
| glm-5.2-xhigh | ⚠️ PARTIAL | 60 | iossavedialog.h:49 QTemporaryDir m_tempDir created on all platforms; unused on non-iOS but minimal waste |
| kimi-k2.7-code | ✅ LEGIT | 85 | iossavedialog.h:49 QTemporaryDir m_tempDir member default-constructs a real temp directory for every app start on all platforms. |
| opus-4.8-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — QTemporaryDir by-value member on all platforms (iossavedialog.h:49) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

