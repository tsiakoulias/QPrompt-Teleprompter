# [FINAL-08] setup.sh vcvarsall.bat executed from bash — MSVC env not propagated

- **Status:** OPEN
- **Severity:** High
- **Category:** Platform/Build
- **Location:** `setup.sh:175`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** setup.sh:175
- **Severity:** High
- **Category:** Platform/Build
- **Analysis:** Windows .bat runs in isolated cmd.exe subprocess; env vars (PATH, INCLUDE, LIB) lost when subprocess exits.
- **Impact:** Windows build path in setup.sh completely broken; cmake can't find MSVC compiler.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 85 | vcvarsall.bat from bash loses env (setup.sh:175) |
| gpt | ✅ LEGIT | 84 | setup.sh vcvarsall.bat executed from bash - MSVC env not propagated (setup.sh:175) |
| deepseek | ✅ LEGIT | 95 | setup.sh:175 vcvarsall.bat executed as shell command in bash — runs in isolated cmd.exe MSVC env vars(INCLUDE/LIB/PATH) lost on subprocess exit |
| glm | ✅ LEGIT | 80 | setup.sh:175 vcvarsall.bat executed from bash; MSVC env vars not propagated to subsequent commands |
| kimi | ✅ LEGIT | 90 | setup.sh:175 runs vcvarsall.bat in a child cmd process; environment variables are lost before cmake is invoked. |
| opus-ultra | ✅ LEGIT | 85 | vcvarsall.bat from bash loses env (setup.sh:175) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

