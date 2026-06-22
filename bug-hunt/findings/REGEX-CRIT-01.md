# [REGEX-CRIT-01] regex_4 destroys <body> tag — removes opening tag instead of color attributes

- **Status:** NEEDS-INFO
- **Severity:** High
- **Category:** 
- **Location:** `documenthandler.cpp:1287`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** documenthandler.cpp:1287
- **Severity:** High
- **Analysis:** Pattern matches from `<body` through last color attribute quote but doesn't consume `>`. replace() deletes everything from `<body` to last `"`, leaving orphaned `>content</body>`. Intended approach (commented-out loop) surgically removes one color at a time.
- **Impact:** HTML body tag destroyed; content after replacement is corrupted HTML.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❔ UNSURE | 45 | regex_4 may strip <body> opening tag; complex regex, hard to confirm (documenthandler.cpp:1287) |
| gpt | ❔ UNSURE | 39 | the body-tag regex is complex; impact needs sample HTML (src/documenthandler.cpp:1287) |
| deepseek | ✅ LEGIT | 85 | documenthandler.cpp:1287: regex_4 matches <body through last color attribute quote but stops before >; replace removes opening tag leaving orphaned >content</body> — corrupted HTML |
| glm | ✅ LEGIT | 80 | documenthandler.cpp:1287 regex_4 destroys <body> tag; removes opening tag instead of just color attributes |
| kimi | ✅ LEGIT | 90 | documenthandler.cpp:1287 regex_4 replace deletes from '<body' through last matched quote, destroying the opening body tag. |
| opus-ultra | ❔ UNSURE | 45 | max: unverifiable statically (runtime/semantic) — regex_4 may strip <body> opening tag; complex regex |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

