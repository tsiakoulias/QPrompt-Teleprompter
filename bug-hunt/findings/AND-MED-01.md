# [AND-MED-01] Missing intent-filter for opening files from other apps

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `AndroidManifest.xml:29-32`
- **Consensus:** 4/6 agents LEGIT · split

## Original report claim

- **File:** AndroidManifest.xml:29-32
- **Severity:** Medium
- **Analysis:** Only LAUNCHER intent-filter. No VIEW filter for text/html or text/plain. Cannot open .html scripts from file managers, email, or Downloads.
- **Impact:** No "Open with QPrompt" or "Share to QPrompt" on Android.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | missing intent-filter for opening files (AndroidManifest.xml:29) |
| gpt | ⚠️ PARTIAL | 58 | observed Missing intent-filter for opening files from other apps (android/AndroidManifest.xml:29) |
| deepseek | ✅ LEGIT | 95 | AndroidManifest.xml:29-32: only LAUNCHER intent-filter; no VIEW filter for text/html or text/plain — cannot open .html scripts from file managers/email/downloads |
| glm | ✅ LEGIT | 75 | AndroidManifest.xml:29-32 missing intent-filter for opening files from other apps |
| kimi | ✅ LEGIT | 95 | AndroidManifest.xml:29-32 only MAIN/LAUNCHER; missing VIEW intent-filter for opening files. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — missing intent-filter for opening files (AndroidManifest.xml:29) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

