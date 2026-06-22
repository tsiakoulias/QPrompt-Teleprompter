# [REGEX-N02] regex_5 accidentally excludes 15+ HTML5 tags from background-color filtering

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.cpp:1300`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** documenthandler.cpp:1300
- **Severity:** Medium
- **Analysis:** `[^sS][^pP][^aA][^nN]` excludes all tags starting with s/p/a/n. Also excludes `<strong>`, `<script>`, `<style>`, `<svg>`, `<section>`, `<source>` etc. These retain unwanted background colors after filtering.
- **Impact:** Pasted HTML from rich editors may retain background colors on these elements.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 55 | regex_5 [^sS][^pP][^aA][^nN] is a flawed 'not span' construct (documenthandler.cpp:1300) |
| gpt | ✅ LEGIT | 78 | regex5 accidentally excludes 15+ HTML5 tags from background-color filtering (src/documenthandler.cpp:1300) |
| deepseek | ✅ LEGIT | 80 | [^sS][^pP][^aA][^nN] at documenthandler.cpp:1300 excludes <strong> <script> <svg> etc from bg-color filter |
| glm | ✅ LEGIT | 80 | documenthandler.cpp:1300 regex_5 excludes 15+ HTML5 tags from background-color filtering due to [^sS][^pP][^aA][^nN] pattern |
| kimi | ✅ LEGIT | 95 | filterHtml regex_5 at documenthandler.cpp:1300 uses <[^sS][^pP][^aA][^nN], excluding strong/script/style/svg/section/source and leaking background colors |
| opus-ultra | ✅ LEGIT | 55 | regex_5 [^sS][^pP][^aA][^nN] is a flawed 'not span' construct (documenthandler.cpp:1300) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

