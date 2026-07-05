# Multi-Agent Bug Review — QPrompt

_723 findings · agents: opus-4.8-extra, gpt-5.5-xhigh, deepseek-v4-pro-max, glm-5.2-xhigh, kimi-k2.7-code, opus-4.8-ultra, fable-5-ultra_

Bird's-eye matrix + divergences. Per-bug detail (incl. each agent's full rationale, the original claim, and the patch workspace) lives in `findings/<ID>.md`; the work queue is `BACKLOG.md`.

## Summary

| Agent | FALSE | LEGIT | PARTIAL | UNSURE |
|---|---|---|---|---|
| opus-4.8-extra | 49 | 288 | 319 | 67 |
| gpt-5.5-xhigh | 44 | 333 | 299 | 47 |
| deepseek-v4-pro-max | 39 | 597 | 51 | 36 |
| glm-5.2-xhigh | 19 | 559 | 133 | 12 |
| kimi-k2.7-code | 73 | 641 | 7 | 2 |
| opus-4.8-ultra | 70 | 496 | 94 | 63 |
| fable-5-ultra | 0 | 0 | 0 | 0 |

**Consensus** (7 agents): AGREE 192 · split 399 · CONFLICT 132

## Matrix

| ID | Sev | opus-4.8-extra | gpt-5.5-xhigh | deepseek-v4-pro-max | glm-5.2-xhigh | kimi-k2.7-code | opus-4.8-ultra | fable-5-ultra | Consensus | Title |
|---|---|---|---|---|---|---|---|---|---|---|
| 042-MEM-01 | High | ✅100 | ✅88 | ✅90 | ✅90 | ✅95 | ✅100 | · | AGREE | Memory Leak: `_markersModel` allocated without parent, never deleted |
| 043-MEM-02 | High | ✅100 | ✅88 | ✅90 | ✅90 | ✅95 | ✅100 | · | AGREE | Memory Leak: `_fileSystemWatcher` allocated without parent, never deleted |
| 145-MEM-03 | Medium | ✅100 | ✅88 | ✅85 | ✅85 | ✅90 | ✅100 | · | AGREE | Memory Leak: `m_fontDialog` allocated without parent, never deleted |
| 039-LOG-01 | High | ✅100 | ✅92 | ✅95 | ✅90 | ✅95 | ✅100 | · | AGREE | SessionModel::rowCount returns m_data.size() for both valid and invalid parents |
| 040-LOG-02 | High | ✅95 | ✅92 | ✅95 | ✅90 | ✅95 | ✅95 | · | AGREE | Off-by-one: beginRemoveRows uses rowCount() instead of rowCount()-1 |
| 141-LOG-03 | Medium | ✅100 | ✅78 | ✅98 | ✅95 | ✅95 | ✅100 | · | AGREE | MarkersModel::data returns data.position for LengthRole instead of data.length |
| 221-LOG-04 | Medium | ✅100 | ✅78 | ⚠️60 | ✅85 | ✅85 | ✅100 | · | split | MarkersModel::extendLastMarker modifies data without emitting dataChanged |
| 142-LOG-05 | Medium | ✅100 | ✅78 | ✅88 | ✅90 | ✅90 | ✅100 | · | AGREE | DocumentHandler::search ignores `loop` parameter when `regEx` is true |
| 222-LOG-06 | Medium | ✅90 | ✅78 | ⚠️70 | ✅85 | ✅85 | ✅90 | · | split | DocumentHandler::replaceAll has potential infinite loop with regex |
| 690-LOG-07 | Low | ⚠️60 | ⚠️52 | ⚠️50 | ⚠️60 | ✅70 | ⚠️50 | · | split | namedMarker() fetches cursor twice — stale-content risk |
| 404-LOG-08 | Low | ✅100 | ✅88 | ✅85 | ⚠️55 | ✅90 | ✅100 | · | split | DataPoint default constructor leaves three members uninitialized |
| 691-LOG-09 | Low | ❌95 | ❌76 | ❌80 | ❌80 | ✅75 | ❌95 | · | **CONFLICT** | Trailing comma in constructor member initializer list (non-standard C++ before C++20) |
| 506-QML-01 | Critical | ❌90 | ❌90 | ❔30 | ❌85 | ✅90 | ❌90 | · | **CONFLICT** | 26 references to undefined `pointerSettings` ID in ReadRegionOverlay |
| 507-QML-02 | Critical | ❌90 | ❌90 | ❔30 | ❌85 | ✅90 | ❌90 | · | **CONFLICT** | Undefined `pointerConfiguration` ID reference in ReadRegionOverlay |
| 014-QML-03 | Critical | ✅95 | ✅92 | ✅75 | ❌80 | ✅90 | ✅95 | · | **CONFLICT** | Undefined `root` ID in WindowDragger.qml |
| 046-QML-04 | High | ✅100 | ✅92 | ✅90 | ✅95 | ✅95 | ✅100 | · | AGREE | Typo: `verticalCentertop` instead of `verticalCenter` |
| 047-QML-05 | High | ✅100 | ✅84 | ✅95 | ✅90 | ✅95 | ✅100 | · | AGREE | `&&` should be `\|\|` in clear button enabled condition |
| 048-QML-06 | High | ✅100 | ✅84 | ✅90 | ✅85 | ✅95 | ✅100 | · | AGREE | Bitwise OR (`\|`) instead of AND (`&`) in modifier key check |
| 543-QML-07 | High | ❌95 | ❌90 | ❌85 | ⚠️60 | ❌85 | ❌95 | · | split | `Text.CurveRendering` enum requires Qt >= 6.7 |
| 613-QML-08 | Medium | ❌80 | ❌76 | ❔40 | ❌80 | ✅90 | ❌80 | · | **CONFLICT** | Invalid anchor target `undefined` |
| 618-QML-09 | Medium | ❌95 | ❌90 | ❌85 | ⚠️55 | ❌85 | ❌95 | · | split | `QtQuick.Shapes 6.6` version mismatch with `QtCore 6.5` |
| 590-QML-10 | Medium | ❌85 | ❌76 | ❔45 | ✅80 | ✅90 | ❌85 | · | **CONFLICT** | `+android/main.qml` missing `QmlUtil` for RecentDocuments |
| 311-QML-11 | Medium | ✅90 | ⚠️58 | ✅85 | ⚠️70 | ✅75 | ✅90 | · | split | Dead code: `window` property declared but never used in WindowDragger |
| 010-SEC-01 | Critical | ✅95 | ✅84 | ✅75 | ✅85 | ✅95 | ✅95 | · | AGREE | Arbitrary Command Execution via `sys://` Marker URIs |
| 184-SEC-02 | Medium | ✅85 | ✅78 | ✅90 | ✅85 | ✅85 | ✅85 | · | AGREE | OBS WebSocket Password Stored in Plaintext |
| 185-SEC-03 | Medium | ✅95 | ✅78 | ✅80 | ✅90 | ✅90 | ✅95 | · | AGREE | Information Disclosure: Full HTML Document Content Logged via qDebug |
| 529-SEC-04 | High | ⚠️55 | ⚠️58 | ✅85 | ✅85 | ✅90 | ⚠️50 | · | split | SSRF / URL Injection — User-Controlled URL Passed to Network Loader |
| 600-SEC-05 | Medium | ⚠️55 | ⚠️58 | ✅70 | ⚠️70 | ✅85 | ⚠️50 | · | split | User-Controlled Filename Passed to QProcess (LibreOffice import) |
| 061-RES-01 | High | ✅95 | ✅84 | ✅90 | ✅85 | ✅90 | ✅95 | · | AGREE | Network reply overwritten without aborting previous download |
| 062-RES-02 | High | ✅95 | ✅84 | ✅92 | ✅90 | ✅90 | ✅95 | · | AGREE | loadFromNetworkFinihed ignores the QNetworkReply* signal parameter |
| 672-RES-03 | Low | ⚠️65 | ⚠️58 | ✅85 | ⚠️60 | ✅80 | ⚠️50 | · | split | ShakeDetector::s_instance never set to nullptr on destruction (dangling pointer) |
| 673-RES-04 | Low | ⚠️65 | ⚠️58 | ✅85 | ⚠️60 | ✅80 | ⚠️50 | · | split | IosSaveDialog::s_instance same singleton dangling pattern |
| 700-RES-05 | Low | ❌80 | ❌76 | ❌75 | ❌80 | ❌70 | ❌80 | · | AGREE | QTextStream left unflushed before QFile destruction |
| 532-TYP-01 | High | ❌80 | ❔39 | ✅95 | ✅85 | ✅95 | ❌80 | · | **CONFLICT** | Dangling pointer from temporary std::string in SpellChecker::loadOne |
| 605-TYP-02 | Medium | ❌90 | ❌76 | ✅90 | ⚠️55 | ✅90 | ❌90 | · | **CONFLICT** | Invalid Qt::LayoutDirection enum value cast |
| 580-TYP-03 | Medium | ⚠️60 | ⚠️58 | ✅85 | ✅85 | ✅85 | ⚠️50 | · | split | Floating-point equality comparison of window opacity |
| 267-TYP-04 | Medium | ✅95 | ⚠️58 | ✅90 | ✅85 | ✅90 | ✅95 | · | split | Bitwise AND on bools hides dead code in preventSleep |
| 268-TYP-05 | Medium | ✅95 | ✅88 | ⚠️60 | ✅90 | ✅90 | ✅95 | · | split | Uninitialized pointer member m_reply in DocumentHandler |
| 447-TYP-06 | Low | ✅95 | ⚠️58 | ✅85 | ❌75 | ✅90 | ✅95 | · | **CONFLICT** | Malformed preprocessor macro: `#define Use_GlobalAccel = 1` |
| 448-TYP-07 | Low | ✅90 | ⚠️58 | ⚠️30 | ✅75 | ✅70 | ✅90 | · | split | Narrowing conversion: `size_t` → `int` in SpellChecker::decode |
| 695-TYP-08 | Low | ❌95 | ❌76 | ❌80 | ❌85 | ✅75 | ❌95 | · | **CONFLICT** | DocumentHandler constructor trailing comma in initializer list |
| 701-TYP-09 | Low | ❌90 | ❌76 | ⚠️40 | ⚠️55 | ❌80 | ❌90 | · | split | Null pointer dereferences in emit textChanged related to uninitialized m_document |
| 696-TYP-10 | Low | ❌55 | ❌76 | ❌60 | ✅80 | ❌85 | ❌55 | · | **CONFLICT** | Uninitialized marker struct fields: length defaults to 1 |
| 027-EDGE-01 | High | ✅95 | ✅84 | ✅95 | ✅85 | ✅90 | ✅95 | · | AGREE | QString::arg() called on string with no placeholder — program name silently dropped |
| 028-EDGE-02 | High | ✅95 | ✅84 | ✅90 | ✅85 | ✅90 | ✅95 | · | AGREE | Empty container `first()` dereference — crash on hotkey with no windows |
| 029-EDGE-03 | High | ✅90 | ✅84 | ✅85 | ✅90 | ✅90 | ✅90 | · | AGREE | Empty container `last()` dereference in `extendLastMarker` |
| 002-EDGE-04 | Critical | ✅90 | ✅88 | ✅92 | ✅90 | ✅95 | ✅90 | · | AGREE | Null pointer dereference: `document()->textDocument()` not checked before `load()` |
| 003-EDGE-05 | Critical | ✅90 | ✅88 | ✅92 | ✅90 | ✅95 | ✅90 | · | AGREE | Null pointer dereference: `textDocument()` unchecked in `search()` |
| 004-EDGE-06 | Critical | ✅90 | ✅88 | ✅92 | ✅90 | ✅95 | ✅90 | · | AGREE | Null pointer dereference: `textDocument()` unchecked in `parse()` |
| 533-EDGE-07 | High | ⚠️60 | ⚠️58 | ✅85 | ⚠️60 | ✅90 | ⚠️50 | · | split | Q_UNREACHABLE in Q_INVOKABLE method — UB if called from QML |
| 553-EDGE-08 | Medium | ❌80 | ❌76 | ✅75 | ✅85 | ✅80 | ❌80 | · | **CONFLICT** | Q_ASSERT as thread-safety guard — removed in release builds |
| 123-EDGE-09 | Medium | ✅90 | ✅88 | ✅85 | ✅75 | ✅85 | ✅90 | · | AGREE | QFile::copy() return value silently ignored |
| 660-EDGE-10 | Low | ❌85 | ⚠️58 | ⚠️50 | ✅80 | ✅70 | ❌85 | · | **CONFLICT** | globalShortcutKey() switch without default — fallthrough to Q_UNREACHABLE |
| 554-EDGE-11 | Medium | ⚠️60 | ⚠️58 | ✅85 | ✅85 | ✅80 | ⚠️50 | · | split | m_reply dereference without null check in loadFromNetworkFinihed() |
| 685-EDGE-12 | Low | ⚠️40 | ⚠️58 | ❌40 | ⚠️60 | ✅60 | ❌72 | · | **CONFLICT** | QTextBlock::iterator scope fragility in parse() |
| 087-PLAT-01 | High | ✅90 | ⚠️58 | ✅90 | ⚠️65 | ✅90 | ✅90 | · | split | KF6Crash_FOUND never defined as C preprocessor macro — KCrash support dead code |
| 155-PLAT-02 | Medium | ✅90 | ✅78 | ✅85 | ✅85 | ✅85 | ✅90 | · | AGREE | REQUIRED_KF6_VERSION variable referenced but never defined |
| 069-PLAT-03 | High | ✅85 | ✅84 | ❔50 | ✅85 | ✅90 | ✅85 | · | split | Wrong target name and wrong include path for KDMacTouchBar |
| 612-PLAT-04 | Medium | ❌95 | ❌90 | ❔40 | ✅80 | ❌90 | ❌95 | · | **CONFLICT** | DS_Store.scpt referenced but file does not exist |
| 234-PLAT-05 | Medium | ✅85 | ✅92 | ✅85 | ❌85 | ✅85 | ✅85 | · | **CONFLICT** | DBINARY_ICONS_RESOURCE is a typo — should be BINARY_ICONS_RESOURCE |
| 367-PLAT-06 | Low | ✅90 | ✅78 | ✅80 | ✅80 | ✅80 | ✅90 | · | AGREE | qprompt_QM_LOADER variable never defined |
| 431-PLAT-07 | Low | ✅95 | ⚠️58 | ✅85 | ❌75 | ✅90 | ✅95 | · | **CONFLICT** | Incorrect macro syntax: `#define Use_GlobalAccel = 1` |
| 589-PLAT-08 | Medium | ⚠️50 | ⚠️58 | ✅85 | ⚠️55 | ✅85 | ⚠️50 | · | split | QNX platform guard inconsistency: main.cpp vs documenthandler.h |
| 670-PLAT-09 | Low | ❔45 | ❔39 | ❔30 | ✅80 | ✅75 | ❔45 | · | split | Pre-build manifest references invalid Android SDK paths |
| 525-R2-GH-01 | High | ❌80 | ❌76 | ✅80 | ✅80 | ✅85 | ❌80 | · | **CONFLICT** | Q_UNREACHABLE reachable when only QHotkey available on Wayland |
| 498-R2-CMAKE-01 | Critical | ❌80 | ❌76 | ✅90 | ✅85 | ✅95 | ❌80 | · | **CONFLICT** | sphinx_add_docs silently ignores all keyword arguments due to empty cmake_parse_arguments prefix |
| 071-R2-CMAKE-02 | High | ✅80 | ✅84 | ✅90 | ⚠️60 | ✅90 | ✅80 | · | split | cmake_minimum_required inside find module pollutes parent project policy settings |
| 240-R2-CMAKE-03 | Medium | ✅80 | ✅78 | ✅85 | ❌80 | ✅85 | ✅80 | · | **CONFLICT** | WORKING_DIRECTORY and COMMENT not parseable by callers of sphinx_add_docs |
| 162-R2-CMAKE-04 | Medium | ✅80 | ✅78 | ✅80 | ✅80 | ✅80 | ✅80 | · | AGREE | QML icon file(GLOB_RECURSE) missing CONFIGURE_DEPENDS causes stale icon sets |
| 242-R2-PRP-01 | Medium | ✅80 | ✅78 | ❔45 | ✅90 | ✅90 | ✅80 | · | split | Qt.LeftToRight used as bare boolean — RTL branch always dead |
| 243-R2-PRP-02 | Medium | ✅85 | ✅92 | ❔40 | ✅85 | ✅90 | ✅85 | · | split | Kirigami.Units.SmallSpacing — uppercase S yields undefined |
| 592-R2-PRP-03 | Medium | ❌75 | ⚠️58 | ❔40 | ✅85 | ✅90 | ❌75 | · | **CONFLICT** | Units.LongDuration / Units.HumanMoment missing Kirigami. prefix |
| 485-R2-PRP-04 | Low | ⚠️50 | ⚠️58 | ❔35 | ⚠️55 | ✅75 | ✅68 | · | split | Inconsistent focus restoration in decreaseVelocityButton |
| 465-R2-PRP-05 | Low | ⚠️45 | ⚠️52 | ❔30 | ✅80 | ✅80 | ✅68 | · | split | Potential null-item access on async Loader in namedMarkerConfiguration.onOpened |
| 593-R2-PTR-01 | Medium | ❌75 | ❌76 | ✅80 | ⚠️60 | ✅90 | ❌75 | · | **CONFLICT** | Type mismatch: textVerticalOffset declared int but fed a real |
| 594-R2-PTR-02 | Medium | ❌75 | ❌76 | ✅80 | ⚠️60 | ✅90 | ❌75 | · | **CONFLICT** | Type mismatch: imageVerticalOffset declared int but fed a real |
| 244-R2-PTR-03 | Medium | ✅80 | ✅78 | ❔40 | ✅85 | ✅85 | ✅80 | · | split | Casing error: Units.longDuration should be Units.LongDuration |
| 245-R2-PTR-04 | Medium | ✅85 | ✅78 | ❔35 | ✅85 | ✅90 | ✅85 | · | split | Inverted indexOf truthiness in platform check for ColorDialog |
| 017-R2-AND-01 | Critical | ✅90 | ⚠️58 | ❔35 | ✅85 | ✅95 | ✅90 | · | split | Android missing QmlUtil causes crash on factory reset and RecentDocuments |
| 015-R2-AND-02 | Critical | ✅90 | ✅84 | ❔35 | ✅80 | ✅95 | ✅90 | · | split | Android missing restartDialog crashes LanguageSettingsOverlay and LayoutDirectionSettingsOverlay |
| 238-R2-AND-03 | Medium | ✅80 | ✅78 | ❔35 | ✅80 | ✅80 | ✅80 | · | split | Android Settings missing fakeFullScreen persistence |
| 463-R2-AND-04 | Low | ⚠️45 | ⚠️58 | ❔30 | ✅75 | ✅70 | ✅68 | · | split | Android Settings for "background" missing transparency persistence |
| 464-R2-AND-05 | Low | ⚠️45 | ⚠️58 | ❔25 | ✅80 | ✅60 | ✅68 | · | split | Android loadTelemetryPage passes no properties object to pageStack push |
| 349-R2-OVL-01 | Medium | ⚠️65 | ⚠️58 | ❔35 | ✅85 | ✅85 | ✅68 | · | split | InputsOverlay onOpened calls cursorAutoHide.restart() instead of reset() |
| 410-R2-OVL-02 | Low | ✅85 | ✅78 | ❔35 | ✅80 | ✅80 | ✅85 | · | split | LanguageSettingsOverlay popup ListView currentIndex always resolves to -1 |
| 165-R2-PTH-01 | Medium | ✅85 | ✅78 | ✅80 | ✅80 | ✅85 | ✅85 | · | AGREE | FileDialog filter matches all files on Linux due to stray glob |
| 166-R2-PTH-02 | Medium | ✅85 | ✅78 | ✅80 | ✅85 | ✅85 | ✅85 | · | AGREE | File path from file:// URL preserves percent-encoding |
| 050-R2-WHE-01 | High | ✅90 | ✅84 | ✅85 | ✅85 | ✅90 | ✅90 | · | AGREE | `focus: true` is JavaScript label, not assignment |
| 241-R2-EDT-01 | Medium | ✅90 | ✅92 | ❔40 | ✅95 | ✅90 | ✅90 | · | split | Qt.AlignHustify typo — nonexistent enum value |
| 072-R2-EDT-02 | High | ✅85 | ✅84 | ❔35 | ✅90 | ✅90 | ✅85 | · | split | wheelThrottleSettingsButton checked bound to completely unrelated document property |
| 073-R2-EDT-03 | High | ✅80 | ✅84 | ⚠️55 | ✅85 | ✅90 | ✅80 | · | split | Checkable ToolButtons break checked property bindings on first click — systematic |
| 246-R2-TEL-01 | Medium | ✅80 | ✅78 | ❔35 | ✅85 | ✅85 | ✅80 | · | split | Telemetry sub-toggles permanently disconnect from master toggle on click |
| 436-R2-REC-01 | Low | ✅85 | ✅92 | ⚠️60 | ⚠️60 | ✅80 | ✅85 | · | split | File URI prefix strip off-by-one on Windows |
| 350-R2-REC-02 | Medium | ⚠️50 | ⚠️58 | ❔30 | ✅80 | ✅75 | ✅68 | · | split | refreshExistence skips UI updates when dynamic children out of sync |
| 088-R2-IOS-01 | High | ✅80 | ✅84 | ❔40 | ⚠️65 | ✅85 | ✅80 | · | split | Method swizzling re-entry causes infinite recursion on second invocation |
| 591-R2-IOS-02 | Medium | ⚠️50 | ❔39 | ❔40 | ✅80 | ✅80 | ⚠️50 | · | split | Delegate block captures raw assign pointer — use-after-free risk |
| 164-R2-IOS-03 | Medium | ✅85 | ✅78 | ✅75 | ✅80 | ✅80 | ✅85 | · | AGREE | UIApplication.keyWindow deprecated since iOS 13; breaks multi-window iPadOS |
| 314-R2-WASM-01 | Medium | ✅85 | ✅78 | ❔35 | ⚠️65 | ✅85 | ✅85 | · | split | File input element never removed from DOM on user cancel |
| 247-R2-WASM-02 | Medium | ✅85 | ✅78 | ❔35 | ✅85 | ✅85 | ✅85 | · | split | Insecure hostname validation via endsWith allows subdomain spoofing |
| 163-R2-FONT-01 | Medium | ✅85 | ✅78 | ✅75 | ✅80 | ✅75 | ✅85 | · | AGREE | RichText label renders unescaped plain text — HTML metacharacters break display |
| 369-R2-FONT-02 | Low | ✅85 | ✅92 | ✅95 | ✅90 | ✅90 | ✅85 | · | AGREE | Duplicate setText call on preview label |
| 161-R2-ANDMAN-01 | Medium | ✅85 | ✅78 | ✅90 | ✅80 | ✅85 | ✅85 | · | AGREE | Ungrantable system/signature permissions bloating manifest |
| 239-R2-ANDMAN-02 | Medium | ✅85 | ✅78 | ✅90 | ✅80 | ⚠️55 | ✅85 | · | split | MANAGE_EXTERNAL_STORAGE likely triggers Play Store scrutiny |
| 007-R3-CTX-01 | Critical | ✅90 | ✅92 | ✅95 | ✅90 | ✅85 | ✅90 | · | AGREE | AbstractUnits missing QML_ELEMENT — all duration constants resolve to undefined |
| 051-R3-CTX-02 | High | ✅90 | ✅84 | ✅98 | ✅85 | ✅90 | ✅90 | · | AGREE | GlobalHotkeys.SkipForward enum value mismatch — trailing 's' missing |
| 008-R3-DOC-01 | Critical | ✅90 | ✅92 | ✅85 | ✅90 | ✅90 | ✅90 | · | AGREE | m_reloading uninitialized — undefined behavior on first load |
| 504-R3-DOC-02 | Critical | ❌85 | ❌76 | ✅90 | ✅85 | ❌60 | ❌85 | · | **CONFLICT** | Unbalanced edit block in setLineHeight/setParagraphHeight |
| 052-R3-DOC-03 | High | ✅85 | ✅84 | ✅90 | ✅85 | ✅85 | ✅85 | · | AGREE | load() sets m_fileUrl and emits fileUrlChanged even on failed load |
| 053-R3-DOC-04 | High | ✅90 | ✅84 | ✅95 | ✅85 | ✅85 | ✅90 | · | AGREE | saveAs() silently ignores write/flush failures |
| 054-R3-DOC-05 | High | ✅85 | ✅84 | ✅90 | ✅80 | ✅80 | ✅85 | · | AGREE | updateContents() produces two separate undo entries — undo destroys document |
| 167-R3-DOC-06 | Medium | ✅90 | ✅78 | ✅85 | ✅80 | ✅90 | ✅90 | · | AGREE | reload() leaks m_reloading=true on URL mismatch |
| 055-R3-DOC-07 | High | ✅85 | ✅84 | ✅90 | ✅85 | ✅85 | ✅85 | · | AGREE | Inverted selection state after failed search() |
| 250-R3-SPL-01 | Medium | ✅70 | ✅78 | ✅80 | ⚠️65 | ✅75 | ✅70 | · | split | encode() uses toLocal8Bit() instead of dictionary-encoding-aware conversion |
| 251-R3-SPL-02 | Medium | ✅70 | ✅78 | ✅80 | ⚠️65 | ✅75 | ✅70 | · | split | decode() uses fromLocal8Bit() — suggestions show as mojibake |
| 572-R3-SPL-03 | Medium | ❌80 | ❌76 | ✅90 | ✅80 | ✅80 | ❌80 | · | **CONFLICT** | removeCustomWord() silently discards all addWord() additions |
| 171-R3-SPL-04 | Medium | ✅75 | ✅78 | ✅90 | ✅80 | ✅70 | ✅75 | · | AGREE | Corrupt cached dictionary file persists permanently after failed copy |
| 596-R3-SPL-05 | Medium | ⚠️45 | ⚠️58 | ✅85 | ✅85 | ⚠️55 | ⚠️50 | · | split | SpellChecker has zero thread safety — all methods unprotected |
| 546-R3-MAIN-01 | Medium | ❌75 | ✅78 | ✅85 | ✅80 | ✅85 | ❌75 | · | **CONFLICT** | Command-line positional argument description/syntax swapped |
| 089-R3-MAIN-02 | High | ⚠️55 | ⚠️58 | ✅90 | ✅85 | ✅75 | ✅68 | · | split | Invalid locale string constructed for short language codes |
| 168-R3-MAIN-03 | Medium | ✅85 | ✅78 | ✅95 | ✅85 | ✅80 | ✅85 | · | AGREE | System locale changed even when translation file fails to load |
| 699-R3-MAIN-04 | Low | ❌85 | ❌76 | ⚠️60 | ⚠️60 | ❌65 | ❌85 | · | split | Stack-allocated QTranslator outlives QApplication on shutdown |
| 248-R3-MAIN-05 | Medium | ✅80 | ⚠️58 | ✅98 | ✅80 | ✅85 | ✅80 | · | split | Hardcoded Homebrew version-specific Kirigami import path |
| 074-R3-MAIN-06 | High | ✅90 | ✅84 | ✅90 | ⚠️55 | ✅75 | ✅90 | · | split | Inconsistent Kirigami platform guards — missing WATCHOS and QNX |
| 169-R3-MAIN-07 | Medium | ✅90 | ✅78 | ✅98 | ✅85 | ✅80 | ✅90 | · | AGREE | XDG_CURRENT_DESKTOP unconditionally forced to "KDE" on all Linux |
| 411-R3-MAIN-08 | Low | ✅55 | ✅78 | ✅80 | ⚠️60 | ✅65 | ✅55 | · | split | QFontDatabase::addApplicationFont return value discarded |
| 692-R3-APP-01 | Low | ❌75 | ❌76 | ❌85 | ⚠️60 | ✅80 | ❌75 | · | **CONFLICT** | AppController singleton and children never deallocated |
| 249-R3-PROP-01 | Medium | ✅80 | ✅78 | ✅80 | ⚠️65 | ✅85 | ✅80 | · | split | selectionIsLowerCase bound to wrong NOTIFY signal |
| 370-R3-SIG-01 | Low | ✅85 | ✅78 | ✅90 | ✅80 | ✅95 | ✅85 | · | AGREE | textChanged() signal declared but never emitted |
| 614-R3-SIG-02 | Medium | ❌85 | ❌90 | ⚠️85 | ✅85 | ❌85 | ❌85 | · | **CONFLICT** | ShakeDetector signals declared but never emitted — dead feature |
| 595-R3-SIG-03 | Medium | ❌90 | ❌90 | ✅75 | ✅85 | ❌85 | ❌90 | · | **CONFLICT** | IosSaveDialog accepted/rejected signals declared but never emitted |
| 090-R3-PMT-01 | High | ⚠️60 | ⚠️58 | ✅95 | ✅85 | ✅95 | ✅68 | · | split | OBS WebSocket JSON.parse without try/catch — crash on malformed input |
| 170-R3-PMT-02 | Medium | ✅60 | ✅78 | ✅90 | ✅80 | ✅90 | ✅60 | · | AGREE | OBS WebSocket no onError handler, no reconnection logic |
| 571-R3-PMT-03 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅75 | ✅90 | ⚠️50 | · | split | goToNextMarker fallback desynchronizes cursor from viewport |
| 573-R3-TMR-01 | Medium | ❔45 | ❔39 | ✅80 | ✅85 | ✅95 | ❔45 | · | split | TimerClock ETA uses __iDefault instead of actual __i during reverse scroll |
| 505-R4-QTV-01 | Critical | ❌90 | ❌76 | ✅95 | ❌80 | ✅80 | ❌90 | · | **CONFLICT** | QtQuick 2.13 import does not exist in Qt 6.5 |
| 509-R4-QTV-02 | Critical | ❌90 | ❌76 | ❔60 | ❌80 | ✅80 | ❌90 | · | **CONFLICT** | QtQuick.Window 2.0 import does not exist in Qt 6.5 |
| 545-R4-QTV-03 | High | ❌90 | ❌76 | ❌98 | ❌75 | ❌90 | ❌90 | · | AGREE | QtQuick.Dialogs 6.6 imported in 9 files on Qt 6.5 target |
| 018-R4-EXP-01 | Critical | ⚠️55 | ⚠️58 | ✅95 | ✅85 | ✅85 | ✅68 | · | split | No XSS sanitization — script tags, event handlers, javascript: URLs unfiltered |
| 056-R4-EXP-02 | High | ✅90 | ✅84 | ✅95 | ✅85 | ✅95 | ✅90 | · | AGREE | insertHtmlAt() bypasses filterHtml() — unsanitized HTML from QML |
| 057-R4-EXP-03 | High | ✅85 | ✅84 | ✅90 | ✅85 | ✅95 | ✅85 | · | AGREE | loadFromNetwork() destroys URL for relative URLs — host/path swapped |
| 058-R4-EXP-04 | High | ✅80 | ✅84 | ✅90 | ✅80 | ✅90 | ✅80 | · | AGREE | AutoText inserts plain text as HTML — content corruption |
| 172-R4-EXP-05 | Medium | ✅70 | ✅78 | ✅90 | ✅85 | ✅80 | ✅70 | · | AGREE | No encoding/charset detection — all imports assumed UTF-8 |
| 173-R4-EXP-06 | Medium | ✅70 | ✅78 | ✅95 | ✅80 | ✅80 | ✅70 | · | AGREE | UTF-8 BOM not stripped — becomes phantom character at position 0 |
| 174-R4-EXP-07 | Medium | ✅60 | ✅78 | ✅90 | ✅80 | ✅90 | ✅60 | · | AGREE | data: URI assumes base64 encoding without checking ;base64 token |
| 175-R4-EXP-08 | Medium | ✅85 | ✅78 | ✅90 | ✅85 | ✅90 | ✅85 | · | AGREE | EPUB/MOBI/AZW import replaces document with error string |
| 466-R4-EXP-09 | Low | ⚠️55 | ⚠️58 | ✅85 | ⚠️65 | ✅85 | ✅68 | · | split | LibreOffice import --cat and --convert-to flags are contradictory |
| 059-R4-ROOT-01 | High | ✅90 | ✅84 | ✅95 | ✅85 | ✅95 | ✅90 | · | AGREE | Qt.openUrlExternally called with translation context string instead of URL |
| 178-R4-ROOT-02 | Medium | ✅85 | ✅92 | ✅95 | ✅85 | ✅90 | ✅85 | · | AGREE | Invalid QML color value "initial" |
| 597-R4-ROOT-03 | Medium | ❌80 | ❌76 | ✅90 | ⚠️65 | ✅90 | ❌80 | · | **CONFLICT** | ESC global shortcut skips single-layer pages — can't dismiss with keyboard |
| 179-R4-ROOT-04 | Medium | ✅90 | ✅92 | ✅98 | ✅85 | ✅95 | ✅90 | · | AGREE | Duplicate "&Open" menu item in native File menu |
| 637-R4-ROOT-05 | Low | ⚠️50 | ✅92 | ✅95 | ⚠️60 | ✅90 | ⚠️50 | · | split | loadRemoteControlPage/loadTelemetryPage reference undefined component IDs |
| 508-R4-EVT-01 | Critical | ❌85 | ❌76 | ✅95 | ❌80 | ❌90 | ❌85 | · | **CONFLICT** | Missing braces on if/else — syntax error in alignRightButton |
| 253-R4-EVT-02 | Medium | ✅90 | ⚠️58 | ✅95 | ✅80 | ✅95 | ✅90 | · | split | Velocity modifier ComboBox lists 2 options but switch handles 4 — dead code |
| 075-R4-EVT-03 | High | ⚠️60 | ✅84 | ✅85 | ✅80 | ✅85 | ✅68 | · | split | CursorAutoHide null access on root.pageStack.currentItem during page transitions |
| 009-R4-CMT-01 | Critical | ✅90 | ✅84 | ✅98 | ✅85 | ✅90 | ✅90 | · | AGREE | PDF import completely broken — converter invocation commented out |
| 544-R4-PRJ-01 | High | ❌80 | ❌76 | ❌85 | ⚠️60 | ❌90 | ❌80 | · | split | flip variable spuriously reset in project() inner loop else-branch |
| 526-R4-PRJ-02 | High | ❔45 | ❔39 | ✅95 | ✅80 | ✅95 | ❔45 | · | split | displayModel.get().flipSetting writes to snapshot copy — never mutates model |
| 176-R4-PRJ-03 | Medium | ✅55 | ✅92 | ✅90 | ✅80 | ✅95 | ✅55 | · | AGREE | setScreensModel() duplicates display entries on each toggle cycle |
| 177-R4-PRJ-04 | Medium | ✅55 | ✅78 | ✅85 | ✅80 | ✅90 | ✅55 | · | AGREE | Division by zero in projection image height |
| 091-R4-ROV-01 | High | ⚠️60 | ⚠️58 | ✅90 | ✅80 | ✅95 | ✅68 | · | split | Division by zero in __customPlacement when overlay full |
| 092-R4-ROV-02 | High | ⚠️65 | ⚠️58 | ✅90 | ✅80 | ✅90 | ✅68 | · | split | Drag permanently breaks y property binding on readRegion |
| 254-R4-ROV-03 | Medium | ✅90 | ✅78 | ✅95 | ⚠️65 | ✅95 | ✅90 | · | split | Bitwise OR \| used for width fallback instead of logical OR |
| 252-R4-BKG-01 | Medium | ✅85 | ✅78 | ✅85 | ⚠️60 | ✅90 | ✅85 | · | split | Flip transform origin stays at (0,0) when Flip stored as property |
| 598-R4-SHD-01 | Medium | ❌80 | ❌76 | ✅90 | ⚠️65 | ✅80 | ❌80 | · | **CONFLICT** | Duplicate class implementation between .cpp and .mm — ODR risk |
| 467-R4-IOSCPP-01 | Low | ⚠️50 | ⚠️58 | ✅90 | ⚠️60 | ✅85 | ✅68 | · | split | QTemporaryDir created on all platforms including non-iOS where unused |
| 468-R4-SIG-ADD-01 | Low | ⚠️45 | ⚠️58 | ⚠️60 | ✅75 | ✅70 | ✅68 | · | split | SessionModel::appendDataPoint declared public slot but never connected |
| 005-FINAL-01 | Critical | ✅90 | ✅92 | ✅98 | ✅85 | ✅95 | ✅90 | · | AGREE | TimerClock references undefined `timer` id — ETA and stopwatch completely broken |
| 501-FINAL-02 | Critical | ❌85 | ❌90 | ❌90 | ✅85 | ✅95 | ❌85 | · | **CONFLICT** | Missing `QtQuick.Controls.Material` import — 3 Material references unresolved |
| 006-FINAL-03 | Critical | ✅95 | ✅84 | ✅98 | ✅80 | ✅90 | ✅95 | · | AGREE | Missing breeze-icons submodule — fresh clone cannot build |
| 099-FINAL-04 | High | ⚠️50 | ⚠️58 | ⚠️60 | ✅80 | ✅95 | ✅68 | · | split | NSIS start-menu shortcut icon name mismatches actual binary name |
| 030-FINAL-05 | High | ✅90 | ✅84 | ✅95 | ✅85 | ✅85 | ✅90 | · | AGREE | WindowDragger mouse delta accumulation error — window moves farther than cursor |
| 084-FINAL-06 | High | ✅90 | ⚠️58 | ❌95 | ✅85 | ✅95 | ✅90 | · | **CONFLICT** | CMAKE_OSX_ARCHITECTURES contains literal quotes — universal binary broken |
| 540-FINAL-07 | High | ❌80 | ❌76 | ❌98 | ⚠️60 | ✅95 | ❌80 | · | **CONFLICT** | CMake wrong variable name: InstallRequiredSystemLibraries instead of CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS |
| 031-FINAL-08 | High | ✅85 | ✅84 | ✅95 | ✅80 | ✅90 | ✅85 | · | AGREE | setup.sh vcvarsall.bat executed from bash — MSVC env not propagated |
| 212-FINAL-09 | Medium | ✅85 | ✅92 | ✅90 | ❌80 | ✅95 | ✅85 | · | **CONFLICT** | `on__IChanged` handler typo — never fires |
| 519-FINAL-10 | High | ⚠️55 | ⚠️58 | ✅90 | ✅80 | ✅90 | ⚠️50 | · | split | Two animations target same `position` property — conflict |
| 032-FINAL-11 | High | ✅85 | ✅84 | ✅95 | ✅85 | ✅95 | ✅85 | · | AGREE | onFrameSwapped calls grabToImage every frame — severe performance hit |
| 128-FINAL-12 | Medium | ✅80 | ✅78 | ✅95 | ✅80 | ✅90 | ✅80 | · | AGREE | SystemFontChooserDialog setWindowFlags strips all decorations |
| 129-FINAL-13 | Medium | ✅90 | ✅92 | ✅95 | ✅90 | ✅95 | ✅90 | · | AGREE | Invalid Korean locale code "ko_KO" — should be "ko_KR" |
| 555-FINAL-14 | Medium | ⚠️55 | ⚠️58 | ✅98 | ✅85 | ✅95 | ⚠️50 | · | split | Wrong placeholder `%0` instead of `%1` — font name never displayed |
| 520-FINAL-15 | High | ⚠️55 | ⚠️58 | ✅90 | ✅85 | ✅85 | ⚠️50 | · | split | Missing edit block wrapping in setLineHeight/setParagraphHeight |
| 497-FINAL-16 | Critical | ❔50 | ⚠️58 | ✅80 | ✅85 | ✅95 | ❔50 | · | split | Countdown completion uses state++ bypassing toggle() entry actions |
| 130-FINAL-17 | Medium | ✅85 | ✅78 | ✅90 | ✅85 | ✅90 | ✅85 | · | AGREE | ScriptAction references non-existent function `paintReady` |
| 131-FINAL-18 | Medium | ✅100 | ✅78 | ✅95 | ✅85 | ✅95 | ✅100 | · | AGREE | MarkersModel extendLastMarker modifies data without emitting dataChanged |
| 213-FINAL-19 | Medium | ✅70 | ✅78 | ✅85 | ⚠️65 | ✅85 | ✅70 | · | split | Encoding fallback uses toLocal8Bit() instead of dictionary's actual encoding |
| 534-FINAL-20 | High | ❌80 | ❌76 | ❌90 | ✅85 | ✅90 | ❌80 | · | **CONFLICT** | Dangling pointer from temporary QByteArray in marker anchor parsing |
| 132-FINAL-21 | Medium | ✅75 | ✅78 | ✅70 | ✅80 | ✅85 | ✅75 | · | AGREE | clearProperty(AnchorHref/AnchorName) ineffective through mergeCharFormat |
| 521-FINAL-22 | High | ⚠️50 | ⚠️58 | ✅85 | ✅80 | ✅85 | ⚠️50 | · | split | Behavior.onRunningChanged calls toggle() from within animation handler — re-entrant state change |
| 001-CUR-N01 | Critical | ✅90 | ✅84 | ✅95 | ✅85 | ✅95 | ✅90 | · | AGREE | replaceAll() infinite loop when replacement contains search pattern |
| 022-CUR-N02 | High | ✅95 | ✅84 | ✅98 | ✅85 | ✅95 | ✅95 | · | AGREE | search() regex path ignores loop parameter — unconditional wrap |
| 117-CUR-N03 | Medium | ✅70 | ✅78 | ✅80 | ✅80 | ✅75 | ✅70 | · | AGREE | alignment() reads blockFormat on multi-block selection — returns wrong alignment |
| 118-DCL-N01 | Medium | ✅55 | ✅78 | ✅95 | ✅80 | ✅95 | ✅55 | · | AGREE | filterHtml default parameter in .cpp but not in header — QML can't call with 1 arg |
| 119-DCL-N02 | Medium | ✅55 | ✅78 | ✅95 | ✅80 | ✅95 | ✅55 | · | AGREE | setKeyMarker default parameter mismatch — same pattern |
| 510-IMP-N01 | Critical | ❌60 | ❌76 | ⚠️75 | ⚠️65 | ❌80 | ❌60 | · | split | import Qt.labs.platform 1.1 — Menu/MenuBar/MenuItem dropped in Qt 6 |
| 503-IMP-N02 | Critical | ❌65 | ❌76 | ✅80 | ⚠️60 | ✅95 | ❌65 | · | **CONFLICT** | import QtWebSockets 1.10 — wrong version for Qt 6.5 |
| 041-MATH-N01 | High | ✅65 | ✅84 | ✅95 | ✅85 | ✅90 | ✅65 | · | AGREE | Division by zero in __timeToArival/__timeToEnd when speed=0 |
| 144-MATH-N02 | Medium | ✅60 | ✅78 | ✅90 | ✅80 | ✅90 | ✅60 | · | AGREE | Bitwise << on floating-point in TimerClock — precision loss |
| 068-LYR-N01 | High | ⚠️60 | ✅84 | ✅85 | ✅85 | ✅90 | ✅68 | · | split | InputsOverlay calls cursorAutoHide.restart() on open instead of reset() |
| 304-LYR-N02 | Medium | ⚠️50 | ✅78 | ✅75 | ⚠️65 | ✅90 | ✅68 | · | split | Three OverlaySheets missing from ESC dismiss chain |
| 586-LYR-N03 | Medium | ❔45 | ✅78 | ✅88 | ⚠️60 | ❌80 | ❔45 | · | **CONFLICT** | ContextDrawer exposes prompter actions while viewing layer pages |
| 224-LYR-N04 | Medium | ⚠️50 | ✅78 | ✅85 | ✅80 | ✅90 | ✅68 | · | split | ESC handler uses activeFocus in base but focus in platform variants — inconsistent |
| 512-TRL-N01 | High | ⚠️55 | ✅84 | ✅95 | ✅85 | ✅95 | ⚠️50 | · | split | qsTr() uses %0 placeholder — should be %1 (font name never displayed) |
| 195-TRL-N02 | Medium | ✅50 | ✅78 | ✅90 | ✅80 | ✅90 | ✅50 | · | AGREE | Application --help description not translatable |
| 265-TRL-N03 | Medium | ⚠️45 | ✅78 | ✅90 | ✅80 | ✅85 | ✅68 | · | split | About-dialog credit roles not translatable |
| 500-W10-HTK-01 | Critical | ❌70 | ❌76 | ✅92 | ✅80 | ✅95 | ❌70 | · | **CONFLICT** | autoRepeat=true for ALL QHotkey shortcuts — non-velocity actions broken when held |
| 066-W10-HTK-02 | High | ✅65 | ✅88 | ✅88 | ✅80 | ✅95 | ✅65 | · | AGREE | QHotkey::setShortcut return value silently ignored — no failure detection |
| 104-W10-PMV-01 | High | ⚠️50 | ⚠️58 | ⚠️70 | ⚠️60 | ✅80 | ✅68 | · | split | font.pixelSize evaluates to 0 before first layout pass — crash hazard |
| 354-W10-PMV-02 | Medium | ⚠️50 | ⚠️58 | ✅80 | ⚠️65 | ✅85 | ✅68 | · | split | Circular ShaderEffectSource dependency — shadow ghost on first frame |
| 101-W10-CLP-01 | High | ⚠️55 | ⚠️58 | ❌80 | ✅80 | ✅85 | ✅68 | · | **CONFLICT** | Paste-without-formatting fails when clipboard lacks text/plain |
| 336-W10-CLP-02 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅80 | ✅85 | ✅68 | · | split | Remote image URLs in pasted HTML cause unsanctioned network requests |
| 064-W10-CNV2-01 | High | ✅80 | ✅92 | ✅90 | ✅85 | ✅95 | ✅80 | · | AGREE | Default stylesheet has invalid CSS color quoting — exported HTML broken in browsers |
| 065-W10-CNV2-02 | High | ✅55 | ✅84 | ✅92 | ✅80 | ✅90 | ✅55 | · | AGREE | No markdown export — round-trip silently destroys all formatting |
| 102-W10-CNV2-03 | High | ⚠️45 | ⚠️58 | ⚠️65 | ✅85 | ✅85 | ✅68 | · | split | import() uses fromStdString on non-Windows — encoding corruption |
| 096-W10-SWT-01 | High | ⚠️55 | ⚠️58 | ✅90 | ✅80 | ✅90 | ✅68 | · | split | CloseActions switch drops RecentLocal/RecentRemote — recent document open silently lost after save |
| 097-W10-SWT-02 | High | ⚠️55 | ⚠️58 | ✅90 | ✅80 | ✅90 | ✅68 | · | split | Same bug in IosSaveDialog.onAccepted path |
| 016-W10-DEP-01 | Critical | ✅75 | ✅92 | ✅92 | ⚠️65 | ✅95 | ✅75 | · | split | Missing vcpkg.json manifest — vcpkg manifest mode installs nothing |
| 019-W10-WSM-01 | Critical | ⚠️55 | ⚠️58 | ✅88 | ✅80 | ✅85 | ✅68 | · | split | Infinite reload loop on unauthorized WASM host — app unusable |
| 337-W10-WSM-02 | Medium | ⚠️50 | ⚠️58 | ✅88 | ✅80 | ✅85 | ✅68 | · | split | Global file-picker state overwritten by re-entrant calls — wrong file delivered |
| 012-W10-PLF-01 | Critical | ✅70 | ✅84 | ✅95 | ✅80 | ✅85 | ✅70 | · | AGREE | BSD detection broken — FreeBSD enters wrong code paths |
| 095-W10-PLF-02 | High | ⚠️50 | ⚠️58 | ✅95 | ✅80 | ✅85 | ✅68 | · | split | QHotkey_FOUND never set in FetchContent path — built but never linked |
| 703-TS-01 |  | ❔40 | ⚠️58 | ✅88 | ✅85 | ✅95 | ❔40 | · | split | Finnish welcome guide → Dutch (not Finnish) |
| 491-TS-02 |  | ⚠️50 | ⚠️58 | ✅90 | ✅85 | ✅95 | ✅68 | · | split | Arabic file `ar_EG` vs UI `ar_AE` mismatch |
| 490-TS-03 |  | ✅90 | ✅78 | ✅90 | ✅90 | ✅95 | ✅90 | · | AGREE | Korean UI `ko_KO` vs file `ko_KR` mismatch |
| 706-TS-04 |  | ❔40 | ❔39 | ✅85 | ❔50 | ✅90 | ❔40 | · | split | French "Saved" → verb "Enregistrer" (should be adjective "Enregistré") |
| 492-TS-05 |  | ⚠️45 | ⚠️58 | ✅85 | ✅80 | ✅85 | ✅68 | · | split | Finnish/French/Korean/Italian "Saved" → verb with stray `&amp;` accelerator |
| 707-TS-06 |  | ❔40 | ❔39 | ✅90 | ❔50 | ✅90 | ❔40 | · | split | Czech/French "Language settings" → "Pointer settings" (copy-paste error) |
| 708-TS-07 |  | ❔40 | ❔39 | ✅85 | ❔50 | ✅90 | ❔40 | · | split | Finnish/French/Korean "Colors for prompter states" → "Toggle Prompter State" |
| 709-TS-08 |  | ❔40 | ❔39 | ✅85 | ❔50 | ✅90 | ❔40 | · | split | French "Prompting:" → "Start prompter" |
| 710-TS-09 |  | ❔40 | ❔39 | ✅85 | ❔50 | ✅90 | ❔40 | · | split | Finnish/French/Korean/Dutch "Vertical offset" → "Velocity" |
| 711-TS-10 |  | ❔40 | ❔39 | ✅85 | ❔50 | ✅90 | ❔40 | · | split | Finnish/Korean "Next reload starts at" → "Step acceleration" |
| 712-TS-11 |  | ❔40 | ❔39 | ✅90 | ❔50 | ✅90 | ❔40 | · | split | French/Finnish/Korean "No pointers" → "Both pointers" (opposite meaning) |
| 713-TS-12 |  | ❔40 | ❔39 | ✅90 | ❔50 | ✅90 | ❔40 | · | split | French "Alt" key → "Tout" (means "All") |
| 714-TS-13 |  | ❔40 | ❔39 | ✅90 | ❔50 | ✅90 | ❔40 | · | split | French "Set velocity to 0–10" (all 11) → identical "Vitesse de départ" |
| 715-TS-14 |  | ❔40 | ❔39 | ✅85 | ❔50 | ✅90 | ❔40 | · | split | French "Clear color" → "Light color" |
| 716-TS-15 |  | ❔40 | ❔39 | ✅85 | ❔50 | ✅90 | ❔40 | · | split | Finnish/Korean right pointer reuse → left pointer (swapped) |
| 493-TS-16 |  | ⚠️45 | ⚠️58 | ✅90 | ✅80 | ✅90 | ✅68 | · | split | Paragraph spacing: 8 languages strip trailing `%` from `<pre>%1%</pre>` |
| 494-TS-17 |  | ⚠️45 | ⚠️58 | ✅90 | ✅80 | ✅90 | ✅68 | · | split | Line width: 7 languages add spurious `%` to `<pre>%1</pre>` |
| 704-TS-18 |  | ❔40 | ❔39 | ✅85 | ✅85 | ✅90 | ❔40 | · | split | Orphan files: Hebrew and Polish exist but UI entries commented out |
| 502-HTK-01 | Critical | ❔45 | ❔39 | ✅95 | ⚠️65 | ✅95 | ❔45 | · | split | KGlobalAccel default permanently destroyed on first user customization |
| 523-HTK-02 | High | ❔45 | ❔39 | ✅92 | ✅80 | ✅90 | ❔45 | · | split | User shortcuts never persisted when only Use_GlobalAccel defined (no QHotkey) |
| 086-HTK-03 | High | ⚠️50 | ⚠️58 | ✅90 | ✅80 | ✅90 | ✅68 | · | split | KGlobalAccel defaults silently zeroed on non-Wayland when QHotkey co-exists |
| 138-HTK-04 | Medium | ✅60 | ✅92 | ✅85 | ✅80 | ✅85 | ✅60 | · | AGREE | Wrong enum type `Qt::KeyboardModifier` (singular) for modifier variable |
| 558-HTK-05 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅85 | ⚠️50 | · | split | VelocityTo0 default shortcut uses `Qt::Key_acute` — unreachable dead key |
| 559-HTK-06 | Medium | ⚠️45 | ⚠️58 | ✅90 | ✅80 | ✅85 | ⚠️50 | · | split | Pause (Ctrl+Space) and Stop (Meta+Space) conflict — Meta+Space captured by OS |
| 630-HTK-07 | Low | ⚠️45 | ⚠️58 | ✅88 | ✅75 | ✅80 | ⚠️50 | · | split | Double `removeAllShortcuts()` IPC round-trip in customization path |
| 631-HTK-08 | Low | ⚠️50 | ⚠️58 | ✅85 | ✅75 | ✅85 | ⚠️50 | · | split | key/modifiers parameters silently discarded mid-function on non-Wayland |
| 531-TMR-01 | High | ❔50 | ❔39 | ✅92 | ✅85 | ✅95 | ❔50 | · | split | Countdown→Prompting auto-transition via state++ bypasses toggle() entirely |
| 579-TMR-02 | Medium | ❔45 | ❔39 | ✅80 | ✅80 | ✅85 | ❔45 | · | split | timer.updateTimer() runs before timer.startTimer() on Prompting entry |
| 327-TMR-03 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅75 | ✅85 | ✅68 | · | split | dissolveIn animation re-triggered entering Running from Ready — flicker |
| 677-TMR-04 | Low | ❔45 | ❔39 | ✅80 | ⚠️60 | ✅80 | ❔45 | · | split | Countdown arc hypotenuse uses geometric center instead of arc center |
| 382-TMR-05 | Low | ✅85 | ✅78 | ✅88 | ✅85 | ✅90 | ✅85 | · | AGREE | ScriptAction `paintReady` references non-existent function |
| 678-TMR-06 | Low | ❔45 | ❔39 | ✅85 | ⚠️60 | ✅80 | ❔45 | · | split | dissolveOut starts too early when disappearWithin > 1 |
| 477-TMR-07 | Low | ✅55 | ⚠️58 | ⚠️65 | ⚠️55 | ✅75 | ✅55 | · | split | countdownAnimation restart uses non-idempotent running=true |
| 679-TMR-08 | Low | ❔45 | ❔39 | ✅80 | ⚠️55 | ✅80 | ❔45 | · | split | timer.running not explicitly set in Countdown state — relies on revert behavior |
| 189-SPL2-11 | Medium | ✅60 | ✅78 | ✅90 | ✅80 | ✅85 | ✅60 | · | AGREE | addCustomWord trims but removeCustomWord does not — asymmetry |
| 190-SPL2-12 | Medium | ✅55 | ✅92 | ✅88 | ✅80 | ✅85 | ✅55 | · | AGREE | Case-sensitive contains/indexOf but case-insensitive sort — duplicates |
| 191-SPL2-13 | Medium | ✅55 | ✅78 | ✅90 | ✅80 | ✅85 | ✅55 | · | AGREE | saveCustomWordsToDisk has void return — callers cannot detect I/O failure |
| 192-SPL2-14 | Medium | ✅65 | ✅92 | ✅85 | ✅75 | ✅85 | ✅65 | · | AGREE | Cached QRC dicts never invalidated after app update |
| 193-SPL2-15 | Medium | ✅60 | ✅78 | ✅90 | ✅85 | ✅85 | ✅60 | · | AGREE | spell() returns true when no dicts loaded — silent no-op |
| 376-SPL2-16 | Low | ✅55 | ✅88 | ✅80 | ✅75 | ✅75 | ✅55 | · | AGREE | QDir::mkpath return unchecked — dict cache directory may silently not exist |
| 377-SPL2-17 | Low | ✅55 | ✅88 | ✅80 | ✅75 | ✅75 | ✅55 | · | AGREE | QFile::setPermissions return unchecked — cached dict may be unreadable |
| 412-SPL2-18 | Low | ✅55 | ✅88 | ✅85 | ⚠️65 | ✅75 | ✅55 | · | split | Hunspell::add return value unchecked at 4 call sites |
| 378-SPL2-19 | Low | ✅55 | ✅78 | ✅85 | ✅80 | ✅80 | ✅55 | · | AGREE | availableDictionaries enumerates .dic without verifying .aff exists |
| 474-SPL2-20 | Low | ⚠️45 | ⚠️58 | ❌85 | ✅75 | ✅70 | ✅68 | · | **CONFLICT** | loadCustomWordsFromDisk redundant exists() before open() |
| 103-WSM-03 | High | ⚠️50 | ⚠️58 | ✅88 | ⚠️65 | ✅80 | ✅68 | · | split | readAsDataURL causes quadruple in-memory copy of file content |
| 108-BLD-05 | Medium | ✅55 | ✅78 | ✅95 | ✅85 | ✅95 | ✅55 | · | AGREE | .env.android references Qt 5.15.2 — project requires Qt 6.8.2+ |
| 098-EVT-01 | High | ⚠️50 | ⚠️58 | ⚠️60 | ✅80 | ✅85 | ✅68 | · | split | velocityDragArea (z:5) blocks viewport.mouse (z:0) wheel events |
| 517-EVT-02 | High | ❌55 | ⚠️58 | ✅88 | ✅80 | ✅85 | ❌55 | · | **CONFLICT** | Zero inputMethodHints on any TextField — IME broken for CJK/Indic |
| 081-EVT-03 | High | ⚠️50 | ⚠️58 | ✅90 | ✅80 | ✅85 | ✅68 | · | split | velocityDragOverlay (z:7) steals clicks from control buttons (z:6) |
| 082-EVT-04 | High | ⚠️50 | ⚠️58 | ✅92 | ✅80 | ✅85 | ✅68 | · | split | Drag breaks editor.x declarative binding permanently |
| 083-EVT-05 | High | ⚠️50 | ⚠️58 | ✅92 | ✅80 | ✅85 | ✅68 | · | split | Drag breaks positionHandler.x declarative binding permanently |
| 292-EVT-06 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅80 | ✅85 | ✅68 | · | split | Drag breaks stopwatch.x binding permanently |
| 126-EVT-07 | Medium | ✅60 | ✅78 | ✅90 | ✅80 | ✅85 | ✅60 | · | AGREE | TabBar currentIndex binding broken on first TabButton click |
| 127-EVT-08 | Medium | ✅60 | ✅78 | ✅88 | ✅80 | ✅85 | ✅60 | · | AGREE | Two additional checkable ToolButton binding breakage instances |
| 457-EVT-09 | Low | ⚠️45 | ⚠️52 | ✅78 | ⚠️60 | ✅70 | ✅68 | · | split | Flow ToolSeparator visibility compares y of potentially invisible rows |
| 458-EVT-10 | Low | ⚠️50 | ⚠️58 | ✅85 | ⚠️60 | ✅85 | ✅68 | · | split | Nested MouseAreas with hoverEnabled steal hover from parent Buttons |
| 124-ENC-01 | Medium | ✅60 | ✅78 | ✅88 | ✅80 | ✅95 | ✅60 | · | AGREE | truncate(-1) when font preview text has no spaces |
| 359-ENC-02 | Low | ✅55 | ✅78 | ✅85 | ✅80 | ✅90 | ✅55 | · | AGREE | getMarkerKey() mid(4) without length/startsWith guard |
| 106-ANM-N01 | Medium | ✅70 | ✅78 | ✅92 | ✅80 | ✅90 | ✅70 | · | AGREE | Easing.EaseOut is not a valid Qt Quick easing type (2 instances) |
| 044-NET-01 | High | ✅65 | ✅84 | ✅92 | ✅85 | ✅95 | ✅65 | · | AGREE | loadFromNetworkFinihed never checks m_reply->error() |
| 587-NET-02 | Medium | ⚠️50 | ⚠️58 | ⚠️70 | ✅80 | ✅90 | ❌72 | · | **CONFLICT** | RedirectPolicyAttribute set to boolean true → NoLessSafeRedirectPolicy |
| 602-THR-01 | Medium | ⚠️45 | ⚠️58 | ✅82 | ⚠️65 | ✅85 | ⚠️50 | · | split | IosSaveDialog::create() — unsynchronized singleton race |
| 603-THR-02 | Medium | ⚠️45 | ⚠️58 | ✅82 | ⚠️65 | ✅85 | ⚠️50 | · | split | ShakeDetector::create() — identical unsynchronized singleton race |
| 643-THR-03 | Low | ⚠️50 | ⚠️58 | ✅80 | ✅80 | ✅85 | ⚠️50 | · | split | search() — mutable static QRegularExpression shared across all callers |
| 578-THR-04 | Medium | ⚠️45 | ✅78 | ⚠️72 | ✅85 | ✅85 | ⚠️50 | · | split | SpellChecker zero thread safety — explicit finding |
| 343-DRW-01 | Medium | ⚠️50 | ⚠️58 | ✅88 | ⚠️65 | ✅85 | ✅68 | · | split | interalFocusElsewhere() misses 3 OverlaySheets + 2 Drawers — hotkeys pass through |
| 344-DRW-02 | Medium | ⚠️50 | ⚠️58 | ✅88 | ⚠️65 | ✅85 | ✅68 | · | split | globalDrawer and contextDrawer missing from ESC dismiss chain |
| 013-AND-BLD-01 | Critical | ✅80 | ✅92 | ✅95 | ⚠️65 | ✅95 | ✅80 | · | split | Missing version.gradle — Gradle build fails |
| 278-AND-RES-01 | Medium | ⚠️45 | ⚠️58 | ✅90 | ✅80 | ✅90 | ✅68 | · | split | Invalid android:scaleType on bitmap element |
| 340-AND-MFT-01 | Medium (latent) | ⚠️45 | ⚠️58 | ✅85 | ⚠️65 | ✅75 | ✅68 | · | split | FileProvider resource @xml/qtprovider_paths — file named filepaths.xml |
| 442-SHADOW-01 | Low | ✅60 | ✅78 | ✅85 | ⚠️60 | ❌80 | ✅60 | · | **CONFLICT** | id: rotation shadows Item.rotation property |
| 443-SHADOW-02 | Low | ✅55 | ✅78 | ✅85 | ⚠️60 | ❌80 | ✅55 | · | **CONFLICT** | id: flow shadows Flow.flow property |
| 360-FOC-N01 | Low | ✅65 | ✅78 | ✅88 | ✅80 | ✅95 | ✅65 | · | AGREE | focus: true is JS label in atEndLoopDelay SpinBox |
| 361-FOC-N02 | Low | ✅65 | ✅78 | ✅88 | ✅80 | ✅95 | ✅65 | · | AGREE | Same JS label bug in countdownConfiguration SpinBoxes (2 instances) |
| 423-FOC-N03 | Low | ⚠️50 | ✅78 | ✅85 | ⚠️60 | ✅85 | ✅68 | · | split | Tab/Backtab asymmetry — Backtab silently unhandled |
| 683-VER-01 | Low | ⚠️45 | ✅78 | ✅85 | ⚠️60 | ❌90 | ❌72 | · | **CONFLICT** | Qt::MarkdownText version guard 0x050F00 (5.15) — API added in 5.14 |
| 658-CPY-01 | Low | ⚠️40 | ⚠️58 | ✅80 | ✅75 | ❌80 | ⚠️50 | · | **CONFLICT** | 5 Q_INVOKABLE methods pass QString by value instead of const& |
| 209-DSZ-01 | Medium | ✅60 | ⚠️58 | ✅88 | ✅80 | ✅80 | ✅60 | · | split | InputsOverlay hardcoded height:680 — overflows on phones |
| 210-DSZ-02 | Medium | ⚠️45 | ✅78 | ✅88 | ✅75 | ✅85 | ✅68 | · | split | pointerConfiguration OverlaySheet no vertical ScrollView |
| 480-DSZ-03 | Low | ⚠️40 | ⚠️58 | ✅85 | ⚠️60 | ❌70 | ✅68 | · | **CONFLICT** | Magic number 68 in ListView height binding |
| 035-JSN-01 | High | ✅65 | ✅92 | ✅90 | ✅85 | ✅90 | ✅65 | · | AGREE | i.d.authentication accessed without undefined guard |
| 218-JSN-02 | Medium | ⚠️50 | ✅78 | ✅90 | ✅80 | ✅85 | ✅68 | · | split | ws.sendTextMessage() called without checking WebSocket status |
| 368-QCN-01 | Low | ✅55 | ✅78 | ✅90 | ✅75 | ✅80 | ✅55 | · | AGREE | O(n²) contains()-in-loop during custom words file load |
| 588-PC-01 | Medium | ❔45 | ❔39 | ✅70 | ⚠️65 | ✅90 | ❔45 | · | split | countdown.state not set in Prompting state — countdown visible during teleprompting |
| 160-QTD-01 | Medium | ✅65 | ✅78 | ✅85 | ✅80 | ✅85 | ✅65 | · | AGREE | m_spellHighlighter not detached when setDocument(nullptr) |
| 702-QTD-02 | Low-Medium | ❔40 | ✅78 | ✅85 | ⚠️60 | ✅80 | ❔40 | · | split | QQuickTextDocument destroyed without destroyed signal connection |
| 231-OPC-01 | Medium | ⚠️50 | ✅78 | ✅90 | ✅80 | ✅85 | ✅68 | · | split | Right-click toggle desynchronizes velocityIndicator visible/opacity |
| 401-HDR-N01 | Low | ✅60 | ⚠️58 | ✅95 | ✅80 | ✅80 | ✅60 | · | split | promptsession.h not in CMakeLists.txt — SessionModel/DataPoint dead code |
| 402-HDR-N02 | Low | ✅60 | ⚠️58 | ✅95 | ✅80 | ✅80 | ✅60 | · | split | telemetry.h not in CMakeLists.txt — Telemetry dead code |
| 217-IO-N01 | Medium | ⚠️45 | ✅78 | ✅90 | ✅80 | ✅90 | ✅68 | · | split | saveAs() leaves _fileSystemWatcher permanently blocked on open failure |
| 034-IO-N02 | High | ✅50 | ✅84 | ✅85 | ✅85 | ✅95 | ✅50 | · | AGREE | save() constructs QUrl without file:// scheme — broken on non-Windows |
| 140-IO-N03 | Medium | ✅55 | ✅88 | ✅90 | ✅80 | ✅75 | ✅55 | · | AGREE | iossavedialog.mm QFile::write() return value unchecked |
| 049-QML-BND-01 | High | ✅60 | ✅84 | ✅90 | ✅80 | ✅90 | ✅60 | · | AGREE | countdownAnimation.running binding permanently broken after first iteration |
| 157-QML-BND-02 | Medium | ✅55 | ✅78 | ✅90 | ✅80 | ✅85 | ✅55 | · | AGREE | clock.__iteration binding broken by post-decrement in animation handler |
| 723-QML-BND-03 | None (info) | ⚠️40 | ⚠️58 | ✅95 | ❌85 | ❌70 | ❌72 | · | **CONFLICT** | ReadRegionOverlay onDestruction — harmless dead code |
| 067-WSM-N01 | High | ✅60 | ✅84 | ✅85 | ✅80 | ✅80 | ✅60 | · | AGREE | Synchronous QImage::load() from HTTP blocks WASM main thread |
| 387-WSM-N02 | Low | ✅60 | ✅78 | ✅90 | ✅80 | ✅85 | ✅60 | · | AGREE | WASM preventSleep() falls through to desktop #else — always returns false |
| 622-QRC-N01 | Low | ❔45 | ✅92 | ✅95 | ✅80 | ✅95 | ❔45 | · | split | icons.qrc contains duplicate \<file\> entry |
| 435-QRC-N02 | Low | ⚠️45 | ⚠️58 | ✅90 | ✅80 | ✅85 | ✅68 | · | split | Four .qrc files are dead code — never referenced by CMakeLists.txt |
| 648-CMAKE-N01 | Low | ⚠️45 | ⚠️58 | ❔60 | ✅80 | ✅70 | ❌72 | · | **CONFLICT** | WASM build excludes TelemetryPage.qml and RemotePage.qml |
| 229-OOB-N01 | Medium | ⚠️50 | ✅78 | ✅90 | ✅80 | ✅90 | ✅68 | · | split | MarkersModel::data() — m_data.at() without row < rowCount() guard |
| 230-OOB-N02 | Medium | ⚠️45 | ✅78 | ✅90 | ✅80 | ✅85 | ✅68 | · | split | SessionModel::data() — same missing row bounds guard |
| 668-OOB-N03 | Low | ⚠️50 | ✅78 | ✅85 | ⚠️60 | ❌80 | ⚠️50 | · | **CONFLICT** | alignment() fetches textCursor() twice — stale cursor race |
| 632-I18N-N01 | Low | ⚠️40 | ⚠️58 | ✅80 | ✅75 | ✅70 | ⚠️50 | · | split | Stale source-location line numbers in all 20 .ts files |
| 633-I18N-N02 | Low | ⚠️40 | ⚠️58 | ✅80 | ✅75 | ✅70 | ⚠️50 | · | split | Vanished translation entries not purged across 13 language files |
| 063-STR-N01 | High | ✅70 | ✅84 | ✅90 | ✅85 | ✅95 | ✅70 | · | AGREE | main.cpp:158 QLatin1String iterator-pair UB from two unrelated string literals |
| 152-NOTIFY-01 | Medium | ✅75 | ✅78 | ✅95 | ✅80 | ✅95 | ✅75 | · | AGREE | setAutoReload doesn't emit autoReloadChanged NOTIFY signal |
| 409-NOTIFY-02 | Low | ✅55 | ✅78 | ⚠️85 | ✅80 | ✅85 | ✅55 | · | split | availableDictionariesChanged NOTIFY signal never emitted |
| 620-MIX-01 | Low | ⚠️40 | ✅78 | ✅90 | ✅75 | ✅70 | ⚠️50 | · | split | spellchecker.cpp:98 size_t→int narrowing in languages() reserve |
| 211-ENUM-01 | Medium | ⚠️45 | ✅78 | ✅90 | ✅80 | ✅85 | ✅68 | · | split | documenthandler.cpp:1108 updateContents switch no default — silent data loss |
| 342-DPI-01 | Medium | ⚠️40 | ⚠️58 | ✅80 | ⚠️65 | ✅85 | ✅68 | · | split | TimerClock.qml:127 devicePixelRatio in raw arithmetic with magic multiplier |
| 455-DPI-02 | Low | ⚠️45 | ⚠️58 | ✅85 | ✅75 | ❌75 | ✅68 | · | **CONFLICT** | MarkersDrawer.qml:37 drawer minimumWidth hardcoded to 260px |
| 456-DPI-03 | Low | ⚠️45 | ⚠️58 | ✅90 | ✅75 | ❌75 | ✅68 | · | **CONFLICT** | Find.qml:38 searchBarWidth:724 hardcoded in px |
| 208-DPI-04 | Medium | ✅60 | ⚠️58 | ✅90 | ✅80 | ✅80 | ✅60 | · | split | InputsOverlay.qml:33 height:680 hardcoded |
| 459-GEO-01 | Low | ⚠️45 | ⚠️58 | ✅80 | ✅75 | ❌80 | ✅68 | · | **CONFLICT** | main.qml initial 728px height too large for 1366x768 laptops |
| 295-GEO-02 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅80 | ✅85 | ✅68 | · | split | main.qml persists x/y/width/height with zero validation |
| 424-GEO-03 | Low | ⚠️40 | ⚠️58 | ✅90 | ✅75 | ✅70 | ✅68 | · | split | +android/main.qml no minimumWidth/minimumHeight |
| 078-UNIT-01 | High | ⚠️55 | ✅84 | ✅95 | ✅80 | ✅95 | ✅68 | · | split | ProgressIndicator.qml:46 Units.ShortDuration with no Kirigami import |
| 079-UNIT-02 | High | ⚠️55 | ✅84 | ✅95 | ✅80 | ✅95 | ✅68 | · | split | PrompterView.qml 7x Units.ShortDuration with no Kirigami import |
| 269-UNIT-03 | Medium | ⚠️50 | ✅78 | ✅95 | ✅75 | ✅90 | ✅68 | · | split | PrompterBackground.qml:160 Units.LongDuration no Kirigami import |
| 270-UNIT-04 | Medium | ⚠️50 | ✅78 | ✅95 | ✅75 | ✅90 | ✅68 | · | split | Flip.qml:34,41 two Units.LongDuration no Kirigami import |
| 413-UNIT-05 | Low | ⚠️50 | ✅78 | ✅95 | ✅75 | ✅90 | ✅68 | · | split | pointer_0.qml:72 Units.VeryLongDuration no Kirigami import |
| 333-UNIT-06 | Medium | ⚠️50 | ✅78 | ✅95 | ⚠️65 | ✅90 | ✅68 | · | split | Find.qml:92 Units.ShortDuration with namespaced Kirigami import |
| 334-UNIT-07 | Medium | ⚠️50 | ✅78 | ✅90 | ⚠️65 | ✅90 | ✅68 | · | split | ReadRegionOverlay.qml 3x Units.ShortDuration with namespaced import |
| 625-AR-01 | Low | ⚠️45 | ✅78 | ✅75 | ⚠️60 | ✅75 | ⚠️50 | · | split | PrompterView.qml:53-58 Rotation debug feature clips on extreme aspect ratios |
| 316-SAFE-01 | Medium | ⚠️45 | ⚠️58 | ✅80 | ✅80 | ✅75 | ✅68 | · | split | +android/main.qml zero safe area insets |
| 317-SAFE-02 | Medium | ⚠️45 | ⚠️58 | ✅80 | ✅75 | ✅75 | ✅68 | · | split | ReadRegionOverlay screenMiddle ignores notch/status bar height |
| 530-SET-01 | High | ⚠️45 | ✅84 | ✅90 | ⚠️65 | ✅90 | ⚠️50 | · | split | macOS/iOS: QSettings split across two preference domains |
| 511-SET-02 | High | ❔45 | ✅84 | ✅90 | ✅80 | ✅90 | ❔45 | · | split | factoryReset() incomplete on macOS/iOS — domain-path settings survive |
| 639-SET-03 | Low | ⚠️50 | ✅78 | ✅85 | ✅75 | ❌75 | ❌72 | · | **CONFLICT** | QString "true" used as default for boolean QSettings value |
| 640-SET-04 | Low | ⚠️45 | ✅78 | ✅85 | ✅75 | ❌75 | ⚠️50 | · | **CONFLICT** | spellCheckLanguages read without explicit default value |
| 216-INV-N01 | Medium | ⚠️50 | ✅78 | ✅85 | ✅80 | ✅85 | ✅68 | · | split | QmlUtil::r() stores QML-owned QQuickItemGrabResult raw pointer — use-after-free |
| 392-CMAKE-NEW-01 | Low | ⚠️45 | ✅78 | ✅90 | ✅75 | ✅80 | ✅68 | · | split | Remote.qml exists on disk but never listed in QML_FILES |
| 111-CMAKE-NEW-02 | Medium | ✅55 | ✅92 | ✅90 | ✅80 | ✅90 | ✅55 | · | AGREE | Duplicate install() of appdata.xml/desktop in root and src/CMakeLists.txt |
| 112-CMAKE-NEW-03 | Medium | ✅55 | ✅78 | ✅90 | ✅80 | ✅85 | ✅55 | · | AGREE | find_package(KF6Crash ... COMPONENTS) — COMPONENTS keyword with zero names |
| 113-CMAKE-NEW-04 | Medium | ✅60 | ✅78 | ✅90 | ✅80 | ✅85 | ✅60 | · | AGREE | execute_process uses CMAKE_PREFIX_PATH (list) as scalar — broken command |
| 024-DLG-N01 | High | ✅60 | ✅84 | ✅90 | ✅85 | ✅95 | ✅60 | · | AGREE | document.modified=false set BEFORE saveAs() — failed save loses unsaved flag |
| 025-DLG-N02 | High | ✅65 | ✅84 | ✅95 | ✅85 | ✅95 | ✅65 | · | AGREE | onError handler clears document.modified on save failure |
| 395-DLG-N03 | Low | ⚠️45 | ✅78 | ✅90 | ✅75 | ✅80 | ✅68 | · | split | errorDialog MessageDialog has no title |
| 120-DLG-N04 | Medium | ✅60 | ✅78 | ✅90 | ✅80 | ✅90 | ✅60 | · | AGREE | load() silently fails with no notification when file missing or unreadable |
| 121-DLG-N05 | Medium | ✅55 | ✅78 | ✅90 | ✅80 | ✅85 | ✅55 | · | AGREE | loadFromNetworkFinihed() silently ignores empty response |
| 026-DLG-N06 | High | ✅65 | ✅84 | ✅90 | ✅80 | ✅90 | ✅65 | · | AGREE | import() error strings passed as document content via updateContents() |
| 396-DLG-N07 | Low | ⚠️45 | ✅78 | ✅85 | ✅75 | ✅85 | ✅68 | · | split | 5 showPassiveNotification() calls ignore passiveNotifications preference |
| 397-DLG-N08 | Low | ⚠️45 | ✅78 | ✅85 | ✅75 | ✅80 | ✅68 | · | split | 3 save-completion passive notifications lack passiveNotifications guard |
| 535-IMP-NEW-01 | High | ❌65 | ❌76 | ✅90 | ❌80 | ✅95 | ❌65 | · | **CONFLICT** | #include \<qnativeinterface.h\> doesn't exist — breaks Android build |
| 698-IMP-NEW-02 | Low | ⚠️45 | ⚠️58 | ⚠️80 | ⚠️60 | ❌80 | ⚠️50 | · | split | main.cpp:22 #include "qglobal.h" uses quotes + Qt5-era name |
| 664-IMP-NEW-03 | Low | ⚠️40 | ⚠️58 | ✅95 | ✅75 | ❌70 | ⚠️50 | · | **CONFLICT** | main.cpp:38-39 redundant #include \<QtQml/qqml.h\> + #include \<QtQml\> |
| 686-IMP-NEW-04 | Low | ⚠️40 | ⚠️58 | ✅90 | ⚠️60 | ❌75 | ❌72 | · | **CONFLICT** | AboutPage.qml imports Kirigami 2.9 vs 2.11 in all other files |
| 687-IMP-NEW-05 | Low (orphaned QRC, never compiled) | ❔45 | ⚠️58 | ⚠️80 | ⚠️55 | ✅70 | ❔45 | · | split | pointers.qrc RESOURCE_PREFIX conflicts with qt_add_qml_module |
| 405-MA-N01 | Low | ⚠️50 | ✅78 | ✅95 | ✅75 | ✅70 | ✅68 | · | split | overlayMouseArea permanently disabled — dead MouseArea |
| 363-MA-N02 | Low | ✅55 | ✅78 | ✅85 | ✅75 | ✅85 | ✅55 | · | AGREE | textDragArea missing cursorShape — ArrowCursor over IBeamCursor on editor |
| 551-CMT-N01 | Medium | ⚠️40 | ⚠️48 | ✅90 | ✅80 | ✅80 | ⚠️50 | · | split | Justify ToolButton comment says it's commented out — but it's active |
| 650-CMT-N02 | Low | ⚠️35 | ⚠️48 | ✅90 | ✅75 | ❌70 | ⚠️50 | · | **CONFLICT** | Truncated comment in markersmodel.cpp:107-108 |
| 606-CMT-N03 | Medium | ⚠️35 | ⚠️48 | ✅85 | ⚠️60 | ❌70 | ⚠️50 | · | **CONFLICT** | Misleading OpenGL workaround comment — scope of impact understated |
| 607-CMT-N04 | Medium | ❌55 | ❌76 | ✅85 | ⚠️60 | ❌75 | ❌55 | · | **CONFLICT** | Comment masks invalid enum bug — 2 - value produces out-of-range LayoutDirection |
| 539-CMT-N05 | High | ⚠️40 | ⚠️48 | ✅85 | ⚠️60 | ❌75 | ❌72 | · | **CONFLICT** | Missing security warning on QProcess RCE sink (sys://) |
| 608-CMT-N06 | Medium | ⚠️40 | ⚠️48 | ✅80 | ⚠️60 | ❌70 | ❌72 | · | **CONFLICT** | Missing warning: re-entrant toggle() inside Behavior.onRunningChanged |
| 609-CMT-N07 | Medium | ⚠️40 | ⚠️48 | ✅85 | ⚠️60 | ❌70 | ❌72 | · | **CONFLICT** | Missing warning: joinPreviousEditBlock() without beginEditBlock() |
| 205-CMT-N08 | Medium | ✅50 | ⚠️48 | ✅90 | ✅75 | ✅75 | ✅50 | · | split | Entire Telemetry class is dead commented-out shell across 4 files |
| 610-CMT-N09 | Medium | ⚠️40 | ⚠️48 | ✅85 | ⚠️60 | ❌70 | ⚠️50 | · | **CONFLICT** | Commented-out PropertyActions in active loop animation — stale state risk |
| 626-CMT-N10 | Low | ⚠️35 | ⚠️48 | ✅90 | ✅75 | ✅90 | ⚠️50 | · | split | Obsolete Qt 5 qmlRegisterType calls as commented-out cruft |
| 548-REGEX-N01 | Medium | ⚠️45 | ✅78 | ✅85 | ✅75 | ✅95 | ⚠️50 | · | split | All 13 QRegularExpression objects lack isValid() checks |
| 180-REGEX-N02 | Medium | ✅55 | ✅78 | ✅80 | ✅80 | ✅95 | ✅55 | · | AGREE | regex_5 accidentally excludes 15+ HTML5 tags from background-color filtering |
| 371-REGEX-N03 | Low | ✅65 | ✅78 | ✅85 | ✅75 | ✅85 | ✅65 | · | AGREE | Unescaped dot in font-size regex — matches any char instead of decimal |
| 085-HK-N01 | High | ⚠️50 | ⚠️58 | ✅90 | ✅80 | ✅95 | ✅68 | · | split | Missing event.isAutoRepeat guard on main Keys.onPressed |
| 136-HK-N02 | Medium | ✅80 | ✅92 | ✅95 | ✅85 | ✅98 | ✅80 | · | AGREE | Typo Qt.Key_VolumeDowm — "Dowm" instead of "Down" — volume-down hardware key dead |
| 100-HK-N03 | High | ⚠️50 | ⚠️58 | ✅90 | ⚠️65 | ✅90 | ✅68 | · | split | platformName() != "wayland" fails on "wayland-egl" — global hotkeys dead |
| 297-HK-N04 | Medium | ⚠️45 | ⚠️58 | ✅85 | ✅80 | ✅90 | ✅68 | · | split | No auto-repeat guard in key-binding configuration Keys.onPressed |
| 137-HK-N05 | Medium | ✅60 | ✅78 | ✅85 | ✅80 | ✅92 | ✅60 | · | AGREE | Strict === equality on modifiers breaks user keybinds with NumLock |
| 425-HK-N06 | Low | ⚠️45 | ⚠️58 | ✅80 | ✅75 | ✅85 | ✅68 | · | split | isValidInput checks local keybindings only — silent conflict with global hotkeys |
| 301-LDR-N01 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅80 | ✅90 | ✅68 | · | split | InputsOverlay typeof null guard fails — null.item crash on rapid close |
| 232-PARSE-N01 | Medium | ⚠️50 | ✅78 | ✅85 | ✅80 | ✅95 | ✅68 | · | split | insertImageAt() stores image resource with file:// key but looks up via plain path |
| 153-PARSE-N02 | Medium | ✅60 | ✅78 | ✅85 | ✅80 | ✅95 | ✅60 | · | AGREE | MarkersModel::keySearch() hits=1 limits search to first marker only |
| 045-PROP-N01 | High | ✅70 | ✅84 | ✅95 | ✅85 | ✅90 | ✅70 | · | AGREE | on__FullScreenChanged handler casing mismatch — never fires |
| 569-PROP-N02 | Medium | ⚠️55 | ⚠️58 | ✅85 | ✅80 | ✅95 | ⚠️50 | · | split | setCursorPosition → reset() — 12-signal storm, no debounce |
| 671-PROP-N03 | Low | ⚠️45 | ⚠️58 | ✅85 | ⚠️60 | ✅90 | ⚠️50 | · | split | setMarker/setKeyMarker/setMarkerHref silently trigger full document reparse |
| 150-NET-N04 | Medium | ✅60 | ✅78 | ✅90 | ✅75 | ✅90 | ✅60 | · | AGREE | No transfer timeout on any QNetworkRequest |
| 151-NET-N05 | Medium | ✅60 | ✅78 | ✅85 | ✅80 | ✅95 | ✅60 | · | AGREE | loadFromNetwork() hardcodes http:// scheme — never upgrades to HTTPS |
| 408-NET-N06 | Low | ✅65 | ⚠️58 | ✅85 | ✅80 | ✅95 | ✅65 | · | split | loadFromNetwork() validates original URL, not constructed resultingUrl |
| 271-URL-N01 | Medium | ✅60 | ⚠️58 | ✅65 | ✅80 | ✅90 | ✅60 | · | split | reload() constructs file:// URL by string concatenation without encoding |
| 358-DISK-N01 | Low | ✅55 | ✅78 | ✅55 | ✅75 | ✅90 | ✅55 | · | AGREE | saveCustomWordsToDisk() non-atomic write — data loss on power failure |
| 139-INIT-N01 | Medium | ✅90 | ✅78 | ✅90 | ✅80 | ✅95 | ✅90 | · | AGREE | Velocity modifier ComboBox model has 2 entries, switch handles 4 cases |
| 362-INIT-N02 | Low | ✅50 | ✅78 | ✅85 | ✅75 | ✅90 | ✅50 | · | AGREE | Find.qml SearchField placeholderText always empty — no guidance text |
| 688-INIT-N03 | Low | ⚠️40 | ⚠️58 | ⚠️40 | ⚠️60 | ✅85 | ❌72 | · | **CONFLICT** | ReadRegionOverlay screenMiddle uses root.y from cross-file id resolution |
| 689-INIT-N04 | Low | ⚠️40 | ⚠️58 | ❌80 | ⚠️60 | ✅75 | ❌72 | · | **CONFLICT** | PrompterView ShaderEffectSource.sourceItem references prompter id declared later |
| 582-CMB-N01 | Medium | ❔45 | ❔39 | ✅70 | ⚠️65 | ✅95 | ❔45 | · | split | autoReloadSeconds SpinBox from binding circular — clamps to 1 when all-zero |
| 649-CMB-N02 | Low | ❔45 | ❔39 | ✅75 | ⚠️60 | ✅90 | ❔45 | · | split | autoReloadMinutes SpinBox from contains redundant circular self-reference |
| 114-CMB-N03 | Medium | ✅85 | ✅78 | ✅85 | ✅80 | ✅95 | ✅85 | · | AGREE | LanguageSettingsOverlay ListView currentIndex always -1 — wrong indexOf() call |
| 487-VIS-N04 | Low | ⚠️45 | ⚠️58 | ⚠️45 | ⚠️60 | ✅85 | ✅68 | · | split | Countdown crosshair frame renders orphan lines when enabled=false |
| 335-VIS-N05 | Medium | ⚠️50 | ⚠️58 | ✅65 | ✅75 | ✅92 | ✅68 | · | split | velocityDragOverlay blocks all interaction during indicator fade-out (~500ms dead zone) |
| 615-SCRL-N01 | Medium | ❔45 | ❔39 | ⚠️50 | ⚠️60 | ✅80 | ⚠️50 | · | split | __jitterMargin: fractional result from modulus violates 0/1 toggle design |
| 319-SCRL-N02 | Medium | ⚠️50 | ⚠️58 | ✅65 | ✅75 | ✅90 | ✅68 | · | split | __destination typed int truncates real-valued position |
| 575-SCRL-N03 | Medium | ❔45 | ❔39 | ✅55 | ✅75 | ✅95 | ❔45 | · | split | setVelocity() triggers two conflicting scroll animations with intermediate velocity |
| 374-SCRL-N04 | Low | ✅55 | ✅78 | ✅85 | ✅75 | ✅95 | ✅55 | · | AGREE | __speed non-zero when __i=0 and __curvature=0 (Math.pow(0,0)===1) |
| 693-SCRL-N05 | Low | ⚠️50 | ⚠️58 | ❌65 | ⚠️60 | ✅80 | ⚠️50 | · | **CONFLICT** | __speedLimit check is dead logic — always true |
| 694-SCRL-N06 | Low | ⚠️40 | ⚠️58 | ❌60 | ⚠️55 | ✅75 | ❌72 | · | **CONFLICT** | __timeToEnd uses unexplained 2× factor |
| 384-TYP-N01 | Low | ✅85 | ✅92 | ✅90 | ✅75 | ✅98 | ✅85 | · | AGREE | Misspelled method name: loadFromNetworkFinihed (missing 's') |
| 385-TYP-N02 | Low | ✅90 | ✅92 | ✅90 | ✅75 | ✅98 | ✅90 | · | AGREE | Misspelled parameter: withoutFormating (missing 't') |
| 644-TYP-N03 | Low | ⚠️35 | ⚠️58 | ✅80 | ✅75 | ✅90 | ⚠️50 | · | split | Inconsistent `_` vs `m_` member prefix: _markersModel, _fileSystemWatcher |
| 681-TYP-N04 | Low | ⚠️35 | ⚠️58 | ✅75 | ✅70 | ❌85 | ⚠️50 | · | **CONFLICT** | Inconsistent m_ method naming: m_initializeSource — mixed underscore+camelCase |
| 386-TYP-N05 | Low | ✅90 | ✅88 | ✅70 | ✅80 | ✅90 | ✅90 | · | AGREE | Uninitialized member m_documentComesFromNetwork |
| 682-TYP-N06 | Low | ⚠️50 | ⚠️58 | ✅65 | ⚠️65 | ✅85 | ⚠️50 | · | split | 9 getters copy-paste double-textCursor() pattern — null check on stale cursor |
| 109-CAST-N01 | Medium | ✅60 | ✅78 | ✅70 | ✅80 | ✅90 | ✅60 | · | AGREE | setFontCapitalization static_cast with no range validation — reachable from QML |
| 584-IMG-N01 | Medium | ❔45 | ❔39 | ❔30 | ✅80 | ✅95 | ❔45 | · | split | Missing go-previous-symbolic.svg — back-navigation icon blank on Android/Windows |
| 581-ACT-N05 | Medium | ❔45 | ⚠️58 | ⚠️45 | ✅80 | ✅85 | ❔45 | · | split | +windows main.qml Controls Settings submenu missing OBS Settings action |
| 451-ACT-N06 | Low | ⚠️45 | ⚠️58 | ⚠️45 | ✅75 | ✅80 | ✅68 | · | split | +windows main.qml Performance tweaks missing enableBarsSetting |
| 199-ACT-N07 | Medium | ✅60 | ⚠️58 | ✅65 | ✅75 | ✅90 | ✅60 | · | split | namedBookmarkButton: checkable button opens dialog — stale indicator after first click |
| 339-ACT-N08 | Medium (masked — Labs.MenuBar dead per IMP-N01) | ✅55 | ⚠️58 | ⚠️50 | ⚠️65 | ✅75 | ✅55 | · | split | All checkable Labs.MenuItems inherit R2-EDT-03 binding-break pattern |
| 256-RENDER-01 | Medium | ⚠️50 | ✅78 | ✅70 | ✅75 | ✅80 | ✅68 | · | split | ShaderEffectSource prompterShadowSource runs unconditionally — wastes GPU capture when shadows disabled |
| 257-RENDER-02 | Medium | ⚠️50 | ✅78 | ✅70 | ✅75 | ✅80 | ✅68 | · | split | ShaderEffectSource pointerShadowSource runs unconditionally — same pattern |
| 680-TXT-N01 | Low | ⚠️40 | ⚠️58 | ⚠️40 | ✅75 | ✅95 | ⚠️50 | · | split | Find/replace fields missing persistentSelection: true |
| 446-TXT-N02 | Low | ⚠️40 | ✅78 | ✅75 | ✅75 | ❌90 | ✅68 | · | **CONFLICT** | TimerClock default text color #AAA on #131619 — fails WCAG AA contrast |
| 567-PLAT-N01 | Medium | ⚠️45 | ✅78 | ❌85 | ✅80 | ✅75 | ⚠️50 | · | **CONFLICT** | qmlutil.hpp incorrectly excludes QNX from QProcess — run()/restartApplication() silently no-op |
| 568-PLAT-N02 | Medium | ❔40 | ✅78 | ❌85 | ✅80 | ✅70 | ❌72 | · | **CONFLICT** | documenthandler.cpp incorrectly excludes QNX from import() — LibreOffice broken on QNX |
| 536-PLAT-N03 | High | ❔45 | ❔39 | ❌80 | ✅80 | ✅90 | ❔45 | · | **CONFLICT** | Zero Q_OS_TVOS preprocessor guards in C++ despite 19 QML references — build failure |
| 619-DECL-N01 | Low | ⚠️45 | ✅78 | ✅75 | ✅75 | ✅95 | ⚠️50 | · | split | MarkersModel::keySearch — default params in definition but not declaration |
| 629-DECL-N02 | Low | ⚠️40 | ✅78 | ✅85 | ⚠️60 | ✅90 | ⚠️50 | · | split | SessionModel::resetInternalData() missing override keyword and Qt 6 version guard |
| 286-COLOR-01 | Medium | ✅70 | ⚠️58 | ⚠️50 | ✅80 | ✅90 | ✅70 | · | split | ProjectionsManager.qml uses invalid "initial" color — repro of R4-ROOT-02 |
| 287-COLOR-02 | Medium | ⚠️40 | ⚠️58 | ✅75 | ✅75 | ✅90 | ✅68 | · | split | Hardcoded #EED text invisible on light themes — WheelSettingsOverlay |
| 479-COLOR-03 | Low | ⚠️40 | ⚠️58 | ⚠️45 | ⚠️60 | ✅90 | ✅68 | · | split | velocityText ColorAnimation flash: #BBB → #FFF → #CCC jump |
| 454-COLOR-04 | Low | ⚠️45 | ⚠️58 | ✅65 | ⚠️55 | ✅90 | ✅68 | · | split | ReadRegionOverlay ColorAnimation tracks __fillColor that never changes |
| 651-COLOR-05 | Low | ⚠️40 | ⚠️58 | ⚠️40 | ✅70 | ✅85 | ⚠️50 | · | split | Prompter scrollbar gradient hardcodes #CCC/#998/#665 — low contrast on light backgrounds |
| 652-COLOR-06 | Low | ⚠️40 | ⚠️58 | ⚠️40 | ✅70 | ✅85 | ⚠️50 | · | split | Countdown #FFF digits on #333-at-0.48-overlay — insufficient contrast on light backgrounds |
| 627-COLOR-07 | Low | ⚠️55 | ⚠️58 | ✅65 | ✅75 | ✅90 | ⚠️50 | · | split | CSS default stylesheet hardcodes #FFFFFF body text — ignores user text color |
| 583-EVT-N10 | Medium | ❔45 | ⚠️58 | ✅70 | ✅75 | ❌60 | ❔45 | · | **CONFLICT** | Editor Ctrl+Letter shortcuts don't accept event — marker key-search double-fires |
| 481-EVT-N11 | Low | ⚠️45 | ⚠️58 | ❌70 | ✅75 | ❌70 | ✅68 | · | **CONFLICT** | windowStayOnTopButton lacks focusPolicy — unreachable via keyboard |
| 482-EVT-N12 | Low | ⚠️50 | ⚠️58 | ✅60 | ⚠️60 | ⚠️50 | ✅68 | · | split | velocityDragArea and viewport.mouse share z:5 — wheel dispatch ambiguous |
| 537-STATE-N01 | High | ❔45 | ✅84 | ⚠️50 | ✅80 | ❌70 | ❔45 | · | **CONFLICT** | Shadowed Prompting→Editing transition — velocity default never saved |
| 262-STATE-N02 | Medium | ⚠️50 | ✅78 | ✅75 | ✅80 | ✅80 | ✅68 | · | split | Find.toggle() uses !visible instead of !isOpen — can't close during Prompting |
| 444-STATE-N03 | Low | ⚠️50 | ✅78 | ✅65 | ⚠️60 | ✅80 | ✅68 | · | split | Countdown Running restarts dissolveIn unnecessarily — visual dim-to-bright flash |
| 641-STATE-N04 | Low | ❔45 | ✅78 | ✅70 | ⚠️55 | ✅75 | ❔45 | · | split | loop animation cancel() state change overridden by toggle() due to QML batching |
| 188-SIZE-N01 | Medium | ✅60 | ✅78 | ✅80 | ✅75 | ✅95 | ✅60 | · | AGREE | concentricCircles Shape has conflicting anchors.fill + anchors.centerIn |
| 375-SIZE-N02 | Low | ✅55 | ✅78 | ✅75 | ✅70 | ✅65 | ✅55 | · | AGREE | Three Button children of Row have dead anchors.bottom declarations |
| 653-CONST-N01 | Low | ⚠️40 | ⚠️58 | ✅60 | ✅70 | ❌75 | ⚠️50 | · | **CONFLICT** | getMarkerKey() not const — pure reader without side effects |
| 654-CONST-N02 | Low | ⚠️40 | ⚠️58 | ✅60 | ✅70 | ❌75 | ⚠️50 | · | **CONFLICT** | getMarkerHref() not const — identical pattern |
| 655-CONST-N03 | Low | ⚠️40 | ⚠️58 | ✅55 | ✅70 | ❌70 | ⚠️50 | · | **CONFLICT** | MarkersModel::previousMarker(), nextMarker(), keySearch(), binarySearch() not const |
| 656-CONST-N04 | Low | ⚠️40 | ⚠️58 | ✅60 | ✅70 | ❌70 | ⚠️50 | · | **CONFLICT** | GlobalHotkeys::globalShortcutKey(Action) not const — Q_INVOKABLE pure query |
| 657-CONST-N05 | Low | ⚠️40 | ⚠️58 | ✅65 | ✅70 | ❌65 | ⚠️50 | · | **CONFLICT** | Unnecessary copy via const auto instead of const auto& in extendLastMarker |
| 259-SAVE-N01 | Medium | ⚠️55 | ✅78 | ✅70 | ✅80 | ✅80 | ✅68 | · | split | loadFromNetworkFinihed sets m_fileUrl to phantom QTemporaryFile path |
| 076-SAVE-N02 | High | ⚠️50 | ✅84 | ✅75 | ✅80 | ✅85 | ✅68 | · | split | iOS save flow never updates C++ m_fileUrl — file URL perpetually stale |
| 182-SAVE-N03 | Medium | ✅55 | ✅78 | ✅75 | ✅80 | ✅85 | ✅55 | · | AGREE | saveAs() never updates _fileSystemWatcher — watches stale file after save-as |
| 623-SAVE-N04 | Low | ⚠️45 | ✅78 | ✅65 | ✅75 | ✅70 | ⚠️50 | · | split | save() unnecessary QString→std::string→QString round-trip through locale encoding |
| 373-SAVE-N05 | Low | ✅50 | ✅78 | ✅70 | ✅80 | ✅80 | ✅50 | · | AGREE | save() broken on Android content:// URIs — empty filename |
| 220-LOAD-N01 | Medium | ⚠️50 | ✅78 | ✅65 | ✅75 | ✅70 | ✅68 | · | split | TOCTOU race between QFile::exists() and file.open() in load() |
| 461-LOAD-N02 | Low | ⚠️50 | ✅78 | ❌75 | ✅75 | ❌75 | ✅68 | · | **CONFLICT** | reset() emits 12 NOTIFY signals when open() fails but exists() succeeds |
| 187-SHDR-N01 | Medium | ✅65 | ✅78 | ✅85 | ✅75 | ✅90 | ✅65 | · | AGREE | Math.cos/Math.sin used with degrees value — shadow offset diagonal instead of horizontal |
| 547-RAII-N01 | Medium | ⚠️50 | ✅78 | ✅60 | ✅80 | ✅85 | ⚠️50 | · | split | QDrag object never deleteLater'd after exec() — leaks on rejected drags |
| 437-RAII-N02 | Low | ⚠️50 | ⚠️58 | ✅55 | ✅75 | ✅80 | ✅68 | · | split | IosSaveDialog::m_tempDir created unconditionally on all platforms — wasted I/O |
| 351-RAII-N03 | Medium | ⚠️50 | ✅78 | ❌70 | ✅80 | ❌70 | ✅68 | · | **CONFLICT** | QProcess orphan — child process detached on waitForFinished() timeout |
| 617-Z-N01 | Medium | ⚠️45 | ✅78 | ⚠️45 | ⚠️60 | ❌65 | ⚠️50 | · | **CONFLICT** | CursorAutoHide has no explicit z — hover detection fragile against Kirigami internals |
| 478-Z-N02 | Low | ⚠️40 | ✅78 | ⚠️40 | ✅70 | ❌70 | ✅68 | · | **CONFLICT** | Two OverlaySheets have z:1 while nine others have none — inconsistent stacking |
| 488-Z-N03 | Low | ⚠️40 | ✅78 | ⚠️40 | ⚠️55 | ❌60 | ✅68 | · | **CONFLICT** | ComboBox Popup z:103 inside OverlaySheets with z:1 — disconnected layering |
| 684-Z-N04 | Low | ⚠️45 | ✅78 | ✅65 | ⚠️55 | ⚠️50 | ⚠️50 | · | split | PrompterBackground (z:0) renders above viewport.mouse (z:0) — latent input intercept |
| 381-TIME-N01 | Low | ✅60 | ✅78 | ✅85 | ✅70 | ✅90 | ✅60 | · | AGREE | copyrightYear computed then discarded — stale "2020-2026" in About after 2026 |
| 697-XFRM-N01 | Low | ❔45 | ❔39 | ⚠️45 | ⚠️60 | ✅85 | ❔45 | · | split | PrompterView.qml Rotation permanently overridden by PrompterPage.qml |
| 200-API-N01 | Medium | ⚠️50 | ✅78 | ✅65 | ✅75 | ✅80 | ✅68 | · | split | setAlignment() missing null-cursor guard — crash risk with no document |
| 107-API-N02 | Medium | ✅80 | ✅78 | ✅80 | ✅80 | ✅85 | ✅80 | · | AGREE | selectionIsLowerCase NOTIFY signal is wrong — fontCapitalizationChanged, never emitted for case changes |
| 201-API-N03 | Medium | ⚠️50 | ✅78 | ✅75 | ✅75 | ✅85 | ✅68 | · | split | CursorAutoHide.qml unconditionally dereferences pageStack.currentItem.prompter |
| 419-API-N04 | Low | ⚠️35 | ✅78 | ✅65 | ✅70 | ⚠️50 | ✅68 | · | split | setMarker(bool) misleadingly named — sets regular marker, not any marker |
| 388-API-N05 | Low | ⚠️50 | ✅78 | ✅70 | ✅70 | ✅70 | ✅68 | · | split | fileName()/fileType() return fabricated defaults — can't distinguish "no file" from "untitled.html" |
| 389-API-N06 | Low | ✅80 | ⚠️58 | ✅80 | ✅85 | ✅70 | ✅80 | · | split | SystemFontChooserDialog::show() calls setText() on same label twice — dead code |
| 390-API-N07 | Low | ✅55 | ✅78 | ✅75 | ⚠️65 | ✅90 | ✅55 | · | split | SpellChecker::encode() fallback says "Latin-1" but calls toLocal8Bit() |
| 717-ARC-01 |  | ⚠️35 | ⚠️48 | ❌50 | ⚠️55 | ✅60 | ⚠️50 | · | **CONFLICT** | Velocity physics engine entirely in QML (~20 readonly property bindings) |
| 718-ARC-02 |  | ⚠️35 | ⚠️48 | ❌50 | ⚠️55 | ✅60 | ⚠️50 | · | **CONFLICT** | Arc-03 Search/replace state machine fully in QML (50+ lines) |
| 719-ARC-03 |  | ⚠️35 | ⚠️48 | ❌50 | ⚠️55 | ✅60 | ⚠️50 | · | **CONFLICT** | OBS WebSocket v5 protocol in QML — opcode dispatch, auth, subscription |
| 720-ARC-04 |  | ⚠️40 | ⚠️48 | ❌50 | ⚠️55 | ✅60 | ⚠️50 | · | **CONFLICT** | DocumentHandler is 2295-line god class spanning file I/O, network, HTML filtering, markers, spellcheck, drag-drop, images, search, undo, clipboard, sleep prevention, font dialog |
| 721-ARC-05 |  | ⚠️35 | ⚠️48 | ❌50 | ⚠️55 | ✅60 | ⚠️50 | · | **CONFLICT** | Prompter.qml is 3139-line god component spanning velocity, state machine, keyboard, WebSocket, markers, spellcheck UI, file dialogs, WYSIWYG toggle, shadows |
| 722-ARC-06 |  | ⚠️35 | ⚠️48 | ❌50 | ⚠️50 | ✅60 | ⚠️50 | · | **CONFLICT** | qmlutil.hpp is utility grab-bag with 10+ unrelated functions |
| 561-KEY-N01 | Medium | ❔45 | ❔39 | ✅70 | ✅75 | ✅90 | ❔45 | · | split | Named marker key binding silently discards all modifier information |
| 341-CLI-N01 | Medium | ⚠️50 | ✅78 | ⚠️55 | ⚠️65 | ✅90 | ✅68 | · | split | --version flag non-functional — version string empty when parser processes |
| 122-DPR-N01 | Medium | ✅55 | ✅78 | ✅70 | ✅75 | ✅80 | ✅55 | · | AGREE | Prompter.qml uses Screen.devicePixelRatio (global) instead of screen.devicePixelRatio (window) |
| 260-SCALE-N01 | Medium | ⚠️50 | ✅78 | ✅65 | ✅75 | ✅80 | ✅68 | · | split | Right pointer xScale: -1 mirrors text pointers — backwards/unreadable text |
| 462-ORIENT-N01 | Low | ⚠️45 | ⚠️58 | ✅60 | ⚠️55 | ✅70 | ✅68 | · | split | TimerClock binary width>height orientation creates sharp 2x font jump at 1:1 |
| 452-BIND-N01 | Low | ⚠️50 | ✅92 | ✅65 | ⚠️55 | ❌70 | ✅68 | · | **CONFLICT** | contentWidth undefined for Shape/Image pointer types — transform origin silently wrong |
| 642-STR-CNV | Low | ⚠️45 | ✅78 | ✅60 | ✅75 | ❌60 | ⚠️50 | · | **CONFLICT** | 5 defensive validation gaps: toInt() without ok flag in getMarkerKey, parse(×2), setFontSize, and 32 hotkey reads |
| 077-SHADOW-N03 | High | ✅70 | ✅84 | ❌75 | ✅75 | ✅95 | ✅70 | · | **CONFLICT** | id: stopwatch shadows property bool stopwatch — timersEnabled always true |
| 472-SHADOW-N04 | Low | ⚠️50 | ✅78 | ✅65 | ⚠️60 | ❌65 | ✅68 | · | **CONFLICT** | id: frame shadows property bool frame — latent hazard |
| 037-LINK-N01 | High | ✅65 | ✅84 | ✅80 | ✅80 | ✅85 | ✅65 | · | AGREE | Qt::Network not linked on iOS static build — unresolved symbols |
| 038-LINK-N02 | High | ✅65 | ✅84 | ✅80 | ✅80 | ✅85 | ✅65 | · | AGREE | Qt::Network not linked on WASM static build — same as LINK-N01 |
| 219-LINK-N03 | Medium | ⚠️50 | ✅78 | ✅85 | ✅75 | ✅80 | ✅68 | · | split | Qt::WebSockets found as REQUIRED but never explicitly linked |
| 564-LINK-N04 | Medium | ❔45 | ✅78 | ❌85 | ✅75 | ✅75 | ❔45 | · | **CONFLICT** | KF6::GlobalAccel find_package/link mismatch on Haiku |
| 357-COMP-N01 | Low | ✅55 | ✅92 | ✅95 | ✅75 | ✅80 | ✅55 | · | AGREE | Case-sensitive duplicate detection in setLanguages() |
| 116-COMP-N02 | Medium | ✅50 | ✅78 | ✅90 | ✅80 | ✅85 | ✅50 | · | AGREE | Case-sensitive suffix check misses mixed-case extensions — silent format loss |
| 628-COMP-N03 | Low | ⚠️50 | ✅78 | ✅95 | ⚠️60 | ✅70 | ⚠️50 | · | split | regularMarker() same double-textCursor anti-pattern as LOG-07 |
| 562-LBL-N01 | Medium | ⚠️45 | ⚠️58 | ✅70 | ✅70 | ✅90 | ⚠️50 | · | split | All 12 Sliders in EditorToolbar missing Layout.fillWidth: true — cramped |
| 563-LBL-N02 | Medium | ⚠️40 | ⚠️52 | ✅80 | ✅70 | ✅80 | ❌72 | · | **CONFLICT** | 11 Labels with Layout.bottomMargin: -14 — undefined behavior, overlap risk |
| 460-LBL-N03 | Low | ⚠️40 | ⚠️58 | ✅85 | ⚠️55 | ✅70 | ✅68 | · | split | PrompterView 3× height overflow in theforce debug mode |
| 665-LAY-N01 | Low | ⚠️45 | ⚠️58 | ❔50 | ✅70 | ✅80 | ⚠️50 | · | split | 10 Labels with Layout.margins but inside MouseArea, not direct layout child — dead |
| 666-LAY-N02 | Low | ⚠️40 | ⚠️58 | ❔50 | ✅70 | ✅80 | ⚠️50 | · | split | WheelSettingsOverlay explanation text constrained to single column in 2-column GridLayout |
| 207-DLG-N10 | Medium | ⚠️45 | ✅78 | ✅90 | ✅75 | ✅85 | ✅68 | · | split | TimerClock ColorDialog selectedColor never initialized from persisted settings |
| 398-DLG-N11 | Low | ⚠️45 | ✅78 | ✅90 | ✅75 | ✅70 | ✅68 | · | split | PrompterPage ColorDialogs — dead acceptedColor property binding |
| 570-QPROP-N02 | Medium | ❌50 | ❌76 | ✅95 | ✅75 | ✅80 | ❌50 | · | **CONFLICT** | comesFromNetwork Q_PROPERTY missing WRITE clause |
| 233-PATH-N01 | Medium | ⚠️50 | ✅78 | ✅85 | ✅80 | ✅80 | ✅68 | · | split | save() fragile percent-encoding round-trip — broken for UNC paths |
| 154-PATH-N02 | Medium | ✅60 | ✅78 | ✅95 | ✅80 | ✅85 | ✅60 | · | AGREE | reload() constructs file:// URL via raw string concat — #/? in filenames break URL |
| 148-MOB-01 | Medium | ✅70 | ✅92 | ✅80 | ✅80 | ✅90 | ✅70 | · | AGREE | Android: projectionManager undefined — 3 unguarded reference sites |
| 227-MOB-02 | Medium | ⚠️50 | ✅78 | ✅95 | ✅80 | ✅80 | ✅68 | · | split | No +ios/ QML selector — iOS inherits base main.qml with desktop-only components |
| 228-MOB-03 | Medium | ⚠️50 | ✅92 | ✅95 | ✅75 | ✅85 | ✅68 | · | split | iOS: IosSaveDialog silently hangs QML caller when temp dir invalid |
| 364-MOB-04 | Low | ✅65 | ✅78 | ✅95 | ✅75 | ✅90 | ✅65 | · | AGREE | Android: restartApplication() quits without restart |
| 365-MOB-05 | Low | ✅85 | ✅78 | ✅95 | ✅80 | ✅85 | ✅85 | · | AGREE | Android: Missing INTERNET permission in manifest |
| 366-MOB-06 | Low | ✅60 | ✅78 | ✅85 | ✅75 | ✅80 | ✅60 | · | AGREE | Android: PrompterPage display delegate Component.onCompleted references projectionManager — startup TypeError |
| 225-MENU-N01 | Medium | ✅55 | ⚠️58 | ✅95 | ✅75 | ✅75 | ✅55 | · | split | contextMenu.popup(this) missing click coordinates — menu at wrong position |
| 226-MENU-N02 | Medium | ✅60 | ⚠️58 | ✅95 | ✅80 | ✅90 | ✅60 | · | split | Mobile "Add to dictionary" missing %1 placeholder — word never shown |
| 305-MENU-N03 | Medium | ⚠️55 | ⚠️58 | ✅95 | ✅75 | ✅85 | ✅68 | · | split | Text alignment menu RTL swap: labels swap but actions don't |
| 406-MENU-N04 | Low | ✅50 | ⚠️58 | ✅75 | ✅70 | ✅70 | ✅50 | · | split | Trailing empty MenuSeparator at end of mobile context menu |
| 429-MENU-N05 | Low | ⚠️45 | ⚠️58 | ✅95 | ✅70 | ✅70 | ✅68 | · | split | "Redo" context menu item missing & accelerator |
| 483-MENU-N06 | Low | ⚠️50 | ⚠️58 | ⚠️70 | ⚠️60 | ✅85 | ✅68 | · | split | Paste behavior inconsistent between context menu and global Edit menu |
| 206-DBG-N01 | Medium | ✅60 | ⚠️58 | ✅95 | ✅75 | ✅90 | ✅60 | · | split | OBS WebSocket auth challenge+salt logged to console in release builds |
| 393-DBG-N02 | Low | ✅55 | ⚠️58 | ✅95 | ✅70 | ✅80 | ✅55 | · | split | Velocity debug logging active in production |
| 489-DBG-N03 | Low | ⚠️45 | ⚠️52 | ⚠️60 | ⚠️60 | ❌60 | ✅68 | · | **CONFLICT** | Latent debug state leak: pointers/debug Setting persists Guides checkbox |
| 394-DBG-N04 | Low | ✅60 | ⚠️58 | ✅90 | ✅70 | ✅80 | ✅60 | · | split | qDebug() in namedMarker()/setMarker() active in release |
| 450-WARN-N01 | Low | ⚠️40 | ⚠️58 | ✅80 | ✅75 | ✅70 | ✅68 | · | split | SpellHighlighter::isEnabled() — dead code, never called |
| 415-WARN-N02 | Low | ✅60 | ⚠️58 | ✅85 | ✅75 | ✅70 | ✅60 | · | split | SpellChecker::addWord() — dead public API, never called |
| 647-WARN-N03 | Low | ⚠️45 | ⚠️58 | ✅90 | ✅70 | ✅70 | ⚠️50 | · | split | quint64→int implicit narrowing in nextMarker()/previousMarker() |
| 416-WARN-N04 | Low | ✅55 | ⚠️58 | ✅95 | ✅70 | ✅70 | ✅55 | · | split | QProcess::startDetached() bool return silently ignored |
| 133-FLOW-N01 | Medium | ✅65 | ✅78 | ✅90 | ✅80 | ✅90 | ✅65 | · | AGREE | setKeyMarker() calls setAnchor("#") — const char*→bool conversion, href never set |
| 556-FLOW-N02 | Medium | ❔45 | ⚠️58 | ✅90 | ✅75 | ✅85 | ❔45 | · | split | increaseVelocity()/decreaseVelocity() skip velocity change when paused |
| 552-DEF-N01 | Medium | ❌65 | ❌76 | ✅90 | ✅75 | ✅75 | ❌65 | · | **CONFLICT** | Flickable.flicking undefined in Qt 6 — wrong cursor during momentum scroll |
| 290-DEF-N02 | Medium | ⚠️50 | ⚠️58 | ✅95 | ✅75 | ✅75 | ✅68 | · | split | DropArea internalDrag always false — internal drag handler dead code |
| 328-TMR-N01 | Medium | ⚠️50 | ⚠️58 | ✅95 | ✅75 | ✅85 | ✅68 | · | split | resetBackground Timer not stopped when new background loaded — race erases new image |
| 329-TMR-N02 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅80 | ✅85 | ✅68 | · | split | Windows onFrameSwapped missing qmlutil.r(p) — per-frame grab result leak |
| 356-CMAKE-N05 | Low | ✅55 | ✅78 | ✅85 | ✅75 | ✅80 | ✅55 | · | AGREE | foreach(file IN LISTS icon_files doc) — "doc" never defined |
| 484-PRE-N01 | Low | ⚠️55 | ⚠️58 | ⚠️75 | ❌80 | ✅85 | ✅68 | · | **CONFLICT** | Preprocessor uses `or` instead of `\|\|` in 6 #if directives — MSVC build break |
| 453-CNTD-N01 | Low | ⚠️50 | ⚠️58 | ✅85 | ⚠️60 | ✅75 | ✅68 | · | split | Countdown Running: dissolveIn and dissolveOut compete for same opacity when __iterations===__disappearWithin===1 |
| 433-QF-N02 | Low | ⚠️45 | ⚠️58 | ✅85 | ✅70 | ✅70 | ✅68 | · | split | QDir::entryList missing QDir::Readable in availableDictionaries() |
| 434-QF-N03 | Low | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅75 | ✅68 | · | split | TOCTOU: QFile::exists() → QFile::copy() in resource cache extraction |
| 499-TXT-CRIT | Critical | ❔45 | ❔39 | ✅85 | ✅80 | ✅95 | ❔45 | · | split | Plain 'v'/'V' keypress silently consumed — letter 'v' cannot be typed |
| 196-TXT-N03 | Medium | ✅80 | ✅78 | ✅90 | ✅80 | ✅90 | ✅80 | · | AGREE | Toolbar paste and Edit menu paste bypass HTML sanitization |
| 332-TXT-N04 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅75 | ✅80 | ✅68 | · | split | goToNextMarker() temporarily sets cursorPosition=-1 — corrupts cursor state |
| 634-INT-N01 | Low | ⚠️45 | ⚠️58 | ✅90 | ✅70 | ✅70 | ⚠️50 | · | split | quint64→int narrowing at DocumentHandler→MarkersModel boundary (4 sites) |
| 560-INT-N02 | Medium | ⚠️40 | ✅78 | ✅90 | ⚠️60 | ✅85 | ⚠️50 | · | split | replaceAll() returns long — 32-bit overflow on Windows x64 |
| 635-INT-N03 | Low | ⚠️40 | ⚠️58 | ✅80 | ✅70 | ✅70 | ⚠️50 | · | split | 6 qsizetype→int narrowing conversions across models and loops |
| 272-URL-N03 | Medium | ✅55 | ⚠️58 | ✅90 | ✅80 | ✅80 | ✅55 | · | split | Network-loaded HTML lacks base URL — relative resources broken |
| 414-URL-N04 | Low | ✅60 | ⚠️58 | ✅90 | ✅75 | ✅85 | ✅60 | · | split | loadFromNetwork() validates wrong URL instance |
| 273-URL-N05 | Medium | ✅55 | ⚠️58 | ✅90 | ✅80 | ✅85 | ✅55 | · | split | openFromRemote() blindly prepends http:// to non-HTTP schemes |
| 566-PERF-N01 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅75 | ⚠️50 | · | split | onFrameSwapped calls markerCompare() unconditionally — wasted JS call every frame |
| 307-PERF-N02 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅80 | ✅68 | · | split | RecentDocuments._load() blocks startup with N synchronous createObject() calls |
| 669-PERF-N03 | Low | ⚠️50 | ⚠️58 | ✅85 | ⚠️60 | ✅75 | ⚠️50 | · | split | velocityDragOverlay hot-loop calls velocity functions without throttling |
| 125-ERR-N01 | Medium | ✅60 | ✅78 | ✅90 | ✅75 | ✅80 | ✅60 | · | AGREE | removeCustomWord() silently drops dictionary languages on partial reload failure |
| 291-ERR-N02 | Medium | ⚠️55 | ⚠️58 | ✅95 | ✅75 | ✅80 | ✅68 | · | split | insertImageAt() async callback silently discards 3 failure modes |
| 524-PATH-N03 | High | ❔45 | ✅84 | ✅90 | ✅75 | ⚠️65 | ❔45 | · | split | Wrong ../fonts/ depth in +android and +windows FontLoader paths |
| 624-SIG-N03 | Low | ⚠️40 | ✅78 | ✅75 | ✅70 | ✅70 | ⚠️50 | · | split | MessageDialog.onButtonClicked declares unused second parameter role |
| 621-QOBJ-N01 | Low | ⚠️40 | ✅78 | ✅85 | ✅70 | ✅60 | ⚠️50 | · | split | QmlUtil missing constructor with parent parameter |
| 323-TAB-N01 | Medium | ⚠️50 | ✅78 | ⚠️60 | ✅75 | ✅80 | ✅68 | · | split | PointerSettings TabButton onClicked skips currentIndex assignment |
| 527-REGEX-CRIT-01 | High | ❔45 | ❔39 | ✅85 | ✅80 | ✅90 | ❔45 | · | split | regex_4 destroys <body> tag — removes opening tag instead of color attributes |
| 060-REGEX-CRIT-02 | High | ✅55 | ✅84 | ✅95 | ✅85 | ✅90 | ✅55 | · | AGREE | searchRegEx.setPattern() from user input — isValid() never called |
| 255-REGEX-N04 | Medium | ⚠️50 | ✅78 | ✅90 | ✅80 | ✅85 | ✅68 | · | split | ReDoS — user-supplied regex has no length limit, timeout, or backtracking guard |
| 372-REGEX-N05 | Low | ✅70 | ✅78 | ✅85 | ✅70 | ✅80 | ✅70 | · | AGREE | regex_0 and regex_3 use . (any-char) instead of \. (literal dot) in decimal matching |
| 181-REGEX-N06 | Medium | ✅55 | ✅78 | ✅90 | ✅75 | ✅85 | ✅55 | · | AGREE | imgSrcRegex captures wrong src when data-src follows real src |
| 645-VCI-N01 | Low | ⚠️40 | ⚠️48 | ✅95 | ✅70 | ✅70 | ⚠️50 | · | split | At-end action buttons use inconsistent font scaling (1/1.5 vs 1/1.75) in same group |
| 646-VCI-N02 | Low | ⚠️40 | ⚠️48 | ✅95 | ✅70 | ✅70 | ⚠️50 | · | split | upperControls and bottomControls fade to different opacity levels during Prompting |
| 486-VCI-N03 | Low | ⚠️40 | ⚠️48 | ⚠️70 | ⚠️55 | ✅90 | ✅68 | · | split | Hardcoded divider/separator/border colors (#292929, #606060, #808080) break theme adaptation |
| 274-UTF-N01 | Medium | ⚠️50 | ✅78 | ✅90 | ✅75 | ✅90 | ✅68 | · | split | text.truncate(64) can split UTF-16 surrogate pairs — corrupted display |
| 495-AND-CRIT-01 | Critical | ✅85 | ✅84 | ✅95 | ✅85 | ✅95 | ✅85 | · | AGREE | Missing android.permission.INTERNET — all network silently fails |
| 080-AND-HIGH-01 | High | ⚠️50 | ⚠️58 | ✅80 | ✅80 | ✅80 | ✅68 | · | split | Android back button doesn't dismiss overlays/drawers before close |
| 020-AND-HIGH-02 | High | ✅60 | ✅84 | ✅90 | ✅80 | ✅90 | ✅60 | · | AGREE | Android screen never sleeps after prompter use |
| 021-AND-HIGH-03 | High | ✅65 | ✅84 | ✅95 | ✅80 | ✅95 | ✅65 | · | AGREE | factoryReset() quits Android app without restarting |
| 277-AND-MED-01 | Medium | ⚠️45 | ⚠️58 | ✅95 | ✅75 | ✅95 | ✅68 | · | split | Missing intent-filter for opening files from other apps |
| 282-CLP-N01 | Medium | ⚠️50 | ✅78 | ⚠️70 | ✅75 | ✅85 | ✅68 | · | split | Copy/Cut exports unfiltered HTML to system clipboard |
| 283-CLP-N02 | Medium | ⚠️50 | ⚠️58 | ✅95 | ✅75 | ✅90 | ✅68 | · | split | DropArea external drop never calls drop.accept() |
| 284-CLP-N03 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅90 | ✅68 | · | split | DropArea external drop: URLs consumed preferentially — text silently lost |
| 194-SWT-N01 | Medium | ✅60 | ✅78 | ✅95 | ✅75 | ✅90 | ✅60 | · | AGREE | OBS WebSocket Switch checked binding broken on first toggle |
| 585-IMH-SYS | Medium | ⚠️40 | ⚠️58 | ⚠️65 | ✅75 | ✅95 | ❌72 | · | **CONFLICT** | Systemic absence of inputMethodHints on ALL TextFields (16 sites) |
| 661-EKA-SYS | Low | ⚠️40 | ⚠️58 | ⚠️65 | ✅70 | ✅90 | ❌72 | · | **CONFLICT** | Systemic absence of EnterKeyAction on ALL TextFields (7 sites) |
| 338-WINDOW-N01 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅75 | ✅85 | ✅68 | · | split | Projection windows not closed on main window close — orphaned on Linux |
| 296-GSW-N01 | Medium | ⚠️45 | ⚠️58 | ✅90 | ✅70 | ✅80 | ✅68 | · | split | MarkersDrawer SwipeListItem navigates on swipe — gesture conflict on touch |
| 663-GSW-N02 | Low | ❔45 | ❔39 | ✅85 | ⚠️60 | ✅80 | ❔45 | · | split | Flickable onDragStarted uses stale __iBackup after non-prompting drags |
| 428-LVW-N01 | Low | ⚠️45 | ⚠️58 | ✅85 | ✅70 | ✅70 | ✅68 | · | split | InputsOverlay.qml ListView currentIndex: PointerSettings.States.Arrow — copy-paste error |
| 430-META-N01 | Low | ⚠️45 | ⚠️58 | ✅95 | ✅70 | ✅75 | ✅68 | · | split | QMetaObject::invokeMethod return value unchecked — silent failure on WASM |
| 636-LOG-N04 | Low | ❌70 | ✅78 | ✅90 | ✅70 | ❌90 | ❌70 | · | **CONFLICT** | qWarning("reloading") fires unconditionally — misleading when URL mismatches |
| 303-LOG-N05 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅80 | ✅68 | · | split | Q_UNREACHABLE() in m_setGlobalShortcut() — UB in release on new enum value |
| 143-LOG-N06 | Medium | ✅70 | ✅78 | ✅95 | ✅75 | ✅90 | ✅70 | · | AGREE | No error log when saveAs() write/flush fail — silent data loss |
| 223-LOG-N07 | Medium | ✅55 | ⚠️58 | ✅95 | ✅75 | ✅90 | ✅55 | · | split | No error log in loadFromNetworkFinihed() — silent bad-data load |
| 557-FONT-N01 | Medium | ⚠️45 | ❔39 | ✅95 | ✅75 | ✅70 | ❌72 | · | **CONFLICT** | font.family: "Monospace" never resolves — no such font on any OS |
| 400-FONT-N02 | Low | ✅65 | ⚠️58 | ✅95 | ✅70 | ✅90 | ✅65 | · | split | FontLoader id typo: westernSeriousSansfFont — stray 'f' in "Sans" |
| 198-XML-N01 | Medium | ✅55 | ✅92 | ✅90 | ✅75 | ✅90 | ✅55 | · | AGREE | android:background="#303030" invalid on \<activity\> — silently ignored |
| 355-CMAKE-N02 | Low | ✅55 | ✅78 | ✅95 | ✅70 | ✅90 | ✅55 | · | AGREE | INTERFACE_LINK_LIBRARIES on executable target — no-op |
| 285-CMAKE-N03 | Medium | ⚠️50 | ❌76 | ✅85 | ✅75 | ✅80 | ✅68 | · | **CONFLICT** | qt_wrap_ui conflicts with global AUTOUIC — double UI processing |
| 110-CMAKE-N04 | Medium | ✅55 | ✅78 | ✅90 | ✅75 | ✅90 | ✅55 | · | AGREE | Relative ../build path in install rules — out-of-tree build failure |
| 576-SETUP-N01 | Medium | ❔40 | ❔39 | ✅95 | ✅75 | ✅90 | ❔40 | · | split | setup.sh uses windeployqt.exe (Qt 5) — should be windeployqt6.exe (Qt 6) |
| 308-POP-N01 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅90 | ✅68 | · | split | ESC cascade missing dictionariesSheet — undismissable by keyboard |
| 309-POP-N02 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅90 | ✅68 | · | split | ESC cascade missing customWordsSheet — undismissable by keyboard |
| 310-POP-N03 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅75 | ✅90 | ✅68 | · | split | ESC cascade missing obsConfiguration — undismissable by keyboard despite alias |
| 235-POP-N04 | Medium | ✅65 | ⚠️58 | ✅95 | ✅75 | ✅90 | ✅65 | · | split | CountdownConfiguration SpinBoxes use focus: true (JS label) instead of focus = true |
| 471-RND-N01 | Low | ⚠️50 | ⚠️58 | ✅95 | ✅70 | ❌70 | ✅68 | · | **CONFLICT** | forceQtTextRenderer dead on Apple platforms — unconditionally uses NativeRendering |
| 440-RND-N02 | Low | ⚠️45 | ⚠️58 | ✅85 | ✅70 | ✅85 | ✅68 | · | split | Missing smooth: true on background Image — aliased upscale |
| 441-RND-N03 | Low | ⚠️50 | ⚠️58 | ✅85 | ✅70 | ✅80 | ✅68 | · | split | Missing smooth: true on projection Image — aliased text on external displays |
| 261-ST-N02 | Medium | ✅50 | ⚠️58 | ✅95 | ✅70 | ✅85 | ✅50 | · | split | Dead overlay.state PropertyChanges — overlay has no states array |
| 281-CFG-N01 | Medium | ⚠️50 | ⚠️58 | ✅95 | ✅70 | ✅80 | ✅68 | · | split | Desktop MimeType incomplete — only text/html, missing text/plain and text/markdown |
| 420-CFG-N02 | Low | ✅55 | ⚠️58 | ❔40 | ✅70 | ✅95 | ✅55 | · | split | v1.1.3 release date "2022-1-16" breaks chronological order — should be 2023-01-16 |
| 391-CFG-N03 | Low | ✅60 | ⚠️58 | ✅95 | ✅70 | ✅95 | ✅60 | · | split | "fixedd" typo in v2.0.2 release description |
| 604-TP-SYS | Medium | ⚠️40 | ⚠️58 | ⚠️70 | ✅70 | ✅75 | ⚠️50 | · | split | Systemic absence of ToolTip on ~60+ controls across entire application |
| 331-TP-N01 | Medium | ⚠️55 | ⚠️58 | ✅90 | ✅70 | ✅80 | ✅68 | · | split | "Error loading file..." used as document content, not placeholderText |
| 275-WATCH-N01 | Medium | ⚠️50 | ✅78 | ✅95 | ✅70 | ✅80 | ✅68 | · | split | addPath() return never checked — silent watch failure |
| 276-WATCH-N02 | Medium | ⚠️50 | ✅78 | ✅90 | ✅70 | ✅80 | ✅68 | · | split | removePath() return never checked — stale path causes double-watch |
| 549-WATCH-N03 | Medium | ❔45 | ✅78 | ✅90 | ✅75 | ✅70 | ❔45 | · | split | Watcher not refreshed after fileChanged — stale inotify on Linux atomic saves |
| 417-WATCH-N04 | Low | ⚠️45 | ✅78 | ✅85 | ✅70 | ✅85 | ✅68 | · | split | unblockFileWatcher() dereferences _fileSystemWatcher without null guard |
| 149-MODEL-N01 | Medium | ✅60 | ✅78 | ✅90 | ✅75 | ✅80 | ✅60 | · | AGREE | MarkersModel::rowCount ignores parent.isValid() — returns full size for child probe |
| 407-MODEL-N02 | Low | ✅55 | ⚠️58 | ✅85 | ✅70 | ✅85 | ✅55 | · | split | SessionModel::clearDataPoints lacks empty-model guard before beginRemoveRows |
| 513-COERC-N01 | High | ❔45 | ✅84 | ❌85 | ✅75 | ✅90 | ❔45 | · | **CONFLICT** | parseInt("") → NaN state bootstrap — first toggle() bricks state machine |
| 115-COERC-N02 | Medium | ✅55 | ✅78 | ✅95 | ✅75 | ✅85 | ✅55 | · | AGREE | Unvalidated string-to-number injects NaN into root.__opacity — all opacity dead |
| 421-COERC-N03 | Low | ⚠️50 | ⚠️58 | ✅80 | ✅70 | ✅80 | ✅68 | · | split | real→int truncation in WindowDragger position compounds drift |
| 237-QLOAD-N01 | Medium | ⚠️50 | ✅78 | ✅95 | ✅75 | ✅85 | ✅68 | · | split | InputsOverlay toggleButtonsOff() null-check bypass — crash on slow async Loaders |
| 659-DETACH-N01 | Low | ⚠️40 | ⚠️58 | ✅75 | ✅70 | ❌60 | ⚠️50 | · | **CONFLICT** | 4 non-const operator[] on QList in keySearch() — unnecessary implicit sharing detach |
| 514-COLOR-CRIT-01 | High | ❔45 | ❔39 | ✅95 | ✅80 | ✅90 | ❌72 | · | **CONFLICT** | selectionColor #333d9ef3 — alpha channel reversed (#AARRGGBB vs #RRGGBBAA), selection invisible |
| 705-SYM-N01 | Low-Medium | ⚠️40 | ⚠️58 | ✅85 | ⚠️55 | ✅65 | ⚠️50 | · | split | 6 RTL/symmetry issues across PointerSettings, Find, PrompterView, Prompter, PrompterPage |
| 496-CLIP-CRIT-01 | Critical | ✅85 | ✅84 | ✅95 | ✅80 | ✅90 | ✅85 | · | AGREE | Paste via toolbar button and File menu bypasses HTML sanitization |
| 204-CLIP-N04 | Medium | ✅65 | ⚠️58 | ✅90 | ✅75 | ✅80 | ✅65 | · | split | Image-only clipboard paste — button enabled but does nothing |
| 214-INT-N04 | Medium | ✅55 | ⚠️58 | ✅85 | ✅75 | ✅85 | ✅55 | · | split | OBS URL/Password fields disabled when WebSocket enabled — inverted logic |
| 215-INT-N05 | Medium | ✅55 | ⚠️58 | ✅90 | ✅75 | ✅85 | ✅55 | · | split | PropertyChanges permanently destroys CheckBox checked bindings on PointerSettings tab switch |
| 134-FMT-N01 | Medium | ✅50 | ✅78 | ✅95 | ✅75 | ✅85 | ✅50 | · | AGREE | Step Speed onAccepted displays 100x correct value |
| 135-FMT-N02 | Medium | ✅50 | ✅78 | ✅95 | ✅75 | ✅85 | ✅50 | · | AGREE | Step Acceleration onAccepted — identical 100x display bug |
| 156-PLAT-N04 | Medium | ✅65 | ✅78 | ✅90 | ✅75 | ✅90 | ✅65 | · | AGREE | "ipados" is not valid Qt.platform.os string — 18 dead guards across 5 files |
| 432-PLAT-N05 | Low | ⚠️45 | ⚠️58 | ✅85 | ✅70 | ✅75 | ✅68 | · | split | Base main.qml fullScreenPlatform missing "wasm" (inconsistent with +windows) |
| 197-WYS-N01 | Medium | ✅60 | ✅78 | ✅90 | ✅75 | ✅85 | ✅60 | · | AGREE | Internal drag-and-drop copy inserts HTML as plain text — tags become visible |
| 418-WYS-N02 | Low | ✅70 | ⚠️58 | ✅85 | ✅70 | ✅95 | ✅70 | · | split | Default stylesheet CSS errors: valign:top (not a CSS property) and border:1pt (missing style) |
| 070-QP-N01 | High | ✅65 | ⚠️58 | ✅95 | ✅80 | ✅95 | ✅65 | · | split | restartApplication() quits even when startDetached fails — app dies with no replacement |
| 158-QP-N02 | Medium | ✅65 | ✅78 | ✅90 | ✅75 | ✅95 | ✅65 | · | AGREE | convert.waitForFinished() blocks GUI thread up to 30s during LibreOffice import |
| 159-QP-N03 | Medium | ✅55 | ✅78 | ✅90 | ✅75 | ✅90 | ✅55 | · | AGREE | convert.exitCode() never checked — LibreOffice error output becomes document content |
| 033-IMG-N02 | High | ✅60 | ✅84 | ✅90 | ✅80 | ✅95 | ✅60 | · | AGREE | insertHtmlAt() silent blocking HTTP load for img src URLs — UI freeze |
| 383-TRN-N01 | Low | ✅55 | ✅78 | ✅90 | ✅70 | ✅95 | ✅55 | · | AGREE | Dead ternary: both branches return Qt.OpenHandCursor |
| 550-A11Y-SYS | Medium | ⚠️45 | ⚠️58 | ✅85 | ✅70 | ✅90 | ⚠️50 | · | split | Systemic absence of Accessible properties — app invisible to screen readers |
| 518-EVT-N13 | High | ❔45 | ⚠️58 | ✅95 | ✅75 | ✅90 | ❔45 | · | split | rewind()/fastForward() event undefined — winding state permanently locked after first use |
| 279-ANM-N02 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅70 | ✅85 | ✅68 | · | split | Standby→Ready countdown opacity flash — PropertyChanges opacity:1 conflicts with dissolveIn |
| 315-RESO-N01 | Medium | ⚠️45 | ⚠️48 | ✅95 | ✅70 | ✅90 | ✅68 | · | split | Editing font size not viewport-scaled — text nearly unreadable on 4K |
| 438-RESO-N02 | Low | ⚠️40 | ⚠️48 | ✅80 | ✅65 | ✅80 | ✅68 | · | split | Scrollbar width 6dp-13dp — below minimum 44dp touch target |
| 674-RESO-N03 | Low | ⚠️40 | ⚠️48 | ✅75 | ⚠️55 | ✅70 | ⚠️50 | · | split | Control spacing hardcoded 8dp — cramped on large displays |
| 675-RESO-N04 | Low | ⚠️40 | ⚠️48 | ✅75 | ⚠️55 | ✅70 | ⚠️50 | · | split | Projection-window margins fixed 10dp/5dp — near-flush on large screens |
| 439-RESO-N05 | Low | ⚠️40 | ⚠️48 | ✅75 | ✅65 | ✅70 | ✅68 | · | split | PointerSettings ListView height hardcoded 180dp — doesn't fill available space |
| 469-RESO-N06 | Low | ⚠️40 | ⚠️48 | ✅80 | ⚠️55 | ✅70 | ✅68 | · | split | ReadRegionOverlay pointer margin 3dp — overlap with text at large fonts |
| 011-STK-N01 | Critical | ✅85 | ✅92 | ✅95 | ✅80 | ✅95 | ✅85 | · | AGREE | Android projectionManager undefined — crash on "Performance tweaks" submenu |
| 036-JSON-N01 | High | ✅65 | ✅84 | ✅95 | ✅80 | ✅95 | ✅65 | · | AGREE | OBS WebSocket Hello auth fields accessed without null guard — crash on auth-disabled |
| 312-QW-N01 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅85 | ✅68 | · | split | Projection Window onClosing references cleared model — spurious runtime errors |
| 313-QW-N02 | Medium | ⚠️55 | ⚠️58 | ✅85 | ✅75 | ✅85 | ✅68 | · | split | Stale QScreen reference in projection model — dangling after monitor hot-unplug |
| 403-JS-N01 | Low | ✅50 | ⚠️58 | ✅70 | ✅65 | ✅90 | ✅50 | · | split | TIMERCLOCK getTimeString() — redundant .toString() on already-string — 54 allocs/sec |
| 300-JS-N02 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅75 | ✅90 | ✅68 | · | split | markerCompare() per-frame JSON.stringify() over OBS marker — 60 allocs/sec |
| 093-THM-SYS | High | ⚠️55 | ⚠️58 | ✅90 | ✅70 | ✅85 | ✅68 | · | split | Complete theme deadlock — 50+ Material.theme: Dark hardcoded, theme toggle commented out |
| 298-HSCROLL-N01 | Medium | ⚠️50 | ⚠️58 | ✅95 | ✅70 | ✅90 | ✅68 | · | split | InputsOverlay Flickables use contentWidth: width instead of implicitWidth — horizontal overflow clipped |
| 299-HSCROLL-N02 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅70 | ✅80 | ✅68 | · | split | Inner Flickables missing flickableDirection: VerticalFlick — conflict with parent horizontal ListView |
| 288-COLOR-N08 | Medium | ⚠️45 | ⚠️58 | ✅90 | ✅70 | ✅85 | ✅68 | · | split | textBackground() returns invalid QColor for body/paragraph text |
| 289-COLOR-N09 | Medium | ⚠️55 | ⚠️58 | ✅90 | ✅70 | ✅85 | ✅68 | · | split | acceptedColor binds transparent QColor on startup — initial text invisible |
| 236-PP-N01 | Medium | ✅55 | ⚠️58 | ✅95 | ✅75 | ✅95 | ✅55 | · | split | Q_OS_APPLE is not a Qt macro — KGlobalAccel block compiles on all Unix including macOS |
| 094-TRF-N01 | High | ⚠️50 | ⚠️58 | ✅95 | ✅75 | ✅90 | ✅68 | · | split | rightWidthAdjustmentBar drag.maximumX formula broken — drag collapses to single point |
| 330-TOG-N01 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅70 | ✅80 | ✅68 | · | split | WheelSettingsOverlay useScrollAsDialButton — cross-path stale checked state |
| 599-RPL-N01 | Medium | ❌55 | ❌76 | ✅95 | ✅70 | ❌90 | ❌55 | · | **CONFLICT** | 6 additional files missing QtQuick.Controls.Material import — ~65 controls unthemed |
| 449-VIS-FB-N01 | Low | ⚠️50 | ⚠️58 | ✅90 | ✅70 | ✅90 | ✅68 | · | split | bookmarkListButton and searchButton missing checkable: true — no checked background |
| 023-DEB-N01 | High | ✅55 | ✅84 | ✅95 | ✅75 | ✅90 | ✅55 | · | AGREE | libvulkan-dev (dev package) listed as Debian runtime dependency |
| 515-DEB-N02 | High | ❔45 | ✅84 | ✅95 | ✅80 | ❌90 | ❔45 | · | **CONFLICT** | qml6-module-qtcore is not a real Debian package — .deb uninstallable |
| 516-DEB-N03 | High | ❔45 | ✅84 | ✅95 | ✅80 | ❌85 | ❔45 | · | **CONFLICT** | qml6-module-qt-labs-platform doesn't exist for Qt 6 — .deb uninstallable |
| 258-RPM-N01 | Medium | ✅50 | ⚠️58 | ✅90 | ✅75 | ✅95 | ✅50 | · | split | RPM dependencies entirely commented out — zero automatic dependency resolution |
| 616-TS-N07 | Medium | ❔40 | ❔39 | ❔40 | ❔50 | ✅95 | ❔40 | · | split | Wrong translations: Chinese "Undo"→"Open", "Bars"→"Toolbar"; French "Pointer Configuration"→"Prompter duration"; Korean "Line width"→"Line height" |
| 611-META-N14 | Medium | ❔45 | ⚠️58 | ✅80 | ⚠️60 | ❔60 | ❔45 | · | split | ModernToolkit removed from AppStream spec — validation error |
| 306-META-N15 | Medium | ⚠️45 | ⚠️58 | ✅90 | ✅70 | ✅80 | ✅68 | · | split | No StartupWMClass in desktop file — duplicate dock entries, missing icon |
| 667-META-N16 | Low | ❔45 | ❔39 | ✅90 | ⚠️60 | ✅95 | ❔45 | · | split | README badges and links reference wrong repo Cuperino/QPrompt (should be QPrompt-Teleprompter) |
| 565-META-N17 | Medium | ❔45 | ❔39 | ✅85 | ✅70 | ✅95 | ❔45 | · | split | README links to non-existent BUILD.md |
| 105-AND-N08 | Medium | ✅60 | ✅78 | ✅95 | ✅75 | ✅95 | ✅60 | · | AGREE | Android saveAs() hardcodes isHtml=true — plain-text files saved with HTML markup |
| 538-TMR-N05 | High | ❔45 | ❔39 | ✅90 | ✅75 | ⚠️70 | ❔45 | · | split | markerCompare() only fires on forward scroll — backward scroll + re-forward misses marker |
| 264-TMR-N06 | Medium | ⚠️50 | ✅78 | ✅90 | ✅70 | ✅85 | ✅68 | · | split | Auto-reload Timer persists after network dialog close — background refetches |
| 522-FONT-METRIC-01 | High | ❔40 | ❔39 | ✅90 | ✅75 | ✅75 | ❔40 | · | split | pixelSize used as line-height proxy — core scroll timing off by ~57% |
| 294-FONT-METRIC-02 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅70 | ✅90 | ✅68 | · | split | FontLoader status never checked — font substitution silently fails |
| 662-FONT-METRIC-03 | Low | ❔40 | ❔39 | ✅85 | ✅70 | ❌70 | ❌72 | · | **CONFLICT** | fontFamily() returns resolved-family not requested-family — substitution invisible |
| 263-STC-N01 | Medium | ✅55 | ⚠️58 | ✅90 | ✅70 | ✅90 | ✅55 | · | split | closeAll() destroys user's per-screen projection flip configuration |
| 475-STC-N02 | Low | ⚠️45 | ⚠️58 | ✅85 | ✅65 | ❌60 | ✅68 | · | **CONFLICT** | Find.qml close() doesn't reset replace-mode or regex-mode flags |
| 601-STC-N03 | Medium | ❔45 | ⚠️58 | ✅90 | ✅70 | ❌65 | ❔45 | · | **CONFLICT** | velocityIndicator.firstResetDone never cleared on dismiss — second activation broken |
| 322-STC-N04 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅70 | ✅75 | ✅68 | · | split | Projection window CursorAutoHide not reset on close — cursor permanently hidden |
| 445-STC-N05 | Low | ⚠️50 | ⚠️58 | ✅85 | ✅65 | ✅80 | ✅68 | · | split | cancel() doesn't call timer.stopTimer() — elapsed time persists across sessions |
| 324-TB-N01 | Medium | ⚠️45 | ⚠️58 | ✅85 | ✅70 | ✅80 | ✅68 | · | split | toolbar toggle timers produce stale state on rapid clicks |
| 325-TB-N02 | Medium | ⚠️45 | ⚠️58 | ✅90 | ✅70 | ✅75 | ✅68 | · | split | baseSpeedSlider/baseAccelerationSlider onMoved yanks focus to prompter instead of restoreFocus() |
| 676-TB-N03 | Low | ⚠️45 | ⚠️58 | ✅70 | ⚠️55 | ✅65 | ⚠️50 | · | split | Collapsible toolbar rows animate height but adjacent rows snap — no y-position animation |
| 352-TB-N04 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅70 | ❌60 | ✅68 | · | **CONFLICT** | velocityDragArea accepts MiddleButton without propagateComposedEvents — scroll blocked |
| 638-RESP-N01 | Low | ⚠️50 | ⚠️58 | ✅85 | ✅65 | ✅90 | ⚠️50 | · | split | minimumHeight: minimumWidth forces square aspect ratio — prevents landscape-strip windows |
| 574-RESP-N02 | Medium | ❔45 | ⚠️58 | ✅90 | ✅70 | ✅85 | ❔45 | · | split | mobileOrSmallScreen threshold at 1231px activates on default 1220px launch |
| 470-RESP-N03 | Low | ⚠️45 | ⚠️58 | ❌85 | ✅65 | ✅70 | ✅68 | · | **CONFLICT** | +android/main.qml omits all size declarations — transient zero-size layout on startup |
| 541-QT-LC-N01 | High | ❌70 | ❌76 | ✅95 | ⚠️60 | ❌90 | ❌70 | · | **CONFLICT** | QQmlFileSelector never instantiated — platform QML file selectors dead |
| 380-TC-N01 | Low | ✅60 | ✅78 | ✅80 | ✅65 | ✅60 | ✅60 | · | AGREE | Image.source assigned boolean false instead of empty string |
| 476-TC-N02 | Low | ⚠️45 | ⚠️58 | ✅80 | ✅65 | ❌60 | ✅68 | · | **CONFLICT** | property color value assigned string expression — silent coercion |
| 280-BLK-N01 | Medium | ✅70 | ⚠️58 | ✅85 | ✅70 | ❔55 | ✅70 | · | split | alignment() returns Qt::AlignCenter (includes vertical bit 0x0080) on null cursor |
| 202-BLK-N02 | Medium | ✅55 | ⚠️58 | ✅90 | ✅70 | ✅80 | ✅55 | · | split | updateContents() fails to reset block formatting — stale formats contaminate new document |
| 203-BLK-N03 | Medium | ✅60 | ⚠️58 | ✅90 | ✅70 | ✅90 | ✅60 | · | split | setLineHeight/setParagraphHeight apply document-wide — destroy per-block customization |
| 321-SHT-N01 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅70 | ✅90 | ✅68 | · | split | markerToggle/namedMarkerToggle forwarded but never handled — dead hotkeys |
| 473-SHT-N02 | Low | ⚠️45 | ⚠️58 | ⚠️75 | ✅65 | ✅75 | ✅68 | · | split | Missing StandardKey.FullScreen on Android |
| 426-LAZY-N01 | Low | ⚠️45 | ⚠️58 | ✅85 | ✅65 | ✅85 | ✅68 | · | split | namedMarkerConfiguration Loader double-loads KeyInputButton — first load wasted |
| 348-LAZY-N02 | Medium | ⚠️50 | ⚠️58 | ⚠️60 | ✅70 | ✅80 | ✅68 | · | split | InputsOverlay ObjectModel eagerly loads both tabs — hidden tab content loaded prematurely |
| 302-LL-N01 | Medium | ⚠️50 | ⚠️58 | ✅80 | ✅65 | ✅75 | ✅68 | · | split | 10 EditorToolbar MouseArea/TextField width-depends-on-width binding loops |
| 427-LL-N02 | Low | ✅55 | ✅78 | ❌95 | ✅65 | ❌55 | ✅55 | · | **CONFLICT** | ProgressIndicator stepSize divide-by-zero when prompter.height is 0 |
| 320-SHDR-N02 | Medium | ✅60 | ⚠️58 | ❌85 | ✅65 | ✅85 | ✅60 | · | **CONFLICT** | id: shadow collides with property ShaderEffectSource shadow — ambiguous resolution in blur chain |
| 345-KB-N01 | Medium | ⚠️45 | ⚠️58 | ✅85 | ✅65 | ❌70 | ✅68 | · | **CONFLICT** | Find.qml: 9 toolbar buttons missing focusPolicy — keyboard-invisible |
| 346-KB-N02 | Medium | ⚠️55 | ⚠️58 | ✅85 | ✅65 | ❌65 | ✅68 | · | **CONFLICT** | InputsOverlay TabBar TabButtons have no focusPolicy + keyNavigationEnabled: false — keyboard dead |
| 347-KB-N03 | Medium | ⚠️50 | ⚠️58 | ❌80 | ✅70 | ✅90 | ✅68 | · | **CONFLICT** | +windows and +android ESC handler uses .focus instead of .activeFocus — wrong boolean |
| 422-DRAG-N01 | Low | ⚠️45 | ⚠️58 | ✅80 | ✅65 | ✅60 | ✅68 | · | split | Image resize body drag: cursor shows OpenHandCursor until drag threshold exceeded |
| 399-DRAG-N02 | Low | ✅55 | ⚠️58 | ✅80 | ✅65 | ✅70 | ✅55 | · | split | textDragArea has no cursorShape — no cursor feedback during text drag |
| 186-SHAPE-N01 | Medium | ✅60 | ✅92 | ✅80 | ✅70 | ✅85 | ✅60 | · | AGREE | pointer_0.qml PathLine parent.width resolves to undefined (ShapePath has no width) — arrow collapsed |
| 577-SHAPE-N02 | Medium | ❔45 | ❔39 | ✅85 | ✅70 | ✅75 | ❔45 | · | split | concentricCircles Shape uses parent-space coordinates in local space — circles off-center |
| 293-FD-N01 | Medium | ⚠️55 | ⚠️58 | ✅90 | ✅65 | ✅85 | ✅68 | · | split | \|\| should be && in autoReload guard — user preference ignored for non-binary files |
| 326-TBND-N01 | Medium | ⚠️50 | ⚠️58 | ✅70 | ✅70 | ✅85 | ✅68 | · | split | SpellHighlighter regex excludes combining diacritical marks — NFD text misspelled |
| 353-TBND-N02 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅70 | ❌55 | ✅68 | · | **CONFLICT** | All CJK text marked misspelled — ideographic characters not in Hunspell dictionaries |
| 379-TBND-N03 | Low | ✅55 | ✅78 | ✅80 | ✅65 | ✅90 | ✅55 | · | AGREE | extendLastMarker() doesn't update Marker::length field — stale after appends |
| 542-MIME-N01 | High | ⚠️45 | ⚠️58 | ❌95 | ⚠️60 | ❌75 | ❌72 | · | split | Temporary QMimeDatabase — QMimeType dangling on Qt 5 (undefined behavior) |
| 146-MIME-N02 | Medium | ✅65 | ✅78 | ✅90 | ✅70 | ✅90 | ✅65 | · | AGREE | loadFromNetworkFinihed() ignores Content-Type header — all network content treated as HTML |
| 147-MIME-N03 | Medium | ✅70 | ✅78 | ✅85 | ✅70 | ✅90 | ✅70 | · | AGREE | PDF/EPUB/MOBI/AZW MIME-detected but import is no-op — error text becomes content |
| 266-TXT-FMT-N01 | Medium | ✅65 | ⚠️58 | ✅80 | ✅70 | ✅90 | ✅65 | · | split | setMarkerHref("") fails to clear QTextFormat::AnchorHref — stale href persists |
| 528-SCR-N01 | High | ❔45 | ❔39 | ✅90 | ✅70 | ✅90 | ❔45 | · | split | Per-screen projection flip settings lost on restart — never serialized |
| 183-SCR-N02 | Medium | ✅55 | ✅92 | ✅90 | ✅70 | ✅90 | ✅55 | · | AGREE | Duplicate entries in displayModel on first toggle — no clear() before setScreensModel() |
| 318-SCR-N03 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅65 | ✅85 | ✅68 | · | split | No runtime screen plug/unplug handling — stale projection windows on disconnected screens |
