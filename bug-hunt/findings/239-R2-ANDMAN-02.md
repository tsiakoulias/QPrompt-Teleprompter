# [239-R2-ANDMAN-02] MANAGE_EXTERNAL_STORAGE likely triggers Play Store scrutiny

- **Status:** OPEN
- **Severity:** Medium
- **Category:** Platform/Build
- **Location:** `android/AndroidManifest.xml:49`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** android/AndroidManifest.xml:49
- **Severity:** Medium
- **Category:** Platform/Build
- **Analysis:** MANAGE_EXTERNAL_STORAGE is an All Files Access permission restricted by Google Play policy. Apps must submit declaration proving core functionality requires broad file access. Teleprompter unlikely to qualify.
- **Impact:** Play Store rejection risk unless app has justified and approved use case. READ_EXTERNAL_STORAGE alone usually sufficient.

---

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus-4.8-extra | ✅ LEGIT | 85 | MANAGE_EXTERNAL_STORAGE Play-policy risk (AndroidManifest.xml:49) |
| gpt-5.5-xhigh | ✅ LEGIT | 78 | MANAGE_EXTERNAL_STORAGE likely triggers Play Store scrutiny (android/AndroidManifest.xml:49) |
| deepseek-v4-pro-max | ✅ LEGIT | 90 | AndroidManifest.xml:49: MANAGE_EXTERNAL_STORAGE is All Files Access restricted by Google Play policy requiring justification; teleprompter unlikely to qualify |
| glm-5.2-xhigh | ✅ LEGIT | 80 | AndroidManifest.xml:49 MANAGE_EXTERNAL_STORAGE triggers Play Store scrutiny and requires declaration |
| kimi-k2.7-code | ⚠️ PARTIAL | 55 | AndroidManifest.xml:49 declares MANAGE_EXTERNAL_STORAGE; valid permission but invites Play Store policy scrutiny and is an anti-pattern. |
| opus-4.8-ultra | ✅ LEGIT | 85 | MANAGE_EXTERNAL_STORAGE Play-policy risk (AndroidManifest.xml:49) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

