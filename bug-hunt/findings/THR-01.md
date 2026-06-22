# [THR-01] IosSaveDialog::create() — unsynchronized singleton race

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `iossavedialog.cpp:37-42`
- **Consensus:** 2/6 agents LEGIT · split

## Original report claim

- **File:** iossavedialog.cpp:37-42
- **Severity:** Medium
- **Analysis:** Classic check-then-act: `if (!s_instance) s_instance = new ...` with no mutex. Constructor writes s_instance=this before construction done. Two QML engine threads → dual instance or partially-constructed object.
- **Impact:** Use-after-free or double-delete under concurrent engine access.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | IosSaveDialog::create unsynchronized singleton race; single-threaded (iossavedialog.cpp:37) |
| gpt | ⚠️ PARTIAL | 58 | observed IosSaveDialog::create() - unsynchronized singleton race (src/iossavedialog.cpp:37) |
| deepseek | ✅ LEGIT | 82 | QML singleton create() runs on main thread; check-then-act pattern is sloppy but not currently racy (iossavedialog.cpp:37-42) |
| glm | ⚠️ PARTIAL | 65 | iossavedialog.cpp:37-42 create() singleton without synchronization; race condition |
| kimi | ✅ LEGIT | 85 | iossavedialog.cpp:39-40 checks !s_instance then assigns in create() with no mutex, creating a check-then-act race. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — IosSaveDialog::create unsynchronized singleton race; single-threaded (iossavedialog.cpp:37 |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

