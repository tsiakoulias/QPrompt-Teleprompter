# [EVT-N13] rewind()/fastForward() event undefined — winding state permanently locked after first use

- **Status:** NEEDS-INFO
- **Severity:** High
- **Category:** 
- **Location:** `Prompter.qml:547-571`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** Prompter.qml:547-571
- **Severity:** High
- **Analysis:** Functions take no event parameter. `keyBeingPressed = event.key` accesses `.key` on undefined → TypeError. keyBeingPressed stays at default 0. In Keys.onReleased, `event.key===keyBeingPressed` always fails (0 ≠ any real key). winding never cleared back to false.
- **Impact:** After pressing rewind or fast-forward once, hold-to-continue functionality permanently broken. Release-detection dead.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❔ UNSURE | 45 | rewind()/fastForward() event-undefined claim; needs function body (Prompter.qml:547) |
| gpt | ⚠️ PARTIAL | 58 | observed rewind()/fastForward() event undefined - winding state permanently locked after first use (src/prompter/Prompter.qml:547) |
| deepseek | ✅ LEGIT | 95 | Prompter.qml:547-571: rewind/fastForward access 'event.key' but accept no event parameter; event=undefined; winding permanently locked |
| glm | ✅ LEGIT | 75 | Prompter.qml:547-571 rewind()/fastForward() reference event.key but declare no event parameter; undefined |
| kimi | ✅ LEGIT | 90 | Prompter.qml:552/565 reference `event.key` inside functions that have no `event` parameter |
| opus-ultra | ❔ UNSURE | 45 | max: unverifiable statically (runtime/semantic) — rewind()/fastForward() event-undefined claim; needs function body (Prompter.qml:547) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

