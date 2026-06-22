# Multi-Agent Bug Review — QPrompt

_723 findings · agents: opus, gpt, deepseek, glm, kimi, opus-ultra · generated 2026-06-23_

Source of truth is `assessments.csv` (long format, grows by rows). Regenerate with `python build_review.py`. Full per-row rationales for unanimous findings live in `assessments.csv`; this file details only the rows where agents disagree.

## Summary

| Agent | FALSE | LEGIT | PARTIAL | UNSURE |
|---|---|---|---|---|
| opus | 49 | 288 | 319 | 67 |
| gpt | 44 | 333 | 299 | 47 |
| deepseek | 39 | 597 | 51 | 36 |
| glm | 19 | 559 | 133 | 12 |
| kimi | 73 | 641 | 7 | 2 |
| opus-ultra | 70 | 496 | 94 | 63 |

**Consensus** (6 agents): AGREE 192 · split 399 · CONFLICT 132

**Status:** OPEN 723

Legend: ✅ LEGIT · ❌ FALSE · ⚠️ PARTIAL · ❔ UNSURE · · = not assessed. Number = confidence.

## Matrix

| ID | Sev | opus | gpt | deepseek | glm | kimi | opus-ultra | Consensus | St | Title |
|---|---|---|---|---|---|---|---|---|---|---|
| MEM-01 | High | ✅100 | ✅88 | ✅90 | ✅90 | ✅95 | ✅100 | AGREE | · | Memory Leak: `_markersModel` allocated without parent, never deleted |
| MEM-02 | High | ✅100 | ✅88 | ✅90 | ✅90 | ✅95 | ✅100 | AGREE | · | Memory Leak: `_fileSystemWatcher` allocated without parent, never deleted |
| MEM-03 | Medium | ✅100 | ✅88 | ✅85 | ✅85 | ✅90 | ✅100 | AGREE | · | Memory Leak: `m_fontDialog` allocated without parent, never deleted |
| LOG-01 | High | ✅100 | ✅92 | ✅95 | ✅90 | ✅95 | ✅100 | AGREE | · | SessionModel::rowCount returns m_data.size() for both valid and invalid parents |
| LOG-02 | High | ✅95 | ✅92 | ✅95 | ✅90 | ✅95 | ✅95 | AGREE | · | Off-by-one: beginRemoveRows uses rowCount() instead of rowCount()-1 |
| LOG-03 | Medium | ✅100 | ✅78 | ✅98 | ✅95 | ✅95 | ✅100 | AGREE | · | MarkersModel::data returns data.position for LengthRole instead of data.length |
| LOG-04 | Medium | ✅100 | ✅78 | ⚠️60 | ✅85 | ✅85 | ✅100 | split | · | MarkersModel::extendLastMarker modifies data without emitting dataChanged |
| LOG-05 | Medium | ✅100 | ✅78 | ✅88 | ✅90 | ✅90 | ✅100 | AGREE | · | DocumentHandler::search ignores `loop` parameter when `regEx` is true |
| LOG-06 | Medium | ✅90 | ✅78 | ⚠️70 | ✅85 | ✅85 | ✅90 | split | · | DocumentHandler::replaceAll has potential infinite loop with regex |
| LOG-07 | Low | ⚠️60 | ⚠️52 | ⚠️50 | ⚠️60 | ✅70 | ⚠️50 | split | · | namedMarker() fetches cursor twice — stale-content risk |
| LOG-08 | Low | ✅100 | ✅88 | ✅85 | ⚠️55 | ✅90 | ✅100 | split | · | DataPoint default constructor leaves three members uninitialized |
| LOG-09 | Low | ❌95 | ❌76 | ❌80 | ❌80 | ✅75 | ❌95 | **CONFLICT** | · | Trailing comma in constructor member initializer list (non-standard C++ before C++20) |
| QML-01 | Critical | ❌90 | ❌90 | ❔30 | ❌85 | ✅90 | ❌90 | **CONFLICT** | · | 26 references to undefined `pointerSettings` ID in ReadRegionOverlay |
| QML-02 | Critical | ❌90 | ❌90 | ❔30 | ❌85 | ✅90 | ❌90 | **CONFLICT** | · | Undefined `pointerConfiguration` ID reference in ReadRegionOverlay |
| QML-03 | Critical | ✅95 | ✅92 | ✅75 | ❌80 | ✅90 | ✅95 | **CONFLICT** | · | Undefined `root` ID in WindowDragger.qml |
| QML-04 | High | ✅100 | ✅92 | ✅90 | ✅95 | ✅95 | ✅100 | AGREE | · | Typo: `verticalCentertop` instead of `verticalCenter` |
| QML-05 | High | ✅100 | ✅84 | ✅95 | ✅90 | ✅95 | ✅100 | AGREE | · | `&&` should be `\|\|` in clear button enabled condition |
| QML-06 | High | ✅100 | ✅84 | ✅90 | ✅85 | ✅95 | ✅100 | AGREE | · | Bitwise OR (`\|`) instead of AND (`&`) in modifier key check |
| QML-07 | High | ❌95 | ❌90 | ❌85 | ⚠️60 | ❌85 | ❌95 | split | · | `Text.CurveRendering` enum requires Qt >= 6.7 |
| QML-08 | Medium | ❌80 | ❌76 | ❔40 | ❌80 | ✅90 | ❌80 | **CONFLICT** | · | Invalid anchor target `undefined` |
| QML-09 | Medium | ❌95 | ❌90 | ❌85 | ⚠️55 | ❌85 | ❌95 | split | · | `QtQuick.Shapes 6.6` version mismatch with `QtCore 6.5` |
| QML-10 | Medium | ❌85 | ❌76 | ❔45 | ✅80 | ✅90 | ❌85 | **CONFLICT** | · | `+android/main.qml` missing `QmlUtil` for RecentDocuments |
| QML-11 | Medium | ✅90 | ⚠️58 | ✅85 | ⚠️70 | ✅75 | ✅90 | split | · | Dead code: `window` property declared but never used in WindowDragger |
| SEC-01 | Critical | ✅95 | ✅84 | ✅75 | ✅85 | ✅95 | ✅95 | AGREE | · | Arbitrary Command Execution via `sys://` Marker URIs |
| SEC-02 | Medium | ✅85 | ✅78 | ✅90 | ✅85 | ✅85 | ✅85 | AGREE | · | OBS WebSocket Password Stored in Plaintext |
| SEC-03 | Medium | ✅95 | ✅78 | ✅80 | ✅90 | ✅90 | ✅95 | AGREE | · | Information Disclosure: Full HTML Document Content Logged via qDebug |
| SEC-04 | High | ⚠️55 | ⚠️58 | ✅85 | ✅85 | ✅90 | ⚠️50 | split | · | SSRF / URL Injection — User-Controlled URL Passed to Network Loader |
| SEC-05 | Medium | ⚠️55 | ⚠️58 | ✅70 | ⚠️70 | ✅85 | ⚠️50 | split | · | User-Controlled Filename Passed to QProcess (LibreOffice import) |
| RES-01 | High | ✅95 | ✅84 | ✅90 | ✅85 | ✅90 | ✅95 | AGREE | · | Network reply overwritten without aborting previous download |
| RES-02 | High | ✅95 | ✅84 | ✅92 | ✅90 | ✅90 | ✅95 | AGREE | · | loadFromNetworkFinihed ignores the QNetworkReply* signal parameter |
| RES-03 | Low | ⚠️65 | ⚠️58 | ✅85 | ⚠️60 | ✅80 | ⚠️50 | split | · | ShakeDetector::s_instance never set to nullptr on destruction (dangling pointer) |
| RES-04 | Low | ⚠️65 | ⚠️58 | ✅85 | ⚠️60 | ✅80 | ⚠️50 | split | · | IosSaveDialog::s_instance same singleton dangling pattern |
| RES-05 | Low | ❌80 | ❌76 | ❌75 | ❌80 | ❌70 | ❌80 | AGREE | · | QTextStream left unflushed before QFile destruction |
| TYP-01 | High | ❌80 | ❔39 | ✅95 | ✅85 | ✅95 | ❌80 | **CONFLICT** | · | Dangling pointer from temporary std::string in SpellChecker::loadOne |
| TYP-02 | Medium | ❌90 | ❌76 | ✅90 | ⚠️55 | ✅90 | ❌90 | **CONFLICT** | · | Invalid Qt::LayoutDirection enum value cast |
| TYP-03 | Medium | ⚠️60 | ⚠️58 | ✅85 | ✅85 | ✅85 | ⚠️50 | split | · | Floating-point equality comparison of window opacity |
| TYP-04 | Medium | ✅95 | ⚠️58 | ✅90 | ✅85 | ✅90 | ✅95 | split | · | Bitwise AND on bools hides dead code in preventSleep |
| TYP-05 | Medium | ✅95 | ✅88 | ⚠️60 | ✅90 | ✅90 | ✅95 | split | · | Uninitialized pointer member m_reply in DocumentHandler |
| TYP-06 | Low | ✅95 | ⚠️58 | ✅85 | ❌75 | ✅90 | ✅95 | **CONFLICT** | · | Malformed preprocessor macro: `#define Use_GlobalAccel = 1` |
| TYP-07 | Low | ✅90 | ⚠️58 | ⚠️30 | ✅75 | ✅70 | ✅90 | split | · | Narrowing conversion: `size_t` → `int` in SpellChecker::decode |
| TYP-08 | Low | ❌95 | ❌76 | ❌80 | ❌85 | ✅75 | ❌95 | **CONFLICT** | · | DocumentHandler constructor trailing comma in initializer list |
| TYP-09 | Low | ❌90 | ❌76 | ⚠️40 | ⚠️55 | ❌80 | ❌90 | split | · | Null pointer dereferences in emit textChanged related to uninitialized m_document |
| TYP-10 | Low | ❌55 | ❌76 | ❌60 | ✅80 | ❌85 | ❌55 | **CONFLICT** | · | Uninitialized marker struct fields: length defaults to 1 |
| EDGE-01 | High | ✅95 | ✅84 | ✅95 | ✅85 | ✅90 | ✅95 | AGREE | · | QString::arg() called on string with no placeholder — program name silently dropped |
| EDGE-02 | High | ✅95 | ✅84 | ✅90 | ✅85 | ✅90 | ✅95 | AGREE | · | Empty container `first()` dereference — crash on hotkey with no windows |
| EDGE-03 | High | ✅90 | ✅84 | ✅85 | ✅90 | ✅90 | ✅90 | AGREE | · | Empty container `last()` dereference in `extendLastMarker` |
| EDGE-04 | Critical | ✅90 | ✅88 | ✅92 | ✅90 | ✅95 | ✅90 | AGREE | · | Null pointer dereference: `document()->textDocument()` not checked before `load()` |
| EDGE-05 | Critical | ✅90 | ✅88 | ✅92 | ✅90 | ✅95 | ✅90 | AGREE | · | Null pointer dereference: `textDocument()` unchecked in `search()` |
| EDGE-06 | Critical | ✅90 | ✅88 | ✅92 | ✅90 | ✅95 | ✅90 | AGREE | · | Null pointer dereference: `textDocument()` unchecked in `parse()` |
| EDGE-07 | High | ⚠️60 | ⚠️58 | ✅85 | ⚠️60 | ✅90 | ⚠️50 | split | · | Q_UNREACHABLE in Q_INVOKABLE method — UB if called from QML |
| EDGE-08 | Medium | ❌80 | ❌76 | ✅75 | ✅85 | ✅80 | ❌80 | **CONFLICT** | · | Q_ASSERT as thread-safety guard — removed in release builds |
| EDGE-09 | Medium | ✅90 | ✅88 | ✅85 | ✅75 | ✅85 | ✅90 | AGREE | · | QFile::copy() return value silently ignored |
| EDGE-10 | Low | ❌85 | ⚠️58 | ⚠️50 | ✅80 | ✅70 | ❌85 | **CONFLICT** | · | globalShortcutKey() switch without default — fallthrough to Q_UNREACHABLE |
| EDGE-11 | Medium | ⚠️60 | ⚠️58 | ✅85 | ✅85 | ✅80 | ⚠️50 | split | · | m_reply dereference without null check in loadFromNetworkFinihed() |
| EDGE-12 | Low | ⚠️40 | ⚠️58 | ❌40 | ⚠️60 | ✅60 | ❌72 | **CONFLICT** | · | QTextBlock::iterator scope fragility in parse() |
| PLAT-01 | High | ✅90 | ⚠️58 | ✅90 | ⚠️65 | ✅90 | ✅90 | split | · | KF6Crash_FOUND never defined as C preprocessor macro — KCrash support dead code |
| PLAT-02 | Medium | ✅90 | ✅78 | ✅85 | ✅85 | ✅85 | ✅90 | AGREE | · | REQUIRED_KF6_VERSION variable referenced but never defined |
| PLAT-03 | High | ✅85 | ✅84 | ❔50 | ✅85 | ✅90 | ✅85 | split | · | Wrong target name and wrong include path for KDMacTouchBar |
| PLAT-04 | Medium | ❌95 | ❌90 | ❔40 | ✅80 | ❌90 | ❌95 | **CONFLICT** | · | DS_Store.scpt referenced but file does not exist |
| PLAT-05 | Medium | ✅85 | ✅92 | ✅85 | ❌85 | ✅85 | ✅85 | **CONFLICT** | · | DBINARY_ICONS_RESOURCE is a typo — should be BINARY_ICONS_RESOURCE |
| PLAT-06 | Low | ✅90 | ✅78 | ✅80 | ✅80 | ✅80 | ✅90 | AGREE | · | qprompt_QM_LOADER variable never defined |
| PLAT-07 | Low | ✅95 | ⚠️58 | ✅85 | ❌75 | ✅90 | ✅95 | **CONFLICT** | · | Incorrect macro syntax: `#define Use_GlobalAccel = 1` |
| PLAT-08 | Medium | ⚠️50 | ⚠️58 | ✅85 | ⚠️55 | ✅85 | ⚠️50 | split | · | QNX platform guard inconsistency: main.cpp vs documenthandler.h |
| PLAT-09 | Low | ❔45 | ❔39 | ❔30 | ✅80 | ✅75 | ❔45 | split | · | Pre-build manifest references invalid Android SDK paths |
| R2-GH-01 | High | ❌80 | ❌76 | ✅80 | ✅80 | ✅85 | ❌80 | **CONFLICT** | · | Q_UNREACHABLE reachable when only QHotkey available on Wayland |
| R2-CMAKE-01 | Critical | ❌80 | ❌76 | ✅90 | ✅85 | ✅95 | ❌80 | **CONFLICT** | · | sphinx_add_docs silently ignores all keyword arguments due to empty cmake_parse_arguments prefix |
| R2-CMAKE-02 | High | ✅80 | ✅84 | ✅90 | ⚠️60 | ✅90 | ✅80 | split | · | cmake_minimum_required inside find module pollutes parent project policy settings |
| R2-CMAKE-03 | Medium | ✅80 | ✅78 | ✅85 | ❌80 | ✅85 | ✅80 | **CONFLICT** | · | WORKING_DIRECTORY and COMMENT not parseable by callers of sphinx_add_docs |
| R2-CMAKE-04 | Medium | ✅80 | ✅78 | ✅80 | ✅80 | ✅80 | ✅80 | AGREE | · | QML icon file(GLOB_RECURSE) missing CONFIGURE_DEPENDS causes stale icon sets |
| R2-PRP-01 | Medium | ✅80 | ✅78 | ❔45 | ✅90 | ✅90 | ✅80 | split | · | Qt.LeftToRight used as bare boolean — RTL branch always dead |
| R2-PRP-02 | Medium | ✅85 | ✅92 | ❔40 | ✅85 | ✅90 | ✅85 | split | · | Kirigami.Units.SmallSpacing — uppercase S yields undefined |
| R2-PRP-03 | Medium | ❌75 | ⚠️58 | ❔40 | ✅85 | ✅90 | ❌75 | **CONFLICT** | · | Units.LongDuration / Units.HumanMoment missing Kirigami. prefix |
| R2-PRP-04 | Low | ⚠️50 | ⚠️58 | ❔35 | ⚠️55 | ✅75 | ✅68 | split | · | Inconsistent focus restoration in decreaseVelocityButton |
| R2-PRP-05 | Low | ⚠️45 | ⚠️52 | ❔30 | ✅80 | ✅80 | ✅68 | split | · | Potential null-item access on async Loader in namedMarkerConfiguration.onOpened |
| R2-PTR-01 | Medium | ❌75 | ❌76 | ✅80 | ⚠️60 | ✅90 | ❌75 | **CONFLICT** | · | Type mismatch: textVerticalOffset declared int but fed a real |
| R2-PTR-02 | Medium | ❌75 | ❌76 | ✅80 | ⚠️60 | ✅90 | ❌75 | **CONFLICT** | · | Type mismatch: imageVerticalOffset declared int but fed a real |
| R2-PTR-03 | Medium | ✅80 | ✅78 | ❔40 | ✅85 | ✅85 | ✅80 | split | · | Casing error: Units.longDuration should be Units.LongDuration |
| R2-PTR-04 | Medium | ✅85 | ✅78 | ❔35 | ✅85 | ✅90 | ✅85 | split | · | Inverted indexOf truthiness in platform check for ColorDialog |
| R2-AND-01 | Critical | ✅90 | ⚠️58 | ❔35 | ✅85 | ✅95 | ✅90 | split | · | Android missing QmlUtil causes crash on factory reset and RecentDocuments |
| R2-AND-02 | Critical | ✅90 | ✅84 | ❔35 | ✅80 | ✅95 | ✅90 | split | · | Android missing restartDialog crashes LanguageSettingsOverlay and LayoutDirectionSettingsOverlay |
| R2-AND-03 | Medium | ✅80 | ✅78 | ❔35 | ✅80 | ✅80 | ✅80 | split | · | Android Settings missing fakeFullScreen persistence |
| R2-AND-04 | Low | ⚠️45 | ⚠️58 | ❔30 | ✅75 | ✅70 | ✅68 | split | · | Android Settings for "background" missing transparency persistence |
| R2-AND-05 | Low | ⚠️45 | ⚠️58 | ❔25 | ✅80 | ✅60 | ✅68 | split | · | Android loadTelemetryPage passes no properties object to pageStack push |
| R2-OVL-01 | Medium | ⚠️65 | ⚠️58 | ❔35 | ✅85 | ✅85 | ✅68 | split | · | InputsOverlay onOpened calls cursorAutoHide.restart() instead of reset() |
| R2-OVL-02 | Low | ✅85 | ✅78 | ❔35 | ✅80 | ✅80 | ✅85 | split | · | LanguageSettingsOverlay popup ListView currentIndex always resolves to -1 |
| R2-PTH-01 | Medium | ✅85 | ✅78 | ✅80 | ✅80 | ✅85 | ✅85 | AGREE | · | FileDialog filter matches all files on Linux due to stray glob |
| R2-PTH-02 | Medium | ✅85 | ✅78 | ✅80 | ✅85 | ✅85 | ✅85 | AGREE | · | File path from file:// URL preserves percent-encoding |
| R2-WHE-01 | High | ✅90 | ✅84 | ✅85 | ✅85 | ✅90 | ✅90 | AGREE | · | `focus: true` is JavaScript label, not assignment |
| R2-EDT-01 | Medium | ✅90 | ✅92 | ❔40 | ✅95 | ✅90 | ✅90 | split | · | Qt.AlignHustify typo — nonexistent enum value |
| R2-EDT-02 | High | ✅85 | ✅84 | ❔35 | ✅90 | ✅90 | ✅85 | split | · | wheelThrottleSettingsButton checked bound to completely unrelated document property |
| R2-EDT-03 | High | ✅80 | ✅84 | ⚠️55 | ✅85 | ✅90 | ✅80 | split | · | Checkable ToolButtons break checked property bindings on first click — systematic |
| R2-TEL-01 | Medium | ✅80 | ✅78 | ❔35 | ✅85 | ✅85 | ✅80 | split | · | Telemetry sub-toggles permanently disconnect from master toggle on click |
| R2-REC-01 | Low | ✅85 | ✅92 | ⚠️60 | ⚠️60 | ✅80 | ✅85 | split | · | File URI prefix strip off-by-one on Windows |
| R2-REC-02 | Medium | ⚠️50 | ⚠️58 | ❔30 | ✅80 | ✅75 | ✅68 | split | · | refreshExistence skips UI updates when dynamic children out of sync |
| R2-IOS-01 | High | ✅80 | ✅84 | ❔40 | ⚠️65 | ✅85 | ✅80 | split | · | Method swizzling re-entry causes infinite recursion on second invocation |
| R2-IOS-02 | Medium | ⚠️50 | ❔39 | ❔40 | ✅80 | ✅80 | ⚠️50 | split | · | Delegate block captures raw assign pointer — use-after-free risk |
| R2-IOS-03 | Medium | ✅85 | ✅78 | ✅75 | ✅80 | ✅80 | ✅85 | AGREE | · | UIApplication.keyWindow deprecated since iOS 13; breaks multi-window iPadOS |
| R2-WASM-01 | Medium | ✅85 | ✅78 | ❔35 | ⚠️65 | ✅85 | ✅85 | split | · | File input element never removed from DOM on user cancel |
| R2-WASM-02 | Medium | ✅85 | ✅78 | ❔35 | ✅85 | ✅85 | ✅85 | split | · | Insecure hostname validation via endsWith allows subdomain spoofing |
| R2-FONT-01 | Medium | ✅85 | ✅78 | ✅75 | ✅80 | ✅75 | ✅85 | AGREE | · | RichText label renders unescaped plain text — HTML metacharacters break display |
| R2-FONT-02 | Low | ✅85 | ✅92 | ✅95 | ✅90 | ✅90 | ✅85 | AGREE | · | Duplicate setText call on preview label |
| R2-ANDMAN-01 | Medium | ✅85 | ✅78 | ✅90 | ✅80 | ✅85 | ✅85 | AGREE | · | Ungrantable system/signature permissions bloating manifest |
| R2-ANDMAN-02 | Medium | ✅85 | ✅78 | ✅90 | ✅80 | ⚠️55 | ✅85 | split | · | MANAGE_EXTERNAL_STORAGE likely triggers Play Store scrutiny |
| R3-CTX-01 | Critical | ✅90 | ✅92 | ✅95 | ✅90 | ✅85 | ✅90 | AGREE | · | AbstractUnits missing QML_ELEMENT — all duration constants resolve to undefined |
| R3-CTX-02 | High | ✅90 | ✅84 | ✅98 | ✅85 | ✅90 | ✅90 | AGREE | · | GlobalHotkeys.SkipForward enum value mismatch — trailing 's' missing |
| R3-DOC-01 | Critical | ✅90 | ✅92 | ✅85 | ✅90 | ✅90 | ✅90 | AGREE | · | m_reloading uninitialized — undefined behavior on first load |
| R3-DOC-02 | Critical | ❌85 | ❌76 | ✅90 | ✅85 | ❌60 | ❌85 | **CONFLICT** | · | Unbalanced edit block in setLineHeight/setParagraphHeight |
| R3-DOC-03 | High | ✅85 | ✅84 | ✅90 | ✅85 | ✅85 | ✅85 | AGREE | · | load() sets m_fileUrl and emits fileUrlChanged even on failed load |
| R3-DOC-04 | High | ✅90 | ✅84 | ✅95 | ✅85 | ✅85 | ✅90 | AGREE | · | saveAs() silently ignores write/flush failures |
| R3-DOC-05 | High | ✅85 | ✅84 | ✅90 | ✅80 | ✅80 | ✅85 | AGREE | · | updateContents() produces two separate undo entries — undo destroys document |
| R3-DOC-06 | Medium | ✅90 | ✅78 | ✅85 | ✅80 | ✅90 | ✅90 | AGREE | · | reload() leaks m_reloading=true on URL mismatch |
| R3-DOC-07 | High | ✅85 | ✅84 | ✅90 | ✅85 | ✅85 | ✅85 | AGREE | · | Inverted selection state after failed search() |
| R3-SPL-01 | Medium | ✅70 | ✅78 | ✅80 | ⚠️65 | ✅75 | ✅70 | split | · | encode() uses toLocal8Bit() instead of dictionary-encoding-aware conversion |
| R3-SPL-02 | Medium | ✅70 | ✅78 | ✅80 | ⚠️65 | ✅75 | ✅70 | split | · | decode() uses fromLocal8Bit() — suggestions show as mojibake |
| R3-SPL-03 | Medium | ❌80 | ❌76 | ✅90 | ✅80 | ✅80 | ❌80 | **CONFLICT** | · | removeCustomWord() silently discards all addWord() additions |
| R3-SPL-04 | Medium | ✅75 | ✅78 | ✅90 | ✅80 | ✅70 | ✅75 | AGREE | · | Corrupt cached dictionary file persists permanently after failed copy |
| R3-SPL-05 | Medium | ⚠️45 | ⚠️58 | ✅85 | ✅85 | ⚠️55 | ⚠️50 | split | · | SpellChecker has zero thread safety — all methods unprotected |
| R3-MAIN-01 | Medium | ❌75 | ✅78 | ✅85 | ✅80 | ✅85 | ❌75 | **CONFLICT** | · | Command-line positional argument description/syntax swapped |
| R3-MAIN-02 | High | ⚠️55 | ⚠️58 | ✅90 | ✅85 | ✅75 | ✅68 | split | · | Invalid locale string constructed for short language codes |
| R3-MAIN-03 | Medium | ✅85 | ✅78 | ✅95 | ✅85 | ✅80 | ✅85 | AGREE | · | System locale changed even when translation file fails to load |
| R3-MAIN-04 | Low | ❌85 | ❌76 | ⚠️60 | ⚠️60 | ❌65 | ❌85 | split | · | Stack-allocated QTranslator outlives QApplication on shutdown |
| R3-MAIN-05 | Medium | ✅80 | ⚠️58 | ✅98 | ✅80 | ✅85 | ✅80 | split | · | Hardcoded Homebrew version-specific Kirigami import path |
| R3-MAIN-06 | High | ✅90 | ✅84 | ✅90 | ⚠️55 | ✅75 | ✅90 | split | · | Inconsistent Kirigami platform guards — missing WATCHOS and QNX |
| R3-MAIN-07 | Medium | ✅90 | ✅78 | ✅98 | ✅85 | ✅80 | ✅90 | AGREE | · | XDG_CURRENT_DESKTOP unconditionally forced to "KDE" on all Linux |
| R3-MAIN-08 | Low | ✅55 | ✅78 | ✅80 | ⚠️60 | ✅65 | ✅55 | split | · | QFontDatabase::addApplicationFont return value discarded |
| R3-APP-01 | Low | ❌75 | ❌76 | ❌85 | ⚠️60 | ✅80 | ❌75 | **CONFLICT** | · | AppController singleton and children never deallocated |
| R3-PROP-01 | Medium | ✅80 | ✅78 | ✅80 | ⚠️65 | ✅85 | ✅80 | split | · | selectionIsLowerCase bound to wrong NOTIFY signal |
| R3-SIG-01 | Low | ✅85 | ✅78 | ✅90 | ✅80 | ✅95 | ✅85 | AGREE | · | textChanged() signal declared but never emitted |
| R3-SIG-02 | Medium | ❌85 | ❌90 | ⚠️85 | ✅85 | ❌85 | ❌85 | **CONFLICT** | · | ShakeDetector signals declared but never emitted — dead feature |
| R3-SIG-03 | Medium | ❌90 | ❌90 | ✅75 | ✅85 | ❌85 | ❌90 | **CONFLICT** | · | IosSaveDialog accepted/rejected signals declared but never emitted |
| R3-PMT-01 | High | ⚠️60 | ⚠️58 | ✅95 | ✅85 | ✅95 | ✅68 | split | · | OBS WebSocket JSON.parse without try/catch — crash on malformed input |
| R3-PMT-02 | Medium | ✅60 | ✅78 | ✅90 | ✅80 | ✅90 | ✅60 | AGREE | · | OBS WebSocket no onError handler, no reconnection logic |
| R3-PMT-03 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅75 | ✅90 | ⚠️50 | split | · | goToNextMarker fallback desynchronizes cursor from viewport |
| R3-TMR-01 | Medium | ❔45 | ❔39 | ✅80 | ✅85 | ✅95 | ❔45 | split | · | TimerClock ETA uses __iDefault instead of actual __i during reverse scroll |
| R4-QTV-01 | Critical | ❌90 | ❌76 | ✅95 | ❌80 | ✅80 | ❌90 | **CONFLICT** | · | QtQuick 2.13 import does not exist in Qt 6.5 |
| R4-QTV-02 | Critical | ❌90 | ❌76 | ❔60 | ❌80 | ✅80 | ❌90 | **CONFLICT** | · | QtQuick.Window 2.0 import does not exist in Qt 6.5 |
| R4-QTV-03 | High | ❌90 | ❌76 | ❌98 | ❌75 | ❌90 | ❌90 | AGREE | · | QtQuick.Dialogs 6.6 imported in 9 files on Qt 6.5 target |
| R4-EXP-01 | Critical | ⚠️55 | ⚠️58 | ✅95 | ✅85 | ✅85 | ✅68 | split | · | No XSS sanitization — script tags, event handlers, javascript: URLs unfiltered |
| R4-EXP-02 | High | ✅90 | ✅84 | ✅95 | ✅85 | ✅95 | ✅90 | AGREE | · | insertHtmlAt() bypasses filterHtml() — unsanitized HTML from QML |
| R4-EXP-03 | High | ✅85 | ✅84 | ✅90 | ✅85 | ✅95 | ✅85 | AGREE | · | loadFromNetwork() destroys URL for relative URLs — host/path swapped |
| R4-EXP-04 | High | ✅80 | ✅84 | ✅90 | ✅80 | ✅90 | ✅80 | AGREE | · | AutoText inserts plain text as HTML — content corruption |
| R4-EXP-05 | Medium | ✅70 | ✅78 | ✅90 | ✅85 | ✅80 | ✅70 | AGREE | · | No encoding/charset detection — all imports assumed UTF-8 |
| R4-EXP-06 | Medium | ✅70 | ✅78 | ✅95 | ✅80 | ✅80 | ✅70 | AGREE | · | UTF-8 BOM not stripped — becomes phantom character at position 0 |
| R4-EXP-07 | Medium | ✅60 | ✅78 | ✅90 | ✅80 | ✅90 | ✅60 | AGREE | · | data: URI assumes base64 encoding without checking ;base64 token |
| R4-EXP-08 | Medium | ✅85 | ✅78 | ✅90 | ✅85 | ✅90 | ✅85 | AGREE | · | EPUB/MOBI/AZW import replaces document with error string |
| R4-EXP-09 | Low | ⚠️55 | ⚠️58 | ✅85 | ⚠️65 | ✅85 | ✅68 | split | · | LibreOffice import --cat and --convert-to flags are contradictory |
| R4-ROOT-01 | High | ✅90 | ✅84 | ✅95 | ✅85 | ✅95 | ✅90 | AGREE | · | Qt.openUrlExternally called with translation context string instead of URL |
| R4-ROOT-02 | Medium | ✅85 | ✅92 | ✅95 | ✅85 | ✅90 | ✅85 | AGREE | · | Invalid QML color value "initial" |
| R4-ROOT-03 | Medium | ❌80 | ❌76 | ✅90 | ⚠️65 | ✅90 | ❌80 | **CONFLICT** | · | ESC global shortcut skips single-layer pages — can't dismiss with keyboard |
| R4-ROOT-04 | Medium | ✅90 | ✅92 | ✅98 | ✅85 | ✅95 | ✅90 | AGREE | · | Duplicate "&Open" menu item in native File menu |
| R4-ROOT-05 | Low | ⚠️50 | ✅92 | ✅95 | ⚠️60 | ✅90 | ⚠️50 | split | · | loadRemoteControlPage/loadTelemetryPage reference undefined component IDs |
| R4-EVT-01 | Critical | ❌85 | ❌76 | ✅95 | ❌80 | ❌90 | ❌85 | **CONFLICT** | · | Missing braces on if/else — syntax error in alignRightButton |
| R4-EVT-02 | Medium | ✅90 | ⚠️58 | ✅95 | ✅80 | ✅95 | ✅90 | split | · | Velocity modifier ComboBox lists 2 options but switch handles 4 — dead code |
| R4-EVT-03 | High | ⚠️60 | ✅84 | ✅85 | ✅80 | ✅85 | ✅68 | split | · | CursorAutoHide null access on root.pageStack.currentItem during page transitions |
| R4-CMT-01 | Critical | ✅90 | ✅84 | ✅98 | ✅85 | ✅90 | ✅90 | AGREE | · | PDF import completely broken — converter invocation commented out |
| R4-PRJ-01 | High | ❌80 | ❌76 | ❌85 | ⚠️60 | ❌90 | ❌80 | split | · | flip variable spuriously reset in project() inner loop else-branch |
| R4-PRJ-02 | High | ❔45 | ❔39 | ✅95 | ✅80 | ✅95 | ❔45 | split | · | displayModel.get().flipSetting writes to snapshot copy — never mutates model |
| R4-PRJ-03 | Medium | ✅55 | ✅92 | ✅90 | ✅80 | ✅95 | ✅55 | AGREE | · | setScreensModel() duplicates display entries on each toggle cycle |
| R4-PRJ-04 | Medium | ✅55 | ✅78 | ✅85 | ✅80 | ✅90 | ✅55 | AGREE | · | Division by zero in projection image height |
| R4-ROV-01 | High | ⚠️60 | ⚠️58 | ✅90 | ✅80 | ✅95 | ✅68 | split | · | Division by zero in __customPlacement when overlay full |
| R4-ROV-02 | High | ⚠️65 | ⚠️58 | ✅90 | ✅80 | ✅90 | ✅68 | split | · | Drag permanently breaks y property binding on readRegion |
| R4-ROV-03 | Medium | ✅90 | ✅78 | ✅95 | ⚠️65 | ✅95 | ✅90 | split | · | Bitwise OR \| used for width fallback instead of logical OR |
| R4-BKG-01 | Medium | ✅85 | ✅78 | ✅85 | ⚠️60 | ✅90 | ✅85 | split | · | Flip transform origin stays at (0,0) when Flip stored as property |
| R4-SHD-01 | Medium | ❌80 | ❌76 | ✅90 | ⚠️65 | ✅80 | ❌80 | **CONFLICT** | · | Duplicate class implementation between .cpp and .mm — ODR risk |
| R4-IOSCPP-01 | Low | ⚠️50 | ⚠️58 | ✅90 | ⚠️60 | ✅85 | ✅68 | split | · | QTemporaryDir created on all platforms including non-iOS where unused |
| R4-SIG-ADD-01 | Low | ⚠️45 | ⚠️58 | ⚠️60 | ✅75 | ✅70 | ✅68 | split | · | SessionModel::appendDataPoint declared public slot but never connected |
| FINAL-01 | Critical | ✅90 | ✅92 | ✅98 | ✅85 | ✅95 | ✅90 | AGREE | · | TimerClock references undefined `timer` id — ETA and stopwatch completely broken |
| FINAL-02 | Critical | ❌85 | ❌90 | ❌90 | ✅85 | ✅95 | ❌85 | **CONFLICT** | · | Missing `QtQuick.Controls.Material` import — 3 Material references unresolved |
| FINAL-03 | Critical | ✅95 | ✅84 | ✅98 | ✅80 | ✅90 | ✅95 | AGREE | · | Missing breeze-icons submodule — fresh clone cannot build |
| FINAL-04 | High | ⚠️50 | ⚠️58 | ⚠️60 | ✅80 | ✅95 | ✅68 | split | · | NSIS start-menu shortcut icon name mismatches actual binary name |
| FINAL-05 | High | ✅90 | ✅84 | ✅95 | ✅85 | ✅85 | ✅90 | AGREE | · | WindowDragger mouse delta accumulation error — window moves farther than cursor |
| FINAL-06 | High | ✅90 | ⚠️58 | ❌95 | ✅85 | ✅95 | ✅90 | **CONFLICT** | · | CMAKE_OSX_ARCHITECTURES contains literal quotes — universal binary broken |
| FINAL-07 | High | ❌80 | ❌76 | ❌98 | ⚠️60 | ✅95 | ❌80 | **CONFLICT** | · | CMake wrong variable name: InstallRequiredSystemLibraries instead of CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS |
| FINAL-08 | High | ✅85 | ✅84 | ✅95 | ✅80 | ✅90 | ✅85 | AGREE | · | setup.sh vcvarsall.bat executed from bash — MSVC env not propagated |
| FINAL-09 | Medium | ✅85 | ✅92 | ✅90 | ❌80 | ✅95 | ✅85 | **CONFLICT** | · | `on__IChanged` handler typo — never fires |
| FINAL-10 | High | ⚠️55 | ⚠️58 | ✅90 | ✅80 | ✅90 | ⚠️50 | split | · | Two animations target same `position` property — conflict |
| FINAL-11 | High | ✅85 | ✅84 | ✅95 | ✅85 | ✅95 | ✅85 | AGREE | · | onFrameSwapped calls grabToImage every frame — severe performance hit |
| FINAL-12 | Medium | ✅80 | ✅78 | ✅95 | ✅80 | ✅90 | ✅80 | AGREE | · | SystemFontChooserDialog setWindowFlags strips all decorations |
| FINAL-13 | Medium | ✅90 | ✅92 | ✅95 | ✅90 | ✅95 | ✅90 | AGREE | · | Invalid Korean locale code "ko_KO" — should be "ko_KR" |
| FINAL-14 | Medium | ⚠️55 | ⚠️58 | ✅98 | ✅85 | ✅95 | ⚠️50 | split | · | Wrong placeholder `%0` instead of `%1` — font name never displayed |
| FINAL-15 | High | ⚠️55 | ⚠️58 | ✅90 | ✅85 | ✅85 | ⚠️50 | split | · | Missing edit block wrapping in setLineHeight/setParagraphHeight |
| FINAL-16 | Critical | ❔50 | ⚠️58 | ✅80 | ✅85 | ✅95 | ❔50 | split | · | Countdown completion uses state++ bypassing toggle() entry actions |
| FINAL-17 | Medium | ✅85 | ✅78 | ✅90 | ✅85 | ✅90 | ✅85 | AGREE | · | ScriptAction references non-existent function `paintReady` |
| FINAL-18 | Medium | ✅100 | ✅78 | ✅95 | ✅85 | ✅95 | ✅100 | AGREE | · | MarkersModel extendLastMarker modifies data without emitting dataChanged |
| FINAL-19 | Medium | ✅70 | ✅78 | ✅85 | ⚠️65 | ✅85 | ✅70 | split | · | Encoding fallback uses toLocal8Bit() instead of dictionary's actual encoding |
| FINAL-20 | High | ❌80 | ❌76 | ❌90 | ✅85 | ✅90 | ❌80 | **CONFLICT** | · | Dangling pointer from temporary QByteArray in marker anchor parsing |
| FINAL-21 | Medium | ✅75 | ✅78 | ✅70 | ✅80 | ✅85 | ✅75 | AGREE | · | clearProperty(AnchorHref/AnchorName) ineffective through mergeCharFormat |
| FINAL-22 | High | ⚠️50 | ⚠️58 | ✅85 | ✅80 | ✅85 | ⚠️50 | split | · | Behavior.onRunningChanged calls toggle() from within animation handler — re-entrant state change |
| CUR-N01 | Critical | ✅90 | ✅84 | ✅95 | ✅85 | ✅95 | ✅90 | AGREE | · | replaceAll() infinite loop when replacement contains search pattern |
| CUR-N02 | High | ✅95 | ✅84 | ✅98 | ✅85 | ✅95 | ✅95 | AGREE | · | search() regex path ignores loop parameter — unconditional wrap |
| CUR-N03 | Medium | ✅70 | ✅78 | ✅80 | ✅80 | ✅75 | ✅70 | AGREE | · | alignment() reads blockFormat on multi-block selection — returns wrong alignment |
| DCL-N01 | Medium | ✅55 | ✅78 | ✅95 | ✅80 | ✅95 | ✅55 | AGREE | · | filterHtml default parameter in .cpp but not in header — QML can't call with 1 arg |
| DCL-N02 | Medium | ✅55 | ✅78 | ✅95 | ✅80 | ✅95 | ✅55 | AGREE | · | setKeyMarker default parameter mismatch — same pattern |
| IMP-N01 | Critical | ❌60 | ❌76 | ⚠️75 | ⚠️65 | ❌80 | ❌60 | split | · | import Qt.labs.platform 1.1 — Menu/MenuBar/MenuItem dropped in Qt 6 |
| IMP-N02 | Critical | ❌65 | ❌76 | ✅80 | ⚠️60 | ✅95 | ❌65 | **CONFLICT** | · | import QtWebSockets 1.10 — wrong version for Qt 6.5 |
| MATH-N01 | High | ✅65 | ✅84 | ✅95 | ✅85 | ✅90 | ✅65 | AGREE | · | Division by zero in __timeToArival/__timeToEnd when speed=0 |
| MATH-N02 | Medium | ✅60 | ✅78 | ✅90 | ✅80 | ✅90 | ✅60 | AGREE | · | Bitwise << on floating-point in TimerClock — precision loss |
| LYR-N01 | High | ⚠️60 | ✅84 | ✅85 | ✅85 | ✅90 | ✅68 | split | · | InputsOverlay calls cursorAutoHide.restart() on open instead of reset() |
| LYR-N02 | Medium | ⚠️50 | ✅78 | ✅75 | ⚠️65 | ✅90 | ✅68 | split | · | Three OverlaySheets missing from ESC dismiss chain |
| LYR-N03 | Medium | ❔45 | ✅78 | ✅88 | ⚠️60 | ❌80 | ❔45 | **CONFLICT** | · | ContextDrawer exposes prompter actions while viewing layer pages |
| LYR-N04 | Medium | ⚠️50 | ✅78 | ✅85 | ✅80 | ✅90 | ✅68 | split | · | ESC handler uses activeFocus in base but focus in platform variants — inconsistent |
| TRL-N01 | High | ⚠️55 | ✅84 | ✅95 | ✅85 | ✅95 | ⚠️50 | split | · | qsTr() uses %0 placeholder — should be %1 (font name never displayed) |
| TRL-N02 | Medium | ✅50 | ✅78 | ✅90 | ✅80 | ✅90 | ✅50 | AGREE | · | Application --help description not translatable |
| TRL-N03 | Medium | ⚠️45 | ✅78 | ✅90 | ✅80 | ✅85 | ✅68 | split | · | About-dialog credit roles not translatable |
| W10-HTK-01 | Critical | ❌70 | ❌76 | ✅92 | ✅80 | ✅95 | ❌70 | **CONFLICT** | · | autoRepeat=true for ALL QHotkey shortcuts — non-velocity actions broken when held |
| W10-HTK-02 | High | ✅65 | ✅88 | ✅88 | ✅80 | ✅95 | ✅65 | AGREE | · | QHotkey::setShortcut return value silently ignored — no failure detection |
| W10-PMV-01 | High | ⚠️50 | ⚠️58 | ⚠️70 | ⚠️60 | ✅80 | ✅68 | split | · | font.pixelSize evaluates to 0 before first layout pass — crash hazard |
| W10-PMV-02 | Medium | ⚠️50 | ⚠️58 | ✅80 | ⚠️65 | ✅85 | ✅68 | split | · | Circular ShaderEffectSource dependency — shadow ghost on first frame |
| W10-CLP-01 | High | ⚠️55 | ⚠️58 | ❌80 | ✅80 | ✅85 | ✅68 | **CONFLICT** | · | Paste-without-formatting fails when clipboard lacks text/plain |
| W10-CLP-02 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅80 | ✅85 | ✅68 | split | · | Remote image URLs in pasted HTML cause unsanctioned network requests |
| W10-CNV2-01 | High | ✅80 | ✅92 | ✅90 | ✅85 | ✅95 | ✅80 | AGREE | · | Default stylesheet has invalid CSS color quoting — exported HTML broken in browsers |
| W10-CNV2-02 | High | ✅55 | ✅84 | ✅92 | ✅80 | ✅90 | ✅55 | AGREE | · | No markdown export — round-trip silently destroys all formatting |
| W10-CNV2-03 | High | ⚠️45 | ⚠️58 | ⚠️65 | ✅85 | ✅85 | ✅68 | split | · | import() uses fromStdString on non-Windows — encoding corruption |
| W10-SWT-01 | High | ⚠️55 | ⚠️58 | ✅90 | ✅80 | ✅90 | ✅68 | split | · | CloseActions switch drops RecentLocal/RecentRemote — recent document open silently lost after save |
| W10-SWT-02 | High | ⚠️55 | ⚠️58 | ✅90 | ✅80 | ✅90 | ✅68 | split | · | Same bug in IosSaveDialog.onAccepted path |
| W10-DEP-01 | Critical | ✅75 | ✅92 | ✅92 | ⚠️65 | ✅95 | ✅75 | split | · | Missing vcpkg.json manifest — vcpkg manifest mode installs nothing |
| W10-WSM-01 | Critical | ⚠️55 | ⚠️58 | ✅88 | ✅80 | ✅85 | ✅68 | split | · | Infinite reload loop on unauthorized WASM host — app unusable |
| W10-WSM-02 | Medium | ⚠️50 | ⚠️58 | ✅88 | ✅80 | ✅85 | ✅68 | split | · | Global file-picker state overwritten by re-entrant calls — wrong file delivered |
| W10-PLF-01 | Critical | ✅70 | ✅84 | ✅95 | ✅80 | ✅85 | ✅70 | AGREE | · | BSD detection broken — FreeBSD enters wrong code paths |
| W10-PLF-02 | High | ⚠️50 | ⚠️58 | ✅95 | ✅80 | ✅85 | ✅68 | split | · | QHotkey_FOUND never set in FetchContent path — built but never linked |
| TS-01 |  | ❔40 | ⚠️58 | ✅88 | ✅85 | ✅95 | ❔40 | split | · | Finnish welcome guide → Dutch (not Finnish) |
| TS-02 |  | ⚠️50 | ⚠️58 | ✅90 | ✅85 | ✅95 | ✅68 | split | · | Arabic file `ar_EG` vs UI `ar_AE` mismatch |
| TS-03 |  | ✅90 | ✅78 | ✅90 | ✅90 | ✅95 | ✅90 | AGREE | · | Korean UI `ko_KO` vs file `ko_KR` mismatch |
| TS-04 |  | ❔40 | ❔39 | ✅85 | ❔50 | ✅90 | ❔40 | split | · | French "Saved" → verb "Enregistrer" (should be adjective "Enregistré") |
| TS-05 |  | ⚠️45 | ⚠️58 | ✅85 | ✅80 | ✅85 | ✅68 | split | · | Finnish/French/Korean/Italian "Saved" → verb with stray `&amp;` accelerator |
| TS-06 |  | ❔40 | ❔39 | ✅90 | ❔50 | ✅90 | ❔40 | split | · | Czech/French "Language settings" → "Pointer settings" (copy-paste error) |
| TS-07 |  | ❔40 | ❔39 | ✅85 | ❔50 | ✅90 | ❔40 | split | · | Finnish/French/Korean "Colors for prompter states" → "Toggle Prompter State" |
| TS-08 |  | ❔40 | ❔39 | ✅85 | ❔50 | ✅90 | ❔40 | split | · | French "Prompting:" → "Start prompter" |
| TS-09 |  | ❔40 | ❔39 | ✅85 | ❔50 | ✅90 | ❔40 | split | · | Finnish/French/Korean/Dutch "Vertical offset" → "Velocity" |
| TS-10 |  | ❔40 | ❔39 | ✅85 | ❔50 | ✅90 | ❔40 | split | · | Finnish/Korean "Next reload starts at" → "Step acceleration" |
| TS-11 |  | ❔40 | ❔39 | ✅90 | ❔50 | ✅90 | ❔40 | split | · | French/Finnish/Korean "No pointers" → "Both pointers" (opposite meaning) |
| TS-12 |  | ❔40 | ❔39 | ✅90 | ❔50 | ✅90 | ❔40 | split | · | French "Alt" key → "Tout" (means "All") |
| TS-13 |  | ❔40 | ❔39 | ✅90 | ❔50 | ✅90 | ❔40 | split | · | French "Set velocity to 0–10" (all 11) → identical "Vitesse de départ" |
| TS-14 |  | ❔40 | ❔39 | ✅85 | ❔50 | ✅90 | ❔40 | split | · | French "Clear color" → "Light color" |
| TS-15 |  | ❔40 | ❔39 | ✅85 | ❔50 | ✅90 | ❔40 | split | · | Finnish/Korean right pointer reuse → left pointer (swapped) |
| TS-16 |  | ⚠️45 | ⚠️58 | ✅90 | ✅80 | ✅90 | ✅68 | split | · | Paragraph spacing: 8 languages strip trailing `%` from `<pre>%1%</pre>` |
| TS-17 |  | ⚠️45 | ⚠️58 | ✅90 | ✅80 | ✅90 | ✅68 | split | · | Line width: 7 languages add spurious `%` to `<pre>%1</pre>` |
| TS-18 |  | ❔40 | ❔39 | ✅85 | ✅85 | ✅90 | ❔40 | split | · | Orphan files: Hebrew and Polish exist but UI entries commented out |
| HTK-01 | Critical | ❔45 | ❔39 | ✅95 | ⚠️65 | ✅95 | ❔45 | split | · | KGlobalAccel default permanently destroyed on first user customization |
| HTK-02 | High | ❔45 | ❔39 | ✅92 | ✅80 | ✅90 | ❔45 | split | · | User shortcuts never persisted when only Use_GlobalAccel defined (no QHotkey) |
| HTK-03 | High | ⚠️50 | ⚠️58 | ✅90 | ✅80 | ✅90 | ✅68 | split | · | KGlobalAccel defaults silently zeroed on non-Wayland when QHotkey co-exists |
| HTK-04 | Medium | ✅60 | ✅92 | ✅85 | ✅80 | ✅85 | ✅60 | AGREE | · | Wrong enum type `Qt::KeyboardModifier` (singular) for modifier variable |
| HTK-05 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅85 | ⚠️50 | split | · | VelocityTo0 default shortcut uses `Qt::Key_acute` — unreachable dead key |
| HTK-06 | Medium | ⚠️45 | ⚠️58 | ✅90 | ✅80 | ✅85 | ⚠️50 | split | · | Pause (Ctrl+Space) and Stop (Meta+Space) conflict — Meta+Space captured by OS |
| HTK-07 | Low | ⚠️45 | ⚠️58 | ✅88 | ✅75 | ✅80 | ⚠️50 | split | · | Double `removeAllShortcuts()` IPC round-trip in customization path |
| HTK-08 | Low | ⚠️50 | ⚠️58 | ✅85 | ✅75 | ✅85 | ⚠️50 | split | · | key/modifiers parameters silently discarded mid-function on non-Wayland |
| TMR-01 | High | ❔50 | ❔39 | ✅92 | ✅85 | ✅95 | ❔50 | split | · | Countdown→Prompting auto-transition via state++ bypasses toggle() entirely |
| TMR-02 | Medium | ❔45 | ❔39 | ✅80 | ✅80 | ✅85 | ❔45 | split | · | timer.updateTimer() runs before timer.startTimer() on Prompting entry |
| TMR-03 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅75 | ✅85 | ✅68 | split | · | dissolveIn animation re-triggered entering Running from Ready — flicker |
| TMR-04 | Low | ❔45 | ❔39 | ✅80 | ⚠️60 | ✅80 | ❔45 | split | · | Countdown arc hypotenuse uses geometric center instead of arc center |
| TMR-05 | Low | ✅85 | ✅78 | ✅88 | ✅85 | ✅90 | ✅85 | AGREE | · | ScriptAction `paintReady` references non-existent function |
| TMR-06 | Low | ❔45 | ❔39 | ✅85 | ⚠️60 | ✅80 | ❔45 | split | · | dissolveOut starts too early when disappearWithin > 1 |
| TMR-07 | Low | ✅55 | ⚠️58 | ⚠️65 | ⚠️55 | ✅75 | ✅55 | split | · | countdownAnimation restart uses non-idempotent running=true |
| TMR-08 | Low | ❔45 | ❔39 | ✅80 | ⚠️55 | ✅80 | ❔45 | split | · | timer.running not explicitly set in Countdown state — relies on revert behavior |
| SPL2-11 | Medium | ✅60 | ✅78 | ✅90 | ✅80 | ✅85 | ✅60 | AGREE | · | addCustomWord trims but removeCustomWord does not — asymmetry |
| SPL2-12 | Medium | ✅55 | ✅92 | ✅88 | ✅80 | ✅85 | ✅55 | AGREE | · | Case-sensitive contains/indexOf but case-insensitive sort — duplicates |
| SPL2-13 | Medium | ✅55 | ✅78 | ✅90 | ✅80 | ✅85 | ✅55 | AGREE | · | saveCustomWordsToDisk has void return — callers cannot detect I/O failure |
| SPL2-14 | Medium | ✅65 | ✅92 | ✅85 | ✅75 | ✅85 | ✅65 | AGREE | · | Cached QRC dicts never invalidated after app update |
| SPL2-15 | Medium | ✅60 | ✅78 | ✅90 | ✅85 | ✅85 | ✅60 | AGREE | · | spell() returns true when no dicts loaded — silent no-op |
| SPL2-16 | Low | ✅55 | ✅88 | ✅80 | ✅75 | ✅75 | ✅55 | AGREE | · | QDir::mkpath return unchecked — dict cache directory may silently not exist |
| SPL2-17 | Low | ✅55 | ✅88 | ✅80 | ✅75 | ✅75 | ✅55 | AGREE | · | QFile::setPermissions return unchecked — cached dict may be unreadable |
| SPL2-18 | Low | ✅55 | ✅88 | ✅85 | ⚠️65 | ✅75 | ✅55 | split | · | Hunspell::add return value unchecked at 4 call sites |
| SPL2-19 | Low | ✅55 | ✅78 | ✅85 | ✅80 | ✅80 | ✅55 | AGREE | · | availableDictionaries enumerates .dic without verifying .aff exists |
| SPL2-20 | Low | ⚠️45 | ⚠️58 | ❌85 | ✅75 | ✅70 | ✅68 | **CONFLICT** | · | loadCustomWordsFromDisk redundant exists() before open() |
| WSM-03 | High | ⚠️50 | ⚠️58 | ✅88 | ⚠️65 | ✅80 | ✅68 | split | · | readAsDataURL causes quadruple in-memory copy of file content |
| BLD-05 | Medium | ✅55 | ✅78 | ✅95 | ✅85 | ✅95 | ✅55 | AGREE | · | .env.android references Qt 5.15.2 — project requires Qt 6.8.2+ |
| EVT-01 | High | ⚠️50 | ⚠️58 | ⚠️60 | ✅80 | ✅85 | ✅68 | split | · | velocityDragArea (z:5) blocks viewport.mouse (z:0) wheel events |
| EVT-02 | High | ❌55 | ⚠️58 | ✅88 | ✅80 | ✅85 | ❌55 | **CONFLICT** | · | Zero inputMethodHints on any TextField — IME broken for CJK/Indic |
| EVT-03 | High | ⚠️50 | ⚠️58 | ✅90 | ✅80 | ✅85 | ✅68 | split | · | velocityDragOverlay (z:7) steals clicks from control buttons (z:6) |
| EVT-04 | High | ⚠️50 | ⚠️58 | ✅92 | ✅80 | ✅85 | ✅68 | split | · | Drag breaks editor.x declarative binding permanently |
| EVT-05 | High | ⚠️50 | ⚠️58 | ✅92 | ✅80 | ✅85 | ✅68 | split | · | Drag breaks positionHandler.x declarative binding permanently |
| EVT-06 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅80 | ✅85 | ✅68 | split | · | Drag breaks stopwatch.x binding permanently |
| EVT-07 | Medium | ✅60 | ✅78 | ✅90 | ✅80 | ✅85 | ✅60 | AGREE | · | TabBar currentIndex binding broken on first TabButton click |
| EVT-08 | Medium | ✅60 | ✅78 | ✅88 | ✅80 | ✅85 | ✅60 | AGREE | · | Two additional checkable ToolButton binding breakage instances |
| EVT-09 | Low | ⚠️45 | ⚠️52 | ✅78 | ⚠️60 | ✅70 | ✅68 | split | · | Flow ToolSeparator visibility compares y of potentially invisible rows |
| EVT-10 | Low | ⚠️50 | ⚠️58 | ✅85 | ⚠️60 | ✅85 | ✅68 | split | · | Nested MouseAreas with hoverEnabled steal hover from parent Buttons |
| ENC-01 | Medium | ✅60 | ✅78 | ✅88 | ✅80 | ✅95 | ✅60 | AGREE | · | truncate(-1) when font preview text has no spaces |
| ENC-02 | Low | ✅55 | ✅78 | ✅85 | ✅80 | ✅90 | ✅55 | AGREE | · | getMarkerKey() mid(4) without length/startsWith guard |
| ANM-N01 | Medium | ✅70 | ✅78 | ✅92 | ✅80 | ✅90 | ✅70 | AGREE | · | Easing.EaseOut is not a valid Qt Quick easing type (2 instances) |
| NET-01 | High | ✅65 | ✅84 | ✅92 | ✅85 | ✅95 | ✅65 | AGREE | · | loadFromNetworkFinihed never checks m_reply->error() |
| NET-02 | Medium | ⚠️50 | ⚠️58 | ⚠️70 | ✅80 | ✅90 | ❌72 | **CONFLICT** | · | RedirectPolicyAttribute set to boolean true → NoLessSafeRedirectPolicy |
| THR-01 | Medium | ⚠️45 | ⚠️58 | ✅82 | ⚠️65 | ✅85 | ⚠️50 | split | · | IosSaveDialog::create() — unsynchronized singleton race |
| THR-02 | Medium | ⚠️45 | ⚠️58 | ✅82 | ⚠️65 | ✅85 | ⚠️50 | split | · | ShakeDetector::create() — identical unsynchronized singleton race |
| THR-03 | Low | ⚠️50 | ⚠️58 | ✅80 | ✅80 | ✅85 | ⚠️50 | split | · | search() — mutable static QRegularExpression shared across all callers |
| THR-04 | Medium | ⚠️45 | ✅78 | ⚠️72 | ✅85 | ✅85 | ⚠️50 | split | · | SpellChecker zero thread safety — explicit finding |
| DRW-01 | Medium | ⚠️50 | ⚠️58 | ✅88 | ⚠️65 | ✅85 | ✅68 | split | · | interalFocusElsewhere() misses 3 OverlaySheets + 2 Drawers — hotkeys pass through |
| DRW-02 | Medium | ⚠️50 | ⚠️58 | ✅88 | ⚠️65 | ✅85 | ✅68 | split | · | globalDrawer and contextDrawer missing from ESC dismiss chain |
| AND-BLD-01 | Critical | ✅80 | ✅92 | ✅95 | ⚠️65 | ✅95 | ✅80 | split | · | Missing version.gradle — Gradle build fails |
| AND-RES-01 | Medium | ⚠️45 | ⚠️58 | ✅90 | ✅80 | ✅90 | ✅68 | split | · | Invalid android:scaleType on bitmap element |
| AND-MFT-01 | Medium (latent) | ⚠️45 | ⚠️58 | ✅85 | ⚠️65 | ✅75 | ✅68 | split | · | FileProvider resource @xml/qtprovider_paths — file named filepaths.xml |
| SHADOW-01 | Low | ✅60 | ✅78 | ✅85 | ⚠️60 | ❌80 | ✅60 | **CONFLICT** | · | id: rotation shadows Item.rotation property |
| SHADOW-02 | Low | ✅55 | ✅78 | ✅85 | ⚠️60 | ❌80 | ✅55 | **CONFLICT** | · | id: flow shadows Flow.flow property |
| FOC-N01 | Low | ✅65 | ✅78 | ✅88 | ✅80 | ✅95 | ✅65 | AGREE | · | focus: true is JS label in atEndLoopDelay SpinBox |
| FOC-N02 | Low | ✅65 | ✅78 | ✅88 | ✅80 | ✅95 | ✅65 | AGREE | · | Same JS label bug in countdownConfiguration SpinBoxes (2 instances) |
| FOC-N03 | Low | ⚠️50 | ✅78 | ✅85 | ⚠️60 | ✅85 | ✅68 | split | · | Tab/Backtab asymmetry — Backtab silently unhandled |
| VER-01 | Low | ⚠️45 | ✅78 | ✅85 | ⚠️60 | ❌90 | ❌72 | **CONFLICT** | · | Qt::MarkdownText version guard 0x050F00 (5.15) — API added in 5.14 |
| CPY-01 | Low | ⚠️40 | ⚠️58 | ✅80 | ✅75 | ❌80 | ⚠️50 | **CONFLICT** | · | 5 Q_INVOKABLE methods pass QString by value instead of const& |
| DSZ-01 | Medium | ✅60 | ⚠️58 | ✅88 | ✅80 | ✅80 | ✅60 | split | · | InputsOverlay hardcoded height:680 — overflows on phones |
| DSZ-02 | Medium | ⚠️45 | ✅78 | ✅88 | ✅75 | ✅85 | ✅68 | split | · | pointerConfiguration OverlaySheet no vertical ScrollView |
| DSZ-03 | Low | ⚠️40 | ⚠️58 | ✅85 | ⚠️60 | ❌70 | ✅68 | **CONFLICT** | · | Magic number 68 in ListView height binding |
| JSN-01 | High | ✅65 | ✅92 | ✅90 | ✅85 | ✅90 | ✅65 | AGREE | · | i.d.authentication accessed without undefined guard |
| JSN-02 | Medium | ⚠️50 | ✅78 | ✅90 | ✅80 | ✅85 | ✅68 | split | · | ws.sendTextMessage() called without checking WebSocket status |
| QCN-01 | Low | ✅55 | ✅78 | ✅90 | ✅75 | ✅80 | ✅55 | AGREE | · | O(n²) contains()-in-loop during custom words file load |
| PC-01 | Medium | ❔45 | ❔39 | ✅70 | ⚠️65 | ✅90 | ❔45 | split | · | countdown.state not set in Prompting state — countdown visible during teleprompting |
| QTD-01 | Medium | ✅65 | ✅78 | ✅85 | ✅80 | ✅85 | ✅65 | AGREE | · | m_spellHighlighter not detached when setDocument(nullptr) |
| QTD-02 | Low-Medium | ❔40 | ✅78 | ✅85 | ⚠️60 | ✅80 | ❔40 | split | · | QQuickTextDocument destroyed without destroyed signal connection |
| OPC-01 | Medium | ⚠️50 | ✅78 | ✅90 | ✅80 | ✅85 | ✅68 | split | · | Right-click toggle desynchronizes velocityIndicator visible/opacity |
| HDR-N01 | Low | ✅60 | ⚠️58 | ✅95 | ✅80 | ✅80 | ✅60 | split | · | promptsession.h not in CMakeLists.txt — SessionModel/DataPoint dead code |
| HDR-N02 | Low | ✅60 | ⚠️58 | ✅95 | ✅80 | ✅80 | ✅60 | split | · | telemetry.h not in CMakeLists.txt — Telemetry dead code |
| IO-N01 | Medium | ⚠️45 | ✅78 | ✅90 | ✅80 | ✅90 | ✅68 | split | · | saveAs() leaves _fileSystemWatcher permanently blocked on open failure |
| IO-N02 | High | ✅50 | ✅84 | ✅85 | ✅85 | ✅95 | ✅50 | AGREE | · | save() constructs QUrl without file:// scheme — broken on non-Windows |
| IO-N03 | Medium | ✅55 | ✅88 | ✅90 | ✅80 | ✅75 | ✅55 | AGREE | · | iossavedialog.mm QFile::write() return value unchecked |
| QML-BND-01 | High | ✅60 | ✅84 | ✅90 | ✅80 | ✅90 | ✅60 | AGREE | · | countdownAnimation.running binding permanently broken after first iteration |
| QML-BND-02 | Medium | ✅55 | ✅78 | ✅90 | ✅80 | ✅85 | ✅55 | AGREE | · | clock.__iteration binding broken by post-decrement in animation handler |
| QML-BND-03 | None (info) | ⚠️40 | ⚠️58 | ✅95 | ❌85 | ❌70 | ❌72 | **CONFLICT** | · | ReadRegionOverlay onDestruction — harmless dead code |
| WSM-N01 | High | ✅60 | ✅84 | ✅85 | ✅80 | ✅80 | ✅60 | AGREE | · | Synchronous QImage::load() from HTTP blocks WASM main thread |
| WSM-N02 | Low | ✅60 | ✅78 | ✅90 | ✅80 | ✅85 | ✅60 | AGREE | · | WASM preventSleep() falls through to desktop #else — always returns false |
| QRC-N01 | Low | ❔45 | ✅92 | ✅95 | ✅80 | ✅95 | ❔45 | split | · | icons.qrc contains duplicate \<file\> entry |
| QRC-N02 | Low | ⚠️45 | ⚠️58 | ✅90 | ✅80 | ✅85 | ✅68 | split | · | Four .qrc files are dead code — never referenced by CMakeLists.txt |
| CMAKE-N01 | Low | ⚠️45 | ⚠️58 | ❔60 | ✅80 | ✅70 | ❌72 | **CONFLICT** | · | WASM build excludes TelemetryPage.qml and RemotePage.qml |
| OOB-N01 | Medium | ⚠️50 | ✅78 | ✅90 | ✅80 | ✅90 | ✅68 | split | · | MarkersModel::data() — m_data.at() without row < rowCount() guard |
| OOB-N02 | Medium | ⚠️45 | ✅78 | ✅90 | ✅80 | ✅85 | ✅68 | split | · | SessionModel::data() — same missing row bounds guard |
| OOB-N03 | Low | ⚠️50 | ✅78 | ✅85 | ⚠️60 | ❌80 | ⚠️50 | **CONFLICT** | · | alignment() fetches textCursor() twice — stale cursor race |
| I18N-N01 | Low | ⚠️40 | ⚠️58 | ✅80 | ✅75 | ✅70 | ⚠️50 | split | · | Stale source-location line numbers in all 20 .ts files |
| I18N-N02 | Low | ⚠️40 | ⚠️58 | ✅80 | ✅75 | ✅70 | ⚠️50 | split | · | Vanished translation entries not purged across 13 language files |
| STR-N01 | High | ✅70 | ✅84 | ✅90 | ✅85 | ✅95 | ✅70 | AGREE | · | main.cpp:158 QLatin1String iterator-pair UB from two unrelated string literals |
| NOTIFY-01 | Medium | ✅75 | ✅78 | ✅95 | ✅80 | ✅95 | ✅75 | AGREE | · | setAutoReload doesn't emit autoReloadChanged NOTIFY signal |
| NOTIFY-02 | Low | ✅55 | ✅78 | ⚠️85 | ✅80 | ✅85 | ✅55 | split | · | availableDictionariesChanged NOTIFY signal never emitted |
| MIX-01 | Low | ⚠️40 | ✅78 | ✅90 | ✅75 | ✅70 | ⚠️50 | split | · | spellchecker.cpp:98 size_t→int narrowing in languages() reserve |
| ENUM-01 | Medium | ⚠️45 | ✅78 | ✅90 | ✅80 | ✅85 | ✅68 | split | · | documenthandler.cpp:1108 updateContents switch no default — silent data loss |
| DPI-01 | Medium | ⚠️40 | ⚠️58 | ✅80 | ⚠️65 | ✅85 | ✅68 | split | · | TimerClock.qml:127 devicePixelRatio in raw arithmetic with magic multiplier |
| DPI-02 | Low | ⚠️45 | ⚠️58 | ✅85 | ✅75 | ❌75 | ✅68 | **CONFLICT** | · | MarkersDrawer.qml:37 drawer minimumWidth hardcoded to 260px |
| DPI-03 | Low | ⚠️45 | ⚠️58 | ✅90 | ✅75 | ❌75 | ✅68 | **CONFLICT** | · | Find.qml:38 searchBarWidth:724 hardcoded in px |
| DPI-04 | Medium | ✅60 | ⚠️58 | ✅90 | ✅80 | ✅80 | ✅60 | split | · | InputsOverlay.qml:33 height:680 hardcoded |
| GEO-01 | Low | ⚠️45 | ⚠️58 | ✅80 | ✅75 | ❌80 | ✅68 | **CONFLICT** | · | main.qml initial 728px height too large for 1366x768 laptops |
| GEO-02 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅80 | ✅85 | ✅68 | split | · | main.qml persists x/y/width/height with zero validation |
| GEO-03 | Low | ⚠️40 | ⚠️58 | ✅90 | ✅75 | ✅70 | ✅68 | split | · | +android/main.qml no minimumWidth/minimumHeight |
| UNIT-01 | High | ⚠️55 | ✅84 | ✅95 | ✅80 | ✅95 | ✅68 | split | · | ProgressIndicator.qml:46 Units.ShortDuration with no Kirigami import |
| UNIT-02 | High | ⚠️55 | ✅84 | ✅95 | ✅80 | ✅95 | ✅68 | split | · | PrompterView.qml 7x Units.ShortDuration with no Kirigami import |
| UNIT-03 | Medium | ⚠️50 | ✅78 | ✅95 | ✅75 | ✅90 | ✅68 | split | · | PrompterBackground.qml:160 Units.LongDuration no Kirigami import |
| UNIT-04 | Medium | ⚠️50 | ✅78 | ✅95 | ✅75 | ✅90 | ✅68 | split | · | Flip.qml:34,41 two Units.LongDuration no Kirigami import |
| UNIT-05 | Low | ⚠️50 | ✅78 | ✅95 | ✅75 | ✅90 | ✅68 | split | · | pointer_0.qml:72 Units.VeryLongDuration no Kirigami import |
| UNIT-06 | Medium | ⚠️50 | ✅78 | ✅95 | ⚠️65 | ✅90 | ✅68 | split | · | Find.qml:92 Units.ShortDuration with namespaced Kirigami import |
| UNIT-07 | Medium | ⚠️50 | ✅78 | ✅90 | ⚠️65 | ✅90 | ✅68 | split | · | ReadRegionOverlay.qml 3x Units.ShortDuration with namespaced import |
| AR-01 | Low | ⚠️45 | ✅78 | ✅75 | ⚠️60 | ✅75 | ⚠️50 | split | · | PrompterView.qml:53-58 Rotation debug feature clips on extreme aspect ratios |
| SAFE-01 | Medium | ⚠️45 | ⚠️58 | ✅80 | ✅80 | ✅75 | ✅68 | split | · | +android/main.qml zero safe area insets |
| SAFE-02 | Medium | ⚠️45 | ⚠️58 | ✅80 | ✅75 | ✅75 | ✅68 | split | · | ReadRegionOverlay screenMiddle ignores notch/status bar height |
| SET-01 | High | ⚠️45 | ✅84 | ✅90 | ⚠️65 | ✅90 | ⚠️50 | split | · | macOS/iOS: QSettings split across two preference domains |
| SET-02 | High | ❔45 | ✅84 | ✅90 | ✅80 | ✅90 | ❔45 | split | · | factoryReset() incomplete on macOS/iOS — domain-path settings survive |
| SET-03 | Low | ⚠️50 | ✅78 | ✅85 | ✅75 | ❌75 | ❌72 | **CONFLICT** | · | QString "true" used as default for boolean QSettings value |
| SET-04 | Low | ⚠️45 | ✅78 | ✅85 | ✅75 | ❌75 | ⚠️50 | **CONFLICT** | · | spellCheckLanguages read without explicit default value |
| INV-N01 | Medium | ⚠️50 | ✅78 | ✅85 | ✅80 | ✅85 | ✅68 | split | · | QmlUtil::r() stores QML-owned QQuickItemGrabResult raw pointer — use-after-free |
| CMAKE-NEW-01 | Low | ⚠️45 | ✅78 | ✅90 | ✅75 | ✅80 | ✅68 | split | · | Remote.qml exists on disk but never listed in QML_FILES |
| CMAKE-NEW-02 | Medium | ✅55 | ✅92 | ✅90 | ✅80 | ✅90 | ✅55 | AGREE | · | Duplicate install() of appdata.xml/desktop in root and src/CMakeLists.txt |
| CMAKE-NEW-03 | Medium | ✅55 | ✅78 | ✅90 | ✅80 | ✅85 | ✅55 | AGREE | · | find_package(KF6Crash ... COMPONENTS) — COMPONENTS keyword with zero names |
| CMAKE-NEW-04 | Medium | ✅60 | ✅78 | ✅90 | ✅80 | ✅85 | ✅60 | AGREE | · | execute_process uses CMAKE_PREFIX_PATH (list) as scalar — broken command |
| DLG-N01 | High | ✅60 | ✅84 | ✅90 | ✅85 | ✅95 | ✅60 | AGREE | · | document.modified=false set BEFORE saveAs() — failed save loses unsaved flag |
| DLG-N02 | High | ✅65 | ✅84 | ✅95 | ✅85 | ✅95 | ✅65 | AGREE | · | onError handler clears document.modified on save failure |
| DLG-N03 | Low | ⚠️45 | ✅78 | ✅90 | ✅75 | ✅80 | ✅68 | split | · | errorDialog MessageDialog has no title |
| DLG-N04 | Medium | ✅60 | ✅78 | ✅90 | ✅80 | ✅90 | ✅60 | AGREE | · | load() silently fails with no notification when file missing or unreadable |
| DLG-N05 | Medium | ✅55 | ✅78 | ✅90 | ✅80 | ✅85 | ✅55 | AGREE | · | loadFromNetworkFinihed() silently ignores empty response |
| DLG-N06 | High | ✅65 | ✅84 | ✅90 | ✅80 | ✅90 | ✅65 | AGREE | · | import() error strings passed as document content via updateContents() |
| DLG-N07 | Low | ⚠️45 | ✅78 | ✅85 | ✅75 | ✅85 | ✅68 | split | · | 5 showPassiveNotification() calls ignore passiveNotifications preference |
| DLG-N08 | Low | ⚠️45 | ✅78 | ✅85 | ✅75 | ✅80 | ✅68 | split | · | 3 save-completion passive notifications lack passiveNotifications guard |
| IMP-NEW-01 | High | ❌65 | ❌76 | ✅90 | ❌80 | ✅95 | ❌65 | **CONFLICT** | · | #include \<qnativeinterface.h\> doesn't exist — breaks Android build |
| IMP-NEW-02 | Low | ⚠️45 | ⚠️58 | ⚠️80 | ⚠️60 | ❌80 | ⚠️50 | split | · | main.cpp:22 #include "qglobal.h" uses quotes + Qt5-era name |
| IMP-NEW-03 | Low | ⚠️40 | ⚠️58 | ✅95 | ✅75 | ❌70 | ⚠️50 | **CONFLICT** | · | main.cpp:38-39 redundant #include \<QtQml/qqml.h\> + #include \<QtQml\> |
| IMP-NEW-04 | Low | ⚠️40 | ⚠️58 | ✅90 | ⚠️60 | ❌75 | ❌72 | **CONFLICT** | · | AboutPage.qml imports Kirigami 2.9 vs 2.11 in all other files |
| IMP-NEW-05 | Low (orphaned QRC, never compiled) | ❔45 | ⚠️58 | ⚠️80 | ⚠️55 | ✅70 | ❔45 | split | · | pointers.qrc RESOURCE_PREFIX conflicts with qt_add_qml_module |
| MA-N01 | Low | ⚠️50 | ✅78 | ✅95 | ✅75 | ✅70 | ✅68 | split | · | overlayMouseArea permanently disabled — dead MouseArea |
| MA-N02 | Low | ✅55 | ✅78 | ✅85 | ✅75 | ✅85 | ✅55 | AGREE | · | textDragArea missing cursorShape — ArrowCursor over IBeamCursor on editor |
| CMT-N01 | Medium | ⚠️40 | ⚠️48 | ✅90 | ✅80 | ✅80 | ⚠️50 | split | · | Justify ToolButton comment says it's commented out — but it's active |
| CMT-N02 | Low | ⚠️35 | ⚠️48 | ✅90 | ✅75 | ❌70 | ⚠️50 | **CONFLICT** | · | Truncated comment in markersmodel.cpp:107-108 |
| CMT-N03 | Medium | ⚠️35 | ⚠️48 | ✅85 | ⚠️60 | ❌70 | ⚠️50 | **CONFLICT** | · | Misleading OpenGL workaround comment — scope of impact understated |
| CMT-N04 | Medium | ❌55 | ❌76 | ✅85 | ⚠️60 | ❌75 | ❌55 | **CONFLICT** | · | Comment masks invalid enum bug — 2 - value produces out-of-range LayoutDirection |
| CMT-N05 | High | ⚠️40 | ⚠️48 | ✅85 | ⚠️60 | ❌75 | ❌72 | **CONFLICT** | · | Missing security warning on QProcess RCE sink (sys://) |
| CMT-N06 | Medium | ⚠️40 | ⚠️48 | ✅80 | ⚠️60 | ❌70 | ❌72 | **CONFLICT** | · | Missing warning: re-entrant toggle() inside Behavior.onRunningChanged |
| CMT-N07 | Medium | ⚠️40 | ⚠️48 | ✅85 | ⚠️60 | ❌70 | ❌72 | **CONFLICT** | · | Missing warning: joinPreviousEditBlock() without beginEditBlock() |
| CMT-N08 | Medium | ✅50 | ⚠️48 | ✅90 | ✅75 | ✅75 | ✅50 | split | · | Entire Telemetry class is dead commented-out shell across 4 files |
| CMT-N09 | Medium | ⚠️40 | ⚠️48 | ✅85 | ⚠️60 | ❌70 | ⚠️50 | **CONFLICT** | · | Commented-out PropertyActions in active loop animation — stale state risk |
| CMT-N10 | Low | ⚠️35 | ⚠️48 | ✅90 | ✅75 | ✅90 | ⚠️50 | split | · | Obsolete Qt 5 qmlRegisterType calls as commented-out cruft |
| REGEX-N01 | Medium | ⚠️45 | ✅78 | ✅85 | ✅75 | ✅95 | ⚠️50 | split | · | All 13 QRegularExpression objects lack isValid() checks |
| REGEX-N02 | Medium | ✅55 | ✅78 | ✅80 | ✅80 | ✅95 | ✅55 | AGREE | · | regex_5 accidentally excludes 15+ HTML5 tags from background-color filtering |
| REGEX-N03 | Low | ✅65 | ✅78 | ✅85 | ✅75 | ✅85 | ✅65 | AGREE | · | Unescaped dot in font-size regex — matches any char instead of decimal |
| HK-N01 | High | ⚠️50 | ⚠️58 | ✅90 | ✅80 | ✅95 | ✅68 | split | · | Missing event.isAutoRepeat guard on main Keys.onPressed |
| HK-N02 | Medium | ✅80 | ✅92 | ✅95 | ✅85 | ✅98 | ✅80 | AGREE | · | Typo Qt.Key_VolumeDowm — "Dowm" instead of "Down" — volume-down hardware key dead |
| HK-N03 | High | ⚠️50 | ⚠️58 | ✅90 | ⚠️65 | ✅90 | ✅68 | split | · | platformName() != "wayland" fails on "wayland-egl" — global hotkeys dead |
| HK-N04 | Medium | ⚠️45 | ⚠️58 | ✅85 | ✅80 | ✅90 | ✅68 | split | · | No auto-repeat guard in key-binding configuration Keys.onPressed |
| HK-N05 | Medium | ✅60 | ✅78 | ✅85 | ✅80 | ✅92 | ✅60 | AGREE | · | Strict === equality on modifiers breaks user keybinds with NumLock |
| HK-N06 | Low | ⚠️45 | ⚠️58 | ✅80 | ✅75 | ✅85 | ✅68 | split | · | isValidInput checks local keybindings only — silent conflict with global hotkeys |
| LDR-N01 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅80 | ✅90 | ✅68 | split | · | InputsOverlay typeof null guard fails — null.item crash on rapid close |
| PARSE-N01 | Medium | ⚠️50 | ✅78 | ✅85 | ✅80 | ✅95 | ✅68 | split | · | insertImageAt() stores image resource with file:// key but looks up via plain path |
| PARSE-N02 | Medium | ✅60 | ✅78 | ✅85 | ✅80 | ✅95 | ✅60 | AGREE | · | MarkersModel::keySearch() hits=1 limits search to first marker only |
| PROP-N01 | High | ✅70 | ✅84 | ✅95 | ✅85 | ✅90 | ✅70 | AGREE | · | on__FullScreenChanged handler casing mismatch — never fires |
| PROP-N02 | Medium | ⚠️55 | ⚠️58 | ✅85 | ✅80 | ✅95 | ⚠️50 | split | · | setCursorPosition → reset() — 12-signal storm, no debounce |
| PROP-N03 | Low | ⚠️45 | ⚠️58 | ✅85 | ⚠️60 | ✅90 | ⚠️50 | split | · | setMarker/setKeyMarker/setMarkerHref silently trigger full document reparse |
| NET-N04 | Medium | ✅60 | ✅78 | ✅90 | ✅75 | ✅90 | ✅60 | AGREE | · | No transfer timeout on any QNetworkRequest |
| NET-N05 | Medium | ✅60 | ✅78 | ✅85 | ✅80 | ✅95 | ✅60 | AGREE | · | loadFromNetwork() hardcodes http:// scheme — never upgrades to HTTPS |
| NET-N06 | Low | ✅65 | ⚠️58 | ✅85 | ✅80 | ✅95 | ✅65 | split | · | loadFromNetwork() validates original URL, not constructed resultingUrl |
| URL-N01 | Medium | ✅60 | ⚠️58 | ✅65 | ✅80 | ✅90 | ✅60 | split | · | reload() constructs file:// URL by string concatenation without encoding |
| DISK-N01 | Low | ✅55 | ✅78 | ✅55 | ✅75 | ✅90 | ✅55 | AGREE | · | saveCustomWordsToDisk() non-atomic write — data loss on power failure |
| INIT-N01 | Medium | ✅90 | ✅78 | ✅90 | ✅80 | ✅95 | ✅90 | AGREE | · | Velocity modifier ComboBox model has 2 entries, switch handles 4 cases |
| INIT-N02 | Low | ✅50 | ✅78 | ✅85 | ✅75 | ✅90 | ✅50 | AGREE | · | Find.qml SearchField placeholderText always empty — no guidance text |
| INIT-N03 | Low | ⚠️40 | ⚠️58 | ⚠️40 | ⚠️60 | ✅85 | ❌72 | **CONFLICT** | · | ReadRegionOverlay screenMiddle uses root.y from cross-file id resolution |
| INIT-N04 | Low | ⚠️40 | ⚠️58 | ❌80 | ⚠️60 | ✅75 | ❌72 | **CONFLICT** | · | PrompterView ShaderEffectSource.sourceItem references prompter id declared later |
| CMB-N01 | Medium | ❔45 | ❔39 | ✅70 | ⚠️65 | ✅95 | ❔45 | split | · | autoReloadSeconds SpinBox from binding circular — clamps to 1 when all-zero |
| CMB-N02 | Low | ❔45 | ❔39 | ✅75 | ⚠️60 | ✅90 | ❔45 | split | · | autoReloadMinutes SpinBox from contains redundant circular self-reference |
| CMB-N03 | Medium | ✅85 | ✅78 | ✅85 | ✅80 | ✅95 | ✅85 | AGREE | · | LanguageSettingsOverlay ListView currentIndex always -1 — wrong indexOf() call |
| VIS-N04 | Low | ⚠️45 | ⚠️58 | ⚠️45 | ⚠️60 | ✅85 | ✅68 | split | · | Countdown crosshair frame renders orphan lines when enabled=false |
| VIS-N05 | Medium | ⚠️50 | ⚠️58 | ✅65 | ✅75 | ✅92 | ✅68 | split | · | velocityDragOverlay blocks all interaction during indicator fade-out (~500ms dead zone) |
| SCRL-N01 | Medium | ❔45 | ❔39 | ⚠️50 | ⚠️60 | ✅80 | ⚠️50 | split | · | __jitterMargin: fractional result from modulus violates 0/1 toggle design |
| SCRL-N02 | Medium | ⚠️50 | ⚠️58 | ✅65 | ✅75 | ✅90 | ✅68 | split | · | __destination typed int truncates real-valued position |
| SCRL-N03 | Medium | ❔45 | ❔39 | ✅55 | ✅75 | ✅95 | ❔45 | split | · | setVelocity() triggers two conflicting scroll animations with intermediate velocity |
| SCRL-N04 | Low | ✅55 | ✅78 | ✅85 | ✅75 | ✅95 | ✅55 | AGREE | · | __speed non-zero when __i=0 and __curvature=0 (Math.pow(0,0)===1) |
| SCRL-N05 | Low | ⚠️50 | ⚠️58 | ❌65 | ⚠️60 | ✅80 | ⚠️50 | **CONFLICT** | · | __speedLimit check is dead logic — always true |
| SCRL-N06 | Low | ⚠️40 | ⚠️58 | ❌60 | ⚠️55 | ✅75 | ❌72 | **CONFLICT** | · | __timeToEnd uses unexplained 2× factor |
| TYP-N01 | Low | ✅85 | ✅92 | ✅90 | ✅75 | ✅98 | ✅85 | AGREE | · | Misspelled method name: loadFromNetworkFinihed (missing 's') |
| TYP-N02 | Low | ✅90 | ✅92 | ✅90 | ✅75 | ✅98 | ✅90 | AGREE | · | Misspelled parameter: withoutFormating (missing 't') |
| TYP-N03 | Low | ⚠️35 | ⚠️58 | ✅80 | ✅75 | ✅90 | ⚠️50 | split | · | Inconsistent `_` vs `m_` member prefix: _markersModel, _fileSystemWatcher |
| TYP-N04 | Low | ⚠️35 | ⚠️58 | ✅75 | ✅70 | ❌85 | ⚠️50 | **CONFLICT** | · | Inconsistent m_ method naming: m_initializeSource — mixed underscore+camelCase |
| TYP-N05 | Low | ✅90 | ✅88 | ✅70 | ✅80 | ✅90 | ✅90 | AGREE | · | Uninitialized member m_documentComesFromNetwork |
| TYP-N06 | Low | ⚠️50 | ⚠️58 | ✅65 | ⚠️65 | ✅85 | ⚠️50 | split | · | 9 getters copy-paste double-textCursor() pattern — null check on stale cursor |
| CAST-N01 | Medium | ✅60 | ✅78 | ✅70 | ✅80 | ✅90 | ✅60 | AGREE | · | setFontCapitalization static_cast with no range validation — reachable from QML |
| IMG-N01 | Medium | ❔45 | ❔39 | ❔30 | ✅80 | ✅95 | ❔45 | split | · | Missing go-previous-symbolic.svg — back-navigation icon blank on Android/Windows |
| ACT-N05 | Medium | ❔45 | ⚠️58 | ⚠️45 | ✅80 | ✅85 | ❔45 | split | · | +windows main.qml Controls Settings submenu missing OBS Settings action |
| ACT-N06 | Low | ⚠️45 | ⚠️58 | ⚠️45 | ✅75 | ✅80 | ✅68 | split | · | +windows main.qml Performance tweaks missing enableBarsSetting |
| ACT-N07 | Medium | ✅60 | ⚠️58 | ✅65 | ✅75 | ✅90 | ✅60 | split | · | namedBookmarkButton: checkable button opens dialog — stale indicator after first click |
| ACT-N08 | Medium (masked — Labs.MenuBar dead per IMP-N01) | ✅55 | ⚠️58 | ⚠️50 | ⚠️65 | ✅75 | ✅55 | split | · | All checkable Labs.MenuItems inherit R2-EDT-03 binding-break pattern |
| RENDER-01 | Medium | ⚠️50 | ✅78 | ✅70 | ✅75 | ✅80 | ✅68 | split | · | ShaderEffectSource prompterShadowSource runs unconditionally — wastes GPU capture when shadows disabled |
| RENDER-02 | Medium | ⚠️50 | ✅78 | ✅70 | ✅75 | ✅80 | ✅68 | split | · | ShaderEffectSource pointerShadowSource runs unconditionally — same pattern |
| TXT-N01 | Low | ⚠️40 | ⚠️58 | ⚠️40 | ✅75 | ✅95 | ⚠️50 | split | · | Find/replace fields missing persistentSelection: true |
| TXT-N02 | Low | ⚠️40 | ✅78 | ✅75 | ✅75 | ❌90 | ✅68 | **CONFLICT** | · | TimerClock default text color #AAA on #131619 — fails WCAG AA contrast |
| PLAT-N01 | Medium | ⚠️45 | ✅78 | ❌85 | ✅80 | ✅75 | ⚠️50 | **CONFLICT** | · | qmlutil.hpp incorrectly excludes QNX from QProcess — run()/restartApplication() silently no-op |
| PLAT-N02 | Medium | ❔40 | ✅78 | ❌85 | ✅80 | ✅70 | ❌72 | **CONFLICT** | · | documenthandler.cpp incorrectly excludes QNX from import() — LibreOffice broken on QNX |
| PLAT-N03 | High | ❔45 | ❔39 | ❌80 | ✅80 | ✅90 | ❔45 | **CONFLICT** | · | Zero Q_OS_TVOS preprocessor guards in C++ despite 19 QML references — build failure |
| DECL-N01 | Low | ⚠️45 | ✅78 | ✅75 | ✅75 | ✅95 | ⚠️50 | split | · | MarkersModel::keySearch — default params in definition but not declaration |
| DECL-N02 | Low | ⚠️40 | ✅78 | ✅85 | ⚠️60 | ✅90 | ⚠️50 | split | · | SessionModel::resetInternalData() missing override keyword and Qt 6 version guard |
| COLOR-01 | Medium | ✅70 | ⚠️58 | ⚠️50 | ✅80 | ✅90 | ✅70 | split | · | ProjectionsManager.qml uses invalid "initial" color — repro of R4-ROOT-02 |
| COLOR-02 | Medium | ⚠️40 | ⚠️58 | ✅75 | ✅75 | ✅90 | ✅68 | split | · | Hardcoded #EED text invisible on light themes — WheelSettingsOverlay |
| COLOR-03 | Low | ⚠️40 | ⚠️58 | ⚠️45 | ⚠️60 | ✅90 | ✅68 | split | · | velocityText ColorAnimation flash: #BBB → #FFF → #CCC jump |
| COLOR-04 | Low | ⚠️45 | ⚠️58 | ✅65 | ⚠️55 | ✅90 | ✅68 | split | · | ReadRegionOverlay ColorAnimation tracks __fillColor that never changes |
| COLOR-05 | Low | ⚠️40 | ⚠️58 | ⚠️40 | ✅70 | ✅85 | ⚠️50 | split | · | Prompter scrollbar gradient hardcodes #CCC/#998/#665 — low contrast on light backgrounds |
| COLOR-06 | Low | ⚠️40 | ⚠️58 | ⚠️40 | ✅70 | ✅85 | ⚠️50 | split | · | Countdown #FFF digits on #333-at-0.48-overlay — insufficient contrast on light backgrounds |
| COLOR-07 | Low | ⚠️55 | ⚠️58 | ✅65 | ✅75 | ✅90 | ⚠️50 | split | · | CSS default stylesheet hardcodes #FFFFFF body text — ignores user text color |
| EVT-N10 | Medium | ❔45 | ⚠️58 | ✅70 | ✅75 | ❌60 | ❔45 | **CONFLICT** | · | Editor Ctrl+Letter shortcuts don't accept event — marker key-search double-fires |
| EVT-N11 | Low | ⚠️45 | ⚠️58 | ❌70 | ✅75 | ❌70 | ✅68 | **CONFLICT** | · | windowStayOnTopButton lacks focusPolicy — unreachable via keyboard |
| EVT-N12 | Low | ⚠️50 | ⚠️58 | ✅60 | ⚠️60 | ⚠️50 | ✅68 | split | · | velocityDragArea and viewport.mouse share z:5 — wheel dispatch ambiguous |
| STATE-N01 | High | ❔45 | ✅84 | ⚠️50 | ✅80 | ❌70 | ❔45 | **CONFLICT** | · | Shadowed Prompting→Editing transition — velocity default never saved |
| STATE-N02 | Medium | ⚠️50 | ✅78 | ✅75 | ✅80 | ✅80 | ✅68 | split | · | Find.toggle() uses !visible instead of !isOpen — can't close during Prompting |
| STATE-N03 | Low | ⚠️50 | ✅78 | ✅65 | ⚠️60 | ✅80 | ✅68 | split | · | Countdown Running restarts dissolveIn unnecessarily — visual dim-to-bright flash |
| STATE-N04 | Low | ❔45 | ✅78 | ✅70 | ⚠️55 | ✅75 | ❔45 | split | · | loop animation cancel() state change overridden by toggle() due to QML batching |
| SIZE-N01 | Medium | ✅60 | ✅78 | ✅80 | ✅75 | ✅95 | ✅60 | AGREE | · | concentricCircles Shape has conflicting anchors.fill + anchors.centerIn |
| SIZE-N02 | Low | ✅55 | ✅78 | ✅75 | ✅70 | ✅65 | ✅55 | AGREE | · | Three Button children of Row have dead anchors.bottom declarations |
| CONST-N01 | Low | ⚠️40 | ⚠️58 | ✅60 | ✅70 | ❌75 | ⚠️50 | **CONFLICT** | · | getMarkerKey() not const — pure reader without side effects |
| CONST-N02 | Low | ⚠️40 | ⚠️58 | ✅60 | ✅70 | ❌75 | ⚠️50 | **CONFLICT** | · | getMarkerHref() not const — identical pattern |
| CONST-N03 | Low | ⚠️40 | ⚠️58 | ✅55 | ✅70 | ❌70 | ⚠️50 | **CONFLICT** | · | MarkersModel::previousMarker(), nextMarker(), keySearch(), binarySearch() not const |
| CONST-N04 | Low | ⚠️40 | ⚠️58 | ✅60 | ✅70 | ❌70 | ⚠️50 | **CONFLICT** | · | GlobalHotkeys::globalShortcutKey(Action) not const — Q_INVOKABLE pure query |
| CONST-N05 | Low | ⚠️40 | ⚠️58 | ✅65 | ✅70 | ❌65 | ⚠️50 | **CONFLICT** | · | Unnecessary copy via const auto instead of const auto& in extendLastMarker |
| SAVE-N01 | Medium | ⚠️55 | ✅78 | ✅70 | ✅80 | ✅80 | ✅68 | split | · | loadFromNetworkFinihed sets m_fileUrl to phantom QTemporaryFile path |
| SAVE-N02 | High | ⚠️50 | ✅84 | ✅75 | ✅80 | ✅85 | ✅68 | split | · | iOS save flow never updates C++ m_fileUrl — file URL perpetually stale |
| SAVE-N03 | Medium | ✅55 | ✅78 | ✅75 | ✅80 | ✅85 | ✅55 | AGREE | · | saveAs() never updates _fileSystemWatcher — watches stale file after save-as |
| SAVE-N04 | Low | ⚠️45 | ✅78 | ✅65 | ✅75 | ✅70 | ⚠️50 | split | · | save() unnecessary QString→std::string→QString round-trip through locale encoding |
| SAVE-N05 | Low | ✅50 | ✅78 | ✅70 | ✅80 | ✅80 | ✅50 | AGREE | · | save() broken on Android content:// URIs — empty filename |
| LOAD-N01 | Medium | ⚠️50 | ✅78 | ✅65 | ✅75 | ✅70 | ✅68 | split | · | TOCTOU race between QFile::exists() and file.open() in load() |
| LOAD-N02 | Low | ⚠️50 | ✅78 | ❌75 | ✅75 | ❌75 | ✅68 | **CONFLICT** | · | reset() emits 12 NOTIFY signals when open() fails but exists() succeeds |
| SHDR-N01 | Medium | ✅65 | ✅78 | ✅85 | ✅75 | ✅90 | ✅65 | AGREE | · | Math.cos/Math.sin used with degrees value — shadow offset diagonal instead of horizontal |
| RAII-N01 | Medium | ⚠️50 | ✅78 | ✅60 | ✅80 | ✅85 | ⚠️50 | split | · | QDrag object never deleteLater'd after exec() — leaks on rejected drags |
| RAII-N02 | Low | ⚠️50 | ⚠️58 | ✅55 | ✅75 | ✅80 | ✅68 | split | · | IosSaveDialog::m_tempDir created unconditionally on all platforms — wasted I/O |
| RAII-N03 | Medium | ⚠️50 | ✅78 | ❌70 | ✅80 | ❌70 | ✅68 | **CONFLICT** | · | QProcess orphan — child process detached on waitForFinished() timeout |
| Z-N01 | Medium | ⚠️45 | ✅78 | ⚠️45 | ⚠️60 | ❌65 | ⚠️50 | **CONFLICT** | · | CursorAutoHide has no explicit z — hover detection fragile against Kirigami internals |
| Z-N02 | Low | ⚠️40 | ✅78 | ⚠️40 | ✅70 | ❌70 | ✅68 | **CONFLICT** | · | Two OverlaySheets have z:1 while nine others have none — inconsistent stacking |
| Z-N03 | Low | ⚠️40 | ✅78 | ⚠️40 | ⚠️55 | ❌60 | ✅68 | **CONFLICT** | · | ComboBox Popup z:103 inside OverlaySheets with z:1 — disconnected layering |
| Z-N04 | Low | ⚠️45 | ✅78 | ✅65 | ⚠️55 | ⚠️50 | ⚠️50 | split | · | PrompterBackground (z:0) renders above viewport.mouse (z:0) — latent input intercept |
| TIME-N01 | Low | ✅60 | ✅78 | ✅85 | ✅70 | ✅90 | ✅60 | AGREE | · | copyrightYear computed then discarded — stale "2020-2026" in About after 2026 |
| XFRM-N01 | Low | ❔45 | ❔39 | ⚠️45 | ⚠️60 | ✅85 | ❔45 | split | · | PrompterView.qml Rotation permanently overridden by PrompterPage.qml |
| API-N01 | Medium | ⚠️50 | ✅78 | ✅65 | ✅75 | ✅80 | ✅68 | split | · | setAlignment() missing null-cursor guard — crash risk with no document |
| API-N02 | Medium | ✅80 | ✅78 | ✅80 | ✅80 | ✅85 | ✅80 | AGREE | · | selectionIsLowerCase NOTIFY signal is wrong — fontCapitalizationChanged, never emitted for case changes |
| API-N03 | Medium | ⚠️50 | ✅78 | ✅75 | ✅75 | ✅85 | ✅68 | split | · | CursorAutoHide.qml unconditionally dereferences pageStack.currentItem.prompter |
| API-N04 | Low | ⚠️35 | ✅78 | ✅65 | ✅70 | ⚠️50 | ✅68 | split | · | setMarker(bool) misleadingly named — sets regular marker, not any marker |
| API-N05 | Low | ⚠️50 | ✅78 | ✅70 | ✅70 | ✅70 | ✅68 | split | · | fileName()/fileType() return fabricated defaults — can't distinguish "no file" from "untitled.html" |
| API-N06 | Low | ✅80 | ⚠️58 | ✅80 | ✅85 | ✅70 | ✅80 | split | · | SystemFontChooserDialog::show() calls setText() on same label twice — dead code |
| API-N07 | Low | ✅55 | ✅78 | ✅75 | ⚠️65 | ✅90 | ✅55 | split | · | SpellChecker::encode() fallback says "Latin-1" but calls toLocal8Bit() |
| ARC-01 |  | ⚠️35 | ⚠️48 | ❌50 | ⚠️55 | ✅60 | ⚠️50 | **CONFLICT** | · | Velocity physics engine entirely in QML (~20 readonly property bindings) |
| ARC-02 |  | ⚠️35 | ⚠️48 | ❌50 | ⚠️55 | ✅60 | ⚠️50 | **CONFLICT** | · | Arc-03 Search/replace state machine fully in QML (50+ lines) |
| ARC-03 |  | ⚠️35 | ⚠️48 | ❌50 | ⚠️55 | ✅60 | ⚠️50 | **CONFLICT** | · | OBS WebSocket v5 protocol in QML — opcode dispatch, auth, subscription |
| ARC-04 |  | ⚠️40 | ⚠️48 | ❌50 | ⚠️55 | ✅60 | ⚠️50 | **CONFLICT** | · | DocumentHandler is 2295-line god class spanning file I/O, network, HTML filtering, markers, spellcheck, drag-drop, images, search, undo, clipboard, sleep prevention, font dialog |
| ARC-05 |  | ⚠️35 | ⚠️48 | ❌50 | ⚠️55 | ✅60 | ⚠️50 | **CONFLICT** | · | Prompter.qml is 3139-line god component spanning velocity, state machine, keyboard, WebSocket, markers, spellcheck UI, file dialogs, WYSIWYG toggle, shadows |
| ARC-06 |  | ⚠️35 | ⚠️48 | ❌50 | ⚠️50 | ✅60 | ⚠️50 | **CONFLICT** | · | qmlutil.hpp is utility grab-bag with 10+ unrelated functions |
| KEY-N01 | Medium | ❔45 | ❔39 | ✅70 | ✅75 | ✅90 | ❔45 | split | · | Named marker key binding silently discards all modifier information |
| CLI-N01 | Medium | ⚠️50 | ✅78 | ⚠️55 | ⚠️65 | ✅90 | ✅68 | split | · | --version flag non-functional — version string empty when parser processes |
| DPR-N01 | Medium | ✅55 | ✅78 | ✅70 | ✅75 | ✅80 | ✅55 | AGREE | · | Prompter.qml uses Screen.devicePixelRatio (global) instead of screen.devicePixelRatio (window) |
| SCALE-N01 | Medium | ⚠️50 | ✅78 | ✅65 | ✅75 | ✅80 | ✅68 | split | · | Right pointer xScale: -1 mirrors text pointers — backwards/unreadable text |
| ORIENT-N01 | Low | ⚠️45 | ⚠️58 | ✅60 | ⚠️55 | ✅70 | ✅68 | split | · | TimerClock binary width>height orientation creates sharp 2x font jump at 1:1 |
| BIND-N01 | Low | ⚠️50 | ✅92 | ✅65 | ⚠️55 | ❌70 | ✅68 | **CONFLICT** | · | contentWidth undefined for Shape/Image pointer types — transform origin silently wrong |
| STR-CNV | Low | ⚠️45 | ✅78 | ✅60 | ✅75 | ❌60 | ⚠️50 | **CONFLICT** | · | 5 defensive validation gaps: toInt() without ok flag in getMarkerKey, parse(×2), setFontSize, and 32 hotkey reads |
| SHADOW-N03 | High | ✅70 | ✅84 | ❌75 | ✅75 | ✅95 | ✅70 | **CONFLICT** | · | id: stopwatch shadows property bool stopwatch — timersEnabled always true |
| SHADOW-N04 | Low | ⚠️50 | ✅78 | ✅65 | ⚠️60 | ❌65 | ✅68 | **CONFLICT** | · | id: frame shadows property bool frame — latent hazard |
| LINK-N01 | High | ✅65 | ✅84 | ✅80 | ✅80 | ✅85 | ✅65 | AGREE | · | Qt::Network not linked on iOS static build — unresolved symbols |
| LINK-N02 | High | ✅65 | ✅84 | ✅80 | ✅80 | ✅85 | ✅65 | AGREE | · | Qt::Network not linked on WASM static build — same as LINK-N01 |
| LINK-N03 | Medium | ⚠️50 | ✅78 | ✅85 | ✅75 | ✅80 | ✅68 | split | · | Qt::WebSockets found as REQUIRED but never explicitly linked |
| LINK-N04 | Medium | ❔45 | ✅78 | ❌85 | ✅75 | ✅75 | ❔45 | **CONFLICT** | · | KF6::GlobalAccel find_package/link mismatch on Haiku |
| COMP-N01 | Low | ✅55 | ✅92 | ✅95 | ✅75 | ✅80 | ✅55 | AGREE | · | Case-sensitive duplicate detection in setLanguages() |
| COMP-N02 | Medium | ✅50 | ✅78 | ✅90 | ✅80 | ✅85 | ✅50 | AGREE | · | Case-sensitive suffix check misses mixed-case extensions — silent format loss |
| COMP-N03 | Low | ⚠️50 | ✅78 | ✅95 | ⚠️60 | ✅70 | ⚠️50 | split | · | regularMarker() same double-textCursor anti-pattern as LOG-07 |
| LBL-N01 | Medium | ⚠️45 | ⚠️58 | ✅70 | ✅70 | ✅90 | ⚠️50 | split | · | All 12 Sliders in EditorToolbar missing Layout.fillWidth: true — cramped |
| LBL-N02 | Medium | ⚠️40 | ⚠️52 | ✅80 | ✅70 | ✅80 | ❌72 | **CONFLICT** | · | 11 Labels with Layout.bottomMargin: -14 — undefined behavior, overlap risk |
| LBL-N03 | Low | ⚠️40 | ⚠️58 | ✅85 | ⚠️55 | ✅70 | ✅68 | split | · | PrompterView 3× height overflow in theforce debug mode |
| LAY-N01 | Low | ⚠️45 | ⚠️58 | ❔50 | ✅70 | ✅80 | ⚠️50 | split | · | 10 Labels with Layout.margins but inside MouseArea, not direct layout child — dead |
| LAY-N02 | Low | ⚠️40 | ⚠️58 | ❔50 | ✅70 | ✅80 | ⚠️50 | split | · | WheelSettingsOverlay explanation text constrained to single column in 2-column GridLayout |
| DLG-N10 | Medium | ⚠️45 | ✅78 | ✅90 | ✅75 | ✅85 | ✅68 | split | · | TimerClock ColorDialog selectedColor never initialized from persisted settings |
| DLG-N11 | Low | ⚠️45 | ✅78 | ✅90 | ✅75 | ✅70 | ✅68 | split | · | PrompterPage ColorDialogs — dead acceptedColor property binding |
| QPROP-N02 | Medium | ❌50 | ❌76 | ✅95 | ✅75 | ✅80 | ❌50 | **CONFLICT** | · | comesFromNetwork Q_PROPERTY missing WRITE clause |
| PATH-N01 | Medium | ⚠️50 | ✅78 | ✅85 | ✅80 | ✅80 | ✅68 | split | · | save() fragile percent-encoding round-trip — broken for UNC paths |
| PATH-N02 | Medium | ✅60 | ✅78 | ✅95 | ✅80 | ✅85 | ✅60 | AGREE | · | reload() constructs file:// URL via raw string concat — #/? in filenames break URL |
| MOB-01 | Medium | ✅70 | ✅92 | ✅80 | ✅80 | ✅90 | ✅70 | AGREE | · | Android: projectionManager undefined — 3 unguarded reference sites |
| MOB-02 | Medium | ⚠️50 | ✅78 | ✅95 | ✅80 | ✅80 | ✅68 | split | · | No +ios/ QML selector — iOS inherits base main.qml with desktop-only components |
| MOB-03 | Medium | ⚠️50 | ✅92 | ✅95 | ✅75 | ✅85 | ✅68 | split | · | iOS: IosSaveDialog silently hangs QML caller when temp dir invalid |
| MOB-04 | Low | ✅65 | ✅78 | ✅95 | ✅75 | ✅90 | ✅65 | AGREE | · | Android: restartApplication() quits without restart |
| MOB-05 | Low | ✅85 | ✅78 | ✅95 | ✅80 | ✅85 | ✅85 | AGREE | · | Android: Missing INTERNET permission in manifest |
| MOB-06 | Low | ✅60 | ✅78 | ✅85 | ✅75 | ✅80 | ✅60 | AGREE | · | Android: PrompterPage display delegate Component.onCompleted references projectionManager — startup TypeError |
| MENU-N01 | Medium | ✅55 | ⚠️58 | ✅95 | ✅75 | ✅75 | ✅55 | split | · | contextMenu.popup(this) missing click coordinates — menu at wrong position |
| MENU-N02 | Medium | ✅60 | ⚠️58 | ✅95 | ✅80 | ✅90 | ✅60 | split | · | Mobile "Add to dictionary" missing %1 placeholder — word never shown |
| MENU-N03 | Medium | ⚠️55 | ⚠️58 | ✅95 | ✅75 | ✅85 | ✅68 | split | · | Text alignment menu RTL swap: labels swap but actions don't |
| MENU-N04 | Low | ✅50 | ⚠️58 | ✅75 | ✅70 | ✅70 | ✅50 | split | · | Trailing empty MenuSeparator at end of mobile context menu |
| MENU-N05 | Low | ⚠️45 | ⚠️58 | ✅95 | ✅70 | ✅70 | ✅68 | split | · | "Redo" context menu item missing & accelerator |
| MENU-N06 | Low | ⚠️50 | ⚠️58 | ⚠️70 | ⚠️60 | ✅85 | ✅68 | split | · | Paste behavior inconsistent between context menu and global Edit menu |
| DBG-N01 | Medium | ✅60 | ⚠️58 | ✅95 | ✅75 | ✅90 | ✅60 | split | · | OBS WebSocket auth challenge+salt logged to console in release builds |
| DBG-N02 | Low | ✅55 | ⚠️58 | ✅95 | ✅70 | ✅80 | ✅55 | split | · | Velocity debug logging active in production |
| DBG-N03 | Low | ⚠️45 | ⚠️52 | ⚠️60 | ⚠️60 | ❌60 | ✅68 | **CONFLICT** | · | Latent debug state leak: pointers/debug Setting persists Guides checkbox |
| DBG-N04 | Low | ✅60 | ⚠️58 | ✅90 | ✅70 | ✅80 | ✅60 | split | · | qDebug() in namedMarker()/setMarker() active in release |
| WARN-N01 | Low | ⚠️40 | ⚠️58 | ✅80 | ✅75 | ✅70 | ✅68 | split | · | SpellHighlighter::isEnabled() — dead code, never called |
| WARN-N02 | Low | ✅60 | ⚠️58 | ✅85 | ✅75 | ✅70 | ✅60 | split | · | SpellChecker::addWord() — dead public API, never called |
| WARN-N03 | Low | ⚠️45 | ⚠️58 | ✅90 | ✅70 | ✅70 | ⚠️50 | split | · | quint64→int implicit narrowing in nextMarker()/previousMarker() |
| WARN-N04 | Low | ✅55 | ⚠️58 | ✅95 | ✅70 | ✅70 | ✅55 | split | · | QProcess::startDetached() bool return silently ignored |
| FLOW-N01 | Medium | ✅65 | ✅78 | ✅90 | ✅80 | ✅90 | ✅65 | AGREE | · | setKeyMarker() calls setAnchor("#") — const char*→bool conversion, href never set |
| FLOW-N02 | Medium | ❔45 | ⚠️58 | ✅90 | ✅75 | ✅85 | ❔45 | split | · | increaseVelocity()/decreaseVelocity() skip velocity change when paused |
| DEF-N01 | Medium | ❌65 | ❌76 | ✅90 | ✅75 | ✅75 | ❌65 | **CONFLICT** | · | Flickable.flicking undefined in Qt 6 — wrong cursor during momentum scroll |
| DEF-N02 | Medium | ⚠️50 | ⚠️58 | ✅95 | ✅75 | ✅75 | ✅68 | split | · | DropArea internalDrag always false — internal drag handler dead code |
| TMR-N01 | Medium | ⚠️50 | ⚠️58 | ✅95 | ✅75 | ✅85 | ✅68 | split | · | resetBackground Timer not stopped when new background loaded — race erases new image |
| TMR-N02 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅80 | ✅85 | ✅68 | split | · | Windows onFrameSwapped missing qmlutil.r(p) — per-frame grab result leak |
| CMAKE-N05 | Low | ✅55 | ✅78 | ✅85 | ✅75 | ✅80 | ✅55 | AGREE | · | foreach(file IN LISTS icon_files doc) — "doc" never defined |
| PRE-N01 | Low | ⚠️55 | ⚠️58 | ⚠️75 | ❌80 | ✅85 | ✅68 | **CONFLICT** | · | Preprocessor uses `or` instead of `\|\|` in 6 #if directives — MSVC build break |
| CNTD-N01 | Low | ⚠️50 | ⚠️58 | ✅85 | ⚠️60 | ✅75 | ✅68 | split | · | Countdown Running: dissolveIn and dissolveOut compete for same opacity when __iterations===__disappearWithin===1 |
| QF-N02 | Low | ⚠️45 | ⚠️58 | ✅85 | ✅70 | ✅70 | ✅68 | split | · | QDir::entryList missing QDir::Readable in availableDictionaries() |
| QF-N03 | Low | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅75 | ✅68 | split | · | TOCTOU: QFile::exists() → QFile::copy() in resource cache extraction |
| TXT-CRIT | Critical | ❔45 | ❔39 | ✅85 | ✅80 | ✅95 | ❔45 | split | · | Plain 'v'/'V' keypress silently consumed — letter 'v' cannot be typed |
| TXT-N03 | Medium | ✅80 | ✅78 | ✅90 | ✅80 | ✅90 | ✅80 | AGREE | · | Toolbar paste and Edit menu paste bypass HTML sanitization |
| TXT-N04 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅75 | ✅80 | ✅68 | split | · | goToNextMarker() temporarily sets cursorPosition=-1 — corrupts cursor state |
| INT-N01 | Low | ⚠️45 | ⚠️58 | ✅90 | ✅70 | ✅70 | ⚠️50 | split | · | quint64→int narrowing at DocumentHandler→MarkersModel boundary (4 sites) |
| INT-N02 | Medium | ⚠️40 | ✅78 | ✅90 | ⚠️60 | ✅85 | ⚠️50 | split | · | replaceAll() returns long — 32-bit overflow on Windows x64 |
| INT-N03 | Low | ⚠️40 | ⚠️58 | ✅80 | ✅70 | ✅70 | ⚠️50 | split | · | 6 qsizetype→int narrowing conversions across models and loops |
| URL-N03 | Medium | ✅55 | ⚠️58 | ✅90 | ✅80 | ✅80 | ✅55 | split | · | Network-loaded HTML lacks base URL — relative resources broken |
| URL-N04 | Low | ✅60 | ⚠️58 | ✅90 | ✅75 | ✅85 | ✅60 | split | · | loadFromNetwork() validates wrong URL instance |
| URL-N05 | Medium | ✅55 | ⚠️58 | ✅90 | ✅80 | ✅85 | ✅55 | split | · | openFromRemote() blindly prepends http:// to non-HTTP schemes |
| PERF-N01 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅75 | ⚠️50 | split | · | onFrameSwapped calls markerCompare() unconditionally — wasted JS call every frame |
| PERF-N02 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅80 | ✅68 | split | · | RecentDocuments._load() blocks startup with N synchronous createObject() calls |
| PERF-N03 | Low | ⚠️50 | ⚠️58 | ✅85 | ⚠️60 | ✅75 | ⚠️50 | split | · | velocityDragOverlay hot-loop calls velocity functions without throttling |
| ERR-N01 | Medium | ✅60 | ✅78 | ✅90 | ✅75 | ✅80 | ✅60 | AGREE | · | removeCustomWord() silently drops dictionary languages on partial reload failure |
| ERR-N02 | Medium | ⚠️55 | ⚠️58 | ✅95 | ✅75 | ✅80 | ✅68 | split | · | insertImageAt() async callback silently discards 3 failure modes |
| PATH-N03 | High | ❔45 | ✅84 | ✅90 | ✅75 | ⚠️65 | ❔45 | split | · | Wrong ../fonts/ depth in +android and +windows FontLoader paths |
| SIG-N03 | Low | ⚠️40 | ✅78 | ✅75 | ✅70 | ✅70 | ⚠️50 | split | · | MessageDialog.onButtonClicked declares unused second parameter role |
| QOBJ-N01 | Low | ⚠️40 | ✅78 | ✅85 | ✅70 | ✅60 | ⚠️50 | split | · | QmlUtil missing constructor with parent parameter |
| TAB-N01 | Medium | ⚠️50 | ✅78 | ⚠️60 | ✅75 | ✅80 | ✅68 | split | · | PointerSettings TabButton onClicked skips currentIndex assignment |
| REGEX-CRIT-01 | High | ❔45 | ❔39 | ✅85 | ✅80 | ✅90 | ❔45 | split | · | regex_4 destroys <body> tag — removes opening tag instead of color attributes |
| REGEX-CRIT-02 | High | ✅55 | ✅84 | ✅95 | ✅85 | ✅90 | ✅55 | AGREE | · | searchRegEx.setPattern() from user input — isValid() never called |
| REGEX-N04 | Medium | ⚠️50 | ✅78 | ✅90 | ✅80 | ✅85 | ✅68 | split | · | ReDoS — user-supplied regex has no length limit, timeout, or backtracking guard |
| REGEX-N05 | Low | ✅70 | ✅78 | ✅85 | ✅70 | ✅80 | ✅70 | AGREE | · | regex_0 and regex_3 use . (any-char) instead of \. (literal dot) in decimal matching |
| REGEX-N06 | Medium | ✅55 | ✅78 | ✅90 | ✅75 | ✅85 | ✅55 | AGREE | · | imgSrcRegex captures wrong src when data-src follows real src |
| VCI-N01 | Low | ⚠️40 | ⚠️48 | ✅95 | ✅70 | ✅70 | ⚠️50 | split | · | At-end action buttons use inconsistent font scaling (1/1.5 vs 1/1.75) in same group |
| VCI-N02 | Low | ⚠️40 | ⚠️48 | ✅95 | ✅70 | ✅70 | ⚠️50 | split | · | upperControls and bottomControls fade to different opacity levels during Prompting |
| VCI-N03 | Low | ⚠️40 | ⚠️48 | ⚠️70 | ⚠️55 | ✅90 | ✅68 | split | · | Hardcoded divider/separator/border colors (#292929, #606060, #808080) break theme adaptation |
| UTF-N01 | Medium | ⚠️50 | ✅78 | ✅90 | ✅75 | ✅90 | ✅68 | split | · | text.truncate(64) can split UTF-16 surrogate pairs — corrupted display |
| AND-CRIT-01 | Critical | ✅85 | ✅84 | ✅95 | ✅85 | ✅95 | ✅85 | AGREE | · | Missing android.permission.INTERNET — all network silently fails |
| AND-HIGH-01 | High | ⚠️50 | ⚠️58 | ✅80 | ✅80 | ✅80 | ✅68 | split | · | Android back button doesn't dismiss overlays/drawers before close |
| AND-HIGH-02 | High | ✅60 | ✅84 | ✅90 | ✅80 | ✅90 | ✅60 | AGREE | · | Android screen never sleeps after prompter use |
| AND-HIGH-03 | High | ✅65 | ✅84 | ✅95 | ✅80 | ✅95 | ✅65 | AGREE | · | factoryReset() quits Android app without restarting |
| AND-MED-01 | Medium | ⚠️45 | ⚠️58 | ✅95 | ✅75 | ✅95 | ✅68 | split | · | Missing intent-filter for opening files from other apps |
| CLP-N01 | Medium | ⚠️50 | ✅78 | ⚠️70 | ✅75 | ✅85 | ✅68 | split | · | Copy/Cut exports unfiltered HTML to system clipboard |
| CLP-N02 | Medium | ⚠️50 | ⚠️58 | ✅95 | ✅75 | ✅90 | ✅68 | split | · | DropArea external drop never calls drop.accept() |
| CLP-N03 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅90 | ✅68 | split | · | DropArea external drop: URLs consumed preferentially — text silently lost |
| SWT-N01 | Medium | ✅60 | ✅78 | ✅95 | ✅75 | ✅90 | ✅60 | AGREE | · | OBS WebSocket Switch checked binding broken on first toggle |
| IMH-SYS | Medium | ⚠️40 | ⚠️58 | ⚠️65 | ✅75 | ✅95 | ❌72 | **CONFLICT** | · | Systemic absence of inputMethodHints on ALL TextFields (16 sites) |
| EKA-SYS | Low | ⚠️40 | ⚠️58 | ⚠️65 | ✅70 | ✅90 | ❌72 | **CONFLICT** | · | Systemic absence of EnterKeyAction on ALL TextFields (7 sites) |
| WINDOW-N01 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅75 | ✅85 | ✅68 | split | · | Projection windows not closed on main window close — orphaned on Linux |
| GSW-N01 | Medium | ⚠️45 | ⚠️58 | ✅90 | ✅70 | ✅80 | ✅68 | split | · | MarkersDrawer SwipeListItem navigates on swipe — gesture conflict on touch |
| GSW-N02 | Low | ❔45 | ❔39 | ✅85 | ⚠️60 | ✅80 | ❔45 | split | · | Flickable onDragStarted uses stale __iBackup after non-prompting drags |
| LVW-N01 | Low | ⚠️45 | ⚠️58 | ✅85 | ✅70 | ✅70 | ✅68 | split | · | InputsOverlay.qml ListView currentIndex: PointerSettings.States.Arrow — copy-paste error |
| META-N01 | Low | ⚠️45 | ⚠️58 | ✅95 | ✅70 | ✅75 | ✅68 | split | · | QMetaObject::invokeMethod return value unchecked — silent failure on WASM |
| LOG-N04 | Low | ❌70 | ✅78 | ✅90 | ✅70 | ❌90 | ❌70 | **CONFLICT** | · | qWarning("reloading") fires unconditionally — misleading when URL mismatches |
| LOG-N05 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅80 | ✅68 | split | · | Q_UNREACHABLE() in m_setGlobalShortcut() — UB in release on new enum value |
| LOG-N06 | Medium | ✅70 | ✅78 | ✅95 | ✅75 | ✅90 | ✅70 | AGREE | · | No error log when saveAs() write/flush fail — silent data loss |
| LOG-N07 | Medium | ✅55 | ⚠️58 | ✅95 | ✅75 | ✅90 | ✅55 | split | · | No error log in loadFromNetworkFinihed() — silent bad-data load |
| FONT-N01 | Medium | ⚠️45 | ❔39 | ✅95 | ✅75 | ✅70 | ❌72 | **CONFLICT** | · | font.family: "Monospace" never resolves — no such font on any OS |
| FONT-N02 | Low | ✅65 | ⚠️58 | ✅95 | ✅70 | ✅90 | ✅65 | split | · | FontLoader id typo: westernSeriousSansfFont — stray 'f' in "Sans" |
| XML-N01 | Medium | ✅55 | ✅92 | ✅90 | ✅75 | ✅90 | ✅55 | AGREE | · | android:background="#303030" invalid on \<activity\> — silently ignored |
| CMAKE-N02 | Low | ✅55 | ✅78 | ✅95 | ✅70 | ✅90 | ✅55 | AGREE | · | INTERFACE_LINK_LIBRARIES on executable target — no-op |
| CMAKE-N03 | Medium | ⚠️50 | ❌76 | ✅85 | ✅75 | ✅80 | ✅68 | **CONFLICT** | · | qt_wrap_ui conflicts with global AUTOUIC — double UI processing |
| CMAKE-N04 | Medium | ✅55 | ✅78 | ✅90 | ✅75 | ✅90 | ✅55 | AGREE | · | Relative ../build path in install rules — out-of-tree build failure |
| SETUP-N01 | Medium | ❔40 | ❔39 | ✅95 | ✅75 | ✅90 | ❔40 | split | · | setup.sh uses windeployqt.exe (Qt 5) — should be windeployqt6.exe (Qt 6) |
| POP-N01 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅90 | ✅68 | split | · | ESC cascade missing dictionariesSheet — undismissable by keyboard |
| POP-N02 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅90 | ✅68 | split | · | ESC cascade missing customWordsSheet — undismissable by keyboard |
| POP-N03 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅75 | ✅90 | ✅68 | split | · | ESC cascade missing obsConfiguration — undismissable by keyboard despite alias |
| POP-N04 | Medium | ✅65 | ⚠️58 | ✅95 | ✅75 | ✅90 | ✅65 | split | · | CountdownConfiguration SpinBoxes use focus: true (JS label) instead of focus = true |
| RND-N01 | Low | ⚠️50 | ⚠️58 | ✅95 | ✅70 | ❌70 | ✅68 | **CONFLICT** | · | forceQtTextRenderer dead on Apple platforms — unconditionally uses NativeRendering |
| RND-N02 | Low | ⚠️45 | ⚠️58 | ✅85 | ✅70 | ✅85 | ✅68 | split | · | Missing smooth: true on background Image — aliased upscale |
| RND-N03 | Low | ⚠️50 | ⚠️58 | ✅85 | ✅70 | ✅80 | ✅68 | split | · | Missing smooth: true on projection Image — aliased text on external displays |
| ST-N02 | Medium | ✅50 | ⚠️58 | ✅95 | ✅70 | ✅85 | ✅50 | split | · | Dead overlay.state PropertyChanges — overlay has no states array |
| CFG-N01 | Medium | ⚠️50 | ⚠️58 | ✅95 | ✅70 | ✅80 | ✅68 | split | · | Desktop MimeType incomplete — only text/html, missing text/plain and text/markdown |
| CFG-N02 | Low | ✅55 | ⚠️58 | ❔40 | ✅70 | ✅95 | ✅55 | split | · | v1.1.3 release date "2022-1-16" breaks chronological order — should be 2023-01-16 |
| CFG-N03 | Low | ✅60 | ⚠️58 | ✅95 | ✅70 | ✅95 | ✅60 | split | · | "fixedd" typo in v2.0.2 release description |
| TP-SYS | Medium | ⚠️40 | ⚠️58 | ⚠️70 | ✅70 | ✅75 | ⚠️50 | split | · | Systemic absence of ToolTip on ~60+ controls across entire application |
| TP-N01 | Medium | ⚠️55 | ⚠️58 | ✅90 | ✅70 | ✅80 | ✅68 | split | · | "Error loading file..." used as document content, not placeholderText |
| WATCH-N01 | Medium | ⚠️50 | ✅78 | ✅95 | ✅70 | ✅80 | ✅68 | split | · | addPath() return never checked — silent watch failure |
| WATCH-N02 | Medium | ⚠️50 | ✅78 | ✅90 | ✅70 | ✅80 | ✅68 | split | · | removePath() return never checked — stale path causes double-watch |
| WATCH-N03 | Medium | ❔45 | ✅78 | ✅90 | ✅75 | ✅70 | ❔45 | split | · | Watcher not refreshed after fileChanged — stale inotify on Linux atomic saves |
| WATCH-N04 | Low | ⚠️45 | ✅78 | ✅85 | ✅70 | ✅85 | ✅68 | split | · | unblockFileWatcher() dereferences _fileSystemWatcher without null guard |
| MODEL-N01 | Medium | ✅60 | ✅78 | ✅90 | ✅75 | ✅80 | ✅60 | AGREE | · | MarkersModel::rowCount ignores parent.isValid() — returns full size for child probe |
| MODEL-N02 | Low | ✅55 | ⚠️58 | ✅85 | ✅70 | ✅85 | ✅55 | split | · | SessionModel::clearDataPoints lacks empty-model guard before beginRemoveRows |
| COERC-N01 | High | ❔45 | ✅84 | ❌85 | ✅75 | ✅90 | ❔45 | **CONFLICT** | · | parseInt("") → NaN state bootstrap — first toggle() bricks state machine |
| COERC-N02 | Medium | ✅55 | ✅78 | ✅95 | ✅75 | ✅85 | ✅55 | AGREE | · | Unvalidated string-to-number injects NaN into root.__opacity — all opacity dead |
| COERC-N03 | Low | ⚠️50 | ⚠️58 | ✅80 | ✅70 | ✅80 | ✅68 | split | · | real→int truncation in WindowDragger position compounds drift |
| QLOAD-N01 | Medium | ⚠️50 | ✅78 | ✅95 | ✅75 | ✅85 | ✅68 | split | · | InputsOverlay toggleButtonsOff() null-check bypass — crash on slow async Loaders |
| DETACH-N01 | Low | ⚠️40 | ⚠️58 | ✅75 | ✅70 | ❌60 | ⚠️50 | **CONFLICT** | · | 4 non-const operator[] on QList in keySearch() — unnecessary implicit sharing detach |
| COLOR-CRIT-01 | High | ❔45 | ❔39 | ✅95 | ✅80 | ✅90 | ❌72 | **CONFLICT** | · | selectionColor #333d9ef3 — alpha channel reversed (#AARRGGBB vs #RRGGBBAA), selection invisible |
| SYM-N01 | Low-Medium | ⚠️40 | ⚠️58 | ✅85 | ⚠️55 | ✅65 | ⚠️50 | split | · | 6 RTL/symmetry issues across PointerSettings, Find, PrompterView, Prompter, PrompterPage |
| CLIP-CRIT-01 | Critical | ✅85 | ✅84 | ✅95 | ✅80 | ✅90 | ✅85 | AGREE | · | Paste via toolbar button and File menu bypasses HTML sanitization |
| CLIP-N04 | Medium | ✅65 | ⚠️58 | ✅90 | ✅75 | ✅80 | ✅65 | split | · | Image-only clipboard paste — button enabled but does nothing |
| INT-N04 | Medium | ✅55 | ⚠️58 | ✅85 | ✅75 | ✅85 | ✅55 | split | · | OBS URL/Password fields disabled when WebSocket enabled — inverted logic |
| INT-N05 | Medium | ✅55 | ⚠️58 | ✅90 | ✅75 | ✅85 | ✅55 | split | · | PropertyChanges permanently destroys CheckBox checked bindings on PointerSettings tab switch |
| FMT-N01 | Medium | ✅50 | ✅78 | ✅95 | ✅75 | ✅85 | ✅50 | AGREE | · | Step Speed onAccepted displays 100x correct value |
| FMT-N02 | Medium | ✅50 | ✅78 | ✅95 | ✅75 | ✅85 | ✅50 | AGREE | · | Step Acceleration onAccepted — identical 100x display bug |
| PLAT-N04 | Medium | ✅65 | ✅78 | ✅90 | ✅75 | ✅90 | ✅65 | AGREE | · | "ipados" is not valid Qt.platform.os string — 18 dead guards across 5 files |
| PLAT-N05 | Low | ⚠️45 | ⚠️58 | ✅85 | ✅70 | ✅75 | ✅68 | split | · | Base main.qml fullScreenPlatform missing "wasm" (inconsistent with +windows) |
| WYS-N01 | Medium | ✅60 | ✅78 | ✅90 | ✅75 | ✅85 | ✅60 | AGREE | · | Internal drag-and-drop copy inserts HTML as plain text — tags become visible |
| WYS-N02 | Low | ✅70 | ⚠️58 | ✅85 | ✅70 | ✅95 | ✅70 | split | · | Default stylesheet CSS errors: valign:top (not a CSS property) and border:1pt (missing style) |
| QP-N01 | High | ✅65 | ⚠️58 | ✅95 | ✅80 | ✅95 | ✅65 | split | · | restartApplication() quits even when startDetached fails — app dies with no replacement |
| QP-N02 | Medium | ✅65 | ✅78 | ✅90 | ✅75 | ✅95 | ✅65 | AGREE | · | convert.waitForFinished() blocks GUI thread up to 30s during LibreOffice import |
| QP-N03 | Medium | ✅55 | ✅78 | ✅90 | ✅75 | ✅90 | ✅55 | AGREE | · | convert.exitCode() never checked — LibreOffice error output becomes document content |
| IMG-N02 | High | ✅60 | ✅84 | ✅90 | ✅80 | ✅95 | ✅60 | AGREE | · | insertHtmlAt() silent blocking HTTP load for img src URLs — UI freeze |
| TRN-N01 | Low | ✅55 | ✅78 | ✅90 | ✅70 | ✅95 | ✅55 | AGREE | · | Dead ternary: both branches return Qt.OpenHandCursor |
| A11Y-SYS | Medium | ⚠️45 | ⚠️58 | ✅85 | ✅70 | ✅90 | ⚠️50 | split | · | Systemic absence of Accessible properties — app invisible to screen readers |
| EVT-N13 | High | ❔45 | ⚠️58 | ✅95 | ✅75 | ✅90 | ❔45 | split | · | rewind()/fastForward() event undefined — winding state permanently locked after first use |
| ANM-N02 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅70 | ✅85 | ✅68 | split | · | Standby→Ready countdown opacity flash — PropertyChanges opacity:1 conflicts with dissolveIn |
| RESO-N01 | Medium | ⚠️45 | ⚠️48 | ✅95 | ✅70 | ✅90 | ✅68 | split | · | Editing font size not viewport-scaled — text nearly unreadable on 4K |
| RESO-N02 | Low | ⚠️40 | ⚠️48 | ✅80 | ✅65 | ✅80 | ✅68 | split | · | Scrollbar width 6dp-13dp — below minimum 44dp touch target |
| RESO-N03 | Low | ⚠️40 | ⚠️48 | ✅75 | ⚠️55 | ✅70 | ⚠️50 | split | · | Control spacing hardcoded 8dp — cramped on large displays |
| RESO-N04 | Low | ⚠️40 | ⚠️48 | ✅75 | ⚠️55 | ✅70 | ⚠️50 | split | · | Projection-window margins fixed 10dp/5dp — near-flush on large screens |
| RESO-N05 | Low | ⚠️40 | ⚠️48 | ✅75 | ✅65 | ✅70 | ✅68 | split | · | PointerSettings ListView height hardcoded 180dp — doesn't fill available space |
| RESO-N06 | Low | ⚠️40 | ⚠️48 | ✅80 | ⚠️55 | ✅70 | ✅68 | split | · | ReadRegionOverlay pointer margin 3dp — overlap with text at large fonts |
| STK-N01 | Critical | ✅85 | ✅92 | ✅95 | ✅80 | ✅95 | ✅85 | AGREE | · | Android projectionManager undefined — crash on "Performance tweaks" submenu |
| JSON-N01 | High | ✅65 | ✅84 | ✅95 | ✅80 | ✅95 | ✅65 | AGREE | · | OBS WebSocket Hello auth fields accessed without null guard — crash on auth-disabled |
| QW-N01 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅85 | ✅68 | split | · | Projection Window onClosing references cleared model — spurious runtime errors |
| QW-N02 | Medium | ⚠️55 | ⚠️58 | ✅85 | ✅75 | ✅85 | ✅68 | split | · | Stale QScreen reference in projection model — dangling after monitor hot-unplug |
| JS-N01 | Low | ✅50 | ⚠️58 | ✅70 | ✅65 | ✅90 | ✅50 | split | · | TIMERCLOCK getTimeString() — redundant .toString() on already-string — 54 allocs/sec |
| JS-N02 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅75 | ✅90 | ✅68 | split | · | markerCompare() per-frame JSON.stringify() over OBS marker — 60 allocs/sec |
| THM-SYS | High | ⚠️55 | ⚠️58 | ✅90 | ✅70 | ✅85 | ✅68 | split | · | Complete theme deadlock — 50+ Material.theme: Dark hardcoded, theme toggle commented out |
| HSCROLL-N01 | Medium | ⚠️50 | ⚠️58 | ✅95 | ✅70 | ✅90 | ✅68 | split | · | InputsOverlay Flickables use contentWidth: width instead of implicitWidth — horizontal overflow clipped |
| HSCROLL-N02 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅70 | ✅80 | ✅68 | split | · | Inner Flickables missing flickableDirection: VerticalFlick — conflict with parent horizontal ListView |
| COLOR-N08 | Medium | ⚠️45 | ⚠️58 | ✅90 | ✅70 | ✅85 | ✅68 | split | · | textBackground() returns invalid QColor for body/paragraph text |
| COLOR-N09 | Medium | ⚠️55 | ⚠️58 | ✅90 | ✅70 | ✅85 | ✅68 | split | · | acceptedColor binds transparent QColor on startup — initial text invisible |
| PP-N01 | Medium | ✅55 | ⚠️58 | ✅95 | ✅75 | ✅95 | ✅55 | split | · | Q_OS_APPLE is not a Qt macro — KGlobalAccel block compiles on all Unix including macOS |
| TRF-N01 | High | ⚠️50 | ⚠️58 | ✅95 | ✅75 | ✅90 | ✅68 | split | · | rightWidthAdjustmentBar drag.maximumX formula broken — drag collapses to single point |
| TOG-N01 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅70 | ✅80 | ✅68 | split | · | WheelSettingsOverlay useScrollAsDialButton — cross-path stale checked state |
| RPL-N01 | Medium | ❌55 | ❌76 | ✅95 | ✅70 | ❌90 | ❌55 | **CONFLICT** | · | 6 additional files missing QtQuick.Controls.Material import — ~65 controls unthemed |
| VIS-FB-N01 | Low | ⚠️50 | ⚠️58 | ✅90 | ✅70 | ✅90 | ✅68 | split | · | bookmarkListButton and searchButton missing checkable: true — no checked background |
| DEB-N01 | High | ✅55 | ✅84 | ✅95 | ✅75 | ✅90 | ✅55 | AGREE | · | libvulkan-dev (dev package) listed as Debian runtime dependency |
| DEB-N02 | High | ❔45 | ✅84 | ✅95 | ✅80 | ❌90 | ❔45 | **CONFLICT** | · | qml6-module-qtcore is not a real Debian package — .deb uninstallable |
| DEB-N03 | High | ❔45 | ✅84 | ✅95 | ✅80 | ❌85 | ❔45 | **CONFLICT** | · | qml6-module-qt-labs-platform doesn't exist for Qt 6 — .deb uninstallable |
| RPM-N01 | Medium | ✅50 | ⚠️58 | ✅90 | ✅75 | ✅95 | ✅50 | split | · | RPM dependencies entirely commented out — zero automatic dependency resolution |
| TS-N07 | Medium | ❔40 | ❔39 | ❔40 | ❔50 | ✅95 | ❔40 | split | · | Wrong translations: Chinese "Undo"→"Open", "Bars"→"Toolbar"; French "Pointer Configuration"→"Prompter duration"; Korean "Line width"→"Line height" |
| META-N14 | Medium | ❔45 | ⚠️58 | ✅80 | ⚠️60 | ❔60 | ❔45 | split | · | ModernToolkit removed from AppStream spec — validation error |
| META-N15 | Medium | ⚠️45 | ⚠️58 | ✅90 | ✅70 | ✅80 | ✅68 | split | · | No StartupWMClass in desktop file — duplicate dock entries, missing icon |
| META-N16 | Low | ❔45 | ❔39 | ✅90 | ⚠️60 | ✅95 | ❔45 | split | · | README badges and links reference wrong repo Cuperino/QPrompt (should be QPrompt-Teleprompter) |
| META-N17 | Medium | ❔45 | ❔39 | ✅85 | ✅70 | ✅95 | ❔45 | split | · | README links to non-existent BUILD.md |
| AND-N08 | Medium | ✅60 | ✅78 | ✅95 | ✅75 | ✅95 | ✅60 | AGREE | · | Android saveAs() hardcodes isHtml=true — plain-text files saved with HTML markup |
| TMR-N05 | High | ❔45 | ❔39 | ✅90 | ✅75 | ⚠️70 | ❔45 | split | · | markerCompare() only fires on forward scroll — backward scroll + re-forward misses marker |
| TMR-N06 | Medium | ⚠️50 | ✅78 | ✅90 | ✅70 | ✅85 | ✅68 | split | · | Auto-reload Timer persists after network dialog close — background refetches |
| FONT-METRIC-01 | High | ❔40 | ❔39 | ✅90 | ✅75 | ✅75 | ❔40 | split | · | pixelSize used as line-height proxy — core scroll timing off by ~57% |
| FONT-METRIC-02 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅70 | ✅90 | ✅68 | split | · | FontLoader status never checked — font substitution silently fails |
| FONT-METRIC-03 | Low | ❔40 | ❔39 | ✅85 | ✅70 | ❌70 | ❌72 | **CONFLICT** | · | fontFamily() returns resolved-family not requested-family — substitution invisible |
| STC-N01 | Medium | ✅55 | ⚠️58 | ✅90 | ✅70 | ✅90 | ✅55 | split | · | closeAll() destroys user's per-screen projection flip configuration |
| STC-N02 | Low | ⚠️45 | ⚠️58 | ✅85 | ✅65 | ❌60 | ✅68 | **CONFLICT** | · | Find.qml close() doesn't reset replace-mode or regex-mode flags |
| STC-N03 | Medium | ❔45 | ⚠️58 | ✅90 | ✅70 | ❌65 | ❔45 | **CONFLICT** | · | velocityIndicator.firstResetDone never cleared on dismiss — second activation broken |
| STC-N04 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅70 | ✅75 | ✅68 | split | · | Projection window CursorAutoHide not reset on close — cursor permanently hidden |
| STC-N05 | Low | ⚠️50 | ⚠️58 | ✅85 | ✅65 | ✅80 | ✅68 | split | · | cancel() doesn't call timer.stopTimer() — elapsed time persists across sessions |
| TB-N01 | Medium | ⚠️45 | ⚠️58 | ✅85 | ✅70 | ✅80 | ✅68 | split | · | toolbar toggle timers produce stale state on rapid clicks |
| TB-N02 | Medium | ⚠️45 | ⚠️58 | ✅90 | ✅70 | ✅75 | ✅68 | split | · | baseSpeedSlider/baseAccelerationSlider onMoved yanks focus to prompter instead of restoreFocus() |
| TB-N03 | Low | ⚠️45 | ⚠️58 | ✅70 | ⚠️55 | ✅65 | ⚠️50 | split | · | Collapsible toolbar rows animate height but adjacent rows snap — no y-position animation |
| TB-N04 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅70 | ❌60 | ✅68 | **CONFLICT** | · | velocityDragArea accepts MiddleButton without propagateComposedEvents — scroll blocked |
| RESP-N01 | Low | ⚠️50 | ⚠️58 | ✅85 | ✅65 | ✅90 | ⚠️50 | split | · | minimumHeight: minimumWidth forces square aspect ratio — prevents landscape-strip windows |
| RESP-N02 | Medium | ❔45 | ⚠️58 | ✅90 | ✅70 | ✅85 | ❔45 | split | · | mobileOrSmallScreen threshold at 1231px activates on default 1220px launch |
| RESP-N03 | Low | ⚠️45 | ⚠️58 | ❌85 | ✅65 | ✅70 | ✅68 | **CONFLICT** | · | +android/main.qml omits all size declarations — transient zero-size layout on startup |
| QT-LC-N01 | High | ❌70 | ❌76 | ✅95 | ⚠️60 | ❌90 | ❌70 | **CONFLICT** | · | QQmlFileSelector never instantiated — platform QML file selectors dead |
| TC-N01 | Low | ✅60 | ✅78 | ✅80 | ✅65 | ✅60 | ✅60 | AGREE | · | Image.source assigned boolean false instead of empty string |
| TC-N02 | Low | ⚠️45 | ⚠️58 | ✅80 | ✅65 | ❌60 | ✅68 | **CONFLICT** | · | property color value assigned string expression — silent coercion |
| BLK-N01 | Medium | ✅70 | ⚠️58 | ✅85 | ✅70 | ❔55 | ✅70 | split | · | alignment() returns Qt::AlignCenter (includes vertical bit 0x0080) on null cursor |
| BLK-N02 | Medium | ✅55 | ⚠️58 | ✅90 | ✅70 | ✅80 | ✅55 | split | · | updateContents() fails to reset block formatting — stale formats contaminate new document |
| BLK-N03 | Medium | ✅60 | ⚠️58 | ✅90 | ✅70 | ✅90 | ✅60 | split | · | setLineHeight/setParagraphHeight apply document-wide — destroy per-block customization |
| SHT-N01 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅70 | ✅90 | ✅68 | split | · | markerToggle/namedMarkerToggle forwarded but never handled — dead hotkeys |
| SHT-N02 | Low | ⚠️45 | ⚠️58 | ⚠️75 | ✅65 | ✅75 | ✅68 | split | · | Missing StandardKey.FullScreen on Android |
| LAZY-N01 | Low | ⚠️45 | ⚠️58 | ✅85 | ✅65 | ✅85 | ✅68 | split | · | namedMarkerConfiguration Loader double-loads KeyInputButton — first load wasted |
| LAZY-N02 | Medium | ⚠️50 | ⚠️58 | ⚠️60 | ✅70 | ✅80 | ✅68 | split | · | InputsOverlay ObjectModel eagerly loads both tabs — hidden tab content loaded prematurely |
| LL-N01 | Medium | ⚠️50 | ⚠️58 | ✅80 | ✅65 | ✅75 | ✅68 | split | · | 10 EditorToolbar MouseArea/TextField width-depends-on-width binding loops |
| LL-N02 | Low | ✅55 | ✅78 | ❌95 | ✅65 | ❌55 | ✅55 | **CONFLICT** | · | ProgressIndicator stepSize divide-by-zero when prompter.height is 0 |
| SHDR-N02 | Medium | ✅60 | ⚠️58 | ❌85 | ✅65 | ✅85 | ✅60 | **CONFLICT** | · | id: shadow collides with property ShaderEffectSource shadow — ambiguous resolution in blur chain |
| KB-N01 | Medium | ⚠️45 | ⚠️58 | ✅85 | ✅65 | ❌70 | ✅68 | **CONFLICT** | · | Find.qml: 9 toolbar buttons missing focusPolicy — keyboard-invisible |
| KB-N02 | Medium | ⚠️55 | ⚠️58 | ✅85 | ✅65 | ❌65 | ✅68 | **CONFLICT** | · | InputsOverlay TabBar TabButtons have no focusPolicy + keyNavigationEnabled: false — keyboard dead |
| KB-N03 | Medium | ⚠️50 | ⚠️58 | ❌80 | ✅70 | ✅90 | ✅68 | **CONFLICT** | · | +windows and +android ESC handler uses .focus instead of .activeFocus — wrong boolean |
| DRAG-N01 | Low | ⚠️45 | ⚠️58 | ✅80 | ✅65 | ✅60 | ✅68 | split | · | Image resize body drag: cursor shows OpenHandCursor until drag threshold exceeded |
| DRAG-N02 | Low | ✅55 | ⚠️58 | ✅80 | ✅65 | ✅70 | ✅55 | split | · | textDragArea has no cursorShape — no cursor feedback during text drag |
| SHAPE-N01 | Medium | ✅60 | ✅92 | ✅80 | ✅70 | ✅85 | ✅60 | AGREE | · | pointer_0.qml PathLine parent.width resolves to undefined (ShapePath has no width) — arrow collapsed |
| SHAPE-N02 | Medium | ❔45 | ❔39 | ✅85 | ✅70 | ✅75 | ❔45 | split | · | concentricCircles Shape uses parent-space coordinates in local space — circles off-center |
| FD-N01 | Medium | ⚠️55 | ⚠️58 | ✅90 | ✅65 | ✅85 | ✅68 | split | · | \|\| should be && in autoReload guard — user preference ignored for non-binary files |
| TBND-N01 | Medium | ⚠️50 | ⚠️58 | ✅70 | ✅70 | ✅85 | ✅68 | split | · | SpellHighlighter regex excludes combining diacritical marks — NFD text misspelled |
| TBND-N02 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅70 | ❌55 | ✅68 | **CONFLICT** | · | All CJK text marked misspelled — ideographic characters not in Hunspell dictionaries |
| TBND-N03 | Low | ✅55 | ✅78 | ✅80 | ✅65 | ✅90 | ✅55 | AGREE | · | extendLastMarker() doesn't update Marker::length field — stale after appends |
| MIME-N01 | High | ⚠️45 | ⚠️58 | ❌95 | ⚠️60 | ❌75 | ❌72 | split | · | Temporary QMimeDatabase — QMimeType dangling on Qt 5 (undefined behavior) |
| MIME-N02 | Medium | ✅65 | ✅78 | ✅90 | ✅70 | ✅90 | ✅65 | AGREE | · | loadFromNetworkFinihed() ignores Content-Type header — all network content treated as HTML |
| MIME-N03 | Medium | ✅70 | ✅78 | ✅85 | ✅70 | ✅90 | ✅70 | AGREE | · | PDF/EPUB/MOBI/AZW MIME-detected but import is no-op — error text becomes content |
| TXT-FMT-N01 | Medium | ✅65 | ⚠️58 | ✅80 | ✅70 | ✅90 | ✅65 | split | · | setMarkerHref("") fails to clear QTextFormat::AnchorHref — stale href persists |
| SCR-N01 | High | ❔45 | ❔39 | ✅90 | ✅70 | ✅90 | ❔45 | split | · | Per-screen projection flip settings lost on restart — never serialized |
| SCR-N02 | Medium | ✅55 | ✅92 | ✅90 | ✅70 | ✅90 | ✅55 | AGREE | · | Duplicate entries in displayModel on first toggle — no clear() before setScreensModel() |
| SCR-N03 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅65 | ✅85 | ✅68 | split | · | No runtime screen plug/unplug handling — stale projection windows on disconnected screens |

## Divergences

Rows where the agents do not unanimously agree (CONFLICT first, then split).

### [ARC-01] Velocity physics engine entirely in QML (~20 readonly property bindings)  ·  _CONFLICT_  ·  
`Prompter.qml:113-129`
- **opus:** ⚠️ PARTIAL (35) — velocity physics in QML; architectural (Prompter.qml:113)
- **gpt:** ⚠️ PARTIAL (48) — maintainability issue observed, but no direct runtime bug shown (src/prompter/Prompter.qml:113)
- **deepseek:** ❌ FALSE (50) — architectural observation; readonly property bindings are a valid QML design pattern
- **glm:** ⚠️ PARTIAL (55) — Prompter.qml:113-129 velocity physics in QML with ~20 readonly property bindings; architectural concern not a bug
- **kimi:** ✅ LEGIT (60) — Prompter.qml:113-129 velocity physics (__speed,__velocity,__timeToEnd,etc.) implemented entirely in QML readonly bindings.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — velocity physics in QML; architectural (Prompter.qml:113)

### [ARC-02] Arc-03 Search/replace state machine fully in QML (50+ lines)  ·  _CONFLICT_  ·  
`Find.qml:112-161`
- **opus:** ⚠️ PARTIAL (35) — search state machine in QML; architectural (Find.qml:112)
- **gpt:** ⚠️ PARTIAL (48) — maintainability issue observed, but no direct runtime bug shown (src/prompter/Find.qml:112)
- **deepseek:** ❌ FALSE (50) — architectural observation; state machine in QML is a valid Qt design pattern
- **glm:** ⚠️ PARTIAL (55) — Find.qml:112-161 search/replace state machine in QML; architectural concern
- **kimi:** ✅ LEGIT (60) — Find.qml:112-161 search/replace orchestration, wrap detection and cursor math implemented fully in QML.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — search state machine in QML; architectural (Find.qml:112)

### [ARC-03] OBS WebSocket v5 protocol in QML — opcode dispatch, auth, subscription  ·  _CONFLICT_  ·  
`Prompter.qml:366-388`
- **opus:** ⚠️ PARTIAL (35) — OBS WS protocol in QML; architectural (Prompter.qml:366)
- **gpt:** ⚠️ PARTIAL (48) — maintainability issue observed, but no direct runtime bug shown (src/prompter/Prompter.qml:366)
- **deepseek:** ❌ FALSE (50) — architectural observation; WebSocket protocol in QML is a valid Qt design pattern
- **glm:** ⚠️ PARTIAL (55) — Prompter.qml:366-388 OBS WebSocket v5 protocol in QML; architectural concern
- **kimi:** ✅ LEGIT (60) — Prompter.qml:366-388 implements OBS WebSocket v5 handshake, opcode dispatch and authentication in QML.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — OBS WS protocol in QML; architectural (Prompter.qml:366)

### [ARC-04] DocumentHandler is 2295-line god class spanning file I/O, network, HTML filtering, markers, spellcheck, drag-drop, images, search, undo, clipboard, sleep prevention, font dialog  ·  _CONFLICT_  ·  
`documenthandler.cpp (2295 lines)`
- **opus:** ⚠️ PARTIAL (40) — DocumentHandler god-class; architectural/subjective
- **gpt:** ⚠️ PARTIAL (48) — maintainability issue observed, but no direct runtime bug shown (src/documenthandler.cpp:1)
- **deepseek:** ❌ FALSE (50) — architectural observation; large class is maintainability concern not a code defect
- **glm:** ⚠️ PARTIAL (55) — documenthandler.cpp is 1933-line god class; architectural concern not a bug
- **kimi:** ✅ LEGIT (60) — DocumentHandler spans file I/O, network, HTML filtering, markers, spellcheck, images, etc.; source is ~1933 lines of mixed concerns.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — DocumentHandler god-class; architectural/subjective

### [ARC-05] Prompter.qml is 3139-line god component spanning velocity, state machine, keyboard, WebSocket, markers, spellcheck UI, file dialogs, WYSIWYG toggle, shadows  ·  _CONFLICT_  ·  
`Prompter.qml (3139 lines)`
- **opus:** ⚠️ PARTIAL (35) — Prompter.qml 3139-line god component; architectural
- **gpt:** ⚠️ PARTIAL (48) — maintainability issue observed, but no direct runtime bug shown (src/prompter/Prompter.qml:1)
- **deepseek:** ❌ FALSE (50) — architectural observation; large QML component is maintainability concern not defect
- **glm:** ⚠️ PARTIAL (55) — Prompter.qml is 3139-line god component; architectural concern
- **kimi:** ✅ LEGIT (60) — Prompter.qml is 3139 lines and mixes velocity engine, state machine, keyboard handling, WebSocket, dialogs and shadows.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — Prompter.qml 3139-line god component; architectural

### [ARC-06] qmlutil.hpp is utility grab-bag with 10+ unrelated functions  ·  _CONFLICT_  ·  
`qmlutil.hpp (184 lines)`
- **opus:** ⚠️ PARTIAL (35) — qmlutil grab-bag; architectural
- **gpt:** ⚠️ PARTIAL (48) — maintainability issue observed, but no direct runtime bug shown (src/qmlutil.hpp:1)
- **deepseek:** ❌ FALSE (50) — architectural observation; utility grab-bag is style concern not code defect
- **glm:** ⚠️ PARTIAL (50) — qmlutil.hpp is 184-line utility grab-bag; minor architectural concern
- **kimi:** ✅ LEGIT (60) — qmlutil.hpp:184 lines mixes QProcess, crypto, cursor control, font list, factory reset and grab-result utilities.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — qmlutil grab-bag; architectural

### [BIND-N01] contentWidth undefined for Shape/Image pointer types — transform origin silently wrong  ·  _CONFLICT_  ·  Low
`ReadRegionOverlay.qml:396`
- **opus:** ⚠️ PARTIAL (50) — contentWidth undefined for Shape/Image pointer (R4-ROV-03 family) (ReadRegionOverlay.qml:396)
- **gpt:** ✅ LEGIT (92) — contentWidth undefined for Shape/Image pointer types - transform origin silently wrong (src/prompter/ReadRegionOverlay.qml:396)
- **deepseek:** ✅ LEGIT (65) — contentWidth undefined for Shape/Image pointer types; transform origin silently wrong (ReadRegionOverlay.qml:396)
- **glm:** ⚠️ PARTIAL (55) — ReadRegionOverlay.qml:396 contentWidth undefined for Shape/Image pointer types; transform origin wrong
- **kimi:** ❌ FALSE (70) — ReadRegionOverlay.qml:396 uses bitwise OR with contentWidth; JS coerces undefined to 0, so origin falls back to width/2, not arbitrary.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — contentWidth undefined for Shape/Image pointer (R4-ROV-03 family) (ReadRegionOverlay.qml:3

### [CMAKE-N01] WASM build excludes TelemetryPage.qml and RemotePage.qml  ·  _CONFLICT_  ·  Low
`src/CMakeLists.txt:106-121, main.qml:175-181`
- **opus:** ⚠️ PARTIAL (45) — WASM omits TelemetryPage/RemotePage; both commented out anyway (CMakeLists.txt:106)
- **gpt:** ⚠️ PARTIAL (58) — observed WASM build excludes TelemetryPage.qml and RemotePage.qml (src/CMakeLists.txt:106)
- **deepseek:** ❔ UNSURE (60) — DUPLICATE-ID — WASM exclusion real at src/CMakeLists.txt:106 but refs in main.qml:175 are commented out
- **glm:** ✅ LEGIT (80) — src/CMakeLists.txt:106-121 WASM build excludes TelemetryPage.qml and RemotePage.qml but main.qml:175-181 references them
- **kimi:** ✅ LEGIT (70) — src/CMakeLists.txt:106-121 omits Remote/Telemetry .qml for WASM while main.qml defines loadRemoteControlPage/loadTelemetryPage references (currently commented).
- **opus-ultra:** ❌ FALSE (72) — max: code correct / claim mischaracterized — WASM omits TelemetryPage/RemotePage; both commented out anyway (CMakeLists.txt:106)

### [CMAKE-N03] qt_wrap_ui conflicts with global AUTOUIC — double UI processing  ·  _CONFLICT_  ·  Medium
`src/CMakeLists.txt:43-46 vs CMakeLists.txt:45`
- **opus:** ⚠️ PARTIAL (50) — qt_wrap_ui + AUTOUIC may double-process .ui (CMakeLists.txt:43)
- **gpt:** ❌ FALSE (76) — AUTOUIC can coexist with qt_wrap_ui; duplicate processing is not shown (src/CMakeLists.txt:43)
- **deepseek:** ✅ LEGIT (85) — src/CMakeLists.txt:43-46 vs CMakeLists.txt:45: qt_wrap_ui + AUTOUIC both process systemfontchooserdialog.ui; double code generation — race in parallel builds
- **glm:** ✅ LEGIT (75) — src/CMakeLists.txt:43-46 qt_wrap_ui conflicts with global AUTOUIC at CMakeLists.txt:45; double UI processing
- **kimi:** ✅ LEGIT (80) — CMakeLists.txt:45 enables CMAKE_AUTOUIC and src/CMakeLists.txt:43-46 also calls qt_wrap_ui causing duplicate processing.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — qt_wrap_ui + AUTOUIC may double-process .ui (CMakeLists.txt:43)

### [CMT-N02] Truncated comment in markersmodel.cpp:107-108  ·  _CONFLICT_  ·  Low
`markersmodel.cpp:107-108`
- **opus:** ⚠️ PARTIAL (35) — truncated comment; cosmetic (markersmodel.cpp:107)
- **gpt:** ⚠️ PARTIAL (48) — comment problem observed, but defect impact is limited (src/markersmodel.cpp:107)
- **deepseek:** ✅ LEGIT (90) — Truncated comment at markersmodel.cpp:107 — 'after' ends mid-sentence workaround rationale lost
- **glm:** ✅ LEGIT (75) — markersmodel.cpp:107-108 truncated comment
- **kimi:** ❌ FALSE (70) — A truncated comment in markersmodel.cpp:107-108 is a documentation wart, not a code defect.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — truncated comment; cosmetic (markersmodel.cpp:107)

### [CMT-N03] Misleading OpenGL workaround comment — scope of impact understated  ·  _CONFLICT_  ·  Medium
`main.cpp:79`
- **opus:** ⚠️ PARTIAL (35) — OpenGL workaround comment scope; meta (main.cpp:79)
- **gpt:** ⚠️ PARTIAL (48) — comment problem observed, but defect impact is limited (src/main.cpp:79)
- **deepseek:** ✅ LEGIT (85) — Comment at main.cpp:79 mentions only 'opacity bug' — omits that opengl backend forces deprecated path on all Windows
- **glm:** ⚠️ PARTIAL (60) — main.cpp:79 OpenGL workaround comment understates scope; affects all Windows not just DirectX
- **kimi:** ❌ FALSE (70) — main.cpp:79 comment understates side effects but the environment variable is placed correctly; not a functional bug.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — OpenGL workaround comment scope; meta (main.cpp:79)

### [CMT-N04] Comment masks invalid enum bug — 2 - value produces out-of-range LayoutDirection  ·  _CONFLICT_  ·  Medium
`main.cpp:165`
- **opus:** ❌ FALSE (55) — claims invalid enum but 2=LayoutDirectionAuto is valid (dup TYP-02) (main.cpp:165)
- **gpt:** ❌ FALSE (76) — the value 2 is Qt::LayoutDirectionAuto not an invalid enum (src/main.cpp:165)
- **deepseek:** ✅ LEGIT (85) — 'Substract from 2' comment at main.cpp:165 masks that 2-0=2 is out-of-range LayoutDirection enum
- **glm:** ⚠️ PARTIAL (60) — main.cpp:165 comment masks invalid enum bug; 2-value produces valid LayoutDirection for 0/1 input
- **kimi:** ❌ FALSE (75) — The comment explains intent; the real enum-range issue is already captured by TYP-02, not a separate bug.
- **opus-ultra:** ❌ FALSE (55) — claims invalid enum but 2=LayoutDirectionAuto is valid (dup TYP-02) (main.cpp:165)

### [CMT-N05] Missing security warning on QProcess RCE sink (sys://)  ·  _CONFLICT_  ·  High
`qmlutil.hpp:84-95`
- **opus:** ⚠️ PARTIAL (40) — only a missing security-comment note on the sys:// RCE sink (qmlutil.hpp:84)
- **gpt:** ⚠️ PARTIAL (48) — comment problem observed, but defect impact is limited (src/qmlutil.hpp:84)
- **deepseek:** ✅ LEGIT (85) — No security comment on QProcess::startDetached at qmlutil.hpp:91 — sys:// RCE sink unannotated
- **glm:** ⚠️ PARTIAL (60) — qmlutil.hpp:84-95 missing security warning on QProcess RCE sink for sys:// URIs
- **kimi:** ❌ FALSE (75) — missing security comment on qmlutil.hpp:84 run() is documentation debt; the actual RCE is captured by SEC-01.
- **opus-ultra:** ❌ FALSE (72) — max: code correct / claim mischaracterized — only a missing security-comment note on the sys:// RCE sink (qmlutil.hpp:84)

### [CMT-N06] Missing warning: re-entrant toggle() inside Behavior.onRunningChanged  ·  _CONFLICT_  ·  Medium
`Prompter.qml:855-856`
- **opus:** ⚠️ PARTIAL (40) — only a missing-warning note re re-entrant toggle (Prompter.qml:855)
- **gpt:** ⚠️ PARTIAL (48) — comment problem observed, but defect impact is limited (src/prompter/Prompter.qml:855)
- **deepseek:** ✅ LEGIT (80) — toggle() at Prompter.qml:855 inside Behavior.onRunningChanged — re-entrant no warning comment
- **glm:** ⚠️ PARTIAL (60) — Prompter.qml:855-856 missing warning: re-entrant toggle() inside Behavior.onRunningChanged
- **kimi:** ❌ FALSE (70) — A missing warning about re-entrancy on Prompter.qml:855 is a comment issue, not an independent functional bug.
- **opus-ultra:** ❌ FALSE (72) — max: code correct / claim mischaracterized — only a missing-warning note re re-entrant toggle (Prompter.qml:855)

### [CMT-N07] Missing warning: joinPreviousEditBlock() without beginEditBlock()  ·  _CONFLICT_  ·  Medium
`documenthandler.cpp:1596,1610`
- **opus:** ⚠️ PARTIAL (40) — only a missing-comment note re joinPreviousEditBlock (documenthandler.cpp:1596)
- **gpt:** ⚠️ PARTIAL (48) — comment problem observed, but defect impact is limited (src/documenthandler.cpp:1596)
- **deepseek:** ✅ LEGIT (85) — joinPreviousEditBlock() at documenthandler.cpp:1596 without beginEditBlock() — no warning comment
- **glm:** ⚠️ PARTIAL (60) — documenthandler.cpp:1596 1610 missing warning: joinPreviousEditBlock without beginEditBlock
- **kimi:** ❌ FALSE (70) — A missing warning on documenthandler.cpp:1596 joinPreviousEditBlock is a comment issue; the underlying bug is R3-DOC-02.
- **opus-ultra:** ❌ FALSE (72) — max: code correct / claim mischaracterized — only a missing-comment note re joinPreviousEditBlock (documenthandler.cpp:1596)

### [CMT-N09] Commented-out PropertyActions in active loop animation — stale state risk  ·  _CONFLICT_  ·  Medium
`Prompter.qml:866-871`
- **opus:** ⚠️ PARTIAL (40) — commented-out PropertyActions; stale-state note (Prompter.qml:866)
- **gpt:** ⚠️ PARTIAL (48) — comment problem observed, but defect impact is limited (src/prompter/Prompter.qml:866)
- **deepseek:** ✅ LEGIT (85) — PropertyActions resetting __i/position commented out at Prompter.qml:866-871 — stale state risk
- **glm:** ⚠️ PARTIAL (60) — Prompter.qml:866-871 commented-out PropertyActions in active loop animation; stale state risk
- **kimi:** ❌ FALSE (70) — Commented-out PropertyActions in Prompter.qml:866-871 are dead code, not an active defect.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — commented-out PropertyActions; stale-state note (Prompter.qml:866)

### [COERC-N01] parseInt("") → NaN state bootstrap — first toggle() bricks state machine  ·  _CONFLICT_  ·  High
`Prompter.qml:448`
- **opus:** ❔ UNSURE (45) — parseInt('') NaN only if initial state unset; depends on default state (Prompter.qml:448)
- **gpt:** ✅ LEGIT (84) — parseInt("") -> NaN state bootstrap - first toggle() bricks state machine (src/prompter/Prompter.qml:448)
- **deepseek:** ❌ FALSE (85) — Prompter.qml:3088 explicitly sets state: Prompter.States.Editing(=0); parseInt('0')=0 not NaN; state is never empty string
- **glm:** ✅ LEGIT (75) — Prompter.qml:448 parseInt(state) when state is non-numeric returns NaN; first toggle() bricks state machine
- **kimi:** ✅ LEGIT (90) — Prompter.qml:448 `parseInt(state)` on empty string yields NaN; `(NaN+1)%4` is NaN and state comparisons fail.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — parseInt('') NaN only if initial state unset; depends on default state (Prompter.qml:448)

### [COLOR-CRIT-01] selectionColor #333d9ef3 — alpha channel reversed (#AARRGGBB vs #RRGGBBAA), selection invisible  ·  _CONFLICT_  ·  High
`Prompter.qml:973-974`
- **opus:** ❔ UNSURE (45) — #333d9ef3 is valid #AARRGGBB (20% blue); 'reversed alpha' likely intentional (Prompter.qml:973)
- **gpt:** ❔ UNSURE (39) — #333d9ef3 is syntactically AARRGGBB; intent is uncertain (src/prompter/Prompter.qml:973)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:973-974: #333d9ef3 uses #AARRGGBB format but dev likely intended #RRGGBBAA; AA=0x33=20% alpha nearly invisible
- **glm:** ✅ LEGIT (80) — Prompter.qml:973-974 selectionColor #333d9ef3 has alpha channel reversed (#AARRGGBB vs #RRGGBBAA); selection invisible
- **kimi:** ✅ LEGIT (90) — Prompter.qml:973-974 #333d9ef3 interpreted by Qt as AARRGGBB (alpha 0x33) making selection nearly invisible.
- **opus-ultra:** ❌ FALSE (72) — max: code correct / claim mischaracterized — #333d9ef3 is valid #AARRGGBB (20% blue); 'reversed alpha' likely intentional (Prompter.qml

### [CONST-N01] getMarkerKey() not const — pure reader without side effects  ·  _CONFLICT_  ·  Low
`documenthandler.h:214, documenthandler.cpp:746`
- **opus:** ⚠️ PARTIAL (40) — getMarkerKey not const; style only (documenthandler.cpp:746)
- **gpt:** ⚠️ PARTIAL (58) — observed getMarkerKey() not const - pure reader without side effects (src/documenthandler.h:214)
- **deepseek:** ✅ LEGIT (60) — getMarkerKey pure reader method missing const qualifier (documenthandler.cpp:746)
- **glm:** ✅ LEGIT (70) — documenthandler.h:214 746 getMarkerKey() not const; pure reader without side effects
- **kimi:** ❌ FALSE (75) — getMarkerKey() is a non-const reader, but its const-correctness is a style issue with no observable misbehavior.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — getMarkerKey not const; style only (documenthandler.cpp:746)

### [CONST-N02] getMarkerHref() not const — identical pattern  ·  _CONFLICT_  ·  Low
`documenthandler.h:216, documenthandler.cpp:779`
- **opus:** ⚠️ PARTIAL (40) — getMarkerHref not const; style only (documenthandler.cpp:779)
- **gpt:** ⚠️ PARTIAL (58) — observed getMarkerHref() not const - identical pattern (src/documenthandler.h:216)
- **deepseek:** ✅ LEGIT (60) — getMarkerHref pure reader method missing const qualifier (documenthandler.cpp:779)
- **glm:** ✅ LEGIT (70) — documenthandler.h:216 779 getMarkerHref() not const; identical pattern
- **kimi:** ❌ FALSE (75) — getMarkerHref() is a non-const reader; absence of const does not cause a runtime bug.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — getMarkerHref not const; style only (documenthandler.cpp:779)

### [CONST-N03] MarkersModel::previousMarker(), nextMarker(), keySearch(), binarySearch() not const  ·  _CONFLICT_  ·  Low
`markersmodel.h:62,63,64,78, markersmodel.cpp:117,151,205,217`
- **opus:** ⚠️ PARTIAL (40) — marker query methods not const (markersmodel.h:62)
- **gpt:** ⚠️ PARTIAL (58) — observed MarkersModel::previousMarker(), nextMarker(), keySearch(), binarySearch() not const (src/markersmodel.h:62)
- **deepseek:** ✅ LEGIT (55) — four marker query methods lack const qualifier (markersmodel.h:62-64 78)
- **glm:** ✅ LEGIT (70) — markersmodel.h:62-64 78 previousMarker/nextMarker/keySearch/binarySearch not const
- **kimi:** ❌ FALSE (70) — MarkersModel query methods lack const, but they are not misused or mutating data incorrectly.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — marker query methods not const (markersmodel.h:62)

### [CONST-N04] GlobalHotkeys::globalShortcutKey(Action) not const — Q_INVOKABLE pure query  ·  _CONFLICT_  ·  Low
`globalhotkeys.h:147, globalhotkeys.cpp:108`
- **opus:** ⚠️ PARTIAL (40) — globalShortcutKey not const; Q_INVOKABLE query (globalhotkeys.h:147)
- **gpt:** ⚠️ PARTIAL (58) — observed GlobalHotkeys::globalShortcutKey(Action) not const - Q_INVOKABLE pure query (src/globalhotkeys.h:147)
- **deepseek:** ✅ LEGIT (60) — Q_INVOKABLE globalShortcutKey pure query method missing const (globalhotkeys.cpp:108)
- **glm:** ✅ LEGIT (70) — globalhotkeys.h:147 108 globalShortcutKey not const; Q_INVOKABLE pure query
- **kimi:** ❌ FALSE (70) — globalShortcutKey() is a query method without const; this is a style issue, not a functional defect.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — globalShortcutKey not const; Q_INVOKABLE query (globalhotkeys.h:147)

### [CONST-N05] Unnecessary copy via const auto instead of const auto& in extendLastMarker  ·  _CONFLICT_  ·  Low
`markersmodel.cpp:111`
- **opus:** ⚠️ PARTIAL (40) — const auto copy vs const auto& in extendLastMarker (markersmodel.cpp:111)
- **gpt:** ⚠️ PARTIAL (58) — observed Unnecessary copy via const auto instead of const auto& in extendLastMarker (src/markersmodel.cpp:111)
- **deepseek:** ✅ LEGIT (65) — const auto copies Marker object; should be const auto& to avoid copy (markersmodel.cpp:111)
- **glm:** ✅ LEGIT (70) — markersmodel.cpp:111 const auto instead of const auto& in extendLastMarker; unnecessary copy
- **kimi:** ❌ FALSE (65) — extendLastMarker copies last element (const auto); this is a minor inefficiency, not a correctness bug.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — const auto copy vs const auto& in extendLastMarker (markersmodel.cpp:111)

### [CPY-01] 5 Q_INVOKABLE methods pass QString by value instead of const&  ·  _CONFLICT_  ·  Low
`markersmodel.h:68, documenthandler.h:213,215,227, systemfontchooserdialog.h:53`
- **opus:** ⚠️ PARTIAL (40) — 5 Q_INVOKABLE pass QString by value (markersmodel.h:68)
- **gpt:** ⚠️ PARTIAL (58) — observed 5 Q_INVOKABLE methods pass QString by value instead of const& (src/markersmodel.h:68)
- **deepseek:** ✅ LEGIT (80) — 5 Q_INVOKABLE methods pass QString by value instead of const&; unnecessary heap copies (documenthandler.h:213 215 227 markersmodel.h:68)
- **glm:** ✅ LEGIT (75) — markersmodel.h:68 documenthandler.h:213 215 227 systemfontchooserdialog.h:53 Q_INVOKABLE methods pass QString by value instead of const&
- **kimi:** ❌ FALSE (80) — QString passed by value is legal and functional; it is an inefficiency, not a correctness bug.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — 5 Q_INVOKABLE pass QString by value (markersmodel.h:68)

### [DBG-N03] Latent debug state leak: pointers/debug Setting persists Guides checkbox  ·  _CONFLICT_  ·  Low
`PointerSettings.qml:94, ReadRegionOverlay.qml:239`
- **opus:** ⚠️ PARTIAL (45) — debug Setting persists Guides checkbox (PointerSettings.qml:94)
- **gpt:** ⚠️ PARTIAL (52) — observed Latent debug state leak: pointers/debug Setting persists Guides checkbox (src/prompter/PointerSettings.qml:94)
- **deepseek:** ⚠️ PARTIAL (60) — PointerSettings.qml:94: debug alias persists; ReadRegionOverlay.qml:239 binding uses !pointerSettings.debug but cross-file reference may be broken after QML-01 fix — depends on other bug status
- **glm:** ⚠️ PARTIAL (60) — PointerSettings.qml:94 ReadRegionOverlay.qml:239 latent debug state leak; pointers/debug Setting persists
- **kimi:** ❌ FALSE (60) — PointerSettings.qml:94 persists debug, but ReadRegionOverlay.qml:239 currently cannot resolve pointerSettings (QML-01), so no production effect.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — debug Setting persists Guides checkbox (PointerSettings.qml:94)

### [DEB-N02] qml6-module-qtcore is not a real Debian package — .deb uninstallable  ·  _CONFLICT_  ·  High
`CMakeLists.txt:446`
- **opus:** ❔ UNSURE (45) — qml6-module-qtcore package-existence claim; Debian-specific (CMakeLists.txt:446)
- **gpt:** ✅ LEGIT (84) — qml6-module-qtcore is not a real Debian package - .deb uninstallable (CMakeLists.txt:446)
- **deepseek:** ✅ LEGIT (95) — CMakeLists.txt:446: qml6-module-qtcore not a real Debian package; QtCore has no QML module; apt resolution fails
- **glm:** ✅ LEGIT (80) — CMakeLists.txt:446 qml6-module-qtcore is not a real Debian package; .deb uninstallable
- **kimi:** ❌ FALSE (90) — qml6-module-qtcore exists in Ubuntu/Debian Qt6 (qt6-declarative); the package name is real
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — qml6-module-qtcore package-existence claim; Debian-specific (CMakeLists.txt:446)

### [DEB-N03] qml6-module-qt-labs-platform doesn't exist for Qt 6 — .deb uninstallable  ·  _CONFLICT_  ·  High
`CMakeLists.txt:446`
- **opus:** ❔ UNSURE (45) — qml6-module-qt-labs-platform package-existence claim; Debian-specific (CMakeLists.txt:446)
- **gpt:** ✅ LEGIT (84) — qml6-module-qt-labs-platform doesn't exist for Qt 6 - .deb uninstallable (CMakeLists.txt:446)
- **deepseek:** ✅ LEGIT (95) — CMakeLists.txt:446: qml6-module-qt-labs-platform doesn't exist for Qt 6; qt.labs.platform was dropped; package unsatisfiable
- **glm:** ✅ LEGIT (80) — CMakeLists.txt:446 qml6-module-qt-labs-platform doesn't exist for Qt 6; .deb uninstallable
- **kimi:** ❌ FALSE (85) — qml6-module-qt-labs-platform exists in Ubuntu/Debian Qt6; the package name is real
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — qml6-module-qt-labs-platform package-existence claim; Debian-specific (CMakeLists.txt:446)

### [DEF-N01] Flickable.flicking undefined in Qt 6 — wrong cursor during momentum scroll  ·  _CONFLICT_  ·  Medium
`Prompter.qml:1981,2024`
- **opus:** ❌ FALSE (65) — Flickable.flicking exists in Qt6; not undefined (Prompter.qml:1981)
- **gpt:** ❌ FALSE (76) — Flickable.flicking is a real Qt Quick property (src/prompter/Prompter.qml:1981)
- **deepseek:** ✅ LEGIT (90) — Prompter.qml:1981/2024: Flickable.flicking property renamed to moving in Qt6; resolves to undefined (falsy) — wrong cursor branch during momentum scroll
- **glm:** ✅ LEGIT (75) — Prompter.qml:1981 2024 Flickable.flicking undefined in Qt 6; wrong cursor during momentum scroll
- **kimi:** ✅ LEGIT (75) — Prompter.qml:1981,2024 reference Flickable.flicking, which does not exist in Qt 6; resolves undefined and yields wrong cursor branch.
- **opus-ultra:** ❌ FALSE (65) — Flickable.flicking exists in Qt6; not undefined (Prompter.qml:1981)

### [DETACH-N01] 4 non-const operator[] on QList in keySearch() — unnecessary implicit sharing detach  ·  _CONFLICT_  ·  Low
`markersmodel.cpp:126,133,137,144`
- **opus:** ⚠️ PARTIAL (40) — non-const operator[] detaches QList (markersmodel.cpp:126)
- **gpt:** ⚠️ PARTIAL (58) — observed 4 non-const operator[] on QList in keySearch() - unnecessary implicit sharing detach (src/markersmodel.cpp:126)
- **deepseek:** ✅ LEGIT (75) — markersmodel.cpp:126 133 137 144: non-const operator[] on QModelIndexList forces implicit sharing detach; all uses read-only
- **glm:** ✅ LEGIT (70) — markersmodel.cpp:126 133 137 144 4 non-const operator[] on QList in keySearch; unnecessary implicit sharing detach
- **kimi:** ❌ FALSE (60) — markersmodel.cpp:126,133,137,144 use non-const operator[] on QModelIndexList; in Qt 6 QModelIndexList is QList with reference stability but claim of implicit-sharing detach is speculative and not a verified bug.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — non-const operator[] detaches QList (markersmodel.cpp:126)

### [DPI-02] MarkersDrawer.qml:37 drawer minimumWidth hardcoded to 260px  ·  _CONFLICT_  ·  Low
`MarkersDrawer.qml:37`
- **opus:** ⚠️ PARTIAL (45) — drawer minimumWidth hardcoded 260px (MarkersDrawer.qml:37)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/kirigami_ui/MarkersDrawer.qml:37)
- **deepseek:** ✅ LEGIT (85) — Hardcoded 260px width at MarkersDrawer.qml:37 — ignores DPI scaling
- **glm:** ✅ LEGIT (75) — MarkersDrawer.qml:37 drawer minimumWidth hardcoded to 260px
- **kimi:** ❌ FALSE (75) — MarkersDrawer.qml:37 width is in QML logical pixels, not raw pixels; high-DPR does not halve it. Layout width concern is overstated.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — drawer minimumWidth hardcoded 260px (MarkersDrawer.qml:37)

### [DPI-03] Find.qml:38 searchBarWidth:724 hardcoded in px  ·  _CONFLICT_  ·  Low
`Find.qml:38`
- **opus:** ⚠️ PARTIAL (45) — searchBarWidth:724 hardcoded px (Find.qml:38)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/prompter/Find.qml:38)
- **deepseek:** ✅ LEGIT (90) — Hardcoded 724px searchBarWidth at Find.qml:38 — ignores DPI
- **glm:** ✅ LEGIT (75) — Find.qml:38 searchBarWidth:724 hardcoded in px
- **kimi:** ❌ FALSE (75) — Find.qml:38 width 724 is logical pixels; claim of DPI corruption mischaracterizes QML coordinate system.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — searchBarWidth:724 hardcoded px (Find.qml:38)

### [DSZ-03] Magic number 68 in ListView height binding  ·  _CONFLICT_  ·  Low
`InputsOverlay.qml:83`
- **opus:** ⚠️ PARTIAL (40) — magic number 68 in ListView height (InputsOverlay.qml:83)
- **gpt:** ⚠️ PARTIAL (58) — observed Magic number 68 in ListView height binding (src/kirigami_ui/InputsOverlay.qml:83)
- **deepseek:** ✅ LEGIT (85) — Hardcoded 68px offset at InputsOverlay.qml:83 — brittle vs Kirigami units
- **glm:** ⚠️ PARTIAL (60) — InputsOverlay.qml:83 magic number 68 in ListView height binding
- **kimi:** ❌ FALSE (70) — Subtracting 68 from overlay height is a brittle constant but does not cause a functional failure on its own.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — magic number 68 in ListView height (InputsOverlay.qml:83)

### [EDGE-08] Q_ASSERT as thread-safety guard — removed in release builds  ·  _CONFLICT_  ·  Medium
`src/appcontroller.cpp:36`
- **opus:** ❌ FALSE (80) — Q_ASSERT debug sanity check is normal (appcontroller.cpp:36)
- **gpt:** ❌ FALSE (76) — Q_ASSERT is only an invariant check after singleton creation (src/appcontroller.cpp:36)
- **deepseek:** ✅ LEGIT (75) — Q_ASSERT thread guard at appcontroller.cpp:36 removed in release builds; cross-thread singleton access silently corrupts — should be Q_CHECK_PTR or runtime assert
- **glm:** ✅ LEGIT (85) — appcontroller.cpp:36 Q_ASSERT for thread check is removed in release builds; thread-safety guard ineffective in production
- **kimi:** ✅ LEGIT (80) — appcontroller.cpp:36 Q_ASSERT thread check is removed in release builds.
- **opus-ultra:** ❌ FALSE (80) — Q_ASSERT debug sanity check is normal (appcontroller.cpp:36)

### [EDGE-10] globalShortcutKey() switch without default — fallthrough to Q_UNREACHABLE  ·  _CONFLICT_  ·  Low
`src/globalhotkeys.cpp:513-515`
- **opus:** ❌ FALSE (85) — early return guards it; switch not compiled (globalhotkeys.cpp:111)
- **gpt:** ⚠️ PARTIAL (58) — Q_UNREACHABLE is after compiled switch cases; only future enums matter (src/globalhotkeys.cpp:513)
- **deepseek:** ⚠️ PARTIAL (50) — Q_UNREACHABLE at globalhotkeys.cpp:514 reachable when only QHotkey on Wayland; but depends on specific preprocessor+platform combo — plausible but narrow
- **glm:** ✅ LEGIT (80) — globalhotkeys.cpp:513-515 switch without default falls through to Q_UNREACHABLE; UB if unknown enum value passed
- **kimi:** ✅ LEGIT (70) — globalhotkeys.cpp:513-515 switch lacks default and can fall through to Q_UNREACHABLE on new enum value.
- **opus-ultra:** ❌ FALSE (85) — early return guards it; switch not compiled (globalhotkeys.cpp:111)

### [EDGE-12] QTextBlock::iterator scope fragility in parse()  ·  _CONFLICT_  ·  Low
`src/documenthandler.cpp:1648,1662-1663`
- **opus:** ⚠️ PARTIAL (40) — iterator-outside-loop anti-pattern; report admits 'None currently' (documenthandler.cpp:1648)
- **gpt:** ⚠️ PARTIAL (58) — observed QTextBlock::iterator scope fragility in parse() (src/documenthandler.cpp:1648)
- **deepseek:** ❌ FALSE (40) — Iterator declared outside loop at doc.cpp:1648/1662 is C++ pattern; no continue inside for-body currently; fragile but not a bug without evidence of misuse
- **glm:** ⚠️ PARTIAL (60) — documenthandler.cpp:1648 1662-1663 QTextBlock::iterator jt declared outside loop but reinitialized each iteration; scope is fine
- **kimi:** ✅ LEGIT (60) — documenthandler.cpp:1648,1662-1663 QTextBlock::iterator declared outside loop; fragile anti-pattern but harmless now.
- **opus-ultra:** ❌ FALSE (72) — max: code correct / claim mischaracterized — iterator-outside-loop anti-pattern; report admits 'None currently' (documenthandler.cpp:16

### [EKA-SYS] Systemic absence of EnterKeyAction on ALL TextFields (7 sites)  ·  _CONFLICT_  ·  Low
`PrompterPage.qml (openUrl, wsUrlField, markerHrefField, newWordField), Find.qml (searchField, replaceField), PathsPage.qml (sofficePathField)`
- **opus:** ⚠️ PARTIAL (40) — no EnterKeyAction on TextFields; minor UX (PrompterPage.qml)
- **gpt:** ⚠️ PARTIAL (58) — observed Systemic absence of EnterKeyAction on ALL TextFields (7 sites) (src/kirigami_ui/PrompterPage.qml:1)
- **deepseek:** ⚠️ PARTIAL (65) — EKA-SYS: absence of EnterKeyAction is mobile UX polish not defect; virtual keyboard enter-key label defaults to Return — not all 7 sites verified
- **glm:** ✅ LEGIT (70) — 7 TextFields across PrompterPage.qml Find.qml PathsPage.qml have no EnterKeyAction
- **kimi:** ✅ LEGIT (90) — No EnterKey attached property in src QML; TextFields lack mobile return-key actions.
- **opus-ultra:** ❌ FALSE (72) — max: code correct / claim mischaracterized — no EnterKeyAction on TextFields; minor UX (PrompterPage.qml)

### [EVT-02] Zero inputMethodHints on any TextField — IME broken for CJK/Indic  ·  _CONFLICT_  ·  High
`Prompter.qml:936, PrompterPage.qml, EditorToolbar.qml (15+ TextFields)`
- **opus:** ❌ FALSE (55) — zero inputMethodHints = ImhNone = default; IME works, not broken (Prompter.qml:936)
- **gpt:** ⚠️ PARTIAL (58) — observed Zero inputMethodHints on any TextField - IME broken for CJK/Indic (src/prompter/Prompter.qml:936)
- **deepseek:** ✅ LEGIT (88) — zero inputMethodHints on all TextFields; CJK/Indic IME composition broken (Prompter.qml:936 EditorToolbar PrompterPage)
- **glm:** ✅ LEGIT (80) — Prompter.qml:936 etc TextFields have no inputMethodHints; IME broken for CJK/Indic input
- **kimi:** ✅ LEGIT (85) — No QML file in src/ sets inputMethodHints on any TextField/TextArea, breaking CJK/Indic IME input.
- **opus-ultra:** ❌ FALSE (55) — zero inputMethodHints = ImhNone = default; IME works

### [EVT-N10] Editor Ctrl+Letter shortcuts don't accept event — marker key-search double-fires  ·  _CONFLICT_  ·  Medium
`Prompter.qml:2123-2161`
- **opus:** ❔ UNSURE (45) — editor Ctrl+Letter doesn't accept event; double-handling claim (Prompter.qml:2123)
- **gpt:** ⚠️ PARTIAL (58) — observed Editor Ctrl+Letter shortcuts don't accept event - marker key-search double-fires (src/prompter/Prompter.qml:2123)
- **deepseek:** ✅ LEGIT (70) — Ctrl+Letter shortcuts return without event.accepted=true; secondary handlers fire (Prompter.qml:2123-2161)
- **glm:** ✅ LEGIT (75) — Prompter.qml:2123-2161 Editor Ctrl+Letter shortcuts don't accept event; marker key-search double-fires
- **kimi:** ❌ FALSE (60) — event.accepted set true at Prompter.qml:2117; Ctrl+F/V and plain V are forwarded and returned; no marker-key-search re-fire visible.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — editor Ctrl+Letter doesn't accept event; double-handling claim (Prompter.qml:2123)

### [EVT-N11] windowStayOnTopButton lacks focusPolicy — unreachable via keyboard  ·  _CONFLICT_  ·  Low
`EditorToolbar.qml:794-804`
- **opus:** ⚠️ PARTIAL (45) — windowStayOnTopButton lacks focusPolicy (EditorToolbar.qml:794)
- **gpt:** ⚠️ PARTIAL (58) — observed windowStayOnTopButton lacks focusPolicy - unreachable via keyboard (src/kirigami_ui/EditorToolbar.qml:794)
- **deepseek:** ❌ FALSE (70) — ToolButton implicit default focusPolicy is Qt.StrongFocus; reachable via Tab key (EditorToolbar.qml:794-804)
- **glm:** ✅ LEGIT (75) — EditorToolbar.qml:794-804 windowStayOnTopButton lacks focusPolicy; unreachable via keyboard
- **kimi:** ❌ FALSE (70) — QML ToolButton has default focusPolicy Qt.TabFocus even when not set; claim of keyboard-unreachable is unsupported.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — windowStayOnTopButton lacks focusPolicy (EditorToolbar.qml:794)

### [FINAL-02] Missing `QtQuick.Controls.Material` import — 3 Material references unresolved  ·  _CONFLICT_  ·  Critical
`src/kirigami_ui/WheelSettingsOverlay.qml:59,78,96`
- **opus:** ❌ FALSE (85) — Material via module IMPORTS; 8 files rely on it
- **gpt:** ❌ FALSE (90) — Material is imported at module level via qt_add_qml_module (src/kirigami_ui/WheelSettingsOverlay.qml:59)
- **deepseek:** ❌ FALSE (90) — WheelSettingsOverlay.qml:59/78/96 Material.theme available through QtQuick.Controls 2.12 import itself — separate QtQuick.Controls.Material import not required
- **glm:** ✅ LEGIT (85) — WheelSettingsOverlay.qml:59 78 96 reference Material without importing QtQuick.Controls.Material
- **kimi:** ✅ LEGIT (95) — WheelSettingsOverlay.qml:59,78,96 use Material.theme/Material.Dark but file never imports QtQuick.Controls.Material.
- **opus-ultra:** ❌ FALSE (85) — Material via module IMPORTS; 8 files rely on it

### [FINAL-06] CMAKE_OSX_ARCHITECTURES contains literal quotes — universal binary broken  ·  _CONFLICT_  ·  High
`CMakeLists.txt:418, src/CMakeLists.txt:29`
- **opus:** ✅ LEGIT (90) — set(CMAKE_OSX_ARCHITECTURES=) quote bug (CMakeLists.txt:418)
- **gpt:** ⚠️ PARTIAL (58) — observed CMAKE_OSX_ARCHITECTURES contains literal quotes - universal binary broken (CMakeLists.txt:418)
- **deepseek:** ❌ FALSE (95) — CMakeLists.txt:418 set() with double-quoted value strips quotes per CMake parser rules — value is x86_64;arm64 without literal quotes
- **glm:** ✅ LEGIT (85) — CMakeLists.txt:418 src/CMakeLists.txt:29 CMAKE_OSX_ARCHITECTURES set with quotes='x86_64;arm64' literal string not list
- **kimi:** ✅ LEGIT (95) — CMakeLists.txt:418 and src/CMakeLists.txt:29 use set(CMAKE_OSX_ARCHITECTURES=\x86_64;arm64\")—literal quotes become part of value and break -arch."
- **opus-ultra:** ✅ LEGIT (90) — set(CMAKE_OSX_ARCHITECTURES=) quote bug (CMakeLists.txt:418)

### [FINAL-07] CMake wrong variable name: InstallRequiredSystemLibraries instead of CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS  ·  _CONFLICT_  ·  High
`CMakeLists.txt:414`
- **opus:** ❌ FALSE (80) — include() bundles runtime; set() harmless (CMakeLists.txt:414)
- **gpt:** ❌ FALSE (76) — set() around CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS is harmless here (CMakeLists.txt:414)
- **deepseek:** ❌ FALSE (98) — CMakeLists.txt:412 set(InstallRequiredSystemLibraries On) IS correct CMake variable for that module; CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS is not
- **glm:** ⚠️ PARTIAL (60) — CMakeLists.txt:414 set(InstallRequiredSystemLibraries On) is correct variable name; report claims wrong name but it matches CMake docs
- **kimi:** ✅ LEGIT (95) — CMakeLists.txt:414 sets InstallRequiredSystemLibraries On; correct variable is CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS. MSVC DLLs never bundled.
- **opus-ultra:** ❌ FALSE (80) — include() bundles runtime; set() harmless (CMakeLists.txt:414)

### [FINAL-09] `on__IChanged` handler typo — never fires  ·  _CONFLICT_  ·  Medium
`src/prompter/Prompter.qml:200`
- **opus:** ✅ LEGIT (85) — on__IChanged vs on__iChanged (Prompter.qml:200)
- **gpt:** ✅ LEGIT (92) — onIChanged handler typo - never fires (src/prompter/Prompter.qml:200)
- **deepseek:** ✅ LEGIT (90) — Prompter.qml:200 on__IChanged(capital I) but property at line 173 is __i(lowercase) — handler never fires; __tikTok toggle broken
- **glm:** ❌ FALSE (80) — Prompter.qml:200 on__IChanged is correct QML signal handler capitalization for property __i
- **kimi:** ✅ LEGIT (95) — Prompter.qml:200 declares on__IChanged but property is __i; QML handler names are case-sensitive so it never fires.
- **opus-ultra:** ✅ LEGIT (85) — on__IChanged vs on__iChanged (Prompter.qml:200)

### [FINAL-20] Dangling pointer from temporary QByteArray in marker anchor parsing  ·  _CONFLICT_  ·  High
`src/documenthandler.cpp:1664`
- **opus:** ❌ FALSE (80) — temporary QByteArray alive during QString ctor; no dangling (documenthandler.cpp:1664)
- **gpt:** ❌ FALSE (76) — temporary QByteArray lives through the QString constructor call (src/documenthandler.cpp:1664)
- **deepseek:** ❌ FALSE (90) — documenthandler.cpp:1664 (*constIterator).toUtf8().constData() — temporary QByteArray lives until semicolon; constData() valid for QString construction
- **glm:** ✅ LEGIT (85) — documenthandler.cpp:1664 (*constIterator).toUtf8().constData() returns pointer to temporary QByteArray; dangling
- **kimi:** ✅ LEGIT (90) — documenthandler.cpp:1664 assigns QString from (*constIterator).toUtf8().constData(); temporary QByteArray destroyed, pointer dangles.
- **opus-ultra:** ❌ FALSE (80) — temporary QByteArray alive during QString ctor; no dangling (documenthandler.cpp:1664)

### [FONT-METRIC-03] fontFamily() returns resolved-family not requested-family — substitution invisible  ·  _CONFLICT_  ·  Low
`documenthandler.cpp:493-501`
- **opus:** ❔ UNSURE (40) — fontFamily returns the format's family list; resolved-vs-requested unclear (documenthandler.cpp:500)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/documenthandler.cpp:493)
- **deepseek:** ✅ LEGIT (85) — documenthandler.cpp:493-501: fontFamilies() returns resolved-family list; if user selects unavailable font getter returns substitution name
- **glm:** ✅ LEGIT (70) — documenthandler.cpp:493-501 fontFamily() returns resolved-family not requested-family; substitution invisible
- **kimi:** ❌ FALSE (70) — documenthandler.cpp:493-501 returns font.families() first if set, which is the requested family, not resolved
- **opus-ultra:** ❌ FALSE (72) — max: code correct / claim mischaracterized — fontFamily returns the format's family list; resolved-vs-requested unclear (documenthandle

### [FONT-N01] font.family: "Monospace" never resolves — no such font on any OS  ·  _CONFLICT_  ·  Medium
`TimerClock.qml:149,161`
- **opus:** ⚠️ PARTIAL (45) — 'Monospace' resolves via Qt font matching on most OS (TimerClock.qml:149)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/TimerClock.qml:149)
- **deepseek:** ✅ LEGIT (95) — TimerClock.qml:149/161: font.family:'Monospace' does exact case-insensitive matching; no font named Monospace on any OS — should use families:['monospace'] for CSS generic resolution
- **glm:** ✅ LEGIT (75) — TimerClock.qml:149 161 font.family 'Monospace' is a generic family; may not resolve to actual font
- **kimi:** ✅ LEGIT (70) — TimerClock.qml:149
- **opus-ultra:** ❌ FALSE (72) — max: code correct / claim mischaracterized — 'Monospace' resolves via Qt font matching on most OS (TimerClock.qml:149)

### [GEO-01] main.qml initial 728px height too large for 1366x768 laptops  ·  _CONFLICT_  ·  Low
`main.qml:77-78, +windows/main.qml`
- **opus:** ⚠️ PARTIAL (45) — initial 728px height large for 1366x768 (main.qml:77)
- **gpt:** ⚠️ PARTIAL (58) — observed main.qml initial 728px height too large for 1366x768 laptops (src/kirigami_ui/main.qml:77)
- **deepseek:** ✅ LEGIT (80) — 728px initial height at main.qml:78 + taskbar exceeds 1366x768 desktop area
- **glm:** ✅ LEGIT (75) — main.qml:77-78 initial 728px height too large for 1366x768 laptops
- **kimi:** ❌ FALSE (80) — main.qml:78 height 728 is logical; the file comment explicitly says it was tested for 1366x768 screens.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — initial 728px height large for 1366x768 (main.qml:77)

### [IMH-SYS] Systemic absence of inputMethodHints on ALL TextFields (16 sites)  ·  _CONFLICT_  ·  Medium
`EditorToolbar.qml (10 numeric TextFields), PrompterPage.qml (openUrl, wsUrlField, markerHrefField), PathsPage.qml (sofficePathField), PointerSettings.qml (3 color hex, 4 path TextFields), Find.qml (replaceField)`
- **opus:** ⚠️ PARTIAL (40) — no inputMethodHints on TextFields = ImhNone default; IME still works (EditorToolbar.qml)
- **gpt:** ⚠️ PARTIAL (58) — observed Systemic absence of inputMethodHints on ALL TextFields (16 sites) (src/kirigami_ui/EditorToolbar.qml:1)
- **deepseek:** ⚠️ PARTIAL (65) — IMH-SYS: systemic absence of inputMethodHints on TextFields is a mobile UX concern but design choice not bug; not all 16 sites individually verified
- **glm:** ✅ LEGIT (75) — 16+ TextFields across EditorToolbar.qml PrompterPage.qml PathsPage.qml PointerSettings.qml Find.qml have no inputMethodHints
- **kimi:** ✅ LEGIT (95) — No inputMethodHints anywhere in src QML; numeric/URL TextFields lack proper IME hints.
- **opus-ultra:** ❌ FALSE (72) — max: code correct / claim mischaracterized — no inputMethodHints on TextFields = ImhNone default; IME still works (EditorToolbar.qml)

### [IMP-N02] import QtWebSockets 1.10 — wrong version for Qt 6.5  ·  _CONFLICT_  ·  Critical
`src/prompter/Prompter.qml:80`
- **opus:** ❌ FALSE (65) — QtWebSockets 1.x import resolves on Qt6 target; OBS feature ships (Prompter.qml:80)
- **gpt:** ❌ FALSE (76) — QtWebSockets QML import version is not the project Qt version (src/prompter/Prompter.qml:80)
- **deepseek:** ✅ LEGIT (80) — Prompter.qml:80 imports QtWebSockets 1.10 — Qt6 registers WebSocket under 6.x only; 1.10 not registered per Qt6 module versioning
- **glm:** ⚠️ PARTIAL (60) — Prompter.qml:80 import QtWebSockets 1.10; versioned import works as minimum in Qt 6.5+
- **kimi:** ✅ LEGIT (95) — Prompter.qml:80 imports QtWebSockets 1.10; Qt 6 modules use Qt version numbers (e.g., 6.8), so 1.10 is invalid.
- **opus-ultra:** ❌ FALSE (65) — QtWebSockets 1.x import resolves on Qt6 target; OBS feature ships (Prompter.qml:80)

### [IMP-NEW-01] #include \<qnativeinterface.h\> doesn't exist — breaks Android build  ·  _CONFLICT_  ·  High
`documenthandler.cpp:83`
- **opus:** ❌ FALSE (65) — qnativeinterface.h exists in Qt6 QtCore; Android builds ship (documenthandler.cpp:83)
- **gpt:** ❌ FALSE (76) — qnativeinterface.h is a Qt 6 header (src/documenthandler.cpp:83)
- **deepseek:** ✅ LEGIT (90) — #include <qnativeinterface.h> at documenthandler.cpp:83 — header doesn't exist in Qt 5 or 6
- **glm:** ❌ FALSE (80) — documenthandler.cpp:83 #include <qnativeinterface.h> exists in Qt 6; valid header for Android platform
- **kimi:** ✅ LEGIT (95) — documenthandler.cpp:83 #include <qnativeinterface.h> is not a valid Qt 6 header; the correct access is through QNativeInterface namespace.
- **opus-ultra:** ❌ FALSE (65) — qnativeinterface.h exists in Qt6 QtCore; Android builds ship (documenthandler.cpp:83)

### [IMP-NEW-03] main.cpp:38-39 redundant #include \<QtQml/qqml.h\> + #include \<QtQml\>  ·  _CONFLICT_  ·  Low
`main.cpp:38-39`
- **opus:** ⚠️ PARTIAL (40) — redundant QtQml/qqml.h + QtQml includes (main.cpp:38)
- **gpt:** ⚠️ PARTIAL (58) — observed main.cpp:38-39 redundant #include \QtQml/qqml.h\ + #include \QtQml\ (src/main.cpp:38)
- **deepseek:** ✅ LEGIT (95) — <QtQml/qqml.h> at main.cpp:38 redundant with <QtQml> at line 39 — umbrella already includes it
- **glm:** ✅ LEGIT (75) — main.cpp:38-39 redundant #include <QtQml/qqml.h> + #include <QtQml>; both not needed
- **kimi:** ❌ FALSE (70) — main.cpp:38-39 duplicate include is redundant, not a functional bug.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — redundant QtQml/qqml.h + QtQml includes (main.cpp:38)

### [IMP-NEW-04] AboutPage.qml imports Kirigami 2.9 vs 2.11 in all other files  ·  _CONFLICT_  ·  Low
`AboutPage.qml:22`
- **opus:** ⚠️ PARTIAL (40) — AboutPage imports Kirigami 2.9 vs 2.11; works (AboutPage.qml:22)
- **gpt:** ⚠️ PARTIAL (58) — observed AboutPage.qml imports Kirigami 2.9 vs 2.11 in all other files (src/kirigami_ui/AboutPage.qml:22)
- **deepseek:** ✅ LEGIT (90) — AboutPage.qml:22 imports Kirigami 2.9 — all other files use 2.11 CMake requires 6.9.0=2.11+
- **glm:** ⚠️ PARTIAL (60) — AboutPage.qml:22 imports Kirigami 2.9 vs 2.11 in other files; version difference is benign
- **kimi:** ❌ FALSE (75) — AboutPage.qml:22 imports Kirigami 2.9; KF6 6.9 supports 2.9 imports, so it works today.
- **opus-ultra:** ❌ FALSE (72) — max: code correct / claim mischaracterized — AboutPage imports Kirigami 2.9 vs 2.11; works (AboutPage.qml:22)

### [INIT-N03] ReadRegionOverlay screenMiddle uses root.y from cross-file id resolution  ·  _CONFLICT_  ·  Low
`ReadRegionOverlay.qml:132-134`
- **opus:** ⚠️ PARTIAL (40) — screenMiddle uses root.y cross-file id; resolves via context (ReadRegionOverlay.qml:132)
- **gpt:** ⚠️ PARTIAL (58) — observed ReadRegionOverlay screenMiddle uses root.y from cross-file id resolution (src/prompter/ReadRegionOverlay.qml:132)
- **deepseek:** ⚠️ PARTIAL (40) — root.y cross-file id resolution is valid via QML context scope chain (ReadRegionOverlay.qml:132-134)
- **glm:** ⚠️ PARTIAL (60) — ReadRegionOverlay.qml:132-134 screenMiddle uses root.y from cross-file id resolution; fragile
- **kimi:** ✅ LEGIT (85) — ReadRegionOverlay.qml:132-134 computes screenMiddle using root.y resolved through cross-file id scope; fragile if hierarchy changes
- **opus-ultra:** ❌ FALSE (72) — max: code correct / claim mischaracterized — screenMiddle uses root.y cross-file id; resolves via context (ReadRegionOverlay.qml:132)

### [INIT-N04] PrompterView ShaderEffectSource.sourceItem references prompter id declared later  ·  _CONFLICT_  ·  Low
`PrompterView.qml:230-236`
- **opus:** ⚠️ PARTIAL (40) — sourceItem refs prompter id; QML id resolution is order-independent (PrompterView.qml:230)
- **gpt:** ⚠️ PARTIAL (58) — observed PrompterView ShaderEffectSource.sourceItem references prompter id declared later (src/prompter/PrompterView.qml:230)
- **deepseek:** ❌ FALSE (80) — QML id resolution is order-independent across component scope (PrompterView.qml:230-236)
- **glm:** ⚠️ PARTIAL (60) — PrompterView.qml:230-236 ShaderEffectSource.sourceItem references prompter id declared later; forward reference
- **kimi:** ✅ LEGIT (75) — PrompterView.qml:230-232 ShaderEffectSource.sourceItem references prompter id declared later at line 235; lazy/circular binding can miss first shadow frame
- **opus-ultra:** ❌ FALSE (72) — max: code correct / claim mischaracterized — sourceItem refs prompter id; QML id resolution is order-independent (PrompterView.qml:230)

### [KB-N01] Find.qml: 9 toolbar buttons missing focusPolicy — keyboard-invisible  ·  _CONFLICT_  ·  Medium
`Find.qml`
- **opus:** ⚠️ PARTIAL (45) — 9 Find buttons missing focusPolicy; keyboard (Find.qml)
- **gpt:** ⚠️ PARTIAL (58) — observed Find.qml: 9 toolbar buttons missing focusPolicy - keyboard-invisible (src/prompter/Find.qml:1)
- **deepseek:** ✅ LEGIT (85) — Find.qml ToolButtons lack focusPolicy:Qt.TabFocus; keyboard Tab navigation skips Find toolbar entirely
- **glm:** ✅ LEGIT (65) — Find.qml 9 toolbar buttons missing focusPolicy; keyboard-invisible
- **kimi:** ❌ FALSE (70) — Find.qml ToolButtons inherit AbstractButton default focusPolicy Qt.TabFocus; keyboard focus works
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — 9 Find buttons missing focusPolicy; keyboard (Find.qml)

### [KB-N02] InputsOverlay TabBar TabButtons have no focusPolicy + keyNavigationEnabled: false — keyboard dead  ·  _CONFLICT_  ·  Medium
`InputsOverlay.qml:57-63,85`
- **opus:** ⚠️ PARTIAL (55) — TabButtons no focusPolicy + keyNavigationEnabled:false (InputsOverlay.qml:57)
- **gpt:** ⚠️ PARTIAL (58) — observed InputsOverlay TabBar TabButtons have no focusPolicy + keyNavigationEnabled: false - keyboard de (src/kirigami_ui/InputsOverlay.qml:57)
- **deepseek:** ✅ LEGIT (85) — TabButtons default Qt.NoFocus + keyNavigationEnabled:false; keyboard users cannot switch tabs
- **glm:** ✅ LEGIT (65) — InputsOverlay.qml:57-63 85 TabBar TabButtons have no focusPolicy + keyNavigationEnabled: false; keyboard dead
- **kimi:** ❌ FALSE (65) — InputsOverlay.qml TabButtons use default focusPolicy; keyNavigationEnabled:false only disables arrow-key tab switching
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — TabButtons no focusPolicy + keyNavigationEnabled:false (InputsOverlay.qml:57)

### [KB-N03] +windows and +android ESC handler uses .focus instead of .activeFocus — wrong boolean  ·  _CONFLICT_  ·  Medium
`+windows/main.qml:483, +android/main.qml:422`
- **opus:** ⚠️ PARTIAL (50) — +windows/+android ESC uses .focus where .activeFocus intended (main.qml:483)
- **gpt:** ⚠️ PARTIAL (58) — observed +windows and +android ESC handler uses .focus instead of .activeFocus - wrong boolean (src/kirigami_ui/+windows/main.qml:483)
- **deepseek:** ❌ FALSE (80) — Claim states 'Base main.qml correctly uses activeFocus' but base also uses .focus at lines 509 511 — factually wrong
- **glm:** ✅ LEGIT (70) — +windows/main.qml:483 +android/main.qml:422 ESC handler uses .focus instead of .activeFocus; wrong boolean
- **kimi:** ✅ LEGIT (90) — +windows/main.qml:483 and +android/main.qml:422 test prompter.focus instead of prompter.activeFocus for ESC
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — +windows/+android ESC uses .focus where .activeFocus intended (main.qml:483)

### [LBL-N02] 11 Labels with Layout.bottomMargin: -14 — undefined behavior, overlap risk  ·  _CONFLICT_  ·  Medium
`EditorToolbar.qml (11 Label instances)`
- **opus:** ⚠️ PARTIAL (40) — negative Layout.bottomMargin is valid (overlap) not UB (EditorToolbar.qml)
- **gpt:** ⚠️ PARTIAL (52) — observed 11 Labels with Layout.bottomMargin: -14 - undefined behavior, overlap risk (src/kirigami_ui/EditorToolbar.qml:1)
- **deepseek:** ✅ LEGIT (80) — EditorToolbar.qml: negative Layout.bottomMargin (-14) on RowLayout children is undefined per Qt docs; relies on accidental layout engine behavior
- **glm:** ✅ LEGIT (70) — EditorToolbar.qml 11 Labels with Layout.bottomMargin: -14; undefined behavior overlap risk
- **kimi:** ✅ LEGIT (80) — EditorToolbar.qml 11 Labels inside MouseArea declare Layout.bottomMargin:-14; attached props ignored and negative margin is undefined.
- **opus-ultra:** ❌ FALSE (72) — max: code correct / claim mischaracterized — negative Layout.bottomMargin is valid (overlap) not UB (EditorToolbar.qml)

### [LINK-N04] KF6::GlobalAccel find_package/link mismatch on Haiku  ·  _CONFLICT_  ·  Medium
`CMakeLists.txt:303-308, src/CMakeLists.txt:446-460`
- **opus:** ❔ UNSURE (45) — KF6::GlobalAccel Haiku find/link mismatch; domain (CMakeLists.txt:303)
- **gpt:** ✅ LEGIT (78) — KF6::GlobalAccel findpackage/link mismatch on Haiku (CMakeLists.txt:303)
- **deepseek:** ❌ FALSE (85) — CMakeLists.txt:242-247 already finds KF6::GlobalAccel for non-Win/Apple/Android/WASM which includes Haiku; Haiku-specific block (304-312) adds IconThemes only but GlobalAccel already resolved
- **glm:** ✅ LEGIT (75) — CMakeLists.txt:303-308 src/CMakeLists.txt:446-460 KF6::GlobalAccel find_package/link mismatch on Haiku
- **kimi:** ✅ LEGIT (75) — CMakeLists.txt:306-308 Haiku finds only IconThemes but src/CMakeLists.txt:458 links KF6::GlobalAccel; fragile mismatch.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — KF6::GlobalAccel Haiku find/link mismatch; domain (CMakeLists.txt:303)

### [LL-N02] ProgressIndicator stepSize divide-by-zero when prompter.height is 0  ·  _CONFLICT_  ·  Low
`ProgressIndicator.qml:35`
- **opus:** ✅ LEGIT (55) — stepSize divide-by-zero when prompter.height=0 (ProgressIndicator.qml:35)
- **gpt:** ✅ LEGIT (78) — ProgressIndicator stepSize divide-by-zero when prompter.height is 0 (src/prompter/ProgressIndicator.qml:35)
- **deepseek:** ❌ FALSE (95) — stepSize=prompter.height/(4*(editor.height+...)); prompter.height=0->stepSize=0 not division by zero; denominator uses editor.height
- **glm:** ✅ LEGIT (65) — ProgressIndicator.qml:35 stepSize divide-by-zero when prompter.height is 0
- **kimi:** ❌ FALSE (55) — ProgressIndicator.qml:35 stepSize numerator is prompter.height; zero height yields zero stepSize, not divide-by-zero
- **opus-ultra:** ✅ LEGIT (55) — stepSize divide-by-zero when prompter.height=0 (ProgressIndicator.qml:35)

### [LOAD-N02] reset() emits 12 NOTIFY signals when open() fails but exists() succeeds  ·  _CONFLICT_  ·  Low
`documenthandler.cpp:1017-1018`
- **opus:** ⚠️ PARTIAL (50) — reset() emits ~12 signals when open fails after exists() (documenthandler.cpp:1017)
- **gpt:** ✅ LEGIT (78) — reset() emits 12 NOTIFY signals when open() fails but exists() succeeds (src/documenthandler.cpp:1017)
- **deepseek:** ❌ FALSE (75) — reset() is inside if(file.open()) block; not called when open fails (documenthandler.cpp:1017-1018)
- **glm:** ✅ LEGIT (75) — documenthandler.cpp:1017-1018 reset() emits 12 NOTIFY signals when open() fails but exists() succeeds
- **kimi:** ❌ FALSE (75) — reset() at documenthandler.cpp:1018 is only reached if file.open() succeeds; no signal storm occurs when open fails.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — reset() emits ~12 signals when open fails after exists() (documenthandler.cpp:1017)

### [LOG-09] Trailing comma in constructor member initializer list (non-standard C++ before C++20)  ·  _CONFLICT_  ·  Low
`src/documenthandler.cpp:129`
- **opus:** ❌ FALSE (95) — no trailing comma at documenthandler.cpp:129
- **gpt:** ❌ FALSE (76) — constructor line has no trailing comma after _markersModel (src/documenthandler.cpp:129)
- **deepseek:** ❌ FALSE (80) — Trailing comma in init list valid in C++17; CMAKE_CXX_STANDARD=17 at CMakeLists.txt:48; MSVC /permissive- accepts trailing comma in C++17+ standard mode
- **glm:** ❌ FALSE (80) — documenthandler.cpp:129 trailing comma in initializer list is valid C++11 and the project targets C++17 (CMakeLists.txt:48)
- **kimi:** ✅ LEGIT (75) — documenthandler.cpp:129 trailing comma in ctor initializer list is non-standard before C++20.
- **opus-ultra:** ❌ FALSE (95) — no trailing comma at documenthandler.cpp:129

### [LOG-N04] qWarning("reloading") fires unconditionally — misleading when URL mismatches  ·  _CONFLICT_  ·  Low
`documenthandler.cpp:862`
- **opus:** ❌ FALSE (70) — qWarning('reloading') is inside if(url==m_fileUrl), not unconditional (documenthandler.cpp:862)
- **gpt:** ✅ LEGIT (78) — qWarning("reloading") fires unconditionally - misleading when URL mismatches (src/documenthandler.cpp:862)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:862: qWarning('reloading') fires at top of reload() before url==m_fileUrl check at line 861; incorrectly claims reload on URL mismatch
- **glm:** ✅ LEGIT (70) — documenthandler.cpp:862 qWarning('reloading') fires unconditionally even when URL mismatches
- **kimi:** ❌ FALSE (90) — documenthandler.cpp:861-862 qWarning fires only when url equals m_fileUrl not unconditionally.
- **opus-ultra:** ❌ FALSE (70) — qWarning('reloading') is inside if(url==m_fileUrl)

### [LYR-N03] ContextDrawer exposes prompter actions while viewing layer pages  ·  _CONFLICT_  ·  Medium
`src/kirigami_ui/main.qml:929`
- **opus:** ❔ UNSURE (45) — ContextDrawer exposes prompter actions on layer pages; UX (main.qml:929)
- **gpt:** ✅ LEGIT (78) — ContextDrawer exposes prompter actions while viewing layer pages (src/kirigami_ui/main.qml:929)
- **deepseek:** ✅ LEGIT (88) — depth<=1 true after clear; prompter actions shown on About/Paths pages should be depth<1 (main.qml:929)
- **glm:** ⚠️ PARTIAL (60) — main.qml:929 contextDrawer exposes prompter actions while viewing layer pages; may show irrelevant actions
- **kimi:** ❌ FALSE (80) — main.qml:929 guards contextDrawer actions with layers.depth <= 1; layer pages are pushed via layers.push, so depth > 1 hides actions correctly.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — ContextDrawer exposes prompter actions on layer pages; UX (main.qml:929)

### [NET-02] RedirectPolicyAttribute set to boolean true → NoLessSafeRedirectPolicy  ·  _CONFLICT_  ·  Medium
`documenthandler.cpp:883,1739`
- **opus:** ⚠️ PARTIAL (50) — RedirectPolicyAttribute=true coerces to 1=NoLessSafe; works but imprecise (documenthandler.cpp:883)
- **gpt:** ⚠️ PARTIAL (58) — observed RedirectPolicyAttribute set to boolean true -> NoLessSafeRedirectPolicy (src/documenthandler.cpp:883)
- **deepseek:** ⚠️ PARTIAL (70) — boolean true=1=NoLessSafeRedirectPolicy prevents http->https downgrade; same-origin same-scheme redirects work fine (documenthandler.cpp:883 1739)
- **glm:** ✅ LEGIT (80) — documenthandler.cpp:883 1739 RedirectPolicyAttribute set to boolean true; should be QNetworkRequest::NoLessSafeRedirectPolicy
- **kimi:** ✅ LEGIT (90) — documenthandler.cpp:883 and 1739 set RedirectPolicyAttribute to boolean true, mapping to NoLessSafeRedirectPolicy and dropping same-scheme redirects.
- **opus-ultra:** ❌ FALSE (72) — max: code correct / claim mischaracterized — RedirectPolicyAttribute=true coerces to 1=NoLessSafe; works but imprecise (documenthandler

### [OOB-N03] alignment() fetches textCursor() twice — stale cursor race  ·  _CONFLICT_  ·  Low
`documenthandler.cpp:547-550`
- **opus:** ⚠️ PARTIAL (50) — alignment() double textCursor() fetch; harmless (LOG-07 family) (documenthandler.cpp:547)
- **gpt:** ✅ LEGIT (78) — alignment() fetches textCursor() twice - stale cursor race (src/documenthandler.cpp:547)
- **deepseek:** ✅ LEGIT (85) — textCursor() called twice at documenthandler.cpp:547+550 — second fetch may return different cursor
- **glm:** ⚠️ PARTIAL (60) — documenthandler.cpp:547-550 alignment() fetches textCursor() twice; second call may return stale cursor
- **kimi:** ❌ FALSE (80) — documenthandler.cpp:547-550 fetches textCursor() twice; it is redundant but both calls happen synchronously with no real race.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — alignment() double textCursor() fetch; harmless (LOG-07 family) (documenthandler.cpp:547)

### [PLAT-04] DS_Store.scpt referenced but file does not exist  ·  _CONFLICT_  ·  Medium
`CMakeLists.txt:485`
- **opus:** ❌ FALSE (95) — dist/macOS/DS_Store.scpt exists (7260 bytes)
- **gpt:** ❌ FALSE (90) — the referenced DS_Store.scpt file exists in dist/macOS (CMakeLists.txt:485)
- **deepseek:** ❔ UNSURE (40) — DS_Store.scpt referenced at CMakeLists.txt:485; cannot verify file existence from source code analysis alone
- **glm:** ✅ LEGIT (80) — CMakeLists.txt:485 references DS_Store.scpt but file does not exist in dist/macOS/
- **kimi:** ❌ FALSE (90) — CMakeLists.txt:485 references dist/macOS/DS_Store.scpt and the file exists on disk.
- **opus-ultra:** ❌ FALSE (95) — dist/macOS/DS_Store.scpt exists (7260 bytes)

### [PLAT-05] DBINARY_ICONS_RESOURCE is a typo — should be BINARY_ICONS_RESOURCE  ·  _CONFLICT_  ·  Medium
`CMakeLists.txt:110`
- **opus:** ✅ LEGIT (85) — DBINARY_ICONS_RESOURCE typo (CMakeLists.txt:110)
- **gpt:** ✅ LEGIT (92) — DBINARY_ICONS_RESOURCE is a typo - should be BINARY_ICONS_RESOURCE (CMakeLists.txt:110)
- **deepseek:** ✅ LEGIT (85) — DBINARY_ICONS_RESOURCE at CMakeLists.txt:110 should be BINARY_ICONS_RESOURCE; ECM expects BINARY_ICONS_RESOURCE — typo confirmed; D prefix makes ECM miss it
- **glm:** ❌ FALSE (85) — CMakeLists.txt:110 sets DBINARY_ICONS_RESOURCE which is a custom variable name not a typo; used consistently
- **kimi:** ✅ LEGIT (85) — CMakeLists.txt:110 sets DBINARY_ICONS_RESOURCE; ECM ecm_install_icons expects BINARY_ICONS_RESOURCE.
- **opus-ultra:** ✅ LEGIT (85) — DBINARY_ICONS_RESOURCE typo (CMakeLists.txt:110)

### [PLAT-07] Incorrect macro syntax: `#define Use_GlobalAccel = 1`  ·  _CONFLICT_  ·  Low
`src/globalhotkeys.cpp:29`
- **opus:** ✅ LEGIT (95) — #define Use_GlobalAccel = 1 malformed (dup TYP-06) (globalhotkeys.cpp:29)
- **gpt:** ⚠️ PARTIAL (58) — bad macro expansion is latent; existing preprocessor tests are presence-only (src/globalhotkeys.cpp:29)
- **deepseek:** ✅ LEGIT (85) — Same as TYP-06; #define Use_GlobalAccel = 1 at globalhotkeys.cpp:29 defines to = 1 not 1; latent compile error if #if value-check used
- **glm:** ❌ FALSE (75) — globalhotkeys.cpp:29 #define Use_GlobalAccel = 1 works as existence-only macro; #ifdef checks pass
- **kimi:** ✅ LEGIT (90) — globalhotkeys.cpp:29 malformed #define Use_GlobalAccel = 1 (same as TYP-06).
- **opus-ultra:** ✅ LEGIT (95) — #define Use_GlobalAccel = 1 malformed (dup TYP-06) (globalhotkeys.cpp:29)

### [PLAT-N01] qmlutil.hpp incorrectly excludes QNX from QProcess — run()/restartApplication() silently no-op  ·  _CONFLICT_  ·  Medium
`qmlutil.hpp:35,86,99`
- **opus:** ⚠️ PARTIAL (45) — qmlutil excludes QNX from QProcess; exotic (qmlutil.hpp:35)
- **gpt:** ✅ LEGIT (78) — qmlutil.hpp incorrectly excludes QNX from QProcess - run()/restartApplication() silently no-op (src/qmlutil.hpp:35)
- **deepseek:** ❌ FALSE (85) — QNX NOT excluded from QProcess guard at line 35; QProcess included for QNX (qmlutil.hpp:35)
- **glm:** ✅ LEGIT (80) — qmlutil.hpp:35 86 99 incorrectly excludes QNX from QProcess; run()/restartApplication() silently no-op
- **kimi:** ✅ LEGIT (75) — qmlutil.hpp:35,86,99 excludes Q_OS_QNX from QProcess, so run() and restartApplication() become no-ops on QNX, contradicting Qt's POSIX QProcess support.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — qmlutil excludes QNX from QProcess; exotic (qmlutil.hpp:35)

### [PLAT-N02] documenthandler.cpp incorrectly excludes QNX from import() — LibreOffice broken on QNX  ·  _CONFLICT_  ·  Medium
`documenthandler.h:330, documenthandler.cpp:964,1012,1043`
- **opus:** ❔ UNSURE (40) — import() guard does NOT exclude QNX; LibreOffice-on-QNX claim ambiguous (documenthandler.cpp:964)
- **gpt:** ✅ LEGIT (78) — documenthandler.cpp incorrectly excludes QNX from import() - LibreOffice broken on QNX (src/documenthandler.h:330)
- **deepseek:** ❌ FALSE (85) — QNX NOT in exclusion guard at line 964; import function included for QNX (documenthandler.cpp:964)
- **glm:** ✅ LEGIT (80) — documenthandler.h:330 documenthandler.cpp:964 1012 1043 incorrectly excludes QNX from import(); LibreOffice broken
- **kimi:** ✅ LEGIT (70) — documenthandler.h:330 and documenthandler.cpp:964,1012 guard import() with Android/iOS/WASM/WATCHOS, excluding QNX; rich format import falls through to raw binary handling there.
- **opus-ultra:** ❌ FALSE (72) — max: code correct / claim mischaracterized — import() guard does NOT exclude QNX; LibreOffice-on-QNX claim ambiguous (documenthandler.c

### [PLAT-N03] Zero Q_OS_TVOS preprocessor guards in C++ despite 19 QML references — build failure  ·  _CONFLICT_  ·  High
`All .cpp/.h/.mm (zero Q_OS_TVOS); 19 QML references to "tvos"`
- **opus:** ❔ UNSURE (45) — Q_OS_TVOS C++ guard gap vs QML refs; tvOS not a shipping target (multi-file)
- **gpt:** ❔ UNSURE (39) — tvOS support is unclear; QML strings alone do not prove C++ build failure (src/kirigami_ui/main.qml:45)
- **deepseek:** ❌ FALSE (80) — tvOS is not a shipping target in CMake; no C++ guards needed for unsupported platform
- **glm:** ✅ LEGIT (80) — Zero Q_OS_TVOS preprocessor guards in C++ despite QML references to tvos; build may fail for tvOS
- **kimi:** ✅ LEGIT (90) — No Q_OS_TVOS appears in any C++ source; main.cpp:23 and documenthandler.h QtWidgets-style guards use only Q_OS_IOS, so a tvOS build would pull in QApplication/QtWidgets and fail.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — Q_OS_TVOS C++ guard gap vs QML refs; tvOS not a shipping target (multi-file)

### [PRE-N01] Preprocessor uses `or` instead of `||` in 6 #if directives — MSVC build break  ·  _CONFLICT_  ·  Low
`documenthandler.cpp:132,347,911,1057; globalhotkeys.cpp:560,832`
- **opus:** ⚠️ PARTIAL (55) — 'or' in #if non-portable for strict MSVC; their Windows build tolerates it (documenthandler.cpp:132)
- **gpt:** ⚠️ PARTIAL (58) — observed Preprocessor uses or instead of || in 6 #if directives - MSVC build break (src/documenthandler.cpp:132)
- **deepseek:** ⚠️ PARTIAL (75) — documenthandler.cpp:132 347 911 1057; globalhotkeys.cpp:560 832: #if uses or instead of ||; or is standard C++ alternative token but MSVC with /permissive- rejects it
- **glm:** ❌ FALSE (80) — documenthandler.cpp:132 347 911 1057 globalhotkeys.cpp:560 832 uses 'or' keyword which is valid C++ alternative token for ||
- **kimi:** ✅ LEGIT (85) — documenthandler.cpp:132,347,911,1057 and globalhotkeys.cpp:560,832 use 'or' in #if directives, failing on MSVC /permissive-.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — 'or' in #if non-portable for strict MSVC; their Windows build tolerates it (documenthandle

### [QML-01] 26 references to undefined `pointerSettings` ID in ReadRegionOverlay  ·  _CONFLICT_  ·  Critical
`src/prompter/ReadRegionOverlay.qml:239,246,261,268,293-395`
- **opus:** ❌ FALSE (90) — pointerSettings resolves via context hierarchy (PrompterPage.qml:1442)
- **gpt:** ❌ FALSE (90) — id exists in PrompterPage; overlay uses same parent context (src/prompter/ReadRegionOverlay.qml:239)
- **deepseek:** ❔ UNSURE (30) — pointerSettings id in ReadRegionOverlay.qml may be resolved via C++ context property or parent hierarchy; cannot verify cross-file QML id scope without full component tree
- **glm:** ❌ FALSE (85) — ReadRegionOverlay.qml:239+ references pointerSettings which resolves through QML context hierarchy from ancestor PointerSettings component
- **kimi:** ✅ LEGIT (90) — ReadRegionOverlay.qml:239-395 references pointerSettings id declared only in PrompterPage.qml/PointerSettings.qml; separate-file component cannot resolve it.
- **opus-ultra:** ❌ FALSE (90) — pointerSettings resolves via context hierarchy (PrompterPage.qml:1442)

### [QML-02] Undefined `pointerConfiguration` ID reference in ReadRegionOverlay  ·  _CONFLICT_  ·  Critical
`src/prompter/ReadRegionOverlay.qml:283,288`
- **opus:** ❌ FALSE (90) — pointerConfiguration resolves via context (PrompterPage.qml:1427)
- **gpt:** ❌ FALSE (90) — pointerConfiguration is declared beside the overlay owner (src/prompter/ReadRegionOverlay.qml:283)
- **deepseek:** ❔ UNSURE (30) — pointerConfiguration id likewise depends on instantiation context; ReadRegionOverlay may be instantiated inside PrompterPage scope making id visible
- **glm:** ❌ FALSE (85) — ReadRegionOverlay.qml:283+ pointerConfiguration resolves via QML context from ancestor component in PrompterPage.qml
- **kimi:** ✅ LEGIT (90) — ReadRegionOverlay.qml:283,288 references pointerConfiguration id declared only in PrompterPage.qml; separate component cannot resolve it.
- **opus-ultra:** ❌ FALSE (90) — pointerConfiguration resolves via context (PrompterPage.qml:1427)

### [QML-03] Undefined `root` ID in WindowDragger.qml  ·  _CONFLICT_  ·  Critical
`src/qt/WindowDragger.qml:41,45`
- **opus:** ✅ LEGIT (95) — root undefined in WindowDragger; should be window (WindowDragger.qml:41)
- **gpt:** ✅ LEGIT (92) — Undefined root ID in WindowDragger.qml (src/qt/WindowDragger.qml:41)
- **deepseek:** ✅ LEGIT (75) — WindowDragger.qml uses root at lines 41,45 but no id:root declared; window property at line 28 exists but never referenced — root is undefined
- **glm:** ❌ FALSE (80) — WindowDragger.qml uses root.x/root.y not an undefined root id; the id root is the Item itself
- **kimi:** ✅ LEGIT (90) — WindowDragger.qml:41,45 uses root.x/root.y but no id root in file; property window is unused.
- **opus-ultra:** ✅ LEGIT (95) — root undefined in WindowDragger; should be window (WindowDragger.qml:41)

### [QML-08] Invalid anchor target `undefined`  ·  _CONFLICT_  ·  Medium
`src/kirigami_ui/PrompterPage.qml:807`
- **opus:** ❌ FALSE (80) — anchors.centerIn: undefined is a valid clear-anchor idiom (PrompterPage.qml:807)
- **gpt:** ❌ FALSE (76) — undefined is used here to clear centerIn, not as a target (src/kirigami_ui/PrompterPage.qml:807)
- **deepseek:** ❔ UNSURE (40) — anchors.centerIn:undefined at PrompterPage.qml:807 may be placeholder/default; need full QML context to assess if this line actually executes or is dead
- **glm:** ❌ FALSE (80) — PrompterPage.qml:807 anchor target resolves via QML context; not actually undefined
- **kimi:** ✅ LEGIT (90) — PrompterPage.qml:807 anchors.centerIn: undefined is invalid anchor target.
- **opus-ultra:** ❌ FALSE (80) — anchors.centerIn: undefined is a valid clear-anchor idiom (PrompterPage.qml:807)

### [QML-10] `+android/main.qml` missing `QmlUtil` for RecentDocuments  ·  _CONFLICT_  ·  Medium
`src/kirigami_ui/+android/main.qml:757-762`
- **opus:** ❌ FALSE (85) — existence check null-guarded root.util ? : true (RecentDocuments.qml:164)
- **gpt:** ❌ FALSE (76) — RecentDocuments checks util before fileExists; this part is guarded (src/kirigami_ui/+android/main.qml:757)
- **deepseek:** ❔ UNSURE (45) — +android/main.qml missing QmlUtil for RecentDocuments — depends on whether Android platform variant defines qmlutil elsewhere or inherits from base
- **glm:** ✅ LEGIT (80) — +android/main.qml:757-762 RecentDocuments used without QmlUtil declaration present in android variant
- **kimi:** ✅ LEGIT (90) — +android/main.qml:684 calls qmlutil.factoryReset() without declaring QmlUtil; RecentDocuments also lacks util assignment.
- **opus-ultra:** ❌ FALSE (85) — existence check null-guarded root.util ? : true (RecentDocuments.qml:164)

### [QML-BND-03] ReadRegionOverlay onDestruction — harmless dead code  ·  _CONFLICT_  ·  None (info)
`ReadRegionOverlay.qml:86-89`
- **opus:** ⚠️ PARTIAL (40) — onDestruction harmless dead code; report admits (ReadRegionOverlay.qml:86)
- **gpt:** ⚠️ PARTIAL (58) — observed ReadRegionOverlay onDestruction - harmless dead code (src/prompter/ReadRegionOverlay.qml:86)
- **deepseek:** ✅ LEGIT (95) — Component.onDestruction at ReadRegionOverlay.qml:86 sets state during teardown — harmless dead code
- **glm:** ❌ FALSE (85) — ReadRegionOverlay.qml:86-89 Component.onDestruction is harmless cleanup code not dead code
- **kimi:** ❌ FALSE (70) — ReadRegionOverlay.qml:86-89 Component.onDestruction is redundant but harmless during teardown.
- **opus-ultra:** ❌ FALSE (72) — max: code correct / claim mischaracterized — onDestruction harmless dead code; report admits (ReadRegionOverlay.qml:86)

### [QPROP-N02] comesFromNetwork Q_PROPERTY missing WRITE clause  ·  _CONFLICT_  ·  Medium
`documenthandler.h:121`
- **opus:** ❌ FALSE (50) — comesFromNetwork is intentionally read-only; WRITE not needed (documenthandler.h:121)
- **gpt:** ❌ FALSE (76) — comesFromNetwork is exposed read-only; no WRITE is required (src/documenthandler.h:121)
- **deepseek:** ✅ LEGIT (95) — documenthandler.h:121: Q_PROPERTY comesFromNetwork missing WRITE; setDocumentComesFromNetwork() exists (called at cpp:896) but QML property system sees read-only
- **glm:** ✅ LEGIT (75) — documenthandler.h:121 comesFromNetwork Q_PROPERTY missing WRITE clause; read-only but setDocumentComesFromNetwork exists
- **kimi:** ✅ LEGIT (80) — documenthandler.h:121 comesFromNetwork Q_PROPERTY lacks WRITE despite setDocumentComesFromNetwork existing and emitting NOTIFY.
- **opus-ultra:** ❌ FALSE (50) — comesFromNetwork is intentionally read-only; WRITE not needed (documenthandler.h:121)

### [QT-LC-N01] QQmlFileSelector never instantiated — platform QML file selectors dead  ·  _CONFLICT_  ·  High
`main.cpp:33`
- **opus:** ❌ FALSE (70) — QQmlApplicationEngine auto-installs a file selector; +variants demonstrably load (main.cpp:33)
- **gpt:** ❌ FALSE (76) — QQmlApplicationEngine applies file selectors for +android/+windows (src/main.cpp:33)
- **deepseek:** ✅ LEGIT (95) — main.cpp:33: #include <QQmlFileSelector> present but never instantiated/attached; +windows/+android variants dead; base main.qml loads on all platforms
- **glm:** ⚠️ PARTIAL (60) — main.cpp:33 QQmlFileSelector included but never instantiated; platform QML file selectors may not work
- **kimi:** ❌ FALSE (90) — main.cpp:220 uses QQmlApplicationEngine, which Qt 6 docs say automatically installs a QQmlFileSelector
- **opus-ultra:** ❌ FALSE (70) — QQmlApplicationEngine auto-installs a file selector; +variants demonstrably load (main.cpp:33)

### [R2-CMAKE-01] sphinx_add_docs silently ignores all keyword arguments due to empty cmake_parse_arguments prefix  ·  _CONFLICT_  ·  Critical
`cmake/FindSphinx.cmake:54-56`
- **opus:** ❌ FALSE (80) — empty prefix yields _ALL matching access (FindSphinx.cmake:55)
- **gpt:** ❌ FALSE (76) — empty cmake_parse_arguments prefix intentionally creates _ALL etc. (cmake/FindSphinx.cmake:54)
- **deepseek:** ✅ LEGIT (90) — cmake_parse_arguments empty prefix '' at FindSphinx.cmake:54; all accesses use _ prefixed vars; ALL/BUILDER etc parsed to unprefixed name — all args silently ignored
- **glm:** ✅ LEGIT (85) — cmake/FindSphinx.cmake:54-56 cmake_parse_arguments with empty prefix ''; keyword args parsed correctly actually—this works as intended
- **kimi:** ✅ LEGIT (95) — cmake/FindSphinx.cmake:54-56 cmake_parse_arguments prefix empty; parsed vars ALL/BUILDER not the accessed _ALL/_BUILDER.
- **opus-ultra:** ❌ FALSE (80) — empty prefix yields _ALL matching access (FindSphinx.cmake:55)

### [R2-CMAKE-03] WORKING_DIRECTORY and COMMENT not parseable by callers of sphinx_add_docs  ·  _CONFLICT_  ·  Medium
`cmake/FindSphinx.cmake:67,72`
- **opus:** ✅ LEGIT (80) — WORKING_DIRECTORY/COMMENT absent from keyword lists (FindSphinx.cmake:67)
- **gpt:** ✅ LEGIT (78) — WORKING_DIRECTORY and COMMENT not parseable by callers of sphinx_add_docs (cmake/FindSphinx.cmake:67)
- **deepseek:** ✅ LEGIT (85) — WORKING_DIRECTORY and COMMENT not in cmake_parse_arguments spec at FindSphinx.cmake:67/72; callers cannot set these — affirmed
- **glm:** ❌ FALSE (80) — cmake/FindSphinx.cmake:67 72 WORKING_DIRECTORY and COMMENT are used in add_custom_target; parseable by callers
- **kimi:** ✅ LEGIT (85) — cmake/FindSphinx.cmake:67,72 reads _WORKING_DIRECTORY/_COMMENT but those keywords are absent from :56-58 spec.
- **opus-ultra:** ✅ LEGIT (80) — WORKING_DIRECTORY/COMMENT absent from keyword lists (FindSphinx.cmake:67)

### [R2-GH-01] Q_UNREACHABLE reachable when only QHotkey available on Wayland  ·  _CONFLICT_  ·  High
`src/globalhotkeys.cpp:514`
- **opus:** ❌ FALSE (80) — Use_GlobalAccel defined on all Unix -> unreachable (globalhotkeys.cpp:514)
- **gpt:** ❌ FALSE (76) — Use_GlobalAccel is defined, so the claimed QHotkey-only branch is not built (src/globalhotkeys.cpp:514)
- **deepseek:** ✅ LEGIT (80) — Q_UNREACHABLE at globalhotkeys.cpp:514 reachable when QHotkey_FOUND defined Use_GlobalAccel not defined platform is non-KDE Wayland; confirmed fallthrough path
- **glm:** ✅ LEGIT (80) — globalhotkeys.cpp:514 Q_UNREACHABLE reached when QHotkey is the only backend on Wayland; platform != wayland check skips QHotkey path
- **kimi:** ✅ LEGIT (85) — globalhotkeys.cpp:514 Q_UNREACHABLE reached when QHotkey_FOUND defined, Use_GlobalAccel undefined, and platform is wayland.
- **opus-ultra:** ❌ FALSE (80) — Use_GlobalAccel defined on all Unix -> unreachable (globalhotkeys.cpp:514)

### [R2-PRP-03] Units.LongDuration / Units.HumanMoment missing Kirigami. prefix  ·  _CONFLICT_  ·  Medium
`src/kirigami_ui/PrompterPage.qml:853,860,870,1202`
- **opus:** ❌ FALSE (75) — misdiagnosed; AbstractUnits refs not Kirigami.Units
- **gpt:** ⚠️ PARTIAL (58) — bare Units is broken by AbstractUnits registration, not by Kirigami prefix (src/kirigami_ui/PrompterPage.qml:853)
- **deepseek:** ❔ UNSURE (40) — Units.LongDuration without Kirigami. prefix; depends on import aliasing in PrompterPage.qml; need file's import statements to verify
- **glm:** ✅ LEGIT (85) — PrompterPage.qml:853+ Units.LongDuration/Units.HumanMoment without Kirigami prefix; resolves via AbstractUnits QML_ELEMENT
- **kimi:** ✅ LEGIT (90) — PrompterPage.qml:853,860,870,1202 uses Units.LongDuration/Units.HumanMoment but Kirigami imported as alias; undefined.
- **opus-ultra:** ❌ FALSE (75) — misdiagnosed; AbstractUnits refs not Kirigami.Units

### [R2-PTR-01] Type mismatch: textVerticalOffset declared int but fed a real  ·  _CONFLICT_  ·  Medium
`src/prompter/pointers/pointer_1.qml:33`
- **opus:** ❌ FALSE (75) — int gets scaled readRegion.height*offset/2 not raw slider (pointer_1.qml:33)
- **gpt:** ❌ FALSE (76) — value is scaled before assignment; int truncation is minor (src/prompter/pointers/pointer_1.qml:33)
- **deepseek:** ✅ LEGIT (80) — textVerticalOffset declared int at pointer_1.qml:33; fed real from slider -1.0..1.0 step 0.01; truncation means only +/-1 survive — confirmed type mismatch
- **glm:** ⚠️ PARTIAL (60) — pointer_1.qml:33 textVerticalOffset declared int but QML bindings may assign real; type coercion handles this
- **kimi:** ✅ LEGIT (90) — pointer_1.qml:33 property int textVerticalOffset truncates real slider values from PointerSettings.
- **opus-ultra:** ❌ FALSE (75) — int gets scaled readRegion.height*offset/2 not raw slider (pointer_1.qml:33)

### [R2-PTR-02] Type mismatch: imageVerticalOffset declared int but fed a real  ·  _CONFLICT_  ·  Medium
`src/prompter/pointers/pointer_2.qml:28`
- **opus:** ❌ FALSE (75) — same scaled-value reasoning (pointer_2.qml:28)
- **gpt:** ❌ FALSE (76) — value is scaled before assignment; int truncation is minor (src/prompter/pointers/pointer_2.qml:28)
- **deepseek:** ✅ LEGIT (80) — imageVerticalOffset same pattern at pointer_2.qml:28; int truncation from real slider — confirmed type mismatch
- **glm:** ⚠️ PARTIAL (60) — pointer_2.qml:28 imageVerticalOffset declared int but fed real; QML coerces
- **kimi:** ✅ LEGIT (90) — pointer_2.qml:28 property int imageVerticalOffset truncates real slider values from PointerSettings.
- **opus-ultra:** ❌ FALSE (75) — same scaled-value reasoning (pointer_2.qml:28)

### [R3-APP-01] AppController singleton and children never deallocated  ·  _CONFLICT_  ·  Low
`src/appcontroller.cpp:35,25-28`
- **opus:** ❌ FALSE (75) — app-lifetime singleton; report admits acceptable (appcontroller.cpp:35)
- **gpt:** ❌ FALSE (76) — the singleton is process-lifetime, so this is not an app bug (src/appcontroller.cpp:35)
- **deepseek:** ❌ FALSE (85) — appcontroller.cpp:35 static auto singleton=new AppController() — intentional application-lifetime singleton; OS reclaims on process exit not a leak
- **glm:** ⚠️ PARTIAL (60) — appcontroller.cpp:35 singleton new AppController() never deleted; benign for app-lifetime singleton
- **kimi:** ✅ LEGIT (80) — appcontroller.cpp:35 allocates static AppController singleton and returns it; the object is never deleted, leaking its heap-allocated children too.
- **opus-ultra:** ❌ FALSE (75) — app-lifetime singleton; report admits acceptable (appcontroller.cpp:35)

### [R3-DOC-02] Unbalanced edit block in setLineHeight/setParagraphHeight  ·  _CONFLICT_  ·  Critical
`src/documenthandler.cpp:1596-1601, 1610-1615`
- **opus:** ❌ FALSE (85) — joinPreviousEditBlock balances endEditBlock; no crash
- **gpt:** ❌ FALSE (76) — joinPreviousEditBlock is later closed by endEditBlock (src/documenthandler.cpp:1596)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:1596/1610 cursor.joinPreviousEditBlock() is no-op without active edit block; endEditBlock() without matching beginEditBlock() — unbalanced
- **glm:** ✅ LEGIT (85) — documenthandler.cpp:1596-1601 1610-1615 joinPreviousEditBlock without beginEditBlock; unbalanced edit block
- **kimi:** ❌ FALSE (60) — documenthandler.cpp:1596-1601 and 1610-1615 use joinPreviousEditBlock() paired with endEditBlock(); Qt docs define this as a valid block opener, so no imbalance.
- **opus-ultra:** ❌ FALSE (85) — joinPreviousEditBlock balances endEditBlock; no crash

### [R3-MAIN-01] Command-line positional argument description/syntax swapped  ·  _CONFLICT_  ·  Medium
`src/main.cpp:158`
- **opus:** ❌ FALSE (75) — not swapped args; malformed QLatin1String(char*,char*) (main.cpp:158)
- **gpt:** ✅ LEGIT (78) — Command-line positional argument description/syntax swapped (src/main.cpp:158)
- **deepseek:** ✅ LEGIT (85) — main.cpp:158 addPositionalArgument signature is(name description syntax); passes('source' 'file' 'File to copy.') — description and syntax swapped
- **glm:** ✅ LEGIT (80) — main.cpp:158 addPositionalArgument('source' 'file') has description/syntax swapped; 'file' should describe 'source'
- **kimi:** ✅ LEGIT (85) — main.cpp:158 addPositionalArgument(description=file,syntax=File to copy.) swaps arguments; help output is malformed.
- **opus-ultra:** ❌ FALSE (75) — not swapped args; malformed QLatin1String(char*

### [R3-SIG-02] ShakeDetector signals declared but never emitted — dead feature  ·  _CONFLICT_  ·  Medium
`src/shakedetector.h:40-42, shakedetector.cpp:45-47`
- **opus:** ❌ FALSE (85) — signals emitted in shakedetector.mm (iOS)
- **gpt:** ❌ FALSE (90) — iOS implementation invokes the shake/undo/redo signals (src/shakedetector.h:40)
- **deepseek:** ⚠️ PARTIAL (85) — shakedetector.cpp:45-47 setupShakeDetection empty on non-iOS but shakedetector.mm:35/96/105 properly emits via QMetaObject::invokeMethod on iOS — broken non-iOS only
- **glm:** ✅ LEGIT (85) — shakedetector.h:40-42 shakeDetected/undoRequested/redoRequested signals never emitted in non-iOS shakedetector.cpp
- **kimi:** ❌ FALSE (85) — shakeDetected/undoRequested/redoRequested are emitted via QMetaObject::invokeMethod in shakedetector.mm:35
- **opus-ultra:** ❌ FALSE (85) — signals emitted in shakedetector.mm (iOS)

### [R3-SIG-03] IosSaveDialog accepted/rejected signals declared but never emitted  ·  _CONFLICT_  ·  Medium
`src/iossavedialog.h:44-45, iossavedialog.cpp:44-47`
- **opus:** ❌ FALSE (90) — accepted/rejected emitted in iossavedialog.mm:43,51
- **gpt:** ❌ FALSE (90) — iOS .mm emits accepted and rejected (src/iossavedialog.h:44)
- **deepseek:** ✅ LEGIT (75) — iossavedialog.cpp:44-47 saveDocument no-op with zero emits of accepted()/rejected() signals — iOS save-as flow broken
- **glm:** ✅ LEGIT (85) — iossavedialog.h:44-45 accepted/rejected signals declared but never emitted in non-iOS iossavedialog.cpp
- **kimi:** ❌ FALSE (85) — accepted/rejected signals are emitted in iOS implementation at iossavedialog.mm:42-51; not dead
- **opus-ultra:** ❌ FALSE (90) — accepted/rejected emitted in iossavedialog.mm:43

### [R3-SPL-03] removeCustomWord() silently discards all addWord() additions  ·  _CONFLICT_  ·  Medium
`src/spellchecker.cpp:134-140 vs 338-344`
- **opus:** ❌ FALSE (80) — addWord dead/uncalled; addCustomWord persists correctly (spellchecker.cpp:134)
- **gpt:** ❌ FALSE (76) — addWord is the transient API; persisted custom words use addCustomWord (src/spellchecker.cpp:134)
- **deepseek:** ✅ LEGIT (90) — spellchecker.cpp:134-140 addWord() calls hunspell->add() but never appends to m_customWords; spellchecker.cpp:338-344 removeCustomWord() reloads losing those words
- **glm:** ✅ LEGIT (80) — spellchecker.cpp:134-140 addWord adds to hunspell but removeCustomWord at 328-344 reloads dicts discarding addWord effects
- **kimi:** ✅ LEGIT (80) — spellchecker.cpp:134-140 addWord() modifies live Hunspell objects only; removeCustomWord() at 338-344 reloads dictionaries, discarding prior addWord() additions.
- **opus-ultra:** ❌ FALSE (80) — addWord dead/uncalled; addCustomWord persists correctly (spellchecker.cpp:134)

### [R4-EVT-01] Missing braces on if/else — syntax error in alignRightButton  ·  _CONFLICT_  ·  Critical
`src/kirigami_ui/EditorToolbar.qml:755-758`
- **opus:** ❌ FALSE (85) — brace-less if/else is valid JS (EditorToolbar.qml:755)
- **gpt:** ❌ FALSE (76) — JavaScript if/else without braces is syntactically valid (src/kirigami_ui/EditorToolbar.qml:755)
- **deepseek:** ✅ LEGIT (95) — EditorToolbar.qml:755-758 if without braces controls only next statement; else orphaned — JS syntax error prevents QML load
- **glm:** ❌ FALSE (80) — EditorToolbar.qml:755-758 if/else without braces is valid JS; not a syntax error. QML parser handles dangling else
- **kimi:** ❌ FALSE (90) — alignRightButton if/else lacks braces but remains syntactically valid JS; no syntax error; EditorToolbar.qml:754-758
- **opus-ultra:** ❌ FALSE (85) — brace-less if/else is valid JS (EditorToolbar.qml:755)

### [R4-QTV-01] QtQuick 2.13 import does not exist in Qt 6.5  ·  _CONFLICT_  ·  Critical
`src/prompter/ProjectionsManager.qml:22`
- **opus:** ❌ FALSE (90) — QtQuick 2.13 valid on Qt 6; target 6.8.2
- **gpt:** ❌ FALSE (76) — QtQuick 2.x import remains valid on Qt 6.8.2 (src/prompter/ProjectionsManager.qml:22)
- **deepseek:** ✅ LEGIT (95) — ProjectionsManager.qml:22 imports QtQuick 2.13 — Qt 6 registers QtQuick only as 6.x and 2.15 backward compat; 2.13 not registered
- **glm:** ❌ FALSE (80) — ProjectionsManager.qml:22 import QtQuick 2.13 is a minimum version; valid in Qt 6.8.2
- **kimi:** ✅ LEGIT (80) — ProjectionsManager.qml:22 imports QtQuick 2.13
- **opus-ultra:** ❌ FALSE (90) — QtQuick 2.13 valid on Qt 6; target 6.8.2

### [R4-QTV-02] QtQuick.Window 2.0 import does not exist in Qt 6.5  ·  _CONFLICT_  ·  Critical
`src/prompter/ReadRegionOverlay.qml:25`
- **opus:** ❌ FALSE (90) — QtQuick.Window 2.0 valid on Qt 6.8.2
- **gpt:** ❌ FALSE (76) — QtQuick.Window 2.0 is valid with the 6.8.2 target (src/prompter/ReadRegionOverlay.qml:25)
- **deepseek:** ❔ UNSURE (60) — ReadRegionOverlay.qml:25 imports QtQuick.Window 2.0 — Qt6 may provide version-mapping for 2.x imports but 2.0 predates 2.15 compat; cannot confirm
- **glm:** ❌ FALSE (80) — ReadRegionOverlay.qml:25 import QtQuick.Window 2.0 is minimum; valid in Qt 6
- **kimi:** ✅ LEGIT (80) — ReadRegionOverlay.qml:25 imports QtQuick.Window 2.0
- **opus-ultra:** ❌ FALSE (90) — QtQuick.Window 2.0 valid on Qt 6.8.2

### [R4-ROOT-03] ESC global shortcut skips single-layer pages — can't dismiss with keyboard  ·  _CONFLICT_  ·  Medium
`src/kirigami_ui/main.qml:481`
- **opus:** ❌ FALSE (80) — layers.depth>1 is correct Kirigami idiom (main.qml:481)
- **gpt:** ❌ FALSE (76) — layers.depth > 1 is the expected Kirigami layer-pop guard (src/kirigami_ui/main.qml:481)
- **deepseek:** ✅ LEGIT (90) — main.qml:481 checks layers.depth>1 before clear(); single layer(depth===1) skipped — ESC doesn't dismiss About/Paths/Remote pages
- **glm:** ⚠️ PARTIAL (65) — main.qml:481 ESC handler uses if/else chain; single-layer pages may not dismiss with keyboard
- **kimi:** ✅ LEGIT (90) — ESC handler checks pageStack.layers.depth > 1 so single-layer pages stay open; main.qml:481
- **opus-ultra:** ❌ FALSE (80) — layers.depth>1 is correct Kirigami idiom (main.qml:481)

### [R4-SHD-01] Duplicate class implementation between .cpp and .mm — ODR risk  ·  _CONFLICT_  ·  Medium
`src/shakedetector.cpp:24-43 and shakedetector.mm:45-64`
- **opus:** ❌ FALSE (80) — one TU per platform; no ODR (src/CMakeLists.txt:94)
- **gpt:** ❌ FALSE (76) — CMake selects either .cpp or .mm per platform, not both (src/shakedetector.cpp:24)
- **deepseek:** ✅ LEGIT (90) — shakedetector.cpp:24-43 and shakedetector.mm:45-64 duplicate constructor/instance/create/s_instance — CMake compiles one per platform but maintenance hazard
- **glm:** ⚠️ PARTIAL (65) — shakedetector.cpp:24-43 and shakedetector.mm:45-64 both define ShakeDetector methods; ODR violation but .mm is iOS-only compilation
- **kimi:** ✅ LEGIT (80) — shakedetector.cpp:24-43 and shakedetector.mm:45-64 duplicate constructor/instance/create/s_instance; ODR/maintenance risk per platform.
- **opus-ultra:** ❌ FALSE (80) — one TU per platform; no ODR (src/CMakeLists.txt:94)

### [RAII-N03] QProcess orphan — child process detached on waitForFinished() timeout  ·  _CONFLICT_  ·  Medium
`documenthandler.cpp:1083-1089`
- **opus:** ⚠️ PARTIAL (50) — QProcess child may linger if waitForFinished times out (documenthandler.cpp:1083)
- **gpt:** ✅ LEGIT (78) — QProcess orphan - child process detached on waitForFinished() timeout (src/documenthandler.cpp:1083)
- **deepseek:** ❌ FALSE (70) — QProcess stack object destructor calls close()/kill() in Qt6; no orphan on timeout (documenthandler.cpp:1083-1089)
- **glm:** ✅ LEGIT (80) — documenthandler.cpp:1083-1089 QProcess orphan; child process detached on waitForFinished() timeout
- **kimi:** ❌ FALSE (70) — Local QProcess goes out of scope after waitForFinished failure and its destructor terminates any still-running child process.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — QProcess child may linger if waitForFinished times out (documenthandler.cpp:1083)

### [RESP-N03] +android/main.qml omits all size declarations — transient zero-size layout on startup  ·  _CONFLICT_  ·  Low
`+android/main.qml`
- **opus:** ⚠️ PARTIAL (45) — +android omits size declarations; transient zero-size (main.qml)
- **gpt:** ⚠️ PARTIAL (58) — observed +android/main.qml omits all size declarations - transient zero-size layout on startup (src/kirigami_ui/+android/main.qml:1)
- **deepseek:** ❌ FALSE (85) — +android/main.qml is dead code (QML file selectors never instantiated per QT-LC-N01); base main.qml always loads with proper width/height
- **glm:** ✅ LEGIT (65) — +android/main.qml omits all size declarations; transient zero-size layout on startup
- **kimi:** ✅ LEGIT (70) — +android/main.qml lacks explicit width/height/minimumWidth; relies only on Settings aliases
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — +android omits size declarations; transient zero-size (main.qml)

### [RND-N01] forceQtTextRenderer dead on Apple platforms — unconditionally uses NativeRendering  ·  _CONFLICT_  ·  Low
`Prompter.qml:994`
- **opus:** ⚠️ PARTIAL (50) — forceQtTextRenderer dead on Apple (always NativeRendering) (Prompter.qml:994)
- **gpt:** ⚠️ PARTIAL (58) — observed forceQtTextRenderer dead on Apple platforms - unconditionally uses NativeRendering (src/prompter/Prompter.qml:994)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:994: iOS/osx short-circuit to NativeRendering unconditionally before evaluating root.forceQtTextRenderer
- **glm:** ✅ LEGIT (70) — Prompter.qml:994 forceQtTextRenderer dead on Apple platforms; unconditionally uses NativeRendering
- **kimi:** ❌ FALSE (70) — Prompter.qml:994 does evaluate `root.forceQtTextRenderer` on non-Apple; claim says Apple branch dead. Conditional is valid; toggle works on other platforms; not solely a code bug.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — forceQtTextRenderer dead on Apple (always NativeRendering) (Prompter.qml:994)

### [RPL-N01] 6 additional files missing QtQuick.Controls.Material import — ~65 controls unthemed  ·  _CONFLICT_  ·  Medium
`Find.qml, PrompterView.qml, Prompter.qml, PrompterPage.qml, EditorToolbar.qml, InputsOverlay.qml`
- **opus:** ❌ FALSE (55) — Material provided module-wide via qt_add_qml_module IMPORTS (dup FINAL-02)
- **gpt:** ❌ FALSE (76) — Material is supplied by module imports, not each individual QML file (src/prompter/Find.qml:1)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml/Find.qml/EditorToolbar.qml all use Material.theme without importing QtQuick.Controls.Material; ~65 controls unthemed
- **glm:** ✅ LEGIT (70) — 6 files missing QtQuick.Controls.Material import; ~65 controls unthemed
- **kimi:** ❌ FALSE (90) — src/CMakeLists.txt:254-255 imports QtQuick.Controls.Material module-wide, so controls in those files are themed
- **opus-ultra:** ❌ FALSE (55) — Material provided module-wide via qt_add_qml_module IMPORTS (dup FINAL-02)

### [SCRL-N05] __speedLimit check is dead logic — always true  ·  _CONFLICT_  ·  Low
`Prompter.qml:129,494,510`
- **opus:** ⚠️ PARTIAL (50) — __speedLimit check claimed always-true; needs full expr (Prompter.qml:129)
- **gpt:** ⚠️ PARTIAL (58) — observed speedLimit check is dead logic - always true (src/prompter/Prompter.qml:129)
- **deepseek:** ❌ FALSE (65) — __speedLimit=__vw*100=width pixels; velocity reachable at high __i values (Prompter.qml:129 494 510)
- **glm:** ⚠️ PARTIAL (60) — Prompter.qml:129 494 510 __speedLimit check is dead logic; always true
- **kimi:** ✅ LEGIT (80) — Prompter.qml:129 defines __speedLimit=__vw*100 (viewport width); checks at 494/510 compare velocity against that limit but legit velocities never reach it, making guard effectively dead.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — __speedLimit check claimed always-true; needs full expr (Prompter.qml:129)

### [SCRL-N06] __timeToEnd uses unexplained 2× factor  ·  _CONFLICT_  ·  Low
`Prompter.qml:122, TimerClock.qml:66`
- **opus:** ⚠️ PARTIAL (40) — __timeToEnd 2x factor is documented intent, not a bug (Prompter.qml:122)
- **gpt:** ⚠️ PARTIAL (58) — observed timeToEnd uses unexplained 2× factor (src/prompter/Prompter.qml:122)
- **deepseek:** ❌ FALSE (60) — 2x factor consistent with identical fallback calc at TimerClock.qml:66 (Prompter.qml:122)
- **glm:** ⚠️ PARTIAL (55) — Prompter.qml:122 TimerClock.qml:66 __timeToEnd uses unexplained 2× factor
- **kimi:** ✅ LEGIT (75) — Prompter.qml:122 computes __timeToEnd with an unexplained 2* multiplier, repeated in TimerClock.qml:66 fallback; no documentation, doubling ETA vs simple distance/rate.
- **opus-ultra:** ❌ FALSE (72) — max: code correct / claim mischaracterized — __timeToEnd 2x factor is documented intent

### [SET-03] QString "true" used as default for boolean QSettings value  ·  _CONFLICT_  ·  Low
`documenthandler.cpp:137`
- **opus:** ⚠️ PARTIAL (50) — string 'true' default for bool toBool() works correctly; cosmetic (documenthandler.cpp:137)
- **gpt:** ✅ LEGIT (78) — QString "true" used as default for boolean QSettings value (src/documenthandler.cpp:137)
- **deepseek:** ✅ LEGIT (85) — Default 'true' (QString) for bool QSettings at documenthandler.cpp:137 — fragile cross-type conversion
- **glm:** ✅ LEGIT (75) — documenthandler.cpp:137 QString 'true' used as default for boolean QSettings value instead of bool
- **kimi:** ❌ FALSE (75) — documenthandler.cpp:137 QVariant converts the default QString \true\" to bool correctly; no functional bug."
- **opus-ultra:** ❌ FALSE (72) — max: code correct / claim mischaracterized — string 'true' default for bool toBool() works correctly; cosmetic (documenthandler.cpp:137

### [SET-04] spellCheckLanguages read without explicit default value  ·  _CONFLICT_  ·  Low
`documenthandler.cpp:153`
- **opus:** ⚠️ PARTIAL (45) — spellCheckLanguages read; empty-list default is fine (documenthandler.cpp:153)
- **gpt:** ✅ LEGIT (78) — spellCheckLanguages read without explicit default value (src/documenthandler.cpp:153)
- **deepseek:** ✅ LEGIT (85) — settings.value() without default at documenthandler.cpp:153 — inconsistent with all other calls
- **glm:** ✅ LEGIT (75) — documenthandler.cpp:153 spellCheckLanguages read without explicit default value
- **kimi:** ❌ FALSE (75) — documenthandler.cpp:153 missing default returns a null QVariant; toStringList yields an empty list, which is handled.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — spellCheckLanguages read; empty-list default is fine (documenthandler.cpp:153)

### [SHADOW-01] id: rotation shadows Item.rotation property  ·  _CONFLICT_  ·  Low
`Prompter.qml:1280`
- **opus:** ✅ LEGIT (60) — id: rotation shadows Item.rotation property (Prompter.qml:1280)
- **gpt:** ✅ LEGIT (78) — id: rotation shadows Item.rotation property (src/prompter/Prompter.qml:1280)
- **deepseek:** ✅ LEGIT (85) — Rotation id:rotation shadows Item.rotation qreal; bare rotation resolves to Rotation object not float (Prompter.qml:1280)
- **glm:** ⚠️ PARTIAL (60) — Prompter.qml:1280 id: rotation shadows Item.rotation property; ambiguous in context
- **kimi:** ❌ FALSE (80) — id:rotation names the Rotation transform and is correctly used as its target; current code does not confuse it with Item.rotation.
- **opus-ultra:** ✅ LEGIT (60) — id: rotation shadows Item.rotation property (Prompter.qml:1280)

### [SHADOW-02] id: flow shadows Flow.flow property  ·  _CONFLICT_  ·  Low
`EditorToolbar.qml:184`
- **opus:** ✅ LEGIT (55) — id: flow shadows Flow.flow property (EditorToolbar.qml:184)
- **gpt:** ✅ LEGIT (78) — id: flow shadows Flow.flow property (src/kirigami_ui/EditorToolbar.qml:184)
- **deepseek:** ✅ LEGIT (85) — Flow id:flow shadows Flow.flow enum; accessing flow direction requires awkward flow.flow (EditorToolbar.qml:184)
- **glm:** ⚠️ PARTIAL (60) — EditorToolbar.qml:184 id: flow shadows Flow.flow property; ambiguous in context
- **kimi:** ❌ FALSE (80) — id:flow names the Flow item; no current use of the Flow.flow enum conflicts, so this is only a naming smell.
- **opus-ultra:** ✅ LEGIT (55) — id: flow shadows Flow.flow property (EditorToolbar.qml:184)

### [SHADOW-N03] id: stopwatch shadows property bool stopwatch — timersEnabled always true  ·  _CONFLICT_  ·  High
`TimerClock.qml:38,122,100`
- **opus:** ✅ LEGIT (70) — id: stopwatch (Item) shadows property bool stopwatch -> timersEnabled always true (TimerClock.qml:38)
- **gpt:** ✅ LEGIT (84) — id: stopwatch shadows property bool stopwatch - timersEnabled always true (src/prompter/TimerClock.qml:38)
- **deepseek:** ❌ FALSE (75) — property bool stopwatch resolves before child Item id; timersEnabled correctly depends on property (TimerClock.qml:38 100 122)
- **glm:** ✅ LEGIT (75) — TimerClock.qml:38 122 100 id: stopwatch shadows property bool stopwatch; timersEnabled always true
- **kimi:** ✅ LEGIT (95) — TimerClock.qml:122 id stopwatch shadows property bool stopwatch; line 100 stopwatch||eta resolves to Item (truthy), ignoring toggles.
- **opus-ultra:** ✅ LEGIT (70) — id: stopwatch (Item) shadows property bool stopwatch -> timersEnabled always true (TimerClock.qml:38)

### [SHADOW-N04] id: frame shadows property bool frame — latent hazard  ·  _CONFLICT_  ·  Low
`Countdown.qml:42,152`
- **opus:** ⚠️ PARTIAL (50) — id: frame may shadow property bool frame; latent (Countdown.qml:42)
- **gpt:** ✅ LEGIT (78) — id: frame shadows property bool frame - latent hazard (src/prompter/Countdown.qml:42)
- **deepseek:** ✅ LEGIT (65) — Shape id:frame shadows property bool frame; access within Countdown ambiguous (Countdown.qml:42 152)
- **glm:** ⚠️ PARTIAL (60) — Countdown.qml:42 152 id: frame shadows property bool frame; latent hazard
- **kimi:** ❌ FALSE (65) — Countdown.qml:42 id frame shadows bool frame, but no bare 'frame' reference exists currently; latent hazard only.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — id: frame may shadow property bool frame; latent (Countdown.qml:42)

### [SHDR-N02] id: shadow collides with property ShaderEffectSource shadow — ambiguous resolution in blur chain  ·  _CONFLICT_  ·  Medium
`Prompter.qml:746,752,754,759,762`
- **opus:** ✅ LEGIT (60) — id: shadow collides with property ShaderEffectSource shadow (Prompter.qml:746)
- **gpt:** ⚠️ PARTIAL (58) — observed id: shadow collides with property ShaderEffectSource shadow - ambiguous resolution in blur chai (src/prompter/Prompter.qml:746)
- **deepseek:** ❌ FALSE (85) — id:shadow takes priority over property shadow in QML scope; shadow.source correctly resolves to prompterShadowSource not self-ref
- **glm:** ✅ LEGIT (65) — Prompter.qml:746 752 754 759 762 id: shadow collides with property ShaderEffectSource shadow; ambiguous resolution
- **kimi:** ✅ LEGIT (85) — Prompter.qml:746 id:shadow collides with the readonly property ShaderEffectSource shadow declared at :752
- **opus-ultra:** ✅ LEGIT (60) — id: shadow collides with property ShaderEffectSource shadow (Prompter.qml:746)

### [SPL2-20] loadCustomWordsFromDisk redundant exists() before open()  ·  _CONFLICT_  ·  Low
`spellchecker.cpp:365-368`
- **opus:** ⚠️ PARTIAL (45) — loadCustomWordsFromDisk redundant exists() before open() (spellchecker.cpp:365)
- **gpt:** ⚠️ PARTIAL (58) — observed loadCustomWordsFromDisk redundant exists() before open() (src/spellchecker.cpp:365)
- **deepseek:** ❌ FALSE (85) — exists() before open() is defensive programming preventing TOCTOU race; not redundant best practice (spellchecker.cpp:365-368)
- **glm:** ✅ LEGIT (75) — spellchecker.cpp:365-368 redundant exists() before open(); open() checks existence internally
- **kimi:** ✅ LEGIT (70) — spellchecker.cpp:365-368 checks file.exists() before open(); redundant because open() already reports failure.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — loadCustomWordsFromDisk redundant exists() before open() (spellchecker.cpp:365)

### [STATE-N01] Shadowed Prompting→Editing transition — velocity default never saved  ·  _CONFLICT_  ·  High
`Prompter.qml:3119-3137`
- **opus:** ❔ UNSURE (45) — shadowed Prompting->Editing transition claim; needs state-machine trace (Prompter.qml:3119)
- **gpt:** ✅ LEGIT (84) — Shadowed Prompting->Editing transition - velocity default never saved (src/prompter/Prompter.qml:3119)
- **deepseek:** ⚠️ PARTIAL (50) — specific Prompting->Editing transition(line 3129) takes priority over general(line 3119) per QML rules (Prompter.qml:3119-3137)
- **glm:** ✅ LEGIT (80) — Prompter.qml:3119-3137 Shadowed Prompting→Editing transition; velocity default never saved
- **kimi:** ❌ FALSE (70) — Transition from Prompting to Editing at Prompter.qml:3127-3137 sets __iDefault when __i>0; generic to-Editing transition is not shadowed.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — shadowed Prompting->Editing transition claim; needs state-machine trace (Prompter.qml:3119

### [STC-N02] Find.qml close() doesn't reset replace-mode or regex-mode flags  ·  _CONFLICT_  ·  Low
`Find.qml:58-62`
- **opus:** ⚠️ PARTIAL (45) — close() doesn't reset replace/regex flags (Find.qml:58)
- **gpt:** ⚠️ PARTIAL (58) — observed Find.qml close() doesn't reset replace-mode or regex-mode flags (src/prompter/Find.qml:58)
- **deepseek:** ✅ LEGIT (85) — Find.qml:58-62: close() sets isOpen=false focusSearch() but doesn't reset find.replace or find.regEx; stale mode carried to next session
- **glm:** ✅ LEGIT (65) — Find.qml:58-62 close() doesn't reset replace-mode or regex-mode flags
- **kimi:** ❌ FALSE (60) — Find.qml:58-62 close() clears the search field; persisting replace/regex mode is common UX, not a defect
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — close() doesn't reset replace/regex flags (Find.qml:58)

### [STC-N03] velocityIndicator.firstResetDone never cleared on dismiss — second activation broken  ·  _CONFLICT_  ·  Medium
`PrompterPage.qml:799-872,928-937`
- **opus:** ❔ UNSURE (45) — velocityIndicator.firstResetDone not cleared on dismiss; domain (PrompterPage.qml:799)
- **gpt:** ⚠️ PARTIAL (58) — observed velocityIndicator.firstResetDone never cleared on dismiss - second activation broken (src/kirigami_ui/PrompterPage.qml:799)
- **deepseek:** ✅ LEGIT (90) — PrompterPage.qml:928-937: dismiss() never clears firstResetDone/originX/Y; second activation cursor warps to page-middle not indicator-center
- **glm:** ✅ LEGIT (70) — PrompterPage.qml:799-872 928-937 velocityIndicator.firstResetDone never cleared on dismiss; second activation broken
- **kimi:** ❌ FALSE (65) — velocityIndicator.firstResetDone is set to false on every activation (PrompterPage.qml:900); stale-on-dismiss not shown
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — velocityIndicator.firstResetDone not cleared on dismiss; domain (PrompterPage.qml:799)

### [STR-CNV] 5 defensive validation gaps: toInt() without ok flag in getMarkerKey, parse(×2), setFontSize, and 32 hotkey reads  ·  _CONFLICT_  ·  Low
`documenthandler.cpp:757,1667,1675,829, globalhotkeys.cpp:569-698`
- **opus:** ⚠️ PARTIAL (45) — several toInt() without ok flag; defensive gap (documenthandler.cpp:757)
- **gpt:** ✅ LEGIT (78) — 5 defensive validation gaps: toInt() without ok flag in getMarkerKey, parse(×2), setFontSize, and 32 hotkey reads (src/documenthandler.cpp:757)
- **deepseek:** ✅ LEGIT (60) — multiple toInt() calls without ok flag silently discard parse failures (documenthandler.cpp:757 829)
- **glm:** ✅ LEGIT (75) — documenthandler.cpp:757 1667 1675 829 globalhotkeys.cpp:569-698 5 defensive validation gaps: toInt() without ok flag
- **kimi:** ❌ FALSE (60) — documenthandler.cpp:757/1667/1675 and globalhotkeys.cpp:569-698 use toInt() without ok flag, but 0 default matches intended sentinel; no defect.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — several toInt() without ok flag; defensive gap (documenthandler.cpp:757)

### [TB-N04] velocityDragArea accepts MiddleButton without propagateComposedEvents — scroll blocked  ·  _CONFLICT_  ·  Medium
`PrompterPage.qml:875-884`
- **opus:** ⚠️ PARTIAL (50) — velocityDragArea accepts MiddleButton without propagateComposedEvents (PrompterPage.qml:875)
- **gpt:** ⚠️ PARTIAL (58) — observed velocityDragArea accepts MiddleButton without propagateComposedEvents - scroll blocked (src/kirigami_ui/PrompterPage.qml:875)
- **deepseek:** ✅ LEGIT (85) — PrompterPage.qml:875-884: velocityDragArea accepts MiddleButton without propagateComposedEvents; middle-click consumed scroll through viewport blocked
- **glm:** ✅ LEGIT (70) — PrompterPage.qml:875-884 velocityDragArea accepts MiddleButton without propagateComposedEvents; scroll blocked
- **kimi:** ❌ FALSE (60) — PrompterPage.qml:881 accepts MiddleButton but sets mouse.accepted=false for unhandled cases, so events propagate
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — velocityDragArea accepts MiddleButton without propagateComposedEvents (PrompterPage.qml:87

### [TBND-N02] All CJK text marked misspelled — ideographic characters not in Hunspell dictionaries  ·  _CONFLICT_  ·  Medium
`spellhighlighter.cpp:53-54`
- **opus:** ⚠️ PARTIAL (50) — CJK marked misspelled; ideographs not in hunspell (spellhighlighter.cpp:53)
- **gpt:** ⚠️ PARTIAL (58) — observed All CJK text marked misspelled - ideographic characters not in Hunspell dictionaries (src/spellhighlighter.cpp:53)
- **deepseek:** ✅ LEGIT (90) — \p{L} matches CJK chars individually; Hunspell has zero ideograph entries->all CJK flagged misspelled at spellhighlighter.cpp:53-54
- **glm:** ✅ LEGIT (70) — spellhighlighter.cpp:53-54 all CJK text marked misspelled; ideographic characters not in Hunspell dictionaries
- **kimi:** ❌ FALSE (55) — CJK characters are matched by \\p{L}; all-CJK misspelled only when no suitable Hunspell dictionary is loaded
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — CJK marked misspelled; ideographs not in hunspell (spellhighlighter.cpp:53)

### [TC-N02] property color value assigned string expression — silent coercion  ·  _CONFLICT_  ·  Low
`PointerSettings.qml:146,178,209`
- **opus:** ⚠️ PARTIAL (45) — property color assigned string expression; coercion (PointerSettings.qml:146)
- **gpt:** ⚠️ PARTIAL (58) — observed property color value assigned string expression - silent coercion (src/prompter/PointerSettings.qml:146)
- **deepseek:** ✅ LEGIT (80) — PointerSettings.qml:146 178 209: property color value assigned from text (string) via ternary; silent string->color coercion
- **glm:** ✅ LEGIT (65) — PointerSettings.qml:146 178 209 property color value assigned string expression; silent coercion
- **kimi:** ❌ FALSE (60) — PointerSettings.qml:146/178/209 stores valid color strings in a color property; QML coercion is normal
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — property color assigned string expression; coercion (PointerSettings.qml:146)

### [TXT-N02] TimerClock default text color #AAA on #131619 — fails WCAG AA contrast  ·  _CONFLICT_  ·  Low
`TimerClock.qml:93,138,151,163`
- **opus:** ⚠️ PARTIAL (40) — #AAA on #131619 contrast (TimerClock.qml:93)
- **gpt:** ✅ LEGIT (78) — TimerClock default text color #AAA on #131619 - fails WCAG AA contrast (src/prompter/TimerClock.qml:93)
- **deepseek:** ✅ LEGIT (75) — #AAA on #131619 yields ~2.5:1 contrast ratio failing WCAG AA 4.5:1 minimum (TimerClock.qml:93 138)
- **glm:** ✅ LEGIT (75) — TimerClock.qml:93 138 151 163 #AAA text on #131619 background fails WCAG AA contrast
- **kimi:** ❌ FALSE (90) — TimerClock.qml:93 default color '#AAA' on background '#131619' (very dark) gives a high-contrast light-on-dark pairing; the claimed 3.16:1 WCAG failure is incorrect.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — #AAA on #131619 contrast (TimerClock.qml:93)

### [TYP-01] Dangling pointer from temporary std::string in SpellChecker::loadOne  ·  _CONFLICT_  ·  High
`src/spellchecker.cpp:154-155`
- **opus:** ❌ FALSE (80) — get_dict_encoding returns const std::string& -> not dangling (spellchecker.cpp:154)
- **gpt:** ❔ UNSURE (39) — Hunspell header is not in-tree, so return lifetime cannot be proven here (src/spellchecker.cpp:154)
- **deepseek:** ✅ LEGIT (95) — get_dict_encoding().c_str() at spellchecker.cpp:154 returns temp std::string; enc dangles at semicolon; QByteArray(enc) reads freed memory — UB confirmed
- **glm:** ✅ LEGIT (85) — spellchecker.cpp:154-155 affPath/dicPath are QByteArray from toLocal8Bit stored as local vars then passed to Hunspell; not dangling
- **kimi:** ✅ LEGIT (95) — spellchecker.cpp:154-155 calls c_str() on temporary std::string from get_dict_encoding(); pointer dangles before QByteArray read.
- **opus-ultra:** ❌ FALSE (80) — get_dict_encoding returns const std::string& -> not dangling (spellchecker.cpp:154)

### [TYP-02] Invalid Qt::LayoutDirection enum value cast  ·  _CONFLICT_  ·  Medium
`src/main.cpp:166`
- **opus:** ❌ FALSE (90) — LayoutDirectionAuto=2 valid; no UB (main.cpp:166)
- **gpt:** ❌ FALSE (76) — 2 maps to Qt layout auto, not an out-of-range enum value (src/main.cpp:166)
- **deepseek:** ✅ LEGIT (90) — static_cast<Qt::LayoutDirection>(2-setting) at main.cpp:166; when setting=0 -> 2 is not valid enum value (only 0=LeftToRight 1=RightToLeft) — UB
- **glm:** ⚠️ PARTIAL (55) — main.cpp:166 static_cast<Qt::LayoutDirection>(2 - value) produces valid LayoutDirection for 0/1/2 input; not out-of-range for expected values
- **kimi:** ✅ LEGIT (90) — main.cpp:166 static_cast<Qt::LayoutDirection>(2 - setting) yields value 2 when setting=0, outside enum.
- **opus-ultra:** ❌ FALSE (90) — LayoutDirectionAuto=2 valid; no UB (main.cpp:166)

### [TYP-06] Malformed preprocessor macro: `#define Use_GlobalAccel = 1`  ·  _CONFLICT_  ·  Low
`src/globalhotkeys.cpp:29`
- **opus:** ✅ LEGIT (95) — #define Use_GlobalAccel = 1 malformed (globalhotkeys.cpp:29)
- **gpt:** ⚠️ PARTIAL (58) — macro value is malformed but current uses are #ifdef/defined only (src/globalhotkeys.cpp:29)
- **deepseek:** ✅ LEGIT (85) — #define Use_GlobalAccel = 1 at globalhotkeys.cpp:29 defines to = 1 not 1; currently only #ifdef tested so benign but any #if value check would fail
- **glm:** ❌ FALSE (75) — globalhotkeys.cpp:29 #define Use_GlobalAccel = 1 defines macro as '= 1' but #ifdef checks only test existence not value; works as intended
- **kimi:** ✅ LEGIT (90) — globalhotkeys.cpp:29 #define Use_GlobalAccel = 1 defines macro to token sequence = 1, not numeric 1.
- **opus-ultra:** ✅ LEGIT (95) — #define Use_GlobalAccel = 1 malformed (globalhotkeys.cpp:29)

### [TYP-08] DocumentHandler constructor trailing comma in initializer list  ·  _CONFLICT_  ·  Low
`src/documenthandler.cpp:129`
- **opus:** ❌ FALSE (95) — no trailing comma at line 129 (dup of LOG-09)
- **gpt:** ❌ FALSE (76) — same constructor line contains no trailing comma (src/documenthandler.cpp:129)
- **deepseek:** ❌ FALSE (80) — Same trailing-comma claim as LOG-09; valid C++17 per CMakeLists.txt:48; MSVC accepts trailing comma in C++17+
- **glm:** ❌ FALSE (85) — documenthandler.cpp:129 trailing comma in initializer list is valid C++11+; project uses C++17
- **kimi:** ✅ LEGIT (75) — documenthandler.cpp:129 trailing comma in initializer list (same issue as LOG-09).
- **opus-ultra:** ❌ FALSE (95) — no trailing comma at line 129 (dup of LOG-09)

### [TYP-10] Uninitialized marker struct fields: length defaults to 1  ·  _CONFLICT_  ·  Low
`src/marker.hpp:48`
- **opus:** ❌ FALSE (55) — length=1 default is correct; report itself says not-a-bug (marker.hpp:48)
- **gpt:** ❌ FALSE (76) — Marker gives length a default value in the struct (src/marker.hpp:48)
- **deepseek:** ❌ FALSE (60) — Marker::length=1 default at marker.hpp:48 is correct initialization; LOG-03 (model never returns length) is the real bug not the struct default
- **glm:** ✅ LEGIT (80) — marker.hpp:48 length defaults to 1; Marker() constructor at :36-38 only sets position=0 leaving length=1
- **kimi:** ❌ FALSE (85) — marker.hpp:48 int length=1 is intentional default; LengthRole bug is in markers model (LOG-03).
- **opus-ultra:** ❌ FALSE (55) — length=1 default is correct; report itself says not-a-bug (marker.hpp:48)

### [TYP-N04] Inconsistent m_ method naming: m_initializeSource — mixed underscore+camelCase  ·  _CONFLICT_  ·  Low
`abstractinputsource.h:50, globalhotkeys.h:150`
- **opus:** ⚠️ PARTIAL (35) — m_ method naming inconsistency; cosmetic (abstractinputsource.h:50)
- **gpt:** ⚠️ PARTIAL (58) — observed Inconsistent m method naming: minitializeSource - mixed underscore+camelCase (src/abstractinputsource.h:50)
- **deepseek:** ✅ LEGIT (75) — m_initializeSource uses m_ member prefix on a method not member (abstractinputsource.h:50)
- **glm:** ✅ LEGIT (70) — abstractinputsource.h:50 globalhotkeys.h:150 m_initializeSource mixed underscore+camelCase
- **kimi:** ❌ FALSE (85) — abstractinputsource.h:50 and globalhotkeys.h:150 name the method m_initializeSource as m_ prefix plus camelCase InitializeSource, consistent with other m_setX methods; no extra internal underscore.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — m_ method naming inconsistency; cosmetic (abstractinputsource.h:50)

### [VER-01] Qt::MarkdownText version guard 0x050F00 (5.15) — API added in 5.14  ·  _CONFLICT_  ·  Low
`documenthandler.cpp:958`
- **opus:** ⚠️ PARTIAL (45) — MarkdownText guard 0x050F00; insertMarkdown was 5.14 but target is Qt6 (documenthandler.cpp:958)
- **gpt:** ✅ LEGIT (78) — Qt::MarkdownText version guard 0x050F00 (5.15) - API added in 5.14 (src/documenthandler.cpp:958)
- **deepseek:** ✅ LEGIT (85) — guard 0x050F00(Qt5.15) but MarkdownText added in Qt5.14; 5.14 users get plain text (documenthandler.cpp:958)
- **glm:** ⚠️ PARTIAL (60) — documenthandler.cpp:958 version guard 0x050F00 (5.15) for MarkdownText which was added in 5.14; guard is overly conservative but not wrong
- **kimi:** ❌ FALSE (90) — CMakeLists.txt:57 sets QT_MIN_VERSION 6.8.2, so the 0x050F00 guard always evaluates true and has no runtime effect.
- **opus-ultra:** ❌ FALSE (72) — max: code correct / claim mischaracterized — MarkdownText guard 0x050F00; insertMarkdown was 5.14 but target is Qt6 (documenthandler.cp

### [W10-CLP-01] Paste-without-formatting fails when clipboard lacks text/plain  ·  _CONFLICT_  ·  High
`src/documenthandler.cpp:1346-1348`
- **opus:** ⚠️ PARTIAL (55) — paste-without-formatting uses mimeData->text(); empty if no text/plain (documenthandler.cpp:1346)
- **gpt:** ⚠️ PARTIAL (58) — observed Paste-without-formatting fails when clipboard lacks text/plain (src/documenthandler.cpp:1346)
- **deepseek:** ❌ FALSE (80) — QMimeData::text() auto-extracts plain text from HTML when text/plain missing; returns content not empty (documenthandler.cpp:1346-1348)
- **glm:** ✅ LEGIT (80) — documenthandler.cpp:1346-1348 paste checks hasHtml() then hasText() but if clipboard has only image button does nothing
- **kimi:** ✅ LEGIT (85) — documenthandler.cpp:1346-1348 inserts mimeData->text() for paste(true); if clipboard has HTML but no text/plain, text() is empty.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — paste-without-formatting uses mimeData->text(); empty if no text/plain (documenthandler.cp

### [W10-HTK-01] autoRepeat=true for ALL QHotkey shortcuts — non-velocity actions broken when held  ·  _CONFLICT_  ·  Critical
`src/globalhotkeys.cpp:1116`
- **opus:** ❌ FALSE (70) — 3rd arg of QHotkey::setShortcut is autoRegister, not autoRepeat (globalhotkeys.cpp:1116)
- **gpt:** ❌ FALSE (76) — third QHotkey setShortcut argument is autoRegister, not autoRepeat (src/globalhotkeys.cpp:1116)
- **deepseek:** ✅ LEGIT (92) — autoRepeat=true unconditional; toggle-type actions flood on hold rapid state flips (globalhotkeys.cpp:1116)
- **glm:** ✅ LEGIT (80) — globalhotkeys.cpp:1116 QHotkey setShortcut with autoRegister=true; all QHotkey shortcuts auto-repeat when held
- **kimi:** ✅ LEGIT (95) — globalhotkeys.cpp:1116 passes true as third argument to QHotkey::setShortcut for every shortcut, enabling autoRepeat on toggle actions.
- **opus-ultra:** ❌ FALSE (70) — 3rd arg of QHotkey::setShortcut is autoRegister

### [Z-N01] CursorAutoHide has no explicit z — hover detection fragile against Kirigami internals  ·  _CONFLICT_  ·  Medium
`main.qml:954, +windows/main.qml:618, +android/main.qml:562`
- **opus:** ⚠️ PARTIAL (45) — CursorAutoHide no explicit z; hover detection fragile (main.qml:954)
- **gpt:** ✅ LEGIT (78) — CursorAutoHide has no explicit z - hover detection fragile against Kirigami internals (src/kirigami_ui/main.qml:954)
- **deepseek:** ⚠️ PARTIAL (45) — no explicit z on CursorAutoHide; stacking fragile against Kirigami internals (main.qml:954)
- **glm:** ⚠️ PARTIAL (60) — main.qml:954 etc CursorAutoHide has no explicit z; hover detection fragile against Kirigami internals
- **kimi:** ❌ FALSE (65) — CursorAutoHide.qml has no explicit z (default 0); no source evidence that hover detection actually fails.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — CursorAutoHide no explicit z; hover detection fragile (main.qml:954)

### [Z-N02] Two OverlaySheets have z:1 while nine others have none — inconsistent stacking  ·  _CONFLICT_  ·  Low
`LanguageSettingsOverlay.qml:36, LayoutDirectionSettingsOverlay.qml:36`
- **opus:** ⚠️ PARTIAL (40) — two OverlaySheets z:1 while others none; inconsistent (LanguageSettingsOverlay.qml:36)
- **gpt:** ✅ LEGIT (78) — Two OverlaySheets have z:1 while nine others have none - inconsistent stacking (src/kirigami_ui/LanguageSettingsOverlay.qml:36)
- **deepseek:** ⚠️ PARTIAL (40) — two OverlaySheets have z:1 while others have none; inconsistent but functional
- **glm:** ✅ LEGIT (70) — LanguageSettingsOverlay.qml:36 LayoutDirectionSettingsOverlay.qml:36 have z:1 while others have none
- **kimi:** ❌ FALSE (70) — Two OverlaySheets explicitly set z:1 while others do not; cosmetic inconsistency, not demonstrated behavior bug.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — two OverlaySheets z:1 while others none; inconsistent (LanguageSettingsOverlay.qml:36)

### [Z-N03] ComboBox Popup z:103 inside OverlaySheets with z:1 — disconnected layering  ·  _CONFLICT_  ·  Low
`LanguageSettingsOverlay.qml:67, LayoutDirectionSettingsOverlay.qml:70`
- **opus:** ⚠️ PARTIAL (40) — ComboBox Popup z:103 inside z:1 sheets (LanguageSettingsOverlay.qml:67)
- **gpt:** ✅ LEGIT (78) — ComboBox Popup z:103 inside OverlaySheets with z:1 - disconnected layering (src/kirigami_ui/LanguageSettingsOverlay.qml:67)
- **deepseek:** ⚠️ PARTIAL (40) — ComboBox popup z:103 inside z:1 sheet; popup has own stacking context
- **glm:** ⚠️ PARTIAL (55) — LanguageSettingsOverlay.qml:67 etc ComboBox Popup z:103 inside OverlaySheets with z:1; disconnected layering
- **kimi:** ❌ FALSE (60) — ComboBox Popup z:103 inside OverlaySheets z:1 is normal high-z popup stacking; no broken layering shown.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — ComboBox Popup z:103 inside z:1 sheets (LanguageSettingsOverlay.qml:67)

### [A11Y-SYS] Systemic absence of Accessible properties — app invisible to screen readers  ·  _SPLIT_  ·  Medium
`All .qml files`
- **opus:** ⚠️ PARTIAL (45) — systemic absence of Accessible properties; real a11y gap
- **gpt:** ⚠️ PARTIAL (58) — observed Systemic absence of Accessible properties - app invisible to screen readers (src/kirigami_ui/main.qml:1)
- **deepseek:** ✅ LEGIT (85) — Zero Accessible.name/description/role in Prompter.qml and EditorToolbar.qml; no screen reader support across codebase
- **glm:** ✅ LEGIT (70) — All .qml files missing Accessible properties; app invisible to screen readers
- **kimi:** ✅ LEGIT (90) — No Accessible.* properties exist in any src/*.qml file; screen-reader support is absent
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — systemic absence of Accessible properties; real a11y gap

### [ACT-N05] +windows main.qml Controls Settings submenu missing OBS Settings action  ·  _SPLIT_  ·  Medium
`+windows/main.qml vs main.qml:261-270`
- **opus:** ❔ UNSURE (45) — +windows Controls submenu missing OBS Settings action; menu-specific (main.qml:261)
- **gpt:** ⚠️ PARTIAL (58) — observed +windows main.qml Controls Settings submenu missing OBS Settings action (src/kirigami_ui/main.qml:261)
- **deepseek:** ⚠️ PARTIAL (45) — missing OBS Settings action in +windows may be intentional per-platform feature gating
- **glm:** ✅ LEGIT (80) — +windows/main.qml Controls Settings submenu missing OBS Settings action present in base main.qml:261-270
- **kimi:** ✅ LEGIT (85) — base main.qml:261-270 adds an OBS Settings action in Controls Settings; +windows/main.qml:244-298 Controls Settings omits it and +windows has no Labs.MenuBar.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — +windows Controls submenu missing OBS Settings action; menu-specific (main.qml:261)

### [ACT-N06] +windows main.qml Performance tweaks missing enableBarsSetting  ·  _SPLIT_  ·  Low
`+windows/main.qml:320-391 vs main.qml:374-386`
- **opus:** ⚠️ PARTIAL (45) — +windows Performance tweaks missing enableBarsSetting (main.qml:320)
- **gpt:** ⚠️ PARTIAL (58) — observed +windows main.qml Performance tweaks missing enableBarsSetting (src/kirigami_ui/+windows/main.qml:320)
- **deepseek:** ⚠️ PARTIAL (45) — missing enableBarsSetting in +windows Performance tweaks may be platform specialization
- **glm:** ✅ LEGIT (75) — +windows/main.qml:320-391 Performance tweaks missing enableBarsSetting present in main.qml:374-386
- **kimi:** ✅ LEGIT (80) — base main.qml:374-386 defines enableBarsSetting under Performance tweaks; +windows/main.qml:320-379 Performance tweaks does not include that action.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — +windows Performance tweaks missing enableBarsSetting (main.qml:320)

### [ACT-N07] namedBookmarkButton: checkable button opens dialog — stale indicator after first click  ·  _SPLIT_  ·  Medium
`EditorToolbar.qml:225-236`
- **opus:** ✅ LEGIT (60) — namedBookmarkButton checkable opens dialog -> stale indicator (R2-EDT-03 family) (EditorToolbar.qml:225)
- **gpt:** ⚠️ PARTIAL (58) — observed namedBookmarkButton: checkable button opens dialog - stale indicator after first click (src/kirigami_ui/EditorToolbar.qml:225)
- **deepseek:** ✅ LEGIT (65) — checkable button opens dialog instead of toggling; checked binding desyncs after first click (EditorToolbar.qml:225-236)
- **glm:** ✅ LEGIT (75) — EditorToolbar.qml:225-236 namedBookmarkButton checkable button opens dialog; stale checked indicator after first click
- **kimi:** ✅ LEGIT (90) — EditorToolbar.qml:225-236 makes namedBookmarkButton checkable with checked bound to document.namedMarker, but onClicked only opens namedMarkerConfiguration, never toggling the property so the binding breaks.
- **opus-ultra:** ✅ LEGIT (60) — namedBookmarkButton checkable opens dialog -> stale indicator (R2-EDT-03 family) (EditorToolbar.qml:225)

### [ACT-N08] All checkable Labs.MenuItems inherit R2-EDT-03 binding-break pattern  ·  _SPLIT_  ·  Medium (masked — Labs.MenuBar dead per IMP-N01)
`main.qml:617-922`
- **opus:** ✅ LEGIT (55) — checkable Labs.MenuItems inherit checked-binding-break (R2-EDT-03 family) (main.qml:617)
- **gpt:** ⚠️ PARTIAL (58) — observed All checkable Labs.MenuItems inherit R2-EDT-03 binding-break pattern (src/kirigami_ui/main.qml:617)
- **deepseek:** ⚠️ PARTIAL (50) — claims Labs.MenuBar binding-break pattern; Labs.MenuBar already dead per IMP-N01 (main.qml:617-922)
- **glm:** ⚠️ PARTIAL (65) — main.qml:617-922 checkable Labs.MenuItems inherit binding-break pattern; Labs platform is valid in Qt 6
- **kimi:** ✅ LEGIT (75) — main.qml:693-889 contains many checkable Labs.MenuItem items using checked:<binding> plus onTriggered:<property>=checked; first user click breaks the declarative binding.
- **opus-ultra:** ✅ LEGIT (55) — checkable Labs.MenuItems inherit checked-binding-break (R2-EDT-03 family) (main.qml:617)

### [AND-BLD-01] Missing version.gradle — Gradle build fails  ·  _SPLIT_  ·  Critical
`android/build.gradle:19`
- **opus:** ✅ LEGIT (80) — apply from '../version.gradle' but file absent at root (android/build.gradle:19)
- **gpt:** ✅ LEGIT (92) — Missing version.gradle - Gradle build fails (android/build.gradle:19)
- **deepseek:** ✅ LEGIT (95) — apply from '../version.gradle' but version.gradle does not exist; projectVersionCode undefined (android/build.gradle:19)
- **glm:** ⚠️ PARTIAL (65) — android/build.gradle:19 references version.gradle; configured via CMakeLists.txt:396. May work if configure_file runs.
- **kimi:** ✅ LEGIT (95) — android/build.gradle:19 applies '../version.gradle'; version.gradle does not exist anywhere in repo (verified).
- **opus-ultra:** ✅ LEGIT (80) — apply from '../version.gradle' but file absent at root (android/build.gradle:19)

### [AND-HIGH-01] Android back button doesn't dismiss overlays/drawers before close  ·  _SPLIT_  ·  High
`+android/main.qml:144-150, PrompterPage.qml:64`
- **opus:** ⚠️ PARTIAL (50) — Android back button overlay-dismissal claim; domain (main.qml:144)
- **gpt:** ⚠️ PARTIAL (58) — observed Android back button doesn't dismiss overlays/drawers before close (src/kirigami_ui/+android/main.qml:144)
- **deepseek:** ✅ LEGIT (80) — +android/main.qml:144-150: onClosing only handles save dialog (modified check); ESC dismiss cascades (layers->drawers->overlays->find) absent from back button — cannot dismiss overlays
- **glm:** ✅ LEGIT (80) — +android/main.qml:144-150 back button doesn't dismiss overlays/drawers before close
- **kimi:** ✅ LEGIT (80) — +android/main.qml:144-150 onClosing checks modified only; PrompterPage.qml:64 onBackRequested closes without dismissing overlays/drawers.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — Android back button overlay-dismissal claim; domain (main.qml:144)

### [AND-MED-01] Missing intent-filter for opening files from other apps  ·  _SPLIT_  ·  Medium
`AndroidManifest.xml:29-32`
- **opus:** ⚠️ PARTIAL (45) — missing intent-filter for opening files (AndroidManifest.xml:29)
- **gpt:** ⚠️ PARTIAL (58) — observed Missing intent-filter for opening files from other apps (android/AndroidManifest.xml:29)
- **deepseek:** ✅ LEGIT (95) — AndroidManifest.xml:29-32: only LAUNCHER intent-filter; no VIEW filter for text/html or text/plain — cannot open .html scripts from file managers/email/downloads
- **glm:** ✅ LEGIT (75) — AndroidManifest.xml:29-32 missing intent-filter for opening files from other apps
- **kimi:** ✅ LEGIT (95) — AndroidManifest.xml:29-32 only MAIN/LAUNCHER; missing VIEW intent-filter for opening files.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — missing intent-filter for opening files (AndroidManifest.xml:29)

### [AND-MFT-01] FileProvider resource @xml/qtprovider_paths — file named filepaths.xml  ·  _SPLIT_  ·  Medium (latent)
`AndroidManifest.xml:43 vs res/xml/filepaths.xml`
- **opus:** ⚠️ PARTIAL (45) — FileProvider @xml/qtprovider_paths vs filepaths.xml; needs res check (AndroidManifest.xml:43)
- **gpt:** ⚠️ PARTIAL (58) — observed FileProvider resource @xml/qtproviderpaths - file named filepaths.xml (android/AndroidManifest.xml:43)
- **deepseek:** ✅ LEGIT (85) — commented FileProvider refs @xml/qtprovider_paths but actual file is filepaths.xml; resource-not-found if activated (AndroidManifest.xml:43)
- **glm:** ⚠️ PARTIAL (65) — AndroidManifest.xml:43 FileProvider references @xml/qtprovider_paths but file is named filepaths.xml. However FileProvider is commented out.
- **kimi:** ✅ LEGIT (75) — AndroidManifest.xml:43 (commented) references @xml/qtprovider_paths while res/xml/filepaths.xml is the actual file; latent mismatch.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — FileProvider @xml/qtprovider_paths vs filepaths.xml; needs res check (AndroidManifest.xml:

### [AND-RES-01] Invalid android:scaleType on bitmap element  ·  _SPLIT_  ·  Medium
`android/res/drawable/splash.xml:7`
- **opus:** ⚠️ PARTIAL (45) — invalid android:scaleType on bitmap; needs res check (splash.xml:7)
- **gpt:** ⚠️ PARTIAL (58) — observed Invalid android:scaleType on bitmap element (android/res/drawable/splash.xml:7)
- **deepseek:** ✅ LEGIT (90) — android:scaleType is ImageView attribute not valid on <bitmap> drawable; AAPT2 error (android/res/drawable/splash.xml:7)
- **glm:** ✅ LEGIT (80) — android/res/drawable/splash.xml:7 invalid android:scaleType on bitmap element
- **kimi:** ✅ LEGIT (90) — android/res/drawable/splash.xml:7 uses android:scaleType on <bitmap>, which is not a valid attribute for bitmap drawable items.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — invalid android:scaleType on bitmap; needs res check (splash.xml:7)

### [ANM-N02] Standby→Ready countdown opacity flash — PropertyChanges opacity:1 conflicts with dissolveIn  ·  _SPLIT_  ·  Medium
`Countdown.qml:265-276`
- **opus:** ⚠️ PARTIAL (50) — Standby->Ready opacity PropertyChanges flash (Countdown.qml:265)
- **gpt:** ⚠️ PARTIAL (58) — observed Standby->Ready countdown opacity flash - PropertyChanges opacity:1 conflicts with dissolveIn (src/prompter/Countdown.qml:265)
- **deepseek:** ✅ LEGIT (90) — Countdown.qml:265-276: Ready state sets opacity:1 AND starts dissolveIn(0->1); PropertyChanges applied first causes visible 1->0->1 flash
- **glm:** ✅ LEGIT (70) — Countdown.qml:265-276 Standby→Ready countdown opacity flash; PropertyChanges opacity:1 conflicts with dissolveIn
- **kimi:** ✅ LEGIT (85) — Countdown.qml:268 sets opacity:1 while dissolveIn animates opacity from 0 to 1, causing a flash
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — Standby->Ready opacity PropertyChanges flash (Countdown.qml:265)

### [API-N01] setAlignment() missing null-cursor guard — crash risk with no document  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:557-558`
- **opus:** ⚠️ PARTIAL (50) — setAlignment no null guard; null-cursor ops are Qt no-ops, crash unlikely (documenthandler.cpp:557)
- **gpt:** ✅ LEGIT (78) — setAlignment() missing null-cursor guard - crash risk with no document (src/documenthandler.cpp:557)
- **deepseek:** ✅ LEGIT (65) — setAlignment lacks null-cursor guard unlike alignment() getter (documenthandler.cpp:557-558)
- **glm:** ✅ LEGIT (75) — documenthandler.cpp:557-558 setAlignment() missing null-cursor guard; crash risk with no document
- **kimi:** ✅ LEGIT (80) — setAlignment() at documenthandler.cpp:553-559 calls mergeBlockFormat on textCursor without isNull() guard; crash risk if no document loaded.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — setAlignment no null guard; null-cursor ops are Qt no-ops

### [API-N03] CursorAutoHide.qml unconditionally dereferences pageStack.currentItem.prompter  ·  _SPLIT_  ·  Medium
`CursorAutoHide.qml:31`
- **opus:** ⚠️ PARTIAL (50) — CursorAutoHide derefs pageStack.currentItem.prompter (R4-EVT-03 family) (CursorAutoHide.qml:31)
- **gpt:** ✅ LEGIT (78) — CursorAutoHide.qml unconditionally dereferences pageStack.currentItem.prompter (src/prompter/CursorAutoHide.qml:31)
- **deepseek:** ✅ LEGIT (75) — unconditional deref of pageStack.currentItem.prompter without null guard (CursorAutoHide.qml:31)
- **glm:** ✅ LEGIT (75) — CursorAutoHide.qml:31 unconditionally dereferences pageStack.currentItem.prompter; null risk during transitions
- **kimi:** ✅ LEGIT (85) — CursorAutoHide.qml:28,31 dereferences root.pageStack.currentItem.editor/prompter without guards; navigating away causes TypeError.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — CursorAutoHide derefs pageStack.currentItem.prompter (R4-EVT-03 family) (CursorAutoHide.qm

### [API-N04] setMarker(bool) misleadingly named — sets regular marker, not any marker  ·  _SPLIT_  ·  Low
`documenthandler.h:123,212`
- **opus:** ⚠️ PARTIAL (35) — setMarker(bool) naming; cosmetic (documenthandler.h:123)
- **gpt:** ✅ LEGIT (78) — setMarker(bool) misleadingly named - sets regular marker, not any marker (src/documenthandler.h:123)
- **deepseek:** ✅ LEGIT (65) — setMarker(bool) only toggles regular marker despite generic name (documenthandler.h:123 212)
- **glm:** ✅ LEGIT (70) — documenthandler.h:123 212 setMarker(bool) misleadingly named; sets regular marker not any marker
- **kimi:** ⚠️ PARTIAL (50) — documenthandler.h:123 WRITE setMarker only creates regular markers with href='#', an API naming limitation more than a runtime defect.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — setMarker(bool) naming; cosmetic (documenthandler.h:123)

### [API-N05] fileName()/fileType() return fabricated defaults — can't distinguish "no file" from "untitled.html"  ·  _SPLIT_  ·  Low
`documenthandler.cpp:838-850`
- **opus:** ⚠️ PARTIAL (50) — fileName/fileType return 'untitled.html' default; can't signal no-file (documenthandler.cpp:838)
- **gpt:** ✅ LEGIT (78) — fileName()/fileType() return fabricated defaults - can't distinguish "no file" from "untitled.html" (src/documenthandler.cpp:838)
- **deepseek:** ✅ LEGIT (70) — fileName returns 'untitled.html' default; no way to distinguish no-file state (documenthandler.cpp:838-843)
- **glm:** ✅ LEGIT (70) — documenthandler.cpp:838-850 fileName()/fileType() return fabricated defaults; can't distinguish no-file from untitled.html
- **kimi:** ✅ LEGIT (70) — documenthandler.cpp:838-850 fileName()/fileType() return 'untitled.html'/'html' defaults, indistinguishable from a real untitled.html file.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — fileName/fileType return 'untitled.html' default; can't signal no-file (documenthandler.cp

### [API-N06] SystemFontChooserDialog::show() calls setText() on same label twice — dead code  ·  _SPLIT_  ·  Low
`systemfontchooserdialog.cpp:55-56`
- **opus:** ✅ LEGIT (80) — setText called twice; dead duplicate (dup R2-FONT-02) (systemfontchooserdialog.cpp:55)
- **gpt:** ⚠️ PARTIAL (58) — observed SystemFontChooserDialog::show() calls setText() on same label twice - dead code (src/systemfontchooserdialog.cpp:55)
- **deepseek:** ✅ LEGIT (80) — setText called twice on same label consecutively; dead duplicate (systemfontchooserdialog.cpp:55-56)
- **glm:** ✅ LEGIT (85) — systemfontchooserdialog.cpp:55-56 setText() called twice on same label; second call is dead code
- **kimi:** ✅ LEGIT (70) — systemfontchooserdialog.cpp:55-56 sets textPreviewLabel text twice with the same argument; harmless duplicate call.
- **opus-ultra:** ✅ LEGIT (80) — setText called twice; dead duplicate (dup R2-FONT-02) (systemfontchooserdialog.cpp:55)

### [API-N07] SpellChecker::encode() fallback says "Latin-1" but calls toLocal8Bit()  ·  _SPLIT_  ·  Low
`spellchecker.cpp:400-406`
- **opus:** ✅ LEGIT (55) — encode() comment says Latin-1 but calls toLocal8Bit (spellchecker.cpp:400)
- **gpt:** ✅ LEGIT (78) — SpellChecker::encode() fallback says "Latin-1" but calls toLocal8Bit() (src/spellchecker.cpp:400)
- **deepseek:** ✅ LEGIT (75) — comment claims Latin-1 fallback but code calls toLocal8Bit which depends on system locale (spellchecker.cpp:400-406)
- **glm:** ⚠️ PARTIAL (65) — spellchecker.cpp:400-406 encode() fallback says Latin-1 but calls toLocal8Bit(); may not match dictionary encoding
- **kimi:** ✅ LEGIT (90) — spellchecker.cpp:404-405 comment says Latin-1 fallback but code calls toLocal8Bit(), using system locale instead of Latin-1.
- **opus-ultra:** ✅ LEGIT (55) — encode() comment says Latin-1 but calls toLocal8Bit (spellchecker.cpp:400)

### [AR-01] PrompterView.qml:53-58 Rotation debug feature clips on extreme aspect ratios  ·  _SPLIT_  ·  Low
`PrompterView.qml:53-58`
- **opus:** ⚠️ PARTIAL (45) — rotation debug feature clips on extreme aspect (PrompterView.qml:53)
- **gpt:** ✅ LEGIT (78) — PrompterView.qml:53-58 Rotation debug feature clips on extreme aspect ratios (src/prompter/PrompterView.qml:53)
- **deepseek:** ✅ LEGIT (75) — Rotation debug at PrompterView.qml:53 wraps at angles — clips on ultrawide/tablet aspect ratios
- **glm:** ⚠️ PARTIAL (60) — PrompterView.qml:53-58 Rotation debug feature clips on extreme aspect ratios; cosmetic
- **kimi:** ✅ LEGIT (75) — PrompterView.qml:53-58 the debug 'theforce' Rotation uses fixed origin/angle that clips content on extreme aspect ratios.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — rotation debug feature clips on extreme aspect (PrompterView.qml:53)

### [BLK-N01] alignment() returns Qt::AlignCenter (includes vertical bit 0x0080) on null cursor  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:549`
- **opus:** ✅ LEGIT (70) — null-cursor returns Qt::AlignCenter incl vertical bit 0x80 (documenthandler.cpp:549)
- **gpt:** ⚠️ PARTIAL (58) — observed alignment() returns Qt::AlignCenter (includes vertical bit 0x0080) on null cursor (src/documenthandler.cpp:549)
- **deepseek:** ✅ LEGIT (85) — documenthandler.cpp:549: alignment() returns Qt::AlignCenter(AlignHCenter|AlignVCenter) on null cursor; AlignVCenter meaningless for blocks
- **glm:** ✅ LEGIT (70) — documenthandler.cpp:549 alignment() returns Qt::AlignCenter (includes vertical bit 0x0080) on null cursor
- **kimi:** ❔ UNSURE (55) — documenthandler.cpp:548-549 returns Qt::AlignCenter on null cursor; impact depends on whether another default is expected
- **opus-ultra:** ✅ LEGIT (70) — null-cursor returns Qt::AlignCenter incl vertical bit 0x80 (documenthandler.cpp:549)

### [BLK-N02] updateContents() fails to reset block formatting — stale formats contaminate new document  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1104-1122`
- **opus:** ✅ LEGIT (55) — updateContents doesn't reset block format; stale formats can persist (documenthandler.cpp:1104)
- **gpt:** ⚠️ PARTIAL (58) — observed updateContents() fails to reset block formatting - stale formats contaminate new document (src/documenthandler.cpp:1104)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:1104-1122: removeSelectedText preserves first block format; insertText inherits old formatting; no QTextBlockFormat reset on load
- **glm:** ✅ LEGIT (70) — documenthandler.cpp:1104-1122 updateContents() fails to reset block formatting; stale formats contaminate new document
- **kimi:** ✅ LEGIT (80) — documenthandler.cpp:1104-1122 updateContents removes text but does not reset block formatting; old spacing can persist
- **opus-ultra:** ✅ LEGIT (55) — updateContents doesn't reset block format; stale formats can persist (documenthandler.cpp:1104)

### [BLK-N03] setLineHeight/setParagraphHeight apply document-wide — destroy per-block customization  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1597,1611`
- **opus:** ✅ LEGIT (60) — setLineHeight/setParagraphHeight select Document -> apply to all blocks (documenthandler.cpp:1597)
- **gpt:** ⚠️ PARTIAL (58) — observed setLineHeight/setParagraphHeight apply document-wide - destroy per-block customization (src/documenthandler.cpp:1597)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:1597 1611: setLineHeight/setParagraphHeight select entire document via cursor.select(Document); destroy per-block customization
- **glm:** ✅ LEGIT (70) — documenthandler.cpp:1597 1611 setLineHeight/setParagraphHeight apply document-wide; destroy per-block customization
- **kimi:** ✅ LEGIT (90) — documenthandler.cpp:1597/1611 select the whole document then mergeBlockFormat, applying height to all blocks
- **opus-ultra:** ✅ LEGIT (60) — setLineHeight/setParagraphHeight select Document -> apply to all blocks (documenthandler.cpp:1597)

### [CFG-N01] Desktop MimeType incomplete — only text/html, missing text/plain and text/markdown  ·  _SPLIT_  ·  Medium
`com.cuperino.qprompt.desktop (both copies)`
- **opus:** ⚠️ PARTIAL (50) — desktop MimeType only text/html, missing text/plain/markdown
- **gpt:** ⚠️ PARTIAL (58) — observed Desktop MimeType incomplete - only text/html, missing text/plain and text/markdown (com.cuperino.qprompt.desktop:1)
- **deepseek:** ✅ LEGIT (95) — com.cuperino.qprompt.desktop (both copies): MimeType=text/html only; appdata.xml also declares text/plain and text/markdown
- **glm:** ✅ LEGIT (70) — com.cuperino.qprompt.desktop MimeType only text/html; missing text/plain and text/markdown
- **kimi:** ✅ LEGIT (80) — com.cuperino.qprompt.desktop:11 and src/com.cuperino.qprompt.desktop:11 list MimeType=text/html only; text/plain and text/markdown missing per appdata.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — desktop MimeType only text/html

### [CFG-N02] v1.1.3 release date "2022-1-16" breaks chronological order — should be 2023-01-16  ·  _SPLIT_  ·  Low
`appdata.xml line 202`
- **opus:** ✅ LEGIT (55) — appdata v1.1.3 date 2022-1-16 breaks chronological order (appdata.xml)
- **gpt:** ⚠️ PARTIAL (58) — observed v1.1.3 release date "2022-1-16" breaks chronological order - should be 2023-01-16 (com.cuperino.qprompt.appdata.xml:202)
- **deepseek:** ❔ UNSURE (40) — 'appdata.xml:202 date "2022-1-16"; cannot independently verify correct year from source alone'
- **glm:** ✅ LEGIT (70) — appdata.xml line 202 v1.1.3 release date '2022-1-16' breaks chronological order; should be 2023-01-16
- **kimi:** ✅ LEGIT (95) — com.cuperino.qprompt.appdata.xml:202 release 1.1.3 has date='2022-1-16'; chronology broken.
- **opus-ultra:** ✅ LEGIT (55) — appdata v1.1.3 date 2022-1-16 breaks chronological order (appdata.xml)

### [CFG-N03] "fixedd" typo in v2.0.2 release description  ·  _SPLIT_  ·  Low
`appdata.xml line 72`
- **opus:** ✅ LEGIT (60) — 'fixedd' typo in v2.0.2 release description (appdata.xml)
- **gpt:** ⚠️ PARTIAL (58) — observed "fixedd" typo in v2.0.2 release description (com.cuperino.qprompt.appdata.xml:72)
- **deepseek:** ✅ LEGIT (95) — 'appdata.xml:72: "issues were fixedd in this release" — verified typo in source'
- **glm:** ✅ LEGIT (70) — appdata.xml line 72 'fixedd' typo in v2.0.2 release description
- **kimi:** ✅ LEGIT (95) — com.cuperino.qprompt.appdata.xml:72 contains 'fixedd' typo in v2.0.2 description.
- **opus-ultra:** ✅ LEGIT (60) — 'fixedd' typo in v2.0.2 release description (appdata.xml)

### [CLI-N01] --version flag non-functional — version string empty when parser processes  ·  _SPLIT_  ·  Medium
`main.cpp:159,214`
- **opus:** ⚠️ PARTIAL (50) — --version may be empty: addVersionOption before setApplicationData (main.cpp:159)
- **gpt:** ✅ LEGIT (78) — --version flag non-functional - version string empty when parser processes (src/main.cpp:159)
- **deepseek:** ⚠️ PARTIAL (55) — addVersionOption before applicationData set; version may be empty depending on flow (main.cpp:159)
- **glm:** ⚠️ PARTIAL (65) — main.cpp:159 214 --version flag may not work if QPROMPT_VERSION_STRING is empty; depends on version header generation
- **kimi:** ✅ LEGIT (90) — main.cpp:157-159 parser.process(app) runs before KAboutData::setApplicationData at line 214, so --version string is empty.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — --version may be empty: addVersionOption before setApplicationData (main.cpp:159)

### [CLIP-N04] Image-only clipboard paste — button enabled but does nothing  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1356-1359`
- **opus:** ✅ LEGIT (65) — image-only paste is a no-op (commented) but button is enabled (documenthandler.cpp:1356)
- **gpt:** ⚠️ PARTIAL (58) — observed Image-only clipboard paste - button enabled but does nothing (src/documenthandler.cpp:1356)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:1356-1359: hasImage() branch entirely commented out; paste button remains enabled but does nothing for images
- **glm:** ✅ LEGIT (75) — documenthandler.cpp:1356-1359 image-only clipboard paste; button enabled but does nothing
- **kimi:** ✅ LEGIT (80) — documenthandler.cpp:1356-1359 hasImage() branch is commented out while paste button can still be enabled.
- **opus-ultra:** ✅ LEGIT (65) — image-only paste is a no-op (commented) but button is enabled (documenthandler.cpp:1356)

### [CLP-N01] Copy/Cut exports unfiltered HTML to system clipboard  ·  _SPLIT_  ·  Medium
`Prompter.qml, EditorToolbar.qml, main.qml`
- **opus:** ⚠️ PARTIAL (50) — copy/cut exports unfiltered HTML to clipboard (Prompter.qml)
- **gpt:** ✅ LEGIT (78) — Copy/Cut exports unfiltered HTML to system clipboard (src/prompter/Prompter.qml:1)
- **deepseek:** ⚠️ PARTIAL (70) — Prompter.qml/EditorToolbar.qml/main.qml: copy/cut paths use editor.copy()/cut() placing raw QTextDocument HTML on clipboard; filterHtml() doesn't strip scripts — verified pattern but not all sites
- **glm:** ✅ LEGIT (75) — Prompter.qml EditorToolbar.qml main.qml copy/cut exports unfiltered HTML to system clipboard
- **kimi:** ✅ LEGIT (85) — Copy/cut paths use editor.copy()/cut() which place raw QTextDocument HTML on clipboard without filterHtml.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — copy/cut exports unfiltered HTML to clipboard (Prompter.qml)

### [CLP-N02] DropArea external drop never calls drop.accept()  ·  _SPLIT_  ·  Medium
`Prompter.qml:1369-1379`
- **opus:** ⚠️ PARTIAL (50) — external drop never calls drop.accept() (Prompter.qml:1369)
- **gpt:** ⚠️ PARTIAL (58) — observed DropArea external drop never calls drop.accept() (src/prompter/Prompter.qml:1369)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:1369-1379: external drop branch (hasUrls/hasHtml/hasText) processes content but never calls drop.accept(); internal drag at 1354 correctly accepts
- **glm:** ✅ LEGIT (75) — Prompter.qml:1369-1379 DropArea external drop never calls drop.accept()
- **kimi:** ✅ LEGIT (90) — Prompter.qml:1369-1379 external drop branch handles content but never calls drop.accept().
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — external drop never calls drop.accept() (Prompter.qml:1369)

### [CLP-N03] DropArea external drop: URLs consumed preferentially — text silently lost  ·  _SPLIT_  ·  Medium
`Prompter.qml:1370-1378`
- **opus:** ⚠️ PARTIAL (50) — external drop consumes URLs preferentially, text lost (Prompter.qml:1370)
- **gpt:** ⚠️ PARTIAL (58) — observed DropArea external drop: URLs consumed preferentially - text silently lost (src/prompter/Prompter.qml:1370)
- **deepseek:** ✅ LEGIT (90) — Prompter.qml:1370-1378: hasUrls branch processes ONLY images via insertImageAt(); else-if chain prevents fallthrough to hasHtml/hasText — drag from browser loses all text
- **glm:** ✅ LEGIT (75) — Prompter.qml:1370-1378 DropArea external drop: URLs consumed preferentially; text silently lost
- **kimi:** ✅ LEGIT (90) — Prompter.qml:1370-1378 drop.hasUrls branch consumes URLs and skips html/text branches.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — external drop consumes URLs preferentially

### [CMAKE-NEW-01] Remote.qml exists on disk but never listed in QML_FILES  ·  _SPLIT_  ·  Low
`src/CMakeLists.txt, src/prompter/Remote.qml`
- **opus:** ⚠️ PARTIAL (45) — Remote.qml on disk but not in QML_FILES (CMakeLists.txt)
- **gpt:** ✅ LEGIT (78) — Remote.qml exists on disk but never listed in QMLFILES (src/CMakeLists.txt:260)
- **deepseek:** ✅ LEGIT (90) — Remote.qml on disk but not in any CMake QML_FILES — orphaned dead code
- **glm:** ✅ LEGIT (75) — src/CMakeLists.txt Remote.qml exists on disk but not listed in QML_FILES (but is in WASM list at :132)
- **kimi:** ✅ LEGIT (80) — src/prompter/Remote.qml exists but is not listed in any CMakeLists.txt QML_FILES/source list.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — Remote.qml on disk but not in QML_FILES (CMakeLists.txt)

### [CMB-N01] autoReloadSeconds SpinBox from binding circular — clamps to 1 when all-zero  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:1381`
- **opus:** ❔ UNSURE (45) — autoReloadSeconds SpinBox circular binding clamps to 1; domain (PrompterPage.qml:1381)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/kirigami_ui/PrompterPage.qml:1381)
- **deepseek:** ✅ LEGIT (70) — SpinBox from binding evaluates to 1 when all three spinners are zero (PrompterPage.qml:1381)
- **glm:** ⚠️ PARTIAL (65) — PrompterPage.qml:1381 autoReloadSeconds SpinBox from binding circular; clamps to 1 when all-zero
- **kimi:** ✅ LEGIT (95) — PrompterPage.qml:1381 autoReloadSeconds from references its own value, creating a loop; when all timers are zero from clamps to 1, preventing all-zero
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — autoReloadSeconds SpinBox circular binding clamps to 1; domain (PrompterPage.qml:1381)

### [CMB-N02] autoReloadMinutes SpinBox from contains redundant circular self-reference  ·  _SPLIT_  ·  Low
`PrompterPage.qml:1356`
- **opus:** ❔ UNSURE (45) — autoReloadMinutes SpinBox circular from binding; domain (PrompterPage.qml:1356)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/kirigami_ui/PrompterPage.qml:1356)
- **deepseek:** ✅ LEGIT (75) — autoReloadMinutes.from self-references autoReloadMinutes.value causing binding loop (PrompterPage.qml:1356)
- **glm:** ⚠️ PARTIAL (60) — PrompterPage.qml:1356 autoReloadMinutes SpinBox from contains redundant circular self-reference
- **kimi:** ✅ LEGIT (90) — PrompterPage.qml:1356 autoReloadMinutes from: value>0 || autoReloadMinutes.value>0... redundantly self-references the same property, causing a binding loop
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — autoReloadMinutes SpinBox circular from binding; domain (PrompterPage.qml:1356)

### [CMT-N01] Justify ToolButton comment says it's commented out — but it's active  ·  _SPLIT_  ·  Medium
`EditorToolbar.qml:761-773`
- **opus:** ⚠️ PARTIAL (40) — comment claims Justify button commented out but it's active (EditorToolbar.qml:761)
- **gpt:** ⚠️ PARTIAL (48) — comment problem observed, but defect impact is limited (src/kirigami_ui/EditorToolbar.qml:761)
- **deepseek:** ✅ LEGIT (90) — Comment says justify is commented out at EditorToolbar.qml:761 but code is active via toolbar.showJustify
- **glm:** ✅ LEGIT (80) — EditorToolbar.qml:761-773 comment says justify is commented out but button is active
- **kimi:** ✅ LEGIT (80) — EditorToolbar.qml:761 comment states justify is commented out, but alignJustifyButton at lines 762-773 is fully active.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — comment claims Justify button commented out but it's active (EditorToolbar.qml:761)

### [CMT-N08] Entire Telemetry class is dead commented-out shell across 4 files  ·  _SPLIT_  ·  Medium
`telemetry.h, telemetry.cpp, promptsession.h, promptsession.cpp`
- **opus:** ✅ LEGIT (50) — Telemetry class is dead commented-out shell (telemetry.h)
- **gpt:** ⚠️ PARTIAL (48) — comment problem observed, but defect impact is limited (src/telemetry.h:1)
- **deepseek:** ✅ LEGIT (90) — All Telemetry methods commented out across 4 files — dead shell creates false expectations
- **glm:** ✅ LEGIT (75) — telemetry.h telemetry.cpp promptsession.h promptsession.cpp Telemetry class is dead commented-out shell
- **kimi:** ✅ LEGIT (75) — telemetry.h/cpp and promptsession.h/cpp are largely commented-out shells and are not compiled.
- **opus-ultra:** ✅ LEGIT (50) — Telemetry class is dead commented-out shell (telemetry.h)

### [CMT-N10] Obsolete Qt 5 qmlRegisterType calls as commented-out cruft  ·  _SPLIT_  ·  Low
`main.cpp:68-69,215-223`
- **opus:** ⚠️ PARTIAL (35) — commented-out Qt5 qmlRegisterType cruft; cosmetic (main.cpp:68)
- **gpt:** ⚠️ PARTIAL (48) — comment problem observed, but defect impact is limited (src/main.cpp:68)
- **deepseek:** ✅ LEGIT (90) — Qt 5 qmlRegisterType calls commented out at main.cpp — cruft misleads about QML_ELEMENT registration
- **glm:** ✅ LEGIT (75) — main.cpp:68-69 215-223 obsolete Qt 5 qmlRegisterType calls as commented-out cruft
- **kimi:** ✅ LEGIT (90) — main.cpp:68-69,215-223 contain commented-out Qt 5 qmlRegisterType/QObject cruft; misleading with current QML_ELEMENT registration
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — commented-out Qt5 qmlRegisterType cruft; cosmetic (main.cpp:68)

### [CNTD-N01] Countdown Running: dissolveIn and dissolveOut compete for same opacity when __iterations===__disappearWithin===1  ·  _SPLIT_  ·  Low
`Countdown.qml:289-291,308`
- **opus:** ⚠️ PARTIAL (50) — dissolveIn/dissolveOut compete for opacity (Countdown.qml:289)
- **gpt:** ⚠️ PARTIAL (58) — observed Countdown Running: dissolveIn and dissolveOut compete for same opacity when iterations===disapp (src/prompter/Countdown.qml:289)
- **deepseek:** ✅ LEGIT (85) — Countdown.qml:289-291/308: Running state sets dissolveIn.running=true (fade-in) AND dissolveOut.running when __iterations===__disappearWithin===1 — both animate same opacity
- **glm:** ⚠️ PARTIAL (60) — Countdown.qml:289-291 308 when __iterations===__disappearWithin===1 dissolveIn and dissolveOut compete for same opacity
- **kimi:** ✅ LEGIT (75) — Countdown.qml:289-291,308 Running state sets both dissolveIn and dissolveOut running when __iterations===__disappearWithin===1.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — dissolveIn/dissolveOut compete for opacity (Countdown.qml:289)

### [COERC-N03] real→int truncation in WindowDragger position compounds drift  ·  _SPLIT_  ·  Low
`WindowDragger.qml:28-34`
- **opus:** ⚠️ PARTIAL (50) — real->int truncation in WindowDragger compounds drift (FINAL-05 family) (WindowDragger.qml:28)
- **gpt:** ⚠️ PARTIAL (58) — observed real->int truncation in WindowDragger position compounds drift (src/qt/WindowDragger.qml:28)
- **deepseek:** ✅ LEGIT (80) — WindowDragger.qml:28-34: mouse.x (qreal) stored to prevX (int) losing fractional precision; compounds drift on each drag start
- **glm:** ✅ LEGIT (70) — WindowDragger.qml:28-34 real→int truncation in position compounds drift
- **kimi:** ✅ LEGIT (80) — WindowDragger.qml:28 prevX/prevY declared int; mouse.x qreal truncated each press; compounds drift.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — real->int truncation in WindowDragger compounds drift (FINAL-05 family) (WindowDragger.qml

### [COLOR-01] ProjectionsManager.qml uses invalid "initial" color — repro of R4-ROOT-02  ·  _SPLIT_  ·  Medium
`ProjectionsManager.qml:195`
- **opus:** ✅ LEGIT (70) — invalid 'initial' color (dup R4-ROOT-02) (ProjectionsManager.qml:195)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/prompter/ProjectionsManager.qml:195)
- **deepseek:** ⚠️ PARTIAL (50) — 'initial' CSS keyword may be valid in Qt6 but is non-standard QML color name (ProjectionsManager.qml:195)
- **glm:** ✅ LEGIT (80) — ProjectionsManager.qml:195 uses invalid 'initial' color value; not valid in QML
- **kimi:** ✅ LEGIT (90) — ProjectionsManager.qml:195 assigns color 'initial'; that CSS keyword is not a valid QML color and falls back to black.
- **opus-ultra:** ✅ LEGIT (70) — invalid 'initial' color (dup R4-ROOT-02) (ProjectionsManager.qml:195)

### [COLOR-02] Hardcoded #EED text invisible on light themes — WheelSettingsOverlay  ·  _SPLIT_  ·  Medium
`WheelSettingsOverlay.qml:105`
- **opus:** ⚠️ PARTIAL (40) — #EED text invisible on light themes (WheelSettingsOverlay.qml:105)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/kirigami_ui/WheelSettingsOverlay.qml:105)
- **deepseek:** ✅ LEGIT (75) — #EED nearly invisible on light themes; hardcoded without theme awareness (WheelSettingsOverlay.qml:105)
- **glm:** ✅ LEGIT (75) — WheelSettingsOverlay.qml:105 hardcoded #EED text invisible on light themes
- **kimi:** ✅ LEGIT (90) — WheelSettingsOverlay.qml:105 labels help text with color '#EED' (very light cream) on a Kirigami OverlaySheet that uses a light background, making it nearly invisible.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — #EED text invisible on light themes (WheelSettingsOverlay.qml:105)

### [COLOR-03] velocityText ColorAnimation flash: #BBB → #FFF → #CCC jump  ·  _SPLIT_  ·  Low
`PrompterPage.qml:842-860`
- **opus:** ⚠️ PARTIAL (40) — velocityText ColorAnimation BBB->FFF->CCC flash (PrompterPage.qml:842)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/kirigami_ui/PrompterPage.qml:842)
- **deepseek:** ⚠️ PARTIAL (45) — #BBB->#FFF->#CCC flash pattern likely intentional velocity-change feedback animation (PrompterPage.qml:842-860)
- **glm:** ⚠️ PARTIAL (60) — PrompterPage.qml:842-860 velocityText ColorAnimation flash #BBB→#FFF→#CCC jump
- **kimi:** ✅ LEGIT (90) — PrompterPage.qml:842 sets velocityText.color='#BBB' and ColorAnimation at 855-860 restarts from '#FFF' to '#CCC', causing a white flash mid-transition.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — velocityText ColorAnimation BBB->FFF->CCC flash (PrompterPage.qml:842)

### [COLOR-04] ReadRegionOverlay ColorAnimation tracks __fillColor that never changes  ·  _SPLIT_  ·  Low
`ReadRegionOverlay.qml:204,616`
- **opus:** ⚠️ PARTIAL (45) — ColorAnimation tracks __fillColor that never changes (ReadRegionOverlay.qml:204)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/prompter/ReadRegionOverlay.qml:204)
- **deepseek:** ✅ LEGIT (65) — ColorAnimation tracks __fillColor='#00000000' constant; never produces visible change (ReadRegionOverlay.qml:204 616)
- **glm:** ⚠️ PARTIAL (55) — ReadRegionOverlay.qml:204 616 ColorAnimation tracks __fillColor that never changes
- **kimi:** ✅ LEGIT (90) — ReadRegionOverlay.qml:204 initializes __fillColor='#00000000' and never reassigns it; the ColorAnimation at 613-617 interpolates it with zero visual effect.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — ColorAnimation tracks __fillColor that never changes (ReadRegionOverlay.qml:204)

### [COLOR-05] Prompter scrollbar gradient hardcodes #CCC/#998/#665 — low contrast on light backgrounds  ·  _SPLIT_  ·  Low
`Prompter.qml:1008-1009`
- **opus:** ⚠️ PARTIAL (40) — scrollbar gradient hardcoded greys; contrast (Prompter.qml:1008)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/prompter/Prompter.qml:1008)
- **deepseek:** ⚠️ PARTIAL (40) — hardcoded scrollbar gradient #CCC/#998/#665 is cosmetic; low contrast on light themes (Prompter.qml:1008-1009)
- **glm:** ✅ LEGIT (70) — Prompter.qml:1008-1009 scrollbar gradient hardcodes #CCC/#998/#665; low contrast on light backgrounds
- **kimi:** ✅ LEGIT (85) — Prompter.qml:1008-1009 hardcodes scrollbar GradientStop colors '#CCC', '#998', '#665' without consulting the theme, becoming low-contrast on light prompter backgrounds.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — scrollbar gradient hardcoded greys; contrast (Prompter.qml:1008)

### [COLOR-06] Countdown #FFF digits on #333-at-0.48-overlay — insufficient contrast on light backgrounds  ·  _SPLIT_  ·  Low
`Countdown.qml:71,192,212`
- **opus:** ⚠️ PARTIAL (40) — #FFF digits on translucent #333 overlay; contrast (Countdown.qml:71)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/prompter/Countdown.qml:71)
- **deepseek:** ⚠️ PARTIAL (40) — #FFF digits on #333-at-0.48 is design choice; contrast varies with background (Countdown.qml:71 192 212)
- **glm:** ✅ LEGIT (70) — Countdown.qml:71 192 212 #FFF digits on #333 at 0.48 overlay; insufficient contrast on light backgrounds
- **kimi:** ✅ LEGIT (85) — Countdown.qml:71 draws a '#333' rectangle at opacity 0.48 and writes digits/strokes in '#FFF'; on light prompter backgrounds effective background is light gray and white text has poor contrast.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — #FFF digits on translucent #333 overlay; contrast (Countdown.qml:71)

### [COLOR-07] CSS default stylesheet hardcodes #FFFFFF body text — ignores user text color  ·  _SPLIT_  ·  Low
`documenthandler.cpp:185-189`
- **opus:** ⚠️ PARTIAL (55) — body color hardcoded #FFFFFF; per-span user colors still override (documenthandler.cpp:185)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/documenthandler.cpp:185)
- **deepseek:** ✅ LEGIT (65) — CSS body{color:#FFFFFF} hardcoded; overrides user text color for HTML docs (documenthandler.cpp:185-189)
- **glm:** ✅ LEGIT (75) — documenthandler.cpp:185-189 CSS default stylesheet hardcodes #FFFFFF body text; ignores user text color
- **kimi:** ✅ LEGIT (90) — documenthandler.cpp:184-189 sets default stylesheet body color '#FFFFFF'; this hardcodes white body text regardless of the user's chosen text color for existing content.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — body color hardcoded #FFFFFF; per-span user colors still override (documenthandler.cpp:185

### [COLOR-N08] textBackground() returns invalid QColor for body/paragraph text  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:528-534`
- **opus:** ⚠️ PARTIAL (45) — textBackground().color() yields black for unset bg, not 'invalid' (documenthandler.cpp:534)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/documenthandler.cpp:528)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:528-534: textBackground() returns format.background().color(); QBrush::color() on NoBrush returns invalid QColor
- **glm:** ✅ LEGIT (70) — documenthandler.cpp:528-534 textBackground() returns invalid QColor for body/paragraph text
- **kimi:** ✅ LEGIT (85) — documenthandler.cpp:534 returns format.background().color(), which is invalid when no background-color is set
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — textBackground().color() yields black for unset bg

### [COLOR-N09] acceptedColor binds transparent QColor on startup — initial text invisible  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:1010,1025, PrompterView.qml:240-241`
- **opus:** ⚠️ PARTIAL (55) — acceptedColor transparent on startup -> initial text invisible (PrompterPage.qml:1010)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/kirigami_ui/PrompterPage.qml:1010)
- **deepseek:** ✅ LEGIT (90) — PrompterPage.qml:1010 1025: acceptedColor uninitialized defaults to Qt.rgba(0 0 0 0); PrompterView.qml:240-241 binds transparent; initial text invisible
- **glm:** ✅ LEGIT (70) — PrompterPage.qml:1010 1025 PrompterView.qml:240-241 acceptedColor binds transparent QColor on startup; initial text invisible
- **kimi:** ✅ LEGIT (85) — PrompterPage.qml:1010/1025 ColorDialog acceptedColor defaults to transparent, making initial text formatting invisible
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — acceptedColor transparent on startup -> initial text invisible (PrompterPage.qml:1010)

### [COMP-N03] regularMarker() same double-textCursor anti-pattern as LOG-07  ·  _SPLIT_  ·  Low
`documenthandler.cpp:693-696`
- **opus:** ⚠️ PARTIAL (50) — regularMarker double textCursor() (LOG-07 family) (documenthandler.cpp:693)
- **gpt:** ✅ LEGIT (78) — regularMarker() same double-textCursor anti-pattern as LOG-07 (src/documenthandler.cpp:693)
- **deepseek:** ✅ LEGIT (95) — documenthandler.cpp:693-696: fetches textCursor() 3 extra times after null-checked local copy; same anti-pattern as namedMarker() at 701-704 — stale formatting reads
- **glm:** ⚠️ PARTIAL (60) — documenthandler.cpp:693-696 regularMarker() same double-textCursor anti-pattern; second cursor may be stale
- **kimi:** ✅ LEGIT (70) — documenthandler.cpp:693-696 regularMarker() null-checks one cursor then reads format from fresh textCursor() calls; stale cursor pattern.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — regularMarker double textCursor() (LOG-07 family) (documenthandler.cpp:693)

### [DBG-N01] OBS WebSocket auth challenge+salt logged to console in release builds  ·  _SPLIT_  ·  Medium
`Prompter.qml:364,372,386`
- **opus:** ✅ LEGIT (60) — console.log(m) logs OBS auth challenge+salt in release (Prompter.qml:372)
- **gpt:** ⚠️ PARTIAL (58) — observed OBS WebSocket auth challenge+salt logged to console in release builds (src/prompter/Prompter.qml:364)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:364 372 386: console.log(status) + console.log(m) logs full WebSocket Hello including auth challenge+salt; console.info maps to unsuppressed qInfo()
- **glm:** ✅ LEGIT (75) — Prompter.qml:364 372 386 OBS WebSocket auth challenge+salt logged to console in release builds
- **kimi:** ✅ LEGIT (90) — Prompter.qml:364,372 log full WebSocket Hello including authentication challenge and salt; line 386 console.info also logs.
- **opus-ultra:** ✅ LEGIT (60) — console.log(m) logs OBS auth challenge+salt in release (Prompter.qml:372)

### [DBG-N02] Velocity debug logging active in production  ·  _SPLIT_  ·  Low
`Prompter.qml:606, InputsOverlay.qml:441`
- **opus:** ✅ LEGIT (55) — velocity debug console.log active in production (Prompter.qml:606)
- **gpt:** ⚠️ PARTIAL (58) — observed Velocity debug logging active in production (src/prompter/Prompter.qml:606)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:606: console.log('velocity: ' velocity) every velocity change; InputsOverlay.qml:441: console.log(setVelocityModifier) every ComboBox change; no debug guard
- **glm:** ✅ LEGIT (70) — Prompter.qml:606 InputsOverlay.qml:441 velocity debug logging active in production
- **kimi:** ✅ LEGIT (80) — Prompter.qml:606 logs velocity on every setVelocity; InputsOverlay.qml:441 logs modifier value on every ComboBox change.
- **opus-ultra:** ✅ LEGIT (55) — velocity debug console.log active in production (Prompter.qml:606)

### [DBG-N04] qDebug() in namedMarker()/setMarker() active in release  ·  _SPLIT_  ·  Low
`documenthandler.cpp:760,793`
- **opus:** ✅ LEGIT (60) — qDebug in namedMarker/setMarker active in release builds (documenthandler.cpp:760)
- **gpt:** ⚠️ PARTIAL (58) — observed qDebug() in namedMarker()/setMarker() active in release (src/documenthandler.cpp:760)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:760 793: qDebug() in getMarkerKey() line 760 and setMarker() line 793 active in release builds; CMake does not define QT_NO_DEBUG_OUTPUT
- **glm:** ✅ LEGIT (70) — documenthandler.cpp:760 793 qDebug() in namedMarker()/setMarker() active in release builds
- **kimi:** ✅ LEGIT (80) — documenthandler.cpp:760 and :793 contain unguarded qDebug() in namedMarker()/setMarker() that emit in release builds.
- **opus-ultra:** ✅ LEGIT (60) — qDebug in namedMarker/setMarker active in release builds (documenthandler.cpp:760)

### [DECL-N01] MarkersModel::keySearch — default params in definition but not declaration  ·  _SPLIT_  ·  Low
`markersmodel.h:64 vs markersmodel.cpp:117`
- **opus:** ⚠️ PARTIAL (45) — keySearch default params in def not decl (markersmodel.h:64)
- **gpt:** ✅ LEGIT (78) — MarkersModel::keySearch - default params in definition but not declaration (src/markersmodel.h:64)
- **deepseek:** ✅ LEGIT (75) — keySearch has default params in definition but not declaration (markersmodel.h:64 vs markersmodel.cpp:117)
- **glm:** ✅ LEGIT (75) — markersmodel.h:64 vs markersmodel.cpp:117 keySearch default params in definition but not declaration
- **kimi:** ✅ LEGIT (95) — markersmodel.h:64 declares keySearch(int key,int currentPosition,bool reverse,bool wrap) without defaults; markersmodel.cpp:117 defines defaults (0,false,true) invisible to MOC and QML callers.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — keySearch default params in def not decl (markersmodel.h:64)

### [DECL-N02] SessionModel::resetInternalData() missing override keyword and Qt 6 version guard  ·  _SPLIT_  ·  Low
`promptsession.h:74-75`
- **opus:** ⚠️ PARTIAL (40) — resetInternalData missing override (promptsession.h:74)
- **gpt:** ✅ LEGIT (78) — SessionModel::resetInternalData() missing override keyword and Qt 6 version guard (src/promptsession.h:74)
- **deepseek:** ✅ LEGIT (85) — resetInternalData missing override keyword; no Qt6 version guard in SessionModel (promptsession.h:74-75)
- **glm:** ⚠️ PARTIAL (60) — promptsession.h:74-75 resetInternalData missing override keyword and Qt 6 version guard
- **kimi:** ✅ LEGIT (90) — promptsession.h:74-75 declares resetInternalData() without override and without the #if QT_VERSION>=6 guard that MarkersModel uses.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — resetInternalData missing override (promptsession.h:74)

### [DEF-N02] DropArea internalDrag always false — internal drag handler dead code  ·  _SPLIT_  ·  Medium
`Prompter.qml:1331,1350`
- **opus:** ⚠️ PARTIAL (50) — DropArea internalDrag always false -> handler dead code (Prompter.qml:1331)
- **gpt:** ⚠️ PARTIAL (58) — observed DropArea internalDrag always false - internal drag handler dead code (src/prompter/Prompter.qml:1331)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:1331/1350: internalDrag always false never set true; startTextDrag/startRangeDrag never called from QML — internal drag handler dead code
- **glm:** ✅ LEGIT (75) — Prompter.qml:1331 1350 DropArea internalDrag always false; internal drag handler dead code
- **kimi:** ✅ LEGIT (75) — Prompter.qml:1331 internalDrag is always false; startTextDrag/startRangeDrag are never called from QML, so internal drag path is dead.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — DropArea internalDrag always false -> handler dead code (Prompter.qml:1331)

### [DLG-N03] errorDialog MessageDialog has no title  ·  _SPLIT_  ·  Low
`Prompter.qml:2510-2513`
- **opus:** ⚠️ PARTIAL (45) — errorDialog MessageDialog has no title (Prompter.qml:2510)
- **gpt:** ✅ LEGIT (78) — errorDialog MessageDialog has no title (src/prompter/Prompter.qml:2510)
- **deepseek:** ✅ LEGIT (90) — errorDialog at Prompter.qml:2510 has no title — blank title bar
- **glm:** ✅ LEGIT (75) — Prompter.qml:2510-2513 errorDialog MessageDialog has no title set
- **kimi:** ✅ LEGIT (80) — Prompter.qml:2510 MessageDialog has no title property, so error dialogs show a blank title bar.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — errorDialog MessageDialog has no title (Prompter.qml:2510)

### [DLG-N07] 5 showPassiveNotification() calls ignore passiveNotifications preference  ·  _SPLIT_  ·  Low
`Find.qml:133,135,160, EditorToolbar.qml:627, PrompterPage.qml:890`
- **opus:** ⚠️ PARTIAL (45) — 5 showPassiveNotification ignore preference (Find.qml:133)
- **gpt:** ✅ LEGIT (78) — 5 showPassiveNotification() calls ignore passiveNotifications preference (src/prompter/Find.qml:133)
- **deepseek:** ✅ LEGIT (85) — 5 showPassiveNotification calls lack root.passiveNotifications guard — fire even when disabled
- **glm:** ✅ LEGIT (75) — Find.qml:133+ 5 showPassiveNotification calls ignore passiveNotifications preference
- **kimi:** ✅ LEGIT (85) — Find.qml:133/135/160, EditorToolbar.qml:627, PrompterPage.qml:890 call showPassiveNotification without checking root.passiveNotifications.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — 5 showPassiveNotification ignore preference (Find.qml:133)

### [DLG-N08] 3 save-completion passive notifications lack passiveNotifications guard  ·  _SPLIT_  ·  Low
`Prompter.qml:2294,2296,2474,2499`
- **opus:** ⚠️ PARTIAL (45) — save notifications lack passiveNotifications guard (Prompter.qml:2294)
- **gpt:** ✅ LEGIT (78) — 3 save-completion passive notifications lack passiveNotifications guard (src/prompter/Prompter.qml:2294)
- **deepseek:** ✅ LEGIT (85) — Save notifications at Prompter.qml:2294 2296 2474 2499 lack passiveNotifications guard
- **glm:** ✅ LEGIT (75) — Prompter.qml:2294+ 3 save-completion passive notifications lack passiveNotifications guard
- **kimi:** ✅ LEGIT (80) — Prompter.qml:2294/2296 save-completion notifications are not guarded by root.passiveNotifications unlike other call sites.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — save notifications lack passiveNotifications guard (Prompter.qml:2294)

### [DLG-N10] TimerClock ColorDialog selectedColor never initialized from persisted settings  ·  _SPLIT_  ·  Medium
`TimerClock.qml:198-210`
- **opus:** ⚠️ PARTIAL (45) — ColorDialog selectedColor not init from settings (TimerClock.qml:198)
- **gpt:** ✅ LEGIT (78) — TimerClock ColorDialog selectedColor never initialized from persisted settings (src/prompter/TimerClock.qml:198)
- **deepseek:** ✅ LEGIT (90) — TimerClock.qml:198-210: onVisibleChanged sets custom 'color' prop but never selectedColor (the dialog's actual display property); dialog shows Qt default on first open
- **glm:** ✅ LEGIT (75) — TimerClock.qml:198-210 ColorDialog selectedColor never initialized from persisted settings
- **kimi:** ✅ LEGIT (85) — TimerClock.qml:198-210 ColorDialog initializes custom 'color' but not 'selectedColor' which the dialog displays.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — ColorDialog selectedColor not init from settings (TimerClock.qml:198)

### [DLG-N11] PrompterPage ColorDialogs — dead acceptedColor property binding  ·  _SPLIT_  ·  Low
`PrompterPage.qml:1010,1025, PrompterView.qml:240-241`
- **opus:** ⚠️ PARTIAL (45) — ColorDialogs dead acceptedColor binding (PrompterPage.qml:1010)
- **gpt:** ✅ LEGIT (78) — PrompterPage ColorDialogs - dead acceptedColor property binding (src/kirigami_ui/PrompterPage.qml:1010)
- **deepseek:** ✅ LEGIT (90) — PrompterPage.qml:1010/1025: acceptedColor declared but never assigned; PrompterView.qml:240-241 binds prompter.textColor/textBackground to dead property — masked by direct setTextColor() in onAccepted
- **glm:** ✅ LEGIT (75) — PrompterPage.qml:1010 1025 PrompterView.qml:240-241 ColorDialogs have dead acceptedColor property binding
- **kimi:** ✅ LEGIT (70) — PrompterPage.qml:1010,1025 ColorDialogs declare acceptedColor but never assign; PrompterView.qml:240-241 binds to the default value.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — ColorDialogs dead acceptedColor binding (PrompterPage.qml:1010)

### [DPI-01] TimerClock.qml:127 devicePixelRatio in raw arithmetic with magic multiplier  ·  _SPLIT_  ·  Medium
`TimerClock.qml:127`
- **opus:** ⚠️ PARTIAL (40) — devicePixelRatio raw arithmetic magic multiplier (TimerClock.qml:127)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/prompter/TimerClock.qml:127)
- **deepseek:** ✅ LEGIT (80) — <<3 multiplier at TimerClock.qml:127 produces inconsistent scaling on fractional HiDPI
- **glm:** ⚠️ PARTIAL (65) — TimerClock.qml:127 devicePixelRatio in raw arithmetic with magic multiplier; non-standard scaling
- **kimi:** ✅ LEGIT (85) — TimerClock.qml:127 mixes screen.devicePixelRatio with a bitwise <<3 on real values, truncating fractional scale.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — devicePixelRatio raw arithmetic magic multiplier (TimerClock.qml:127)

### [DPI-04] InputsOverlay.qml:33 height:680 hardcoded  ·  _SPLIT_  ·  Medium
`InputsOverlay.qml:33`
- **opus:** ✅ LEGIT (60) — InputsOverlay height:680 hardcoded (InputsOverlay.qml:33)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/kirigami_ui/InputsOverlay.qml:33)
- **deepseek:** ✅ LEGIT (90) — Hardcoded 680px height at InputsOverlay.qml:33 — exceeds screen on HiDPI at 1080p
- **glm:** ✅ LEGIT (80) — InputsOverlay.qml:33 height:680 hardcoded (duplicate of DSZ-01)
- **kimi:** ✅ LEGIT (80) — InputsOverlay.qml:33 fixed logical height 680 exceeds small-screen phones, causing clipping.
- **opus-ultra:** ✅ LEGIT (60) — InputsOverlay height:680 hardcoded (InputsOverlay.qml:33)

### [DRAG-N01] Image resize body drag: cursor shows OpenHandCursor until drag threshold exceeded  ·  _SPLIT_  ·  Low
`Prompter.qml:1651`
- **opus:** ⚠️ PARTIAL (45) — image-resize body drag cursor until threshold (Prompter.qml:1651)
- **gpt:** ⚠️ PARTIAL (58) — observed Image resize body drag: cursor shows OpenHandCursor until drag threshold exceeded (src/prompter/Prompter.qml:1651)
- **deepseek:** ✅ LEGIT (80) — dragTarget.manualDrag=false until threshold; cursorShape shows OpenHandCursor during press-to-drag phase at Prompter.qml:1651
- **glm:** ✅ LEGIT (65) — Prompter.qml:1651 Image resize body drag: cursor shows OpenHandCursor until drag threshold exceeded
- **kimi:** ✅ LEGIT (60) — Prompter.qml image-resize body MouseArea defaults to OpenHandCursor; only changes on active drag
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — image-resize body drag cursor until threshold (Prompter.qml:1651)

### [DRAG-N02] textDragArea has no cursorShape — no cursor feedback during text drag  ·  _SPLIT_  ·  Low
`Prompter.qml:1429-1431`
- **opus:** ✅ LEGIT (55) — textDragArea no cursorShape; no drag cursor feedback (Prompter.qml:1429)
- **gpt:** ⚠️ PARTIAL (58) — observed textDragArea has no cursorShape - no cursor feedback during text drag (src/prompter/Prompter.qml:1429)
- **deepseek:** ✅ LEGIT (80) — textDragArea MouseArea lacks cursorShape at Prompter.qml:1429-1431; no visual cursor change during text drag
- **glm:** ✅ LEGIT (65) — Prompter.qml:1429-1431 textDragArea has no cursorShape; no cursor feedback during text drag
- **kimi:** ✅ LEGIT (70) — Prompter.qml:1429-1431 textDragArea has no cursorShape; no text-drag cursor feedback
- **opus-ultra:** ✅ LEGIT (55) — textDragArea no cursorShape; no drag cursor feedback (Prompter.qml:1429)

### [DRW-01] interalFocusElsewhere() misses 3 OverlaySheets + 2 Drawers — hotkeys pass through  ·  _SPLIT_  ·  Medium
`Prompter.qml:283-296`
- **opus:** ⚠️ PARTIAL (50) — interalFocusElsewhere() misses sheets/drawers -> hotkey passthrough (Prompter.qml:283)
- **gpt:** ⚠️ PARTIAL (58) — observed interalFocusElsewhere() misses 3 OverlaySheets + 2 Drawers - hotkeys pass through (src/prompter/Prompter.qml:283)
- **deepseek:** ✅ LEGIT (88) — hotkey guard misses obsConfiguration dictionariesSheet customWordsSheet contextDrawer globalMenu (Prompter.qml:283-296)
- **glm:** ⚠️ PARTIAL (65) — Prompter.qml:283-296 interalFocusElsewhere misses 3 OverlaySheets + 2 Drawers; hotkeys pass through
- **kimi:** ✅ LEGIT (85) — Prompter.qml:283-296 omits obsConfiguration/dictionariesSheet/customWordsSheet/globalMenu/contextDrawer; hotkeys pass through open overlays/drawers.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — interalFocusElsewhere() misses sheets/drawers -> hotkey passthrough (Prompter.qml:283)

### [DRW-02] globalDrawer and contextDrawer missing from ESC dismiss chain  ·  _SPLIT_  ·  Medium
`main.qml:481-504, +windows:452-487, +android:391-426`
- **opus:** ⚠️ PARTIAL (50) — globalDrawer/contextDrawer not in ESC dismiss chain (main.qml:481)
- **gpt:** ⚠️ PARTIAL (58) — observed globalDrawer and contextDrawer missing from ESC dismiss chain (src/kirigami_ui/main.qml:481)
- **deepseek:** ✅ LEGIT (88) — ESC handler checks 8 sheets but not contextDrawer.drawerOpen nor globalMenu.drawerOpen; drawer stays (main.qml:481-504)
- **glm:** ⚠️ PARTIAL (65) — main.qml:481-504 ESC handler missing globalDrawer and contextDrawer from dismiss chain
- **kimi:** ✅ LEGIT (85) — main.qml:481-504 closes markersDrawer and overlay sheets but never checks contextDrawer.drawerOpen or globalMenu.drawerOpen.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — globalDrawer/contextDrawer not in ESC dismiss chain (main.qml:481)

### [DSZ-01] InputsOverlay hardcoded height:680 — overflows on phones  ·  _SPLIT_  ·  Medium
`InputsOverlay.qml:33`
- **opus:** ✅ LEGIT (60) — hardcoded height:680 overflows small phones (dup DPI-04) (InputsOverlay.qml:33)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/kirigami_ui/InputsOverlay.qml:33)
- **deepseek:** ✅ LEGIT (88) — hardcoded height:680 no Math.min; on phones(~500dp usable) content exceeds viewport (InputsOverlay.qml:33)
- **glm:** ✅ LEGIT (80) — InputsOverlay.qml:33 height:680 hardcoded; overflows on phones
- **kimi:** ✅ LEGIT (80) — InputsOverlay.qml:33 hardcodes height:680, which overflows the usable height on phones and small screens.
- **opus-ultra:** ✅ LEGIT (60) — hardcoded height:680 overflows small phones (dup DPI-04) (InputsOverlay.qml:33)

### [DSZ-02] pointerConfiguration OverlaySheet no vertical ScrollView  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:1426-1445`
- **opus:** ⚠️ PARTIAL (45) — pointerConfiguration sheet lacks vertical ScrollView (PrompterPage.qml:1426)
- **gpt:** ✅ LEGIT (78) — pointerConfiguration OverlaySheet no vertical ScrollView (src/kirigami_ui/PrompterPage.qml:1426)
- **deepseek:** ✅ LEGIT (88) — PointerSettings inside OverlaySheet no ScrollView/Flickable; ~600-800px implicit height overflows small screens (PrompterPage.qml:1426-1445)
- **glm:** ✅ LEGIT (75) — PrompterPage.qml:1426-1445 pointerConfiguration OverlaySheet no vertical ScrollView
- **kimi:** ✅ LEGIT (85) — PrompterPage.qml:1426 pointerConfiguration OverlaySheet contains PointerSettings directly with no ScrollView/Flickable for overflow.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — pointerConfiguration sheet lacks vertical ScrollView (PrompterPage.qml:1426)

### [EDGE-07] Q_UNREACHABLE in Q_INVOKABLE method — UB if called from QML  ·  _SPLIT_  ·  High
`src/shakedetector.cpp:49-51`
- **opus:** ⚠️ PARTIAL (60) — Q_UNREACHABLE in Q_INVOKABLE but only caller fires on iOS (shakedetector.cpp:51)
- **gpt:** ⚠️ PARTIAL (58) — observed Q_UNREACHABLE in Q_INVOKABLE method - UB if called from QML (src/shakedetector.cpp:49)
- **deepseek:** ✅ LEGIT (85) — Q_UNREACHABLE() at shakedetector.cpp:49-51 in Q_INVOKABLE showUndoRedoDialog; compiles to __builtin_unreachable() in release — UB if QML calls this
- **glm:** ⚠️ PARTIAL (60) — shakedetector.cpp:49-51 Q_UNREACHABLE in showUndoRedoDialog; reachable from QML but non-iOS .cpp build has empty body not Q_UNREACHABLE
- **kimi:** ✅ LEGIT (90) — shakedetector.cpp:49-51 Q_UNREACHABLE in Q_INVOKABLE showUndoRedoDialog; reachable from QML -> UB.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — Q_UNREACHABLE in Q_INVOKABLE but only caller fires on iOS (shakedetector.cpp:51)

### [EDGE-11] m_reply dereference without null check in loadFromNetworkFinihed()  ·  _SPLIT_  ·  Medium
`src/documenthandler.cpp:890`
- **opus:** ⚠️ PARTIAL (60) — m_reply->readAll no null check; fires after get() (documenthandler.cpp:890)
- **gpt:** ⚠️ PARTIAL (58) — observed m_reply dereference without null check in loadFromNetworkFinihed() (src/documenthandler.cpp:890)
- **deepseek:** ✅ LEGIT (85) — m_reply->readAll() at doc.cpp:890 w/o null check; m_reply uninitialized in constructor; signal-carried reply pointer ignored — null deref risk
- **glm:** ✅ LEGIT (85) — documenthandler.cpp:890 m_reply->readAll() without null check; m_reply could be null if request never started
- **kimi:** ✅ LEGIT (80) — documenthandler.cpp:890 m_reply->readAll() without null check.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — m_reply->readAll no null check; fires after get() (documenthandler.cpp:890)

### [ENUM-01] documenthandler.cpp:1108 updateContents switch no default — silent data loss  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1108`
- **opus:** ⚠️ PARTIAL (45) — updateContents switch has no default but covers all TextFormat values (documenthandler.cpp:1108)
- **gpt:** ✅ LEGIT (78) — documenthandler.cpp:1108 updateContents switch no default - silent data loss (src/documenthandler.cpp:1108)
- **deepseek:** ✅ LEGIT (90) — No default case in switch(format) at documenthandler.cpp:1108 — doc cleared with zero content inserted
- **glm:** ✅ LEGIT (80) — documenthandler.cpp:1108 updateContents switch has no default case; silent data loss for unknown format
- **kimi:** ✅ LEGIT (85) — documenthandler.cpp:1108 updateContents switch has no default; an unknown format value clears the document without inserting content.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — updateContents switch has no default but covers all TextFormat values (documenthandler.cpp

### [ERR-N02] insertImageAt() async callback silently discards 3 failure modes  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1744-1752`
- **opus:** ⚠️ PARTIAL (55) — insertImageAt async callback returns silently on 3 failure modes (documenthandler.cpp:1744)
- **gpt:** ⚠️ PARTIAL (58) — observed insertImageAt() async callback silently discards 3 failure modes (src/documenthandler.cpp:1744)
- **deepseek:** ✅ LEGIT (95) — documenthandler.cpp:1744-1752: async callback three silent returns — reply error (1744) null image (1748) null doc (1751); none emit error() — user sees nothing
- **glm:** ✅ LEGIT (75) — documenthandler.cpp:1744-1752 insertImageAt async callback silently discards 3 failure modes
- **kimi:** ✅ LEGIT (80) — documenthandler.cpp:1744-1752 insertImageAt async callback returns silently on network error, null image or null document.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — insertImageAt async callback returns silently on 3 failure modes (documenthandler.cpp:1744

### [EVT-01] velocityDragArea (z:5) blocks viewport.mouse (z:0) wheel events  ·  _SPLIT_  ·  High
`PrompterPage.qml:875 vs PrompterView.qml:254`
- **opus:** ⚠️ PARTIAL (50) — velocityDragArea z:5 may intercept viewport wheel; depends on enabled/anchors (PrompterPage.qml:875)
- **gpt:** ⚠️ PARTIAL (58) — observed velocityDragArea (z:5) blocks viewport.mouse (z:0) wheel events (src/kirigami_ui/PrompterPage.qml:875)
- **deepseek:** ⚠️ PARTIAL (60) — velocityDragArea z:5 above mouse z:0 but acceptedButtons=Middle|Right wheel not consumed; passes through normally (PrompterPage.qml:875 PrompterView.qml:254)
- **glm:** ✅ LEGIT (80) — PrompterPage.qml:875 velocityDragArea z:5 blocks viewport.mouse z:0 wheel events
- **kimi:** ✅ LEGIT (85) — PrompterPage.qml:875 velocityDragArea has z:5 and fills viewport; PrompterView.qml:254 viewport.mouse is z:0, so wheel events are blocked.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — velocityDragArea z:5 may intercept viewport wheel; depends on enabled/anchors (PrompterPag

### [EVT-03] velocityDragOverlay (z:7) steals clicks from control buttons (z:6)  ·  _SPLIT_  ·  High
`PrompterPage.qml:914 vs PrompterView.qml:61`
- **opus:** ⚠️ PARTIAL (50) — velocityDragOverlay z:7 may steal clicks from z:6 buttons (PrompterPage.qml:914)
- **gpt:** ⚠️ PARTIAL (58) — observed velocityDragOverlay (z:7) steals clicks from control buttons (z:6) (src/kirigami_ui/PrompterPage.qml:914)
- **deepseek:** ✅ LEGIT (90) — velocityDragOverlay z:7 above upperControls z:6; left-click buttons requires double-click when indicator on (PrompterPage.qml:914 PrompterView.qml:61)
- **glm:** ✅ LEGIT (80) — PrompterPage.qml:914 velocityDragOverlay z:7 steals clicks from control buttons z:6
- **kimi:** ✅ LEGIT (85) — PrompterPage.qml:914 velocityDragOverlay has z:7; PrompterView.qml:62/112/196 upper controls are z:6, so overlay steals clicks.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — velocityDragOverlay z:7 may steal clicks from z:6 buttons (PrompterPage.qml:914)

### [EVT-04] Drag breaks editor.x declarative binding permanently  ·  _SPLIT_  ·  High
`Prompter.qml:1984,958`
- **opus:** ⚠️ PARTIAL (50) — width-handle drag.target editor may break editor.x binding (Prompter.qml:1984)
- **gpt:** ⚠️ PARTIAL (58) — observed Drag breaks editor.x declarative binding permanently (src/prompter/Prompter.qml:1984)
- **deepseek:** ✅ LEGIT (92) — drag.target:editor writes x imperatively breaking x:contentsPlacement*(prompter.width)+20 binding (Prompter.qml:1984 958)
- **glm:** ✅ LEGIT (80) — Prompter.qml:1984 958 Drag on editor breaks x declarative binding permanently
- **kimi:** ✅ LEGIT (85) — Prompter.qml:1984 sets drag.target: editor, which imperatively writes x and breaks the declarative x binding at Prompter.qml:958.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — width-handle drag.target editor may break editor.x binding (Prompter.qml:1984)

### [EVT-05] Drag breaks positionHandler.x declarative binding permanently  ·  _SPLIT_  ·  High
`Prompter.qml:2018,926`
- **opus:** ⚠️ PARTIAL (50) — drag.target positionHandler may break its x binding (Prompter.qml:2018)
- **gpt:** ⚠️ PARTIAL (58) — observed Drag breaks positionHandler.x declarative binding permanently (src/prompter/Prompter.qml:2018)
- **deepseek:** ✅ LEGIT (92) — drag.target:positionHandler writes x imperatively breaking declarative x binding (Prompter.qml:2018 926)
- **glm:** ✅ LEGIT (80) — Prompter.qml:2018 926 Drag breaks positionHandler.x declarative binding permanently
- **kimi:** ✅ LEGIT (85) — Prompter.qml:2018 sets drag.target: positionHandler, which imperatively writes x and breaks the declarative x binding at Prompter.qml:926.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — drag.target positionHandler may break its x binding (Prompter.qml:2018)

### [EVT-06] Drag breaks stopwatch.x binding permanently  ·  _SPLIT_  ·  Medium
`TimerClock.qml:178,130`
- **opus:** ⚠️ PARTIAL (50) — drag breaks stopwatch.x binding (TimerClock.qml:178)
- **gpt:** ⚠️ PARTIAL (58) — observed Drag breaks stopwatch.x binding permanently (src/prompter/TimerClock.qml:178)
- **deepseek:** ✅ LEGIT (90) — drag.target:parent writes x imperatively; stopwatch no longer re-centers on resize after one drag (TimerClock.qml:178 130)
- **glm:** ✅ LEGIT (80) — TimerClock.qml:178 130 Drag breaks stopwatch.x binding permanently
- **kimi:** ✅ LEGIT (85) — TimerClock.qml:178 sets drag.target: parent (stopwatch), which imperatively writes x and breaks the x binding at TimerClock.qml:130.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — drag breaks stopwatch.x binding (TimerClock.qml:178)

### [EVT-09] Flow ToolSeparator visibility compares y of potentially invisible rows  ·  _SPLIT_  ·  Low
`EditorToolbar.qml:246-249,284-287,309-312,347-350,433-437,549-552,710-713,774-777`
- **opus:** ⚠️ PARTIAL (45) — Flow ToolSeparator visibility compares y of invisible rows (EditorToolbar.qml:246)
- **gpt:** ⚠️ PARTIAL (52) — observed Flow ToolSeparator visibility compares y of potentially invisible rows (src/kirigami_ui/EditorToolbar.qml:246)
- **deepseek:** ✅ LEGIT (78) — ToolSeparator visibility compares row.y when row may be invisible(y=0); false positive match (EditorToolbar.qml:246-249)
- **glm:** ⚠️ PARTIAL (60) — EditorToolbar.qml:246+ ToolSeparator visibility compares y of potentially invisible rows; cosmetic
- **kimi:** ✅ LEGIT (70) — EditorToolbar.qml:246-249 ToolSeparator visibility compares anchorsRow.y to playbackRow.y even when a row may be invisible at y=0.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — Flow ToolSeparator visibility compares y of invisible rows (EditorToolbar.qml:246)

### [EVT-10] Nested MouseAreas with hoverEnabled steal hover from parent Buttons  ·  _SPLIT_  ·  Low
`ProjectionsManager.qml:347-354,376-383,405-412`
- **opus:** ⚠️ PARTIAL (50) — nested hoverEnabled MouseAreas steal hover (ProjectionsManager.qml:347)
- **gpt:** ⚠️ PARTIAL (58) — observed Nested MouseAreas with hoverEnabled steal hover from parent Buttons (src/prompter/ProjectionsManager.qml:347)
- **deepseek:** ✅ LEGIT (85) — nested MouseArea hoverEnabled:true fills parent Button; Button.hovered never fires (ProjectionsManager.qml:347-354)
- **glm:** ⚠️ PARTIAL (60) — ProjectionsManager.qml:347+ nested MouseAreas with hoverEnabled steal hover from parent Buttons
- **kimi:** ✅ LEGIT (85) — ProjectionsManager.qml:347-354 places a hover-enabled MouseArea filling a Button, so the Button's hovered state never triggers.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — nested hoverEnabled MouseAreas steal hover (ProjectionsManager.qml:347)

### [EVT-N12] velocityDragArea and viewport.mouse share z:5 — wheel dispatch ambiguous  ·  _SPLIT_  ·  Low
`PrompterPage.qml:875-877 vs PrompterView.qml:3083`
- **opus:** ⚠️ PARTIAL (50) — velocityDragArea/viewport.mouse share z:5; wheel ambiguous (PrompterPage.qml:875)
- **gpt:** ⚠️ PARTIAL (58) — observed velocityDragArea and viewport.mouse share z:5 - wheel dispatch ambiguous (src/kirigami_ui/PrompterPage.qml:875)
- **deepseek:** ✅ LEGIT (60) — velocityDragArea and viewport.mouse share z:5; wheel event dispatch ambiguous (PrompterPage.qml:875-877 vs PrompterView.qml:249)
- **glm:** ⚠️ PARTIAL (60) — PrompterPage.qml:875-877 vs PrompterView.qml:3083 velocityDragArea and viewport.mouse share z:5; wheel dispatch ambiguous
- **kimi:** ⚠️ PARTIAL (50) — velocityDragArea is z:5 but viewport.mouse gets z:5 only in Prompting/Countdown states; real ambiguity not demonstrated.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — velocityDragArea/viewport.mouse share z:5; wheel ambiguous (PrompterPage.qml:875)

### [EVT-N13] rewind()/fastForward() event undefined — winding state permanently locked after first use  ·  _SPLIT_  ·  High
`Prompter.qml:547-571`
- **opus:** ❔ UNSURE (45) — rewind()/fastForward() event-undefined claim; needs function body (Prompter.qml:547)
- **gpt:** ⚠️ PARTIAL (58) — observed rewind()/fastForward() event undefined - winding state permanently locked after first use (src/prompter/Prompter.qml:547)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:547-571: rewind/fastForward access 'event.key' but accept no event parameter; event=undefined; winding permanently locked
- **glm:** ✅ LEGIT (75) — Prompter.qml:547-571 rewind()/fastForward() reference event.key but declare no event parameter; undefined
- **kimi:** ✅ LEGIT (90) — Prompter.qml:552/565 reference `event.key` inside functions that have no `event` parameter
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — rewind()/fastForward() event-undefined claim; needs function body (Prompter.qml:547)

### [FD-N01] || should be && in autoReload guard — user preference ignored for non-binary files  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1025`
- **opus:** ⚠️ PARTIAL (55) — !skipAutoReload || autoReload() likely should be &&; ambiguous (documenthandler.cpp:1025)
- **gpt:** ⚠️ PARTIAL (58) — observed || should be && in autoReload guard - user preference ignored for non-binary files (src/documenthandler.cpp:1025)
- **deepseek:** ✅ LEGIT (90) — !skipAutoReload||autoReload() always true when skipAutoReload=false; user autoReload setting ignored at documenthandler.cpp:1025
- **glm:** ✅ LEGIT (65) — documenthandler.cpp:1025 || should be && in autoReload guard; user preference ignored for non-binary files
- **kimi:** ✅ LEGIT (85) — documenthandler.cpp:1025 watcher is added when !skipAutoReload||autoReload(), so autoReload=false is ignored for normal files
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — !skipAutoReload || autoReload() likely should be &&; ambiguous (documenthandler.cpp:1025)

### [FINAL-04] NSIS start-menu shortcut icon name mismatches actual binary name  ·  _SPLIT_  ·  High
`CMakeLists.txt:465`
- **opus:** ⚠️ PARTIAL (50) — qprompt.exe vs QPrompt.exe; Windows FS case-insensitive (CMakeLists.txt:465)
- **gpt:** ⚠️ PARTIAL (58) — observed NSIS start-menu shortcut icon name mismatches actual binary name (CMakeLists.txt:465)
- **deepseek:** ⚠️ PARTIAL (60) — CMakeLists.txt:465 overwrites line 463 QPrompt.exe with qprompt.exe — case mismatch but Windows FS case-insensitive so functionally works
- **glm:** ✅ LEGIT (80) — CMakeLists.txt:465 NSIS_INSTALLED_ICON_NAME set to 'qprompt' but binary is QPrompt on Windows
- **kimi:** ✅ LEGIT (95) — CMakeLists.txt:465 sets CPACK_NSIS_INSTALLED_ICON_NAME to qprompt${CMAKE_EXECUTABLE_SUFFIX}, overwriting correct QPrompt.exe at line 463.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — qprompt.exe vs QPrompt.exe; Windows FS case-insensitive (CMakeLists.txt:465)

### [FINAL-10] Two animations target same `position` property — conflict  ·  _SPLIT_  ·  High
`src/prompter/Prompter.qml:839,909`
- **opus:** ⚠️ PARTIAL (55) — Behavior + NumberAnimation both on position (Prompter.qml:839,909)
- **gpt:** ⚠️ PARTIAL (58) — observed Two animations target same position property - conflict (src/prompter/Prompter.qml:839)
- **deepseek:** ✅ LEGIT (90) — Prompter.qml:839 Behavior on position AND line 909 NumberAnimation on position both target prompter.position — conflicting animations
- **glm:** ✅ LEGIT (80) — Prompter.qml:839 909 Behavior on position and NumberAnimation on position both target position property
- **kimi:** ✅ LEGIT (90) — Prompter.qml:839 Behavior on position and line 909 NumberAnimation on position both target prompter.position, causing conflicting animations.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — Behavior + NumberAnimation both on position (Prompter.qml:839

### [FINAL-14] Wrong placeholder `%0` instead of `%1` — font name never displayed  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/EditorToolbar.qml:588`
- **opus:** ⚠️ PARTIAL (55) — qsTr('Active font: %0'); %0 unconventional, Qt arg() handling uncertain (EditorToolbar.qml:588)
- **gpt:** ⚠️ PARTIAL (58) — Qt arg can substitute %0; this is unconventional, not proven broken (src/kirigami_ui/EditorToolbar.qml:588)
- **deepseek:** ✅ LEGIT (98) — EditorToolbar.qml:588 qsTr('Active font: %0').arg() — Qt arg() uses 1-based placeholders(%1); %0 treated as literal font name never displayed
- **glm:** ✅ LEGIT (85) — EditorToolbar.qml:588 qsTr('Active font: %0') uses %0 but String.arg expects %1; font name never displayed
- **kimi:** ✅ LEGIT (95) — EditorToolbar.qml:588 uses qsTr(\Active font: %0\").arg(...); qsTr/arg use 1-based placeholders
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — qsTr('Active font: %0'); %0 unconventional

### [FINAL-15] Missing edit block wrapping in setLineHeight/setParagraphHeight  ·  _SPLIT_  ·  High
`src/documenthandler.cpp:1596,1610`
- **opus:** ⚠️ PARTIAL (55) — joinPreviousEditBlock undo-grouping; restatement of R3-DOC-02 (documenthandler.cpp:1596)
- **gpt:** ⚠️ PARTIAL (58) — observed Missing edit block wrapping in setLineHeight/setParagraphHeight (src/documenthandler.cpp:1596)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:1596/1610 joinPreviousEditBlock() no-op without beginEditBlock; endEditBlock() unmatched — same as R3-DOC-02(duplicate finding)
- **glm:** ✅ LEGIT (85) — documenthandler.cpp:1596 1610 setLineHeight/setParagraphHeight use joinPreviousEditBlock without beginEditBlock; unbalanced
- **kimi:** ✅ LEGIT (85) — documenthandler.cpp:1596,1610 joinPreviousEditBlock() is called without a matching beginEditBlock(), causing malformed undo grouping.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — joinPreviousEditBlock undo-grouping; restatement of R3-DOC-02 (documenthandler.cpp:1596)

### [FINAL-16] Countdown completion uses state++ bypassing toggle() entry actions  ·  _SPLIT_  ·  Critical
`src/prompter/Countdown.qml:122-123`
- **opus:** ❔ UNSURE (50) — state++ bypasses toggle() side-effects; state-machine claim (Countdown.qml:122)
- **gpt:** ⚠️ PARTIAL (58) — observed Countdown completion uses state++ bypassing toggle() entry actions (src/prompter/Countdown.qml:122)
- **deepseek:** ✅ LEGIT (80) — Countdown.qml:122-123 prompter.state++ increments enum int directly — bypasses toggle() entry/exit actions and state transition guards
- **glm:** ✅ LEGIT (85) — Countdown.qml:122-123 state++ bypasses toggle() entry actions; direct state mutation skips transition logic
- **kimi:** ✅ LEGIT (95) — Countdown.qml:122-123 does prompter.state++ at end, bypassing toggle() which should reset timer/preventSleep/projections.
- **opus-ultra:** ❔ UNSURE (50) — max: unverifiable statically (runtime/semantic) — state++ bypasses toggle() side-effects; state-machine claim (Countdown.qml:122)

### [FINAL-19] Encoding fallback uses toLocal8Bit() instead of dictionary's actual encoding  ·  _SPLIT_  ·  Medium
`src/spellchecker.cpp:402-406, 408-412`
- **opus:** ✅ LEGIT (70) — encode/decode use locale 8-bit not dict encoding (dup R3-SPL) (spellchecker.cpp:402)
- **gpt:** ✅ LEGIT (78) — Encoding fallback uses toLocal8Bit() instead of dictionary's actual encoding (src/spellchecker.cpp:402)
- **deepseek:** ✅ LEGIT (85) — spellchecker.cpp:402-406/408-412 encode/decode fallback toLocal8Bit/fromLocal8Bit ignores dictionary encoding — same root as R3-SPL-01/02(duplicate)
- **glm:** ⚠️ PARTIAL (65) — spellchecker.cpp:402-412 encode/decode fallback uses toLocal8Bit/fromLocal8Bit instead of dictionary's actual encoding
- **kimi:** ✅ LEGIT (85) — spellchecker.cpp:402-406,408-412 encode/decode fall back to toLocal8Bit/fromLocal8Bit when encoding is not UTF-8, ignoring d.encoding.
- **opus-ultra:** ✅ LEGIT (70) — encode/decode use locale 8-bit not dict encoding (dup R3-SPL) (spellchecker.cpp:402)

### [FINAL-22] Behavior.onRunningChanged calls toggle() from within animation handler — re-entrant state change  ·  _SPLIT_  ·  High
`src/prompter/Prompter.qml:855`
- **opus:** ⚠️ PARTIAL (50) — toggle() in animation onRunningChanged; likely intended end-of-scroll (Prompter.qml:855)
- **gpt:** ⚠️ PARTIAL (58) — observed Behavior.onRunningChanged calls toggle() from within animation handler - re-entrant state chang (src/prompter/Prompter.qml:855)
- **deepseek:** ✅ LEGIT (85) — Prompter.qml:855 return prompter.toggle() inside Behavior.onRunningChanged animation handler — re-entrant state change during animation callback
- **glm:** ✅ LEGIT (80) — Prompter.qml:855 Behavior.onRunningChanged calls toggle() from within animation handler; re-entrant state change
- **kimi:** ✅ LEGIT (85) — Prompter.qml:855 calls prompter.toggle() inside Behavior on position onRunningChanged handler, causing re-entrant state transition.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — toggle() in animation onRunningChanged; likely intended end-of-scroll (Prompter.qml:855)

### [FLOW-N02] increaseVelocity()/decreaseVelocity() skip velocity change when paused  ·  _SPLIT_  ·  Medium
`Prompter.qml:494-497,510-513`
- **opus:** ❔ UNSURE (45) — increase/decreaseVelocity skip change when paused; domain (Prompter.qml:494)
- **gpt:** ⚠️ PARTIAL (58) — observed increaseVelocity()/decreaseVelocity() skip velocity change when paused (src/prompter/Prompter.qml:494)
- **deepseek:** ✅ LEGIT (90) — Prompter.qml:494-497/510-513: increaseVelocity/decreaseVelocity gate __i modification on this.__play; when paused __i never changes but __play=true & position updated — behavioral inconsistency
- **glm:** ✅ LEGIT (75) — Prompter.qml:494-497 510-513 increaseVelocity/decreaseVelocity skip velocity change when paused (__play false)
- **kimi:** ✅ LEGIT (85) — Prompter.qml:494-497,510-513 increase/decreaseVelocity only modify __i when __play is true, so paused adjustments do nothing to velocity.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — increase/decreaseVelocity skip change when paused; domain (Prompter.qml:494)

### [FOC-N03] Tab/Backtab asymmetry — Backtab silently unhandled  ·  _SPLIT_  ·  Low
`Prompter.qml:2170-2173`
- **opus:** ⚠️ PARTIAL (50) — Tab/Backtab asymmetry; Backtab unhandled (Prompter.qml:2170)
- **gpt:** ✅ LEGIT (78) — Tab/Backtab asymmetry - Backtab silently unhandled (src/prompter/Prompter.qml:2170)
- **deepseek:** ✅ LEGIT (85) — Keys.onPressed handles Qt.Key_Tab but not Qt.Key_Backtab; Shift+Tab silently unhandled (Prompter.qml:2170-2173)
- **glm:** ⚠️ PARTIAL (60) — Prompter.qml:2170-2173 Tab handled but Backtab silently unhandled; minor asymmetry
- **kimi:** ✅ LEGIT (85) — Prompter.qml:2170-2173 handles Qt.Key_Tab but has no Qt.Key_Backtab case, breaking Shift+Tab navigation.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — Tab/Backtab asymmetry; Backtab unhandled (Prompter.qml:2170)

### [FONT-METRIC-01] pixelSize used as line-height proxy — core scroll timing off by ~57%  ·  _SPLIT_  ·  High
`Prompter.qml:119-122,125,128`
- **opus:** ❔ UNSURE (40) — pixelSize-as-lineheight scroll-timing heuristic; '57%' unverifiable (Prompter.qml:119)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Prompter.qml:119)
- **deepseek:** ✅ LEGIT (90) — Prompter.qml:119-122: fontSize (pixelSize=em-size) used as line-height proxy; actual height ~1.57x; __relativeSpeed ~57% off
- **glm:** ✅ LEGIT (75) — Prompter.qml:119-122 125 128 pixelSize used as line-height proxy; core scroll timing off by ~57%
- **kimi:** ✅ LEGIT (75) — Prompter.qml:119-122 scroll timing uses editor.font.pixelSize, not the actual rendered line height
- **opus-ultra:** ❔ UNSURE (40) — max: unverifiable statically (runtime/semantic) — pixelSize-as-lineheight scroll-timing heuristic; '57%' unverifiable (Prompter.qml:119)

### [FONT-METRIC-02] FontLoader status never checked — font substitution silently fails  ·  _SPLIT_  ·  Medium
`Prompter.qml:995-998`
- **opus:** ⚠️ PARTIAL (50) — FontLoader status never checked; substitution silent (Prompter.qml:995)
- **gpt:** ⚠️ PARTIAL (58) — observed FontLoader status never checked - font substitution silently fails (src/prompter/Prompter.qml:995)
- **deepseek:** ✅ LEGIT (85) — Prompter.qml:995-998: FontLoader source set but status never checked; corrupted/missing font silently substituted with no error
- **glm:** ✅ LEGIT (70) — Prompter.qml:995-998 FontLoader status never checked; font substitution silently fails
- **kimi:** ✅ LEGIT (90) — Prompter.qml:995-998 FontLoader has no status handling; font substitution failures are silent
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — FontLoader status never checked; substitution silent (Prompter.qml:995)

### [FONT-N02] FontLoader id typo: westernSeriousSansfFont — stray 'f' in "Sans"  ·  _SPLIT_  ·  Low
`EditorToolbar.qml:558, Prompter.qml:996`
- **opus:** ✅ LEGIT (65) — FontLoader id typo westernSeriousSansfFont stray f (EditorToolbar.qml:558)
- **gpt:** ⚠️ PARTIAL (58) — observed FontLoader id typo: westernSeriousSansFont - stray 'f' in "Sans" (src/kirigami_ui/EditorToolbar.qml:558)
- **deepseek:** ✅ LEGIT (95) — EditorToolbar.qml:558/Prompter.qml:996: FontLoader id westernSeriousSansfFont — stray f in Sansf; zero runtime impact (only id) but confusing for maintainers
- **glm:** ✅ LEGIT (70) — EditorToolbar.qml:558 Prompter.qml:996 FontLoader id typo: westernSeriousSansfFont has stray 'f'
- **kimi:** ✅ LEGIT (90) — EditorToolbar.qml:558 and Prompter.qml:996 FontLoader id westernSeriousSansfFont contains stray 'f' typo.
- **opus-ultra:** ✅ LEGIT (65) — FontLoader id typo westernSeriousSansfFont stray f (EditorToolbar.qml:558)

### [GEO-02] main.qml persists x/y/width/height with zero validation  ·  _SPLIT_  ·  Medium
`main.qml:85-91, +windows/main.qml`
- **opus:** ⚠️ PARTIAL (50) — persists x/y/w/h with no on-restore validation; can restore off-screen (main.qml:85)
- **gpt:** ⚠️ PARTIAL (58) — observed main.qml persists x/y/width/height with zero validation (src/kirigami_ui/main.qml:85)
- **deepseek:** ✅ LEGIT (90) — Settings alias x/y/width/height at main.qml:87-90 — no screen bounds validation on restore
- **glm:** ✅ LEGIT (80) — main.qml:85-91 persists x/y/width/height with zero validation; could restore off-screen
- **kimi:** ✅ LEGIT (85) — main.qml:85-91 persists window geometry without clamping to available screen geometry; can place window off-screen.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — persists x/y/w/h with no on-restore validation; can restore off-screen (main.qml:85)

### [GEO-03] +android/main.qml no minimumWidth/minimumHeight  ·  _SPLIT_  ·  Low
`+android/main.qml`
- **opus:** ⚠️ PARTIAL (40) — +android no minimumWidth/Height (main.qml)
- **gpt:** ⚠️ PARTIAL (58) — observed +android/main.qml no minimumWidth/minimumHeight (src/kirigami_ui/+android/main.qml:1)
- **deepseek:** ✅ LEGIT (90) — +android/main.qml lacks minimumWidth/minimumHeight — base variant has 351/291
- **glm:** ✅ LEGIT (75) — +android/main.qml no minimumWidth/minimumHeight declarations
- **kimi:** ✅ LEGIT (70) — +android/main.qml has no minimumWidth/minimumHeight unlike base and +windows variants.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — +android no minimumWidth/Height (main.qml)

### [GSW-N01] MarkersDrawer SwipeListItem navigates on swipe — gesture conflict on touch  ·  _SPLIT_  ·  Medium
`MarkersDrawer.qml:70-74`
- **opus:** ⚠️ PARTIAL (45) — SwipeListItem navigates on swipe; gesture conflict (MarkersDrawer.qml:70)
- **gpt:** ⚠️ PARTIAL (58) — observed MarkersDrawer SwipeListItem navigates on swipe - gesture conflict on touch (src/kirigami_ui/MarkersDrawer.qml:70)
- **deepseek:** ✅ LEGIT (90) — MarkersDrawer.qml:70-74: SwipeListItem onPressed fires at start of every touch including swipe; navigating to marker+closing drawer on swipe-to-reveal gesture conflict
- **glm:** ✅ LEGIT (70) — MarkersDrawer.qml:70-74 SwipeListItem navigates on swipe; gesture conflict on touch
- **kimi:** ✅ LEGIT (80) — MarkersDrawer.qml:70-74 SwipeListItem onPressed navigates and conflicts with swipe gesture.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — SwipeListItem navigates on swipe; gesture conflict (MarkersDrawer.qml:70)

### [GSW-N02] Flickable onDragStarted uses stale __iBackup after non-prompting drags  ·  _SPLIT_  ·  Low
`Prompter.qml:773-781,788-798`
- **opus:** ❔ UNSURE (45) — onDragStarted stale __iBackup; domain (Prompter.qml:773)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Prompter.qml:773)
- **deepseek:** ✅ LEGIT (85) — Prompter.qml:773-781/788-798: onMovementEnded leaves __iBackup non-zero in editing mode; second drag guard (line 776) prevents backup — stale first-drag velocity restored
- **glm:** ⚠️ PARTIAL (60) — Prompter.qml:773-781 788-798 Flickable onDragStarted uses stale __iBackup after non-prompting drags
- **kimi:** ✅ LEGIT (80) — Prompter.qml:773-798 __iBackup saved during non-Prompting drag and reused stale in later Prompting drag.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — onDragStarted stale __iBackup; domain (Prompter.qml:773)

### [HDR-N01] promptsession.h not in CMakeLists.txt — SessionModel/DataPoint dead code  ·  _SPLIT_  ·  Low
`src/promptsession.h, src/promptsess.cpp, src/CMakeLists.txt`
- **opus:** ✅ LEGIT (60) — promptsession.h/cpp not in CMakeLists; SessionModel dead code (promptsession.h)
- **gpt:** ⚠️ PARTIAL (58) — observed promptsession.h not in CMakeLists.txt - SessionModel/DataPoint dead code (src/promptsession.h:1)
- **deepseek:** ✅ LEGIT (95) — prompsession.h/cpp not in src/CMakeLists.txt — never MOC-processed never compiled dead code
- **glm:** ✅ LEGIT (80) — promptsession.h not in CMakeLists.txt; SessionModel/DataPoint are dead code
- **kimi:** ✅ LEGIT (80) — promptsession.h/cpp exist but are absent from src/CMakeLists.txt source lists; the code is never compiled.
- **opus-ultra:** ✅ LEGIT (60) — promptsession.h/cpp not in CMakeLists; SessionModel dead code (promptsession.h)

### [HDR-N02] telemetry.h not in CMakeLists.txt — Telemetry dead code  ·  _SPLIT_  ·  Low
`src/telemetry.h, src/telemetry.cpp, src/CMakeLists.txt`
- **opus:** ✅ LEGIT (60) — telemetry.h not in CMakeLists; Telemetry dead code (telemetry.h)
- **gpt:** ⚠️ PARTIAL (58) — observed telemetry.h not in CMakeLists.txt - Telemetry dead code (src/telemetry.h:1)
- **deepseek:** ✅ LEGIT (95) — telemetry.h/cpp not in src/CMakeLists.txt — Q_OBJECT class never compiled dead code
- **glm:** ✅ LEGIT (80) — telemetry.h/telemetry.cpp not in CMakeLists.txt; Telemetry dead code
- **kimi:** ✅ LEGIT (80) — telemetry.h/cpp exist but are absent from src/CMakeLists.txt source lists; class is never compiled.
- **opus-ultra:** ✅ LEGIT (60) — telemetry.h not in CMakeLists; Telemetry dead code (telemetry.h)

### [HK-N01] Missing event.isAutoRepeat guard on main Keys.onPressed  ·  _SPLIT_  ·  High
`Prompter.qml:2672`
- **opus:** ⚠️ PARTIAL (50) — no event.isAutoRepeat guard on main Keys.onPressed; impact varies (Prompter.qml:2672)
- **gpt:** ⚠️ PARTIAL (58) — observed Missing event.isAutoRepeat guard on main Keys.onPressed (src/prompter/Prompter.qml:2672)
- **deepseek:** ✅ LEGIT (90) — Keys.onPressed at Prompter.qml:2672 — no event.isAutoRepeat guard repeat-fire on held keys
- **glm:** ✅ LEGIT (80) — Prompter.qml:2672 Keys.onPressed has no event.isAutoRepeat guard; key auto-repeat triggers multiple actions
- **kimi:** ✅ LEGIT (95) — Prompter.qml:2672 Keys.onPressed has no event.isAutoRepeat guard, so held keys rapidly retrigger velocity/pause/stop/skip actions
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — no event.isAutoRepeat guard on main Keys.onPressed; impact varies (Prompter.qml:2672)

### [HK-N03] platformName() != "wayland" fails on "wayland-egl" — global hotkeys dead  ·  _SPLIT_  ·  High
`globalhotkeys.cpp:16 sites`
- **opus:** ⚠️ PARTIAL (50) — platformName()!='wayland' could miss 'wayland-egl'; Qt usually reports 'wayland' (globalhotkeys.cpp)
- **gpt:** ⚠️ PARTIAL (58) — observed platformName() != "wayland" fails on "wayland-egl" - global hotkeys dead (src/globalhotkeys.cpp:822)
- **deepseek:** ✅ LEGIT (90) — platform!='wayland' at globalhotkeys.cpp:119 fails on 'wayland-egl' — all global hotkeys dead
- **glm:** ⚠️ PARTIAL (65) — globalhotkeys.cpp platformName()!='wayland' fails on 'wayland-egl'; but this is for QHotkey which doesn't support Wayland anyway
- **kimi:** ✅ LEGIT (90) — globalhotkeys.cpp ~16 sites compare platformName() != 'wayland'; on wayland-egl QHotkey path runs and KGlobalAccel is bypassed, breaking global hotkeys
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — platformName()!='wayland' could miss 'wayland-egl'; Qt usually reports 'wayland' (globalho

### [HK-N04] No auto-repeat guard in key-binding configuration Keys.onPressed  ·  _SPLIT_  ·  Medium
`KeyInputButton.qml:103`
- **opus:** ⚠️ PARTIAL (45) — no auto-repeat guard in key-binding Keys.onPressed (KeyInputButton.qml:103)
- **gpt:** ⚠️ PARTIAL (58) — observed No auto-repeat guard in key-binding configuration Keys.onPressed (src/kirigami_ui/KeyInputButton.qml:103)
- **deepseek:** ✅ LEGIT (85) — Keys.onPressed at KeyInputButton.qml:103 — no auto-repeat guard races with toggleButtonsOff
- **glm:** ✅ LEGIT (80) — KeyInputButton.qml:103 key-binding configuration Keys.onPressed has no auto-repeat guard
- **kimi:** ✅ LEGIT (90) — KeyInputButton.qml:103 Keys.onPressed lacks event.isAutoRepeat guard, allowing double-assignment while rebinding keys
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — no auto-repeat guard in key-binding Keys.onPressed (KeyInputButton.qml:103)

### [HK-N06] isValidInput checks local keybindings only — silent conflict with global hotkeys  ·  _SPLIT_  ·  Low
`KeyInputButton.qml:62-85`
- **opus:** ⚠️ PARTIAL (45) — isValidInput checks local keybinds only (KeyInputButton.qml:62)
- **gpt:** ⚠️ PARTIAL (58) — observed isValidInput checks local keybindings only - silent conflict with global hotkeys (src/kirigami_ui/KeyInputButton.qml:62)
- **deepseek:** ✅ LEGIT (80) — isValidInput at KeyInputButton.qml:62 checks only local prompter.keys — silent conflict with global hotkeys
- **glm:** ✅ LEGIT (75) — KeyInputButton.qml:62-85 isValidInput checks local keybindings only; silent conflict with global hotkeys
- **kimi:** ✅ LEGIT (85) — KeyInputButton.qml:62-95 isValidInput only checks prompter.keys actions, ignoring AppController global hotkeys so identical binds can coexist
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — isValidInput checks local keybinds only (KeyInputButton.qml:62)

### [HSCROLL-N01] InputsOverlay Flickables use contentWidth: width instead of implicitWidth — horizontal overflow clipped  ·  _SPLIT_  ·  Medium
`InputsOverlay.qml:95,552`
- **opus:** ⚠️ PARTIAL (50) — Flickable contentWidth:width vs implicitWidth (InputsOverlay.qml:95)
- **gpt:** ⚠️ PARTIAL (58) — observed InputsOverlay Flickables use contentWidth: width instead of implicitWidth - horizontal overflow (src/kirigami_ui/InputsOverlay.qml:95)
- **deepseek:** ✅ LEGIT (95) — InputsOverlay.qml:95 552: contentWidth set to Flickable's own width via buttonGrid.width/hotkeyGrid.width; horizontal overflow clipped
- **glm:** ✅ LEGIT (70) — InputsOverlay.qml:95 552 Flickables use contentWidth: width instead of implicitWidth; horizontal overflow clipped
- **kimi:** ✅ LEGIT (90) — InputsOverlay.qml:95/552 set contentWidth to grid.width (== Flickable width), preventing horizontal scroll
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — Flickable contentWidth:width vs implicitWidth (InputsOverlay.qml:95)

### [HSCROLL-N02] Inner Flickables missing flickableDirection: VerticalFlick — conflict with parent horizontal ListView  ·  _SPLIT_  ·  Medium
`InputsOverlay.qml:92,549`
- **opus:** ⚠️ PARTIAL (50) — inner Flickables missing flickableDirection (InputsOverlay.qml:92)
- **gpt:** ⚠️ PARTIAL (58) — observed Inner Flickables missing flickableDirection: VerticalFlick - conflict with parent horizontal Li (src/kirigami_ui/InputsOverlay.qml:92)
- **deepseek:** ✅ LEGIT (90) — InputsOverlay.qml:92 549: inner Flickables lack flickableDirection:VerticalFlick; default AutoFlickDirection intercepts horizontal tab swipes
- **glm:** ✅ LEGIT (70) — InputsOverlay.qml:92 549 inner Flickables missing flickableDirection: VerticalFlick; conflict with parent
- **kimi:** ✅ LEGIT (80) — InputsOverlay.qml:92/549 Flickables inside a horizontal ListView lack flickableDirection: VerticalFlick
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — inner Flickables missing flickableDirection (InputsOverlay.qml:92)

### [HTK-01] KGlobalAccel default permanently destroyed on first user customization  ·  _SPLIT_  ·  Critical
`globalhotkeys.cpp:1130,1138`
- **opus:** ❔ UNSURE (45) — KGlobalAccel default/override logic; needs customization-path trace (globalhotkeys.cpp:1130)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/globalhotkeys.cpp:1130)
- **deepseek:** ✅ LEGIT (95) — removeAllShortcuts at 1130 clears default+user then reads already-cleared default at 1138; defaults lost (globalhotkeys.cpp:1130 1138)
- **glm:** ⚠️ PARTIAL (65) — globalhotkeys.cpp:1130 1138 KGlobalAccel defaults overwritten on customization but setDefaultShortcut preserves them
- **kimi:** ✅ LEGIT (95) — globalhotkeys.cpp:1130 removeAllShortcuts clears defaults; line 1138 reads already-cleared defaultShortcut, then writes empty default.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — KGlobalAccel default/override logic; needs customization-path trace (globalhotkeys.cpp:113

### [HTK-02] User shortcuts never persisted when only Use_GlobalAccel defined (no QHotkey)  ·  _SPLIT_  ·  High
`globalhotkeys.cpp:831`
- **opus:** ❔ UNSURE (45) — QSettings save under #ifdef QHotkey; KGlobalAccel persists itself (globalhotkeys.cpp:831)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/globalhotkeys.cpp:831)
- **deepseek:** ✅ LEGIT (92) — QSettings save gated on #ifdef QHotkey_FOUND; KDE-only builds never persist shortcuts (globalhotkeys.cpp:831)
- **glm:** ✅ LEGIT (80) — globalhotkeys.cpp:831 when only Use_GlobalAccel is defined (no QHotkey) settings.setValue is in QHotkey ifdef block; not persisted
- **kimi:** ✅ LEGIT (90) — globalhotkeys.cpp:831 QSettings persistence block is inside #ifdef QHotkey_FOUND, so KDE-only builds never save custom shortcuts.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — QSettings save under #ifdef QHotkey; KGlobalAccel persists itself (globalhotkeys.cpp:831)

### [HTK-03] KGlobalAccel defaults silently zeroed on non-Wayland when QHotkey co-exists  ·  _SPLIT_  ·  High
`globalhotkeys.cpp:1123-1127,1132`
- **opus:** ⚠️ PARTIAL (50) — KGlobalAccel shortcut zeroed on non-Wayland when QHotkey co-exists; by-design (globalhotkeys.cpp:1123)
- **gpt:** ⚠️ PARTIAL (58) — observed KGlobalAccel defaults silently zeroed on non-Wayland when QHotkey co-exists (src/globalhotkeys.cpp:1123)
- **deepseek:** ✅ LEGIT (90) — on non-Wayland key->unknown/modifiers->NoModifier before setDefault; zeroed fallback (globalhotkeys.cpp:1123-1127)
- **glm:** ✅ LEGIT (80) — globalhotkeys.cpp:1123-1127 1132 on non-Wayland with QHotkey co-existing KGlobalAccel defaults zeroed via shortcut=Qt::Key_unknown
- **kimi:** ✅ LEGIT (90) — globalhotkeys.cpp:1123-1127 overwrite key/modifiers to unknown/NoModifier on non-Wayland when QHotkey exists, zeroing KGlobalAccel defaults.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — KGlobalAccel shortcut zeroed on non-Wayland when QHotkey co-exists; by-design (globalhotke

### [HTK-05] VelocityTo0 default shortcut uses `Qt::Key_acute` — unreachable dead key  ·  _SPLIT_  ·  Medium
`globalhotkeys.cpp:657`
- **opus:** ⚠️ PARTIAL (50) — Qt::Key_acute default; obscure but intentional (globalhotkeys.cpp:657)
- **gpt:** ⚠️ PARTIAL (58) — observed VelocityTo0 default shortcut uses Qt::Keyacute - unreachable dead key (src/globalhotkeys.cpp:657)
- **deepseek:** ✅ LEGIT (90) — Qt::Key_acute is combining dead key unreachable via physical US/ANSI keyboard (globalhotkeys.cpp:657)
- **glm:** ✅ LEGIT (75) — globalhotkeys.cpp:657 VelocityTo0 default uses Qt::Key_acute which is a dead key; unreachable on most layouts
- **kimi:** ✅ LEGIT (85) — globalhotkeys.cpp:657 uses Qt::Key_acute as default for VelocityTo0; acute is a dead key on US/ANSI keyboards.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — Qt::Key_acute default; obscure but intentional (globalhotkeys.cpp:657)

### [HTK-06] Pause (Ctrl+Space) and Stop (Meta+Space) conflict — Meta+Space captured by OS  ·  _SPLIT_  ·  Medium
`globalhotkeys.cpp:581,586`
- **opus:** ⚠️ PARTIAL (45) — Ctrl/Meta+Space shortcut OS-conflict; environment (globalhotkeys.cpp:581)
- **gpt:** ⚠️ PARTIAL (58) — observed Pause (Ctrl+Space) and Stop (Meta+Space) conflict - Meta+Space captured by OS (src/globalhotkeys.cpp:581)
- **deepseek:** ✅ LEGIT (90) — Stop uses Meta/Win+Space captured by Windows Start Menu/GNOME/macOS Spotlight (globalhotkeys.cpp:581 586)
- **glm:** ✅ LEGIT (80) — globalhotkeys.cpp:581 586 Pause=Ctrl+Space and Stop=Meta+Space; Meta+Space captured by OS on many platforms
- **kimi:** ✅ LEGIT (85) — globalhotkeys.cpp:581/586 default Stop shortcut is Meta+Space, captured by Windows Start/GNOME input/macOS Spotlight.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — Ctrl/Meta+Space shortcut OS-conflict; environment (globalhotkeys.cpp:581)

### [HTK-07] Double `removeAllShortcuts()` IPC round-trip in customization path  ·  _SPLIT_  ·  Low
`globalhotkeys.cpp:1130,1139`
- **opus:** ⚠️ PARTIAL (45) — double removeAllShortcuts() IPC round-trip (globalhotkeys.cpp:1130)
- **gpt:** ⚠️ PARTIAL (58) — observed Double removeAllShortcuts() IPC round-trip in customization path (src/globalhotkeys.cpp:1130)
- **deepseek:** ✅ LEGIT (88) — removeAllShortcuts called unconditionally at 1130 then again at 1139; redundant D-Bus round-trip (globalhotkeys.cpp:1130 1139)
- **glm:** ✅ LEGIT (75) — globalhotkeys.cpp:1130 1139 removeAllShortcuts called twice in customization path; redundant IPC
- **kimi:** ✅ LEGIT (80) — globalhotkeys.cpp:1130 calls removeAllShortcuts unconditionally, then again at line 1139 in the !setAsDefault branch.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — double removeAllShortcuts() IPC round-trip (globalhotkeys.cpp:1130)

### [HTK-08] key/modifiers parameters silently discarded mid-function on non-Wayland  ·  _SPLIT_  ·  Low
`globalhotkeys.cpp:1123-1127`
- **opus:** ⚠️ PARTIAL (50) — key/modifiers zeroed mid-function on non-Wayland; by-design (globalhotkeys.cpp:1123)
- **gpt:** ⚠️ PARTIAL (58) — observed key/modifiers parameters silently discarded mid-function on non-Wayland (src/globalhotkeys.cpp:1123)
- **deepseek:** ✅ LEGIT (85) — key/modifiers by-value params overwritten mid-function; misleading signature obscured HTK-01/03 (globalhotkeys.cpp:1123-1127)
- **glm:** ✅ LEGIT (75) — globalhotkeys.cpp:1123-1127 key/modifiers parameters discarded on non-Wayland when QHotkey co-exists
- **kimi:** ✅ LEGIT (85) — globalhotkeys.cpp:1123-1127 silently overwrite key and modifiers parameters to unknown/NoModifier on non-Wayland.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — key/modifiers zeroed mid-function on non-Wayland; by-design (globalhotkeys.cpp:1123)

### [I18N-N01] Stale source-location line numbers in all 20 .ts files  ·  _SPLIT_  ·  Low
`po/*.ts (20 files)`
- **opus:** ⚠️ PARTIAL (40) — stale source-location line numbers in .ts files; harmless
- **gpt:** ⚠️ PARTIAL (58) — observed Stale source-location line numbers in all 20 .ts files (po/qprompt_en.ts:1)
- **deepseek:** ✅ LEGIT (80) — lupdate not re-run — source line numbers in 20 .ts files stale Qt Linguist navigation broken
- **glm:** ✅ LEGIT (75) — po/*.ts files have stale source-location line numbers from lupdate not being re-run
- **kimi:** ✅ LEGIT (70) — po/*.ts files contain stale source-location line numbers because lupdate has not been rerun; translator UX issue.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — stale source-location line numbers in .ts files; harmless

### [I18N-N02] Vanished translation entries not purged across 13 language files  ·  _SPLIT_  ·  Low
`13 of 20 .ts files (de:14, es:14, pt_PT:13, ru:13, uk:13, zh:13, pt_BR:10, cs:8, fr:8, fi:4, ko:4, nl:4, oc:2)`
- **opus:** ⚠️ PARTIAL (40) — vanished translation entries not purged; harmless
- **gpt:** ⚠️ PARTIAL (58) — observed Vanished translation entries not purged across 13 language files (po/qprompt_de.ts:14)
- **deepseek:** ✅ LEGIT (80) — 13 .ts files contain type='vanished' entries — not cleaned with lupdate -no-obsolete
- **glm:** ✅ LEGIT (75) — 13 of 20 .ts files have vanished translation entries not purged with lrelease -idbased
- **kimi:** ✅ LEGIT (70) — Multiple .ts files contain type=\vanished\" entries that have not been purged with lupdate -no-obsolete."
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — vanished translation entries not purged; harmless

### [IMG-N01] Missing go-previous-symbolic.svg — back-navigation icon blank on Android/Windows  ·  _SPLIT_  ·  Medium
`+android/main.qml:575, +windows/main.qml:631`
- **opus:** ❔ UNSURE (45) — go-previous-symbolic.svg may be absent from breeze subset; needs icon check (main.qml:575)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/kirigami_ui/+android/main.qml:575)
- **deepseek:** ❔ UNSURE (30) — icon presence depends on breeze-internal subset bundling; DUPLICATE-ID per csv
- **glm:** ✅ LEGIT (80) — +android/main.qml:575 +windows/main.qml:631 reference go-previous-symbolic.svg; icon exists in Breeze subset
- **kimi:** ✅ LEGIT (95) — +android/main.qml:575 and +windows/main.qml:631 source qrc:/.../go-previous-symbolic.svg, but the file does not exist anywhere in the repository.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — go-previous-symbolic.svg may be absent from breeze subset; needs icon check (main.qml:575)

### [IMP-N01] import Qt.labs.platform 1.1 — Menu/MenuBar/MenuItem dropped in Qt 6  ·  _SPLIT_  ·  Critical
`src/kirigami_ui/main.qml:29,617-922`
- **opus:** ❌ FALSE (60) — Qt.labs.platform Menu/MenuBar/MenuItem still exist in Qt 6; ships & works (main.qml:29)
- **gpt:** ❌ FALSE (76) — Qt.labs.platform types are still used here under Qt 6 (src/kirigami_ui/main.qml:29)
- **deepseek:** ⚠️ PARTIAL (75) — main.qml:29 imports Qt.labs.platform 1.1 — Qt6.2+ re-added Labs Platform module with version mapping; but exact 1.1->6.x mapping depends on Qt build
- **glm:** ⚠️ PARTIAL (65) — main.qml:29 imports Qt.labs.platform 1.1 as Labs; in Qt 6 the module is Qt.labs.platform but version should be omitted. Labs.Menu/MenuBar still exist in Qt 6.
- **kimi:** ❌ FALSE (80) — Qt.labs.platform 1.1 still exports MenuBar/Menu/MenuItem in Qt 6.8.2 target; types are not dropped (native integration is platform-limited).
- **opus-ultra:** ❌ FALSE (60) — Qt.labs.platform Menu/MenuBar/MenuItem still exist in Qt 6; ships & works (main.qml:29)

### [IMP-NEW-02] main.cpp:22 #include "qglobal.h" uses quotes + Qt5-era name  ·  _SPLIT_  ·  Low
`main.cpp:22`
- **opus:** ⚠️ PARTIAL (45) — #include \qglobal.h\" quotes + Qt5-era name; works (main.cpp:22)"
- **gpt:** ⚠️ PARTIAL (58) — observed main.cpp:22 #include "qglobal.h" uses quotes + Qt5-era name (src/main.cpp:22)
- **deepseek:** ⚠️ PARTIAL (80) — #include 'qglobal.h' at main.cpp:22 — quotes + Qt5 name; Qt6 canonical is <QtGlobal> harmless currently
- **glm:** ⚠️ PARTIAL (60) — main.cpp:22 #include 'qglobal.h' uses quotes and Qt5-era name; works but non-idiomatic
- **kimi:** ❌ FALSE (80) — main.cpp:22 #include \qglobal.h\" works because Qt still provides the header; it is non-canonical but not broken."
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — #include \qglobal.h\" quotes + Qt5-era name; works (main.cpp:22)"

### [IMP-NEW-05] pointers.qrc RESOURCE_PREFIX conflicts with qt_add_qml_module  ·  _SPLIT_  ·  Low (orphaned QRC, never compiled)
`pointers.qrc:2, src/CMakeLists.txt:253`
- **opus:** ❔ UNSURE (45) — pointers.qrc RESOURCE_PREFIX vs qt_add_qml_module; domain (CMakeLists.txt:2)
- **gpt:** ⚠️ PARTIAL (58) — observed pointers.qrc RESOURCEPREFIX conflicts with qtaddqmlmodule (src/prompter/pointers/pointers.qrc:2)
- **deepseek:** ⚠️ PARTIAL (80) — pointers.qrc prefix conflicts with qt_add_qml_module at src/CMakeLists.txt:253 but QRC is orphaned never compiled
- **glm:** ⚠️ PARTIAL (55) — pointers.qrc RESOURCE_PREFIX conflicts with qt_add_qml_module; orphaned QRC never compiled
- **kimi:** ✅ LEGIT (70) — pointers.qrc is orphaned and its RESOURCE_PREFIX would overlap the qt_add_qml_module prefix if ever activated.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — pointers.qrc RESOURCE_PREFIX vs qt_add_qml_module; domain (CMakeLists.txt:2)

### [INT-N01] quint64→int narrowing at DocumentHandler→MarkersModel boundary (4 sites)  ·  _SPLIT_  ·  Low
`documenthandler.cpp:1713,1721, markersmodel.h:62-63`
- **opus:** ⚠️ PARTIAL (45) — quint64->int narrowing at marker boundary; docs never exceed INT_MAX (documenthandler.cpp:1713)
- **gpt:** ⚠️ PARTIAL (58) — observed quint64->int narrowing at DocumentHandler->MarkersModel boundary (4 sites) (src/documenthandler.cpp:1713)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:1713/1721: quint64->int narrowing when Q_INVOKABLE passes position to MarkersModel (takes int); markersmodel.h:62-63 confirm int params — 4 sites
- **glm:** ✅ LEGIT (70) — documenthandler.cpp:1713 1721 markersmodel.h:62-63 quint64→int narrowing at DocumentHandler→MarkersModel boundary
- **kimi:** ✅ LEGIT (70) — documenthandler.cpp:1713,1721 take quint64 but markersmodel.h:62-63 nextMarker/previousMarker take int; narrowing on large docs.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — quint64->int narrowing at marker boundary; docs never exceed INT_MAX (documenthandler.cpp:

### [INT-N02] replaceAll() returns long — 32-bit overflow on Windows x64  ·  _SPLIT_  ·  Medium
`documenthandler.h:228, documenthandler.cpp:1494`
- **opus:** ⚠️ PARTIAL (40) — replaceAll long is 32-bit on Win64; overflow practically impossible (documenthandler.cpp:1494)
- **gpt:** ✅ LEGIT (78) — replaceAll() returns long - 32-bit overflow on Windows x64 (src/documenthandler.h:228)
- **deepseek:** ✅ LEGIT (90) — documenthandler.h:228 / cpp:1494: replaceAll() returns long which is 32-bit on Windows x64 (LLP64); replacement counter overflows at 2^31 matches — use qlonglong
- **glm:** ⚠️ PARTIAL (60) — documenthandler.h:228 1494 replaceAll returns long; 32-bit overflow on Windows x64 where long is 32-bit
- **kimi:** ✅ LEGIT (85) — documenthandler.h:228 / documenthandler.cpp:1494 replaceAll returns long, which is 32-bit on Windows LLP64, overflowing past 2^31.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — replaceAll long is 32-bit on Win64; overflow practically impossible (documenthandler.cpp:1

### [INT-N03] 6 qsizetype→int narrowing conversions across models and loops  ·  _SPLIT_  ·  Low
`markersmodel.cpp:101,121, promptsession.cpp:88, main.cpp:274, spellchecker.cpp:98,328`
- **opus:** ⚠️ PARTIAL (40) — qsizetype->int narrowing 6 sites (markersmodel.cpp:101)
- **gpt:** ⚠️ PARTIAL (58) — observed 6 qsize_type->int narrowing conversions across models and loops (src/markersmodel.cpp:101)
- **deepseek:** ✅ LEGIT (80) — markersmodel.cpp:101/121 promptsession.cpp:88 main.cpp:274 spellchecker.cpp:98/328: qsizetype size()/length()/indexOf() narrowed to int (32-bit); practical docs within range
- **glm:** ✅ LEGIT (70) — markersmodel.cpp:101 121 promptsession.cpp:88 main.cpp:274 spellchecker.cpp:98 328 6 qsizetype→int narrowing conversions
- **kimi:** ✅ LEGIT (70) — markersmodel.cpp:101,121; promptsession.cpp:88; main.cpp:274; spellchecker.cpp:98,328 narrow qsizetype returns to int.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — qsizetype->int narrowing 6 sites (markersmodel.cpp:101)

### [INT-N04] OBS URL/Password fields disabled when WebSocket enabled — inverted logic  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:1478,1500`
- **opus:** ✅ LEGIT (55) — OBS URL/Password fields disabled when WebSocket enabled; inverted (PrompterPage.qml:1478)
- **gpt:** ⚠️ PARTIAL (58) — observed OBS URL/Password fields disabled when WebSocket enabled - inverted logic (src/kirigami_ui/PrompterPage.qml:1478)
- **deepseek:** ✅ LEGIT (85) — PrompterPage.qml:1484: wsUrlField.enabled: !enabledToggle.checked; fields disabled when WebSocket on; cannot reconfigure without disconnect
- **glm:** ✅ LEGIT (75) — PrompterPage.qml:1478 1500 OBS URL/Password fields disabled when WebSocket enabled; inverted logic
- **kimi:** ✅ LEGIT (85) — PrompterPage.qml:1484,1500 wsUrlField/wsPasswordField.enabled: !enabledToggle.checked — disabled when connection ON.
- **opus-ultra:** ✅ LEGIT (55) — OBS URL/Password fields disabled when WebSocket enabled; inverted (PrompterPage.qml:1478)

### [INT-N05] PropertyChanges permanently destroys CheckBox checked bindings on PointerSettings tab switch  ·  _SPLIT_  ·  Medium
`PointerSettings.qml:70-83`
- **opus:** ✅ LEGIT (55) — PropertyChanges destroys CheckBox checked bindings (PointerSettings.qml:70)
- **gpt:** ⚠️ PARTIAL (58) — observed PropertyChanges permanently destroys CheckBox checked bindings on PointerSettings tab switch (src/prompter/PointerSettings.qml:70)
- **deepseek:** ✅ LEGIT (90) — PointerSettings.qml:70-83: Arrow state PropertyChanges overwrites checked/enabled bindings; checkboxes permanently desync after tab switch
- **glm:** ✅ LEGIT (75) — PointerSettings.qml:70-83 PropertyChanges permanently destroys CheckBox checked bindings on tab switch
- **kimi:** ✅ LEGIT (85) — PointerSettings.qml:70-83 Arrow state PropertyChanges assigns `checked` value, breaking bindings on sameAsLeftPointer/tint checkboxes.
- **opus-ultra:** ✅ LEGIT (55) — PropertyChanges destroys CheckBox checked bindings (PointerSettings.qml:70)

### [INV-N01] QmlUtil::r() stores QML-owned QQuickItemGrabResult raw pointer — use-after-free  ·  _SPLIT_  ·  Medium
`qmlutil.hpp:175-180, main.qml:1045`
- **opus:** ⚠️ PARTIAL (50) — r() stores QML-owned grab-result raw ptr + deleteLater; UAF risk (qmlutil.hpp:175)
- **gpt:** ✅ LEGIT (78) — QmlUtil::r() stores QML-owned QQuickItemGrabResult raw pointer - use-after-free (src/qmlutil.hpp:175)
- **deepseek:** ✅ LEGIT (85) — Raw QQuickItemGrabResult* store at qmlutil.hpp:179 — QML GC may free while C++ holds pointer
- **glm:** ✅ LEGIT (80) — qmlutil.hpp:175-180 r() stores QQuickItemGrabResult raw pointer; QML may delete the source causing use-after-free
- **kimi:** ✅ LEGIT (85) — qmlutil.hpp:175-180 stores a JS-owned QQuickItemGrabResult* raw pointer and later calls deleteLater, risking use-after-free/double-free.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — r() stores QML-owned grab-result raw ptr + deleteLater; UAF risk (qmlutil.hpp:175)

### [IO-N01] saveAs() leaves _fileSystemWatcher permanently blocked on open failure  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1143,1161`
- **opus:** ⚠️ PARTIAL (45) — saveAs open-failure path may skip watcher unblock (documenthandler.cpp:1143)
- **gpt:** ✅ LEGIT (78) — saveAs() leaves _fileSystemWatcher permanently blocked on open failure (src/documenthandler.cpp:1143)
- **deepseek:** ✅ LEGIT (90) — _fileSystemWatcher->blockSignals(true) at documenthandler.cpp:1143; early return skips unblock at 1170
- **glm:** ✅ LEGIT (80) — documenthandler.cpp:1143 1161 saveAs blocks _fileSystemWatcher on open failure; never unblocked if file.open fails
- **kimi:** ✅ LEGIT (90) — documenthandler.cpp:1143 blocks watcher and line 1170 unblocks only after success; the open-failure return on line 1159 skips unblock.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — saveAs open-failure path may skip watcher unblock (documenthandler.cpp:1143)

### [JS-N01] TIMERCLOCK getTimeString() — redundant .toString() on already-string — 54 allocs/sec  ·  _SPLIT_  ·  Low
`TimerClock.qml:46-50`
- **opus:** ✅ LEGIT (50) — redundant .toString() on toFixed() result (TimerClock.qml:46)
- **gpt:** ⚠️ PARTIAL (58) — observed TIMERCLOCK getTimeString() - redundant .toString() on already-string - 54 allocs/sec (src/prompter/TimerClock.qml:46)
- **deepseek:** ✅ LEGIT (70) — TimerClock.qml:50: toFixed(2) already returns String; redundant .toString() creates extra allocs; minor GC pressure
- **glm:** ✅ LEGIT (65) — TimerClock.qml:46-50 getTimeString() redundant .toString() on already-string; 54 allocs/sec
- **kimi:** ✅ LEGIT (90) — TimerClock.qml:50 calls .toString() on values already returned as strings by .toFixed(2)
- **opus-ultra:** ✅ LEGIT (50) — redundant .toString() on toFixed() result (TimerClock.qml:46)

### [JS-N02] markerCompare() per-frame JSON.stringify() over OBS marker — 60 allocs/sec  ·  _SPLIT_  ·  Medium
`Prompter.qml:401-413`
- **opus:** ⚠️ PARTIAL (50) — per-frame JSON.stringify over OBS marker; allocations (Prompter.qml:401)
- **gpt:** ⚠️ PARTIAL (58) — observed markerCompare() per-frame JSON.stringify() over OBS marker - 60 allocs/sec (src/prompter/Prompter.qml:401)
- **deepseek:** ✅ LEGIT (85) — Prompter.qml:401-413: markerCompare fires every frame; JSON.stringify + object creation 60fps; severe GC pressure during OBS prompting
- **glm:** ✅ LEGIT (75) — Prompter.qml:401-413 markerCompare() per-frame JSON.stringify() over OBS marker; 60 allocs/sec
- **kimi:** ✅ LEGIT (90) — Prompter.qml:413 calls JSON.stringify(req) each frame while an OBS scene marker is in the read region
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — per-frame JSON.stringify over OBS marker; allocations (Prompter.qml:401)

### [JSN-02] ws.sendTextMessage() called without checking WebSocket status  ·  _SPLIT_  ·  Medium
`Prompter.qml:383,413`
- **opus:** ⚠️ PARTIAL (50) — sendTextMessage without checking ws.status (Prompter.qml:383)
- **gpt:** ✅ LEGIT (78) — ws.sendTextMessage() called without checking WebSocket status (src/prompter/Prompter.qml:383)
- **deepseek:** ✅ LEGIT (90) — ws.sendTextMessage() at Prompter.qml:383 413 without ws.status===WebSocket.Open guard
- **glm:** ✅ LEGIT (80) — Prompter.qml:383 413 ws.sendTextMessage() called without checking WebSocket active status
- **kimi:** ✅ LEGIT (85) — Prompter.qml:383 and :413 call ws.sendTextMessage without verifying ws.status === WebSocket.Open.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — sendTextMessage without checking ws.status (Prompter.qml:383)

### [KEY-N01] Named marker key binding silently discards all modifier information  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:1187, documenthandler.h:213, documenthandler.cpp:707-715, markersmodel.cpp:117-120`
- **opus:** ❔ UNSURE (45) — named-marker stores key_<code>; modifier-loss is a domain claim (documenthandler.cpp:707)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/kirigami_ui/PrompterPage.qml:1187)
- **deepseek:** ✅ LEGIT (70) — keyCode stored as bare int via toInt; Ctrl/Shift/Alt/Meta modifier info lost (documenthandler.cpp:757)
- **glm:** ✅ LEGIT (75) — PrompterPage.qml:1187 documenthandler.cpp:707-715 markersmodel.cpp:117-120 named marker key binding discards modifier info
- **kimi:** ✅ LEGIT (90) — PrompterPage.qml:1187 onSetKey ignores modifiers and calls setKeyMarker(keyCode); markers store key_<bare_code> without modifiers.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — named-marker stores key_<code>; modifier-loss is a domain claim (documenthandler.cpp:707)

### [LAY-N01] 10 Labels with Layout.margins but inside MouseArea, not direct layout child — dead  ·  _SPLIT_  ·  Low
`EditorToolbar.qml (10 Labels)`
- **opus:** ⚠️ PARTIAL (45) — Labels with Layout.margins inside MouseArea not layout child; dead (EditorToolbar.qml)
- **gpt:** ⚠️ PARTIAL (58) — observed 10 Labels with Layout.margins but inside MouseArea, not direct layout child - dead (src/kirigami_ui/EditorToolbar.qml:1)
- **deepseek:** ❔ UNSURE (50) — LAY-N01: labels inside MouseArea children not direct RowLayout children so Layout.margins dead; structure plausible but not fully traced in EditorToolbar.qml hierarchy
- **glm:** ✅ LEGIT (70) — EditorToolbar.qml 10 Labels with Layout.margins inside MouseArea not direct layout child; dead
- **kimi:** ✅ LEGIT (80) — EditorToolbar.qml Labels are children of MouseArea, not the surrounding RowLayout, so their Layout.margins are ignored.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — Labels with Layout.margins inside MouseArea not layout child; dead (EditorToolbar.qml)

### [LAY-N02] WheelSettingsOverlay explanation text constrained to single column in 2-column GridLayout  ·  _SPLIT_  ·  Low
`WheelSettingsOverlay.qml:100-109`
- **opus:** ⚠️ PARTIAL (40) — explanation text constrained to single column (WheelSettingsOverlay.qml:100)
- **gpt:** ⚠️ PARTIAL (58) — observed WheelSettingsOverlay explanation text constrained to single column in 2-column GridLayout (src/kirigami_ui/WheelSettingsOverlay.qml:100)
- **deepseek:** ❔ UNSURE (50) — LAY-N02: WheelSettingsOverlay.qml not fully read; claim about 1-column text in 2-column GridLayout cannot be verified without inspecting actual element hierarchy
- **glm:** ✅ LEGIT (70) — WheelSettingsOverlay.qml:100-109 explanation text constrained to single column in 2-column GridLayout
- **kimi:** ✅ LEGIT (80) — WheelSettingsOverlay.qml:100-109 explanation RowLayout in 2-column GridLayout lacks Layout.columnSpan:2, constrained to half width.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — explanation text constrained to single column (WheelSettingsOverlay.qml:100)

### [LAZY-N01] namedMarkerConfiguration Loader double-loads KeyInputButton — first load wasted  ·  _SPLIT_  ·  Low
`PrompterPage.qml:1172-1179`
- **opus:** ⚠️ PARTIAL (45) — namedMarkerConfiguration Loader double-loads KeyInputButton (PrompterPage.qml:1172)
- **gpt:** ⚠️ PARTIAL (58) — observed namedMarkerConfiguration Loader double-loads KeyInputButton - first load wasted (src/kirigami_ui/PrompterPage.qml:1172)
- **deepseek:** ✅ LEGIT (85) — source:'KeyInputButton.qml' starts async load; Component.onCompleted setSource() cancels+reloads — first load wasted
- **glm:** ✅ LEGIT (65) — PrompterPage.qml:1172-1179 namedMarkerConfiguration Loader double-loads KeyInputButton; first load wasted
- **kimi:** ✅ LEGIT (85) — PrompterPage.qml:1172 Loader already sets source, then onCompleted:1179 calls setSource again, reloading KeyInputButton
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — namedMarkerConfiguration Loader double-loads KeyInputButton (PrompterPage.qml:1172)

### [LAZY-N02] InputsOverlay ObjectModel eagerly loads both tabs — hidden tab content loaded prematurely  ·  _SPLIT_  ·  Medium
`InputsOverlay.qml:90-547`
- **opus:** ⚠️ PARTIAL (50) — ObjectModel eagerly loads both tabs (InputsOverlay.qml:90)
- **gpt:** ⚠️ PARTIAL (58) — observed InputsOverlay ObjectModel eagerly loads both tabs - hidden tab content loaded prematurely (src/kirigami_ui/InputsOverlay.qml:90)
- **deepseek:** ⚠️ PARTIAL (60) — ObjectModel eagerly instantiates all children by design; performance concern but not a correctness bug
- **glm:** ✅ LEGIT (70) — InputsOverlay.qml:90-547 ObjectModel eagerly loads both tabs; hidden tab content loaded prematurely
- **kimi:** ✅ LEGIT (80) — InputsOverlay.qml:90 ObjectModel contains both tab Flickables as direct children; ListView instantiates them eagerly
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — ObjectModel eagerly loads both tabs (InputsOverlay.qml:90)

### [LBL-N01] All 12 Sliders in EditorToolbar missing Layout.fillWidth: true — cramped  ·  _SPLIT_  ·  Medium
`EditorToolbar.qml (12 Slider instances)`
- **opus:** ⚠️ PARTIAL (45) — 12 Sliders missing Layout.fillWidth (EditorToolbar.qml)
- **gpt:** ⚠️ PARTIAL (58) — observed All 12 Sliders in EditorToolbar missing Layout.fillWidth: true - cramped (src/kirigami_ui/EditorToolbar.qml:1)
- **deepseek:** ✅ LEGIT (70) — EditorToolbar.qml: Sliders in RowLayout lack Layout.fillWidth — render at ~100px implicit width regardless of toolbar size; cramped controls on wide displays
- **glm:** ✅ LEGIT (70) — EditorToolbar.qml 12 Slider instances missing Layout.fillWidth: true; cramped
- **kimi:** ✅ LEGIT (90) — EditorToolbar.qml has 12 Slider declarations and none set Layout.fillWidth, so sliders render at implicit width.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — 12 Sliders missing Layout.fillWidth (EditorToolbar.qml)

### [LBL-N03] PrompterView 3× height overflow in theforce debug mode  ·  _SPLIT_  ·  Low
`PrompterPage.qml:739`
- **opus:** ⚠️ PARTIAL (40) — PrompterView height overflow in theforce debug mode (PrompterPage.qml:739)
- **gpt:** ⚠️ PARTIAL (58) — observed PrompterView 3× height overflow in theforce debug mode (src/kirigami_ui/PrompterPage.qml:739)
- **deepseek:** ✅ LEGIT (85) — PrompterPage.qml:739: when root.theforce debug mode active height=3*parent.height; at min window (291px) produces 873px — off-screen render overhead
- **glm:** ⚠️ PARTIAL (55) — PrompterPage.qml:739 PrompterView 3x height overflow in theforce debug mode; debug-only
- **kimi:** ✅ LEGIT (70) — PrompterPage.qml:739 height=(root.theforce?3:1)*parent.height creates 3x overflow in theforce debug mode.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — PrompterView height overflow in theforce debug mode (PrompterPage.qml:739)

### [LDR-N01] InputsOverlay typeof null guard fails — null.item crash on rapid close  ·  _SPLIT_  ·  Medium
`InputsOverlay.qml:105-112,562-569`
- **opus:** ⚠️ PARTIAL (50) — typeof null guard can still hit null.item on rapid close (InputsOverlay.qml:105)
- **gpt:** ⚠️ PARTIAL (58) — observed InputsOverlay typeof null guard fails - null.item crash on rapid close (src/kirigami_ui/InputsOverlay.qml:105)
- **deepseek:** ✅ LEGIT (85) — typeof null==='object' at InputsOverlay.qml:107 — guard passes when Loader.item is null TypeError on .checked
- **glm:** ✅ LEGIT (80) — InputsOverlay.qml:105-112 562-569 typeof null guard fails; typeof null==='object' so null.item crashes
- **kimi:** ✅ LEGIT (90) — InputsOverlay.qml:105-112/562-569 uses typeof item !== 'undefined'; Loader.item is null while async loading, so null.checked access can crash
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — typeof null guard can still hit null.item on rapid close (InputsOverlay.qml:105)

### [LINK-N03] Qt::WebSockets found as REQUIRED but never explicitly linked  ·  _SPLIT_  ·  Medium
`CMakeLists.txt:145, all target_link_libraries blocks`
- **opus:** ⚠️ PARTIAL (50) — Qt::WebSockets found REQUIRED but not explicitly linked; QML plugin pulls it (CMakeLists.txt:145)
- **gpt:** ✅ LEGIT (78) — Qt::WebSockets found as REQUIRED but never explicitly linked (CMakeLists.txt:145)
- **deepseek:** ✅ LEGIT (85) — src/CMakeLists.txt: all target_link_libraries blocks lack Qt6::WebSockets; find_package REQUIRED but never linked — breaks static builds if qmlimportscanner misses it
- **glm:** ✅ LEGIT (75) — CMakeLists.txt:145 Qt::WebSockets found as REQUIRED but never explicitly linked in target_link_libraries
- **kimi:** ✅ LEGIT (80) — CMakeLists.txt:145 finds Qt::WebSockets REQUIRED but src/CMakeLists.txt target_link_libraries blocks never link it.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — Qt::WebSockets found REQUIRED but not explicitly linked; QML plugin pulls it (CMakeLists.t

### [LL-N01] 10 EditorToolbar MouseArea/TextField width-depends-on-width binding loops  ·  _SPLIT_  ·  Medium
`EditorToolbar.qml (10 instances, lines 924-2053)`
- **opus:** ⚠️ PARTIAL (50) — width-depends-on-width MouseArea/TextField binding-loop risk (EditorToolbar.qml)
- **gpt:** ⚠️ PARTIAL (58) — observed 10 EditorToolbar MouseArea/TextField width-depends-on-width binding loops (src/kirigami_ui/EditorToolbar.qml:924)
- **deepseek:** ✅ LEGIT (80) — MouseArea.width->TextField.width(anchors.fill:parent)->MouseArea.width binding loop; QML engine breaks loop->TextField width=0
- **glm:** ✅ LEGIT (65) — EditorToolbar.qml 10 instances of width-depends-on-width binding loops lines 924-2053
- **kimi:** ✅ LEGIT (75) — EditorToolbar.qml:923/1039/1198 direct-input MouseAreas bind width to child widths, creating circular width dependencies
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — width-depends-on-width MouseArea/TextField binding-loop risk (EditorToolbar.qml)

### [LOAD-N01] TOCTOU race between QFile::exists() and file.open() in load()  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:944-947`
- **opus:** ⚠️ PARTIAL (50) — TOCTOU between exists() and open(); minor for desktop (documenthandler.cpp:944)
- **gpt:** ✅ LEGIT (78) — TOCTOU race between QFile::exists() and file.open() in load() (src/documenthandler.cpp:944)
- **deepseek:** ✅ LEGIT (65) — classic TOCTOU race between QFile::exists and file.open (documenthandler.cpp:944-947)
- **glm:** ✅ LEGIT (75) — documenthandler.cpp:944-947 TOCTOU race between QFile::exists() and file.open() in load()
- **kimi:** ✅ LEGIT (70) — load() checks QFile::exists at documenthandler.cpp:944 before opening at :947; file can vanish between check and open.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — TOCTOU between exists() and open(); minor for desktop (documenthandler.cpp:944)

### [LOG-04] MarkersModel::extendLastMarker modifies data without emitting dataChanged  ·  _SPLIT_  ·  Medium
`src/markersmodel.cpp:109-114`
- **opus:** ✅ LEGIT (100) — extendLastMarker no dataChanged (markersmodel.cpp:109)
- **gpt:** ✅ LEGIT (78) — extendLastMarker changes the last row without dataChanged (src/markersmodel.cpp:109)
- **deepseek:** ⚠️ PARTIAL (60) — extendLastMarker mutates m_data w/o dataChanged at markersmodel.cpp:112; but method only called from parse() which rebuilds model — may be intentional internal helper
- **glm:** ✅ LEGIT (85) — markersmodel.cpp:109-114 extendLastMarker mutates m_data.last().text but never emits dataChanged signal
- **kimi:** ✅ LEGIT (85) — markersmodel.cpp:109-114 extendLastMarker changes last marker text without emitting dataChanged.
- **opus-ultra:** ✅ LEGIT (100) — extendLastMarker no dataChanged (markersmodel.cpp:109)

### [LOG-06] DocumentHandler::replaceAll has potential infinite loop with regex  ·  _SPLIT_  ·  Medium
`src/documenthandler.cpp:1492-1520`
- **opus:** ✅ LEGIT (90) — replaceAll regex infinite-loop risk (documenthandler.cpp:1504)
- **gpt:** ✅ LEGIT (78) — DocumentHandler::replaceAll has potential infinite loop with regex (src/documenthandler.cpp:1492)
- **deepseek:** ⚠️ PARTIAL (70) — replaceAll at doc.cpp:1504-1515 wraps in beginEditBlock; insertion length change shifts search; infinite if replacement contains searchPattern but edge-case dependent
- **glm:** ✅ LEGIT (85) — documenthandler.cpp:1503-1515 replaceAll loops while resultsFound; regex replacement that contains the search pattern could loop infinitely
- **kimi:** ✅ LEGIT (85) — documenthandler.cpp:1492-1520 replaceAll loops while search finds matches; no progress guard can hang on regex/replacement overlap.
- **opus-ultra:** ✅ LEGIT (90) — replaceAll regex infinite-loop risk (documenthandler.cpp:1504)

### [LOG-07] namedMarker() fetches cursor twice — stale-content risk  ·  _SPLIT_  ·  Low
`src/documenthandler.cpp:699-705`
- **opus:** ⚠️ PARTIAL (60) — refetches textCursor() but harmless (documenthandler.cpp:699)
- **gpt:** ⚠️ PARTIAL (52) — observed namedMarker() fetches cursor twice - stale-content risk (src/documenthandler.cpp:699)
- **deepseek:** ⚠️ PARTIAL (50) — namedMarker fetches cursor 3x at doc.cpp:701-704; but QTextCursor copies are cheap; practical staleness risk minimal in single-thread context
- **glm:** ⚠️ PARTIAL (60) — documenthandler.cpp:699-705 namedMarker fetches cursor twice via textCursor() but the cursor is built from current selection state so staleness risk is minimal
- **kimi:** ✅ LEGIT (70) — documenthandler.cpp:699-705 namedMarker() null-checks one cursor then fetches fresh textCursor() twice.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — refetches textCursor() but harmless (documenthandler.cpp:699)

### [LOG-08] DataPoint default constructor leaves three members uninitialized  ·  _SPLIT_  ·  Low
`src/promptsession.h:31,38-41`
- **opus:** ✅ LEGIT (100) — 3 int members uninitialized (promptsession.h:38-40)
- **gpt:** ✅ LEGIT (88) — DataPoint default constructor leaves three members uninitialized (src/promptsession.h:31)
- **deepseek:** ✅ LEGIT (85) — DataPoint default ctor{} at promptsess.h:31; prompterWidth/lineWidth/lineHeight uninitialized fields with no =0 defaults — UB on default construct
- **glm:** ⚠️ PARTIAL (55) — promptsession.h:31 DataPoint default ctor leaves prompterWidth/lineWidth/lineHeight uninitialized but code paths always construct with explicit values
- **kimi:** ✅ LEGIT (90) — promptsession.h:31,38-40 DataPoint default ctor leaves prompterWidth/lineWidth/lineHeight uninitialized.
- **opus-ultra:** ✅ LEGIT (100) — 3 int members uninitialized (promptsession.h:38-40)

### [LOG-N05] Q_UNREACHABLE() in m_setGlobalShortcut() — UB in release on new enum value  ·  _SPLIT_  ·  Medium
`globalhotkeys.cpp:1109`
- **opus:** ⚠️ PARTIAL (50) — Q_UNREACHABLE in m_setGlobalShortcut; reachability like EDGE-10 (globalhotkeys.cpp:1109)
- **gpt:** ⚠️ PARTIAL (58) — observed Q_UNREACHABLE() in m_setGlobalShortcut() - UB in release on new enum value (src/globalhotkeys.cpp:1109)
- **deepseek:** ✅ LEGIT (90) — globalhotkeys.cpp:1109: 33-case switch with no default + Q_UNREACHABLE(); if GlobalHotkeys::Action enum extended -> undefined behavior in release builds
- **glm:** ✅ LEGIT (75) — globalhotkeys.cpp:1109 Q_UNREACHABLE() in m_setGlobalShortcut; UB in release if new enum value added
- **kimi:** ✅ LEGIT (80) — globalhotkeys.cpp:1109 Q_UNREACHABLE after switch is UB in release if an unexpected enum value occurs.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — Q_UNREACHABLE in m_setGlobalShortcut; reachability like EDGE-10 (globalhotkeys.cpp:1109)

### [LOG-N07] No error log in loadFromNetworkFinihed() — silent bad-data load  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:888-901`
- **opus:** ✅ LEGIT (55) — no error log on bad/empty network data (documenthandler.cpp:888)
- **gpt:** ⚠️ PARTIAL (58) — observed No error log in loadFromNetworkFinihed() - silent bad-data load (src/documenthandler.cpp:888)
- **deepseek:** ✅ LEGIT (95) — documenthandler.cpp:888-901: m_reply->readAll() without checking m_reply->error(); HTTP errors silently become document content with no warning log
- **glm:** ✅ LEGIT (75) — documenthandler.cpp:888-901 no error log in loadFromNetworkFinihed; silent bad-data load
- **kimi:** ✅ LEGIT (90) — documenthandler.cpp:888-901 loadFromNetworkFinihed ignores m_reply->error() and silently ignores empty responses.
- **opus-ultra:** ✅ LEGIT (55) — no error log on bad/empty network data (documenthandler.cpp:888)

### [LVW-N01] InputsOverlay.qml ListView currentIndex: PointerSettings.States.Arrow — copy-paste error  ·  _SPLIT_  ·  Low
`InputsOverlay.qml:77`
- **opus:** ⚠️ PARTIAL (45) — ListView currentIndex copy-paste PointerSettings.States.Arrow (InputsOverlay.qml:77)
- **gpt:** ⚠️ PARTIAL (58) — observed InputsOverlay.qml ListView currentIndex: PointerSettings.States.Arrow - copy-paste error (src/kirigami_ui/InputsOverlay.qml:77)
- **deepseek:** ✅ LEGIT (85) — InputsOverlay.qml:77: currentIndex: PointerSettings.States.Arrow — copy-paste from PointerSettings.qml; resolves to 0 accidentally but semantically wrong for 2-tab InputsOverlay
- **glm:** ✅ LEGIT (70) — InputsOverlay.qml:77 ListView currentIndex: PointerSettings.States.Arrow; copy-paste error from PointerSettings
- **kimi:** ✅ LEGIT (70) — InputsOverlay.qml:77 sets ListView currentIndex to PointerSettings.States.Arrow instead of first tab index.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — ListView currentIndex copy-paste PointerSettings.States.Arrow (InputsOverlay.qml:77)

### [LYR-N01] InputsOverlay calls cursorAutoHide.restart() on open instead of reset()  ·  _SPLIT_  ·  High
`src/kirigami_ui/InputsOverlay.qml:41`
- **opus:** ⚠️ PARTIAL (60) — cursorAutoHide.restart() on open vs reset() elsewhere (dup R2-OVL-01) (InputsOverlay.qml:41)
- **gpt:** ✅ LEGIT (84) — InputsOverlay calls cursorAutoHide.restart() on open instead of reset() (src/kirigami_ui/InputsOverlay.qml:41)
- **deepseek:** ✅ LEGIT (85) — InputsOverlay.qml:41 onOpened calls cursorAutoHide.restart() instead of reset() — cursor auto-hides after 1s during key binding configuration
- **glm:** ✅ LEGIT (85) — InputsOverlay.qml:41 cursorAutoHide.restart() on open instead of reset(); restart re-triggers hide timer
- **kimi:** ✅ LEGIT (90) — InputsOverlay.qml:41 calls cursorAutoHide.restart(); other overlays call reset(), so cursor auto-hides during key binding.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — cursorAutoHide.restart() on open vs reset() elsewhere (dup R2-OVL-01) (InputsOverlay.qml:4

### [LYR-N02] Three OverlaySheets missing from ESC dismiss chain  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/main.qml:489-504`
- **opus:** ⚠️ PARTIAL (50) — three OverlaySheets missing from ESC dismiss chain (main.qml:489)
- **gpt:** ✅ LEGIT (78) — Three OverlaySheets missing from ESC dismiss chain (src/kirigami_ui/main.qml:489)
- **deepseek:** ✅ LEGIT (75) — main.qml:489-504 ESC if-else chain missing obsConfiguration/dictionariesSheet/customWordsSheet — these 3 sheets never dismissed by ESC
- **glm:** ⚠️ PARTIAL (65) — main.qml:489-504 ESC handler chain missing three OverlaySheets from dismiss chain
- **kimi:** ✅ LEGIT (90) — main.qml:489-504 ESC handler omits obsConfiguration, dictionariesSheet and customWordsSheet defined in PrompterPage.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — three OverlaySheets missing from ESC dismiss chain (main.qml:489)

### [LYR-N04] ESC handler uses activeFocus in base but focus in platform variants — inconsistent  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/main.qml:512 vs +windows:483 vs +android:422`
- **opus:** ⚠️ PARTIAL (50) — ESC uses activeFocus in base vs focus in variants; inconsistent (main.qml:512)
- **gpt:** ✅ LEGIT (78) — ESC handler uses activeFocus in base but focus in platform variants - inconsistent (src/kirigami_ui/main.qml:512)
- **deepseek:** ✅ LEGIT (85) — base uses prompter.activeFocus(512) windows/android use .focus(483/422); FocusScope activeFocus vs focus divergence (main.qml:512 +windows:483 +android:422)
- **glm:** ✅ LEGIT (80) — main.qml:512 uses activeFocus; +windows:483 and +android:422 use .focus; inconsistent focus checking
- **kimi:** ✅ LEGIT (90) — main.qml:512 checks prompter.activeFocus, but +windows/main.qml:483 and +android/main.qml:422 check prompter.focus only.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — ESC uses activeFocus in base vs focus in variants; inconsistent (main.qml:512)

### [MA-N01] overlayMouseArea permanently disabled — dead MouseArea  ·  _SPLIT_  ·  Low
`ReadRegionOverlay.qml:116-122`
- **opus:** ⚠️ PARTIAL (50) — overlayMouseArea permanently disabled; dead (ReadRegionOverlay.qml:116)
- **gpt:** ✅ LEGIT (78) — overlayMouseArea permanently disabled - dead MouseArea (src/prompter/ReadRegionOverlay.qml:116)
- **deepseek:** ✅ LEGIT (95) — overlayMouseArea at ReadRegionOverlay.qml:116 has enabled:false hardcoded — dead MouseArea
- **glm:** ✅ LEGIT (75) — ReadRegionOverlay.qml:116-122 overlayMouseArea enabled:false; dead MouseArea
- **kimi:** ✅ LEGIT (70) — ReadRegionOverlay.qml:116 overlayMouseArea is enabled:false and never changed; it is dead code.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — overlayMouseArea permanently disabled; dead (ReadRegionOverlay.qml:116)

### [MENU-N01] contextMenu.popup(this) missing click coordinates — menu at wrong position  ·  _SPLIT_  ·  Medium
`Prompter.qml:1402`
- **opus:** ✅ LEGIT (55) — contextMenu.popup(this) without coordinates -> wrong position (Prompter.qml:1402)
- **gpt:** ⚠️ PARTIAL (58) — observed contextMenu.popup(this) missing click coordinates - menu at wrong position (src/prompter/Prompter.qml:1402)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:1402: contextMenu.popup(this) equivalent to popup(parent 0 0); mouse parameter with actual coordinates available but ignored — menu at wrong position on mobile/WASM
- **glm:** ✅ LEGIT (75) — Prompter.qml:1402 contextMenu.popup(this) missing click coordinates; menu at wrong position
- **kimi:** ✅ LEGIT (75) — Prompter.qml:1402 calls contextMenu.popup(this), ignoring mouse coordinates so menu opens at top-left of editor.
- **opus-ultra:** ✅ LEGIT (55) — contextMenu.popup(this) without coordinates -> wrong position (Prompter.qml:1402)

### [MENU-N02] Mobile "Add to dictionary" missing %1 placeholder — word never shown  ·  _SPLIT_  ·  Medium
`Prompter.qml:2620`
- **opus:** ✅ LEGIT (60) — mobile 'Add to dictionary' qsTr missing %1; word never shown (Prompter.qml:2620)
- **gpt:** ⚠️ PARTIAL (58) — observed Mobile "Add to dictionary" missing %1 placeholder - word never shown (src/prompter/Prompter.qml:2620)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:2620: qsTr('Add to dictionary') has no %1 placeholder; .arg(prompter.spellMisspelledWord) silently does nothing — word never shown to user
- **glm:** ✅ LEGIT (80) — Prompter.qml:2620 'Add to dictionary' uses .arg() but qsTr string may lack %1 placeholder; word never shown
- **kimi:** ✅ LEGIT (90) — Prompter.qml:2620 qsTr('Add to dictionary').arg(word) has no %1 placeholder, so the misspelled word is never shown.
- **opus-ultra:** ✅ LEGIT (60) — mobile 'Add to dictionary' qsTr missing %1; word never shown (Prompter.qml:2620)

### [MENU-N03] Text alignment menu RTL swap: labels swap but actions don't  ·  _SPLIT_  ·  Medium
`EditorToolbar.qml:362-374`
- **opus:** ⚠️ PARTIAL (55) — RTL alignment menu: labels swap but actions don't (EditorToolbar.qml:362)
- **gpt:** ⚠️ PARTIAL (58) — observed Text alignment menu RTL swap: labels swap but actions don't (src/kirigami_ui/EditorToolbar.qml:362)
- **deepseek:** ✅ LEGIT (95) — EditorToolbar.qml:362-374: text labels swap for RTL (Left<->Right) but onTriggered actions hardcoded AlignLeft/AlignRight unconditionally; RTL clicking Right sets AlignLeft
- **glm:** ✅ LEGIT (75) — EditorToolbar.qml:362-374 text alignment menu RTL swap: labels swap but actions don't
- **kimi:** ✅ LEGIT (85) — EditorToolbar.qml:362-374 RTL swaps menu labels but onTriggered always sets AlignLeft/AlignRight regardless of layout direction.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — RTL alignment menu: labels swap but actions don't (EditorToolbar.qml:362)

### [MENU-N04] Trailing empty MenuSeparator at end of mobile context menu  ·  _SPLIT_  ·  Low
`Prompter.qml:2662`
- **opus:** ✅ LEGIT (50) — trailing empty MenuSeparator at end of context menu (Prompter.qml:2662)
- **gpt:** ⚠️ PARTIAL (58) — observed Trailing empty MenuSeparator at end of mobile context menu (src/prompter/Prompter.qml:2662)
- **deepseek:** ✅ LEGIT (75) — Prompter.qml:2662: trailing MenuSeparator with no items after it creates dangling separator line at bottom of mobile context menu
- **glm:** ✅ LEGIT (70) — Prompter.qml:2662 trailing empty MenuSeparator at end of mobile context menu
- **kimi:** ✅ LEGIT (70) — Prompter.qml:2662 ends contextMenu with a MenuSeparator that has no following items.
- **opus-ultra:** ✅ LEGIT (50) — trailing empty MenuSeparator at end of context menu (Prompter.qml:2662)

### [MENU-N05] "Redo" context menu item missing & accelerator  ·  _SPLIT_  ·  Low
`Prompter.qml:2633`
- **opus:** ⚠️ PARTIAL (45) — Redo menu item missing & accelerator (Prompter.qml:2633)
- **gpt:** ⚠️ PARTIAL (58) — observed "Redo" context menu item missing & accelerator (src/prompter/Prompter.qml:2633)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:2633: 'Redo' text lacks & accelerator prefix; all other menu items (&Undo line 2628 &Copy line 2639) have it — keyboard cycling skips Redo
- **glm:** ✅ LEGIT (70) — Prompter.qml:2633 'Redo' context menu item missing & accelerator
- **kimi:** ✅ LEGIT (70) — Prompter.qml:2633 Redo menu item text lacks & accelerator while all others have one.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — Redo menu item missing & accelerator (Prompter.qml:2633)

### [MENU-N06] Paste behavior inconsistent between context menu and global Edit menu  ·  _SPLIT_  ·  Low
`Prompter.qml:2564,2651 vs main.qml:686`
- **opus:** ⚠️ PARTIAL (50) — paste inconsistent: context menu vs Edit menu (Prompter.qml:2564)
- **gpt:** ⚠️ PARTIAL (58) — observed Paste behavior inconsistent between context menu and global Edit menu (src/prompter/Prompter.qml:2564)
- **deepseek:** ⚠️ PARTIAL (70) — Prompter.qml vs main.qml:686: context menu Paste claimed to filter HTML while Edit menu Paste uses raw editor.paste(); not fully verified at main.qml:686
- **glm:** ⚠️ PARTIAL (60) — Prompter.qml:2564 2651 vs main.qml:686 paste behavior inconsistent between context menu and global Edit menu
- **kimi:** ✅ LEGIT (85) — Prompter.qml:2651 context paste calls document.paste() filtered; main.qml:686 Edit menu calls editor.paste() unfiltered.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — paste inconsistent: context menu vs Edit menu (Prompter.qml:2564)

### [META-N01] QMetaObject::invokeMethod return value unchecked — silent failure on WASM  ·  _SPLIT_  ·  Low
`wasmintegration.cpp:71`
- **opus:** ⚠️ PARTIAL (45) — invokeMethod return unchecked (wasmintegration.cpp:71)
- **gpt:** ⚠️ PARTIAL (58) — observed QMetaObject::invokeMethod return value unchecked - silent failure on WASM (src/wasmintegration.cpp:71)
- **deepseek:** ✅ LEGIT (95) — wasmintegration.cpp:71: QMetaObject::invokeMethod returns bool — discarded; if QML function renamed/removed background image upload silently breaks on WASM
- **glm:** ✅ LEGIT (70) — wasmintegration.cpp:71 QMetaObject::invokeMethod return value unchecked; silent failure on WASM
- **kimi:** ✅ LEGIT (75) — wasmintegration.cpp:71-73 QMetaObject::invokeMethod return value is unchecked; silent failure possible.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — invokeMethod return unchecked (wasmintegration.cpp:71)

### [META-N14] ModernToolkit removed from AppStream spec — validation error  ·  _SPLIT_  ·  Medium
`appdata.xml:66`
- **opus:** ❔ UNSURE (45) — ModernToolkit removed from AppStream spec; needs validator (appdata.xml:66)
- **gpt:** ⚠️ PARTIAL (58) — observed ModernToolkit removed from AppStream spec - validation error (com.cuperino.qprompt.appdata.xml:66)
- **deepseek:** ✅ LEGIT (80) — appdata.xml:66 uses ModernToolkit kudo; ModernToolkit removed from AppStream spec checklist in recent versions; validator may reject
- **glm:** ⚠️ PARTIAL (60) — appdata.xml:66 ModernToolkit removed from AppStream spec; may cause validation warning
- **kimi:** ❔ UNSURE (60) — appdata.xml:66 uses <kudo>ModernToolkit</kudo>; its current AppStream validity cannot be confirmed from source alone
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — ModernToolkit removed from AppStream spec; needs validator (appdata.xml:66)

### [META-N15] No StartupWMClass in desktop file — duplicate dock entries, missing icon  ·  _SPLIT_  ·  Medium
`com.cuperino.qprompt.desktop`
- **opus:** ⚠️ PARTIAL (45) — no StartupWMClass in desktop file
- **gpt:** ⚠️ PARTIAL (58) — observed No StartupWMClass in desktop file - duplicate dock entries, missing icon (com.cuperino.qprompt.desktop:1)
- **deepseek:** ✅ LEGIT (90) — com.cuperino.qprompt.desktop (both copies): no StartupWMClass entry; causes duplicate dock entries and missing icon on Linux
- **glm:** ✅ LEGIT (70) — com.cuperino.qprompt.desktop no StartupWMClass; duplicate dock entries missing icon
- **kimi:** ✅ LEGIT (80) — com.cuperino.qprompt.desktop has no StartupWMClass; duplicate dock entries / missing icon can occur
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — no StartupWMClass in desktop file

### [META-N16] README badges and links reference wrong repo Cuperino/QPrompt (should be QPrompt-Teleprompter)  ·  _SPLIT_  ·  Low
`README.md`
- **opus:** ❔ UNSURE (45) — README repo URL Cuperino/QPrompt; needs repo check
- **gpt:** ❔ UNSURE (39) — repo rename claim needs external project history, not code (README.md:1)
- **deepseek:** ✅ LEGIT (90) — README.md:1-6: badges reference Cuperino/QPrompt not QPrompt-Teleprompter; line 18 BUILD.md link points to Cuperino/QPrompt
- **glm:** ⚠️ PARTIAL (60) — README.md badges and links reference Cuperino/QPrompt instead of QPrompt-Teleprompter; may be intentional fork
- **kimi:** ✅ LEGIT (95) — README.md badges and links point to Cuperino/QPrompt, not this QPrompt-Teleprompter repo
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — README repo URL Cuperino/QPrompt; needs repo check

### [META-N17] README links to non-existent BUILD.md  ·  _SPLIT_  ·  Medium
`README.md:18`
- **opus:** ❔ UNSURE (45) — README links to BUILD.md; needs file check
- **gpt:** ❔ UNSURE (39) — README link target needs packaging/release context (README.md:18)
- **deepseek:** ✅ LEGIT (85) — README.md:18 links to BUILD.md at Cuperino/QPrompt/blob/main/BUILD.md; file likely nonexistent after repo rename
- **glm:** ✅ LEGIT (70) — README.md:18 links to non-existent BUILD.md
- **kimi:** ✅ LEGIT (95) — README.md:18 links to Cuperino/QPrompt/blob/main/BUILD.md; that file does not exist in this repo
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — README links to BUILD.md; needs file check

### [MIME-N01] Temporary QMimeDatabase — QMimeType dangling on Qt 5 (undefined behavior)  ·  _SPLIT_  ·  High
`documenthandler.cpp:945`
- **opus:** ⚠️ PARTIAL (45) — temp QMimeDatabase; QMimeType-dangling is Qt5-only, target is Qt6 (documenthandler.cpp:945)
- **gpt:** ⚠️ PARTIAL (58) — observed Temporary QMimeDatabase - QMimeType dangling on Qt 5 (undefined behavior) (src/documenthandler.cpp:945)
- **deepseek:** ❌ FALSE (95) — QT_MIN_VERSION=6.8.2 per CMakeLists.txt:57; Qt 5 not supported. QMimeType independent of QMimeDatabase in Qt 6
- **glm:** ⚠️ PARTIAL (60) — documenthandler.cpp:945 QMimeDatabase on stack; QMimeType dangling only on Qt 5 not Qt 6
- **kimi:** ❌ FALSE (75) — documenthandler.cpp:945 QMimeType is implicitly shared and valid after the temporary QMimeDatabase is destroyed
- **opus-ultra:** ❌ FALSE (72) — max: code correct / claim mischaracterized — temp QMimeDatabase; QMimeType-dangling is Qt5-only

### [MIX-01] spellchecker.cpp:98 size_t→int narrowing in languages() reserve  ·  _SPLIT_  ·  Low
`spellchecker.cpp:98`
- **opus:** ⚠️ PARTIAL (40) — size_t->int narrowing in languages() reserve (spellchecker.cpp:98)
- **gpt:** ✅ LEGIT (78) — spellchecker.cpp:98 size_t->int narrowing in languages() reserve (src/spellchecker.cpp:98)
- **deepseek:** ✅ LEGIT (90) — static_cast<int>(m_dicts.size()) at spellchecker.cpp:98 — size_t to int narrowing
- **glm:** ✅ LEGIT (75) — spellchecker.cpp:98 size_t to int narrowing in languages() reserve
- **kimi:** ✅ LEGIT (70) — spellchecker.cpp:98 narrows size_t to int via static_cast for reserve; potential overflow/correctness issue.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — size_t->int narrowing in languages() reserve (spellchecker.cpp:98)

### [MOB-02] No +ios/ QML selector — iOS inherits base main.qml with desktop-only components  ·  _SPLIT_  ·  Medium
`Missing +ios/main.qml`
- **opus:** ⚠️ PARTIAL (50) — no +ios selector; iOS inherits base with desktop-only bits (main.qml)
- **gpt:** ✅ LEGIT (78) — No +ios/ QML selector - iOS inherits base main.qml with desktop-only components (src/kirigami_ui/main.qml:1)
- **deepseek:** ✅ LEGIT (95) — No +ios/main.qml exists; iOS inherits base main.qml with ProjectionsManager (QWindow) onFrameSwapped grabToImage and desktop-only components
- **glm:** ✅ LEGIT (80) — No +ios/ QML selector directory; iOS inherits base main.qml with desktop-only components
- **kimi:** ✅ LEGIT (80) — No +ios/main.qml exists; iOS loads base main.qml with desktop-only ProjectionsManager, Labs.MenuBar and per-frame grabToImage.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — no +ios selector; iOS inherits base with desktop-only bits (main.qml)

### [MOB-03] iOS: IosSaveDialog silently hangs QML caller when temp dir invalid  ·  _SPLIT_  ·  Medium
`iossavedialog.mm:79-81`
- **opus:** ⚠️ PARTIAL (50) — iOS save hangs QML caller when temp dir invalid (iossavedialog.mm:79)
- **gpt:** ✅ LEGIT (92) — iOS: IosSaveDialog silently hangs QML caller when temp dir invalid (src/iossavedialog.mm:79)
- **deepseek:** ✅ LEGIT (95) — iossavedialog.mm:79-81: early return on !m_tempDir.isValid() without emitting rejected() or accepted(); QML caller hangs waiting for signal
- **glm:** ✅ LEGIT (75) — iossavedialog.mm:79-81 IosSaveDialog silently hangs QML caller when temp dir invalid
- **kimi:** ✅ LEGIT (85) — iossavedialog.mm:79-81 returns silently when temp dir is invalid without emitting rejected(), hanging QML save flow.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — iOS save hangs QML caller when temp dir invalid (iossavedialog.mm:79)

### [MODEL-N02] SessionModel::clearDataPoints lacks empty-model guard before beginRemoveRows  ·  _SPLIT_  ·  Low
`promptsession.cpp:79-84`
- **opus:** ✅ LEGIT (55) — clearDataPoints no empty guard before beginRemoveRows; dead code (promptsession.cpp:79)
- **gpt:** ⚠️ PARTIAL (58) — observed SessionModel::clearDataPoints lacks empty-model guard before beginRemoveRows (src/promptsession.cpp:79)
- **deepseek:** ✅ LEGIT (85) — promptsession.cpp:79-84: clearDataPoints calls beginRemoveRows(0 rowCount()) without empty-model guard; signals removal from empty model
- **glm:** ✅ LEGIT (70) — promptsession.cpp:79-84 clearDataPoints lacks empty-model guard before beginRemoveRows
- **kimi:** ✅ LEGIT (85) — promptsession.cpp:79-84 clearDataPoints calls beginRemoveRows(0,rowCount()) even when rowCount()=0; contract violation.
- **opus-ultra:** ✅ LEGIT (55) — clearDataPoints no empty guard before beginRemoveRows; dead code (promptsession.cpp:79)

### [NET-N06] loadFromNetwork() validates original URL, not constructed resultingUrl  ·  _SPLIT_  ·  Low
`documenthandler.cpp:881`
- **opus:** ✅ LEGIT (65) — if(url.isValid()) validates original url not resultingUrl (documenthandler.cpp:881)
- **gpt:** ⚠️ PARTIAL (58) — observed loadFromNetwork() validates original URL, not constructed resultingUrl (src/documenthandler.cpp:881)
- **deepseek:** ✅ LEGIT (85) — url.isValid() at documenthandler.cpp:881 checks input URL not constructed resultingUrl — masked construction errors
- **glm:** ✅ LEGIT (80) — documenthandler.cpp:881 loadFromNetwork validates original url not constructed resultingUrl
- **kimi:** ✅ LEGIT (95) — documenthandler.cpp:881 tests url.isValid() (the original argument) instead of resultingUrl.isValid() after URL construction
- **opus-ultra:** ✅ LEGIT (65) — if(url.isValid()) validates original url not resultingUrl (documenthandler.cpp:881)

### [NOTIFY-02] availableDictionariesChanged NOTIFY signal never emitted  ·  _SPLIT_  ·  Low
`documenthandler.h:137,318`
- **opus:** ✅ LEGIT (55) — availableDictionariesChanged NOTIFY never emitted (documenthandler.h:137)
- **gpt:** ✅ LEGIT (78) — availableDictionariesChanged NOTIFY signal never emitted (src/documenthandler.h:137)
- **deepseek:** ⚠️ PARTIAL (85) — availableDictionariesChanged at documenthandler.h:137 never emitted; but method is static disk-scan can't change
- **glm:** ✅ LEGIT (80) — documenthandler.h:137 318 availableDictionariesChanged signal never emitted
- **kimi:** ✅ LEGIT (85) — documenthandler.h:137 declares availableDictionariesChanged but no code emits it; list is static.
- **opus-ultra:** ✅ LEGIT (55) — availableDictionariesChanged NOTIFY never emitted (documenthandler.h:137)

### [OOB-N01] MarkersModel::data() — m_data.at() without row < rowCount() guard  ·  _SPLIT_  ·  Medium
`markersmodel.cpp:40-43`
- **opus:** ⚠️ PARTIAL (50) — data() m_data.at() relies on isValid() not rowCount bound (markersmodel.cpp:40)
- **gpt:** ✅ LEGIT (78) — MarkersModel::data() - mdata.at() without row rowCount() guard (src/markersmodel.cpp:40)
- **deepseek:** ✅ LEGIT (90) — m_data.at(row) at markersmodel.cpp:43 — isValid() doesn't enforce row<rowCount()
- **glm:** ✅ LEGIT (80) — markersmodel.cpp:40-43 m_data.at(index.row()) without row < rowCount() bounds guard
- **kimi:** ✅ LEGIT (90) — markersmodel.cpp:40-43 only checks index.isValid() before m_data.at(index.row()); missing row<rowCount guard.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — data() m_data.at() relies on isValid() not rowCount bound (markersmodel.cpp:40)

### [OOB-N02] SessionModel::data() — same missing row bounds guard  ·  _SPLIT_  ·  Medium
`promptsession.cpp:40-43`
- **opus:** ⚠️ PARTIAL (45) — SessionModel::data missing bounds guard; dead code (promptsession.cpp:40)
- **gpt:** ✅ LEGIT (78) — SessionModel::data() - same missing row bounds guard (src/promptsession.cpp:40)
- **deepseek:** ✅ LEGIT (90) — m_data.at(row) at promptsession.cpp:43 — same missing rowCount guard as OOB-N01
- **glm:** ✅ LEGIT (80) — promptsession.cpp:40-43 m_data.at(index.row()) without row bounds guard
- **kimi:** ✅ LEGIT (85) — promptsession.cpp:40-43 has the same missing row-bound guard as OOB-N01 (though the file is dead code).
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — SessionModel::data missing bounds guard; dead code (promptsession.cpp:40)

### [OPC-01] Right-click toggle desynchronizes velocityIndicator visible/opacity  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:906,979-980`
- **opus:** ⚠️ PARTIAL (50) — right-click toggle desyncs indicator visible/opacity (PrompterPage.qml:906)
- **gpt:** ✅ LEGIT (78) — Right-click toggle desynchronizes velocityIndicator visible/opacity (src/kirigami_ui/PrompterPage.qml:906)
- **deepseek:** ✅ LEGIT (90) — Only opacity toggled at PrompterPage.qml:906; visible stays true — breaks middle-click reactivation
- **glm:** ✅ LEGIT (80) — PrompterPage.qml:906 979-980 right-click toggle desynchronizes velocityIndicator visible/opacity
- **kimi:** ✅ LEGIT (85) — PrompterPage.qml:906 right-click only flips velocityIndicator.opacity; visible stays true so velocityDragOverlay keeps capturing input.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — right-click toggle desyncs indicator visible/opacity (PrompterPage.qml:906)

### [ORIENT-N01] TimerClock binary width>height orientation creates sharp 2x font jump at 1:1  ·  _SPLIT_  ·  Low
`TimerClock.qml:127`
- **opus:** ⚠️ PARTIAL (45) — binary width>height -> 2x font jump at 1:1 (TimerClock.qml:127)
- **gpt:** ⚠️ PARTIAL (58) — observed TimerClock binary widthheight orientation creates sharp 2x font jump at 1:1 (src/prompter/TimerClock.qml:127)
- **deepseek:** ✅ LEGIT (60) — binary width>height check creates 2x font size jump at exact square 1:1 aspect (TimerClock.qml:127)
- **glm:** ⚠️ PARTIAL (55) — TimerClock.qml:127 binary width>height orientation creates sharp 2x font jump at 1:1
- **kimi:** ✅ LEGIT (70) — TimerClock.qml:127 uses binary width/height>1 ratio, causing abrupt 2x font jump when window crosses near-square aspect.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — binary width>height -> 2x font jump at 1:1 (TimerClock.qml:127)

### [PARSE-N01] insertImageAt() stores image resource with file:// key but looks up via plain path  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1766-1769`
- **opus:** ⚠️ PARTIAL (50) — image resource keyed by QUrl but format name=path string; possible mismatch (documenthandler.cpp:1766)
- **gpt:** ✅ LEGIT (78) — insertImageAt() stores image resource with file:// key but looks up via plain path (src/documenthandler.cpp:1766)
- **deepseek:** ✅ LEGIT (85) — addResource with file:// QUrl at documenthandler.cpp:1766 but imageFormat.setName uses plain path at 1769
- **glm:** ✅ LEGIT (80) — documenthandler.cpp:1766-1769 insertImageAt stores image resource with file:// key but looks up via plain path
- **kimi:** ✅ LEGIT (95) — documenthandler.cpp:1766-1769 stores local image under file:// key but sets imageFormat.name to toLocalFile(); imageAt/imageRect lookup via QUrl(name) misses
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — image resource keyed by QUrl but format name=path string; possible mismatch (documenthandl

### [PATH-N01] save() fragile percent-encoding round-trip — broken for UNC paths  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1183`
- **opus:** ⚠️ PARTIAL (50) — save() percent-encoding round-trip fragile for UNC (documenthandler.cpp:1183)
- **gpt:** ✅ LEGIT (78) — save() fragile percent-encoding round-trip - broken for UNC paths (src/documenthandler.cpp:1183)
- **deepseek:** ✅ LEGIT (85) — documenthandler.cpp:1183: toPercentEncoding->toStdString->fromStdString->setUrl() round-trip fragile; UNC paths (//server/share) mangled because setUrl interprets leading // as authority
- **glm:** ✅ LEGIT (80) — documenthandler.cpp:1183 save() fragile percent-encoding round-trip; broken for UNC paths
- **kimi:** ✅ LEGIT (80) — documenthandler.cpp:1183 save() round-trips fileName through toPercentEncoding/toStdString/fromStdString/setUrl instead of fromLocalFile.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — save() percent-encoding round-trip fragile for UNC (documenthandler.cpp:1183)

### [PATH-N03] Wrong ../fonts/ depth in +android and +windows FontLoader paths  ·  _SPLIT_  ·  High
`+android/main.qml:465, +windows/main.qml:531`
- **opus:** ❔ UNSURE (45) — FontLoader ../fonts depth in +android/+windows; needs path trace (main.qml:465)
- **gpt:** ✅ LEGIT (84) — Wrong ../fonts/ depth in +android and +windows FontLoader paths (src/kirigami_ui/+android/main.qml:465)
- **deepseek:** ✅ LEGIT (90) — +android/main.qml:465 / +windows/main.qml:531: FontLoader source '../fonts/...' one level too shallow; files in qrc at different depth than base main.qml — font fails to load
- **glm:** ✅ LEGIT (75) — +android/main.qml:465 +windows/main.qml:531 wrong ../fonts/ depth in FontLoader paths
- **kimi:** ⚠️ PARTIAL (65) — +android/+windows main.qml use '../fonts' like base main.qml:560; fonts prefix is /qt/qml/com/cuperino/qprompt/ so the relative path is wrong for all variants, not only Android/Windows.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — FontLoader ../fonts depth in +android/+windows; needs path trace (main.qml:465)

### [PC-01] countdown.state not set in Prompting state — countdown visible during teleprompting  ·  _SPLIT_  ·  Medium
`Prompter.qml:3027-3086`
- **opus:** ❔ UNSURE (45) — countdown.state not set in Prompting; visibility claim; domain (Prompter.qml:3027)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Prompter.qml:3027)
- **deepseek:** ✅ LEGIT (70) — Prompting state (Prompter.qml:3027) has no countdown.state PropertyChanges — countdown may stay visible
- **glm:** ⚠️ PARTIAL (65) — Prompter.qml:3027-3086 countdown.state not set in Prompting state; countdown may be visible during teleprompting
- **kimi:** ✅ LEGIT (90) — Prompter.qml:3027-3086 Prompting state has no PropertyChanges target: countdown, so countdown stays in visible state.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — countdown.state not set in Prompting; visibility claim; domain (Prompter.qml:3027)

### [PERF-N01] onFrameSwapped calls markerCompare() unconditionally — wasted JS call every frame  ·  _SPLIT_  ·  Medium
`main.qml:1038`
- **opus:** ⚠️ PARTIAL (50) — markerCompare() every onFrameSwapped; by-design per comment (main.qml:1038)
- **gpt:** ⚠️ PARTIAL (58) — observed onFrameSwapped calls markerCompare() unconditionally - wasted JS call every frame (src/kirigami_ui/main.qml:1038)
- **deepseek:** ✅ LEGIT (90) — main.qml:1038: markerCompare() called every display frame (60-144Hz) even when not prompting; internal guard returns immediately but JS call overhead wasted — should hoist state check
- **glm:** ✅ LEGIT (75) — main.qml:1038 onFrameSwapped calls markerCompare() unconditionally; wasted JS call every frame
- **kimi:** ✅ LEGIT (75) — main.qml:1038 calls root.pageStack.currentItem.prompter.markerCompare() unconditionally every onFrameSwapped.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — markerCompare() every onFrameSwapped; by-design per comment (main.qml:1038)

### [PERF-N02] RecentDocuments._load() blocks startup with N synchronous createObject() calls  ·  _SPLIT_  ·  Medium
`RecentDocuments.qml:221,82-107`
- **opus:** ⚠️ PARTIAL (50) — _load blocks startup with N sync createObject (RecentDocuments.qml:221)
- **gpt:** ⚠️ PARTIAL (58) — observed RecentDocuments.load() blocks startup with N synchronous createObject() calls (src/kirigami_ui/RecentDocuments.qml:221)
- **deepseek:** ✅ LEGIT (90) — RecentDocuments.qml:221/82-107: _load() triggers _rebuildChildren() on Component.onCompleted; creates up to 30 Kirigami.Action synchronously on main thread — startup delay
- **glm:** ✅ LEGIT (75) — RecentDocuments.qml:221 82-107 _load() blocks startup with N synchronous createObject() calls
- **kimi:** ✅ LEGIT (80) — RecentDocuments.qml:221 _load() synchronously creates up to maxEntries Kirigami.Action objects during startup.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — _load blocks startup with N sync createObject (RecentDocuments.qml:221)

### [PERF-N03] velocityDragOverlay hot-loop calls velocity functions without throttling  ·  _SPLIT_  ·  Low
`PrompterPage.qml:939-976`
- **opus:** ⚠️ PARTIAL (50) — velocityDragOverlay calls velocity fns without throttle (PrompterPage.qml:939)
- **gpt:** ⚠️ PARTIAL (58) — observed velocityDragOverlay hot-loop calls velocity functions without throttling (src/kirigami_ui/PrompterPage.qml:939)
- **deepseek:** ✅ LEGIT (85) — PrompterPage.qml:939-976: onPositionChanged for-loop calls increaseVelocity/decreaseVelocity N=floor(deltaY/20) times per mouse event; dozens of full binding cascade+navigation per event
- **glm:** ⚠️ PARTIAL (60) — PrompterPage.qml:939-976 velocityDragOverlay hot-loop calls velocity functions without throttling
- **kimi:** ✅ LEGIT (75) — PrompterPage.qml:939-976 velocity drag loop calls increase/decreaseVelocity once per 20px with no throttling.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — velocityDragOverlay calls velocity fns without throttle (PrompterPage.qml:939)

### [PLAT-01] KF6Crash_FOUND never defined as C preprocessor macro — KCrash support dead code  ·  _SPLIT_  ·  High
`src/main.cpp:50, CMakeLists.txt:316`
- **opus:** ✅ LEGIT (90) — KF6Crash_FOUND never -D; KF6::Crash never linked (main.cpp:50)
- **gpt:** ⚠️ PARTIAL (58) — observed KF6Crash_FOUND never defined as C preprocessor macro - KCrash support dead code (src/main.cpp:50)
- **deepseek:** ✅ LEGIT (90) — KF6Crash_FOUND at main.cpp:50 checked via #if defined but CMake never adds compile definition; KCrash code dead; confirmed at CMakeLists.txt:316 — find_package sets CMake var not C++ macro
- **glm:** ⚠️ PARTIAL (65) — main.cpp:50 uses KF6Crash_FOUND but CMakeLists.txt:316 uses find_package without add_compile_definitions; KCrash block dead
- **kimi:** ✅ LEGIT (90) — main.cpp:50 #if defined(KF6Crash_FOUND) never true; CMakeLists.txt:316 find_package sets CMake var not compile definition.
- **opus-ultra:** ✅ LEGIT (90) — KF6Crash_FOUND never -D; KF6::Crash never linked (main.cpp:50)

### [PLAT-03] Wrong target name and wrong include path for KDMacTouchBar  ·  _SPLIT_  ·  High
`src/CMakeLists.txt:491,492`
- **opus:** ✅ LEGIT (85) — mactouchbar wrong target; 493 uses KDMacTouchBar (src/CMakeLists.txt:491)
- **gpt:** ✅ LEGIT (84) — Wrong target name and wrong include path for KDMacTouchBar (src/CMakeLists.txt:491)
- **deepseek:** ❔ UNSURE (50) — KDMacTouchBar target name wrong at src/CMakeLists.txt:491-492; need to verify actual target name from 3rdparty/KDMacTouchBar/CMakeLists.txt
- **glm:** ✅ LEGIT (85) — src/CMakeLists.txt:491 target_include_directories(mactouchbar) wrong target name; should be ${PROJECT_NAME}. Line 492 wrong include path
- **kimi:** ✅ LEGIT (90) — src/CMakeLists.txt:491,492 uses target mactouchbar (does not exist) and doubled include path; should be KDMacTouchBar.
- **opus-ultra:** ✅ LEGIT (85) — mactouchbar wrong target; 493 uses KDMacTouchBar (src/CMakeLists.txt:491)

### [PLAT-08] QNX platform guard inconsistency: main.cpp vs documenthandler.h  ·  _SPLIT_  ·  Medium
`src/main.cpp:23, src/documenthandler.h:82`
- **opus:** ⚠️ PARTIAL (50) — documenthandler.h:82 guard omits QNX vs main.cpp:23; exotic target (main.cpp:23)
- **gpt:** ⚠️ PARTIAL (58) — observed QNX platform guard inconsistency: main.cpp vs documenthandler.h (src/main.cpp:23)
- **deepseek:** ✅ LEGIT (85) — documenthandler.h:82 omits Q_OS_QNX from guard but main.cpp:23 and doc.cpp:85 include it; QNX build would fail on missing QDialog symbols
- **glm:** ⚠️ PARTIAL (55) — main.cpp:23 includes QNX in platform guard; documenthandler.h:82 excludes QNX from some guards; inconsistency is intentional for QApplication vs QGuiApplication
- **kimi:** ✅ LEGIT (85) — main.cpp:23,42 include Q_OS_QNX in mobile/WASM guard; documenthandler.h:82 omits QNX causing build failure.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — documenthandler.h:82 guard omits QNX vs main.cpp:23; exotic target (main.cpp:23)

### [PLAT-09] Pre-build manifest references invalid Android SDK paths  ·  _SPLIT_  ·  Low
`.env.android`
- **opus:** ❔ UNSURE (45) — .env.android stale SDK paths; environment-specific
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (.env.android:6)
- **deepseek:** ❔ UNSURE (30) — .env.android path claims not verifiable from source code; environment-specific local paths
- **glm:** ✅ LEGIT (80) — .env.android:6 references Qt 5.15.2 but CMakeLists.txt:57 requires Qt 6.8.2; outdated build environment file
- **kimi:** ✅ LEGIT (75) — .env.android references Qt 5.15.2 and outdated Android SDK/NDK paths incompatible with Qt 6.8.2 target.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — .env.android stale SDK paths; environment-specific

### [PLAT-N05] Base main.qml fullScreenPlatform missing "wasm" (inconsistent with +windows)  ·  _SPLIT_  ·  Low
`main.qml:45`
- **opus:** ⚠️ PARTIAL (45) — fullScreenPlatform missing 'wasm' vs +windows (main.qml:45)
- **gpt:** ⚠️ PARTIAL (58) — observed Base main.qml fullScreenPlatform missing "wasm" (inconsistent with +windows) (src/kirigami_ui/main.qml:45)
- **deepseek:** ✅ LEGIT (85) — 'main.qml:45 fullScreenPlatform array lacks "wasm"; +windows variant includes it; wasm shows own fullscreen button alongside browser''s'
- **glm:** ✅ LEGIT (70) — main.qml:45 fullScreenPlatform missing 'wasm' in list; inconsistent with +windows variant
- **kimi:** ✅ LEGIT (75) — main.qml:45 fullScreenPlatform omits 'wasm' while +windows:40 includes it; inconsistent but only base matters for WASM so app's own toggle is shown.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — fullScreenPlatform missing 'wasm' vs +windows (main.qml:45)

### [POP-N01] ESC cascade missing dictionariesSheet — undismissable by keyboard  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:1512, all 3 main.qml ESC handlers`
- **opus:** ⚠️ PARTIAL (50) — ESC cascade omits dictionariesSheet (PrompterPage.qml:1512)
- **gpt:** ⚠️ PARTIAL (58) — observed ESC cascade missing dictionariesSheet - undismissable by keyboard (src/kirigami_ui/PrompterPage.qml:1512)
- **deepseek:** ✅ LEGIT (90) — ESC handler at main.qml:476-518 checks 9 sheets but omits dictionariesSheet (PrompterPage.qml:1512); no alias no ESC chain entry
- **glm:** ✅ LEGIT (75) — PrompterPage.qml:1512 dictionariesSheet not in ESC cascade; undismissable by keyboard
- **kimi:** ✅ LEGIT (90) — ESC cascade in main.qml variants omits dictionariesSheet defined at PrompterPage.qml:1512.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — ESC cascade omits dictionariesSheet (PrompterPage.qml:1512)

### [POP-N02] ESC cascade missing customWordsSheet — undismissable by keyboard  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:1589, all 3 main.qml ESC handlers`
- **opus:** ⚠️ PARTIAL (50) — ESC cascade omits customWordsSheet (PrompterPage.qml:1589)
- **gpt:** ⚠️ PARTIAL (58) — observed ESC cascade missing customWordsSheet - undismissable by keyboard (src/kirigami_ui/PrompterPage.qml:1589)
- **deepseek:** ✅ LEGIT (90) — ESC handler at main.qml:476-518 omits customWordsSheet (PrompterPage.qml:1589); identical to POP-N01
- **glm:** ✅ LEGIT (75) — PrompterPage.qml:1589 customWordsSheet not in ESC cascade; undismissable by keyboard
- **kimi:** ✅ LEGIT (90) — ESC cascade in main.qml variants omits customWordsSheet defined at PrompterPage.qml:1589.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — ESC cascade omits customWordsSheet (PrompterPage.qml:1589)

### [POP-N03] ESC cascade missing obsConfiguration — undismissable by keyboard despite alias  ·  _SPLIT_  ·  Medium
`All 3 main.qml ESC handlers`
- **opus:** ⚠️ PARTIAL (50) — ESC cascade omits obsConfiguration sheet (main.qml)
- **gpt:** ⚠️ PARTIAL (58) — observed ESC cascade missing obsConfiguration - undismissable by keyboard despite alias (src/kirigami_ui/main.qml:481)
- **deepseek:** ✅ LEGIT (85) — obsConfiguration IS aliased at PrompterPage.qml:53 but ESC handler main.qml:489-504 never checks obsConfiguration.opened
- **glm:** ✅ LEGIT (75) — obsConfiguration not in ESC cascade despite alias; undismissable by keyboard
- **kimi:** ✅ LEGIT (90) — ESC cascade in main.qml variants omits obsConfiguration alias/id at PrompterPage.qml:53/1447.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — ESC cascade omits obsConfiguration sheet (main.qml)

### [POP-N04] CountdownConfiguration SpinBoxes use focus: true (JS label) instead of focus = true  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:1092,1114`
- **opus:** ✅ LEGIT (65) — CountdownConfiguration SpinBox focus: true is a JS label not assignment (PrompterPage.qml:1092)
- **gpt:** ⚠️ PARTIAL (58) — observed CountdownConfiguration SpinBoxes use focus: true (JS label) instead of focus = true (src/kirigami_ui/PrompterPage.qml:1092)
- **deepseek:** ✅ LEGIT (95) — PrompterPage.qml:1092 1114: 'focus: true' inside onValueModified is a JS label not assignment; correct would be 'focus = true'
- **glm:** ✅ LEGIT (75) — PrompterPage.qml:1092 1114 CountdownConfiguration SpinBoxes use focus: true (JS label) instead of focus=true
- **kimi:** ✅ LEGIT (90) — PrompterPage.qml:1092,1114 use `focus: true` inside onValueModified — JS label, not assignment; spinbox never gains focus.
- **opus-ultra:** ✅ LEGIT (65) — CountdownConfiguration SpinBox focus: true is a JS label not assignment (PrompterPage.qml:1092)

### [PP-N01] Q_OS_APPLE is not a Qt macro — KGlobalAccel block compiles on all Unix including macOS  ·  _SPLIT_  ·  Medium
`globalhotkeys.cpp:26`
- **opus:** ✅ LEGIT (55) — Q_OS_APPLE not a Qt macro; should be Q_OS_DARWIN/defined check (globalhotkeys.cpp:26)
- **gpt:** ⚠️ PARTIAL (58) — observed Q_OS_APPLE is not a Qt macro - KGlobalAccel block compiles on all Unix including macOS (src/globalhotkeys.cpp:26)
- **deepseek:** ✅ LEGIT (95) — globalhotkeys.cpp:26: Q_OS_APPLE not defined by Qt (correct macro: Q_OS_DARWIN); !defined always true; KGlobalAccel compiles on all Unix
- **glm:** ✅ LEGIT (75) — globalhotkeys.cpp:26 Q_OS_APPLE is not a Qt macro; KGlobalAccel block compiles on all Unix including macOS
- **kimi:** ✅ LEGIT (95) — globalhotkeys.cpp:26 uses !defined(Q_OS_APPLE); Q_OS_APPLE is not a Qt macro so the guard is always true
- **opus-ultra:** ✅ LEGIT (55) — Q_OS_APPLE not a Qt macro; should be Q_OS_DARWIN/defined check (globalhotkeys.cpp:26)

### [PROP-N02] setCursorPosition → reset() — 12-signal storm, no debounce  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:455-463,1187-1201`
- **opus:** ⚠️ PARTIAL (55) — setCursorPosition->reset() emits ~12 signals per move; by-design, no debounce (documenthandler.cpp:461)
- **gpt:** ⚠️ PARTIAL (58) — observed setCursorPosition -> reset() - 12-signal storm, no debounce (src/documenthandler.cpp:455)
- **deepseek:** ✅ LEGIT (85) — setCursorPosition->reset() at documenthandler.cpp:461 emits 12 signals no debounce — 720 emissions/sec on scroll
- **glm:** ✅ LEGIT (80) — documenthandler.cpp:455-463 1187-1201 setCursorPosition→reset() emits 12 NOTIFY signals; no debounce
- **kimi:** ✅ LEGIT (95) — documenthandler.cpp:455-463 setCursorPosition unconditionally calls reset(); reset() at :1187-1201 emits 12 property-changed signals with no debounce
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — setCursorPosition->reset() emits ~12 signals per move; by-design

### [PROP-N03] setMarker/setKeyMarker/setMarkerHref silently trigger full document reparse  ·  _SPLIT_  ·  Low
`documenthandler.cpp:720,775,804`
- **opus:** ⚠️ PARTIAL (45) — marker setters dirty the list -> reparse on next nav; by-design (documenthandler.cpp:720)
- **gpt:** ⚠️ PARTIAL (58) — observed setMarker/setKeyMarker/setMarkerHref silently trigger full document reparse (src/documenthandler.cpp:720)
- **deepseek:** ✅ LEGIT (85) — setMarker/setKeyMarker/setMarkerHref at documenthandler.cpp:720 775 804 all trigger full parse() via setMarkersListDirty
- **glm:** ⚠️ PARTIAL (60) — documenthandler.cpp:720 775 804 setMarker/setKeyMarker/setMarkerHref trigger full document reparse via setMarkersListDirty
- **kimi:** ✅ LEGIT (90) — setKeyMarker (:720), setMarkerHref (:775), and setMarker (:804) call setMarkersListDirty(), forcing O(n) parse() on next marker navigation
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — marker setters dirty the list -> reparse on next nav; by-design (documenthandler.cpp:720)

### [QF-N02] QDir::entryList missing QDir::Readable in availableDictionaries()  ·  _SPLIT_  ·  Low
`spellchecker.cpp:254`
- **opus:** ⚠️ PARTIAL (45) — entryList missing QDir::Readable filter (spellchecker.cpp:254)
- **gpt:** ⚠️ PARTIAL (58) — observed QDir::entryList missing QDir::Readable in availableDictionaries() (src/spellchecker.cpp:254)
- **deepseek:** ✅ LEGIT (85) — spellchecker.cpp:254: QDir::entryList uses QDir::Files without QDir::Readable; unreadable .dic files pollute available list causing Hunspell open failure with only qWarning
- **glm:** ✅ LEGIT (70) — spellchecker.cpp:254 QDir::entryList missing QDir::Readable in availableDictionaries filters
- **kimi:** ✅ LEGIT (70) — spellchecker.cpp:254 entryList uses QDir::Files without QDir::Readable, listing dictionaries that may be unreadable.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — entryList missing QDir::Readable filter (spellchecker.cpp:254)

### [QF-N03] TOCTOU: QFile::exists() → QFile::copy() in resource cache extraction  ·  _SPLIT_  ·  Low
`spellchecker.cpp:198-199`
- **opus:** ⚠️ PARTIAL (50) — TOCTOU exists()->copy() in cache extraction (spellchecker.cpp:198)
- **gpt:** ⚠️ PARTIAL (58) — observed TOCTOU: QFile::exists() -> QFile::copy() in resource cache extraction (src/spellchecker.cpp:198)
- **deepseek:** ✅ LEGIT (90) — spellchecker.cpp:198-199: QFile::exists() then QFile::copy() — TOCTOU race; another process creating outPath between check and copy silently corrupts dictionary cache
- **glm:** ✅ LEGIT (75) — spellchecker.cpp:198-199 TOCTOU: QFile::exists() then QFile::copy() in resource cache extraction
- **kimi:** ✅ LEGIT (75) — spellchecker.cpp:198-199 checks QFile::exists then calls QFile::copy without checking return value or using atomic write.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — TOCTOU exists()->copy() in cache extraction (spellchecker.cpp:198)

### [QLOAD-N01] InputsOverlay toggleButtonsOff() null-check bypass — crash on slow async Loaders  ·  _SPLIT_  ·  Medium
`InputsOverlay.qml:107,564`
- **opus:** ⚠️ PARTIAL (50) — toggleButtonsOff null-check bypass on slow async Loader (InputsOverlay.qml:107)
- **gpt:** ✅ LEGIT (78) — InputsOverlay toggleButtonsOff() null-check bypass - crash on slow async Loaders (src/kirigami_ui/InputsOverlay.qml:107)
- **deepseek:** ✅ LEGIT (95) — InputsOverlay.qml:107 564: typeof null==='object' bypasses guard; null.checked=false throws TypeError on slow async Loader completion
- **glm:** ✅ LEGIT (75) — InputsOverlay.qml:107 564 toggleButtonsOff() null-check bypass; crash on slow async Loaders
- **kimi:** ✅ LEGIT (85) — InputsOverlay.qml:107,564 guard `typeof children[i].item !== 'undefined'` passes for null; null.checked TypeError.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — toggleButtonsOff null-check bypass on slow async Loader (InputsOverlay.qml:107)

### [QML-07] `Text.CurveRendering` enum requires Qt >= 6.7  ·  _SPLIT_  ·  High
`src/prompter/Countdown.qml:196`
- **opus:** ❌ FALSE (95) — CurveRendering exists on Qt 6.8.2 target (CMakeLists.txt:57)
- **gpt:** ❌ FALSE (90) — Qt target is 6.8.2, so CurveRendering is available (src/prompter/Countdown.qml:196)
- **deepseek:** ❌ FALSE (85) — QT_MIN_VERSION=6.8.2 at CMakeLists.txt:57; CurveRendering added in Qt 6.7; project can use it; QML import QtCore 6.5 is minimum version not exact
- **glm:** ⚠️ PARTIAL (60) — Countdown.qml:196 Text.CurveRendering requires Qt 6.7+ but CMakeLists.txt:57 targets Qt 6.8.2 so this is fine
- **kimi:** ❌ FALSE (85) — CMakeLists.txt:57 sets QT_MIN_VERSION 6.8.2; Text.CurveRendering (Qt 6.7) is available, so no mismatch.
- **opus-ultra:** ❌ FALSE (95) — CurveRendering exists on Qt 6.8.2 target (CMakeLists.txt:57)

### [QML-09] `QtQuick.Shapes 6.6` version mismatch with `QtCore 6.5`  ·  _SPLIT_  ·  Medium
`src/prompter/Countdown.qml:24`
- **opus:** ❌ FALSE (95) — Shapes 6.6 valid on Qt 6.8.2
- **gpt:** ❌ FALSE (90) — Shapes 6.6 is below the 6.8.2 project target (src/prompter/Countdown.qml:24)
- **deepseek:** ❌ FALSE (85) — ReadRegionOverlay.qml:22 imports QtQuick 2.12 not Shapes 6.6; the Countdown.qml claim also invalid — QT_MIN_VERSION=6.8.2 means Qt>=6.8.2 >=6.6
- **glm:** ⚠️ PARTIAL (55) — Countdown.qml:24 imports QtQuick.Shapes 6.6 but target is Qt 6.8.2 so version is compatible
- **kimi:** ❌ FALSE (85) — CMakeLists.txt:57 targets Qt 6.8.2; QtQuick.Shapes 6.6 import is satisfied despite QtCore 6.5 import.
- **opus-ultra:** ❌ FALSE (95) — Shapes 6.6 valid on Qt 6.8.2

### [QML-11] Dead code: `window` property declared but never used in WindowDragger  ·  _SPLIT_  ·  Medium
`src/qt/WindowDragger.qml:28`
- **opus:** ✅ LEGIT (90) — window property dead; impl uses root (WindowDragger.qml:27)
- **gpt:** ⚠️ PARTIAL (58) — observed Dead code: window property declared but never used in WindowDragger (src/qt/WindowDragger.qml:28)
- **deepseek:** ✅ LEGIT (85) — WindowDragger.qml:28 declares window:parent property but implementation uses undefined root instead at lines 41,45 — window is dead code
- **glm:** ⚠️ PARTIAL (70) — WindowDragger.qml:28 property var window is declared but the drag logic uses root.x/root.y directly
- **kimi:** ✅ LEGIT (75) — WindowDragger.qml:28 declares window property but onPositionChanged uses root instead, so assignment is wasted.
- **opus-ultra:** ✅ LEGIT (90) — window property dead; impl uses root (WindowDragger.qml:27)

### [QOBJ-N01] QmlUtil missing constructor with parent parameter  ·  _SPLIT_  ·  Low
`qmlutil.hpp:47`
- **opus:** ⚠️ PARTIAL (40) — QmlUtil missing parent-arg constructor (qmlutil.hpp:47)
- **gpt:** ✅ LEGIT (78) — QmlUtil missing constructor with parent parameter (src/qmlutil.hpp:47)
- **deepseek:** ✅ LEGIT (85) — qmlutil.hpp:47: QML_ELEMENT class with all methods inline; no explicit parent-taking constructor; new QmlUtil from C++ would leak (currently only QML singleton instantiated)
- **glm:** ✅ LEGIT (70) — qmlutil.hpp:47 QmlUtil missing constructor with parent parameter
- **kimi:** ✅ LEGIT (60) — qmlutil.hpp:47 QmlUtil has no constructor taking parent; C++ instantiation would leak if not parented.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — QmlUtil missing parent-arg constructor (qmlutil.hpp:47)

### [QP-N01] restartApplication() quits even when startDetached fails — app dies with no replacement  ·  _SPLIT_  ·  High
`qmlutil.hpp:97-102`
- **opus:** ✅ LEGIT (65) — restartApplication quits even if startDetached fails (return ignored) (qmlutil.hpp:97)
- **gpt:** ⚠️ PARTIAL (58) — observed restartApplication() quits even when startDetached fails - app dies with no replacement (src/qmlutil.hpp:97)
- **deepseek:** ✅ LEGIT (95) — qmlutil.hpp:97-102: QProcess::startDetached return bool discarded; quit() fires unconditionally; app dies if restart fails
- **glm:** ✅ LEGIT (80) — qmlutil.hpp:97-102 restartApplication() quits even when startDetached fails; app dies with no replacement
- **kimi:** ✅ LEGIT (95) — qmlutil.hpp:100-102 discards startDetached() return and calls quit() unconditionally
- **opus-ultra:** ✅ LEGIT (65) — restartApplication quits even if startDetached fails (return ignored) (qmlutil.hpp:97)

### [QRC-N01] icons.qrc contains duplicate \<file\> entry  ·  _SPLIT_  ·  Low
`src/icons/icons.qrc:45,47`
- **opus:** ❔ UNSURE (45) — icons.qrc duplicate <file> entry; needs file read
- **gpt:** ✅ LEGIT (92) — icons.qrc contains duplicate \file\ entry (src/icons/icons.qrc:45)
- **deepseek:** ✅ LEGIT (95) — Identical <file> entry at icons.qrc:45 and :47 — same SVG embedded twice
- **glm:** ✅ LEGIT (80) — src/icons/icons.qrc has duplicate <file> entry at lines 45 and 47
- **kimi:** ✅ LEGIT (95) — src/icons/icons.qrc:45 and :47 list the same gnumeric-object-scrollbar.svg alias twice.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — icons.qrc duplicate <file> entry; needs file read

### [QRC-N02] Four .qrc files are dead code — never referenced by CMakeLists.txt  ·  _SPLIT_  ·  Low
`src/icons/icons.qrc, src/fonts/fonts.qrc, src/fonts/chinese.qrc, src/prompter/pointers/pointers.qrc`
- **opus:** ⚠️ PARTIAL (45) — four .qrc files unreferenced by CMake; dead
- **gpt:** ⚠️ PARTIAL (58) — observed Four .qrc files are dead code - never referenced by CMakeLists.txt (src/icons/icons.qrc:1)
- **deepseek:** ✅ LEGIT (90) — .qrc files orphaned — resources compiled via qt_add_qml_module/Resources in src/CMakeLists.txt instead
- **glm:** ✅ LEGIT (80) — icons.qrc fonts.qrc chinese.qrc pointers.qrc never referenced by CMakeLists.txt; dead QRC files
- **kimi:** ✅ LEGIT (85) — No CMakeLists.txt references src/icons/icons.qrc, src/fonts/fonts.qrc, chinese.qrc, or pointers.qrc; they are dead artifacts.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — four .qrc files unreferenced by CMake; dead

### [QTD-02] QQuickTextDocument destroyed without destroyed signal connection  ·  _SPLIT_  ·  Low-Medium
`documenthandler.h:334, documenthandler.cpp:175-202`
- **opus:** ❔ UNSURE (40) — QQuickTextDocument destroyed-signal not connected; lifetime QML-managed (documenthandler.cpp:175)
- **gpt:** ✅ LEGIT (78) — QQuickTextDocument destroyed without destroyed signal connection (src/documenthandler.h:334)
- **deepseek:** ✅ LEGIT (85) — Raw QQuickTextDocument* m_document at documenthandler.h:334 — no destroyed signal dangles on QML teardown
- **glm:** ⚠️ PARTIAL (60) — documenthandler.h:334 QQuickTextDocument destroyed without destroyed signal connection; potential dangling
- **kimi:** ✅ LEGIT (80) — documenthandler.h:334 stores QQuickTextDocument* raw; no destroyed handler to null it on QML teardown.
- **opus-ultra:** ❔ UNSURE (40) — max: unverifiable statically (runtime/semantic) — QQuickTextDocument destroyed-signal not connected; lifetime QML-managed (documenthandler.c

### [QW-N01] Projection Window onClosing references cleared model — spurious runtime errors  ·  _SPLIT_  ·  Medium
`ProjectionsManager.qml:130-133,196-201`
- **opus:** ⚠️ PARTIAL (50) — onClosing references cleared model (ProjectionsManager.qml:130)
- **gpt:** ⚠️ PARTIAL (58) — observed Projection Window onClosing references cleared model - spurious runtime errors (src/prompter/ProjectionsManager.qml:130)
- **deepseek:** ✅ LEGIT (90) — ProjectionsManager.qml:130-133: closeAll clears projectionModel; async Instantiator destruction triggers onClosing remove on cleared model
- **glm:** ✅ LEGIT (75) — ProjectionsManager.qml:130-133 196-201 Projection Window onClosing references cleared model; spurious runtime errors
- **kimi:** ✅ LEGIT (85) — ProjectionsManager.qml:132 clears projectionModel then onClosing at 199 calls remove(model.index) on the empty model
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — onClosing references cleared model (ProjectionsManager.qml:130)

### [QW-N02] Stale QScreen reference in projection model — dangling after monitor hot-unplug  ·  _SPLIT_  ·  Medium
`ProjectionsManager.qml:119,177`
- **opus:** ⚠️ PARTIAL (55) — stores QScreen ref; dangling after hot-unplug (ProjectionsManager.qml:119)
- **gpt:** ⚠️ PARTIAL (58) — observed Stale QScreen reference in projection model - dangling after monitor hot-unplug (src/prompter/ProjectionsManager.qml:119)
- **deepseek:** ✅ LEGIT (85) — ProjectionsManager.qml:119 177: QScreen objects captured into ListModel at project(); monitor unplug -> dangling pointer; wrong coords
- **glm:** ✅ LEGIT (75) — ProjectionsManager.qml:119 177 stale QScreen reference in projection model; dangling after monitor hot-unplug
- **kimi:** ✅ LEGIT (85) — ProjectionsManager.qml:119 stores `screen` QScreen objects in the model, which become stale after hot-unplug
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — stores QScreen ref; dangling after hot-unplug (ProjectionsManager.qml:119)

### [R2-AND-01] Android missing QmlUtil causes crash on factory reset and RecentDocuments  ·  _SPLIT_  ·  Critical
`src/kirigami_ui/+android/main.qml (absent object), line 684`
- **opus:** ✅ LEGIT (90) — no qmlutil -> factoryReset crash (+android/main.qml:684)
- **gpt:** ⚠️ PARTIAL (58) — factory reset uses missing qmlutil, but RecentDocuments has a null guard (src/kirigami_ui/+android/main.qml:684)
- **deepseek:** ❔ UNSURE (35) — Android QmlUtil absence — depends on whether +android/main.qml inherits from base qml or is standalone; need file analysis
- **glm:** ✅ LEGIT (85) — +android/main.qml:684 qmlutil.factoryReset() called but QmlUtil {} never declared in android variant
- **kimi:** ✅ LEGIT (95) — +android/main.qml:684 calls qmlutil.factoryReset() with no QmlUtil declared; RecentDocuments lacks util property.
- **opus-ultra:** ✅ LEGIT (90) — no qmlutil -> factoryReset crash (+android/main.qml:684)

### [R2-AND-02] Android missing restartDialog crashes LanguageSettingsOverlay and LayoutDirectionSettingsOverlay  ·  _SPLIT_  ·  Critical
`src/kirigami_ui/+android/main.qml (absent object)`
- **opus:** ✅ LEGIT (90) — no restartDialog -> overlay crash (+android)
- **gpt:** ✅ LEGIT (84) — Android missing restartDialog crashes LanguageSettingsOverlay and LayoutDirectionSettingsOverlay (src/kirigami_ui/+android/main.qml:1)
- **deepseek:** ❔ UNSURE (35) — Android restartDialog absence — same inheritance question as R2-AND-01
- **glm:** ✅ LEGIT (80) — +android/main.qml references restartDialog but no MessageDialog with that id declared in android variant
- **kimi:** ✅ LEGIT (95) — +android/main.qml has no restartDialog; LanguageSettingsOverlay.qml:48 / LayoutDirectionSettingsOverlay.qml:47 require it.
- **opus-ultra:** ✅ LEGIT (90) — no restartDialog -> overlay crash (+android)

### [R2-AND-03] Android Settings missing fakeFullScreen persistence  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/+android/main.qml:72-77`
- **opus:** ✅ LEGIT (80) — no fakeFullScreen persistence alias (+android)
- **gpt:** ✅ LEGIT (78) — Android Settings missing fakeFullScreen persistence (src/kirigami_ui/+android/main.qml:72)
- **deepseek:** ❔ UNSURE (35) — Android fakeFullScreen persistence — need to verify Settings block structure in +android/main.qml
- **glm:** ✅ LEGIT (80) — +android/main.qml:72-77 Settings block missing __fakeFullscreen alias present in base main.qml
- **kimi:** ✅ LEGIT (80) — +android/main.qml:72-77 mainWindow Settings lacks fakeFullScreen alias present in base/windows variants.
- **opus-ultra:** ✅ LEGIT (80) — no fakeFullScreen persistence alias (+android)

### [R2-AND-04] Android Settings for "background" missing transparency persistence  ·  _SPLIT_  ·  Low
`src/kirigami_ui/+android/main.qml:96-100`
- **opus:** ⚠️ PARTIAL (45) — +android background Settings missing transparency alias; no current impact (main.qml:96)
- **gpt:** ⚠️ PARTIAL (58) — observed Android Settings for "background" missing transparency persistence (src/kirigami_ui/+android/main.qml:96)
- **deepseek:** ❔ UNSURE (30) — Android transparency persistence — future compat issue minimal current impact
- **glm:** ✅ LEGIT (75) — +android/main.qml:96-100 background Settings missing transparency alias present in base
- **kimi:** ✅ LEGIT (70) — +android/main.qml:96-100 background Settings lacks transparency alias present in base/windows variants.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — +android background Settings missing transparency alias; no current impact (main.qml:96)

### [R2-AND-05] Android loadTelemetryPage passes no properties object to pageStack push  ·  _SPLIT_  ·  Low
`src/kirigami_ui/+android/main.qml:162`
- **opus:** ⚠️ PARTIAL (45) — +android loadTelemetryPage push no properties obj (main.qml:162)
- **gpt:** ⚠️ PARTIAL (58) — observed Android loadTelemetryPage passes no properties object to pageStack push (src/kirigami_ui/+android/main.qml:162)
- **deepseek:** ❔ UNSURE (25) — Telemetry page push missing props — commented-out component; no current impact
- **glm:** ✅ LEGIT (80) — +android/main.qml:162 layers.push(telemetryPageComponent) missing {} second arg unlike sibling calls
- **kimi:** ✅ LEGIT (60) — +android/main.qml:162 pushes telemetryPageComponent without {} properties object used in base/windows.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — +android loadTelemetryPage push no properties obj (main.qml:162)

### [R2-ANDMAN-02] MANAGE_EXTERNAL_STORAGE likely triggers Play Store scrutiny  ·  _SPLIT_  ·  Medium
`android/AndroidManifest.xml:49`
- **opus:** ✅ LEGIT (85) — MANAGE_EXTERNAL_STORAGE Play-policy risk (AndroidManifest.xml:49)
- **gpt:** ✅ LEGIT (78) — MANAGE_EXTERNAL_STORAGE likely triggers Play Store scrutiny (android/AndroidManifest.xml:49)
- **deepseek:** ✅ LEGIT (90) — AndroidManifest.xml:49: MANAGE_EXTERNAL_STORAGE is All Files Access restricted by Google Play policy requiring justification; teleprompter unlikely to qualify
- **glm:** ✅ LEGIT (80) — AndroidManifest.xml:49 MANAGE_EXTERNAL_STORAGE triggers Play Store scrutiny and requires declaration
- **kimi:** ⚠️ PARTIAL (55) — AndroidManifest.xml:49 declares MANAGE_EXTERNAL_STORAGE; valid permission but invites Play Store policy scrutiny and is an anti-pattern.
- **opus-ultra:** ✅ LEGIT (85) — MANAGE_EXTERNAL_STORAGE Play-policy risk (AndroidManifest.xml:49)

### [R2-CMAKE-02] cmake_minimum_required inside find module pollutes parent project policy settings  ·  _SPLIT_  ·  High
`cmake/FindSphinx.cmake:19`
- **opus:** ✅ LEGIT (80) — cmake_minimum_required in find module (FindSphinx.cmake:19)
- **gpt:** ✅ LEGIT (84) — cmake_minimum_required inside find module pollutes parent project policy settings (cmake/FindSphinx.cmake:19)
- **deepseek:** ✅ LEGIT (90) — cmake_minimum_required inside find module at FindSphinx.cmake:19 pollutes parent policy; per CMake docs should not be in find modules
- **glm:** ⚠️ PARTIAL (60) — cmake/FindSphinx.cmake:19 cmake_minimum_required inside find module; pollutes policy but not a build breaker
- **kimi:** ✅ LEGIT (90) — cmake/FindSphinx.cmake:19 cmake_minimum_required inside find module changes parent project policies.
- **opus-ultra:** ✅ LEGIT (80) — cmake_minimum_required in find module (FindSphinx.cmake:19)

### [R2-EDT-01] Qt.AlignHustify typo — nonexistent enum value  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/EditorToolbar.qml:380`
- **opus:** ✅ LEGIT (90) — Qt.AlignHustify typo -> enabled always true (EditorToolbar.qml:380)
- **gpt:** ✅ LEGIT (92) — Qt.AlignHustify typo - nonexistent enum value (src/kirigami_ui/EditorToolbar.qml:380)
- **deepseek:** ❔ UNSURE (40) — Qt.AlignHustify typo at EditorToolbar.qml:380; need to verify Qt namespace enums; likely genuine typo but requires Qt API confirmation
- **glm:** ✅ LEGIT (95) — EditorToolbar.qml:380 Qt.AlignHustify is a typo for Qt.AlignJustify; resolves to undefined
- **kimi:** ✅ LEGIT (90) — EditorToolbar.qml:380 compares alignment to Qt.AlignHustify (undefined typo); should be Qt.AlignJustify.
- **opus-ultra:** ✅ LEGIT (90) — Qt.AlignHustify typo -> enabled always true (EditorToolbar.qml:380)

### [R2-EDT-02] wheelThrottleSettingsButton checked bound to completely unrelated document property  ·  _SPLIT_  ·  High
`src/kirigami_ui/EditorToolbar.qml:790`
- **opus:** ✅ LEGIT (85) — wheel button checked bound to document.namedMarker (EditorToolbar.qml:790)
- **gpt:** ✅ LEGIT (84) — wheelThrottleSettingsButton checked bound to completely unrelated document property (src/kirigami_ui/EditorToolbar.qml:790)
- **deepseek:** ❔ UNSURE (35) — wheelThrottleSettingsButton checked bound to namedMarker at EditorToolbar.qml:790; need full QML to verify if this is intentional or copy-paste
- **glm:** ✅ LEGIT (90) — EditorToolbar.qml:790 wheelThrottleSettingsButton checked bound to document.namedMarker (unrelated property)
- **kimi:** ✅ LEGIT (90) — EditorToolbar.qml:790 wheelThrottleSettingsButton checked bound to document.namedMarker instead of wheel setting.
- **opus-ultra:** ✅ LEGIT (85) — wheel button checked bound to document.namedMarker (EditorToolbar.qml:790)

### [R2-EDT-03] Checkable ToolButtons break checked property bindings on first click — systematic  ·  _SPLIT_  ·  High
`src/kirigami_ui/EditorToolbar.qml:223-224,233-236,380-381,392-394,404-406,416-418,429-431,449-452,460-463,471-474,482-485,493-503,513-525,725-727,741-743,751-753,769-772,790-792,836`
- **opus:** ✅ LEGIT (80) — checkable + checked:binding -> click destroys binding (EditorToolbar.qml:223)
- **gpt:** ✅ LEGIT (84) — Checkable ToolButtons break checked property bindings on first click - systematic (src/kirigami_ui/EditorToolbar.qml:223)
- **deepseek:** ⚠️ PARTIAL (55) — Checkable ToolButtons breaking declarative bindings is well-known QtQuick behavior; ~20 buttons affected — binding breakage is real but intentional by Qt design
- **glm:** ✅ LEGIT (85) — EditorToolbar.qml:223+ checkable ToolButtons with checked binding break on first click; systematic pattern across many buttons
- **kimi:** ✅ LEGIT (90) — EditorToolbar.qml:223-224 etc. checkable ToolButtons with checked: expression break binding when first clicked.
- **opus-ultra:** ✅ LEGIT (80) — checkable + checked:binding -> click destroys binding (EditorToolbar.qml:223)

### [R2-IOS-01] Method swizzling re-entry causes infinite recursion on second invocation  ·  _SPLIT_  ·  High
`src/shakedetector.mm:74-78`
- **opus:** ✅ LEGIT (80) — swizzle re-entry captures self -> recursion (shakedetector.mm:74)
- **gpt:** ✅ LEGIT (84) — Method swizzling re-entry causes infinite recursion on second invocation (src/shakedetector.mm:74)
- **deepseek:** ❔ UNSURE (40) — Method swizzling re-entry at shakedetector.mm:74-78; .mm file not read; plausible iOS ObjC runtime bug but cannot verify without .mm source
- **glm:** ⚠️ PARTIAL (65) — shakedetector.mm:74-78 class_addMethod returns true on first call then method_setImplementation on second; but class_addMethod already replaced so no recursion
- **kimi:** ✅ LEGIT (85) — shakedetector.mm:74-78 setupShakeDetection swizzles without guard; second call captures itself causing infinite recursion.
- **opus-ultra:** ✅ LEGIT (80) — swizzle re-entry captures self -> recursion (shakedetector.mm:74)

### [R2-IOS-02] Delegate block captures raw assign pointer — use-after-free risk  ·  _SPLIT_  ·  Medium
`src/iossavedialog.mm:42-44,50-52`
- **opus:** ⚠️ PARTIAL (50) — delegate captures assign raw ptr; UAF needs singleton destroyed (iossavedialog.mm:42)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/iossavedialog.mm:42)
- **deepseek:** ❔ UNSURE (40) — Delegate block captures assign pointer at iossavedialog.mm:42-44; .mm file not read; plausible but need ObjC source verification
- **glm:** ✅ LEGIT (80) — iossavedialog.mm:42-44 delegate uses assign property capturing raw pointer; use-after-free risk if dialog destroyed before callback
- **kimi:** ✅ LEGIT (80) — iossavedialog.mm:31-44,50-52 delegate property is assign and block captures raw pointer; UAF if dialog destroyed.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — delegate captures assign raw ptr; UAF needs singleton destroyed (iossavedialog.mm:42)

### [R2-OVL-01] InputsOverlay onOpened calls cursorAutoHide.restart() instead of reset()  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/InputsOverlay.qml:41`
- **opus:** ⚠️ PARTIAL (65) — cursorAutoHide.restart() on open vs reset() elsewhere (InputsOverlay.qml:41)
- **gpt:** ⚠️ PARTIAL (58) — observed InputsOverlay onOpened calls cursorAutoHide.restart() instead of reset() (src/kirigami_ui/InputsOverlay.qml:41)
- **deepseek:** ❔ UNSURE (35) — restart vs reset at InputsOverlay.qml:41 — need to verify Timer API and intended behavior
- **glm:** ✅ LEGIT (85) — InputsOverlay.qml:41 cursorAutoHide.restart() called on open; should be reset() per the pattern used elsewhere
- **kimi:** ✅ LEGIT (85) — InputsOverlay.qml:41 calls cursorAutoHide.restart() while other overlays call reset(); cursor hides during config.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — cursorAutoHide.restart() on open vs reset() elsewhere (InputsOverlay.qml:41)

### [R2-OVL-02] LanguageSettingsOverlay popup ListView currentIndex always resolves to -1  ·  _SPLIT_  ·  Low
`src/kirigami_ui/LanguageSettingsOverlay.qml:73`
- **opus:** ✅ LEGIT (85) — popup currentIndex indexOf(int) over object array -> -1 (LanguageSettingsOverlay.qml:73)
- **gpt:** ✅ LEGIT (78) — LanguageSettingsOverlay popup ListView currentIndex always resolves to -1 (src/kirigami_ui/LanguageSettingsOverlay.qml:73)
- **deepseek:** ❔ UNSURE (35) — ListView currentIndex=-1 at LanguageSettingsOverlay.qml:73 — need to verify model structure and indexOf semantics
- **glm:** ✅ LEGIT (80) — LanguageSettingsOverlay.qml:73 ListView currentIndex uses indexOf which returns -1 when not found; always -1
- **kimi:** ✅ LEGIT (80) — LanguageSettingsOverlay.qml:73 indexOf(integer) on model array of objects always returns -1.
- **opus-ultra:** ✅ LEGIT (85) — popup currentIndex indexOf(int) over object array -> -1 (LanguageSettingsOverlay.qml:73)

### [R2-PRP-01] Qt.LeftToRight used as bare boolean — RTL branch always dead  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/PrompterPage.qml:189,193,659`
- **opus:** ✅ LEGIT (80) — bare Qt.LeftToRight used as condition (PrompterPage.qml:189)
- **gpt:** ✅ LEGIT (78) — Qt.LeftToRight used as bare boolean - RTL branch always dead (src/kirigami_ui/PrompterPage.qml:189)
- **deepseek:** ❔ UNSURE (45) — Qt.LeftToRight used as bare boolean at PrompterPage.qml:189/193/659 — need to verify QML context; Qt.LeftToRight is non-zero enum but usage pattern unclear without full file
- **glm:** ✅ LEGIT (90) — PrompterPage.qml:189 193 659 uses Qt.LeftToRight (enum value 0) as boolean; always falsy so RTL branch always taken
- **kimi:** ✅ LEGIT (90) — PrompterPage.qml:189,193,659 uses Qt.LeftToRight as bare boolean; should compare to Qt.application.layoutDirection.
- **opus-ultra:** ✅ LEGIT (80) — bare Qt.LeftToRight used as condition (PrompterPage.qml:189)

### [R2-PRP-02] Kirigami.Units.SmallSpacing — uppercase S yields undefined  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/PrompterPage.qml:1331,1332,1352,1353,1377,1378`
- **opus:** ✅ LEGIT (85) — Units.SmallSpacing should be smallSpacing (PrompterPage.qml:1331)
- **gpt:** ✅ LEGIT (92) — Kirigami.Units.SmallSpacing - uppercase S yields undefined (src/kirigami_ui/PrompterPage.qml:1331)
- **deepseek:** ❔ UNSURE (40) — Kirigami.Units.SmallSpacing uppercase S claimed undefined; depends on Kirigami 2.x API; need to verify actual property name in Kirigami's Units singleton
- **glm:** ✅ LEGIT (85) — PrompterPage.qml:1331+ uses Kirigami.Units.SmallSpacing with capital S; correct API is kirigamiUnits.smallSpacing or Units.smallSpacing
- **kimi:** ✅ LEGIT (90) — PrompterPage.qml:1331,1332,1352,1353,1377,1378 uses Kirigami.Units.SmallSpacing (undefined); correct is smallSpacing.
- **opus-ultra:** ✅ LEGIT (85) — Units.SmallSpacing should be smallSpacing (PrompterPage.qml:1331)

### [R2-PRP-04] Inconsistent focus restoration in decreaseVelocityButton  ·  _SPLIT_  ·  Low
`src/kirigami_ui/PrompterPage.qml:89`
- **opus:** ⚠️ PARTIAL (50) — decreaseVelocityButton focus assign vs restoreFocus() (PrompterPage.qml:89)
- **gpt:** ⚠️ PARTIAL (58) — observed Inconsistent focus restoration in decreaseVelocityButton (src/kirigami_ui/PrompterPage.qml:89)
- **deepseek:** ❔ UNSURE (35) — Inconsistent focus restoration at PrompterPage.qml:89; need full QML context to verify intent vs bug
- **glm:** ⚠️ PARTIAL (55) — PrompterPage.qml:89 focus restoration in decreaseVelocityButton uses prompter.focus=true instead of restoreFocus(); minor inconsistency
- **kimi:** ✅ LEGIT (75) — PrompterPage.qml:89 decreaseVelocityButton sets focus=true instead of restoreFocus() used by increaseVelocityButton.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — decreaseVelocityButton focus assign vs restoreFocus() (PrompterPage.qml:89)

### [R2-PRP-05] Potential null-item access on async Loader in namedMarkerConfiguration.onOpened  ·  _SPLIT_  ·  Low
`src/kirigami_ui/PrompterPage.qml:1144,1146`
- **opus:** ⚠️ PARTIAL (45) — async Loader null-item in namedMarkerConfiguration.onOpened (PrompterPage.qml:1144)
- **gpt:** ⚠️ PARTIAL (52) — observed Potential null-item access on async Loader in namedMarkerConfiguration.onOpened (src/kirigami_ui/PrompterPage.qml:1144)
- **deepseek:** ❔ UNSURE (30) — Async Loader null-item access depends on timing and QML engine behavior; cannot verify without runtime test
- **glm:** ✅ LEGIT (80) — PrompterPage.qml:1144 1146 Loader.item access in onOpened without null check; async Loader may not have loaded yet
- **kimi:** ✅ LEGIT (80) — PrompterPage.qml:1144,1146 accesses setMarkerKeyButton alias of asynchronous Loader before item may be ready.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — async Loader null-item in namedMarkerConfiguration.onOpened (PrompterPage.qml:1144)

### [R2-PTR-03] Casing error: Units.longDuration should be Units.LongDuration  ·  _SPLIT_  ·  Medium
`src/prompter/ProjectionsManager.qml:329`
- **opus:** ✅ LEGIT (80) — Units.longDuration casing (ProjectionsManager.qml:329)
- **gpt:** ✅ LEGIT (78) — Casing error: Units.longDuration should be Units.LongDuration (src/prompter/ProjectionsManager.qml:329)
- **deepseek:** ❔ UNSURE (40) — Units.longDuration lowercase vs LongDuration at ProjectionsManager.qml:329; depends on Kirigami Units property case — need API reference
- **glm:** ✅ LEGIT (85) — ProjectionsManager.qml:329 Units.longDuration should be Units.LongDuration; casing error
- **kimi:** ✅ LEGIT (85) — ProjectionsManager.qml:329 uses Units.longDuration (lowercase) and file does not import Kirigami; undefined.
- **opus-ultra:** ✅ LEGIT (80) — Units.longDuration casing (ProjectionsManager.qml:329)

### [R2-PTR-04] Inverted indexOf truthiness in platform check for ColorDialog  ·  _SPLIT_  ·  Medium
`src/prompter/PointerSettings.qml:653`
- **opus:** ✅ LEGIT (85) — indexOf truthiness bug (PointerSettings.qml:653)
- **gpt:** ✅ LEGIT (78) — Inverted indexOf truthiness in platform check for ColorDialog (src/prompter/PointerSettings.qml:653)
- **deepseek:** ❔ UNSURE (35) — indexOf truthiness inversion at PointerSettings.qml:653; JS logic analysis correct on paper but need to verify actual runtime context
- **glm:** ✅ LEGIT (85) — PointerSettings.qml:653 indexOf returns -1 for not found which is truthy; logic inverted for platform check
- **kimi:** ✅ LEGIT (90) — PointerSettings.qml:653 inverted indexOf truthiness flips ColorDialog.DontUseNativeDialog logic on non-macOS/iOS.
- **opus-ultra:** ✅ LEGIT (85) — indexOf truthiness bug (PointerSettings.qml:653)

### [R2-REC-01] File URI prefix strip off-by-one on Windows  ·  _SPLIT_  ·  Low
`src/kirigami_ui/RecentDocuments.qml:70`
- **opus:** ✅ LEGIT (85) — substring(7) leaves leading / on Windows (RecentDocuments.qml:70)
- **gpt:** ✅ LEGIT (92) — File URI prefix strip off-by-one on Windows (src/kirigami_ui/RecentDocuments.qml:70)
- **deepseek:** ⚠️ PARTIAL (60) — Windows file:// URL has 3 slashes (file:///C:...); substring(7) strips 7 chars leaving /C: — off-by-one for 3-slash URIs confirmed
- **glm:** ⚠️ PARTIAL (60) — RecentDocuments.qml:70 URI prefix strip off-by-one on Windows; file:// is 7 chars but stripping may include extra char
- **kimi:** ✅ LEGIT (80) — RecentDocuments.qml:70 uri.substring(7) on Windows file:///C:/... leaves leading slash in tooltip path.
- **opus-ultra:** ✅ LEGIT (85) — substring(7) leaves leading / on Windows (RecentDocuments.qml:70)

### [R2-REC-02] refreshExistence skips UI updates when dynamic children out of sync  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/RecentDocuments.qml:171`
- **opus:** ⚠️ PARTIAL (50) — refreshExistence skips when counts diverge (RecentDocuments.qml:171)
- **gpt:** ⚠️ PARTIAL (58) — observed refreshExistence skips UI updates when dynamic children out of sync (src/kirigami_ui/RecentDocuments.qml:171)
- **deepseek:** ❔ UNSURE (30) — refreshExistence count synchronization — race condition plausible but need dynamic analysis
- **glm:** ✅ LEGIT (80) — RecentDocuments.qml:171 refreshExistence skips UI updates when dynamic children count is out of sync
- **kimi:** ✅ LEGIT (75) — RecentDocuments.qml:171 guard _dynamicChildren.length === recentsModel.count skips UI updates when counts diverge.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — refreshExistence skips when counts diverge (RecentDocuments.qml:171)

### [R2-TEL-01] Telemetry sub-toggles permanently disconnect from master toggle on click  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/TelemetryPage.qml:80-88,101-110,123-132,149-158`
- **opus:** ✅ LEGIT (80) — telemetry sub-toggles break from master on click (TelemetryPage.qml:80)
- **gpt:** ✅ LEGIT (78) — Telemetry sub-toggles permanently disconnect from master toggle on click (src/kirigami_ui/TelemetryPage.qml:80)
- **deepseek:** ❔ UNSURE (35) — Telemetry sub-toggles disconnect from master — commented-out code; need verification of active code paths
- **glm:** ✅ LEGIT (85) — TelemetryPage.qml:80+ sub-toggles disconnect from master toggle on click due to imperative assignment breaking binding
- **kimi:** ✅ LEGIT (85) — TelemetryPage.qml:80-88,101-110,123-132,149-158 sub-toggles checked: root.__telemetry break binding when toggled individually.
- **opus-ultra:** ✅ LEGIT (80) — telemetry sub-toggles break from master on click (TelemetryPage.qml:80)

### [R2-WASM-01] File input element never removed from DOM on user cancel  ·  _SPLIT_  ·  Medium
`src/wasmintegration.cpp:148-149`
- **opus:** ✅ LEGIT (85) — input element leaked in DOM on cancel (wasmintegration.cpp:148)
- **gpt:** ✅ LEGIT (78) — File input element never removed from DOM on user cancel (src/wasmintegration.cpp:148)
- **deepseek:** ❔ UNSURE (35) — DOM input element leak at wasmintegration.cpp:148-149; need wasmintegration.cpp source verification
- **glm:** ⚠️ PARTIAL (65) — wasmintegration.cpp:148-149 file input element removed on change event but not on user cancel (no cancel listener)
- **kimi:** ✅ LEGIT (85) — wasmintegration.cpp:148-149 file input appended to DOM is only removed in change handler; cancel leaks the element.
- **opus-ultra:** ✅ LEGIT (85) — input element leaked in DOM on cancel (wasmintegration.cpp:148)

### [R2-WASM-02] Insecure hostname validation via endsWith allows subdomain spoofing  ·  _SPLIT_  ·  Medium
`src/wasmintegration.cpp:192`
- **opus:** ✅ LEGIT (85) — endsWith host spoofing (wasmintegration.cpp:192)
- **gpt:** ✅ LEGIT (78) — Insecure hostname validation via endsWith allows subdomain spoofing (src/wasmintegration.cpp:192)
- **deepseek:** ❔ UNSURE (35) — endsWith hostname validation at wasmintegration.cpp:192; need source verification of officialHost() implementation
- **glm:** ✅ LEGIT (85) — wasmintegration.cpp:192 endsWith for hostname validation allows subdomain spoofing (e.g. evil.qprompt.app)
- **kimi:** ✅ LEGIT (85) — wasmintegration.cpp:192 endsWith('localhost'/'qprompt.app') allows evillocalhost.com/fakeqprompt.app spoofing.
- **opus-ultra:** ✅ LEGIT (85) — endsWith host spoofing (wasmintegration.cpp:192)

### [R3-MAIN-02] Invalid locale string constructed for short language codes  ·  _SPLIT_  ·  High
`src/main.cpp:141-143`
- **opus:** ⚠️ PARTIAL (55) — language+.UTF-8 invalid only for 2-letter codes (main.cpp:141)
- **gpt:** ⚠️ PARTIAL (58) — observed Invalid locale string constructed for short language codes (src/main.cpp:141)
- **deepseek:** ✅ LEGIT (90) — main.cpp:141 language.toUtf8()+'.UTF-8' for short codes like 'es' produces 'es.UTF-8' — not valid POSIX locale; setlocale silently fails
- **glm:** ✅ LEGIT (85) — main.cpp:141-143 for short language codes like 'en' QLocale name produces 'en' not 'en_US'; translator.load may fail
- **kimi:** ✅ LEGIT (75) — main.cpp:141 appends .UTF-8 to the user language string; short codes like en become invalid locale names (e.g. en.UTF-8).
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — language+.UTF-8 invalid only for 2-letter codes (main.cpp:141)

### [R3-MAIN-04] Stack-allocated QTranslator outlives QApplication on shutdown  ·  _SPLIT_  ·  Low
`src/main.cpp:133,107/109,138/149`
- **opus:** ❌ FALSE (85) — translator-after-app is standard Qt idiom
- **gpt:** ❌ FALSE (76) — translator lifetime follows normal stack order after QApplication (src/main.cpp:133)
- **deepseek:** ⚠️ PARTIAL (60) — main.cpp:133 QTranslator declared after app(line 107/109) destroyed before app — violates installTranslator contract but Qt gracefully handles during teardown
- **glm:** ⚠️ PARTIAL (60) — main.cpp:133 QTranslator on stack outlives QApplication only during shutdown; benign in practice
- **kimi:** ❌ FALSE (65) — main.cpp:133 QTranslator is declared after QApplication, so it is destroyed before app on shutdown; no outliving occurs.
- **opus-ultra:** ❌ FALSE (85) — translator-after-app is standard Qt idiom

### [R3-MAIN-05] Hardcoded Homebrew version-specific Kirigami import path  ·  _SPLIT_  ·  Medium
`src/main.cpp:314`
- **opus:** ✅ LEGIT (80) — hardcoded Homebrew Cellar Kirigami path (main.cpp:314)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/main.cpp:314)
- **deepseek:** ✅ LEGIT (98) — main.cpp:314 hardcoded /opt/homebrew/Cellar/kf5-kirigami2/5.95.0/lib/qt6/qml — every brew upgrade breaks path
- **glm:** ✅ LEGIT (80) — main.cpp:314 hardcoded Homebrew version-specific Kirigami import path /opt/homebrew/Cellar/kf5-kirigami2/5.95.0/lib/qt6/qml
- **kimi:** ✅ LEGIT (85) — main.cpp:314 hardcodes /opt/homebrew/Cellar/kf5-kirigami2/5.95.0/lib/qt6/qml; brittle, breaks when Homebrew formula version changes.
- **opus-ultra:** ✅ LEGIT (80) — hardcoded Homebrew Cellar Kirigami path (main.cpp:314)

### [R3-MAIN-06] Inconsistent Kirigami platform guards — missing WATCHOS and QNX  ·  _SPLIT_  ·  High
`src/main.cpp:225,42-43`
- **opus:** ✅ LEGIT (90) — registerTypes guards 3; include guards 5 platforms (main.cpp:225)
- **gpt:** ✅ LEGIT (84) — Inconsistent Kirigami platform guards - missing WATCHOS and QNX (src/main.cpp:225)
- **deepseek:** ✅ LEGIT (90) — main.cpp:42-43 KIRIGAMI_BUILD_TYPE_STATIC for 5 platforms but main.cpp:225 registerTypes() only for ANDROID/IOS/WASM — WATCHOS+QNX omitted
- **glm:** ⚠️ PARTIAL (55) — main.cpp:225 platform guards include Android/iOS/WASM but QNX and WATCHOS are handled separately; not strictly inconsistent
- **kimi:** ✅ LEGIT (75) — main.cpp:42-43 guards include WATCHOS/QNX but line 225 KirigamiPlugin::registerTypes() excludes them; inconsistent platform bootstrapping.
- **opus-ultra:** ✅ LEGIT (90) — registerTypes guards 3; include guards 5 platforms (main.cpp:225)

### [R3-MAIN-08] QFontDatabase::addApplicationFont return value discarded  ·  _SPLIT_  ·  Low
`src/main.cpp:120`
- **opus:** ✅ LEGIT (55) — addApplicationFont return discarded (main.cpp:120)
- **gpt:** ✅ LEGIT (78) — QFontDatabase::addApplicationFont return value discarded (src/main.cpp:120)
- **deepseek:** ✅ LEGIT (80) — main.cpp:120 QFontDatabase::addApplicationFont() return value(-1 on fail) discarded — WASM emoji font failure silent
- **glm:** ⚠️ PARTIAL (60) — main.cpp:120 addApplicationFont return value discarded; font may silently fail to load
- **kimi:** ✅ LEGIT (65) — main.cpp:120 discards QFontDatabase::addApplicationFont() return value; missing font resource is silently ignored.
- **opus-ultra:** ✅ LEGIT (55) — addApplicationFont return discarded (main.cpp:120)

### [R3-PMT-01] OBS WebSocket JSON.parse without try/catch — crash on malformed input  ·  _SPLIT_  ·  High
`src/prompter/Prompter.qml:368`
- **opus:** ⚠️ PARTIAL (60) — JSON.parse no try/catch; crash-to-desktop overstated (Prompter.qml:367)
- **gpt:** ⚠️ PARTIAL (58) — observed OBS WebSocket JSON.parse without try/catch - crash on malformed input (src/prompter/Prompter.qml:368)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:368 JSON.parse(m) in onTextMessageReceived has no try/catch — malformed OBS WebSocket JSON causes unhandled exception/crash
- **glm:** ✅ LEGIT (85) — Prompter.qml:368 JSON.parse(m) without try/catch; crashes on malformed WebSocket message
- **kimi:** ✅ LEGIT (95) — WebSocket onTextMessageReceived calls JSON.parse(m) without try/catch at Prompter.qml:368
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — JSON.parse no try/catch; crash-to-desktop overstated (Prompter.qml:367)

### [R3-PMT-03] goToNextMarker fallback desynchronizes cursor from viewport  ·  _SPLIT_  ·  Medium
`src/prompter/Prompter.qml:658-659`
- **opus:** ⚠️ PARTIAL (50) — goToNextMarker fallback desyncs cursor/viewport; domain (Prompter.qml:658)
- **gpt:** ⚠️ PARTIAL (58) — observed goToNextMarker fallback desynchronizes cursor from viewport (src/prompter/Prompter.qml:658)
- **deepseek:** ✅ LEGIT (85) — Prompter.qml:658-659 fallback scrolls viewport to document end but does NOT update editor.cursorPosition — cursor/viewport desynchronized
- **glm:** ✅ LEGIT (75) — Prompter.qml:658-659 goToNextMarker sets cursorPosition then reads cursorRectangle.y which may not have updated yet
- **kimi:** ✅ LEGIT (90) — goToNextMarker fallback jumps prompter.position to end without updating editor.cursorPosition at Prompter.qml:658-659
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — goToNextMarker fallback desyncs cursor/viewport; domain (Prompter.qml:658)

### [R3-PROP-01] selectionIsLowerCase bound to wrong NOTIFY signal  ·  _SPLIT_  ·  Medium
`src/documenthandler.h:119`
- **opus:** ✅ LEGIT (80) — selectionIsLowerCase wrong NOTIFY (documenthandler.h:119)
- **gpt:** ✅ LEGIT (78) — selectionIsLowerCase bound to wrong NOTIFY signal (src/documenthandler.h:119)
- **deepseek:** ✅ LEGIT (80) — documenthandler.h:119 selectionIsLowerCase NOTIFY fontCapitalizationChanged — cursor-move-only changes never fire; stale bindings after text edits
- **glm:** ⚠️ PARTIAL (65) — documenthandler.h:119 selectionIsLowerCase NOTIFY is fontCapitalizationChanged; signal doesn't fire for case-only changes
- **kimi:** ✅ LEGIT (85) — documenthandler.h:119 selectionIsLowerCase property NOTIFY is fontCapitalizationChanged; its value actually depends on cursor selection, not capitalization.
- **opus-ultra:** ✅ LEGIT (80) — selectionIsLowerCase wrong NOTIFY (documenthandler.h:119)

### [R3-SPL-01] encode() uses toLocal8Bit() instead of dictionary-encoding-aware conversion  ·  _SPLIT_  ·  Medium
`src/spellchecker.cpp:400-406`
- **opus:** ✅ LEGIT (70) — encode() toLocal8Bit ignores dict encoding (spellchecker.cpp:400)
- **gpt:** ✅ LEGIT (78) — encode() uses toLocal8Bit() instead of dictionary-encoding-aware conversion (src/spellchecker.cpp:400)
- **deepseek:** ✅ LEGIT (80) — spellchecker.cpp:400-405 encode() fallback toLocal8Bit() ignores d.encoding — uses system locale not dictionary encoding(KOI8-R/CP1251 mismatch)
- **glm:** ⚠️ PARTIAL (65) — spellchecker.cpp:400-406 encode uses toLocal8Bit for non-UTF-8 dicts; correct for legacy encodings but may not match dictionary encoding
- **kimi:** ✅ LEGIT (75) — spellchecker.cpp:400-406 encode falls back to toLocal8Bit() regardless of d.encoding; non-UTF-8 dictionaries will mangle input.
- **opus-ultra:** ✅ LEGIT (70) — encode() toLocal8Bit ignores dict encoding (spellchecker.cpp:400)

### [R3-SPL-02] decode() uses fromLocal8Bit() — suggestions show as mojibake  ·  _SPLIT_  ·  Medium
`src/spellchecker.cpp:408-413`
- **opus:** ✅ LEGIT (70) — decode() fromLocal8Bit ignores dict encoding (spellchecker.cpp:408)
- **gpt:** ✅ LEGIT (78) — decode() uses fromLocal8Bit() - suggestions show as mojibake (src/spellchecker.cpp:408)
- **deepseek:** ✅ LEGIT (80) — spellchecker.cpp:408-412 decode() fallback fromLocal8Bit() same encoding mismatch as encode() — non-UTF-8 dictionary suggestions garbled
- **glm:** ⚠️ PARTIAL (65) — spellchecker.cpp:408-413 decode uses fromLocal8Bit; correct for legacy encodings but may produce mojibake if system locale differs
- **kimi:** ✅ LEGIT (75) — spellchecker.cpp:408-413 decode falls back to fromLocal8Bit() ignoring d.encoding; suggestions from non-UTF-8 dictionaries become mojibake.
- **opus-ultra:** ✅ LEGIT (70) — decode() fromLocal8Bit ignores dict encoding (spellchecker.cpp:408)

### [R3-SPL-05] SpellChecker has zero thread safety — all methods unprotected  ·  _SPLIT_  ·  Medium
`src/spellchecker.h:32-77`
- **opus:** ⚠️ PARTIAL (45) — SpellChecker no mutexes; speculative single-threaded (spellchecker.h:32)
- **gpt:** ⚠️ PARTIAL (58) — observed SpellChecker has zero thread safety - all methods unprotected (src/spellchecker.h:32)
- **deepseek:** ✅ LEGIT (85) — spellchecker.h:32-77 no QMutex/std::mutex anywhere; m_dicts iterated by highlightBlock while mutated by setLanguage/removeCustomWord — iterator invalidation risk
- **glm:** ✅ LEGIT (85) — spellchecker.h:32-77 all methods access m_dicts/m_customWords without mutex; zero thread safety
- **kimi:** ⚠️ PARTIAL (55) — spellchecker.h:32-77 methods mutate shared m_dicts/m_customWords without locks; no source evidence of concurrent access, so latent rather than proven bug.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — SpellChecker no mutexes; speculative single-threaded (spellchecker.h:32)

### [R3-TMR-01] TimerClock ETA uses __iDefault instead of actual __i during reverse scroll  ·  _SPLIT_  ·  Medium
`src/prompter/TimerClock.qml:66`
- **opus:** ❔ UNSURE (45) — __iDefault vs __i in ETA fallback; domain call (TimerClock.qml:66)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/TimerClock.qml:66)
- **deepseek:** ✅ LEGIT (80) — TimerClock.qml:66 ETA fallback uses prompter.__iDefault(static default) instead of actual __i — wrong ETA after mid-session velocity change
- **glm:** ✅ LEGIT (85) — TimerClock.qml:66 ETA uses __iDefault instead of actual __i during reverse scroll; wrong ETA when reversed
- **kimi:** ✅ LEGIT (95) — ETA fallback uses prompter.__iDefault instead of actual __i for reverse scroll at TimerClock.qml:66
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — __iDefault vs __i in ETA fallback; domain call (TimerClock.qml:66)

### [R4-BKG-01] Flip transform origin stays at (0,0) when Flip stored as property  ·  _SPLIT_  ·  Medium
`src/prompter/PrompterBackground.qml:89-90 (also ReadRegionOverlay:65,90)`
- **opus:** ✅ LEGIT (85) — Scale has no width; origin.x: width/2=0 (Flip.qml:27)
- **gpt:** ✅ LEGIT (78) — Flip transform origin stays at (0,0) when Flip stored as property (src/prompter/PrompterBackground.qml:89)
- **deepseek:** ✅ LEGIT (85) — PrompterBackground.qml:89-90 Scale Flip{} without explicit origin — default (0 0) causes flip around top-left not center
- **glm:** ⚠️ PARTIAL (60) — PrompterBackground.qml:89-90 Flip transform origin at (0 0) when Flip is property; cosmetic issue
- **kimi:** ✅ LEGIT (90) — PrompterBackground.qml:89-90 Flip{} Scale binds origin.x/y to its own zero width/height, so flips occur around (0,0).
- **opus-ultra:** ✅ LEGIT (85) — Scale has no width; origin.x: width/2=0 (Flip.qml:27)

### [R4-EVT-02] Velocity modifier ComboBox lists 2 options but switch handles 4 — dead code  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/InputsOverlay.qml:425-441`
- **opus:** ✅ LEGIT (90) — ComboBox 2 items, switch 0-3 (InputsOverlay.qml:425)
- **gpt:** ⚠️ PARTIAL (58) — observed Velocity modifier ComboBox lists 2 options but switch handles 4 - dead code (src/kirigami_ui/InputsOverlay.qml:425)
- **deepseek:** ✅ LEGIT (95) — InputsOverlay.qml:425-428 ComboBox model has 2 items(Alt Ctrl) but switch onActivated handles cases 0-3 — Shift/Meta unreachable
- **glm:** ✅ LEGIT (80) — InputsOverlay.qml:425-441 ComboBox model has 2 entries but switch handles 4 cases; cases 2-3 are dead code
- **kimi:** ✅ LEGIT (95) — ComboBox model has 2 items but onActivated switch includes unreachable cases 2 and 3; InputsOverlay.qml:423-441
- **opus-ultra:** ✅ LEGIT (90) — ComboBox 2 items

### [R4-EVT-03] CursorAutoHide null access on root.pageStack.currentItem during page transitions  ·  _SPLIT_  ·  High
`src/prompter/CursorAutoHide.qml:28,31,43,56`
- **opus:** ⚠️ PARTIAL (60) — pageStack.currentItem null during transitions; plausible (CursorAutoHide.qml:28)
- **gpt:** ✅ LEGIT (84) — CursorAutoHide null access on root.pageStack.currentItem during page transitions (src/prompter/CursorAutoHide.qml:28)
- **deepseek:** ✅ LEGIT (85) — CursorAutoHide.qml:28/31/43/56 dereference root.pageStack.currentItem without null guard — during page transitions currentItem briefly null
- **glm:** ✅ LEGIT (80) — CursorAutoHide.qml:28 31 43 56 dereferences pageStack.currentItem.prompter during page transitions; null risk
- **kimi:** ✅ LEGIT (85) — CursorAutoHide accesses root.pageStack.currentItem without null guard at lines 28
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — pageStack.currentItem null during transitions; plausible (CursorAutoHide.qml:28)

### [R4-EXP-01] No XSS sanitization — script tags, event handlers, javascript: URLs unfiltered  ·  _SPLIT_  ·  Critical
`src/documenthandler.cpp:1246-1334`
- **opus:** ⚠️ PARTIAL (55) — filterHtml doesn't strip scripts but Qt richtext runs no JS (documenthandler.cpp:1246)
- **gpt:** ⚠️ PARTIAL (58) — observed No XSS sanitization - script tags, event handlers, javascript: URLs unfiltered (src/documenthandler.cpp:1246)
- **deepseek:** ✅ LEGIT (95) — documenthandler.cpp:1246-1334 filterHtml applies 6 CSS-property regexes only; no removal of script/iframe/object/embed/event-handlers or javascript: URLs
- **glm:** ✅ LEGIT (85) — documenthandler.cpp:1246-1334 filterHtml doesn't sanitize script tags event handlers or javascript: URLs
- **kimi:** ✅ LEGIT (85) — filterHtml at documenthandler.cpp:1246-1334 strips CSS/IDs only; no script tag/event handler/javascript URL sanitization
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — filterHtml doesn't strip scripts but Qt richtext runs no JS (documenthandler.cpp:1246)

### [R4-EXP-09] LibreOffice import --cat and --convert-to flags are contradictory  ·  _SPLIT_  ·  Low
`src/documenthandler.cpp:1076`
- **opus:** ⚠️ PARTIAL (55) — --cat and --convert-to are contradictory soffice flags (documenthandler.cpp:1076)
- **gpt:** ⚠️ PARTIAL (58) — observed LibreOffice import --cat and --convert-to flags are contradictory (src/documenthandler.cpp:1076)
- **deepseek:** ✅ LEGIT (85) — documenthandler.cpp:1076 --cat(pipe to stdout) and --convert-to(write file) are contradictory flags — LibreOffice may produce empty stdout
- **glm:** ⚠️ PARTIAL (65) — documenthandler.cpp:1076 --cat and --convert-to are both passed to LibreOffice; --cat outputs to stdout but --convert-to writes to file
- **kimi:** ✅ LEGIT (85) — LibreOffice arguments include both --cat and --convert-to which are mutually contradictory; documenthandler.cpp:1076
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — --cat and --convert-to are contradictory soffice flags (documenthandler.cpp:1076)

### [R4-IOSCPP-01] QTemporaryDir created on all platforms including non-iOS where unused  ·  _SPLIT_  ·  Low
`src/iossavedialog.h:49`
- **opus:** ⚠️ PARTIAL (50) — QTemporaryDir by-value member on all platforms (iossavedialog.h:49)
- **gpt:** ⚠️ PARTIAL (58) — observed QTemporaryDir created on all platforms including non-iOS where unused (src/iossavedialog.h:49)
- **deepseek:** ✅ LEGIT (90) — iossavedialog.h:49 QTemporaryDir m_tempDir by-value member — default constructor creates temp dir on ALL platforms even non-iOS
- **glm:** ⚠️ PARTIAL (60) — iossavedialog.h:49 QTemporaryDir m_tempDir created on all platforms; unused on non-iOS but minimal waste
- **kimi:** ✅ LEGIT (85) — iossavedialog.h:49 QTemporaryDir m_tempDir member default-constructs a real temp directory for every app start on all platforms.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — QTemporaryDir by-value member on all platforms (iossavedialog.h:49)

### [R4-PRJ-01] flip variable spuriously reset in project() inner loop else-branch  ·  _SPLIT_  ·  High
`src/prompter/ProjectionsManager.qml:108-114`
- **opus:** ❌ FALSE (80) — break preserves match (ProjectionsManager.qml:108)
- **gpt:** ❌ FALSE (76) — the inner break exits after a match; it does not discard it (src/prompter/ProjectionsManager.qml:108)
- **deepseek:** ❌ FALSE (85) — ProjectionsManager.qml:108-114 break exits immediately on match before else runs for that iteration — flip correctly set by match; no spurious reset
- **glm:** ⚠️ PARTIAL (60) — ProjectionsManager.qml:108-114 flip variable reset in else-branch; may cause visual glitch but not critical
- **kimi:** ❌ FALSE (90) — Inner loop breaks on match; non-matching else resets default but does not discard the actual match; ProjectionsManager.qml:108-114
- **opus-ultra:** ❌ FALSE (80) — break preserves match (ProjectionsManager.qml:108)

### [R4-PRJ-02] displayModel.get().flipSetting writes to snapshot copy — never mutates model  ·  _SPLIT_  ·  High
`src/prompter/ProjectionsManager.qml:83,141,150`
- **opus:** ❔ UNSURE (45) — ListModel.get() mutation is version-dependent (ProjectionsManager.qml:83)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/ProjectionsManager.qml:83)
- **deepseek:** ✅ LEGIT (95) — ProjectionsManager.qml:83/141/150 ListModel.get() returns JS snapshot not live ref — flipSetting writes to copy never mutate model
- **glm:** ✅ LEGIT (80) — ProjectionsManager.qml:83 141 150 displayModel.get().flipSetting writes to snapshot copy via ListModel setProperty not direct mutation
- **kimi:** ✅ LEGIT (95) — displayModel.get()/projectionModel.get() return JS copies; writing flipSetting/flip does not update the model; ProjectionsManager.qml:83
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — ListModel.get() mutation is version-dependent (ProjectionsManager.qml:83)

### [R4-ROOT-05] loadRemoteControlPage/loadTelemetryPage reference undefined component IDs  ·  _SPLIT_  ·  Low
`src/kirigami_ui/main.qml:175-181`
- **opus:** ⚠️ PARTIAL (50) — loadRemoteControl/Telemetry reference commented-out components (main.qml:175)
- **gpt:** ✅ LEGIT (92) — loadRemoteControlPage/loadTelemetryPage reference undefined component IDs (src/kirigami_ui/main.qml:175)
- **deepseek:** ✅ LEGIT (95) — main.qml:175-181 loadRemoteControlPage/loadTelemetryPage reference commented-out components(1072-1079) — ReferenceError if C++ calls these
- **glm:** ⚠️ PARTIAL (60) — main.qml:175-181 loadRemoteControlPage/loadTelemetryPage reference component IDs that may resolve via context
- **kimi:** ✅ LEGIT (90) — Functions push remoteControlPageComponent and telemetryPageComponent which are commented out; main.qml:177-181
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — loadRemoteControl/Telemetry reference commented-out components (main.qml:175)

### [R4-ROV-01] Division by zero in __customPlacement when overlay full  ·  _SPLIT_  ·  High
`src/prompter/ReadRegionOverlay.qml:189`
- **opus:** ⚠️ PARTIAL (60) — div-by-zero only when readRegion fills overlay (ReadRegionOverlay.qml:189)
- **gpt:** ⚠️ PARTIAL (58) — observed Division by zero in __customPlacement when overlay full (src/prompter/ReadRegionOverlay.qml:189)
- **deepseek:** ✅ LEGIT (90) — ReadRegionOverlay.qml:189 readRegion.y/(overlay.height-readRegion.height) — when readRegion fills overlay denominator=0 — Infinity/NaN
- **glm:** ✅ LEGIT (80) — ReadRegionOverlay.qml:189 division by zero in __customPlacement when overlay.height equals readRegion.height
- **kimi:** ✅ LEGIT (95) — ReadRegionOverlay.qml:189 divides readRegion.y by (overlay.height-readRegion.height); denominator 0 when heights equal, yielding Infinity/NaN.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — div-by-zero only when readRegion fills overlay (ReadRegionOverlay.qml:189)

### [R4-ROV-02] Drag permanently breaks y property binding on readRegion  ·  _SPLIT_  ·  High
`src/prompter/ReadRegionOverlay.qml:181-182,141`
- **opus:** ⚠️ PARTIAL (65) — drag breaks y binding; impact partial (ReadRegionOverlay.qml:141,181)
- **gpt:** ⚠️ PARTIAL (58) — observed Drag permanently breaks y property binding on readRegion (src/prompter/ReadRegionOverlay.qml:181)
- **deepseek:** ✅ LEGIT (90) — ReadRegionOverlay.qml:181-182 drag.target assigns y directly breaking declarative y binding at line 141; no re-establishment after drag
- **glm:** ✅ LEGIT (80) — ReadRegionOverlay.qml:181-182 Drag on parent breaks y property binding at :141
- **kimi:** ✅ LEGIT (90) — ReadRegionOverlay.qml:181 MouseArea drag.target:parent writes readRegion.y directly, destroying the declarative y binding at line 141.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — drag breaks y binding; impact partial (ReadRegionOverlay.qml:141

### [R4-ROV-03] Bitwise OR | used for width fallback instead of logical OR  ·  _SPLIT_  ·  Medium
`src/prompter/ReadRegionOverlay.qml:396`
- **opus:** ✅ LEGIT (90) — bitwise | for width (ReadRegionOverlay.qml:396)
- **gpt:** ✅ LEGIT (78) — Bitwise OR | used for width fallback instead of logical OR (src/prompter/ReadRegionOverlay.qml:396)
- **deepseek:** ✅ LEGIT (95) — ReadRegionOverlay.qml:396 bitwise OR | on two non-zero ints(eg 50|60=62) instead of logical || or ternary — right pointer origin off-center
- **glm:** ⚠️ PARTIAL (65) — ReadRegionOverlay.qml:396 bitwise | for width fallback; works but should be logical ||
- **kimi:** ✅ LEGIT (95) — ReadRegionOverlay.qml:396 uses bitwise OR (width|contentWidth)/2 instead of logical OR/ternary, producing wrong transform origin.
- **opus-ultra:** ✅ LEGIT (90) — bitwise | for width (ReadRegionOverlay.qml:396)

### [R4-SIG-ADD-01] SessionModel::appendDataPoint declared public slot but never connected  ·  _SPLIT_  ·  Low
`src/prompsession.h:71`
- **opus:** ⚠️ PARTIAL (45) — appendDataPoint public slot never connected; dead-code area (promptsession.h:71)
- **gpt:** ⚠️ PARTIAL (58) — observed SessionModel::appendDataPoint declared public slot but never connected (src/prompsession.h:71)
- **deepseek:** ⚠️ PARTIAL (60) — promptsession.h:71 appendDataPoint in public slots never connected to any signal; but QML can still invoke slots directly — signal-driven recording dead
- **glm:** ✅ LEGIT (75) — promptsession.h:71 appendDataPoint declared as public slot but never connected via signal/slot
- **kimi:** ✅ LEGIT (70) — promptsession.h:71 appendDataPoint is a slot but not connected externally; signal-driven path dead, yet callable from QML.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — appendDataPoint public slot never connected; dead-code area (promptsession.h:71)

### [RAII-N01] QDrag object never deleteLater'd after exec() — leaks on rejected drags  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1486-1489`
- **opus:** ⚠️ PARTIAL (50) — QDrag parented to this; accumulates per drag rather than leaks outright (documenthandler.cpp:1486)
- **gpt:** ✅ LEGIT (78) — QDrag object never deleteLater'd after exec() - leaks on rejected drags (src/documenthandler.cpp:1486)
- **deepseek:** ✅ LEGIT (60) — QDrag new'd per drag operation with parent this; accumulates over session (documenthandler.cpp:1486-1489)
- **glm:** ✅ LEGIT (80) — documenthandler.cpp:1486-1489 QDrag never deleteLater'd after exec(); leaks on rejected drags. Actually QDrag(this) has parent so auto-deleted.
- **kimi:** ✅ LEGIT (85) — new QDrag at documenthandler.cpp:1486 is not deleteLater'd after exec() returns; object leaks on rejected drag operations.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — QDrag parented to this; accumulates per drag rather than leaks outright (documenthandler.c

### [RAII-N02] IosSaveDialog::m_tempDir created unconditionally on all platforms — wasted I/O  ·  _SPLIT_  ·  Low
`iossavedialog.h:49`
- **opus:** ⚠️ PARTIAL (50) — m_tempDir created unconditionally; wasted I/O (dup R4-IOSCPP-01) (iossavedialog.h:49)
- **gpt:** ⚠️ PARTIAL (58) — observed IosSaveDialog::mtempDir created unconditionally on all platforms - wasted I/O (src/iossavedialog.h:49)
- **deepseek:** ✅ LEGIT (55) — QTemporaryDir m_tempDir constructed unconditionally on all platforms (iossavedialog.h:49)
- **glm:** ✅ LEGIT (75) — iossavedialog.h:49 QTemporaryDir m_tempDir created unconditionally on all platforms
- **kimi:** ✅ LEGIT (80) — IosSaveDialog.h:49 contains QTemporaryDir m_tempDir; the singleton is created on all platforms, wasting temp dirs outside iOS.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — m_tempDir created unconditionally; wasted I/O (dup R4-IOSCPP-01) (iossavedialog.h:49)

### [REGEX-CRIT-01] regex_4 destroys <body> tag — removes opening tag instead of color attributes  ·  _SPLIT_  ·  High
`documenthandler.cpp:1287`
- **opus:** ❔ UNSURE (45) — regex_4 may strip <body> opening tag; complex regex, hard to confirm (documenthandler.cpp:1287)
- **gpt:** ❔ UNSURE (39) — the body-tag regex is complex; impact needs sample HTML (src/documenthandler.cpp:1287)
- **deepseek:** ✅ LEGIT (85) — documenthandler.cpp:1287: regex_4 matches <body through last color attribute quote but stops before >; replace removes opening tag leaving orphaned >content</body> — corrupted HTML
- **glm:** ✅ LEGIT (80) — documenthandler.cpp:1287 regex_4 destroys <body> tag; removes opening tag instead of just color attributes
- **kimi:** ✅ LEGIT (90) — documenthandler.cpp:1287 regex_4 replace deletes from '<body' through last matched quote, destroying the opening body tag.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — regex_4 may strip <body> opening tag; complex regex

### [REGEX-N01] All 13 QRegularExpression objects lack isValid() checks  ·  _SPLIT_  ·  Medium
`documenthandler.cpp, spellhighlighter.cpp (13 regex objects)`
- **opus:** ⚠️ PARTIAL (45) — 13 regexes lack isValid(); all but search are author-literal (always valid)
- **gpt:** ✅ LEGIT (78) — All 13 QRegularExpression objects lack isValid() checks (src/documenthandler.cpp:893)
- **deepseek:** ✅ LEGIT (85) — 13 QRegularExpression objects lack isValid() checks — pattern typo silently matches nothing
- **glm:** ✅ LEGIT (75) — 13 QRegularExpression objects across documenthandler.cpp and spellhighlighter.cpp lack isValid() checks
- **kimi:** ✅ LEGIT (95) — documenthandler.cpp has 12 QRegularExpression objects (regex_0..regex_8, imgSrcRegex, searchRegEx) and spellhighlighter.cpp has 1 (wordRe); none call isValid()
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — 13 regexes lack isValid(); all but search are author-literal (always valid)

### [REGEX-N04] ReDoS — user-supplied regex has no length limit, timeout, or backtracking guard  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1543-1557`
- **opus:** ⚠️ PARTIAL (50) — ReDoS: user regex no length/timeout guard; user's own input (documenthandler.cpp:1543)
- **gpt:** ✅ LEGIT (78) — ReDoS - user-supplied regex has no length limit, timeout, or backtracking guard (src/documenthandler.cpp:1543)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:1543-1557: user-supplied regex has no length limit no MatchTimeout no optimize(); evil regex like (a+)+b causes exponential backtracking — 100% CPU hang
- **glm:** ✅ LEGIT (80) — documenthandler.cpp:1543-1557 user-supplied regex has no length limit timeout or backtracking guard; ReDoS risk
- **kimi:** ✅ LEGIT (85) — documenthandler.cpp:1543-1557 accepts arbitrary user regex with no length limit, timeout or optimize(); malicious input can ReDoS.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — ReDoS: user regex no length/timeout guard; user's own input (documenthandler.cpp:1543)

### [RENDER-01] ShaderEffectSource prompterShadowSource runs unconditionally — wastes GPU capture when shadows disabled  ·  _SPLIT_  ·  Medium
`PrompterView.qml:230-233`
- **opus:** ⚠️ PARTIAL (50) — prompterShadowSource runs unconditionally; GPU waste (PrompterView.qml:230)
- **gpt:** ✅ LEGIT (78) — ShaderEffectSource prompterShadowSource runs unconditionally - wastes GPU capture when shadows disabled (src/prompter/PrompterView.qml:230)
- **deepseek:** ✅ LEGIT (70) — ShaderEffectSource unconditionally captures GPU regardless of shadows setting (PrompterView.qml:230-233)
- **glm:** ✅ LEGIT (75) — PrompterView.qml:230-233 prompterShadowSource ShaderEffectSource runs unconditionally even when shadows disabled
- **kimi:** ✅ LEGIT (80) — PrompterView.qml:230-233 instantiates prompterShadowSource with default live=true and no guard; Prompter.qml:744 only enables the consuming layer when root.shadows, so capture continues while shadows are disabled.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — prompterShadowSource runs unconditionally; GPU waste (PrompterView.qml:230)

### [RENDER-02] ShaderEffectSource pointerShadowSource runs unconditionally — same pattern  ·  _SPLIT_  ·  Medium
`ReadRegionOverlay.qml:123-126`
- **opus:** ⚠️ PARTIAL (50) — pointerShadowSource runs unconditionally (ReadRegionOverlay.qml:123)
- **gpt:** ✅ LEGIT (78) — ShaderEffectSource pointerShadowSource runs unconditionally - same pattern (src/prompter/ReadRegionOverlay.qml:123)
- **deepseek:** ✅ LEGIT (70) — pointerShadowSource ShaderEffectSource captures unconditionally (ReadRegionOverlay.qml:123-126)
- **glm:** ✅ LEGIT (75) — ReadRegionOverlay.qml:123-126 pointerShadowSource ShaderEffectSource runs unconditionally
- **kimi:** ✅ LEGIT (80) — ReadRegionOverlay.qml:123-126 instantiates pointerShadowSource with default live=true and no guard; the shadow effect at line 145 is gated by layer.enabled only.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — pointerShadowSource runs unconditionally (ReadRegionOverlay.qml:123)

### [RES-03] ShakeDetector::s_instance never set to nullptr on destruction (dangling pointer)  ·  _SPLIT_  ·  Low
`src/shakedetector.cpp:24,29`
- **opus:** ⚠️ PARTIAL (65) — s_instance not reset; singleton lifetime low (shakedetector.cpp:24)
- **gpt:** ⚠️ PARTIAL (58) — observed ShakeDetector::s_instance never set to nullptr on destruction (dangling pointer) (src/shakedetector.cpp:24)
- **deepseek:** ✅ LEGIT (85) — s_instance set in ctor at shakedetector.cpp:29 but never reset to nullptr on destruction; dangling pointer after QML engine recreate
- **glm:** ⚠️ PARTIAL (60) — shakedetector.cpp:24 s_instance set in constructor and never nulled in destructor; dangling but QML singleton lifecycle makes this benign
- **kimi:** ✅ LEGIT (80) — shakedetector.cpp:24,29 sets s_instance in ctor but no dtor resets it; recreated singleton returns dangling pointer.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — s_instance not reset; singleton lifetime low (shakedetector.cpp:24)

### [RES-04] IosSaveDialog::s_instance same singleton dangling pattern  ·  _SPLIT_  ·  Low
`src/iossavedialog.cpp:24,29`
- **opus:** ⚠️ PARTIAL (65) — same singleton pattern (iossavedialog.cpp:24)
- **gpt:** ⚠️ PARTIAL (58) — observed IosSaveDialog::s_instance same singleton dangling pattern (src/iossavedialog.cpp:24)
- **deepseek:** ✅ LEGIT (85) — Identical s_instance dangling pattern at iossavedialog.cpp:29; never reset to nullptr; use-after-free risk on singleton destruction
- **glm:** ⚠️ PARTIAL (60) — iossavedialog.cpp:24 same singleton pattern as RES-03; dangling pointer on destruction but benign for QML singleton
- **kimi:** ✅ LEGIT (80) — iossavedialog.cpp:24,29 sets s_instance in ctor but no dtor resets it; same dangling pattern.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — same singleton pattern (iossavedialog.cpp:24)

### [RESO-N01] Editing font size not viewport-scaled — text nearly unreadable on 4K  ·  _SPLIT_  ·  Medium
`PrompterView.qml:242`
- **opus:** ⚠️ PARTIAL (45) — editing font size not viewport-scaled on 4K (PrompterView.qml:242)
- **gpt:** ⚠️ PARTIAL (48) — visual issue is plausible but depends on theme or device (src/prompter/PrompterView.qml:242)
- **deepseek:** ✅ LEGIT (95) — PrompterView.qml:242: editing branch lacks *prompter.__vw/10 multiplier present in WYSIWYG branch; font disproportionately small on 4K
- **glm:** ✅ LEGIT (70) — PrompterView.qml:242 editing font size not viewport-scaled; text nearly unreadable on 4K
- **kimi:** ✅ LEGIT (90) — PrompterView.qml:242 editing font-size branch omits the `*prompter.__vw/10` viewport scaling used in WYSIWYG
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — editing font size not viewport-scaled on 4K (PrompterView.qml:242)

### [RESO-N02] Scrollbar width 6dp-13dp — below minimum 44dp touch target  ·  _SPLIT_  ·  Low
`ProgressIndicator.qml:39`
- **opus:** ⚠️ PARTIAL (40) — scrollbar 6-13dp below 44dp touch target (ProgressIndicator.qml:39)
- **gpt:** ⚠️ PARTIAL (48) — visual issue is plausible but depends on theme or device (src/prompter/ProgressIndicator.qml:39)
- **deepseek:** ✅ LEGIT (80) — ProgressIndicator.qml:39: implicitWidth 6-13dp; well below minimum 44dp touch target per accessibility guidelines
- **glm:** ✅ LEGIT (65) — ProgressIndicator.qml:39 scrollbar width 6dp-13dp below minimum 44dp touch target
- **kimi:** ✅ LEGIT (80) — ProgressIndicator.qml:39 sets scrollbar width to 6 or 13, well below the 44dp touch-target guideline
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — scrollbar 6-13dp below 44dp touch target (ProgressIndicator.qml:39)

### [RESO-N03] Control spacing hardcoded 8dp — cramped on large displays  ·  _SPLIT_  ·  Low
`PrompterView.qml:63,64,113, Prompter.qml:1047`
- **opus:** ⚠️ PARTIAL (40) — control spacing hardcoded 8dp (PrompterView.qml:63)
- **gpt:** ⚠️ PARTIAL (48) — visual issue is plausible but depends on theme or device (src/prompter/PrompterView.qml:63)
- **deepseek:** ✅ LEGIT (75) — PrompterView.qml:63 64: spacing/padding hardcoded 8dp; cramped on large displays; minor observation
- **glm:** ⚠️ PARTIAL (55) — PrompterView.qml:63 64 113 Prompter.qml:1047 control spacing hardcoded 8dp; cramped on large displays
- **kimi:** ✅ LEGIT (70) — PrompterView.qml:63/113 and Prompter.qml:1047 hardcode spacing:8, ignoring display density
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — control spacing hardcoded 8dp (PrompterView.qml:63)

### [RESO-N04] Projection-window margins fixed 10dp/5dp — near-flush on large screens  ·  _SPLIT_  ·  Low
`ProjectionsManager.qml:324-325`
- **opus:** ⚠️ PARTIAL (40) — projection margins fixed 10/5dp (ProjectionsManager.qml:324)
- **gpt:** ⚠️ PARTIAL (48) — visual issue is plausible but depends on theme or device (src/prompter/ProjectionsManager.qml:324)
- **deepseek:** ✅ LEGIT (75) — ProjectionsManager.qml:324-325: margins fixed 10dp/5dp; near-flush on large projection screens; minor
- **glm:** ⚠️ PARTIAL (55) — ProjectionsManager.qml:324-325 projection-window margins fixed 10dp/5dp; near-flush on large screens
- **kimi:** ✅ LEGIT (70) — ProjectionsManager.qml:324-325 hardcode anchors.leftMargin:10 and bottomMargin:5
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — projection margins fixed 10/5dp (ProjectionsManager.qml:324)

### [RESO-N05] PointerSettings ListView height hardcoded 180dp — doesn't fill available space  ·  _SPLIT_  ·  Low
`PointerSettings.qml:254`
- **opus:** ⚠️ PARTIAL (40) — ListView height hardcoded 180dp (PointerSettings.qml:254)
- **gpt:** ⚠️ PARTIAL (48) — visual issue is plausible but depends on theme or device (src/prompter/PointerSettings.qml:254)
- **deepseek:** ✅ LEGIT (75) — PointerSettings.qml:254: ListView height hardcoded 180dp; doesn't fill available space
- **glm:** ✅ LEGIT (65) — PointerSettings.qml:254 ListView height hardcoded 180dp; doesn't fill available space
- **kimi:** ✅ LEGIT (70) — PointerSettings.qml:254 hardcodes ListView height:180 instead of filling available space
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — ListView height hardcoded 180dp (PointerSettings.qml:254)

### [RESO-N06] ReadRegionOverlay pointer margin 3dp — overlap with text at large fonts  ·  _SPLIT_  ·  Low
`ReadRegionOverlay.qml:260,267`
- **opus:** ⚠️ PARTIAL (40) — pointer margin 3dp overlap at large fonts (ReadRegionOverlay.qml:260)
- **gpt:** ⚠️ PARTIAL (48) — visual issue is plausible but depends on theme or device (src/prompter/ReadRegionOverlay.qml:260)
- **deepseek:** ✅ LEGIT (80) — ReadRegionOverlay.qml:260 267: pointer margin 3dp; overlaps text at large font sizes
- **glm:** ⚠️ PARTIAL (55) — ReadRegionOverlay.qml:260 267 pointer margin 3dp; overlap with text at large fonts
- **kimi:** ✅ LEGIT (70) — ReadRegionOverlay.qml:260/267 set pointer margins to 3, causing overlap at large font sizes
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — pointer margin 3dp overlap at large fonts (ReadRegionOverlay.qml:260)

### [RESP-N01] minimumHeight: minimumWidth forces square aspect ratio — prevents landscape-strip windows  ·  _SPLIT_  ·  Low
`main.qml:83, +windows:78`
- **opus:** ⚠️ PARTIAL (50) — minimumHeight: minimumWidth forces square aspect (main.qml:83)
- **gpt:** ⚠️ PARTIAL (58) — observed minimumHeight: minimumWidth forces square aspect ratio - prevents landscape-strip windows (src/kirigami_ui/main.qml:83)
- **deepseek:** ✅ LEGIT (85) — main.qml:83: minimumHeight: minimumWidth forces square minimum; prevents landscape-strip window shapes that layout would handle
- **glm:** ✅ LEGIT (65) — main.qml:83 +windows:78 minimumHeight: minimumWidth forces square aspect ratio; prevents landscape-strip windows
- **kimi:** ✅ LEGIT (90) — main.qml:83 sets minimumHeight: minimumWidth, forcing a square minimum window
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — minimumHeight: minimumWidth forces square aspect (main.qml:83)

### [RESP-N02] mobileOrSmallScreen threshold at 1231px activates on default 1220px launch  ·  _SPLIT_  ·  Medium
`main.qml:54,77`
- **opus:** ❔ UNSURE (45) — mobileOrSmallScreen 1231px vs 1220px launch; heuristic threshold (main.qml:54)
- **gpt:** ⚠️ PARTIAL (58) — observed mobileOrSmallScreen threshold at 1231px activates on default 1220px launch (src/kirigami_ui/main.qml:54)
- **deepseek:** ✅ LEGIT (90) — main.qml:54 77: mobileOrSmallScreen threshold 1231px vs default width 1220px; every fresh launch starts in mobile/compact toolbar mode
- **glm:** ✅ LEGIT (70) — main.qml:54 77 mobileOrSmallScreen threshold at 1231px activates on default 1220px launch
- **kimi:** ✅ LEGIT (85) — main.qml:54 mobileOrSmallScreen is true for root.width<1231; default width is 1220 (main.qml:77)
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — mobileOrSmallScreen 1231px vs 1220px launch; heuristic threshold (main.qml:54)

### [RND-N02] Missing smooth: true on background Image — aliased upscale  ·  _SPLIT_  ·  Low
`PrompterBackground.qml:79-87`
- **opus:** ⚠️ PARTIAL (45) — missing smooth:true on background Image (PrompterBackground.qml:79)
- **gpt:** ⚠️ PARTIAL (58) — observed Missing smooth: true on background Image - aliased upscale (src/prompter/PrompterBackground.qml:79)
- **deepseek:** ✅ LEGIT (85) — PrompterBackground.qml:79-87: Image with PreserveAspectCrop fillMode lacks smooth:true; nearest-neighbor scaling
- **glm:** ✅ LEGIT (70) — PrompterBackground.qml:79-87 missing smooth: true on background Image; aliased upscale
- **kimi:** ✅ LEGIT (85) — PrompterBackground.qml:79-88 Image with PreserveAspectCrop lacks `smooth: true`; nearest upscale is policy, but claim of aliasing is verified.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — missing smooth:true on background Image (PrompterBackground.qml:79)

### [RND-N03] Missing smooth: true on projection Image — aliased text on external displays  ·  _SPLIT_  ·  Low
`ProjectionsManager.qml:284-304`
- **opus:** ⚠️ PARTIAL (50) — missing smooth:true on projection Image; aliased (ProjectionsManager.qml:284)
- **gpt:** ⚠️ PARTIAL (58) — observed Missing smooth: true on projection Image - aliased text on external displays (src/prompter/ProjectionsManager.qml:284)
- **deepseek:** ✅ LEGIT (85) — ProjectionsManager.qml:284-304: projection Image lacks smooth:true; text aliased on scaled external displays
- **glm:** ✅ LEGIT (70) — ProjectionsManager.qml:284-304 missing smooth: true on projection Image; aliased text
- **kimi:** ✅ LEGIT (80) — ProjectionsManager.qml:284-304 projection Image lacks `smooth: true`; scaling with nearest filter causes aliasing.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — missing smooth:true on projection Image; aliased (ProjectionsManager.qml:284)

### [RPM-N01] RPM dependencies entirely commented out — zero automatic dependency resolution  ·  _SPLIT_  ·  Medium
`CMakeLists.txt:450`
- **opus:** ✅ LEGIT (50) — RPM dependencies entirely commented out (CMakeLists.txt:450)
- **gpt:** ⚠️ PARTIAL (58) — observed RPM dependencies entirely commented out - zero automatic dependency resolution (CMakeLists.txt:450)
- **deepseek:** ✅ LEGIT (90) — CMakeLists.txt:450: CPACK_RPM_PACKAGE_REQUIRES entirely commented out; generated RPMs have empty Requires; dnf installs without Qt/KDE
- **glm:** ✅ LEGIT (75) — CMakeLists.txt:450 RPM dependencies entirely commented out; zero automatic dependency resolution
- **kimi:** ✅ LEGIT (95) — CMakeLists.txt:450 CPACK_RPM_PACKAGE_REQUIRES is commented out; RPM gets no automatic deps
- **opus-ultra:** ✅ LEGIT (50) — RPM dependencies entirely commented out (CMakeLists.txt:450)

### [SAFE-01] +android/main.qml zero safe area insets  ·  _SPLIT_  ·  Medium
`+android/main.qml`
- **opus:** ⚠️ PARTIAL (45) — +android no safe-area insets; notch handling (main.qml)
- **gpt:** ⚠️ PARTIAL (58) — observed +android/main.qml zero safe area insets (src/kirigami_ui/+android/main.qml:1)
- **deepseek:** ✅ LEGIT (80) — +android/main.qml full-screen — zero safe area margins for notch/gesture pill
- **glm:** ✅ LEGIT (80) — +android/main.qml no safe area insets for notch/status bar
- **kimi:** ✅ LEGIT (75) — +android/main.qml applies no safe-area margins; content can be hidden by notch or gesture bar.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — +android no safe-area insets; notch handling (main.qml)

### [SAFE-02] ReadRegionOverlay screenMiddle ignores notch/status bar height  ·  _SPLIT_  ·  Medium
`ReadRegionOverlay.qml:132-134`
- **opus:** ⚠️ PARTIAL (45) — screenMiddle ignores notch/status bar (ReadRegionOverlay.qml:132)
- **gpt:** ⚠️ PARTIAL (58) — observed ReadRegionOverlay screenMiddle ignores notch/status bar height (src/prompter/ReadRegionOverlay.qml:132)
- **deepseek:** ✅ LEGIT (80) — screenMiddle at ReadRegionOverlay.qml:132 uses raw screen.height — ignores notch/status bar
- **glm:** ✅ LEGIT (75) — ReadRegionOverlay.qml:132-134 screenMiddle ignores notch/status bar height
- **kimi:** ✅ LEGIT (75) — ReadRegionOverlay.qml:132-134 computes screenMiddle from raw screen.height without accounting for status-bar/notch offset.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — screenMiddle ignores notch/status bar (ReadRegionOverlay.qml:132)

### [SAVE-N01] loadFromNetworkFinihed sets m_fileUrl to phantom QTemporaryFile path  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:897,144`
- **opus:** ⚠️ PARTIAL (55) — network doc m_fileUrl set to QTemporaryFile path (documenthandler.cpp:897)
- **gpt:** ✅ LEGIT (78) — loadFromNetworkFinihed sets m_fileUrl to phantom QTemporaryFile path (src/documenthandler.cpp:897)
- **deepseek:** ✅ LEGIT (70) — network docs set m_fileUrl to QTemporaryFile path not source network URL (documenthandler.cpp:897)
- **glm:** ✅ LEGIT (80) — documenthandler.cpp:897 144 loadFromNetworkFinihed sets m_fileUrl to m_cache->fileName() (QTemporaryFile path)
- **kimi:** ✅ LEGIT (80) — loadFromNetworkFinihed assigns m_cache->fileName() to m_fileUrl at documenthandler.cpp:897, so fileUrl points to a temporary cache.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — network doc m_fileUrl set to QTemporaryFile path (documenthandler.cpp:897)

### [SAVE-N02] iOS save flow never updates C++ m_fileUrl — file URL perpetually stale  ·  _SPLIT_  ·  High
`Prompter.qml:2493-2506, iossavedialog.mm:36-46`
- **opus:** ⚠️ PARTIAL (50) — iOS onAccepted doesn't refresh C++ m_fileUrl; domain (Prompter.qml:2493)
- **gpt:** ✅ LEGIT (84) — iOS save flow never updates C++ m_fileUrl - file URL perpetually stale (src/prompter/Prompter.qml:2493)
- **deepseek:** ✅ LEGIT (75) — iOS save flow in QML never calls C++ method to update m_fileUrl (Prompter.qml:2493-2506)
- **glm:** ✅ LEGIT (80) — Prompter.qml:2493-2506 iOS save flow never updates C++ m_fileUrl; file URL perpetually stale
- **kimi:** ✅ LEGIT (85) — iOS save Connections onAccepted (Prompter.qml:2493-2506) never assigns the returned fileUrl back to document; m_fileUrl stays stale.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — iOS onAccepted doesn't refresh C++ m_fileUrl; domain (Prompter.qml:2493)

### [SAVE-N04] save() unnecessary QString→std::string→QString round-trip through locale encoding  ·  _SPLIT_  ·  Low
`documenthandler.cpp:1183`
- **opus:** ⚠️ PARTIAL (45) — save() needless QString->std::string->QString round-trip (documenthandler.cpp:1183)
- **gpt:** ✅ LEGIT (78) — save() unnecessary QString->std::string->QString round-trip through locale encoding (src/documenthandler.cpp:1183)
- **deepseek:** ✅ LEGIT (65) — unnecessary QString->std::string->QString round-trip via locale encoding (documenthandler.cpp:1183)
- **glm:** ✅ LEGIT (75) — documenthandler.cpp:1183 unnecessary QString→std::string→QString round-trip through locale encoding
- **kimi:** ✅ LEGIT (70) — save() at documenthandler.cpp:1183 round-trips the percent-encoded path through toStdString/fromStdString; redundant and encoding-risky.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — save() needless QString->std::string->QString round-trip (documenthandler.cpp:1183)

### [SCALE-N01] Right pointer xScale: -1 mirrors text pointers — backwards/unreadable text  ·  _SPLIT_  ·  Medium
`ReadRegionOverlay.qml:391-398`
- **opus:** ⚠️ PARTIAL (50) — right pointer xScale:-1 mirrors text; domain (ReadRegionOverlay.qml:391)
- **gpt:** ✅ LEGIT (78) — Right pointer xScale: -1 mirrors text pointers - backwards/unreadable text (src/prompter/ReadRegionOverlay.qml:391)
- **deepseek:** ✅ LEGIT (65) — right pointer xScale:-1 mirrors Arrow/sameAsLeft text making it backwards (ReadRegionOverlay.qml:391-398)
- **glm:** ✅ LEGIT (75) — ReadRegionOverlay.qml:391-398 right pointer xScale:-1 mirrors text; backwards/unreadable text
- **kimi:** ✅ LEGIT (80) — ReadRegionOverlay.qml:391-398 applies Scale xScale:-1 to Text pointers, mirroring text and making it unreadable.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — right pointer xScale:-1 mirrors text; domain (ReadRegionOverlay.qml:391)

### [SCR-N01] Per-screen projection flip settings lost on restart — never serialized  ·  _SPLIT_  ·  High
`ProjectionsManager.qml:39,168-173`
- **opus:** ❔ UNSURE (45) — per-screen flip persistence; ties to R4-PRJ-02 snapshot issue (ProjectionsManager.qml:39)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/ProjectionsManager.qml:39)
- **deepseek:** ✅ LEGIT (90) — screensStringified Settings alias commented out at ProjectionsManager.qml:172; per-screen flip config never persisted across restart
- **glm:** ✅ LEGIT (70) — ProjectionsManager.qml:39 168-173 per-screen projection flip settings lost on restart; never serialized
- **kimi:** ✅ LEGIT (90) — ProjectionsManager.qml:168-174 Settings only saves isEnabled and reScale; per-screen flipSetting is never persisted
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — per-screen flip persistence; ties to R4-PRJ-02 snapshot issue (ProjectionsManager.qml:39)

### [SCR-N03] No runtime screen plug/unplug handling — stale projection windows on disconnected screens  ·  _SPLIT_  ·  Medium
`ProjectionsManager.qml:157-166`
- **opus:** ⚠️ PARTIAL (50) — no runtime screen plug/unplug handling (ProjectionsManager.qml:157)
- **gpt:** ⚠️ PARTIAL (58) — observed No runtime screen plug/unplug handling - stale projection windows on disconnected screens (src/prompter/ProjectionsManager.qml:157)
- **deepseek:** ✅ LEGIT (85) — ProjectionsManager.qml:157-166: no connection to screenAdded/screenRemoved signals; monitor hotplug requires manual toggle to refresh
- **glm:** ✅ LEGIT (65) — ProjectionsManager.qml:157-166 no runtime screen plug/unplug handling; stale projection windows on disconnected screens
- **kimi:** ✅ LEGIT (85) — ProjectionsManager.qml has no screenAdded/screenRemoved handlers; projections become stale on monitor hotplug
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — no runtime screen plug/unplug handling (ProjectionsManager.qml:157)

### [SCRL-N01] __jitterMargin: fractional result from modulus violates 0/1 toggle design  ·  _SPLIT_  ·  Medium
`Prompter.qml:114`
- **opus:** ❔ UNSURE (45) — __jitterMargin fractional from modulus; scroll-toggle design claim (Prompter.qml:114)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Prompter.qml:114)
- **deepseek:** ⚠️ PARTIAL (50) — modulus on mixed int/real types yields fractional; depends on jitter design intent (Prompter.qml:114)
- **glm:** ⚠️ PARTIAL (60) — Prompter.qml:114 __jitterMargin fractional result from modulus violates 0/1 toggle design
- **kimi:** ✅ LEGIT (80) — Prompter.qml:114 __jitterMargin uses %2 on real operands; with __tikTok stuck at 0 the remainder is a static offset instead of a toggling 0/1 subpixel jitter
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — __jitterMargin fractional from modulus; scroll-toggle design claim (Prompter.qml:114)

### [SCRL-N02] __destination typed int truncates real-valued position  ·  _SPLIT_  ·  Medium
`Prompter.qml:125`
- **opus:** ⚠️ PARTIAL (50) — __destination int truncates real position; sub-pixel (Prompter.qml:125)
- **gpt:** ⚠️ PARTIAL (58) — observed destination typed int truncates real-valued position (src/prompter/Prompter.qml:125)
- **deepseek:** ✅ LEGIT (65) — real-valued destination assigned to int property truncates sub-pixel position (Prompter.qml:125)
- **glm:** ✅ LEGIT (75) — Prompter.qml:125 __destination typed int truncates real-valued position
- **kimi:** ✅ LEGIT (90) — Prompter.qml:125 __destination is declared int but RHS uses real editor.height/fontSize/topMargin, truncating subpixel animation targets
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — __destination int truncates real position; sub-pixel (Prompter.qml:125)

### [SCRL-N03] setVelocity() triggers two conflicting scroll animations with intermediate velocity  ·  _SPLIT_  ·  Medium
`Prompter.qml:605-613`
- **opus:** ❔ UNSURE (45) — setVelocity two conflicting animations; domain (Prompter.qml:605)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Prompter.qml:605)
- **deepseek:** ✅ LEGIT (55) — setVelocity sets position to __destination twice with __i changed between stmts causing two scrolls (Prompter.qml:605-613)
- **glm:** ✅ LEGIT (75) — Prompter.qml:605-613 setVelocity triggers two conflicting scroll animations with intermediate velocity
- **kimi:** ✅ LEGIT (95) — setVelocity sets __i=velocity-1, assigns position=__destination, then __i=velocity and assigns position=__destination at Prompter.qml:605-611; animation retargets mid-flight.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — setVelocity two conflicting animations; domain (Prompter.qml:605)

### [SEC-04] SSRF / URL Injection — User-Controlled URL Passed to Network Loader  ·  _SPLIT_  ·  High
`src/documenthandler.cpp:867-886, src/kirigami_ui/PrompterPage.qml:1277-1291`
- **opus:** ⚠️ PARTIAL (55) — user-initiated load; SSRF framing weak but host/path bug real (documenthandler.cpp:873)
- **gpt:** ⚠️ PARTIAL (58) — observed SSRF / URL Injection - User-Controlled URL Passed to Network Loader (src/documenthandler.cpp:867)
- **deepseek:** ✅ LEGIT (85) — Relative URL path becomes host at doc.cpp:873; user-supplied URL like 'localhost:4455' -> HTTP GET to internal service — genuine SSRF vector
- **glm:** ✅ LEGIT (85) — documenthandler.cpp:867-886 loadFromNetwork takes user-controlled URL and passes it to QNetworkAccessManager without validation
- **kimi:** ✅ LEGIT (90) — documenthandler.cpp:867-886 treats relative URL host as url.path() allowing requests to internal IPs; no whitelist.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — user-initiated load; SSRF framing weak but host/path bug real (documenthandler.cpp:873)

### [SEC-05] User-Controlled Filename Passed to QProcess (LibreOffice import)  ·  _SPLIT_  ·  Medium
`src/documenthandler.cpp:1076-1077`
- **opus:** ⚠️ PARTIAL (55) — filename to LibreOffice args; flag injection minor (documenthandler.cpp:1076)
- **gpt:** ⚠️ PARTIAL (58) — observed User-Controlled Filename Passed to QProcess (LibreOffice import) (src/documenthandler.cpp:1076)
- **deepseek:** ✅ LEGIT (70) — User-controlled fileName appended to QProcess args at doc.cpp:1076-1077; file named --help.odt would inject flags into LibreOffice — flag injection confirmed
- **glm:** ⚠️ PARTIAL (70) — documenthandler.cpp:1076-1077 filename passed to QProcess but it comes from user file dialog not arbitrary input
- **kimi:** ✅ LEGIT (85) — documenthandler.cpp:1076-1077 appends user-supplied filename to LibreOffice QProcess args enabling flag injection.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — filename to LibreOffice args; flag injection minor (documenthandler.cpp:1076)

### [SET-01] macOS/iOS: QSettings split across two preference domains  ·  _SPLIT_  ·  High
`documenthandler.cpp, globalhotkeys.cpp`
- **opus:** ⚠️ PARTIAL (45) — macOS/iOS QSettings uses different domain combo but consistent within platform
- **gpt:** ✅ LEGIT (84) — macOS/iOS: QSettings split across two preference domains (src/documenthandler.cpp:132)
- **deepseek:** ✅ LEGIT (90) — C++ QSettings uses organizationDomain() (com.cuperino.qprompt) QML uses default (Cuperino/qprompt) — split domains
- **glm:** ⚠️ PARTIAL (65) — documenthandler.cpp globalhotkeys.cpp macOS/iOS QSettings split across organizationDomain vs organizationName
- **kimi:** ✅ LEGIT (90) — main.cpp sets orgDomain=com.cuperino.qprompt; C++ uses organizationDomain on macOS/iOS while QML Settings use organizationName, splitting domains.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — macOS/iOS QSettings uses different domain combo but consistent within platform

### [SET-02] factoryReset() incomplete on macOS/iOS — domain-path settings survive  ·  _SPLIT_  ·  High
`qmlutil.hpp:135-137`
- **opus:** ❔ UNSURE (45) — factoryReset default QSettings; appName already lowercase so likely matches (qmlutil.hpp:135)
- **gpt:** ✅ LEGIT (84) — factoryReset() incomplete on macOS/iOS - domain-path settings survive (src/qmlutil.hpp:135)
- **deepseek:** ✅ LEGIT (90) — factoryReset() at qmlutil.hpp:135 clears only default QSettings domain — C++ domain settings survive
- **glm:** ✅ LEGIT (80) — qmlutil.hpp:135-137 factoryReset() calls settings.clear() which only clears default domain; domain-path settings survive on macOS/iOS
- **kimi:** ✅ LEGIT (90) — qmlutil.hpp:135 factoryReset only clears default QSettings domain; C++ settings in organizationDomain survive.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — factoryReset default QSettings; appName already lowercase so likely matches (qmlutil.hpp:1

### [SETUP-N01] setup.sh uses windeployqt.exe (Qt 5) — should be windeployqt6.exe (Qt 6)  ·  _SPLIT_  ·  Medium
`setup.sh:233`
- **opus:** ❔ UNSURE (40) — setup.sh windeployqt; Qt6 tool is still 'windeployqt' not '6' (setup.sh:233)
- **gpt:** ❔ UNSURE (39) — Qt 6 still ships windeployqt, so the tool name alone is not wrong (setup.sh:233)
- **deepseek:** ✅ LEGIT (95) — setup.sh:233: windeployqt.exe is Qt5 tool; Qt6 ships windeployqt6.exe — on Qt6-only machines tool not found mixed Qt5+6 deploys wrong DLLs
- **glm:** ✅ LEGIT (75) — setup.sh:233 uses windeployqt.exe (Qt 5) instead of windeployqt6.exe (Qt 6)
- **kimi:** ✅ LEGIT (90) — setup.sh:235 invokes windeployqt.exe but Qt6 project should use windeployqt6.exe.
- **opus-ultra:** ❔ UNSURE (40) — max: unverifiable statically (runtime/semantic) — setup.sh windeployqt; Qt6 tool is still 'windeployqt' not '6' (setup.sh:233)

### [SHAPE-N02] concentricCircles Shape uses parent-space coordinates in local space — circles off-center  ·  _SPLIT_  ·  Medium
`Countdown.qml:202-239`
- **opus:** ❔ UNSURE (45) — concentricCircles parent-space coords; domain (Countdown.qml:202)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Countdown.qml:202)
- **deepseek:** ✅ LEGIT (85) — offsetCentre/prompter.centreY parent-space(~640px) in Shape local coords(84px); circles render far offscreen at Countdown.qml:202-239
- **glm:** ✅ LEGIT (70) — Countdown.qml:202-239 concentricCircles Shape uses parent-space coordinates in local space; circles off-center
- **kimi:** ✅ LEGIT (75) — Countdown.qml:202-239 concentricCircles Shape anchors centerIn parent but computes arc centers in overlay coordinates
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — concentricCircles parent-space coords; domain (Countdown.qml:202)

### [SHT-N01] markerToggle/namedMarkerToggle forwarded but never handled — dead hotkeys  ·  _SPLIT_  ·  Medium
`Prompter.qml:2097-2098,2118,2672-2870`
- **opus:** ⚠️ PARTIAL (50) — markerToggle/namedMarkerToggle forwarded but unhandled (Prompter.qml:2097)
- **gpt:** ⚠️ PARTIAL (58) — observed markerToggle/namedMarkerToggle forwarded but never handled - dead hotkeys (src/prompter/Prompter.qml:2097)
- **deepseek:** ✅ LEGIT (90) — Prompter.qml:2097-2098 editor forwards markerToggle/namedMarkerToggle to prompter.Keys.onPressed:2672-2870 which never handles either key
- **glm:** ✅ LEGIT (70) — Prompter.qml:2097-2098 2118 2672-2870 markerToggle/namedMarkerToggle forwarded but never handled; dead hotkeys
- **kimi:** ✅ LEGIT (90) — Prompter.qml:2097-2118 forwards markerToggle/namedMarkerToggle, but Prompter Keys.onPressed never handles them
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — markerToggle/namedMarkerToggle forwarded but unhandled (Prompter.qml:2097)

### [SHT-N02] Missing StandardKey.FullScreen on Android  ·  _SPLIT_  ·  Low
`+android/main.qml (absent from base:523 and +windows:494)`
- **opus:** ⚠️ PARTIAL (45) — missing StandardKey.FullScreen on Android (main.qml:523)
- **gpt:** ⚠️ PARTIAL (58) — observed Missing StandardKey.FullScreen on Android (src/kirigami_ui/+android/main.qml:1)
- **deepseek:** ⚠️ PARTIAL (75) — Android missing StandardKey.FullScreen vs base/windows but Android OS manages fullscreen natively — may be intentional
- **glm:** ✅ LEGIT (65) — +android/main.qml missing StandardKey.FullScreen absent from base:523 and +windows:494
- **kimi:** ✅ LEGIT (75) — +android/main.qml:390-428 has StandardKey.Cancel but no StandardKey.FullScreen action present in base/+windows
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — missing StandardKey.FullScreen on Android (main.qml:523)

### [SIG-N03] MessageDialog.onButtonClicked declares unused second parameter role  ·  _SPLIT_  ·  Low
`main.qml:1088, +windows:757,777,797, +android:681,701`
- **opus:** ⚠️ PARTIAL (40) — MessageDialog.onButtonClicked unused 2nd param; harmless (main.qml:1088)
- **gpt:** ✅ LEGIT (78) — MessageDialog.onButtonClicked declares unused second parameter role (src/kirigami_ui/main.qml:1088)
- **deepseek:** ✅ LEGIT (75) — main.qml:1088 +windows:757 777 797 +android:681 701: MessageDialog buttonClicked signal has 1 param (StandardButton) but handlers declare (button role) — role always undefined
- **glm:** ✅ LEGIT (70) — main.qml:1088 MessageDialog.onButtonClicked declares unused second parameter role
- **kimi:** ✅ LEGIT (70) — main.qml:1088, +windows:757, +android:681 MessageDialog.onButtonClicked handlers declare (button, role) but signal has one parameter.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — MessageDialog.onButtonClicked unused 2nd param; harmless (main.qml:1088)

### [SPL2-18] Hunspell::add return value unchecked at 4 call sites  ·  _SPLIT_  ·  Low
`spellchecker.cpp:139,173,179,321`
- **opus:** ✅ LEGIT (55) — Hunspell::add return unchecked at 4 sites (spellchecker.cpp:139)
- **gpt:** ✅ LEGIT (88) — Hunspell::add return value unchecked at 4 call sites (src/spellchecker.cpp:139)
- **deepseek:** ✅ LEGIT (85) — Hunspell::add return unchecked at 139 173 179 321; failed word additions silent (spellchecker.cpp:139 173 179 321)
- **glm:** ⚠️ PARTIAL (65) — spellchecker.cpp:139 173 179 321 Hunspell::add return value unchecked; failures silently ignored
- **kimi:** ✅ LEGIT (75) — spellchecker.cpp:139/173/179/321 call Hunspell::add and ignore the returned status.
- **opus-ultra:** ✅ LEGIT (55) — Hunspell::add return unchecked at 4 sites (spellchecker.cpp:139)

### [ST-N02] Dead overlay.state PropertyChanges — overlay has no states array  ·  _SPLIT_  ·  Medium
`ReadRegionOverlay.qml:34-37, Prompter.qml:2899-3032`
- **opus:** ✅ LEGIT (50) — dead overlay.state PropertyChanges; overlay has no states (ReadRegionOverlay.qml:34)
- **gpt:** ⚠️ PARTIAL (58) — observed Dead overlay.state PropertyChanges - overlay has no states array (src/prompter/ReadRegionOverlay.qml:34)
- **deepseek:** ✅ LEGIT (95) — ReadRegionOverlay.qml:34-37 has enum States but no states: array; Prompter.qml:2899 overlay.state PropertyChanges is dead property assignment
- **glm:** ✅ LEGIT (70) — ReadRegionOverlay.qml:34-37 Prompter.qml:2899-3032 dead overlay.state PropertyChanges; overlay has no states array
- **kimi:** ✅ LEGIT (85) — ReadRegionOverlay.qml:34 defines States enum but no `states:` array; Prompter.qml:2899-2900/2934 PropertyChanges target overlay.state are no-ops.
- **opus-ultra:** ✅ LEGIT (50) — dead overlay.state PropertyChanges; overlay has no states (ReadRegionOverlay.qml:34)

### [STATE-N02] Find.toggle() uses !visible instead of !isOpen — can't close during Prompting  ·  _SPLIT_  ·  Medium
`Find.qml:51`
- **opus:** ⚠️ PARTIAL (50) — toggle() uses !visible vs !isOpen; can desync (Find.qml:51)
- **gpt:** ✅ LEGIT (78) — Find.toggle() uses !visible instead of !isOpen - can't close during Prompting (src/prompter/Find.qml:51)
- **deepseek:** ✅ LEGIT (75) — toggle() uses !visible which desyncs from isOpen state machine flag (Find.qml:51)
- **glm:** ✅ LEGIT (80) — Find.qml:51 toggle() uses !visible instead of !isOpen; can't close during Prompting
- **kimi:** ✅ LEGIT (80) — Find.toggle() uses visible (derived from height) instead of isOpen; during Prompting height is forced 0 so toggle cannot close the bar.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — toggle() uses !visible vs !isOpen; can desync (Find.qml:51)

### [STATE-N03] Countdown Running restarts dissolveIn unnecessarily — visual dim-to-bright flash  ·  _SPLIT_  ·  Low
`Countdown.qml:289`
- **opus:** ⚠️ PARTIAL (50) — Running re-runs dissolveIn; visual flash (Countdown.qml:289)
- **gpt:** ✅ LEGIT (78) — Countdown Running restarts dissolveIn unnecessarily - visual dim-to-bright flash (src/prompter/Countdown.qml:289)
- **deepseek:** ✅ LEGIT (65) — Running state always restarts dissolveIn when re-entered causing visual flash (Countdown.qml:289)
- **glm:** ⚠️ PARTIAL (60) — Countdown.qml:289 Running restarts dissolveIn unnecessarily; visual dim-to-bright flash
- **kimi:** ✅ LEGIT (80) — Countdown.qml:289 sets dissolveIn.running=true after Ready state already set it; causes a 1->0->1 opacity flicker.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — Running re-runs dissolveIn; visual flash (Countdown.qml:289)

### [STATE-N04] loop animation cancel() state change overridden by toggle() due to QML batching  ·  _SPLIT_  ·  Low
`Prompter.qml:900-907`
- **opus:** ❔ UNSURE (45) — loop cancel() vs toggle() QML batching; domain (Prompter.qml:900)
- **gpt:** ✅ LEGIT (78) — loop animation cancel() state change overridden by toggle() due to QML batching (src/prompter/Prompter.qml:900)
- **deepseek:** ✅ LEGIT (70) — cancel() then toggle() in same ScriptAction batch; QML batching may override cancel (Prompter.qml:900-907)
- **glm:** ⚠️ PARTIAL (55) — Prompter.qml:900-907 loop animation cancel() state change overridden by toggle() due to QML batching
- **kimi:** ✅ LEGIT (75) — Prompter.qml:900-907 ScriptAction calls cancel() then toggle() together, risking QML batching overriding the cancel state.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — loop cancel() vs toggle() QML batching; domain (Prompter.qml:900)

### [STC-N01] closeAll() destroys user's per-screen projection flip configuration  ·  _SPLIT_  ·  Medium
`ProjectionsManager.qml:130-132`
- **opus:** ✅ LEGIT (55) — closeAll() displayModel.clear() wipes per-screen flip config (ProjectionsManager.qml:130)
- **gpt:** ⚠️ PARTIAL (58) — observed closeAll() destroys user's per-screen projection flip configuration (src/prompter/ProjectionsManager.qml:130)
- **deepseek:** ✅ LEGIT (90) — ProjectionsManager.qml:130-132: closeAll clears displayModel holding per-screen flipSetting values; toggling projections off discards all custom config
- **glm:** ✅ LEGIT (70) — ProjectionsManager.qml:130-132 closeAll() destroys user's per-screen projection flip configuration
- **kimi:** ✅ LEGIT (90) — ProjectionsManager.qml:130 closeAll() clears displayModel, destroying per-screen flip configuration
- **opus-ultra:** ✅ LEGIT (55) — closeAll() displayModel.clear() wipes per-screen flip config (ProjectionsManager.qml:130)

### [STC-N04] Projection window CursorAutoHide not reset on close — cursor permanently hidden  ·  _SPLIT_  ·  Medium
`ProjectionsManager.qml:202-206,196-200`
- **opus:** ⚠️ PARTIAL (50) — projection CursorAutoHide not reset on close (ProjectionsManager.qml:202)
- **gpt:** ⚠️ PARTIAL (58) — observed Projection window CursorAutoHide not reset on close - cursor permanently hidden (src/prompter/ProjectionsManager.qml:202)
- **deepseek:** ✅ LEGIT (85) — ProjectionsManager.qml:202-206 196-200: onClosing never calls cursorAutoHide.reset(); cursor stays hidden system-wide after window destruction
- **glm:** ✅ LEGIT (70) — ProjectionsManager.qml:202-206 196-200 projection window CursorAutoHide not reset on close; cursor permanently hidden
- **kimi:** ✅ LEGIT (75) — ProjectionsManager.qml:196-206 onClosing removes window without cursorAutoHide.reset(); hidden cursor may persist
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — projection CursorAutoHide not reset on close (ProjectionsManager.qml:202)

### [STC-N05] cancel() doesn't call timer.stopTimer() — elapsed time persists across sessions  ·  _SPLIT_  ·  Low
`Prompter.qml:460-466`
- **opus:** ⚠️ PARTIAL (50) — cancel() doesn't stopTimer(); elapsed persists (Prompter.qml:460)
- **gpt:** ⚠️ PARTIAL (58) — observed cancel() doesn't call timer.stopTimer() - elapsed time persists across sessions (src/prompter/Prompter.qml:460)
- **deepseek:** ✅ LEGIT (85) — Prompter.qml:432-435: cancel() sets state to Editing but doesn't call timer.stopTimer(); elapsed time persists across prompting sessions
- **glm:** ✅ LEGIT (65) — Prompter.qml:460-466 cancel() doesn't call timer.stopTimer(); elapsed time persists across sessions
- **kimi:** ✅ LEGIT (80) — Prompter.qml:432-435 cancel() enters Editing but never calls timer.stopTimer(); elapsed time carries over
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — cancel() doesn't stopTimer(); elapsed persists (Prompter.qml:460)

### [SYM-N01] 6 RTL/symmetry issues across PointerSettings, Find, PrompterView, Prompter, PrompterPage  ·  _SPLIT_  ·  Low-Medium
`PointerSettings.qml:380 (right pointer label not RTL-mirrored), Find.qml:63-66 (search bar always left-pinned), PrompterView.qml:74-76 (upper controls not RTL-aware), Prompter.qml:658-659 (goToNextMarker has end-fallback but goToPreviousMarker lacks start-fallback), PrompterPage.qml:266,278 (pointer tooltips not RTL-mirrored, contradict button labels)`
- **opus:** ⚠️ PARTIAL (40) — 6 RTL/symmetry issues (PointerSettings.qml:380)
- **gpt:** ⚠️ PARTIAL (58) — observed 6 RTL/symmetry issues across PointerSettings, Find, PrompterView, Prompter, PrompterPage (src/prompter/PointerSettings.qml:380)
- **deepseek:** ✅ LEGIT (85) — 6 RTL issues: PointerSettings.qml:380 label not mirrored; Find.qml:63-66 left-pinned; PrompterView.qml:74-76 not RTL-aware; Prompter.qml:658-659 one-sided fallback; PrompterPage.qml:266 tooltip not RTL-mirrored
- **glm:** ⚠️ PARTIAL (55) — 6 RTL/symmetry issues across PointerSettings Find PrompterView Prompter PrompterPage; mixed severity
- **kimi:** ✅ LEGIT (65) — Multiple files have RTL/symmetry issues; verified PointerSettings label, Find bar margin, PrompterView upper controls, goToPreviousMarker no start fallback, PrompterPage tooltip mismatch.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — 6 RTL/symmetry issues (PointerSettings.qml:380)

### [TAB-N01] PointerSettings TabButton onClicked skips currentIndex assignment  ·  _SPLIT_  ·  Medium
`PointerSettings.qml:268-289`
- **opus:** ⚠️ PARTIAL (50) — TabButton onClicked skips currentIndex assignment (PointerSettings.qml:268)
- **gpt:** ✅ LEGIT (78) — PointerSettings TabButton onClicked skips currentIndex assignment (src/prompter/PointerSettings.qml:268)
- **deepseek:** ⚠️ PARTIAL (60) — PointerSettings.qml:268-289: TabButtons set positionViewAtIndex but never TabBar.currentIndex; however TabBar.currentIndex is bound to pointerSettings.pointerKind at line 266
- **glm:** ✅ LEGIT (75) — PointerSettings.qml:268-289 TabButton onClicked skips currentIndex assignment
- **kimi:** ✅ LEGIT (80) — PointerSettings.qml:268-289 TabButton onClicked only calls positionViewAtIndex; currentIndex is bound to pointerKind so highlight does not update.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — TabButton onClicked skips currentIndex assignment (PointerSettings.qml:268)

### [TB-N01] toolbar toggle timers produce stale state on rapid clicks  ·  _SPLIT_  ·  Medium
`EditorToolbar.qml:816-851`
- **opus:** ⚠️ PARTIAL (45) — toggle timers stale state on rapid clicks (EditorToolbar.qml:816)
- **gpt:** ⚠️ PARTIAL (58) — observed toolbar toggle timers produce stale state on rapid clicks (src/kirigami_ui/EditorToolbar.qml:816)
- **deepseek:** ✅ LEGIT (85) — EditorToolbar.qml:816-851: 250ms delayed Timer toggles showFontSpacingOptions/showAnimationConfigOptions with stale pre-click state on rapid clicks
- **glm:** ✅ LEGIT (70) — EditorToolbar.qml:816-851 toolbar toggle timers produce stale state on rapid clicks
- **kimi:** ✅ LEGIT (80) — EditorToolbar.qml:821-851 toggles rely on 250 ms Timers; rapid clicks can fire timers into an inverted state
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — toggle timers stale state on rapid clicks (EditorToolbar.qml:816)

### [TB-N02] baseSpeedSlider/baseAccelerationSlider onMoved yanks focus to prompter instead of restoreFocus()  ·  _SPLIT_  ·  Medium
`EditorToolbar.qml:2009-2010,2128-2129`
- **opus:** ⚠️ PARTIAL (45) — slider onMoved yanks focus to prompter (EditorToolbar.qml:2009)
- **gpt:** ⚠️ PARTIAL (58) — observed baseSpeedSlider/baseAccelerationSlider onMoved yanks focus to prompter instead of restoreFocus( (src/kirigami_ui/EditorToolbar.qml:2009)
- **deepseek:** ✅ LEGIT (90) — EditorToolbar.qml:2009-2010 2128-2129: baseSpeed/AccelerationSlider onMoved sets viewport.prompter.focus=true instead of restoreFocus(); editor loses focus
- **glm:** ✅ LEGIT (70) — EditorToolbar.qml:2009-2010 2128-2129 baseSpeedSlider/baseAccelerationSlider onMoved yanks focus to prompter instead of restoreFocus()
- **kimi:** ✅ LEGIT (75) — EditorToolbar.qml:2009-2010 and :2128-2129 onMoved set prompter.focus=true instead of restoreFocus()
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — slider onMoved yanks focus to prompter (EditorToolbar.qml:2009)

### [TB-N03] Collapsible toolbar rows animate height but adjacent rows snap — no y-position animation  ·  _SPLIT_  ·  Low
`EditorToolbar.qml:1175-1906 (8 collapsible rows)`
- **opus:** ⚠️ PARTIAL (45) — collapsible rows animate height but neighbors snap (EditorToolbar.qml:1175)
- **gpt:** ⚠️ PARTIAL (58) — observed Collapsible toolbar rows animate height but adjacent rows snap - no y-position animation (src/kirigami_ui/EditorToolbar.qml:1175)
- **deepseek:** ✅ LEGIT (70) — EditorToolbar.qml: collapsible rows have Behavior on height but Flow recalculates siblings immediately; rows below snap without animation
- **glm:** ⚠️ PARTIAL (55) — EditorToolbar.qml:1175-1906 8 collapsible rows animate height but adjacent rows snap; no y-position animation
- **kimi:** ✅ LEGIT (65) — EditorToolbar collapsible rows animate height only; adjacent rows snap because no y-position animation is applied
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — collapsible rows animate height but neighbors snap (EditorToolbar.qml:1175)

### [TBND-N01] SpellHighlighter regex excludes combining diacritical marks — NFD text misspelled  ·  _SPLIT_  ·  Medium
`spellhighlighter.cpp:53-54`
- **opus:** ⚠️ PARTIAL (50) — highlighter regex excludes combining diacritics; NFD text (spellhighlighter.cpp:53)
- **gpt:** ⚠️ PARTIAL (58) — observed SpellHighlighter regex excludes combining diacritical marks - NFD text misspelled (src/spellhighlighter.cpp:53)
- **deepseek:** ✅ LEGIT (70) — Regex \p{L}+ excludes \p{M} combining marks; NFD text cafe->cafe without accent->incorrect spellcheck at spellhighlighter.cpp:53-54
- **glm:** ✅ LEGIT (70) — spellhighlighter.cpp:53-54 regex excludes combining diacritical marks; NFD text misspelled
- **kimi:** ✅ LEGIT (85) — spellhighlighter.cpp:53-54 wordRe matches \\p{L} only; combining diacritics split words
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — highlighter regex excludes combining diacritics; NFD text (spellhighlighter.cpp:53)

### [THM-SYS] Complete theme deadlock — 50+ Material.theme: Dark hardcoded, theme toggle commented out  ·  _SPLIT_  ·  High
`14 QML files`
- **opus:** ⚠️ PARTIAL (55) — 50+ hardcoded Material.theme:Dark means runtime theme toggle is effectively dead (multi-file)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/kirigami_ui/main.qml:122)
- **deepseek:** ✅ LEGIT (90) — Material.theme: Material.Dark hardcoded across ~50 controls in 14+ QML files; theme toggle commented out; no light mode support
- **glm:** ✅ LEGIT (70) — 14 QML files have Material.theme: Dark hardcoded; theme toggle commented out
- **kimi:** ✅ LEGIT (85) — Dozens of `Material.theme: Material.Dark` are hardcoded across QML files; theme toggle is commented out
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — 50+ hardcoded Material.theme:Dark means runtime theme toggle is effectively dead (multi-fi

### [THR-01] IosSaveDialog::create() — unsynchronized singleton race  ·  _SPLIT_  ·  Medium
`iossavedialog.cpp:37-42`
- **opus:** ⚠️ PARTIAL (45) — IosSaveDialog::create unsynchronized singleton race; single-threaded (iossavedialog.cpp:37)
- **gpt:** ⚠️ PARTIAL (58) — observed IosSaveDialog::create() - unsynchronized singleton race (src/iossavedialog.cpp:37)
- **deepseek:** ✅ LEGIT (82) — QML singleton create() runs on main thread; check-then-act pattern is sloppy but not currently racy (iossavedialog.cpp:37-42)
- **glm:** ⚠️ PARTIAL (65) — iossavedialog.cpp:37-42 create() singleton without synchronization; race condition
- **kimi:** ✅ LEGIT (85) — iossavedialog.cpp:39-40 checks !s_instance then assigns in create() with no mutex, creating a check-then-act race.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — IosSaveDialog::create unsynchronized singleton race; single-threaded (iossavedialog.cpp:37

### [THR-02] ShakeDetector::create() — identical unsynchronized singleton race  ·  _SPLIT_  ·  Medium
`shakedetector.cpp:38-43`
- **opus:** ⚠️ PARTIAL (45) — ShakeDetector::create singleton race (dup THR-01) (shakedetector.cpp:38)
- **gpt:** ⚠️ PARTIAL (58) — observed ShakeDetector::create() - identical unsynchronized singleton race (src/shakedetector.cpp:38)
- **deepseek:** ✅ LEGIT (82) — same QML singleton pattern as THR-01; main-thread creation no actual concurrency (shakedetector.cpp:38-43)
- **glm:** ⚠️ PARTIAL (65) — shakedetector.cpp:38-43 create() singleton without synchronization; race condition
- **kimi:** ✅ LEGIT (85) — shakedetector.cpp:40-41 checks !s_instance then assigns in create() with no mutex, same race as THR-01.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — ShakeDetector::create singleton race (dup THR-01) (shakedetector.cpp:38)

### [THR-03] search() — mutable static QRegularExpression shared across all callers  ·  _SPLIT_  ·  Low
`documenthandler.cpp:1543-1544`
- **opus:** ⚠️ PARTIAL (50) — static QRegularExpression shared/mutated; OK single-threaded (documenthandler.cpp:1543)
- **gpt:** ⚠️ PARTIAL (58) — observed search() - mutable static QRegularExpression shared across all callers (src/documenthandler.cpp:1543)
- **deepseek:** ✅ LEGIT (80) — mutable static QRegularExpression shared across calls; main-thread only currently no actual data race (documenthandler.cpp:1543-1544)
- **glm:** ✅ LEGIT (80) — documenthandler.cpp:1543-1544 static QRegularExpression shared across callers; thread-safety issue if called from multiple threads
- **kimi:** ✅ LEGIT (85) — documenthandler.cpp:1543-1544 uses static QRegularExpression searchRegEx and mutates its pattern across all callers, not thread-safe.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — static QRegularExpression shared/mutated; OK single-threaded (documenthandler.cpp:1543)

### [THR-04] SpellChecker zero thread safety — explicit finding  ·  _SPLIT_  ·  Medium
`spellchecker.h:76-77, spellchecker.cpp`
- **opus:** ⚠️ PARTIAL (45) — SpellChecker zero thread safety (dup R3-SPL-05) (spellchecker.h:76)
- **gpt:** ✅ LEGIT (78) — SpellChecker zero thread safety - explicit finding (src/spellchecker.h:76)
- **deepseek:** ⚠️ PARTIAL (72) — m_dicts+m_customWords no mutex; Qt6.7+ async QSyntaxHighlighter could cause concurrent spell/suggest vs mutate (spellchecker.h:76-77)
- **glm:** ✅ LEGIT (85) — spellchecker.h:76-77 all methods unprotected by mutex; zero thread safety
- **kimi:** ✅ LEGIT (85) — spellchecker.h:76-77 holds m_dicts and m_customWords with no mutex; all read/write methods are unprotected.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — SpellChecker zero thread safety (dup R3-SPL-05) (spellchecker.h:76)

### [TMR-01] Countdown→Prompting auto-transition via state++ bypasses toggle() entirely  ·  _SPLIT_  ·  High
`Countdown.qml:123`
- **opus:** ❔ UNSURE (50) — state++ bypasses toggle() side-effects (dup FINAL-16); state-machine claim (Countdown.qml:123)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Countdown.qml:123)
- **deepseek:** ✅ LEGIT (92) — prompter.state++ skips toggle():timer.reset document.parse preventSleep projections fix (Countdown.qml:123)
- **glm:** ✅ LEGIT (85) — Countdown.qml:123 state++ bypasses toggle() entry actions; direct state mutation skips transition
- **kimi:** ✅ LEGIT (95) — Countdown.qml:123 increments prompter.state++ directly, bypassing toggle() and its timer/parse/preventSleep side effects.
- **opus-ultra:** ❔ UNSURE (50) — max: unverifiable statically (runtime/semantic) — state++ bypasses toggle() side-effects (dup FINAL-16); state-machine claim (Countdown.qml:

### [TMR-02] timer.updateTimer() runs before timer.startTimer() on Prompting entry  ·  _SPLIT_  ·  Medium
`Prompter.qml:3093 vs :3113`
- **opus:** ❔ UNSURE (45) — updateTimer before startTimer on Prompting entry; domain (Prompter.qml:3093)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Prompter.qml:3093)
- **deepseek:** ✅ LEGIT (80) — updateTimer runs before startTimer in Prompting transition; computes elapsed with stale startTime (Prompter.qml:3093 vs 3113)
- **glm:** ✅ LEGIT (80) — Prompter.qml:3093 vs :3113 timer.updateTimer() runs before timer.startTimer() on Prompting entry
- **kimi:** ✅ LEGIT (85) — Prompter.qml:3093 timer.updateTimer() runs in onStateChanged before the Transition at :3113 calls timer.startTimer().
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — updateTimer before startTimer on Prompting entry; domain (Prompter.qml:3093)

### [TMR-03] dissolveIn animation re-triggered entering Running from Ready — flicker  ·  _SPLIT_  ·  Medium
`Countdown.qml:274-276,289-291`
- **opus:** ⚠️ PARTIAL (50) — dissolveIn re-triggered Ready->Running; flicker (Countdown.qml:274)
- **gpt:** ⚠️ PARTIAL (58) — observed dissolveIn animation re-triggered entering Running from Ready - flicker (src/prompter/Countdown.qml:274)
- **deepseek:** ✅ LEGIT (85) — dissolveIn.running:true in both Ready and Running states; Ready->Running restarts from 0 causing flicker (Countdown.qml:274-276 289-291)
- **glm:** ✅ LEGIT (75) — Countdown.qml:274-276 289-291 dissolveIn re-triggered entering Running from Ready; visual flicker
- **kimi:** ✅ LEGIT (85) — Countdown.qml:274-276 (Ready) and 289-291 (Running) both set dissolveIn.running=true, re-triggering it on Ready->Running.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — dissolveIn re-triggered Ready->Running; flicker (Countdown.qml:274)

### [TMR-04] Countdown arc hypotenuse uses geometric center instead of arc center  ·  _SPLIT_  ·  Low
`Countdown.qml:79`
- **opus:** ❔ UNSURE (45) — arc hypotenuse 1.4333 magic geometry (Countdown.qml:79)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Countdown.qml:79)
- **deepseek:** ✅ LEGIT (80) — hypotenuse uses prompter.centreX/Y but arc drawn at offsetCentre; radius mismatch when scrolled (Countdown.qml:79)
- **glm:** ⚠️ PARTIAL (60) — Countdown.qml:79 arc hypotenuse uses geometric center; cosmetic inaccuracy
- **kimi:** ✅ LEGIT (80) — Countdown.qml:79 computes __hypotenuse from prompter.centreX/Y, but the arc center at line 89 uses offsetCentre, so radius is wrong when editor is offset.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — arc hypotenuse 1.4333 magic geometry (Countdown.qml:79)

### [TMR-06] dissolveOut starts too early when disappearWithin > 1  ·  _SPLIT_  ·  Low
`Countdown.qml:110-113,145`
- **opus:** ❔ UNSURE (45) — dissolveOut early when disappearWithin>1; domain (Countdown.qml:110)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Countdown.qml:110)
- **deepseek:** ✅ LEGIT (85) — dissolveOut 1000ms duration starts disappearWithin-1 iterations early; visible text prematurely (Countdown.qml:110-113 145)
- **glm:** ⚠️ PARTIAL (60) — Countdown.qml:110-113 145 dissolveOut starts when __iterations===__disappearWithin-1; may be too early
- **kimi:** ✅ LEGIT (80) — Countdown.qml:110-113 starts dissolveOut at iteration disappearWithin-1; with disappearWithin>1 the 1000ms fade finishes before the countdown ends.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — dissolveOut early when disappearWithin>1; domain (Countdown.qml:110)

### [TMR-07] countdownAnimation restart uses non-idempotent running=true  ·  _SPLIT_  ·  Low
`Countdown.qml:119`
- **opus:** ✅ LEGIT (55) — countdownAnimation running=true imperative breaks binding (Countdown.qml:119)
- **gpt:** ⚠️ PARTIAL (58) — observed countdownAnimation restart uses non-idempotent running=true (src/prompter/Countdown.qml:119)
- **deepseek:** ⚠️ PARTIAL (65) — running=true on already-running animation; some Qt versions accept restart Qt Quick docs ambiguous (Countdown.qml:119)
- **glm:** ⚠️ PARTIAL (55) — Countdown.qml:119 countdownAnimation restart uses running=true; may not be idempotent
- **kimi:** ✅ LEGIT (75) — Countdown.qml:119 assigns running=true inside onFinished; re-starting an already-running animation is non-idempotent on some Qt builds.
- **opus-ultra:** ✅ LEGIT (55) — countdownAnimation running=true imperative breaks binding (Countdown.qml:119)

### [TMR-08] timer.running not explicitly set in Countdown state — relies on revert behavior  ·  _SPLIT_  ·  Low
`Prompter.qml:2980-3026`
- **opus:** ❔ UNSURE (45) — timer.running relies on state revert; domain (Prompter.qml:2980)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Prompter.qml:2980)
- **deepseek:** ✅ LEGIT (80) — timer.running not set in Countdown State(2980-3026); relies on revert; interrupted transition leaves stale (Prompter.qml:2980-3026)
- **glm:** ⚠️ PARTIAL (55) — Prompter.qml:2980-3026 timer.running not explicitly set; relies on PropertyChanges revert
- **kimi:** ✅ LEGIT (80) — Prompter.qml:2980-3026 Countdown state does not set timer.running; it relies on revert from the Prompting state.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — timer.running relies on state revert; domain (Prompter.qml:2980)

### [TMR-N01] resetBackground Timer not stopped when new background loaded — race erases new image  ·  _SPLIT_  ·  Medium
`PrompterBackground.qml:47-57,73-76`
- **opus:** ⚠️ PARTIAL (50) — resetBackground Timer not stopped on new bg; race (PrompterBackground.qml:47)
- **gpt:** ⚠️ PARTIAL (58) — observed resetBackground Timer not stopped when new background loaded - race erases new image (src/prompter/PrompterBackground.qml:47)
- **deepseek:** ✅ LEGIT (95) — PrompterBackground.qml:47-57/73-76: clearBackground() starts 2.8s resetBackground timer; setBackgroundImage() never stops it — race erases new image after ~2.8s
- **glm:** ✅ LEGIT (75) — PrompterBackground.qml:47-57 73-76 resetBackground Timer not stopped when new background loaded; race erases new image
- **kimi:** ✅ LEGIT (85) — PrompterBackground.qml:47-57,73-76 clearBackground starts 2.8s resetBackground timer; setBackgroundImage never stops it.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — resetBackground Timer not stopped on new bg; race (PrompterBackground.qml:47)

### [TMR-N02] Windows onFrameSwapped missing qmlutil.r(p) — per-frame grab result leak  ·  _SPLIT_  ·  Medium
`+windows/main.qml:706-716 vs main.qml:1036-1047`
- **opus:** ⚠️ PARTIAL (50) — +windows onFrameSwapped omits qmlutil.r(p); grab result not released (main.qml:706)
- **gpt:** ⚠️ PARTIAL (58) — observed Windows onFrameSwapped missing qmlutil.r(p) - per-frame grab result leak (src/kirigami_ui/+windows/main.qml:706)
- **deepseek:** ✅ LEGIT (90) — +windows/main.qml:706-716 vs main.qml:1036-1047: Windows variant missing qmlutil.r(p) call after grabToImage — per-frame QQuickItemGrabResult leak at 60fps
- **glm:** ✅ LEGIT (80) — +windows/main.qml:706-716 onFrameSwapped missing qmlutil.r(p) call present in base main.qml:1045; per-frame grab result leak
- **kimi:** ✅ LEGIT (85) — +windows/main.qml:706-716 onFrameSwapped grabToImage callback omits qmlutil.r(p) that base main.qml:1045 calls, leaking grab results.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — +windows onFrameSwapped omits qmlutil.r(p); grab result not released (main.qml:706)

### [TMR-N05] markerCompare() only fires on forward scroll — backward scroll + re-forward misses marker  ·  _SPLIT_  ·  High
`Prompter.qml:391-420`
- **opus:** ❔ UNSURE (45) — markerCompare forward-only claim; needs full function (Prompter.qml:391)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Prompter.qml:391)
- **deepseek:** ✅ LEGIT (90) — Prompter.qml:391-420: if(prompter.q<p) only triggers on forward scroll; after overshoot+backward q stays stale; re-forward q==p skips marker
- **glm:** ✅ LEGIT (75) — Prompter.qml:391-420 markerCompare() only fires on forward scroll; backward scroll + re-forward misses marker
- **kimi:** ⚠️ PARTIAL (70) — Prompter.qml:392 only acts when q<p (forward), but markerCompare is never actually invoked anywhere
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — markerCompare forward-only claim; needs full function (Prompter.qml:391)

### [TMR-N06] Auto-reload Timer persists after network dialog close — background refetches  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:1246-1253,1415-1420`
- **opus:** ⚠️ PARTIAL (50) — auto-reload Timer persists after network dialog close (PrompterPage.qml:1246)
- **gpt:** ✅ LEGIT (78) — Auto-reload Timer persists after network dialog close - background refetches (src/kirigami_ui/PrompterPage.qml:1246)
- **deepseek:** ✅ LEGIT (90) — PrompterPage.qml:1246-1253 1415-1420: onClosed doesn't set autoReloadRunning=false; Timer keeps firing openFromRemote() without visible UI
- **glm:** ✅ LEGIT (70) — PrompterPage.qml:1246-1253 1415-1420 auto-reload Timer persists after network dialog close; background refetches
- **kimi:** ✅ LEGIT (85) — PrompterPage.qml:1246-1264 autoReloadTimer depends on autoReloadRunning, never reset on dialog close
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — auto-reload Timer persists after network dialog close (PrompterPage.qml:1246)

### [TOG-N01] WheelSettingsOverlay useScrollAsDialButton — cross-path stale checked state  ·  _SPLIT_  ·  Medium
`WheelSettingsOverlay.qml:50-60`
- **opus:** ⚠️ PARTIAL (50) — useScrollAsDialButton cross-path stale checked (WheelSettingsOverlay.qml:50)
- **gpt:** ⚠️ PARTIAL (58) — observed WheelSettingsOverlay useScrollAsDialButton - cross-path stale checked state (src/kirigami_ui/WheelSettingsOverlay.qml:50)
- **deepseek:** ✅ LEGIT (85) — WheelSettingsOverlay.qml:50-60: checked: root.__scrollAsDial binding breaks on click; changing via 3 other paths leaves stale state
- **glm:** ✅ LEGIT (70) — WheelSettingsOverlay.qml:50-60 useScrollAsDialButton cross-path stale checked state
- **kimi:** ✅ LEGIT (80) — WheelSettingsOverlay.qml:54-55 checked binding is broken by the Button's own click toggle, leaving stale state from other paths
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — useScrollAsDialButton cross-path stale checked (WheelSettingsOverlay.qml:50)

### [TP-N01] "Error loading file..." used as document content, not placeholderText  ·  _SPLIT_  ·  Medium
`Prompter.qml:969`
- **opus:** ⚠️ PARTIAL (55) — 'Error loading file' shown as document content not placeholder (Prompter.qml:969)
- **gpt:** ⚠️ PARTIAL (58) — observed "Error loading file..." used as document content, not placeholderText (src/prompter/Prompter.qml:969)
- **deepseek:** ✅ LEGIT (90) — Prompter.qml:969: qsTr('Error loading file...') assigned as TextArea.text content not placeholderText; shows as editable document body
- **glm:** ✅ LEGIT (70) — Prompter.qml:969 'Error loading file...' used as document content not placeholderText
- **kimi:** ✅ LEGIT (80) — Prompter.qml:969 sets TextArea.text: qsTr('Error loading file…') as default initial text instead of placeholder.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — 'Error loading file' shown as document content not placeholder (Prompter.qml:969)

### [TP-SYS] Systemic absence of ToolTip on ~60+ controls across entire application  ·  _SPLIT_  ·  Medium
`Find.qml (8 buttons), EditorToolbar.qml (~28 buttons), PrompterView.qml (4 buttons), Prompter.qml (4 at-end buttons), MarkersDrawer (pin button), KeyInputButton (clear button), PrompterPage (~18 drawer actions)`
- **opus:** ⚠️ PARTIAL (40) — systemic absence of ToolTips; UX
- **gpt:** ⚠️ PARTIAL (58) — missing tooltip is a UX gap, not a functional failure (src/prompter/Find.qml:1)
- **deepseek:** ⚠️ PARTIAL (70) — Systemic absence of ToolTip across ~60 controls is accurate observation but subjective; some buttons use text labels; not a code defect per se
- **glm:** ✅ LEGIT (70) — ~60+ controls across entire application missing ToolTip; systemic absence
- **kimi:** ✅ LEGIT (75) — Source files show many ToolButtons/Actions with no tooltip; verified in Find.qml, EditorToolbar.qml, PrompterView.qml, PrompterPage.qml.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — systemic absence of ToolTips; UX

### [TRF-N01] rightWidthAdjustmentBar drag.maximumX formula broken — drag collapses to single point  ·  _SPLIT_  ·  High
`Prompter.qml:2022`
- **opus:** ⚠️ PARTIAL (50) — rightWidthAdjustmentBar maximumX collapses when minimumX>=maxX (Prompter.qml:2022)
- **gpt:** ⚠️ PARTIAL (58) — observed rightWidthAdjustmentBar drag.maximumX formula broken - drag collapses to single point (src/prompter/Prompter.qml:2022)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:2022: maxX=prompter.width-editor.x-parent.width-LM-13; with parent.width~=prompter.width: maxX ~= -editor.x-LM-13 < drag.minimumX always
- **glm:** ✅ LEGIT (75) — Prompter.qml:2022 rightWidthAdjustmentBar drag.maximumX formula broken; drag collapses to single point
- **kimi:** ✅ LEGIT (90) — Prompter.qml:2022 maxX simplifies to -editor.x-33, below minimumX -editor.x+20, collapsing the drag range
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — rightWidthAdjustmentBar maximumX collapses when minimumX>=maxX (Prompter.qml:2022)

### [TRL-N01] qsTr() uses %0 placeholder — should be %1 (font name never displayed)  ·  _SPLIT_  ·  High
`src/kirigami_ui/EditorToolbar.qml:588`
- **opus:** ⚠️ PARTIAL (55) — qsTr('Active font: %0'); %0 unconventional, Qt arg() handling uncertain (EditorToolbar.qml:588)
- **gpt:** ✅ LEGIT (84) — qsTr() uses %0 placeholder - should be %1 (font name never displayed) (src/kirigami_ui/EditorToolbar.qml:588)
- **deepseek:** ✅ LEGIT (95) — Qt arg() uses 1-based %1 %2; %0 treated as literal font name never displayed (EditorToolbar.qml:588)
- **glm:** ✅ LEGIT (85) — EditorToolbar.qml:588 qsTr uses %0 placeholder; should be %1; font name never displayed
- **kimi:** ✅ LEGIT (95) — EditorToolbar.qml:588 uses qsTr(\Active font: %0\"); Qt arg() requires 1-based %1
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — qsTr('Active font: %0'); %0 unconventional

### [TRL-N03] About-dialog credit roles not translatable  ·  _SPLIT_  ·  Medium
`src/main.cpp:194,202,205-206`
- **opus:** ⚠️ PARTIAL (45) — About credit roles not translatable (main.cpp:194)
- **gpt:** ✅ LEGIT (78) — About-dialog credit roles not translatable (src/main.cpp:194)
- **deepseek:** ✅ LEGIT (90) — credit roles use QLatin1String not tr(); About dialog always English (main.cpp:194 202 205-206)
- **glm:** ✅ LEGIT (80) — main.cpp:194 202 205-206 About dialog credit roles ('Author' 'Software Tester') not wrapped in tr()
- **kimi:** ✅ LEGIT (85) — main.cpp:194/202/205-206 use QStringLiteral for About-dialog credit roles/descriptions, not tr().
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — About credit roles not translatable (main.cpp:194)

### [TS-01] Finnish welcome guide → Dutch (not Finnish)  ·  _SPLIT_  ·  
`po/qprompt_fi.ts:656 — `welcome_nl.html` should be `welcome_fi.html``
- **opus:** ❔ UNSURE (40) — Finnish welcome -> Dutch html ref; translation/structural (qprompt_fi.ts:656)
- **gpt:** ⚠️ PARTIAL (58) — observed Finnish welcome guide -> Dutch (not Finnish) (po/qprompt_fi.ts:656)
- **deepseek:** ✅ LEGIT (88) — Finnish welcome_en.html->welcome_nl.html(Dutch) should be welcome_fi.html (po/qprompt_fi.ts:656)
- **glm:** ✅ LEGIT (85) — po/qprompt_fi.ts:656 Finnish translation has welcome_nl.html (Dutch) instead of welcome_fi.html
- **kimi:** ✅ LEGIT (95) — po/qprompt_fi.ts:656 translates welcome guide as welcome_nl.html instead of welcome_fi.html.
- **opus-ultra:** ❔ UNSURE (40) — max: unverifiable statically (runtime/semantic) — Finnish welcome -> Dutch html ref; translation/structural (qprompt_fi.ts:656)

### [TS-02] Arabic file `ar_EG` vs UI `ar_AE` mismatch  ·  _SPLIT_  ·  
`po/qprompt_ar.ts:3 — `language="ar_EG"` but LanguageSettingsOverlay.qml uses `ar_AE``
- **opus:** ⚠️ PARTIAL (50) — ar_EG file vs ar_AE UI locale mismatch; structural (qprompt_ar.ts:3)
- **gpt:** ⚠️ PARTIAL (58) — observed Arabic file arEG vs UI arAE mismatch (po/qprompt_ar.ts:3)
- **deepseek:** ✅ LEGIT (90) — Arabic .ts declares ar_EG but LanguageSettingsOverlay uses ar_AE; locale mismatch (po/qprompt_ar.ts:3)
- **glm:** ✅ LEGIT (85) — po/qprompt_ar.ts:3 language='ar_EG' but LanguageSettingsOverlay uses 'ar_AE'; locale code mismatch
- **kimi:** ✅ LEGIT (95) — po/qprompt_ar.ts:3 declares language ar_EG while LanguageSettingsOverlay.qml:83 offers ar_AE, mismatching the UI entry.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — ar_EG file vs ar_AE UI locale mismatch; structural (qprompt_ar.ts:3)

### [TS-04] French "Saved" → verb "Enregistrer" (should be adjective "Enregistré")  ·  _SPLIT_  ·  
`po/qprompt_fr.ts:679`
- **opus:** ❔ UNSURE (40) — French Saved verb-vs-adjective; semantic (qprompt_fr.ts:679)
- **gpt:** ❔ UNSURE (39) — semantic translation nuance needs French review (po/qprompt_fr.ts:679)
- **deepseek:** ✅ LEGIT (85) — French Saved->Enregistrer(verb to save) should be Enregistré(adjective saved) (po/qprompt_fr.ts:679)
- **glm:** ❔ UNSURE (50) — po/qprompt_fr.ts:679 'Enregistrer' could be verb or adjective depending on context; cannot verify without full context
- **kimi:** ✅ LEGIT (90) — po/qprompt_fr.ts:679 translates source \Saved\" as verb \"Enregistrer\" instead of adjective/past participle \"Enregistré\"."
- **opus-ultra:** ❔ UNSURE (40) — max: unverifiable statically (runtime/semantic) — French Saved verb-vs-adjective; semantic (qprompt_fr.ts:679)

### [TS-05] Finnish/French/Korean/Italian "Saved" → verb with stray `&amp;` accelerator  ·  _SPLIT_  ·  
`po/qprompt_fi.ts:678, po/qprompt_ko.ts:677, po/qprompt_it.ts:679`
- **opus:** ⚠️ PARTIAL (45) — stray &amp; accelerator in 'Saved'; structural (qprompt_fi.ts:678)
- **gpt:** ⚠️ PARTIAL (58) — observed Finnish/French/Korean/Italian "Saved" -> verb with stray &amp; accelerator (po/qprompt_fi.ts:678)
- **deepseek:** ✅ LEGIT (85) — Finnish Saved->&amp;Tallenna with stray &amp; accelerator; same in ko/it (po/qprompt_fi.ts:678)
- **glm:** ✅ LEGIT (80) — po/qprompt_fi.ts:678 etc have stray &amp; accelerator in 'Saved' translation; structural placeholder issue
- **kimi:** ✅ LEGIT (85) — po/qprompt_fi.ts:678, ko.ts:677 and it.ts:679 translate \Saved\" with a stray & accelerator not present in the source."
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — stray &amp; accelerator in 'Saved'; structural (qprompt_fi.ts:678)

### [TS-06] Czech/French "Language settings" → "Pointer settings" (copy-paste error)  ·  _SPLIT_  ·  
`po/qprompt_cs.ts:354, po/qprompt_fr.ts:353`
- **opus:** ❔ UNSURE (40) — Language settings->Pointer settings copy-paste; semantic (qprompt_cs.ts:354)
- **gpt:** ❔ UNSURE (39) — translation meaning cannot be verified from code alone (po/qprompt_cs.ts:354)
- **deepseek:** ✅ LEGIT (90) — Czech Language settings->Nastavení ukazatele(Pointer settings); copy-paste error (po/qprompt_cs.ts:354)
- **glm:** ❔ UNSURE (50) — po/qprompt_cs.ts:354 etc 'Pointer settings' may be copy-paste error; cannot verify Czech without language expertise
- **kimi:** ✅ LEGIT (90) — po/qprompt_cs.ts:354 and fr.ts:353 translate \Language settings\" as \"Pointer settings\" (copy-paste error)."
- **opus-ultra:** ❔ UNSURE (40) — max: unverifiable statically (runtime/semantic) — Language settings->Pointer settings copy-paste; semantic (qprompt_cs.ts:354)

### [TS-07] Finnish/French/Korean "Colors for prompter states" → "Toggle Prompter State"  ·  _SPLIT_  ·  
`po/qprompt_fi.ts:462, po/qprompt_fr.ts:463`
- **opus:** ❔ UNSURE (40) — semantic mistranslation claim; needs language expertise (qprompt_fi.ts:462)
- **gpt:** ❔ UNSURE (39) — wrong-word translation claim is semantic, not structurally provable (po/qprompt_fi.ts:462)
- **deepseek:** ✅ LEGIT (85) — Colors for prompter states->Toggle Prompter State in fi/fr/ko; wrong meaning (po/qprompt_fi.ts:462)
- **glm:** ❔ UNSURE (50) — po/qprompt_fr.ts:463 translation mismatch for 'Colors for prompter states'; cannot verify French semantics
- **kimi:** ✅ LEGIT (90) — po/qprompt_fi.ts:462 and fr.ts:463 translate \Colors for prompter states\" as \"Toggle Prompter State\"."
- **opus-ultra:** ❔ UNSURE (40) — max: unverifiable statically (runtime/semantic) — semantic mistranslation claim; needs language expertise (qprompt_fi.ts:462)

### [TS-08] French "Prompting:" → "Start prompter"  ·  _SPLIT_  ·  
`po/qprompt_fr.ts:478`
- **opus:** ❔ UNSURE (40) — semantic mistranslation claim (qprompt_fr.ts:478)
- **gpt:** ❔ UNSURE (39) — translation meaning cannot be verified from code alone (po/qprompt_fr.ts:478)
- **deepseek:** ✅ LEGIT (85) — French Prompting:->Démarrer prompter(Start prompter); semantic error (po/qprompt_fr.ts:478)
- **glm:** ❔ UNSURE (50) — po/qprompt_fr.ts:478 'Start prompter' vs 'Prompting:'; cannot verify French translation accuracy
- **kimi:** ✅ LEGIT (90) — po/qprompt_fr.ts:478 translates source \Prompting:\" as \"Démarrer le prompteur\" (Start prompter)."
- **opus-ultra:** ❔ UNSURE (40) — max: unverifiable statically (runtime/semantic) — semantic mistranslation claim (qprompt_fr.ts:478)

### [TS-09] Finnish/French/Korean/Dutch "Vertical offset" → "Velocity"  ·  _SPLIT_  ·  
`po/qprompt_fi.ts:560, po/qprompt_fr.ts:561, po/qprompt_ko.ts:559, po/qprompt_nl.ts:561`
- **opus:** ❔ UNSURE (40) — semantic mistranslation claim (qprompt_fi.ts:560)
- **gpt:** ❔ UNSURE (39) — translation meaning cannot be verified from code alone (po/qprompt_fi.ts:560)
- **deepseek:** ✅ LEGIT (85) — Vertical offset->Velocity in fi/fr/ko/nl; wrong term translated (po/qprompt_fi.ts:560)
- **glm:** ❔ UNSURE (50) — po/qprompt_fr.ts:561 'Velocity' for 'Vertical offset'; cannot verify translation accuracy
- **kimi:** ✅ LEGIT (90) — po/qprompt_fi.ts:560, fr.ts:561, ko.ts:559 and nl.ts:561 translate \Vertical offset\" with velocity terms (e.g.
- **opus-ultra:** ❔ UNSURE (40) — max: unverifiable statically (runtime/semantic) — semantic mistranslation claim (qprompt_fi.ts:560)

### [TS-10] Finnish/Korean "Next reload starts at" → "Step acceleration"  ·  _SPLIT_  ·  
`po/qprompt_fi.ts:158, po/qprompt_ko.ts:158`
- **opus:** ❔ UNSURE (40) — semantic mistranslation claim (qprompt_fi.ts:158)
- **gpt:** ❔ UNSURE (39) — translation meaning cannot be verified from code alone (po/qprompt_fi.ts:158)
- **deepseek:** ✅ LEGIT (85) — Next reload starts at->Step acceleration in fi/ko; wrong meaning (po/qprompt_fi.ts:158)
- **glm:** ❔ UNSURE (50) — po/qprompt_fi.ts:158 'Step acceleration' for 'Next reload starts at'; cannot verify
- **kimi:** ✅ LEGIT (90) — po/qprompt_fi.ts:158 and ko.ts:158 translate \Next reload starts at\" as step-acceleration text."
- **opus-ultra:** ❔ UNSURE (40) — max: unverifiable statically (runtime/semantic) — semantic mistranslation claim (qprompt_fi.ts:158)

### [TS-11] French/Finnish/Korean "No pointers" → "Both pointers" (opposite meaning)  ·  _SPLIT_  ·  
`po/qprompt_fr.ts:1003, po/qprompt_fi.ts:981, po/qprompt_ko.ts:980`
- **opus:** ❔ UNSURE (40) — opposite-meaning translation claim (qprompt_fr.ts:1003)
- **gpt:** ❔ UNSURE (39) — translation meaning cannot be verified from code alone (po/qprompt_fr.ts:1003)
- **deepseek:** ✅ LEGIT (90) — No pointers->Both pointers in fr/fi/ko; opposite meaning (po/qprompt_fr.ts:1003)
- **glm:** ❔ UNSURE (50) — po/qprompt_fr.ts:1003 'Both pointers' for 'No pointers'; opposite meaning; cannot verify
- **kimi:** ✅ LEGIT (90) — po/qprompt_fr.ts:1003, fi.ts:981 and ko.ts:980 translate \No pointers\" as \"Both pointers\" (opposite meaning)."
- **opus-ultra:** ❔ UNSURE (40) — max: unverifiable statically (runtime/semantic) — opposite-meaning translation claim (qprompt_fr.ts:1003)

### [TS-12] French "Alt" key → "Tout" (means "All")  ·  _SPLIT_  ·  
`po/qprompt_fr.ts:270`
- **opus:** ❔ UNSURE (40) — French Alt->Tout semantic claim (qprompt_fr.ts:270)
- **gpt:** ❔ UNSURE (39) — translation meaning cannot be verified from code alone (po/qprompt_fr.ts:270)
- **deepseek:** ✅ LEGIT (90) — French Alt->Tout(means All); clearly wrong translation (po/qprompt_fr.ts:270)
- **glm:** ❔ UNSURE (50) — po/qprompt_fr.ts:270 'Tout' for 'Alt'; cannot verify French translation
- **kimi:** ✅ LEGIT (90) — po/qprompt_fr.ts:270 translates source \Alt\" key as \"Tout\" (All)."
- **opus-ultra:** ❔ UNSURE (40) — max: unverifiable statically (runtime/semantic) — French Alt->Tout semantic claim (qprompt_fr.ts:270)

### [TS-13] French "Set velocity to 0–10" (all 11) → identical "Vitesse de départ"  ·  _SPLIT_  ·  
`po/qprompt_fr.ts:276-337`
- **opus:** ❔ UNSURE (40) — 11 identical 'Vitesse de depart'; semantic (qprompt_fr.ts:276)
- **gpt:** ❔ UNSURE (39) — translation meaning cannot be verified from code alone (po/qprompt_fr.ts:276)
- **deepseek:** ✅ LEGIT (90) — French all 11 Set velocity X->identical Vitesse de départ; no distinction (po/qprompt_fr.ts:276-337)
- **glm:** ❔ UNSURE (50) — po/qprompt_fr.ts:276-337 identical translations for different velocity values; likely wrong but cannot verify
- **kimi:** ✅ LEGIT (90) — po/qprompt_fr.ts:276-337 translates all eleven \Set velocity to 0–10\" sources identically as \"Vitesse de départ\"."
- **opus-ultra:** ❔ UNSURE (40) — max: unverifiable statically (runtime/semantic) — 11 identical 'Vitesse de depart'; semantic (qprompt_fr.ts:276)

### [TS-14] French "Clear color" → "Light color"  ·  _SPLIT_  ·  
`po/qprompt_fr.ts:1048`
- **opus:** ❔ UNSURE (40) — French Clear color->Light color; semantic (qprompt_fr.ts:1048)
- **gpt:** ❔ UNSURE (39) — translation meaning cannot be verified from code alone (po/qprompt_fr.ts:1048)
- **deepseek:** ✅ LEGIT (85) — French Clear color->Couleur claire(Light color); wrong translation (po/qprompt_fr.ts:1048)
- **glm:** ❔ UNSURE (50) — po/qprompt_fr.ts:1048 'Light color' for 'Clear color'; cannot verify
- **kimi:** ✅ LEGIT (90) — po/qprompt_fr.ts:1048 translates source \Clear color\" as \"Couleur claire\" (Light color)."
- **opus-ultra:** ❔ UNSURE (40) — max: unverifiable statically (runtime/semantic) — French Clear color->Light color; semantic (qprompt_fr.ts:1048)

### [TS-15] Finnish/Korean right pointer reuse → left pointer (swapped)  ·  _SPLIT_  ·  
`po/qprompt_fi.ts:494, po/qprompt_ko.ts:493`
- **opus:** ❔ UNSURE (40) — semantic mistranslation claim (qprompt_fi.ts:494)
- **gpt:** ❔ UNSURE (39) — translation meaning cannot be verified from code alone (po/qprompt_fi.ts:494)
- **deepseek:** ✅ LEGIT (85) — right pointer translations reuse left pointer text in fi/ko; swapped (po/qprompt_fi.ts:494 po/qprompt_ko.ts:493)
- **glm:** ❔ UNSURE (50) — po/qprompt_fi.ts:494 pointer swap in translation; cannot verify
- **kimi:** ✅ LEGIT (90) — po/qprompt_fi.ts:494 and ko.ts:493 translate \Right pointer\" as left-pointer text (swapped)."
- **opus-ultra:** ❔ UNSURE (40) — max: unverifiable statically (runtime/semantic) — semantic mistranslation claim (qprompt_fi.ts:494)

### [TS-16] Paragraph spacing: 8 languages strip trailing `%` from `<pre>%1%</pre>`  ·  _SPLIT_  ·  
`po/qprompt_cs.ts:128, po/qprompt_de.ts:132, po/qprompt_es.ts:132, po/qprompt_fr.ts:128, po/qprompt_fi.ts:128, po/qprompt_ko.ts:128, po/qprompt_nl.ts:128, po/qprompt_zh.ts:128`
- **opus:** ⚠️ PARTIAL (45) — <pre>%1%</pre> trailing % stripped; placeholder/structural (qprompt_cs.ts:128)
- **gpt:** ⚠️ PARTIAL (58) — observed Paragraph spacing: 8 languages strip trailing % from pre%1%/pre (po/qprompt_cs.ts:128)
- **deepseek:** ✅ LEGIT (90) — 8 languages strip trailing % from <pre>%1%</pre> markup; format broken (po/qprompt_cs.ts:128)
- **glm:** ✅ LEGIT (80) — po/qprompt_cs.ts:128 etc trailing % stripped from <pre>%1%</pre> placeholder; structural issue
- **kimi:** ✅ LEGIT (90) — po/qprompt_cs/de/es/fr/fi/ko/nl/zh.ts lines cited strip the trailing % from source <pre>%1%</pre> for paragraph spacing.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — <pre>%1%</pre> trailing % stripped; placeholder/structural (qprompt_cs.ts:128)

### [TS-17] Line width: 7 languages add spurious `%` to `<pre>%1</pre>`  ·  _SPLIT_  ·  
`po/qprompt_de.ts:539, po/qprompt_es.ts:543, po/qprompt_fi.ts:529, po/qprompt_fr.ts:530, po/qprompt_ko.ts:528, po/qprompt_nl.ts:530, po/qprompt_pt_BR.ts:539, po/qprompt_zh.ts:539`
- **opus:** ⚠️ PARTIAL (45) — <pre>%1</pre> spurious % in 7 langs; placeholder/structural (qprompt_de.ts:539)
- **gpt:** ⚠️ PARTIAL (58) — observed Line width: 7 languages add spurious % to pre%1/pre (po/qprompt_de.ts:539)
- **deepseek:** ✅ LEGIT (90) — 7 languages add spurious % to <pre>%1</pre> markup; format broken (po/qprompt_de.ts:539)
- **glm:** ✅ LEGIT (80) — po/qprompt_de.ts:539 etc spurious % added to <pre>%1</pre>; structural placeholder issue
- **kimi:** ✅ LEGIT (90) — po/qprompt_de/es/fi/fr/ko/nl/pt_BR/zh.ts lines cited add a spurious % to source <pre>%1</pre> for line width.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — <pre>%1</pre> spurious % in 7 langs; placeholder/structural (qprompt_de.ts:539)

### [TS-18] Orphan files: Hebrew and Polish exist but UI entries commented out  ·  _SPLIT_  ·  
`po/qprompt_he.ts, po/qprompt_pl.ts`
- **opus:** ❔ UNSURE (40) — Hebrew/Polish orphan files; UI entries commented out (qprompt_he.ts)
- **gpt:** ❔ UNSURE (39) — translation meaning cannot be verified from code alone (po/qprompt_he.ts:1)
- **deepseek:** ✅ LEGIT (85) — Hebrew/Polish .ts files exist but UI entries commented out; orphaned (po/qprompt_he.ts po/qprompt_pl.ts)
- **glm:** ✅ LEGIT (85) — po/qprompt_he.ts and qprompt_pl.ts exist but no UI entries in LanguageSettingsOverlay; orphaned files
- **kimi:** ✅ LEGIT (90) — po/qprompt_he.ts and po/qprompt_pl.ts exist, but LanguageSettingsOverlay.qml:111/135 entries for he-IL and pl_PL are commented out.
- **opus-ultra:** ❔ UNSURE (40) — max: unverifiable statically (runtime/semantic) — Hebrew/Polish orphan files; UI entries commented out (qprompt_he.ts)

### [TS-N07] Wrong translations: Chinese "Undo"→"Open", "Bars"→"Toolbar"; French "Pointer Configuration"→"Prompter duration"; Korean "Line width"→"Line height"  ·  _SPLIT_  ·  Medium
`qprompt_zh.ts, qprompt_fr.ts, qprompt_ko.ts`
- **opus:** ❔ UNSURE (40) — Chinese/French wrong-meaning translations; semantic (qprompt_zh.ts)
- **gpt:** ❔ UNSURE (39) — mixed Chinese/French/Korean semantic claims need language review (po/qprompt_zh.ts:1)
- **deepseek:** ❔ UNSURE (40) — Cannot verify translation file contents without reading .ts files; claim plausible but unconfirmed from source
- **glm:** ❔ UNSURE (50) — po/qprompt_zh.ts qprompt_fr.ts qprompt_ko.ts wrong translations; cannot verify without language expertise
- **kimi:** ✅ LEGIT (95) — zh &Undo=打开 (Open); zh Bars=工具栏 (Toolbar); fr Pointer Configuration=Durée du prompteur; ko Line width=줄 높이
- **opus-ultra:** ❔ UNSURE (40) — max: unverifiable statically (runtime/semantic) — Chinese/French wrong-meaning translations; semantic (qprompt_zh.ts)

### [TXT-CRIT] Plain 'v'/'V' keypress silently consumed — letter 'v' cannot be typed  ·  _SPLIT_  ·  Critical
`Prompter.qml:2163-2168`
- **opus:** ❔ UNSURE (45) — Key_V consumed only matters if handler active in editing mode; likely state-gated (Prompter.qml:2166)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Prompter.qml:2163)
- **deepseek:** ✅ LEGIT (85) — Prompter.qml:2163-2168: no-modifiers branch case Qt.Key_V forwards to prompter handler which only handles Ctrl+V paste; plain v keypress silently discarded — cannot type letter v
- **glm:** ✅ LEGIT (80) — Prompter.qml:2163-2168 bare 'v'/'V' keypress forwarded to prompter even with no modifiers; letter 'v' cannot be typed in editor
- **kimi:** ✅ LEGIT (95) — Prompter.qml:2163-2168 consumes plain Qt.Key_V and forwards to prompter handler, which has no action for unmodified 'v'; letter cannot be typed.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — Key_V consumed only matters if handler active in editing mode; likely state-gated (Prompte

### [TXT-FMT-N01] setMarkerHref("") fails to clear QTextFormat::AnchorHref — stale href persists  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:769-774`
- **opus:** ✅ LEGIT (65) — setMarkerHref('') doesn't clear AnchorHref via mergeCharFormat (FINAL-21 family) (documenthandler.cpp:769)
- **gpt:** ⚠️ PARTIAL (58) — observed setMarkerHref("") fails to clear QTextFormat::AnchorHref - stale href persists (src/documenthandler.cpp:769)
- **deepseek:** ✅ LEGIT (80) — setMarkerHref('') sets setAnchor(false) but skips clearProperty(AnchorHref) at documenthandler.cpp:769-774; stale href persists
- **glm:** ✅ LEGIT (70) — documenthandler.cpp:769-774 setMarkerHref('') fails to clear QTextFormat::AnchorHref; stale href persists
- **kimi:** ✅ LEGIT (90) — documenthandler.cpp:765-774 setMarkerHref('') never calls clearProperty(QTextFormat::AnchorHref); stale href remains
- **opus-ultra:** ✅ LEGIT (65) — setMarkerHref('') doesn't clear AnchorHref via mergeCharFormat (FINAL-21 family) (documenthandler.cpp:769)

### [TXT-N01] Find/replace fields missing persistentSelection: true  ·  _SPLIT_  ·  Low
`Find.qml:182,230`
- **opus:** ⚠️ PARTIAL (40) — find/replace fields missing persistentSelection (Find.qml:182)
- **gpt:** ⚠️ PARTIAL (58) — observed Find/replace fields missing persistentSelection: true (src/prompter/Find.qml:182)
- **deepseek:** ⚠️ PARTIAL (40) — persistentSelection missing is UX preference not functional defect (Find.qml:182 230)
- **glm:** ✅ LEGIT (75) — Find.qml:182 230 Find/replace fields missing persistentSelection: true
- **kimi:** ✅ LEGIT (95) — Find.qml:182 searchField and Find.qml:230 replaceField set selectByMouse:true but omit persistentSelection:true, so user selections vanish on focus loss.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — find/replace fields missing persistentSelection (Find.qml:182)

### [TXT-N04] goToNextMarker() temporarily sets cursorPosition=-1 — corrupts cursor state  ·  _SPLIT_  ·  Medium
`Prompter.qml:656-659`
- **opus:** ⚠️ PARTIAL (50) — goToNextMarker temporarily sets cursorPosition=-1 (Prompter.qml:656)
- **gpt:** ⚠️ PARTIAL (58) — observed goToNextMarker() temporarily sets cursorPosition=-1 - corrupts cursor state (src/prompter/Prompter.qml:656)
- **deepseek:** ✅ LEGIT (85) — Prompter.qml:656-659: editor.cursorPosition set to nextMarker().position which is -1 when no markers exist; cursorPosition=-1 fires onChange signals before guard corrects
- **glm:** ✅ LEGIT (75) — Prompter.qml:656-659 goToNextMarker temporarily sets cursorPosition=-1; corrupts cursor state
- **kimi:** ✅ LEGIT (80) — Prompter.qml:656-659 goToNextMarker sets editor.cursorPosition from nextMarker(-1) when no markers exist, corrupting cursor before fallback.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — goToNextMarker temporarily sets cursorPosition=-1 (Prompter.qml:656)

### [TYP-03] Floating-point equality comparison of window opacity  ·  _SPLIT_  ·  Medium
`src/main.cpp:273`
- **opus:** ⚠️ PARTIAL (60) — float ==1.0 but only 1.0/0.2 ever set (main.cpp:273)
- **gpt:** ⚠️ PARTIAL (58) — observed Floating-point equality comparison of window opacity (src/main.cpp:273)
- **deepseek:** ✅ LEGIT (85) — opacity()==1.0 at main.cpp:273 is exact floating-point equality on qreal(double); 0.9999999999!=1.0 — unreliable should use qFuzzyCompare
- **glm:** ✅ LEGIT (85) — main.cpp:273 compares floating-point opacity with ==1.0; exact equality check on float is fragile
- **kimi:** ✅ LEGIT (85) — main.cpp:273 compares topWindow->opacity() == 1.0 exactly; floating point equality is unreliable.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — float ==1.0 but only 1.0/0.2 ever set (main.cpp:273)

### [TYP-04] Bitwise AND on bools hides dead code in preventSleep  ·  _SPLIT_  ·  Medium
`src/documenthandler.cpp:1928,1931`
- **opus:** ✅ LEGIT (95) — false & prevent -> prevent dead (documenthandler.cpp:1928)
- **gpt:** ⚠️ PARTIAL (58) — observed Bitwise AND on bools hides dead code in preventSleep (src/documenthandler.cpp:1928)
- **deepseek:** ✅ LEGIT (90) — return false & prevent at doc.cpp:1928/1931; bitwise & on bool always 0(false) — prevent param dead code; should be && or just return false
- **glm:** ✅ LEGIT (85) — documenthandler.cpp:1928 1931 uses false & prevent which is bitwise AND on bools; both branches return false making iOS preventSleep always return false
- **kimi:** ✅ LEGIT (90) — documenthandler.cpp:1928,1931 return false & prevent; result is always false so prevent parameter is ignored.
- **opus-ultra:** ✅ LEGIT (95) — false & prevent -> prevent dead (documenthandler.cpp:1928)

### [TYP-05] Uninitialized pointer member m_reply in DocumentHandler  ·  _SPLIT_  ·  Medium
`src/documenthandler.h:353, src/documenthandler.cpp:123-158`
- **opus:** ✅ LEGIT (95) — m_reply uninitialized (documenthandler.h:353)
- **gpt:** ✅ LEGIT (88) — Uninitialized pointer member m_reply in DocumentHandler (src/documenthandler.h:353)
- **deepseek:** ⚠️ PARTIAL (60) — m_reply in doc.h:353 declared as raw pointer; not in constructor init list at doc.cpp:123-130; holds indeterminate value until loadFromNetwork sets it — real but low risk
- **glm:** ✅ LEGIT (90) — documenthandler.h:353 m_reply never initialized in constructor; documenthandler.cpp:123-158 constructor doesn't initialize it
- **kimi:** ✅ LEGIT (90) — documenthandler.h:353 QNetworkReply* m_reply never initialized in constructor :123-158.
- **opus-ultra:** ✅ LEGIT (95) — m_reply uninitialized (documenthandler.h:353)

### [TYP-07] Narrowing conversion: `size_t` → `int` in SpellChecker::decode  ·  _SPLIT_  ·  Low
`src/spellchecker.cpp:411-412`
- **opus:** ✅ LEGIT (90) — size_t->int narrowing; trivial (spellchecker.cpp:411)
- **gpt:** ⚠️ PARTIAL (58) — observed Narrowing conversion: size_t -> int in SpellChecker::decode (src/spellchecker.cpp:411)
- **deepseek:** ⚠️ PARTIAL (30) — Narrowing size_t->int at spellchecker.cpp:411; max word length < INT_MAX in practice — correctness nit zero practical impact
- **glm:** ✅ LEGIT (75) — spellchecker.cpp:411-412 static_cast<int>(word.size()) narrows qsizetype to int; safe for typical word lengths but technically narrowing
- **kimi:** ✅ LEGIT (70) — spellchecker.cpp:411-412 static_cast<int>(word.size()) narrows 64-bit size_t to signed 32-bit int.
- **opus-ultra:** ✅ LEGIT (90) — size_t->int narrowing; trivial (spellchecker.cpp:411)

### [TYP-09] Null pointer dereferences in emit textChanged related to uninitialized m_document  ·  _SPLIT_  ·  Low
`src/documenthandler.cpp:320,325,334,343,383 (related)`
- **opus:** ❌ FALSE (90) — cited lines are #ifdef; textChanged never emitted anywhere
- **gpt:** ❌ FALSE (76) — cited setters emit member signals; m_document is not dereferenced there (src/documenthandler.cpp:320)
- **deepseek:** ⚠️ PARTIAL (40) — Various emit textChanged() paths depend on document() non-null at doc.cpp:320-383; but gated by m_document checks in callers — fragile but currently guarded
- **glm:** ⚠️ PARTIAL (55) — documenthandler.cpp:320+ textCursor() returns null cursor when m_document is null; methods check cursor.isNull() so safe
- **kimi:** ❌ FALSE (80) — documenthandler.cpp does not emit textChanged at cited lines; signal is declared but never emitted.
- **opus-ultra:** ❌ FALSE (90) — cited lines are #ifdef; textChanged never emitted anywhere

### [TYP-N03] Inconsistent `_` vs `m_` member prefix: _markersModel, _fileSystemWatcher  ·  _SPLIT_  ·  Low
`documenthandler.h:343-344`
- **opus:** ⚠️ PARTIAL (35) — _ vs m_ member prefix inconsistency; cosmetic (documenthandler.h:343)
- **gpt:** ⚠️ PARTIAL (58) — observed Inconsistent vs m member prefix: markersModel, _fileSystemWatcher (src/documenthandler.h:343)
- **deepseek:** ✅ LEGIT (80) — _markersModel and _fileSystemWatcher use _ prefix vs m_ for other members (documenthandler.h:343-344)
- **glm:** ✅ LEGIT (75) — documenthandler.h:343-344 inconsistent _ prefix vs m_ for _markersModel and _fileSystemWatcher
- **kimi:** ✅ LEGIT (90) — documenthandler.h:343-344 names members _markersModel and _fileSystemWatcher while the rest of the class uses m_ prefix.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — _ vs m_ member prefix inconsistency; cosmetic (documenthandler.h:343)

### [TYP-N06] 9 getters copy-paste double-textCursor() pattern — null check on stale cursor  ·  _SPLIT_  ·  Low
`documenthandler.cpp: alignment(548), bold(565), italic(581), underline(597), strike(613), subscript(629), superscript(648), fontCapitalization(669), regularMarker(694)`
- **opus:** ⚠️ PARTIAL (50) — 9 getters share the double-textCursor() pattern (LOG-07 family)
- **gpt:** ⚠️ PARTIAL (58) — observed 9 getters copy-paste double-textCursor() pattern - null check on stale cursor (src/documenthandler.cpp:1)
- **deepseek:** ✅ LEGIT (65) — alignment() null-checks first textCursor() but reads second stale textCursor() (documenthandler.cpp:548-550)
- **glm:** ⚠️ PARTIAL (65) — documenthandler.cpp:548+ 9 getters call textCursor() twice; second call may return stale cursor
- **kimi:** ✅ LEGIT (85) — documenthandler.cpp:545-696 repeats the double-textCursor() pattern in alignment,bold,italic,underline,strike,subscript,superscript,fontCapitalization,regularMarker: null-checking one cursor then reading from a fresh textCursor().
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — 9 getters share the double-textCursor() pattern (LOG-07 family)

### [UNIT-01] ProgressIndicator.qml:46 Units.ShortDuration with no Kirigami import  ·  _SPLIT_  ·  High
`ProgressIndicator.qml:46`
- **opus:** ⚠️ PARTIAL (55) — Units.ShortDuration broken via R3-CTX-01, 'no Kirigami import' misdiagnoses cause (ProgressIndicator.qml:46)
- **gpt:** ✅ LEGIT (84) — ProgressIndicator.qml:46 Units.ShortDuration with no Kirigami import (src/prompter/ProgressIndicator.qml:46)
- **deepseek:** ✅ LEGIT (95) — Units.ShortDuration at ProgressIndicator.qml:46 — no Kirigami import Units undefined
- **glm:** ✅ LEGIT (80) — ProgressIndicator.qml:46 Units.ShortDuration with no Kirigami import; resolves via AbstractUnits
- **kimi:** ✅ LEGIT (95) — ProgressIndicator.qml:46 uses Units.ShortDuration but file imports no Kirigami; AbstractUnits is not registered as a singleton.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — Units.ShortDuration broken via R3-CTX-01

### [UNIT-02] PrompterView.qml 7x Units.ShortDuration with no Kirigami import  ·  _SPLIT_  ·  High
`PrompterView.qml:80,87,103,132,139,155,185`
- **opus:** ⚠️ PARTIAL (55) — Units.ShortDuration broken via R3-CTX-01, but 'no Kirigami import' misdiagnoses cause (PrompterView.qml:80)
- **gpt:** ✅ LEGIT (84) — PrompterView.qml 7x Units.ShortDuration with no Kirigami import (src/prompter/PrompterView.qml:80)
- **deepseek:** ✅ LEGIT (95) — 7x Units.ShortDuration in PrompterView.qml — no Kirigami import at all
- **glm:** ✅ LEGIT (80) — PrompterView.qml:80+ 7x Units.ShortDuration; resolves via AbstractUnits QML_ELEMENT
- **kimi:** ✅ LEGIT (95) — PrompterView.qml uses Units.ShortDuration at multiple lines but imports only QtQuick/QtCore/com.cuperino.qprompt.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — Units.ShortDuration broken via R3-CTX-01

### [UNIT-03] PrompterBackground.qml:160 Units.LongDuration no Kirigami import  ·  _SPLIT_  ·  Medium
`PrompterBackground.qml:160`
- **opus:** ⚠️ PARTIAL (50) — Units.LongDuration broken via R3-CTX-01 (PrompterBackground.qml:160)
- **gpt:** ✅ LEGIT (78) — PrompterBackground.qml:160 Units.LongDuration no Kirigami import (src/prompter/PrompterBackground.qml:160)
- **deepseek:** ✅ LEGIT (95) — Units.LongDuration at PrompterBackground.qml:160 — no Kirigami import
- **glm:** ✅ LEGIT (75) — PrompterBackground.qml:160 Units.LongDuration; resolves via AbstractUnits
- **kimi:** ✅ LEGIT (90) — PrompterBackground.qml:160 uses Units.LongDuration with no Kirigami import.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — Units.LongDuration broken via R3-CTX-01 (PrompterBackground.qml:160)

### [UNIT-04] Flip.qml:34,41 two Units.LongDuration no Kirigami import  ·  _SPLIT_  ·  Medium
`Flip.qml:34,41`
- **opus:** ⚠️ PARTIAL (50) — Units.LongDuration broken via R3-CTX-01 (Flip.qml:34)
- **gpt:** ✅ LEGIT (78) — Flip.qml:34,41 two Units.LongDuration no Kirigami import (src/prompter/Flip.qml:34)
- **deepseek:** ✅ LEGIT (95) — 2x Units.LongDuration at Flip.qml — no Kirigami import (only QtQuick+com.cuperino)
- **glm:** ✅ LEGIT (75) — Flip.qml:34 41 Units.LongDuration; resolves via AbstractUnits
- **kimi:** ✅ LEGIT (90) — Flip.qml:34 and :41 use Units.LongDuration with only QtQuick/QtCore imports.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — Units.LongDuration broken via R3-CTX-01 (Flip.qml:34)

### [UNIT-05] pointer_0.qml:72 Units.VeryLongDuration no Kirigami import  ·  _SPLIT_  ·  Low
`pointer_0.qml:72`
- **opus:** ⚠️ PARTIAL (50) — Units.VeryLongDuration broken via R3-CTX-01 (pointer_0.qml:72)
- **gpt:** ✅ LEGIT (78) — pointer_0.qml:72 Units.VeryLongDuration no Kirigami import (src/prompter/pointers/pointer_0.qml:72)
- **deepseek:** ✅ LEGIT (95) — Units.VeryLongDuration at pointer_0.qml:72 — no Kirigami import
- **glm:** ✅ LEGIT (75) — pointer_0.qml:72 Units.VeryLongDuration; resolves via AbstractUnits
- **kimi:** ✅ LEGIT (90) — pointer_0.qml:72 uses Units.VeryLongDuration with no Kirigami import.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — Units.VeryLongDuration broken via R3-CTX-01 (pointer_0.qml:72)

### [UNIT-06] Find.qml:92 Units.ShortDuration with namespaced Kirigami import  ·  _SPLIT_  ·  Medium
`Find.qml:92`
- **opus:** ⚠️ PARTIAL (50) — Units.ShortDuration broken via R3-CTX-01 (Find.qml:92)
- **gpt:** ✅ LEGIT (78) — Find.qml:92 Units.ShortDuration with namespaced Kirigami import (src/prompter/Find.qml:92)
- **deepseek:** ✅ LEGIT (95) — Units.ShortDuration at Find.qml:92 — imported as Kirigami should be Kirigami.Units
- **glm:** ⚠️ PARTIAL (65) — Find.qml:92 Units.ShortDuration with namespaced Kirigami import; may not resolve
- **kimi:** ✅ LEGIT (90) — Find.qml:92 uses bare Units.ShortDuration while importing org.kde.kirigami 2.11 as Kirigami.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — Units.ShortDuration broken via R3-CTX-01 (Find.qml:92)

### [UNIT-07] ReadRegionOverlay.qml 3x Units.ShortDuration with namespaced import  ·  _SPLIT_  ·  Medium
`ReadRegionOverlay.qml:546,610,616`
- **opus:** ⚠️ PARTIAL (50) — Units.ShortDuration broken via R3-CTX-01 (ReadRegionOverlay.qml:546)
- **gpt:** ✅ LEGIT (78) — ReadRegionOverlay.qml 3x Units.ShortDuration with namespaced import (src/prompter/ReadRegionOverlay.qml:546)
- **deepseek:** ✅ LEGIT (90) — 3x Units.ShortDuration at ReadRegionOverlay.qml:546 610 616 — NO Kirigami import at all (bug said namespaced)
- **glm:** ⚠️ PARTIAL (65) — ReadRegionOverlay.qml:546+ Units.ShortDuration; resolves via AbstractUnits
- **kimi:** ✅ LEGIT (90) — ReadRegionOverlay.qml:546/610/616 use bare Units.ShortDuration while Kirigami is imported namespaced.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — Units.ShortDuration broken via R3-CTX-01 (ReadRegionOverlay.qml:546)

### [URL-N01] reload() constructs file:// URL by string concatenation without encoding  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:860`
- **opus:** ✅ LEGIT (60) — reload file:// URL by concat without encoding (dup PATH-N02) (documenthandler.cpp:860)
- **gpt:** ⚠️ PARTIAL (58) — observed reload() constructs file:// URL by string concatenation without encoding (src/documenthandler.cpp:860)
- **deepseek:** ✅ LEGIT (65) — file:// URL built by string concatenation without percent-encoding (documenthandler.cpp:860)
- **glm:** ✅ LEGIT (80) — documenthandler.cpp:860 reload() constructs file:// URL by string concatenation without encoding
- **kimi:** ✅ LEGIT (90) — documenthandler.cpp:860 reload() builds QUrl from 'file://' + fileUrl without percent-encoding; paths with #/space/non-ASCII may break reload
- **opus-ultra:** ✅ LEGIT (60) — reload file:// URL by concat without encoding (dup PATH-N02) (documenthandler.cpp:860)

### [URL-N03] Network-loaded HTML lacks base URL — relative resources broken  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:888-901`
- **opus:** ✅ LEGIT (55) — network HTML lacks base URL; relative resources break (documenthandler.cpp:888)
- **gpt:** ⚠️ PARTIAL (58) — observed Network-loaded HTML lacks base URL - relative resources broken (src/documenthandler.cpp:888)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:888-901: loadFromNetworkFinihed never calls doc->setBaseUrl(); original network URL discarded — relative resources (images/stylesheets) in HTML cannot resolve
- **glm:** ✅ LEGIT (80) — documenthandler.cpp:888-901 network-loaded HTML lacks base URL; relative resources broken
- **kimi:** ✅ LEGIT (80) — documenthandler.cpp:888-901 loadFromNetworkFinihed never calls doc->setBaseUrl(), so relative resources in network HTML fail.
- **opus-ultra:** ✅ LEGIT (55) — network HTML lacks base URL; relative resources break (documenthandler.cpp:888)

### [URL-N04] loadFromNetwork() validates wrong URL instance  ·  _SPLIT_  ·  Low
`documenthandler.cpp:881`
- **opus:** ✅ LEGIT (60) — validates wrong URL instance (dup NET-N06) (documenthandler.cpp:881)
- **gpt:** ⚠️ PARTIAL (58) — observed loadFromNetwork() validates wrong URL instance (src/documenthandler.cpp:881)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:881: url.isValid() validates original url not constructed resultingUrl; valid relative URL can produce invalid resultingUrl that passes unchecked
- **glm:** ✅ LEGIT (75) — documenthandler.cpp:881 loadFromNetwork validates original url not constructed resultingUrl
- **kimi:** ✅ LEGIT (85) — documenthandler.cpp:881 validates original 'url' parameter, not the constructed 'resultingUrl', allowing invalid requests.
- **opus-ultra:** ✅ LEGIT (60) — validates wrong URL instance (dup NET-N06) (documenthandler.cpp:881)

### [URL-N05] openFromRemote() blindly prepends http:// to non-HTTP schemes  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:1279-1282`
- **opus:** ✅ LEGIT (55) — openFromRemote blindly prepends http:// to non-HTTP schemes (PrompterPage.qml:1279)
- **gpt:** ⚠️ PARTIAL (58) — observed openFromRemote() blindly prepends http:// to non-HTTP schemes (src/kirigami_ui/PrompterPage.qml:1279)
- **deepseek:** ✅ LEGIT (90) — PrompterPage.qml:1279-1282: any URL not starting http:// or https:// gets http:// prepended; file:// becomes http://file:// case variants like HTTP:// missed
- **glm:** ✅ LEGIT (80) — PrompterPage.qml:1279-1282 openFromRemote() blindly prepends http:// to non-HTTP schemes
- **kimi:** ✅ LEGIT (85) — PrompterPage.qml:1279-1282 prepends 'http://' to any URL not starting with http/https, breaking file:// and other schemes.
- **opus-ultra:** ✅ LEGIT (55) — openFromRemote blindly prepends http:// to non-HTTP schemes (PrompterPage.qml:1279)

### [UTF-N01] text.truncate(64) can split UTF-16 surrogate pairs — corrupted display  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:736`
- **opus:** ⚠️ PARTIAL (50) — truncate(64) can split a UTF-16 surrogate pair; rare (documenthandler.cpp:736)
- **gpt:** ✅ LEGIT (78) — text.truncate(64) can split UTF-16 surrogate pairs - corrupted display (src/documenthandler.cpp:736)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:736: text.truncate(64) cuts at UTF-16 code unit 64; supplementary-plane chars (emoji rare CJK) straddling boundary -> orphaned high surrogate — corrupted preview
- **glm:** ✅ LEGIT (75) — documenthandler.cpp:736 text.truncate(64) can split UTF-16 surrogate pairs; corrupted display
- **kimi:** ✅ LEGIT (90) — text.truncate(64) at documenthandler.cpp:736 cuts UTF-16 code units and can split surrogate pairs.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — truncate(64) can split a UTF-16 surrogate pair; rare (documenthandler.cpp:736)

### [VCI-N01] At-end action buttons use inconsistent font scaling (1/1.5 vs 1/1.75) in same group  ·  _SPLIT_  ·  Low
`Prompter.qml:1158,1185,1212 vs 1256,1269,1309`
- **opus:** ⚠️ PARTIAL (40) — at-end buttons inconsistent font scaling (Prompter.qml:1158)
- **gpt:** ⚠️ PARTIAL (48) — visual issue is plausible but depends on theme or device (src/prompter/Prompter.qml:1158)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:1158/1185/1212 vs 1256/1269/1309: Stop/Exit/Loop buttons scale font /1.5 while adjacent Flipable/SpinBox scale /1.75 — visible 16.7% size mismatch
- **glm:** ✅ LEGIT (70) — Prompter.qml:1158+ at-end action buttons use inconsistent font scaling 1/1.5 vs 1/1.75
- **kimi:** ✅ LEGIT (70) — Prompter.qml:1158-1212 at-end Stop/Exit/Loop buttons scale font by 1/1.5 while adjacent Flipable/SpinBox at ~1256-1309 scale by 1/1.75.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — at-end buttons inconsistent font scaling (Prompter.qml:1158)

### [VCI-N02] upperControls and bottomControls fade to different opacity levels during Prompting  ·  _SPLIT_  ·  Low
`PrompterView.qml:70 vs 120`
- **opus:** ⚠️ PARTIAL (40) — upper/bottom controls fade to different opacity (PrompterView.qml:70)
- **gpt:** ⚠️ PARTIAL (48) — visual issue is plausible but depends on theme or device (src/prompter/PrompterView.qml:70)
- **deepseek:** ✅ LEGIT (95) — PrompterView.qml:70 vs 120: upperControls fades to 0.1 during Prompting; bottomControls to 0.2 — top controls nearly invisible while bottom twice as visible
- **glm:** ✅ LEGIT (70) — PrompterView.qml:70 vs 120 upperControls and bottomControls fade to different opacity levels
- **kimi:** ✅ LEGIT (70) — PrompterView.qml:70 fades upperControls to opacity 0.1 during Prompting while line 120 fades bottomControls to 0.2.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — upper/bottom controls fade to different opacity (PrompterView.qml:70)

### [VCI-N03] Hardcoded divider/separator/border colors (#292929, #606060, #808080) break theme adaptation  ·  _SPLIT_  ·  Low
`PointerSettings.qml, InputsOverlay.qml, Find.qml, PrompterPage.qml, ProgressIndicator.qml`
- **opus:** ⚠️ PARTIAL (40) — hardcoded divider/border colors break theming (PointerSettings.qml)
- **gpt:** ⚠️ PARTIAL (48) — visual issue is plausible but depends on theme or device (src/prompter/PointerSettings.qml:1)
- **deepseek:** ⚠️ PARTIAL (70) — PointerSettings/InputsOverlay/Find/PrompterPage/ProgressIndicator: hardcoded colors (#292929 at PointerSettings.qml:260 verified); others not all checked but pattern consistent
- **glm:** ⚠️ PARTIAL (55) — PointerSettings.qml etc hardcoded divider/separator/border colors break theme adaptation
- **kimi:** ✅ LEGIT (90) — Hardcoded #292929/#606060/#808080 in PointerSettings.qml:240/260 InputsOverlay.qml:69 Find.qml:83 PrompterPage.qml:817 ProgressIndicator.qml:52 break theme adaptation.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — hardcoded divider/border colors break theming (PointerSettings.qml)

### [VIS-FB-N01] bookmarkListButton and searchButton missing checkable: true — no checked background  ·  _SPLIT_  ·  Low
`EditorToolbar.qml:188,202`
- **opus:** ⚠️ PARTIAL (50) — bookmarkListButton/searchButton missing checkable:true (EditorToolbar.qml:188)
- **gpt:** ⚠️ PARTIAL (58) — observed bookmarkListButton and searchButton missing checkable: true - no checked background (src/kirigami_ui/EditorToolbar.qml:188)
- **deepseek:** ✅ LEGIT (90) — EditorToolbar.qml:188 202: bookmarkListButton.searchButton declare checked binding but omit checkable:true; no Material checked background
- **glm:** ✅ LEGIT (70) — EditorToolbar.qml:188 202 bookmarkListButton and searchButton missing checkable: true; no checked background
- **kimi:** ✅ LEGIT (90) — EditorToolbar.qml:188/202 set `checked` on bookmarkListButton/searchButton but omit `checkable: true`
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — bookmarkListButton/searchButton missing checkable:true (EditorToolbar.qml:188)

### [VIS-N04] Countdown crosshair frame renders orphan lines when enabled=false  ·  _SPLIT_  ·  Low
`Countdown.qml:151-178`
- **opus:** ⚠️ PARTIAL (45) — crosshair frame orphan lines when enabled=false (Countdown.qml:151)
- **gpt:** ⚠️ PARTIAL (58) — observed Countdown crosshair frame renders orphan lines when enabled=false (src/prompter/Countdown.qml:151)
- **deepseek:** ⚠️ PARTIAL (45) — Shape lines lack visible binding to frame property; render independent of toggle (Countdown.qml:151-178)
- **glm:** ⚠️ PARTIAL (60) — Countdown.qml:151-178 crosshair frame renders orphan lines when enabled=false
- **kimi:** ✅ LEGIT (85) — Countdown.qml:151-178 frame Shape has no visible:countdown.enabled binding; if countdown becomes visible while enabled=false, hairline crosshairs still render
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — crosshair frame orphan lines when enabled=false (Countdown.qml:151)

### [VIS-N05] velocityDragOverlay blocks all interaction during indicator fade-out (~500ms dead zone)  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:913-919,865-872`
- **opus:** ⚠️ PARTIAL (50) — velocityDragOverlay blocks interaction during ~500ms fade (PrompterPage.qml:913)
- **gpt:** ⚠️ PARTIAL (58) — observed velocityDragOverlay blocks all interaction during indicator fade-out (~500ms dead zone) (src/kirigami_ui/PrompterPage.qml:913)
- **deepseek:** ✅ LEGIT (65) — velocityDragOverlay stays visible during fade animation blocking input for Units.LongDuration (PrompterPage.qml:913-919)
- **glm:** ✅ LEGIT (75) — PrompterPage.qml:913-919 865-872 velocityDragOverlay blocks all interaction during fade-out (~500ms dead zone)
- **kimi:** ✅ LEGIT (92) — PrompterPage.qml:913-919 velocityDragOverlay visible = velocityIndicator.visible; during the ~500ms fade-out the overlay blocks all viewport interaction
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — velocityDragOverlay blocks interaction during ~500ms fade (PrompterPage.qml:913)

### [W10-CLP-02] Remote image URLs in pasted HTML cause unsanctioned network requests  ·  _SPLIT_  ·  Medium
`src/documenthandler.cpp:1246-1334, 1425-1455`
- **opus:** ⚠️ PARTIAL (50) — pasted remote img URLs can trigger network fetch via richtext engine (documenthandler.cpp:1246)
- **gpt:** ⚠️ PARTIAL (58) — observed Remote image URLs in pasted HTML cause unsanctioned network requests (src/documenthandler.cpp:1246)
- **deepseek:** ✅ LEGIT (90) — filterHtml never strips img remote src; insertHtmlAt downloads via image.load(src) leaking user IP (documenthandler.cpp:1449-1451)
- **glm:** ✅ LEGIT (80) — documenthandler.cpp:1246-1334 1425-1455 pasted HTML with remote image URLs causes unsolicited network requests
- **kimi:** ✅ LEGIT (85) — filterHtml at documenthandler.cpp:1246-1334 does not strip img src; insertHtmlAt at 1425-1455 synchronously loads remote http/https images.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — pasted remote img URLs can trigger network fetch via richtext engine (documenthandler.cpp:

### [W10-CNV2-03] import() uses fromStdString on non-Windows — encoding corruption  ·  _SPLIT_  ·  High
`src/documenthandler.cpp:1096`
- **opus:** ⚠️ PARTIAL (45) — fromStdString is fromUtf8 in Qt6; LibreOffice emits UTF-8 (documenthandler.cpp:1096)
- **gpt:** ⚠️ PARTIAL (58) — observed import() uses fromStdString on non-Windows - encoding corruption (src/documenthandler.cpp:1096)
- **deepseek:** ⚠️ PARTIAL (65) — on Qt5 non-Win fromStdString uses locale encoding; Qt6(target) uses UTF-8 correctly dead-code path (documenthandler.cpp:1096)
- **glm:** ✅ LEGIT (85) — documenthandler.cpp:1096 import() uses fromStdString on non-Windows; encoding may corrupt non-UTF-8 data
- **kimi:** ✅ LEGIT (85) — documenthandler.cpp:1096 decodes LibreOffice output via QString::fromStdString(bytes.toStdString()) on non-Windows, risking encoding corruption.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — fromStdString is fromUtf8 in Qt6; LibreOffice emits UTF-8 (documenthandler.cpp:1096)

### [W10-DEP-01] Missing vcpkg.json manifest — vcpkg manifest mode installs nothing  ·  _SPLIT_  ·  Critical
`vcpkg-configuration.json (no companion vcpkg.json)`
- **opus:** ✅ LEGIT (75) — vcpkg.json absent; only vcpkg-configuration.json present -> manifest mode installs nothing
- **gpt:** ✅ LEGIT (92) — Missing vcpkg.json manifest - vcpkg manifest mode installs nothing (vcpkg-configuration.json:1)
- **deepseek:** ✅ LEGIT (92) — vcpkg-configuration.json exists but no vcpkg.json manifest; vcpkg manifest mode installs nothing (project root)
- **glm:** ⚠️ PARTIAL (65) — vcpkg-configuration.json exists but no vcpkg.json manifest; manifest mode installs nothing
- **kimi:** ✅ LEGIT (95) — vcpkg-configuration.json exists but vcpkg.json is absent, so vcpkg manifest mode installs no dependencies.
- **opus-ultra:** ✅ LEGIT (75) — vcpkg.json absent; only vcpkg-configuration.json present -> manifest mode installs nothing

### [W10-PLF-02] QHotkey_FOUND never set in FetchContent path — built but never linked  ·  _SPLIT_  ·  High
`CMakeLists.txt:252-258, src/CMakeLists.txt:495-500`
- **opus:** ⚠️ PARTIAL (50) — FetchContent may not set QHotkey_FOUND; unconfirmed whether set manually (CMakeLists.txt:252)
- **gpt:** ⚠️ PARTIAL (58) — observed QHotkeyFOUND never set in FetchContent path - built but never linked (CMakeLists.txt:252)
- **deepseek:** ✅ LEGIT (95) — FetchContent_MakeAvailable doesn't set QHotkey_FOUND; add_def+target_link_libraries gated library never linked (CMakeLists.txt:252 src/CMakeLists.txt:495-500)
- **glm:** ✅ LEGIT (80) — CMakeLists.txt:252-258 FetchContent for QHotkey but src/CMakeLists.txt:495-500 checks QHotkey_FOUND which may not be set
- **kimi:** ✅ LEGIT (85) — CMakeLists.txt:252-258 fetches QHotkey but never sets QHotkey_FOUND; src/CMakeLists.txt:495-500 therefore skips linking qhotkey.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — FetchContent may not set QHotkey_FOUND; unconfirmed whether set manually (CMakeLists.txt:2

### [W10-PMV-01] font.pixelSize evaluates to 0 before first layout pass — crash hazard  ·  _SPLIT_  ·  High
`src/prompter/PrompterView.qml:242`
- **opus:** ⚠️ PARTIAL (50) — fontSize 0 before layout -> pixelSize warning, not a crash (PrompterView.qml:242)
- **gpt:** ⚠️ PARTIAL (58) — observed font.pixelSize evaluates to 0 before first layout pass - crash hazard (src/prompter/PrompterView.qml:242)
- **deepseek:** ⚠️ PARTIAL (70) — pixelSize depends on __vw=width/100; before first layout width=0 gives fontSize=0 but parseInt guard mitigates (PrompterView.qml:242)
- **glm:** ⚠️ PARTIAL (60) — PrompterView.qml:242 font.pixelSize may be 0 before first layout pass; guarded by state check in practice
- **kimi:** ✅ LEGIT (80) — PrompterView.qml:242 fontSize depends on prompter.__vw (width/100); before layout width=0, so pixelSize can be zero.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — fontSize 0 before layout -> pixelSize warning

### [W10-PMV-02] Circular ShaderEffectSource dependency — shadow ghost on first frame  ·  _SPLIT_  ·  Medium
`src/prompter/PrompterView.qml:230-233, Prompter.qml:744-770`
- **opus:** ⚠️ PARTIAL (50) — circular ShaderEffectSource; shadow ghost first frame (PrompterView.qml:230)
- **gpt:** ⚠️ PARTIAL (58) — observed Circular ShaderEffectSource dependency - shadow ghost on first frame (src/prompter/PrompterView.qml:230)
- **deepseek:** ✅ LEGIT (80) — ShaderEffectSource captures prompter with layer applied feeds back as shadow texture one-frame ghost (PrompterView.qml:230-233)
- **glm:** ⚠️ PARTIAL (65) — PrompterView.qml:230-233 ShaderEffectSource circular dependency with Prompter.qml:744-770; shadow ghost on first frame
- **kimi:** ✅ LEGIT (85) — PrompterView.qml:230-233 prompterShadowSource sourceItem is prompter, and Prompter.qml:744-770 layer.effect reads that source, creating a circular dependency.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — circular ShaderEffectSource; shadow ghost first frame (PrompterView.qml:230)

### [W10-SWT-01] CloseActions switch drops RecentLocal/RecentRemote — recent document open silently lost after save  ·  _SPLIT_  ·  High
`src/prompter/Prompter.qml:2479`
- **opus:** ⚠️ PARTIAL (55) — CloseActions switch omits RecentLocal/RecentRemote cases (Prompter.qml:2479)
- **gpt:** ⚠️ PARTIAL (58) — observed CloseActions switch drops RecentLocal/RecentRemote - recent document open silently lost after s (src/prompter/Prompter.qml:2479)
- **deepseek:** ✅ LEGIT (90) — switch misses RecentLocal/RecentRemote; recent document intent silently lost after save (Prompter.qml:2479-2486)
- **glm:** ✅ LEGIT (80) — Prompter.qml:2479 CloseActions switch missing RecentLocal/RecentRemote cases; recent document open silently lost after save
- **kimi:** ✅ LEGIT (90) — Prompter.qml:2479-2486 CloseActions switch handles LoadGuide/LoadNew/Open/Network/Quit but omits RecentLocal and RecentRemote.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — CloseActions switch omits RecentLocal/RecentRemote cases (Prompter.qml:2479)

### [W10-SWT-02] Same bug in IosSaveDialog.onAccepted path  ·  _SPLIT_  ·  High
`src/prompter/Prompter.qml:2500`
- **opus:** ⚠️ PARTIAL (55) — same omission in IosSaveDialog.onAccepted (Prompter.qml:2500)
- **gpt:** ⚠️ PARTIAL (58) — observed Same bug in IosSaveDialog.onAccepted path (src/prompter/Prompter.qml:2500)
- **deepseek:** ✅ LEGIT (90) — same omission in IosSaveDialog.onAccepted switch; identical bug on iOS (Prompter.qml:2500-2506)
- **glm:** ✅ LEGIT (80) — Prompter.qml:2500 same missing CloseActions cases in IosSaveDialog.onAccepted path
- **kimi:** ✅ LEGIT (90) — Prompter.qml:2500-2506 IosSaveDialog onAccepted switch repeats the same omission of RecentLocal and RecentRemote.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — same omission in IosSaveDialog.onAccepted (Prompter.qml:2500)

### [W10-WSM-01] Infinite reload loop on unauthorized WASM host — app unusable  ·  _SPLIT_  ·  Critical
`src/prompter/Prompter.qml:439, src/wasmintegration.cpp:189-194`
- **opus:** ⚠️ PARTIAL (55) — officialHost()->quit()->reload real, but called in toggle() not startup; 'infinite' overstated (Prompter.qml:439)
- **gpt:** ⚠️ PARTIAL (58) — observed Infinite reload loop on unauthorized WASM host - app unusable (src/prompter/Prompter.qml:439)
- **deepseek:** ✅ LEGIT (88) — toggle->officialHost->quit->aboutToQuit->location.reload->same unauthorized host; inescapable loop (wasmintegration.cpp:189-194)
- **glm:** ✅ LEGIT (80) — Prompter.qml:439 wasmintegration.cpp:189-194 officialHost() calls quit() on unauthorized host; reload loop on WASM
- **kimi:** ✅ LEGIT (85) — Prompter.qml:439 calls AppController.wasm.officialHost(); wasmintegration.cpp:192 quits on unauthorized hosts, triggering aboutToQuit reload loop.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — officialHost()->quit()->reload real

### [W10-WSM-02] Global file-picker state overwritten by re-entrant calls — wrong file delivered  ·  _SPLIT_  ·  Medium
`src/wasmintegration.cpp:37-40, 64-88, 164-171`
- **opus:** ⚠️ PARTIAL (50) — global picker state overwritten by re-entrant calls (wasmintegration.cpp:37)
- **gpt:** ⚠️ PARTIAL (58) — observed Global file-picker state overwritten by re-entrant calls - wrong file delivered (src/wasmintegration.cpp:37)
- **deepseek:** ✅ LEGIT (88) — static s_pending* globals no re-entrancy guard; second call overwrites first delivers to wrong target (wasmintegration.cpp:37-40)
- **glm:** ✅ LEGIT (80) — wasmintegration.cpp:37-40 64-88 global file-picker state overwritten by re-entrant calls
- **kimi:** ✅ LEGIT (85) — wasmintegration.cpp:37-40/64-88/164-171 use static s_pending* globals with no reentrancy guard; concurrent picker calls overwrite state.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — global picker state overwritten by re-entrant calls (wasmintegration.cpp:37)

### [WARN-N01] SpellHighlighter::isEnabled() — dead code, never called  ·  _SPLIT_  ·  Low
`spellhighlighter.h:36`
- **opus:** ⚠️ PARTIAL (40) — SpellHighlighter::isEnabled dead, never called (spellhighlighter.h:36)
- **gpt:** ⚠️ PARTIAL (58) — observed SpellHighlighter::isEnabled() - dead code, never called (src/spellhighlighter.h:36)
- **deepseek:** ✅ LEGIT (80) — spellhighlighter.h:36: isEnabled() public method never called anywhere in codebase; setEnabled() is called but isEnabled() is dead code
- **glm:** ✅ LEGIT (75) — spellhighlighter.h:36 isEnabled() dead code never called
- **kimi:** ✅ LEGIT (70) — spellhighlighter.h:36 SpellHighlighter::isEnabled() is defined but never invoked anywhere in the codebase.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — SpellHighlighter::isEnabled dead

### [WARN-N02] SpellChecker::addWord() — dead public API, never called  ·  _SPLIT_  ·  Low
`spellchecker.h:48, spellchecker.cpp:134-140`
- **opus:** ✅ LEGIT (60) — addWord() is dead public API never called (spellchecker.h:48)
- **gpt:** ⚠️ PARTIAL (58) — observed SpellChecker::addWord() - dead public API, never called (src/spellchecker.h:48)
- **deepseek:** ✅ LEGIT (85) — spellchecker.h:48 / spellchecker.cpp:134-140: addWord() full implementation exists but never invoked; DocumentHandler uses addCustomWord() instead — dead public API
- **glm:** ✅ LEGIT (75) — spellchecker.h:48 spellchecker.cpp:134-140 addWord() dead public API never called from DocumentHandler
- **kimi:** ✅ LEGIT (70) — spellchecker.h:48 / spellchecker.cpp:134-140 addWord() is fully implemented but never called; addCustomWord() is used instead.
- **opus-ultra:** ✅ LEGIT (60) — addWord() is dead public API never called (spellchecker.h:48)

### [WARN-N03] quint64→int implicit narrowing in nextMarker()/previousMarker()  ·  _SPLIT_  ·  Low
`documenthandler.cpp:1713,1721`
- **opus:** ⚠️ PARTIAL (45) — quint64->int narrowing (dup INT-N01) (documenthandler.cpp:1713)
- **gpt:** ⚠️ PARTIAL (58) — observed quint64->int implicit narrowing in nextMarker()/previousMarker() (src/documenthandler.cpp:1713)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:1713/1721: Q_INVOKABLE takes quint64 position but MarkersModel::nextMarker/previousMarker accept int (markersmodel.h:62-63); 64->32 bit unsigned->signed truncation
- **glm:** ✅ LEGIT (70) — documenthandler.cpp:1713 1721 quint64→int implicit narrowing in nextMarker()/previousMarker()
- **kimi:** ✅ LEGIT (70) — documenthandler.cpp:1713,1721 pass quint64 position to MarkersModel methods taking int, causing 64->32 narrowing.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — quint64->int narrowing (dup INT-N01) (documenthandler.cpp:1713)

### [WARN-N04] QProcess::startDetached() bool return silently ignored  ·  _SPLIT_  ·  Low
`qmlutil.hpp:91`
- **opus:** ✅ LEGIT (55) — startDetached bool return ignored (qmlutil.hpp:91)
- **gpt:** ⚠️ PARTIAL (58) — observed QProcess::startDetached() bool return silently ignored (src/qmlutil.hpp:91)
- **deepseek:** ✅ LEGIT (95) — qmlutil.hpp:91: QProcess::startDetached() returns bool — discarded; if program not found failure is silent with no error log or QML notification
- **glm:** ✅ LEGIT (70) — qmlutil.hpp:91 QProcess::startDetached() bool return silently ignored
- **kimi:** ✅ LEGIT (70) — qmlutil.hpp:91 discards QProcess::startDetached() return value; failure to launch is silent.
- **opus-ultra:** ✅ LEGIT (55) — startDetached bool return ignored (qmlutil.hpp:91)

### [WATCH-N01] addPath() return never checked — silent watch failure  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1026`
- **opus:** ⚠️ PARTIAL (50) — addPath() return value unchecked (documenthandler.cpp:1026)
- **gpt:** ✅ LEGIT (78) — addPath() return never checked - silent watch failure (src/documenthandler.cpp:1026)
- **deepseek:** ✅ LEGIT (95) — documenthandler.cpp:1026: addPath() bool return discarded; silent failure on unsupported filesystems
- **glm:** ✅ LEGIT (70) — documenthandler.cpp:1026 addPath() return never checked; silent watch failure
- **kimi:** ✅ LEGIT (80) — documenthandler.cpp:1026 calls _fileSystemWatcher->addPath(fileName) without checking bool return.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — addPath() return value unchecked (documenthandler.cpp:1026)

### [WATCH-N02] removePath() return never checked — stale path causes double-watch  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1024`
- **opus:** ⚠️ PARTIAL (50) — removePath() return value unchecked (documenthandler.cpp:1024)
- **gpt:** ✅ LEGIT (78) — removePath() return never checked - stale path causes double-watch (src/documenthandler.cpp:1024)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:1024: removePath() return unchecked; stale path stays watched causing double-watch on fileChanged
- **glm:** ✅ LEGIT (70) — documenthandler.cpp:1024 removePath() return never checked; stale path causes double-watch
- **kimi:** ✅ LEGIT (80) — documenthandler.cpp:1024 calls removePath(...) with no return check; stale watch possible.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — removePath() return value unchecked (documenthandler.cpp:1024)

### [WATCH-N03] Watcher not refreshed after fileChanged — stale inotify on Linux atomic saves  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:857-864,1020-1027`
- **opus:** ❔ UNSURE (45) — watcher stale after atomic-save inotify swap; Linux-specific (documenthandler.cpp:857)
- **gpt:** ✅ LEGIT (78) — Watcher not refreshed after fileChanged - stale inotify on Linux atomic saves (src/documenthandler.cpp:857)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:857-864: reload() loads document but watcher not re-added after fileChanged; next atomic save undetected
- **glm:** ✅ LEGIT (75) — documenthandler.cpp:857-864 1020-1027 watcher not refreshed after fileChanged; stale inotify on Linux atomic saves
- **kimi:** ✅ LEGIT (70) — documenthandler.cpp reload() / load() calls removePath/addPath on new path but fileChanged handler does not re-add; atomic-save inode change can lose events.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — watcher stale after atomic-save inotify swap; Linux-specific (documenthandler.cpp:857)

### [WATCH-N04] unblockFileWatcher() dereferences _fileSystemWatcher without null guard  ·  _SPLIT_  ·  Low
`documenthandler.cpp:1125-1128`
- **opus:** ⚠️ PARTIAL (45) — _fileSystemWatcher always constructed in ctor; null-deref unlikely (documenthandler.cpp:1125)
- **gpt:** ✅ LEGIT (78) — unblockFileWatcher() dereferences _fileSystemWatcher without null guard (src/documenthandler.cpp:1125)
- **deepseek:** ✅ LEGIT (85) — documenthandler.cpp:1125-1128: _fileSystemWatcher dereferenced without null guard; reachable via QTimer::singleShot from saveAs()
- **glm:** ✅ LEGIT (70) — documenthandler.cpp:1125-1128 unblockFileWatcher() dereferences _fileSystemWatcher without null guard
- **kimi:** ✅ LEGIT (85) — documenthandler.cpp:1125-1127 unblockFileWatcher derefs _fileSystemWatcher without null check.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — _fileSystemWatcher always constructed in ctor; null-deref unlikely (documenthandler.cpp:11

### [WINDOW-N01] Projection windows not closed on main window close — orphaned on Linux  ·  _SPLIT_  ·  Medium
`main.qml:159-165, +windows:154-160, +android:144-150`
- **opus:** ⚠️ PARTIAL (50) — projection windows may orphan on main-window close; lifecycle (main.qml:159)
- **gpt:** ⚠️ PARTIAL (58) — observed Projection windows not closed on main window close - orphaned on Linux (src/kirigami_ui/main.qml:159)
- **deepseek:** ✅ LEGIT (85) — main.qml:159-165/+android:144-150/+windows:154-160: onClosing only handles save dialog; no projectionManager.closeAll() or isEnabled=false — orphaned projection windows on Linux
- **glm:** ✅ LEGIT (75) — main.qml:159-165 projection windows not closed on main window close; orphaned on Linux
- **kimi:** ✅ LEGIT (85) — main.qml/+windows/+android onClosing handlers never close projectionManager windows.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — projection windows may orphan on main-window close; lifecycle (main.qml:159)

### [WSM-03] readAsDataURL causes quadruple in-memory copy of file content  ·  _SPLIT_  ·  High
`wasmintegration.cpp:129-144`
- **opus:** ⚠️ PARTIAL (50) — readAsDataURL -> base64+encode+malloc multiple copies; large-file memory (wasmintegration.cpp:129)
- **gpt:** ⚠️ PARTIAL (58) — observed readAsDataURL causes quadruple in-memory copy of file content (src/wasmintegration.cpp:129)
- **deepseek:** ✅ LEGIT (88) — readAsDataURL base64(+33%)->TextEncoder->malloc+HEAPU8->QString::fromUtf8; quadruple copy high memory (wasmintegration.cpp:129-144)
- **glm:** ⚠️ PARTIAL (65) — wasmintegration.cpp:129-144 readAsDataURL causes multiple in-memory copies; performance issue
- **kimi:** ✅ LEGIT (80) — wasmintegration.cpp:129-144 uses readAsDataURL then TextEncoder, causing base64+UTF-8 copies and large peak memory for big files.
- **opus-ultra:** ✅ LEGIT (68) — max: real defect; severity is a separate axis (was PARTIAL) — readAsDataURL -> base64+encode+malloc multiple copies; large-file memory (wasmintegration.

### [WYS-N02] Default stylesheet CSS errors: valign:top (not a CSS property) and border:1pt (missing style)  ·  _SPLIT_  ·  Low
`documenthandler.cpp:188`
- **opus:** ✅ LEGIT (70) — valign:top not a CSS prop; border:1pt malformed in default stylesheet (documenthandler.cpp:188)
- **gpt:** ⚠️ PARTIAL (58) — observed Default stylesheet CSS errors: valign:top (not a CSS property) and border:1pt (missing style) (src/documenthandler.cpp:188)
- **deepseek:** ✅ LEGIT (85) — documenthandler.cpp:188: valign:top not valid CSS (should be vertical-align:top); border:1pt missing style keyword (e.g. solid)
- **glm:** ✅ LEGIT (70) — documenthandler.cpp:188 CSS errors: valign:top not a CSS property and border:1pt missing style
- **kimi:** ✅ LEGIT (95) — documenthandler.cpp:188 has `border:1pt;valign:top;`; `valign` is not CSS and `border` lacks a style keyword
- **opus-ultra:** ✅ LEGIT (70) — valign:top not a CSS prop; border:1pt malformed in default stylesheet (documenthandler.cpp:188)

### [XFRM-N01] PrompterView.qml Rotation permanently overridden by PrompterPage.qml  ·  _SPLIT_  ·  Low
`PrompterView.qml:53-58 vs PrompterPage.qml:750-765`
- **opus:** ❔ UNSURE (45) — PrompterView Rotation overridden by PrompterPage; domain (PrompterView.qml:53)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/PrompterView.qml:53)
- **deepseek:** ⚠️ PARTIAL (45) — Rotation overridden by PrompterPage is expected parent-child transform layering (PrompterView.qml:53-58)
- **glm:** ⚠️ PARTIAL (60) — PrompterView.qml:53-58 vs PrompterPage.qml:750-765 Rotation permanently overridden by PrompterPage
- **kimi:** ✅ LEGIT (85) — PrompterView.qml:53-58 defines a Rotation transform, but PrompterPage.qml:750-765 sets transform on the same viewport, overriding it.
- **opus-ultra:** ❔ UNSURE (45) — max: unverifiable statically (runtime/semantic) — PrompterView Rotation overridden by PrompterPage; domain (PrompterView.qml:53)

### [Z-N04] PrompterBackground (z:0) renders above viewport.mouse (z:0) — latent input intercept  ·  _SPLIT_  ·  Low
`PrompterView.qml:249,320`
- **opus:** ⚠️ PARTIAL (45) — PrompterBackground z:0 vs viewport.mouse z:0; order-dependent (PrompterView.qml:249)
- **gpt:** ✅ LEGIT (78) — PrompterBackground (z:0) renders above viewport.mouse (z:0) - latent input intercept (src/prompter/PrompterView.qml:249)
- **deepseek:** ✅ LEGIT (65) — PrompterBackground(z:0) declared after MouseArea(z:0) renders on top intercepting input (PrompterView.qml:249 320)
- **glm:** ⚠️ PARTIAL (55) — PrompterView.qml:249 320 PrompterBackground z:0 and viewport.mouse z:0; latent input intercept
- **kimi:** ⚠️ PARTIAL (50) — Both PrompterBackground and viewport.mouse default to z:0; rendering/input order follows declaration, intercept not proven.
- **opus-ultra:** ⚠️ PARTIAL (50) — max: real but non-behavioral (style/arch/non-issue) — PrompterBackground z:0 vs viewport.mouse z:0; order-dependent (PrompterView.qml:249)

