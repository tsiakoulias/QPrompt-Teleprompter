# [XML-N01] android:background="#303030" invalid on \<activity\> — silently ignored

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `AndroidManifest.xml:26`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** AndroidManifest.xml:26
- **Severity:** Medium
- **Analysis:** android:background is a View/layout attribute, not valid on activity elements. Ignored by Android platform. Needs android:theme with windowBackground instead.
- **Impact:** Activity flashes white/system-default on launch instead of intended dark #303030.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 55 | android:background invalid on <activity>; silently ignored (AndroidManifest.xml:26) |
| gpt | ✅ LEGIT | 92 | android:background="#303030" invalid on \activity\ - silently ignored (android/AndroidManifest.xml:26) |
| deepseek | ✅ LEGIT | 90 | AndroidManifest.xml:26: android:background is View/layout attribute invalid on activity element; silently ignored — should use android:theme with windowBackground |
| glm | ✅ LEGIT | 75 | AndroidManifest.xml:26 android:background='#303030' invalid on <activity>; silently ignored |
| kimi | ✅ LEGIT | 90 | AndroidManifest.xml:26 sets android:background on activity element; it is invalid and ignored. |
| opus-ultra | ✅ LEGIT | 55 | android:background invalid on <activity>; silently ignored (AndroidManifest.xml:26) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

