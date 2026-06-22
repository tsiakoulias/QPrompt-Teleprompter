# [CMT-N05] Missing security warning on QProcess RCE sink (sys://)

- **Status:** REJECTED
- **Severity:** High
- **Category:** 
- **Location:** `qmlutil.hpp:84-95`
- **Consensus:** 1/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** qmlutil.hpp:84-95
- **Severity:** High
- **Analysis:** `run()` executes arbitrary commands via QProcess::startDetached. No comment warns of security implications or unsanitized input. Bug: SEC-01.
- **Impact:** Dangerous code sink with no annotation for future maintainers.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 40 | only a missing security-comment note on the sys:// RCE sink (qmlutil.hpp:84) |
| gpt | ⚠️ PARTIAL | 48 | comment problem observed, but defect impact is limited (src/qmlutil.hpp:84) |
| deepseek | ✅ LEGIT | 85 | No security comment on QProcess::startDetached at qmlutil.hpp:91 — sys:// RCE sink unannotated |
| glm | ⚠️ PARTIAL | 60 | qmlutil.hpp:84-95 missing security warning on QProcess RCE sink for sys:// URIs |
| kimi | ❌ FALSE | 75 | missing security comment on qmlutil.hpp:84 run() is documentation debt; the actual RCE is captured by SEC-01. |
| opus-ultra | ❌ FALSE | 72 | max: code correct / claim mischaracterized — only a missing security-comment note on the sys:// RCE sink (qmlutil.hpp:84) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

