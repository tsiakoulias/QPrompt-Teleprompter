# [R2-ANDMAN-01] Ungrantable system/signature permissions bloating manifest

- **Status:** OPEN
- **Severity:** Medium
- **Category:** Platform/Build
- **Location:** `android/AndroidManifest.xml:51-53`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** android/AndroidManifest.xml:51-53
- **Severity:** Medium
- **Category:** Platform/Build
- **Analysis:** MOUNT_UNMOUNT_FILESYSTEMS, MOUNT_FORMAT_FILESYSTEMS, and ACCESS_CHECKIN_PROPERTIES are signature|privileged permissions a third-party app can never obtain. Google Play may flag as suspicious or reject.
- **Impact:** Potential Play Store rejection or review delay. Zero functional benefit.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 85 | ungrantable signature permissions (AndroidManifest.xml:51) |
| gpt | ✅ LEGIT | 78 | Ungrantable system/signature permissions bloating manifest (android/AndroidManifest.xml:51) |
| deepseek | ✅ LEGIT | 90 | AndroidManifest.xml:51-53: MOUNT_UNMOUNT_FILESYSTEMS/MOUNT_FORMAT_FILESYSTEMS/ACCESS_CHECKIN_PROPERTIES are signature-level permissions ungrantable to third-party apps |
| glm | ✅ LEGIT | 80 | AndroidManifest.xml:51-53 MOUNT_UNMOUNT_FILESYSTEMS and MOUNT_FORMAT_FILESYSTEMS are system/signature permissions not grantable to normal apps |
| kimi | ✅ LEGIT | 85 | AndroidManifest.xml:51-53 declares MOUNT_UNMOUNT_FILESYSTEMS/MOUNT_FORMAT_FILESYSTEMS/ACCESS_CHECKIN_PROPERTIES; these are system/signature-level and ungrantable to third-party apps. |
| opus-ultra | ✅ LEGIT | 85 | ungrantable signature permissions (AndroidManifest.xml:51) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

