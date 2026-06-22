# [SEC-05] User-Controlled Filename Passed to QProcess (LibreOffice import)

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `src/documenthandler.cpp:1076-1077`
- **Consensus:** 2/6 agents LEGIT · split

## Original report claim

- **File:** src/documenthandler.cpp:1076-1077
- **Severity:** Medium
- **Code:**
  ```cpp
  arguments << QLatin1String("--cat") << QLatin1String("--convert-to")
            << QLatin1String("html:HTML") << fileName;
  convert.start(program, arguments);
  ```
- **Analysis:** The file name from the opened URL is appended directly to QProcess arguments. A file named `--help.odt` would be interpreted as a flag by LibreOffice. On Windows, QProcess uses `CreateProcess` command-line conversion which has known escaping edge cases.
- **Impact:** Flag injection in LibreOffice; potential command injection on Windows.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 55 | filename to LibreOffice args; flag injection minor (documenthandler.cpp:1076) |
| gpt | ⚠️ PARTIAL | 58 | observed User-Controlled Filename Passed to QProcess (LibreOffice import) (src/documenthandler.cpp:1076) |
| deepseek | ✅ LEGIT | 70 | User-controlled fileName appended to QProcess args at doc.cpp:1076-1077; file named --help.odt would inject flags into LibreOffice — flag injection confirmed |
| glm | ⚠️ PARTIAL | 70 | documenthandler.cpp:1076-1077 filename passed to QProcess but it comes from user file dialog not arbitrary input |
| kimi | ✅ LEGIT | 85 | documenthandler.cpp:1076-1077 appends user-supplied filename to LibreOffice QProcess args enabling flag injection. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — filename to LibreOffice args; flag injection minor (documenthandler.cpp:1076) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

