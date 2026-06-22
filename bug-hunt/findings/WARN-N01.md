# [WARN-N01] SpellHighlighter::isEnabled() — dead code, never called

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `spellhighlighter.h:36`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** spellhighlighter.h:36
- **Severity:** Low
- **Analysis:** Public method defined but zero invocations in entire codebase.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 40 | SpellHighlighter::isEnabled dead, never called (spellhighlighter.h:36) |
| gpt | ⚠️ PARTIAL | 58 | observed SpellHighlighter::isEnabled() - dead code, never called (src/spellhighlighter.h:36) |
| deepseek | ✅ LEGIT | 80 | spellhighlighter.h:36: isEnabled() public method never called anywhere in codebase; setEnabled() is called but isEnabled() is dead code |
| glm | ✅ LEGIT | 75 | spellhighlighter.h:36 isEnabled() dead code never called |
| kimi | ✅ LEGIT | 70 | spellhighlighter.h:36 SpellHighlighter::isEnabled() is defined but never invoked anywhere in the codebase. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — SpellHighlighter::isEnabled dead |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

