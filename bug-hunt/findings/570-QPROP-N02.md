# [570-QPROP-N02] comesFromNetwork Q_PROPERTY missing WRITE clause

- **Status:** REJECTED
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.h:121`
- **Consensus:** 3/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** documenthandler.h:121
- **Severity:** Medium
- **Analysis:** `setDocumentComesFromNetwork()` exists (public, emits NOTIFY, called from C++), but WRITE absent from Q_PROPERTY declaration. Read-only to QML property system.
- **Impact:** Any QML attempting to set comesFromNetwork silently fails.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ❌ FALSE | 50 | comesFromNetwork is intentionally read-only; WRITE not needed (documenthandler.h:121) |
| gpt-5.5-xhigh | ❌ FALSE | 76 | comesFromNetwork is exposed read-only; no WRITE is required (src/documenthandler.h:121) |
| deepseek-v4-pro-max | ✅ LEGIT | 95 | documenthandler.h:121: Q_PROPERTY comesFromNetwork missing WRITE; setDocumentComesFromNetwork() exists (called at cpp:896) but QML property system sees read-only |
| glm-5.2-xhigh | ✅ LEGIT | 75 | documenthandler.h:121 comesFromNetwork Q_PROPERTY missing WRITE clause; read-only but setDocumentComesFromNetwork exists |
| kimi-k2.7-code | ✅ LEGIT | 80 | documenthandler.h:121 comesFromNetwork Q_PROPERTY lacks WRITE despite setDocumentComesFromNetwork existing and emitting NOTIFY. |
| opus-4.8-ultra | ❌ FALSE | 50 | comesFromNetwork is intentionally read-only; WRITE not needed (documenthandler.h:121) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

