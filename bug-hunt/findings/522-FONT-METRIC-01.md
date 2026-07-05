# [522-FONT-METRIC-01] pixelSize used as line-height proxy — core scroll timing off by ~57%

- **Status:** NEEDS-INFO
- **Severity:** High
- **Category:** 
- **Location:** `Prompter.qml:119-122,125,128`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** Prompter.qml:119-122,125,128
- **Severity:** High
- **Analysis:** font.pixelSize is em-size, not rendered line height. For DejaVu Sans at 14px, actual height is ~22px (1.57×). Every scroll calculation using fontSize as line-height proxy is wrong: __relativeSpeed ~57% slower, __destination stops ~1 line short, __atEnd detection fires wrong.
- **Impact:** Core teleprompter scroll speed, ETA display, and end-of-document detection all miscalibrated. Primary feature accuracy compromised.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ❔ UNSURE | 40 | pixelSize-as-lineheight scroll-timing heuristic; '57%' unverifiable (Prompter.qml:119) |
| gpt-5.5-xhigh | ❔ UNSURE | 39 | runtime/platform behavior is not decidable from the cited snippet (src/prompter/Prompter.qml:119) |
| deepseek-v4-pro-max | ✅ LEGIT | 90 | Prompter.qml:119-122: fontSize (pixelSize=em-size) used as line-height proxy; actual height ~1.57x; __relativeSpeed ~57% off |
| glm-5.2-xhigh | ✅ LEGIT | 75 | Prompter.qml:119-122 125 128 pixelSize used as line-height proxy; core scroll timing off by ~57% |
| kimi-k2.7-code | ✅ LEGIT | 75 | Prompter.qml:119-122 scroll timing uses editor.font.pixelSize, not the actual rendered line height |
| opus-4.8-ultra | ❔ UNSURE | 40 | max: unverifiable statically (runtime/semantic) — pixelSize-as-lineheight scroll-timing heuristic; '57%' unverifiable (Prompter.qml:119) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

