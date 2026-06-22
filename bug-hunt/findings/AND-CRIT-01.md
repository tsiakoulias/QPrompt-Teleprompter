# [AND-CRIT-01] Missing android.permission.INTERNET — all network silently fails

- **Status:** OPEN
- **Severity:** Critical
- **Category:** 
- **Location:** `AndroidManifest.xml:47-53`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** AndroidManifest.xml:47-53
- **Severity:** Critical
- **Analysis:** Manifest requests READ_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE, ACCESS_WIFI_STATE, but omits INTERNET. App uses QNetworkAccessManager for loadFromNetwork() and WebSocket for OBS.
- **Impact:** Remote file loading and OBS scene switching silently fail on all Android versions.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 85 | no android.permission.INTERNET in manifest; app uses QtNetwork/WebSocket (AndroidManifest.xml) |
| gpt | ✅ LEGIT | 84 | Missing android.permission.INTERNET - all network silently fails (android/AndroidManifest.xml:47) |
| deepseek | ✅ LEGIT | 95 | AndroidManifest.xml:47-53: no INTERNET permission; app uses QNetworkAccessManager+WebSocket — remote files/OBS silently fail on all Android versions |
| glm | ✅ LEGIT | 85 | AndroidManifest.xml:47-53 missing android.permission.INTERNET; all network silently fails |
| kimi | ✅ LEGIT | 95 | AndroidManifest.xml:48-53 lists storage/wifi permissions but omits android.permission.INTERNET. |
| opus-ultra | ✅ LEGIT | 85 | no android.permission.INTERNET in manifest; app uses QtNetwork/WebSocket (AndroidManifest.xml) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

