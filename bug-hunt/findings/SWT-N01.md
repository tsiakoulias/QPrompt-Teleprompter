# [SWT-N01] OBS WebSocket Switch checked binding broken on first toggle

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `PrompterPage.qml:1468-1474`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** PrompterPage.qml:1468-1474
- **Severity:** Medium
- **Analysis:** `checked: viewport.prompter.ws.active` + `onToggled: viewport.prompter.ws.active = checked`. User toggle severs declarative binding. If WebSocket disconnects, ws.active=false but Switch still shows ON. Same class as R2-EDT-03.
- **Impact:** UI state mismatch — OBS Switch shows connected when actually disconnected.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 60 | OBS Switch checked binding broken on first toggle (checkable family) (PrompterPage.qml:1468) |
| gpt | ✅ LEGIT | 78 | OBS WebSocket Switch checked binding broken on first toggle (src/kirigami_ui/PrompterPage.qml:1468) |
| deepseek | ✅ LEGIT | 95 | PrompterPage.qml:1468-1474: checked: ws.active binding severed on first user toggle via onToggled assignment; classic declarative->imperative binding destruction — UI mismatch |
| glm | ✅ LEGIT | 75 | PrompterPage.qml:1468-1474 OBS WebSocket Switch checked binding broken on first toggle |
| kimi | ✅ LEGIT | 90 | PrompterPage.qml:1473-1474 Switch onToggled assignment breaks checked binding to ws.active. |
| opus-ultra | ✅ LEGIT | 60 | OBS Switch checked binding broken on first toggle (checkable family) (PrompterPage.qml:1468) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

