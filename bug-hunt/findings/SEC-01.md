# [SEC-01] Arbitrary Command Execution via `sys://` Marker URIs

- **Status:** OPEN
- **Severity:** Critical
- **Category:** 
- **Location:** `src/prompter/Prompter.qml:415-416, src/qmlutil.hpp:84-94`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** src/prompter/Prompter.qml:415-416, src/qmlutil.hpp:84-94
- **Severity:** Critical
- **Code:**
  ```cpp
  Q_INVOKABLE void run(const QString &command) {
      QStringList parts = QProcess::splitCommand(command);
      const QString program = parts.takeFirst();
      QProcess::startDetached(program, parts);
  }
  ```
  ```qml
  else if (m.url.startsWith("sys://"))
      qmlutil.run(m.url.slice(6));
  ```
- **Analysis:** The prompter scrolls past markers and checks `m.url`. If URL starts with `sys://`, the rest is passed to `QProcess::startDetached()` with zero sanitization. A crafted `.html` file with `<a href="sys://malicious">` causes arbitrary command execution when the prompter scrolls past it.
- **Impact:** Remote code execution via shared prompter script files. Any document containing `sys://` anchor hrefs achieves arbitrary command execution with user privileges.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 95 | sys:// marker -> QProcess::startDetached unsanitized (qmlutil.hpp:84) |
| gpt | ✅ LEGIT | 84 | Arbitrary Command Execution via sys:// Marker URIs (src/prompter/Prompter.qml:415) |
| deepseek | ✅ LEGIT | 75 | sys:// URLs passed to QProcess::startDetached at qmlutil.hpp:84-94 via Prompter.qml:415-416; no sanitization — genuine RCE risk from crafted documents |
| glm | ✅ LEGIT | 85 | Prompter.qml:415-416 qmlutil.run(m.url.slice(6)) for sys:// URIs passes arbitrary command to QProcess::startDetached (qmlutil.hpp:84-94) |
| kimi | ✅ LEGIT | 95 | Prompter.qml:415-416 slices sys:// URI and passes to qmlutil.run; qmlutil.hpp:84-94 executes via QProcess::startDetached. |
| opus-ultra | ✅ LEGIT | 95 | sys:// marker -> QProcess::startDetached unsanitized (qmlutil.hpp:84) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

