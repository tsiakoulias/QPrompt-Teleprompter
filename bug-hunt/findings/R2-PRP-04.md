# [R2-PRP-04] Inconsistent focus restoration in decreaseVelocityButton

- **Status:** OPEN
- **Severity:** Low
- **Category:** Type Safety
- **Location:** `src/kirigami_ui/PrompterPage.qml:89`
- **Consensus:** 2/6 agents LEGIT · split

## Original report claim

- **File:** src/kirigami_ui/PrompterPage.qml:89
- **Severity:** Low
- **Category:** Type Safety
- **Analysis:** Every other action's onTriggered (53 occurrences, including paired increaseVelocityButton at line 102) calls `viewport.prompter.restoreFocus()`. Line 89 uniquely uses `viewport.prompter.focus = true`. `restoreFocus()` likely restores prior focus location; simple focus assignment moves it to viewport directly.
- **Impact:** After decrease-velocity button, focus moves to prompter viewport instead of prior location (e.g., editor). User must tap back to continue typing.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 50 | decreaseVelocityButton focus assign vs restoreFocus() (PrompterPage.qml:89) |
| gpt | ⚠️ PARTIAL | 58 | observed Inconsistent focus restoration in decreaseVelocityButton (src/kirigami_ui/PrompterPage.qml:89) |
| deepseek | ❔ UNSURE | 35 | Inconsistent focus restoration at PrompterPage.qml:89; need full QML context to verify intent vs bug |
| glm | ⚠️ PARTIAL | 55 | PrompterPage.qml:89 focus restoration in decreaseVelocityButton uses prompter.focus=true instead of restoreFocus(); minor inconsistency |
| kimi | ✅ LEGIT | 75 | PrompterPage.qml:89 decreaseVelocityButton sets focus=true instead of restoreFocus() used by increaseVelocityButton. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — decreaseVelocityButton focus assign vs restoreFocus() (PrompterPage.qml:89) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

