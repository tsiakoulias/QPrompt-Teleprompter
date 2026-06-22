# [SEC-02] OBS WebSocket Password Stored in Plaintext

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `src/prompter/Prompter.qml:275-280, src/kirigami_ui/PrompterPage.qml:1496-1506`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/prompter/Prompter.qml:275-280, src/kirigami_ui/PrompterPage.qml:1496-1506
- **Severity:** Medium
- **Code:**
  ```qml
  Settings {
      category: "obs"
      property alias password: ws.password
  }
  ```
- **Analysis:** The OBS WebSocket password is stored via QSettings in plaintext (Windows registry `HKCU\Software\Cuperino\qprompt\obs\password`; Linux `~/.config/Cuperino/qprompt.conf`). No encryption.
- **Impact:** Any process running as the same user can read the OBS WebSocket password.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 85 | OBS password plaintext QSettings (Prompter.qml:279) |
| gpt | ✅ LEGIT | 78 | OBS WebSocket Password Stored in Plaintext (src/prompter/Prompter.qml:275) |
| deepseek | ✅ LEGIT | 90 | OBS WebSocket password stored via QSettings plaintext in Prompter.qml:275-280; Windows registry/HKCU Linux ~/.config — no encryption |
| glm | ✅ LEGIT | 85 | Prompter.qml:275-280 OBS WebSocket password stored in QML property as plaintext string |
| kimi | ✅ LEGIT | 85 | PrompterPage.qml:1496-1506 / Prompter.qml:275-280 alias OBS password into QSettings without encryption. |
| opus-ultra | ✅ LEGIT | 85 | OBS password plaintext QSettings (Prompter.qml:279) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

