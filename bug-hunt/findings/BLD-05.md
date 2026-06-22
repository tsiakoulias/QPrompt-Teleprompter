# [BLD-05] .env.android references Qt 5.15.2 — project requires Qt 6.8.2+

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `.env.android:6`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** .env.android:6
- **Severity:** Medium
- **Analysis:** `export Qt5_android=$ADIR/Qt/5.15.2/android/` — stale Qt 5 configuration.
- **Impact:** Android builds fail for developers following this file.

---

### QML Events / Interaction (10 bugs)

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 55 | .env.android references Qt 5.15.2; project needs 6.8.2+ (.env.android:6) |
| gpt | ✅ LEGIT | 78 | .env.android references Qt 5.15.2 - project requires Qt 6.8.2+ (env.android:6) |
| deepseek | ✅ LEGIT | 95 | .env.android line 6:export Qt5_android=Qt/5.15.2 but project requires Qt 6.8.2+ (.env.android:6 CMakeLists.txt:57) |
| glm | ✅ LEGIT | 85 | .env.android:6 references Qt 5.15.2 but CMakeLists.txt:57 requires Qt 6.8.2 |
| kimi | ✅ LEGIT | 95 | .env.android:6 sets Qt5_android to Qt/5.15.2/android/, but CMakeLists.txt requires Qt 6.8.2+. |
| opus-ultra | ✅ LEGIT | 55 | .env.android references Qt 5.15.2; project needs 6.8.2+ (.env.android:6) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

