# [499-TXT-CRIT] Plain 'v'/'V' keypress silently consumed — letter 'v' cannot be typed

- **Status:** NEEDS-INFO
- **Severity:** Critical
- **Category:** 
- **Location:** `Prompter.qml:2163-2168`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** Prompter.qml:2163-2168
- **Severity:** Critical
- **Analysis:** In no-modifiers branch, `case Qt.Key_V:` catches every plain 'v', Shift+'v', Alt+'v' and forwards to prompter handler where Ctrl modifier check fails → nothing happens. Letter silently discarded. Copy-paste error from Ctrl+modifier block where `case Qt.Key_V` correctly handles Ctrl+V paste.
- **Impact:** Letter 'v' cannot be typed anywhere in scripts — ~1% of English characters lost. Documents requiring "very", "voice", "video" etc. impossible to type.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ❔ UNSURE | 45 | Key_V consumed only matters if handler active in editing mode; likely state-gated (Prompter.qml:2166) |
| gpt-5.5-xhigh | ❔ UNSURE | 39 | runtime/platform behavior is not decidable from the cited snippet (src/prompter/Prompter.qml:2163) |
| deepseek-v4-pro-max | ✅ LEGIT | 85 | Prompter.qml:2163-2168: no-modifiers branch case Qt.Key_V forwards to prompter handler which only handles Ctrl+V paste; plain v keypress silently discarded — cannot type letter v |
| glm-5.2-xhigh | ✅ LEGIT | 80 | Prompter.qml:2163-2168 bare 'v'/'V' keypress forwarded to prompter even with no modifiers; letter 'v' cannot be typed in editor |
| kimi-k2.7-code | ✅ LEGIT | 95 | Prompter.qml:2163-2168 consumes plain Qt.Key_V and forwards to prompter handler, which has no action for unmodified 'v'; letter cannot be typed. |
| opus-4.8-ultra | ❔ UNSURE | 45 | max: unverifiable statically (runtime/semantic) — Key_V consumed only matters if handler active in editing mode; likely state-gated (Prompte |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

