# [SCRL-N01] __jitterMargin: fractional result from modulus violates 0/1 toggle design

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `Prompter.qml:114`
- **Consensus:** 1/6 agents LEGIT · split

## Original report claim

- **File:** Prompter.qml:114
- **Severity:** Medium
- **Analysis:** `(__tikTok+viewport.__baseSpeed+viewport.__curvature+fontSize)%2` — real operands produce fractional remainder via JS `%`. Designed as 0/1 subpixel toggle but yields arbitrary fractional values. Combined with FINAL-09 (__tikTok stuck at 0), jitter becomes static fraction from slider positions.
- **Impact:** Subpixel jitter function permanently broken; produces static fraction instead of alternating.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❔ UNSURE | 45 | __jitterMargin fractional from modulus; scroll-toggle design claim (Prompter.qml:114) |
| gpt | ❔ UNSURE | 39 | runtime/platform behavior is not decidable from the cited snippet (src/prompter/Prompter.qml:114) |
| deepseek | ⚠️ PARTIAL | 50 | modulus on mixed int/real types yields fractional; depends on jitter design intent (Prompter.qml:114) |
| glm | ⚠️ PARTIAL | 60 | Prompter.qml:114 __jitterMargin fractional result from modulus violates 0/1 toggle design |
| kimi | ✅ LEGIT | 80 | Prompter.qml:114 __jitterMargin uses %2 on real operands; with __tikTok stuck at 0 the remainder is a static offset instead of a toggling 0/1 subpixel jitter |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — __jitterMargin fractional from modulus; scroll-toggle design claim (Prompter.qml:114) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

