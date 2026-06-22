# [INT-N04] OBS URL/Password fields disabled when WebSocket enabled — inverted logic

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `PrompterPage.qml:1478,1500`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** PrompterPage.qml:1478,1500
- **Severity:** Medium
- **Analysis:** `wsUrlField.enabled: !enabledToggle.checked` — when WebSocket is ON, fields become disabled. Should be always editable or enabled when disconnected.
- **Impact:** Cannot reconfigure OBS connection without first disabling it.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 55 | OBS URL/Password fields disabled when WebSocket enabled; inverted (PrompterPage.qml:1478) |
| gpt | ⚠️ PARTIAL | 58 | observed OBS URL/Password fields disabled when WebSocket enabled - inverted logic (src/kirigami_ui/PrompterPage.qml:1478) |
| deepseek | ✅ LEGIT | 85 | PrompterPage.qml:1484: wsUrlField.enabled: !enabledToggle.checked; fields disabled when WebSocket on; cannot reconfigure without disconnect |
| glm | ✅ LEGIT | 75 | PrompterPage.qml:1478 1500 OBS URL/Password fields disabled when WebSocket enabled; inverted logic |
| kimi | ✅ LEGIT | 85 | PrompterPage.qml:1484,1500 wsUrlField/wsPasswordField.enabled: !enabledToggle.checked — disabled when connection ON. |
| opus-ultra | ✅ LEGIT | 55 | OBS URL/Password fields disabled when WebSocket enabled; inverted (PrompterPage.qml:1478) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

