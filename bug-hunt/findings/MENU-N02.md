# [MENU-N02] Mobile "Add to dictionary" missing %1 placeholder — word never shown

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `Prompter.qml:2620`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** Prompter.qml:2620
- **Severity:** Medium
- **Analysis:** `qsTr("Add to dictionary", ...).arg(prompter.spellMisspelledWord)` — no `%1` in string. arg() silently does nothing. Desktop version has `qsTr("Add \"%1\" to dictionary", ...)`.
- **Impact:** Users see "Add to dictionary" with no indication of which word.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 60 | mobile 'Add to dictionary' qsTr missing %1; word never shown (Prompter.qml:2620) |
| gpt | ⚠️ PARTIAL | 58 | observed Mobile "Add to dictionary" missing %1 placeholder - word never shown (src/prompter/Prompter.qml:2620) |
| deepseek | ✅ LEGIT | 95 | Prompter.qml:2620: qsTr('Add to dictionary') has no %1 placeholder; .arg(prompter.spellMisspelledWord) silently does nothing — word never shown to user |
| glm | ✅ LEGIT | 80 | Prompter.qml:2620 'Add to dictionary' uses .arg() but qsTr string may lack %1 placeholder; word never shown |
| kimi | ✅ LEGIT | 90 | Prompter.qml:2620 qsTr('Add to dictionary').arg(word) has no %1 placeholder, so the misspelled word is never shown. |
| opus-ultra | ✅ LEGIT | 60 | mobile 'Add to dictionary' qsTr missing %1; word never shown (Prompter.qml:2620) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

