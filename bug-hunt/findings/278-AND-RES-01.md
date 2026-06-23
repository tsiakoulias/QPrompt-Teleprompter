# [278-AND-RES-01] Invalid android:scaleType on bitmap element

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `android/res/drawable/splash.xml:7`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** android/res/drawable/splash.xml:7
- **Severity:** Medium
- **Analysis:** scaleType is ImageView attribute, not valid on bitmap drawable. AAPT2 error.
- **Impact:** Build failure or silently ignored attribute.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | invalid android:scaleType on bitmap; needs res check (splash.xml:7) |
| gpt | ⚠️ PARTIAL | 58 | observed Invalid android:scaleType on bitmap element (android/res/drawable/splash.xml:7) |
| deepseek | ✅ LEGIT | 90 | android:scaleType is ImageView attribute not valid on <bitmap> drawable; AAPT2 error (android/res/drawable/splash.xml:7) |
| glm | ✅ LEGIT | 80 | android/res/drawable/splash.xml:7 invalid android:scaleType on bitmap element |
| kimi | ✅ LEGIT | 90 | android/res/drawable/splash.xml:7 uses android:scaleType on <bitmap>, which is not a valid attribute for bitmap drawable items. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — invalid android:scaleType on bitmap; needs res check (splash.xml:7) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

