# [514-COLOR-CRIT-01] selectionColor #333d9ef3 — alpha channel reversed (#AARRGGBB vs #RRGGBBAA), selection invisible

- **Status:** REJECTED
- **Severity:** High
- **Category:** 
- **Location:** `Prompter.qml:973-974`
- **Consensus:** 3/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** Prompter.qml:973-974
- **Severity:** High
- **Analysis:** Qt parses 8-char hex as #AARRGGBB. #333d9ef3 = AA=0x33 → alpha≈20%. Developer likely intended CSS-style #RRGGBBAA with alpha 0xf3=95%. Both selectionColor and selectedTextColor at ~20% opacity — practically invisible on any background.
- **Impact:** Text selection outside find mode is effectively invisible. Users cannot see what they've highlighted during normal editing.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ❔ UNSURE | 45 | #333d9ef3 is valid #AARRGGBB (20% blue); 'reversed alpha' likely intentional (Prompter.qml:973) |
| gpt-5.5-xhigh | ❔ UNSURE | 39 | #333d9ef3 is syntactically AARRGGBB; intent is uncertain (src/prompter/Prompter.qml:973) |
| deepseek-v4-pro-max | ✅ LEGIT | 95 | Prompter.qml:973-974: #333d9ef3 uses #AARRGGBB format but dev likely intended #RRGGBBAA; AA=0x33=20% alpha nearly invisible |
| glm-5.2-xhigh | ✅ LEGIT | 80 | Prompter.qml:973-974 selectionColor #333d9ef3 has alpha channel reversed (#AARRGGBB vs #RRGGBBAA); selection invisible |
| kimi-k2.7-code | ✅ LEGIT | 90 | Prompter.qml:973-974 #333d9ef3 interpreted by Qt as AARRGGBB (alpha 0x33) making selection nearly invisible. |
| opus-4.8-ultra | ❌ FALSE | 72 | max: code correct / claim mischaracterized — #333d9ef3 is valid #AARRGGBB (20% blue); 'reversed alpha' likely intentional (Prompter.qml |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

