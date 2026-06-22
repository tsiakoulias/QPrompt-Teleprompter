# [R4-EXP-09] LibreOffice import --cat and --convert-to flags are contradictory

- **Status:** OPEN
- **Severity:** Low
- **Category:** Logic
- **Location:** `src/documenthandler.cpp:1076`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** src/documenthandler.cpp:1076
- **Severity:** Low
- **Category:** Logic
- **Analysis:** --cat dumps to stdout; --convert-to writes to file. These conflict — --convert-to suppresses stdout. Code reads from stdout expecting --cat behavior but LibreOffice may produce nothing.
- **Impact:** LibreOffice imports may produce empty output depending on version.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 55 | --cat and --convert-to are contradictory soffice flags (documenthandler.cpp:1076) |
| gpt | ⚠️ PARTIAL | 58 | observed LibreOffice import --cat and --convert-to flags are contradictory (src/documenthandler.cpp:1076) |
| deepseek | ✅ LEGIT | 85 | documenthandler.cpp:1076 --cat(pipe to stdout) and --convert-to(write file) are contradictory flags — LibreOffice may produce empty stdout |
| glm | ⚠️ PARTIAL | 65 | documenthandler.cpp:1076 --cat and --convert-to are both passed to LibreOffice; --cat outputs to stdout but --convert-to writes to file |
| kimi | ✅ LEGIT | 85 | LibreOffice arguments include both --cat and --convert-to which are mutually contradictory; documenthandler.cpp:1076 |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — --cat and --convert-to are contradictory soffice flags (documenthandler.cpp:1076) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

