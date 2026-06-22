# [TMR-N06] Auto-reload Timer persists after network dialog close — background refetches

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `PrompterPage.qml:1246-1253,1415-1420`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** PrompterPage.qml:1246-1253,1415-1420
- **Severity:** Medium
- **Analysis:** onClosed doesn't set autoReloadRunning=false. Timer fires openFromRemote() in background with no visible UI.
- **Impact:** Unprompted network reloads continue indefinitely after dialog dismissed.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | auto-reload Timer persists after network dialog close (PrompterPage.qml:1246) |
| gpt | ✅ LEGIT | 78 | Auto-reload Timer persists after network dialog close - background refetches (src/kirigami_ui/PrompterPage.qml:1246) |
| deepseek | ✅ LEGIT | 90 | PrompterPage.qml:1246-1253 1415-1420: onClosed doesn't set autoReloadRunning=false; Timer keeps firing openFromRemote() without visible UI |
| glm | ✅ LEGIT | 70 | PrompterPage.qml:1246-1253 1415-1420 auto-reload Timer persists after network dialog close; background refetches |
| kimi | ✅ LEGIT | 85 | PrompterPage.qml:1246-1264 autoReloadTimer depends on autoReloadRunning, never reset on dialog close |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — auto-reload Timer persists after network dialog close (PrompterPage.qml:1246) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

