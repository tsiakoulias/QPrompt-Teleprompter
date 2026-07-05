# [495-AND-CRIT-01] Missing android.permission.INTERNET — all network silently fails

- **Status:** FIXED  (INTERNET permission added; commit 76c55a9 on fix/android-internet-permission; merged upstream PR #477)
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
| opus-4.8-extra | ✅ LEGIT | 85 | no android.permission.INTERNET in manifest; app uses QtNetwork/WebSocket (AndroidManifest.xml) |
| gpt-5.5-xhigh | ✅ LEGIT | 84 | Missing android.permission.INTERNET - all network silently fails (android/AndroidManifest.xml:47) |
| deepseek-v4-pro-max | ✅ LEGIT | 95 | AndroidManifest.xml:47-53: no INTERNET permission; app uses QNetworkAccessManager+WebSocket — remote files/OBS silently fail on all Android versions |
| glm-5.2-xhigh | ✅ LEGIT | 85 | AndroidManifest.xml:47-53 missing android.permission.INTERNET; all network silently fails |
| kimi-k2.7-code | ✅ LEGIT | 95 | AndroidManifest.xml:48-53 lists storage/wifi permissions but omits android.permission.INTERNET. |
| opus-4.8-ultra | ✅ LEGIT | 85 | no android.permission.INTERNET in manifest; app uses QtNetwork/WebSocket (AndroidManifest.xml) |

## Patch

- **Root cause:** The project ships its own `android/AndroidManifest.xml` (replacing Qt's
  default template, which normally includes `INTERNET`). It declares storage/wifi/mount
  permissions but omits `android.permission.INTERNET`. On Android, all socket/network I/O
  requires this install-time permission, so every network operation failed with no user-visible
  error. Confirmed the app genuinely uses the network: `QNetworkAccessManager` in
  `src/documenthandler.cpp:143` (`loadFromNetwork()` at `:867`, remote image fetch at `:1737`)
  and an OBS WebSocket via `QtWebSockets` in `src/prompter/Prompter.qml:80,353`.
- **Fix:** Added `<uses-permission android:name="android.permission.INTERNET"/>` to the manifest's
  permission block. `INTERNET` is a normal (install-time) permission — declaring it is sufficient;
  no runtime request needed. Scoped strictly to the reported defect (did not add `ACCESS_NETWORK_STATE`
  or others the bug didn't call for).
- **Files changed:** `android/AndroidManifest.xml` (+1 line).
- **Verification:** XML validated well-formed (`xml.dom.minidom`); diff is exactly the single added
  line. No build regression possible from a manifest permission addition. Full Android build not run
  locally (no Android SDK/NDK/Qt-for-Android toolchain on this Windows host) — the change is a
  declarative manifest permission with no code path to compile.
- **Commit / PR:** `76c55a9` on branch `fix/android-internet-permission` (cut from `main`).

