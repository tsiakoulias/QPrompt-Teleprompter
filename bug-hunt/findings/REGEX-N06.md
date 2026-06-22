# [REGEX-N06] imgSrcRegex captures wrong src when data-src follows real src

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `documenthandler.cpp:1432-1434`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** documenthandler.cpp:1432-1434
- **Severity:** Medium
- **Analysis:** Pattern `[^>]+` is greedy. For `<img src="real.jpg" data-src="lazy.jpg">`, backtracks to last `src=` occurrence (inside data-src), capturing lazy.jpg. Should use `[^>]+?` or word boundary before `src`.
- **Impact:** Wrong (lazy/placeholder) image URL loaded for images with lazy-load attributes.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 55 | imgSrcRegex 'src' also matches inside data-src= (documenthandler.cpp:1432) |
| gpt | ✅ LEGIT | 78 | imgSrcRegex captures wrong src when data-src follows real src (src/documenthandler.cpp:1432) |
| deepseek | ✅ LEGIT | 90 | documenthandler.cpp:1432-1434: imgSrcRegex [^>]+ is greedy; for <img src='real' data-src='lazy'> backtracks to last src= inside data-src — wrong URL captured |
| glm | ✅ LEGIT | 75 | documenthandler.cpp:1432-1434 imgSrcRegex captures wrong src when data-src follows real src |
| kimi | ✅ LEGIT | 85 | documenthandler.cpp:1432-1434 imgSrcRegex greedily matches '[^>]+', backtracking to data-src= and capturing the lazy image URL. |
| opus-ultra | ✅ LEGIT | 55 | imgSrcRegex 'src' also matches inside data-src= (documenthandler.cpp:1432) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

