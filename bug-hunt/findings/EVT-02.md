# [EVT-02] Zero inputMethodHints on any TextField — IME broken for CJK/Indic

- **Status:** REJECTED
- **Severity:** High
- **Category:** 
- **Location:** `Prompter.qml:936, PrompterPage.qml, EditorToolbar.qml (15+ TextFields)`
- **Consensus:** 3/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** Prompter.qml:936, PrompterPage.qml, EditorToolbar.qml (15+ TextFields)
- **Severity:** High
- **Analysis:** No inputMethodHints on any field. Virtual keyboard can't show correct layout. CJK composition events blocked.
- **Impact:** CJK/Indic users cannot compose. Mobile keyboard shows wrong layout. Accessibility barrier.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❌ FALSE | 55 | zero inputMethodHints = ImhNone = default; IME works, not broken (Prompter.qml:936) |
| gpt | ⚠️ PARTIAL | 58 | observed Zero inputMethodHints on any TextField - IME broken for CJK/Indic (src/prompter/Prompter.qml:936) |
| deepseek | ✅ LEGIT | 88 | zero inputMethodHints on all TextFields; CJK/Indic IME composition broken (Prompter.qml:936 EditorToolbar PrompterPage) |
| glm | ✅ LEGIT | 80 | Prompter.qml:936 etc TextFields have no inputMethodHints; IME broken for CJK/Indic input |
| kimi | ✅ LEGIT | 85 | No QML file in src/ sets inputMethodHints on any TextField/TextArea, breaking CJK/Indic IME input. |
| opus-ultra | ❌ FALSE | 55 | zero inputMethodHints = ImhNone = default; IME works |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

