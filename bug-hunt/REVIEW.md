# Multi-Agent Bug Review — QPrompt

_723 findings · agents: opus, gpt, deepseek, glm, kimi, opus-ultra_

Bird's-eye matrix + divergences. Per-bug detail (incl. each agent's full rationale, the original claim, and the patch workspace) lives in `findings/<ID>.md`; the work queue is `BACKLOG.md`.

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

## Matrix

| ID | Sev | opus | gpt | deepseek | glm | kimi | opus-ultra | Consensus | Title |
|---|---|---|---|---|---|---|---|---|---|
| MEM-01 | High | ✅100 | ✅88 | ✅90 | ✅90 | ✅95 | ✅100 | AGREE | Memory Leak: `_markersModel` allocated without parent, never deleted |
| MEM-02 | High | ✅100 | ✅88 | ✅90 | ✅90 | ✅95 | ✅100 | AGREE | Memory Leak: `_fileSystemWatcher` allocated without parent, never deleted |
| MEM-03 | Medium | ✅100 | ✅88 | ✅85 | ✅85 | ✅90 | ✅100 | AGREE | Memory Leak: `m_fontDialog` allocated without parent, never deleted |
| LOG-01 | High | ✅100 | ✅92 | ✅95 | ✅90 | ✅95 | ✅100 | AGREE | SessionModel::rowCount returns m_data.size() for both valid and invalid parents |
| LOG-02 | High | ✅95 | ✅92 | ✅95 | ✅90 | ✅95 | ✅95 | AGREE | Off-by-one: beginRemoveRows uses rowCount() instead of rowCount()-1 |
| LOG-03 | Medium | ✅100 | ✅78 | ✅98 | ✅95 | ✅95 | ✅100 | AGREE | MarkersModel::data returns data.position for LengthRole instead of data.length |
| LOG-04 | Medium | ✅100 | ✅78 | ⚠️60 | ✅85 | ✅85 | ✅100 | split | MarkersModel::extendLastMarker modifies data without emitting dataChanged |
| LOG-05 | Medium | ✅100 | ✅78 | ✅88 | ✅90 | ✅90 | ✅100 | AGREE | DocumentHandler::search ignores `loop` parameter when `regEx` is true |
| LOG-06 | Medium | ✅90 | ✅78 | ⚠️70 | ✅85 | ✅85 | ✅90 | split | DocumentHandler::replaceAll has potential infinite loop with regex |
| LOG-07 | Low | ⚠️60 | ⚠️52 | ⚠️50 | ⚠️60 | ✅70 | ⚠️50 | split | namedMarker() fetches cursor twice — stale-content risk |
| LOG-08 | Low | ✅100 | ✅88 | ✅85 | ⚠️55 | ✅90 | ✅100 | split | DataPoint default constructor leaves three members uninitialized |
| LOG-09 | Low | ❌95 | ❌76 | ❌80 | ❌80 | ✅75 | ❌95 | **CONFLICT** | Trailing comma in constructor member initializer list (non-standard C++ before C++20) |
| QML-01 | Critical | ❌90 | ❌90 | ❔30 | ❌85 | ✅90 | ❌90 | **CONFLICT** | 26 references to undefined `pointerSettings` ID in ReadRegionOverlay |
| QML-02 | Critical | ❌90 | ❌90 | ❔30 | ❌85 | ✅90 | ❌90 | **CONFLICT** | Undefined `pointerConfiguration` ID reference in ReadRegionOverlay |
| QML-03 | Critical | ✅95 | ✅92 | ✅75 | ❌80 | ✅90 | ✅95 | **CONFLICT** | Undefined `root` ID in WindowDragger.qml |
| QML-04 | High | ✅100 | ✅92 | ✅90 | ✅95 | ✅95 | ✅100 | AGREE | Typo: `verticalCentertop` instead of `verticalCenter` |
| QML-05 | High | ✅100 | ✅84 | ✅95 | ✅90 | ✅95 | ✅100 | AGREE | `&&` should be `\|\|` in clear button enabled condition |
| QML-06 | High | ✅100 | ✅84 | ✅90 | ✅85 | ✅95 | ✅100 | AGREE | Bitwise OR (`\|`) instead of AND (`&`) in modifier key check |
| QML-07 | High | ❌95 | ❌90 | ❌85 | ⚠️60 | ❌85 | ❌95 | split | `Text.CurveRendering` enum requires Qt >= 6.7 |
| QML-08 | Medium | ❌80 | ❌76 | ❔40 | ❌80 | ✅90 | ❌80 | **CONFLICT** | Invalid anchor target `undefined` |
| QML-09 | Medium | ❌95 | ❌90 | ❌85 | ⚠️55 | ❌85 | ❌95 | split | `QtQuick.Shapes 6.6` version mismatch with `QtCore 6.5` |
| QML-10 | Medium | ❌85 | ❌76 | ❔45 | ✅80 | ✅90 | ❌85 | **CONFLICT** | `+android/main.qml` missing `QmlUtil` for RecentDocuments |
| QML-11 | Medium | ✅90 | ⚠️58 | ✅85 | ⚠️70 | ✅75 | ✅90 | split | Dead code: `window` property declared but never used in WindowDragger |
| SEC-01 | Critical | ✅95 | ✅84 | ✅75 | ✅85 | ✅95 | ✅95 | AGREE | Arbitrary Command Execution via `sys://` Marker URIs |
| SEC-02 | Medium | ✅85 | ✅78 | ✅90 | ✅85 | ✅85 | ✅85 | AGREE | OBS WebSocket Password Stored in Plaintext |
| SEC-03 | Medium | ✅95 | ✅78 | ✅80 | ✅90 | ✅90 | ✅95 | AGREE | Information Disclosure: Full HTML Document Content Logged via qDebug |
| SEC-04 | High | ⚠️55 | ⚠️58 | ✅85 | ✅85 | ✅90 | ⚠️50 | split | SSRF / URL Injection — User-Controlled URL Passed to Network Loader |
| SEC-05 | Medium | ⚠️55 | ⚠️58 | ✅70 | ⚠️70 | ✅85 | ⚠️50 | split | User-Controlled Filename Passed to QProcess (LibreOffice import) |
| RES-01 | High | ✅95 | ✅84 | ✅90 | ✅85 | ✅90 | ✅95 | AGREE | Network reply overwritten without aborting previous download |
| RES-02 | High | ✅95 | ✅84 | ✅92 | ✅90 | ✅90 | ✅95 | AGREE | loadFromNetworkFinihed ignores the QNetworkReply* signal parameter |
| RES-03 | Low | ⚠️65 | ⚠️58 | ✅85 | ⚠️60 | ✅80 | ⚠️50 | split | ShakeDetector::s_instance never set to nullptr on destruction (dangling pointer) |
| RES-04 | Low | ⚠️65 | ⚠️58 | ✅85 | ⚠️60 | ✅80 | ⚠️50 | split | IosSaveDialog::s_instance same singleton dangling pattern |
| RES-05 | Low | ❌80 | ❌76 | ❌75 | ❌80 | ❌70 | ❌80 | AGREE | QTextStream left unflushed before QFile destruction |
| TYP-01 | High | ❌80 | ❔39 | ✅95 | ✅85 | ✅95 | ❌80 | **CONFLICT** | Dangling pointer from temporary std::string in SpellChecker::loadOne |
| TYP-02 | Medium | ❌90 | ❌76 | ✅90 | ⚠️55 | ✅90 | ❌90 | **CONFLICT** | Invalid Qt::LayoutDirection enum value cast |
| TYP-03 | Medium | ⚠️60 | ⚠️58 | ✅85 | ✅85 | ✅85 | ⚠️50 | split | Floating-point equality comparison of window opacity |
| TYP-04 | Medium | ✅95 | ⚠️58 | ✅90 | ✅85 | ✅90 | ✅95 | split | Bitwise AND on bools hides dead code in preventSleep |
| TYP-05 | Medium | ✅95 | ✅88 | ⚠️60 | ✅90 | ✅90 | ✅95 | split | Uninitialized pointer member m_reply in DocumentHandler |
| TYP-06 | Low | ✅95 | ⚠️58 | ✅85 | ❌75 | ✅90 | ✅95 | **CONFLICT** | Malformed preprocessor macro: `#define Use_GlobalAccel = 1` |
| TYP-07 | Low | ✅90 | ⚠️58 | ⚠️30 | ✅75 | ✅70 | ✅90 | split | Narrowing conversion: `size_t` → `int` in SpellChecker::decode |
| TYP-08 | Low | ❌95 | ❌76 | ❌80 | ❌85 | ✅75 | ❌95 | **CONFLICT** | DocumentHandler constructor trailing comma in initializer list |
| TYP-09 | Low | ❌90 | ❌76 | ⚠️40 | ⚠️55 | ❌80 | ❌90 | split | Null pointer dereferences in emit textChanged related to uninitialized m_document |
| TYP-10 | Low | ❌55 | ❌76 | ❌60 | ✅80 | ❌85 | ❌55 | **CONFLICT** | Uninitialized marker struct fields: length defaults to 1 |
| EDGE-01 | High | ✅95 | ✅84 | ✅95 | ✅85 | ✅90 | ✅95 | AGREE | QString::arg() called on string with no placeholder — program name silently dropped |
| EDGE-02 | High | ✅95 | ✅84 | ✅90 | ✅85 | ✅90 | ✅95 | AGREE | Empty container `first()` dereference — crash on hotkey with no windows |
| EDGE-03 | High | ✅90 | ✅84 | ✅85 | ✅90 | ✅90 | ✅90 | AGREE | Empty container `last()` dereference in `extendLastMarker` |
| EDGE-04 | Critical | ✅90 | ✅88 | ✅92 | ✅90 | ✅95 | ✅90 | AGREE | Null pointer dereference: `document()->textDocument()` not checked before `load()` |
| EDGE-05 | Critical | ✅90 | ✅88 | ✅92 | ✅90 | ✅95 | ✅90 | AGREE | Null pointer dereference: `textDocument()` unchecked in `search()` |
| EDGE-06 | Critical | ✅90 | ✅88 | ✅92 | ✅90 | ✅95 | ✅90 | AGREE | Null pointer dereference: `textDocument()` unchecked in `parse()` |
| EDGE-07 | High | ⚠️60 | ⚠️58 | ✅85 | ⚠️60 | ✅90 | ⚠️50 | split | Q_UNREACHABLE in Q_INVOKABLE method — UB if called from QML |
| EDGE-08 | Medium | ❌80 | ❌76 | ✅75 | ✅85 | ✅80 | ❌80 | **CONFLICT** | Q_ASSERT as thread-safety guard — removed in release builds |
| EDGE-09 | Medium | ✅90 | ✅88 | ✅85 | ✅75 | ✅85 | ✅90 | AGREE | QFile::copy() return value silently ignored |
| EDGE-10 | Low | ❌85 | ⚠️58 | ⚠️50 | ✅80 | ✅70 | ❌85 | **CONFLICT** | globalShortcutKey() switch without default — fallthrough to Q_UNREACHABLE |
| EDGE-11 | Medium | ⚠️60 | ⚠️58 | ✅85 | ✅85 | ✅80 | ⚠️50 | split | m_reply dereference without null check in loadFromNetworkFinihed() |
| EDGE-12 | Low | ⚠️40 | ⚠️58 | ❌40 | ⚠️60 | ✅60 | ❌72 | **CONFLICT** | QTextBlock::iterator scope fragility in parse() |
| PLAT-01 | High | ✅90 | ⚠️58 | ✅90 | ⚠️65 | ✅90 | ✅90 | split | KF6Crash_FOUND never defined as C preprocessor macro — KCrash support dead code |
| PLAT-02 | Medium | ✅90 | ✅78 | ✅85 | ✅85 | ✅85 | ✅90 | AGREE | REQUIRED_KF6_VERSION variable referenced but never defined |
| PLAT-03 | High | ✅85 | ✅84 | ❔50 | ✅85 | ✅90 | ✅85 | split | Wrong target name and wrong include path for KDMacTouchBar |
| PLAT-04 | Medium | ❌95 | ❌90 | ❔40 | ✅80 | ❌90 | ❌95 | **CONFLICT** | DS_Store.scpt referenced but file does not exist |
| PLAT-05 | Medium | ✅85 | ✅92 | ✅85 | ❌85 | ✅85 | ✅85 | **CONFLICT** | DBINARY_ICONS_RESOURCE is a typo — should be BINARY_ICONS_RESOURCE |
| PLAT-06 | Low | ✅90 | ✅78 | ✅80 | ✅80 | ✅80 | ✅90 | AGREE | qprompt_QM_LOADER variable never defined |
| PLAT-07 | Low | ✅95 | ⚠️58 | ✅85 | ❌75 | ✅90 | ✅95 | **CONFLICT** | Incorrect macro syntax: `#define Use_GlobalAccel = 1` |
| PLAT-08 | Medium | ⚠️50 | ⚠️58 | ✅85 | ⚠️55 | ✅85 | ⚠️50 | split | QNX platform guard inconsistency: main.cpp vs documenthandler.h |
| PLAT-09 | Low | ❔45 | ❔39 | ❔30 | ✅80 | ✅75 | ❔45 | split | Pre-build manifest references invalid Android SDK paths |
| R2-GH-01 | High | ❌80 | ❌76 | ✅80 | ✅80 | ✅85 | ❌80 | **CONFLICT** | Q_UNREACHABLE reachable when only QHotkey available on Wayland |
| R2-CMAKE-01 | Critical | ❌80 | ❌76 | ✅90 | ✅85 | ✅95 | ❌80 | **CONFLICT** | sphinx_add_docs silently ignores all keyword arguments due to empty cmake_parse_arguments prefix |
| R2-CMAKE-02 | High | ✅80 | ✅84 | ✅90 | ⚠️60 | ✅90 | ✅80 | split | cmake_minimum_required inside find module pollutes parent project policy settings |
| R2-CMAKE-03 | Medium | ✅80 | ✅78 | ✅85 | ❌80 | ✅85 | ✅80 | **CONFLICT** | WORKING_DIRECTORY and COMMENT not parseable by callers of sphinx_add_docs |
| R2-CMAKE-04 | Medium | ✅80 | ✅78 | ✅80 | ✅80 | ✅80 | ✅80 | AGREE | QML icon file(GLOB_RECURSE) missing CONFIGURE_DEPENDS causes stale icon sets |
| R2-PRP-01 | Medium | ✅80 | ✅78 | ❔45 | ✅90 | ✅90 | ✅80 | split | Qt.LeftToRight used as bare boolean — RTL branch always dead |
| R2-PRP-02 | Medium | ✅85 | ✅92 | ❔40 | ✅85 | ✅90 | ✅85 | split | Kirigami.Units.SmallSpacing — uppercase S yields undefined |
| R2-PRP-03 | Medium | ❌75 | ⚠️58 | ❔40 | ✅85 | ✅90 | ❌75 | **CONFLICT** | Units.LongDuration / Units.HumanMoment missing Kirigami. prefix |
| R2-PRP-04 | Low | ⚠️50 | ⚠️58 | ❔35 | ⚠️55 | ✅75 | ✅68 | split | Inconsistent focus restoration in decreaseVelocityButton |
| R2-PRP-05 | Low | ⚠️45 | ⚠️52 | ❔30 | ✅80 | ✅80 | ✅68 | split | Potential null-item access on async Loader in namedMarkerConfiguration.onOpened |
| R2-PTR-01 | Medium | ❌75 | ❌76 | ✅80 | ⚠️60 | ✅90 | ❌75 | **CONFLICT** | Type mismatch: textVerticalOffset declared int but fed a real |
| R2-PTR-02 | Medium | ❌75 | ❌76 | ✅80 | ⚠️60 | ✅90 | ❌75 | **CONFLICT** | Type mismatch: imageVerticalOffset declared int but fed a real |
| R2-PTR-03 | Medium | ✅80 | ✅78 | ❔40 | ✅85 | ✅85 | ✅80 | split | Casing error: Units.longDuration should be Units.LongDuration |
| R2-PTR-04 | Medium | ✅85 | ✅78 | ❔35 | ✅85 | ✅90 | ✅85 | split | Inverted indexOf truthiness in platform check for ColorDialog |
| R2-AND-01 | Critical | ✅90 | ⚠️58 | ❔35 | ✅85 | ✅95 | ✅90 | split | Android missing QmlUtil causes crash on factory reset and RecentDocuments |
| R2-AND-02 | Critical | ✅90 | ✅84 | ❔35 | ✅80 | ✅95 | ✅90 | split | Android missing restartDialog crashes LanguageSettingsOverlay and LayoutDirectionSettingsOverlay |
| R2-AND-03 | Medium | ✅80 | ✅78 | ❔35 | ✅80 | ✅80 | ✅80 | split | Android Settings missing fakeFullScreen persistence |
| R2-AND-04 | Low | ⚠️45 | ⚠️58 | ❔30 | ✅75 | ✅70 | ✅68 | split | Android Settings for "background" missing transparency persistence |
| R2-AND-05 | Low | ⚠️45 | ⚠️58 | ❔25 | ✅80 | ✅60 | ✅68 | split | Android loadTelemetryPage passes no properties object to pageStack push |
| R2-OVL-01 | Medium | ⚠️65 | ⚠️58 | ❔35 | ✅85 | ✅85 | ✅68 | split | InputsOverlay onOpened calls cursorAutoHide.restart() instead of reset() |
| R2-OVL-02 | Low | ✅85 | ✅78 | ❔35 | ✅80 | ✅80 | ✅85 | split | LanguageSettingsOverlay popup ListView currentIndex always resolves to -1 |
| R2-PTH-01 | Medium | ✅85 | ✅78 | ✅80 | ✅80 | ✅85 | ✅85 | AGREE | FileDialog filter matches all files on Linux due to stray glob |
| R2-PTH-02 | Medium | ✅85 | ✅78 | ✅80 | ✅85 | ✅85 | ✅85 | AGREE | File path from file:// URL preserves percent-encoding |
| R2-WHE-01 | High | ✅90 | ✅84 | ✅85 | ✅85 | ✅90 | ✅90 | AGREE | `focus: true` is JavaScript label, not assignment |
| R2-EDT-01 | Medium | ✅90 | ✅92 | ❔40 | ✅95 | ✅90 | ✅90 | split | Qt.AlignHustify typo — nonexistent enum value |
| R2-EDT-02 | High | ✅85 | ✅84 | ❔35 | ✅90 | ✅90 | ✅85 | split | wheelThrottleSettingsButton checked bound to completely unrelated document property |
| R2-EDT-03 | High | ✅80 | ✅84 | ⚠️55 | ✅85 | ✅90 | ✅80 | split | Checkable ToolButtons break checked property bindings on first click — systematic |
| R2-TEL-01 | Medium | ✅80 | ✅78 | ❔35 | ✅85 | ✅85 | ✅80 | split | Telemetry sub-toggles permanently disconnect from master toggle on click |
| R2-REC-01 | Low | ✅85 | ✅92 | ⚠️60 | ⚠️60 | ✅80 | ✅85 | split | File URI prefix strip off-by-one on Windows |
| R2-REC-02 | Medium | ⚠️50 | ⚠️58 | ❔30 | ✅80 | ✅75 | ✅68 | split | refreshExistence skips UI updates when dynamic children out of sync |
| R2-IOS-01 | High | ✅80 | ✅84 | ❔40 | ⚠️65 | ✅85 | ✅80 | split | Method swizzling re-entry causes infinite recursion on second invocation |
| R2-IOS-02 | Medium | ⚠️50 | ❔39 | ❔40 | ✅80 | ✅80 | ⚠️50 | split | Delegate block captures raw assign pointer — use-after-free risk |
| R2-IOS-03 | Medium | ✅85 | ✅78 | ✅75 | ✅80 | ✅80 | ✅85 | AGREE | UIApplication.keyWindow deprecated since iOS 13; breaks multi-window iPadOS |
| R2-WASM-01 | Medium | ✅85 | ✅78 | ❔35 | ⚠️65 | ✅85 | ✅85 | split | File input element never removed from DOM on user cancel |
| R2-WASM-02 | Medium | ✅85 | ✅78 | ❔35 | ✅85 | ✅85 | ✅85 | split | Insecure hostname validation via endsWith allows subdomain spoofing |
| R2-FONT-01 | Medium | ✅85 | ✅78 | ✅75 | ✅80 | ✅75 | ✅85 | AGREE | RichText label renders unescaped plain text — HTML metacharacters break display |
| R2-FONT-02 | Low | ✅85 | ✅92 | ✅95 | ✅90 | ✅90 | ✅85 | AGREE | Duplicate setText call on preview label |
| R2-ANDMAN-01 | Medium | ✅85 | ✅78 | ✅90 | ✅80 | ✅85 | ✅85 | AGREE | Ungrantable system/signature permissions bloating manifest |
| R2-ANDMAN-02 | Medium | ✅85 | ✅78 | ✅90 | ✅80 | ⚠️55 | ✅85 | split | MANAGE_EXTERNAL_STORAGE likely triggers Play Store scrutiny |
| R3-CTX-01 | Critical | ✅90 | ✅92 | ✅95 | ✅90 | ✅85 | ✅90 | AGREE | AbstractUnits missing QML_ELEMENT — all duration constants resolve to undefined |
| R3-CTX-02 | High | ✅90 | ✅84 | ✅98 | ✅85 | ✅90 | ✅90 | AGREE | GlobalHotkeys.SkipForward enum value mismatch — trailing 's' missing |
| R3-DOC-01 | Critical | ✅90 | ✅92 | ✅85 | ✅90 | ✅90 | ✅90 | AGREE | m_reloading uninitialized — undefined behavior on first load |
| R3-DOC-02 | Critical | ❌85 | ❌76 | ✅90 | ✅85 | ❌60 | ❌85 | **CONFLICT** | Unbalanced edit block in setLineHeight/setParagraphHeight |
| R3-DOC-03 | High | ✅85 | ✅84 | ✅90 | ✅85 | ✅85 | ✅85 | AGREE | load() sets m_fileUrl and emits fileUrlChanged even on failed load |
| R3-DOC-04 | High | ✅90 | ✅84 | ✅95 | ✅85 | ✅85 | ✅90 | AGREE | saveAs() silently ignores write/flush failures |
| R3-DOC-05 | High | ✅85 | ✅84 | ✅90 | ✅80 | ✅80 | ✅85 | AGREE | updateContents() produces two separate undo entries — undo destroys document |
| R3-DOC-06 | Medium | ✅90 | ✅78 | ✅85 | ✅80 | ✅90 | ✅90 | AGREE | reload() leaks m_reloading=true on URL mismatch |
| R3-DOC-07 | High | ✅85 | ✅84 | ✅90 | ✅85 | ✅85 | ✅85 | AGREE | Inverted selection state after failed search() |
| R3-SPL-01 | Medium | ✅70 | ✅78 | ✅80 | ⚠️65 | ✅75 | ✅70 | split | encode() uses toLocal8Bit() instead of dictionary-encoding-aware conversion |
| R3-SPL-02 | Medium | ✅70 | ✅78 | ✅80 | ⚠️65 | ✅75 | ✅70 | split | decode() uses fromLocal8Bit() — suggestions show as mojibake |
| R3-SPL-03 | Medium | ❌80 | ❌76 | ✅90 | ✅80 | ✅80 | ❌80 | **CONFLICT** | removeCustomWord() silently discards all addWord() additions |
| R3-SPL-04 | Medium | ✅75 | ✅78 | ✅90 | ✅80 | ✅70 | ✅75 | AGREE | Corrupt cached dictionary file persists permanently after failed copy |
| R3-SPL-05 | Medium | ⚠️45 | ⚠️58 | ✅85 | ✅85 | ⚠️55 | ⚠️50 | split | SpellChecker has zero thread safety — all methods unprotected |
| R3-MAIN-01 | Medium | ❌75 | ✅78 | ✅85 | ✅80 | ✅85 | ❌75 | **CONFLICT** | Command-line positional argument description/syntax swapped |
| R3-MAIN-02 | High | ⚠️55 | ⚠️58 | ✅90 | ✅85 | ✅75 | ✅68 | split | Invalid locale string constructed for short language codes |
| R3-MAIN-03 | Medium | ✅85 | ✅78 | ✅95 | ✅85 | ✅80 | ✅85 | AGREE | System locale changed even when translation file fails to load |
| R3-MAIN-04 | Low | ❌85 | ❌76 | ⚠️60 | ⚠️60 | ❌65 | ❌85 | split | Stack-allocated QTranslator outlives QApplication on shutdown |
| R3-MAIN-05 | Medium | ✅80 | ⚠️58 | ✅98 | ✅80 | ✅85 | ✅80 | split | Hardcoded Homebrew version-specific Kirigami import path |
| R3-MAIN-06 | High | ✅90 | ✅84 | ✅90 | ⚠️55 | ✅75 | ✅90 | split | Inconsistent Kirigami platform guards — missing WATCHOS and QNX |
| R3-MAIN-07 | Medium | ✅90 | ✅78 | ✅98 | ✅85 | ✅80 | ✅90 | AGREE | XDG_CURRENT_DESKTOP unconditionally forced to "KDE" on all Linux |
| R3-MAIN-08 | Low | ✅55 | ✅78 | ✅80 | ⚠️60 | ✅65 | ✅55 | split | QFontDatabase::addApplicationFont return value discarded |
| R3-APP-01 | Low | ❌75 | ❌76 | ❌85 | ⚠️60 | ✅80 | ❌75 | **CONFLICT** | AppController singleton and children never deallocated |
| R3-PROP-01 | Medium | ✅80 | ✅78 | ✅80 | ⚠️65 | ✅85 | ✅80 | split | selectionIsLowerCase bound to wrong NOTIFY signal |
| R3-SIG-01 | Low | ✅85 | ✅78 | ✅90 | ✅80 | ✅95 | ✅85 | AGREE | textChanged() signal declared but never emitted |
| R3-SIG-02 | Medium | ❌85 | ❌90 | ⚠️85 | ✅85 | ❌85 | ❌85 | **CONFLICT** | ShakeDetector signals declared but never emitted — dead feature |
| R3-SIG-03 | Medium | ❌90 | ❌90 | ✅75 | ✅85 | ❌85 | ❌90 | **CONFLICT** | IosSaveDialog accepted/rejected signals declared but never emitted |
| R3-PMT-01 | High | ⚠️60 | ⚠️58 | ✅95 | ✅85 | ✅95 | ✅68 | split | OBS WebSocket JSON.parse without try/catch — crash on malformed input |
| R3-PMT-02 | Medium | ✅60 | ✅78 | ✅90 | ✅80 | ✅90 | ✅60 | AGREE | OBS WebSocket no onError handler, no reconnection logic |
| R3-PMT-03 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅75 | ✅90 | ⚠️50 | split | goToNextMarker fallback desynchronizes cursor from viewport |
| R3-TMR-01 | Medium | ❔45 | ❔39 | ✅80 | ✅85 | ✅95 | ❔45 | split | TimerClock ETA uses __iDefault instead of actual __i during reverse scroll |
| R4-QTV-01 | Critical | ❌90 | ❌76 | ✅95 | ❌80 | ✅80 | ❌90 | **CONFLICT** | QtQuick 2.13 import does not exist in Qt 6.5 |
| R4-QTV-02 | Critical | ❌90 | ❌76 | ❔60 | ❌80 | ✅80 | ❌90 | **CONFLICT** | QtQuick.Window 2.0 import does not exist in Qt 6.5 |
| R4-QTV-03 | High | ❌90 | ❌76 | ❌98 | ❌75 | ❌90 | ❌90 | AGREE | QtQuick.Dialogs 6.6 imported in 9 files on Qt 6.5 target |
| R4-EXP-01 | Critical | ⚠️55 | ⚠️58 | ✅95 | ✅85 | ✅85 | ✅68 | split | No XSS sanitization — script tags, event handlers, javascript: URLs unfiltered |
| R4-EXP-02 | High | ✅90 | ✅84 | ✅95 | ✅85 | ✅95 | ✅90 | AGREE | insertHtmlAt() bypasses filterHtml() — unsanitized HTML from QML |
| R4-EXP-03 | High | ✅85 | ✅84 | ✅90 | ✅85 | ✅95 | ✅85 | AGREE | loadFromNetwork() destroys URL for relative URLs — host/path swapped |
| R4-EXP-04 | High | ✅80 | ✅84 | ✅90 | ✅80 | ✅90 | ✅80 | AGREE | AutoText inserts plain text as HTML — content corruption |
| R4-EXP-05 | Medium | ✅70 | ✅78 | ✅90 | ✅85 | ✅80 | ✅70 | AGREE | No encoding/charset detection — all imports assumed UTF-8 |
| R4-EXP-06 | Medium | ✅70 | ✅78 | ✅95 | ✅80 | ✅80 | ✅70 | AGREE | UTF-8 BOM not stripped — becomes phantom character at position 0 |
| R4-EXP-07 | Medium | ✅60 | ✅78 | ✅90 | ✅80 | ✅90 | ✅60 | AGREE | data: URI assumes base64 encoding without checking ;base64 token |
| R4-EXP-08 | Medium | ✅85 | ✅78 | ✅90 | ✅85 | ✅90 | ✅85 | AGREE | EPUB/MOBI/AZW import replaces document with error string |
| R4-EXP-09 | Low | ⚠️55 | ⚠️58 | ✅85 | ⚠️65 | ✅85 | ✅68 | split | LibreOffice import --cat and --convert-to flags are contradictory |
| R4-ROOT-01 | High | ✅90 | ✅84 | ✅95 | ✅85 | ✅95 | ✅90 | AGREE | Qt.openUrlExternally called with translation context string instead of URL |
| R4-ROOT-02 | Medium | ✅85 | ✅92 | ✅95 | ✅85 | ✅90 | ✅85 | AGREE | Invalid QML color value "initial" |
| R4-ROOT-03 | Medium | ❌80 | ❌76 | ✅90 | ⚠️65 | ✅90 | ❌80 | **CONFLICT** | ESC global shortcut skips single-layer pages — can't dismiss with keyboard |
| R4-ROOT-04 | Medium | ✅90 | ✅92 | ✅98 | ✅85 | ✅95 | ✅90 | AGREE | Duplicate "&Open" menu item in native File menu |
| R4-ROOT-05 | Low | ⚠️50 | ✅92 | ✅95 | ⚠️60 | ✅90 | ⚠️50 | split | loadRemoteControlPage/loadTelemetryPage reference undefined component IDs |
| R4-EVT-01 | Critical | ❌85 | ❌76 | ✅95 | ❌80 | ❌90 | ❌85 | **CONFLICT** | Missing braces on if/else — syntax error in alignRightButton |
| R4-EVT-02 | Medium | ✅90 | ⚠️58 | ✅95 | ✅80 | ✅95 | ✅90 | split | Velocity modifier ComboBox lists 2 options but switch handles 4 — dead code |
| R4-EVT-03 | High | ⚠️60 | ✅84 | ✅85 | ✅80 | ✅85 | ✅68 | split | CursorAutoHide null access on root.pageStack.currentItem during page transitions |
| R4-CMT-01 | Critical | ✅90 | ✅84 | ✅98 | ✅85 | ✅90 | ✅90 | AGREE | PDF import completely broken — converter invocation commented out |
| R4-PRJ-01 | High | ❌80 | ❌76 | ❌85 | ⚠️60 | ❌90 | ❌80 | split | flip variable spuriously reset in project() inner loop else-branch |
| R4-PRJ-02 | High | ❔45 | ❔39 | ✅95 | ✅80 | ✅95 | ❔45 | split | displayModel.get().flipSetting writes to snapshot copy — never mutates model |
| R4-PRJ-03 | Medium | ✅55 | ✅92 | ✅90 | ✅80 | ✅95 | ✅55 | AGREE | setScreensModel() duplicates display entries on each toggle cycle |
| R4-PRJ-04 | Medium | ✅55 | ✅78 | ✅85 | ✅80 | ✅90 | ✅55 | AGREE | Division by zero in projection image height |
| R4-ROV-01 | High | ⚠️60 | ⚠️58 | ✅90 | ✅80 | ✅95 | ✅68 | split | Division by zero in __customPlacement when overlay full |
| R4-ROV-02 | High | ⚠️65 | ⚠️58 | ✅90 | ✅80 | ✅90 | ✅68 | split | Drag permanently breaks y property binding on readRegion |
| R4-ROV-03 | Medium | ✅90 | ✅78 | ✅95 | ⚠️65 | ✅95 | ✅90 | split | Bitwise OR \| used for width fallback instead of logical OR |
| R4-BKG-01 | Medium | ✅85 | ✅78 | ✅85 | ⚠️60 | ✅90 | ✅85 | split | Flip transform origin stays at (0,0) when Flip stored as property |
| R4-SHD-01 | Medium | ❌80 | ❌76 | ✅90 | ⚠️65 | ✅80 | ❌80 | **CONFLICT** | Duplicate class implementation between .cpp and .mm — ODR risk |
| R4-IOSCPP-01 | Low | ⚠️50 | ⚠️58 | ✅90 | ⚠️60 | ✅85 | ✅68 | split | QTemporaryDir created on all platforms including non-iOS where unused |
| R4-SIG-ADD-01 | Low | ⚠️45 | ⚠️58 | ⚠️60 | ✅75 | ✅70 | ✅68 | split | SessionModel::appendDataPoint declared public slot but never connected |
| FINAL-01 | Critical | ✅90 | ✅92 | ✅98 | ✅85 | ✅95 | ✅90 | AGREE | TimerClock references undefined `timer` id — ETA and stopwatch completely broken |
| FINAL-02 | Critical | ❌85 | ❌90 | ❌90 | ✅85 | ✅95 | ❌85 | **CONFLICT** | Missing `QtQuick.Controls.Material` import — 3 Material references unresolved |
| FINAL-03 | Critical | ✅95 | ✅84 | ✅98 | ✅80 | ✅90 | ✅95 | AGREE | Missing breeze-icons submodule — fresh clone cannot build |
| FINAL-04 | High | ⚠️50 | ⚠️58 | ⚠️60 | ✅80 | ✅95 | ✅68 | split | NSIS start-menu shortcut icon name mismatches actual binary name |
| FINAL-05 | High | ✅90 | ✅84 | ✅95 | ✅85 | ✅85 | ✅90 | AGREE | WindowDragger mouse delta accumulation error — window moves farther than cursor |
| FINAL-06 | High | ✅90 | ⚠️58 | ❌95 | ✅85 | ✅95 | ✅90 | **CONFLICT** | CMAKE_OSX_ARCHITECTURES contains literal quotes — universal binary broken |
| FINAL-07 | High | ❌80 | ❌76 | ❌98 | ⚠️60 | ✅95 | ❌80 | **CONFLICT** | CMake wrong variable name: InstallRequiredSystemLibraries instead of CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS |
| FINAL-08 | High | ✅85 | ✅84 | ✅95 | ✅80 | ✅90 | ✅85 | AGREE | setup.sh vcvarsall.bat executed from bash — MSVC env not propagated |
| FINAL-09 | Medium | ✅85 | ✅92 | ✅90 | ❌80 | ✅95 | ✅85 | **CONFLICT** | `on__IChanged` handler typo — never fires |
| FINAL-10 | High | ⚠️55 | ⚠️58 | ✅90 | ✅80 | ✅90 | ⚠️50 | split | Two animations target same `position` property — conflict |
| FINAL-11 | High | ✅85 | ✅84 | ✅95 | ✅85 | ✅95 | ✅85 | AGREE | onFrameSwapped calls grabToImage every frame — severe performance hit |
| FINAL-12 | Medium | ✅80 | ✅78 | ✅95 | ✅80 | ✅90 | ✅80 | AGREE | SystemFontChooserDialog setWindowFlags strips all decorations |
| FINAL-13 | Medium | ✅90 | ✅92 | ✅95 | ✅90 | ✅95 | ✅90 | AGREE | Invalid Korean locale code "ko_KO" — should be "ko_KR" |
| FINAL-14 | Medium | ⚠️55 | ⚠️58 | ✅98 | ✅85 | ✅95 | ⚠️50 | split | Wrong placeholder `%0` instead of `%1` — font name never displayed |
| FINAL-15 | High | ⚠️55 | ⚠️58 | ✅90 | ✅85 | ✅85 | ⚠️50 | split | Missing edit block wrapping in setLineHeight/setParagraphHeight |
| FINAL-16 | Critical | ❔50 | ⚠️58 | ✅80 | ✅85 | ✅95 | ❔50 | split | Countdown completion uses state++ bypassing toggle() entry actions |
| FINAL-17 | Medium | ✅85 | ✅78 | ✅90 | ✅85 | ✅90 | ✅85 | AGREE | ScriptAction references non-existent function `paintReady` |
| FINAL-18 | Medium | ✅100 | ✅78 | ✅95 | ✅85 | ✅95 | ✅100 | AGREE | MarkersModel extendLastMarker modifies data without emitting dataChanged |
| FINAL-19 | Medium | ✅70 | ✅78 | ✅85 | ⚠️65 | ✅85 | ✅70 | split | Encoding fallback uses toLocal8Bit() instead of dictionary's actual encoding |
| FINAL-20 | High | ❌80 | ❌76 | ❌90 | ✅85 | ✅90 | ❌80 | **CONFLICT** | Dangling pointer from temporary QByteArray in marker anchor parsing |
| FINAL-21 | Medium | ✅75 | ✅78 | ✅70 | ✅80 | ✅85 | ✅75 | AGREE | clearProperty(AnchorHref/AnchorName) ineffective through mergeCharFormat |
| FINAL-22 | High | ⚠️50 | ⚠️58 | ✅85 | ✅80 | ✅85 | ⚠️50 | split | Behavior.onRunningChanged calls toggle() from within animation handler — re-entrant state change |
| CUR-N01 | Critical | ✅90 | ✅84 | ✅95 | ✅85 | ✅95 | ✅90 | AGREE | replaceAll() infinite loop when replacement contains search pattern |
| CUR-N02 | High | ✅95 | ✅84 | ✅98 | ✅85 | ✅95 | ✅95 | AGREE | search() regex path ignores loop parameter — unconditional wrap |
| CUR-N03 | Medium | ✅70 | ✅78 | ✅80 | ✅80 | ✅75 | ✅70 | AGREE | alignment() reads blockFormat on multi-block selection — returns wrong alignment |
| DCL-N01 | Medium | ✅55 | ✅78 | ✅95 | ✅80 | ✅95 | ✅55 | AGREE | filterHtml default parameter in .cpp but not in header — QML can't call with 1 arg |
| DCL-N02 | Medium | ✅55 | ✅78 | ✅95 | ✅80 | ✅95 | ✅55 | AGREE | setKeyMarker default parameter mismatch — same pattern |
| IMP-N01 | Critical | ❌60 | ❌76 | ⚠️75 | ⚠️65 | ❌80 | ❌60 | split | import Qt.labs.platform 1.1 — Menu/MenuBar/MenuItem dropped in Qt 6 |
| IMP-N02 | Critical | ❌65 | ❌76 | ✅80 | ⚠️60 | ✅95 | ❌65 | **CONFLICT** | import QtWebSockets 1.10 — wrong version for Qt 6.5 |
| MATH-N01 | High | ✅65 | ✅84 | ✅95 | ✅85 | ✅90 | ✅65 | AGREE | Division by zero in __timeToArival/__timeToEnd when speed=0 |
| MATH-N02 | Medium | ✅60 | ✅78 | ✅90 | ✅80 | ✅90 | ✅60 | AGREE | Bitwise << on floating-point in TimerClock — precision loss |
| LYR-N01 | High | ⚠️60 | ✅84 | ✅85 | ✅85 | ✅90 | ✅68 | split | InputsOverlay calls cursorAutoHide.restart() on open instead of reset() |
| LYR-N02 | Medium | ⚠️50 | ✅78 | ✅75 | ⚠️65 | ✅90 | ✅68 | split | Three OverlaySheets missing from ESC dismiss chain |
| LYR-N03 | Medium | ❔45 | ✅78 | ✅88 | ⚠️60 | ❌80 | ❔45 | **CONFLICT** | ContextDrawer exposes prompter actions while viewing layer pages |
| LYR-N04 | Medium | ⚠️50 | ✅78 | ✅85 | ✅80 | ✅90 | ✅68 | split | ESC handler uses activeFocus in base but focus in platform variants — inconsistent |
| TRL-N01 | High | ⚠️55 | ✅84 | ✅95 | ✅85 | ✅95 | ⚠️50 | split | qsTr() uses %0 placeholder — should be %1 (font name never displayed) |
| TRL-N02 | Medium | ✅50 | ✅78 | ✅90 | ✅80 | ✅90 | ✅50 | AGREE | Application --help description not translatable |
| TRL-N03 | Medium | ⚠️45 | ✅78 | ✅90 | ✅80 | ✅85 | ✅68 | split | About-dialog credit roles not translatable |
| W10-HTK-01 | Critical | ❌70 | ❌76 | ✅92 | ✅80 | ✅95 | ❌70 | **CONFLICT** | autoRepeat=true for ALL QHotkey shortcuts — non-velocity actions broken when held |
| W10-HTK-02 | High | ✅65 | ✅88 | ✅88 | ✅80 | ✅95 | ✅65 | AGREE | QHotkey::setShortcut return value silently ignored — no failure detection |
| W10-PMV-01 | High | ⚠️50 | ⚠️58 | ⚠️70 | ⚠️60 | ✅80 | ✅68 | split | font.pixelSize evaluates to 0 before first layout pass — crash hazard |
| W10-PMV-02 | Medium | ⚠️50 | ⚠️58 | ✅80 | ⚠️65 | ✅85 | ✅68 | split | Circular ShaderEffectSource dependency — shadow ghost on first frame |
| W10-CLP-01 | High | ⚠️55 | ⚠️58 | ❌80 | ✅80 | ✅85 | ✅68 | **CONFLICT** | Paste-without-formatting fails when clipboard lacks text/plain |
| W10-CLP-02 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅80 | ✅85 | ✅68 | split | Remote image URLs in pasted HTML cause unsanctioned network requests |
| W10-CNV2-01 | High | ✅80 | ✅92 | ✅90 | ✅85 | ✅95 | ✅80 | AGREE | Default stylesheet has invalid CSS color quoting — exported HTML broken in browsers |
| W10-CNV2-02 | High | ✅55 | ✅84 | ✅92 | ✅80 | ✅90 | ✅55 | AGREE | No markdown export — round-trip silently destroys all formatting |
| W10-CNV2-03 | High | ⚠️45 | ⚠️58 | ⚠️65 | ✅85 | ✅85 | ✅68 | split | import() uses fromStdString on non-Windows — encoding corruption |
| W10-SWT-01 | High | ⚠️55 | ⚠️58 | ✅90 | ✅80 | ✅90 | ✅68 | split | CloseActions switch drops RecentLocal/RecentRemote — recent document open silently lost after save |
| W10-SWT-02 | High | ⚠️55 | ⚠️58 | ✅90 | ✅80 | ✅90 | ✅68 | split | Same bug in IosSaveDialog.onAccepted path |
| W10-DEP-01 | Critical | ✅75 | ✅92 | ✅92 | ⚠️65 | ✅95 | ✅75 | split | Missing vcpkg.json manifest — vcpkg manifest mode installs nothing |
| W10-WSM-01 | Critical | ⚠️55 | ⚠️58 | ✅88 | ✅80 | ✅85 | ✅68 | split | Infinite reload loop on unauthorized WASM host — app unusable |
| W10-WSM-02 | Medium | ⚠️50 | ⚠️58 | ✅88 | ✅80 | ✅85 | ✅68 | split | Global file-picker state overwritten by re-entrant calls — wrong file delivered |
| W10-PLF-01 | Critical | ✅70 | ✅84 | ✅95 | ✅80 | ✅85 | ✅70 | AGREE | BSD detection broken — FreeBSD enters wrong code paths |
| W10-PLF-02 | High | ⚠️50 | ⚠️58 | ✅95 | ✅80 | ✅85 | ✅68 | split | QHotkey_FOUND never set in FetchContent path — built but never linked |
| TS-01 |  | ❔40 | ⚠️58 | ✅88 | ✅85 | ✅95 | ❔40 | split | Finnish welcome guide → Dutch (not Finnish) |
| TS-02 |  | ⚠️50 | ⚠️58 | ✅90 | ✅85 | ✅95 | ✅68 | split | Arabic file `ar_EG` vs UI `ar_AE` mismatch |
| TS-03 |  | ✅90 | ✅78 | ✅90 | ✅90 | ✅95 | ✅90 | AGREE | Korean UI `ko_KO` vs file `ko_KR` mismatch |
| TS-04 |  | ❔40 | ❔39 | ✅85 | ❔50 | ✅90 | ❔40 | split | French "Saved" → verb "Enregistrer" (should be adjective "Enregistré") |
| TS-05 |  | ⚠️45 | ⚠️58 | ✅85 | ✅80 | ✅85 | ✅68 | split | Finnish/French/Korean/Italian "Saved" → verb with stray `&amp;` accelerator |
| TS-06 |  | ❔40 | ❔39 | ✅90 | ❔50 | ✅90 | ❔40 | split | Czech/French "Language settings" → "Pointer settings" (copy-paste error) |
| TS-07 |  | ❔40 | ❔39 | ✅85 | ❔50 | ✅90 | ❔40 | split | Finnish/French/Korean "Colors for prompter states" → "Toggle Prompter State" |
| TS-08 |  | ❔40 | ❔39 | ✅85 | ❔50 | ✅90 | ❔40 | split | French "Prompting:" → "Start prompter" |
| TS-09 |  | ❔40 | ❔39 | ✅85 | ❔50 | ✅90 | ❔40 | split | Finnish/French/Korean/Dutch "Vertical offset" → "Velocity" |
| TS-10 |  | ❔40 | ❔39 | ✅85 | ❔50 | ✅90 | ❔40 | split | Finnish/Korean "Next reload starts at" → "Step acceleration" |
| TS-11 |  | ❔40 | ❔39 | ✅90 | ❔50 | ✅90 | ❔40 | split | French/Finnish/Korean "No pointers" → "Both pointers" (opposite meaning) |
| TS-12 |  | ❔40 | ❔39 | ✅90 | ❔50 | ✅90 | ❔40 | split | French "Alt" key → "Tout" (means "All") |
| TS-13 |  | ❔40 | ❔39 | ✅90 | ❔50 | ✅90 | ❔40 | split | French "Set velocity to 0–10" (all 11) → identical "Vitesse de départ" |
| TS-14 |  | ❔40 | ❔39 | ✅85 | ❔50 | ✅90 | ❔40 | split | French "Clear color" → "Light color" |
| TS-15 |  | ❔40 | ❔39 | ✅85 | ❔50 | ✅90 | ❔40 | split | Finnish/Korean right pointer reuse → left pointer (swapped) |
| TS-16 |  | ⚠️45 | ⚠️58 | ✅90 | ✅80 | ✅90 | ✅68 | split | Paragraph spacing: 8 languages strip trailing `%` from `<pre>%1%</pre>` |
| TS-17 |  | ⚠️45 | ⚠️58 | ✅90 | ✅80 | ✅90 | ✅68 | split | Line width: 7 languages add spurious `%` to `<pre>%1</pre>` |
| TS-18 |  | ❔40 | ❔39 | ✅85 | ✅85 | ✅90 | ❔40 | split | Orphan files: Hebrew and Polish exist but UI entries commented out |
| HTK-01 | Critical | ❔45 | ❔39 | ✅95 | ⚠️65 | ✅95 | ❔45 | split | KGlobalAccel default permanently destroyed on first user customization |
| HTK-02 | High | ❔45 | ❔39 | ✅92 | ✅80 | ✅90 | ❔45 | split | User shortcuts never persisted when only Use_GlobalAccel defined (no QHotkey) |
| HTK-03 | High | ⚠️50 | ⚠️58 | ✅90 | ✅80 | ✅90 | ✅68 | split | KGlobalAccel defaults silently zeroed on non-Wayland when QHotkey co-exists |
| HTK-04 | Medium | ✅60 | ✅92 | ✅85 | ✅80 | ✅85 | ✅60 | AGREE | Wrong enum type `Qt::KeyboardModifier` (singular) for modifier variable |
| HTK-05 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅85 | ⚠️50 | split | VelocityTo0 default shortcut uses `Qt::Key_acute` — unreachable dead key |
| HTK-06 | Medium | ⚠️45 | ⚠️58 | ✅90 | ✅80 | ✅85 | ⚠️50 | split | Pause (Ctrl+Space) and Stop (Meta+Space) conflict — Meta+Space captured by OS |
| HTK-07 | Low | ⚠️45 | ⚠️58 | ✅88 | ✅75 | ✅80 | ⚠️50 | split | Double `removeAllShortcuts()` IPC round-trip in customization path |
| HTK-08 | Low | ⚠️50 | ⚠️58 | ✅85 | ✅75 | ✅85 | ⚠️50 | split | key/modifiers parameters silently discarded mid-function on non-Wayland |
| TMR-01 | High | ❔50 | ❔39 | ✅92 | ✅85 | ✅95 | ❔50 | split | Countdown→Prompting auto-transition via state++ bypasses toggle() entirely |
| TMR-02 | Medium | ❔45 | ❔39 | ✅80 | ✅80 | ✅85 | ❔45 | split | timer.updateTimer() runs before timer.startTimer() on Prompting entry |
| TMR-03 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅75 | ✅85 | ✅68 | split | dissolveIn animation re-triggered entering Running from Ready — flicker |
| TMR-04 | Low | ❔45 | ❔39 | ✅80 | ⚠️60 | ✅80 | ❔45 | split | Countdown arc hypotenuse uses geometric center instead of arc center |
| TMR-05 | Low | ✅85 | ✅78 | ✅88 | ✅85 | ✅90 | ✅85 | AGREE | ScriptAction `paintReady` references non-existent function |
| TMR-06 | Low | ❔45 | ❔39 | ✅85 | ⚠️60 | ✅80 | ❔45 | split | dissolveOut starts too early when disappearWithin > 1 |
| TMR-07 | Low | ✅55 | ⚠️58 | ⚠️65 | ⚠️55 | ✅75 | ✅55 | split | countdownAnimation restart uses non-idempotent running=true |
| TMR-08 | Low | ❔45 | ❔39 | ✅80 | ⚠️55 | ✅80 | ❔45 | split | timer.running not explicitly set in Countdown state — relies on revert behavior |
| SPL2-11 | Medium | ✅60 | ✅78 | ✅90 | ✅80 | ✅85 | ✅60 | AGREE | addCustomWord trims but removeCustomWord does not — asymmetry |
| SPL2-12 | Medium | ✅55 | ✅92 | ✅88 | ✅80 | ✅85 | ✅55 | AGREE | Case-sensitive contains/indexOf but case-insensitive sort — duplicates |
| SPL2-13 | Medium | ✅55 | ✅78 | ✅90 | ✅80 | ✅85 | ✅55 | AGREE | saveCustomWordsToDisk has void return — callers cannot detect I/O failure |
| SPL2-14 | Medium | ✅65 | ✅92 | ✅85 | ✅75 | ✅85 | ✅65 | AGREE | Cached QRC dicts never invalidated after app update |
| SPL2-15 | Medium | ✅60 | ✅78 | ✅90 | ✅85 | ✅85 | ✅60 | AGREE | spell() returns true when no dicts loaded — silent no-op |
| SPL2-16 | Low | ✅55 | ✅88 | ✅80 | ✅75 | ✅75 | ✅55 | AGREE | QDir::mkpath return unchecked — dict cache directory may silently not exist |
| SPL2-17 | Low | ✅55 | ✅88 | ✅80 | ✅75 | ✅75 | ✅55 | AGREE | QFile::setPermissions return unchecked — cached dict may be unreadable |
| SPL2-18 | Low | ✅55 | ✅88 | ✅85 | ⚠️65 | ✅75 | ✅55 | split | Hunspell::add return value unchecked at 4 call sites |
| SPL2-19 | Low | ✅55 | ✅78 | ✅85 | ✅80 | ✅80 | ✅55 | AGREE | availableDictionaries enumerates .dic without verifying .aff exists |
| SPL2-20 | Low | ⚠️45 | ⚠️58 | ❌85 | ✅75 | ✅70 | ✅68 | **CONFLICT** | loadCustomWordsFromDisk redundant exists() before open() |
| WSM-03 | High | ⚠️50 | ⚠️58 | ✅88 | ⚠️65 | ✅80 | ✅68 | split | readAsDataURL causes quadruple in-memory copy of file content |
| BLD-05 | Medium | ✅55 | ✅78 | ✅95 | ✅85 | ✅95 | ✅55 | AGREE | .env.android references Qt 5.15.2 — project requires Qt 6.8.2+ |
| EVT-01 | High | ⚠️50 | ⚠️58 | ⚠️60 | ✅80 | ✅85 | ✅68 | split | velocityDragArea (z:5) blocks viewport.mouse (z:0) wheel events |
| EVT-02 | High | ❌55 | ⚠️58 | ✅88 | ✅80 | ✅85 | ❌55 | **CONFLICT** | Zero inputMethodHints on any TextField — IME broken for CJK/Indic |
| EVT-03 | High | ⚠️50 | ⚠️58 | ✅90 | ✅80 | ✅85 | ✅68 | split | velocityDragOverlay (z:7) steals clicks from control buttons (z:6) |
| EVT-04 | High | ⚠️50 | ⚠️58 | ✅92 | ✅80 | ✅85 | ✅68 | split | Drag breaks editor.x declarative binding permanently |
| EVT-05 | High | ⚠️50 | ⚠️58 | ✅92 | ✅80 | ✅85 | ✅68 | split | Drag breaks positionHandler.x declarative binding permanently |
| EVT-06 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅80 | ✅85 | ✅68 | split | Drag breaks stopwatch.x binding permanently |
| EVT-07 | Medium | ✅60 | ✅78 | ✅90 | ✅80 | ✅85 | ✅60 | AGREE | TabBar currentIndex binding broken on first TabButton click |
| EVT-08 | Medium | ✅60 | ✅78 | ✅88 | ✅80 | ✅85 | ✅60 | AGREE | Two additional checkable ToolButton binding breakage instances |
| EVT-09 | Low | ⚠️45 | ⚠️52 | ✅78 | ⚠️60 | ✅70 | ✅68 | split | Flow ToolSeparator visibility compares y of potentially invisible rows |
| EVT-10 | Low | ⚠️50 | ⚠️58 | ✅85 | ⚠️60 | ✅85 | ✅68 | split | Nested MouseAreas with hoverEnabled steal hover from parent Buttons |
| ENC-01 | Medium | ✅60 | ✅78 | ✅88 | ✅80 | ✅95 | ✅60 | AGREE | truncate(-1) when font preview text has no spaces |
| ENC-02 | Low | ✅55 | ✅78 | ✅85 | ✅80 | ✅90 | ✅55 | AGREE | getMarkerKey() mid(4) without length/startsWith guard |
| ANM-N01 | Medium | ✅70 | ✅78 | ✅92 | ✅80 | ✅90 | ✅70 | AGREE | Easing.EaseOut is not a valid Qt Quick easing type (2 instances) |
| NET-01 | High | ✅65 | ✅84 | ✅92 | ✅85 | ✅95 | ✅65 | AGREE | loadFromNetworkFinihed never checks m_reply->error() |
| NET-02 | Medium | ⚠️50 | ⚠️58 | ⚠️70 | ✅80 | ✅90 | ❌72 | **CONFLICT** | RedirectPolicyAttribute set to boolean true → NoLessSafeRedirectPolicy |
| THR-01 | Medium | ⚠️45 | ⚠️58 | ✅82 | ⚠️65 | ✅85 | ⚠️50 | split | IosSaveDialog::create() — unsynchronized singleton race |
| THR-02 | Medium | ⚠️45 | ⚠️58 | ✅82 | ⚠️65 | ✅85 | ⚠️50 | split | ShakeDetector::create() — identical unsynchronized singleton race |
| THR-03 | Low | ⚠️50 | ⚠️58 | ✅80 | ✅80 | ✅85 | ⚠️50 | split | search() — mutable static QRegularExpression shared across all callers |
| THR-04 | Medium | ⚠️45 | ✅78 | ⚠️72 | ✅85 | ✅85 | ⚠️50 | split | SpellChecker zero thread safety — explicit finding |
| DRW-01 | Medium | ⚠️50 | ⚠️58 | ✅88 | ⚠️65 | ✅85 | ✅68 | split | interalFocusElsewhere() misses 3 OverlaySheets + 2 Drawers — hotkeys pass through |
| DRW-02 | Medium | ⚠️50 | ⚠️58 | ✅88 | ⚠️65 | ✅85 | ✅68 | split | globalDrawer and contextDrawer missing from ESC dismiss chain |
| AND-BLD-01 | Critical | ✅80 | ✅92 | ✅95 | ⚠️65 | ✅95 | ✅80 | split | Missing version.gradle — Gradle build fails |
| AND-RES-01 | Medium | ⚠️45 | ⚠️58 | ✅90 | ✅80 | ✅90 | ✅68 | split | Invalid android:scaleType on bitmap element |
| AND-MFT-01 | Medium (latent) | ⚠️45 | ⚠️58 | ✅85 | ⚠️65 | ✅75 | ✅68 | split | FileProvider resource @xml/qtprovider_paths — file named filepaths.xml |
| SHADOW-01 | Low | ✅60 | ✅78 | ✅85 | ⚠️60 | ❌80 | ✅60 | **CONFLICT** | id: rotation shadows Item.rotation property |
| SHADOW-02 | Low | ✅55 | ✅78 | ✅85 | ⚠️60 | ❌80 | ✅55 | **CONFLICT** | id: flow shadows Flow.flow property |
| FOC-N01 | Low | ✅65 | ✅78 | ✅88 | ✅80 | ✅95 | ✅65 | AGREE | focus: true is JS label in atEndLoopDelay SpinBox |
| FOC-N02 | Low | ✅65 | ✅78 | ✅88 | ✅80 | ✅95 | ✅65 | AGREE | Same JS label bug in countdownConfiguration SpinBoxes (2 instances) |
| FOC-N03 | Low | ⚠️50 | ✅78 | ✅85 | ⚠️60 | ✅85 | ✅68 | split | Tab/Backtab asymmetry — Backtab silently unhandled |
| VER-01 | Low | ⚠️45 | ✅78 | ✅85 | ⚠️60 | ❌90 | ❌72 | **CONFLICT** | Qt::MarkdownText version guard 0x050F00 (5.15) — API added in 5.14 |
| CPY-01 | Low | ⚠️40 | ⚠️58 | ✅80 | ✅75 | ❌80 | ⚠️50 | **CONFLICT** | 5 Q_INVOKABLE methods pass QString by value instead of const& |
| DSZ-01 | Medium | ✅60 | ⚠️58 | ✅88 | ✅80 | ✅80 | ✅60 | split | InputsOverlay hardcoded height:680 — overflows on phones |
| DSZ-02 | Medium | ⚠️45 | ✅78 | ✅88 | ✅75 | ✅85 | ✅68 | split | pointerConfiguration OverlaySheet no vertical ScrollView |
| DSZ-03 | Low | ⚠️40 | ⚠️58 | ✅85 | ⚠️60 | ❌70 | ✅68 | **CONFLICT** | Magic number 68 in ListView height binding |
| JSN-01 | High | ✅65 | ✅92 | ✅90 | ✅85 | ✅90 | ✅65 | AGREE | i.d.authentication accessed without undefined guard |
| JSN-02 | Medium | ⚠️50 | ✅78 | ✅90 | ✅80 | ✅85 | ✅68 | split | ws.sendTextMessage() called without checking WebSocket status |
| QCN-01 | Low | ✅55 | ✅78 | ✅90 | ✅75 | ✅80 | ✅55 | AGREE | O(n²) contains()-in-loop during custom words file load |
| PC-01 | Medium | ❔45 | ❔39 | ✅70 | ⚠️65 | ✅90 | ❔45 | split | countdown.state not set in Prompting state — countdown visible during teleprompting |
| QTD-01 | Medium | ✅65 | ✅78 | ✅85 | ✅80 | ✅85 | ✅65 | AGREE | m_spellHighlighter not detached when setDocument(nullptr) |
| QTD-02 | Low-Medium | ❔40 | ✅78 | ✅85 | ⚠️60 | ✅80 | ❔40 | split | QQuickTextDocument destroyed without destroyed signal connection |
| OPC-01 | Medium | ⚠️50 | ✅78 | ✅90 | ✅80 | ✅85 | ✅68 | split | Right-click toggle desynchronizes velocityIndicator visible/opacity |
| HDR-N01 | Low | ✅60 | ⚠️58 | ✅95 | ✅80 | ✅80 | ✅60 | split | promptsession.h not in CMakeLists.txt — SessionModel/DataPoint dead code |
| HDR-N02 | Low | ✅60 | ⚠️58 | ✅95 | ✅80 | ✅80 | ✅60 | split | telemetry.h not in CMakeLists.txt — Telemetry dead code |
| IO-N01 | Medium | ⚠️45 | ✅78 | ✅90 | ✅80 | ✅90 | ✅68 | split | saveAs() leaves _fileSystemWatcher permanently blocked on open failure |
| IO-N02 | High | ✅50 | ✅84 | ✅85 | ✅85 | ✅95 | ✅50 | AGREE | save() constructs QUrl without file:// scheme — broken on non-Windows |
| IO-N03 | Medium | ✅55 | ✅88 | ✅90 | ✅80 | ✅75 | ✅55 | AGREE | iossavedialog.mm QFile::write() return value unchecked |
| QML-BND-01 | High | ✅60 | ✅84 | ✅90 | ✅80 | ✅90 | ✅60 | AGREE | countdownAnimation.running binding permanently broken after first iteration |
| QML-BND-02 | Medium | ✅55 | ✅78 | ✅90 | ✅80 | ✅85 | ✅55 | AGREE | clock.__iteration binding broken by post-decrement in animation handler |
| QML-BND-03 | None (info) | ⚠️40 | ⚠️58 | ✅95 | ❌85 | ❌70 | ❌72 | **CONFLICT** | ReadRegionOverlay onDestruction — harmless dead code |
| WSM-N01 | High | ✅60 | ✅84 | ✅85 | ✅80 | ✅80 | ✅60 | AGREE | Synchronous QImage::load() from HTTP blocks WASM main thread |
| WSM-N02 | Low | ✅60 | ✅78 | ✅90 | ✅80 | ✅85 | ✅60 | AGREE | WASM preventSleep() falls through to desktop #else — always returns false |
| QRC-N01 | Low | ❔45 | ✅92 | ✅95 | ✅80 | ✅95 | ❔45 | split | icons.qrc contains duplicate \<file\> entry |
| QRC-N02 | Low | ⚠️45 | ⚠️58 | ✅90 | ✅80 | ✅85 | ✅68 | split | Four .qrc files are dead code — never referenced by CMakeLists.txt |
| CMAKE-N01 | Low | ⚠️45 | ⚠️58 | ❔60 | ✅80 | ✅70 | ❌72 | **CONFLICT** | WASM build excludes TelemetryPage.qml and RemotePage.qml |
| OOB-N01 | Medium | ⚠️50 | ✅78 | ✅90 | ✅80 | ✅90 | ✅68 | split | MarkersModel::data() — m_data.at() without row < rowCount() guard |
| OOB-N02 | Medium | ⚠️45 | ✅78 | ✅90 | ✅80 | ✅85 | ✅68 | split | SessionModel::data() — same missing row bounds guard |
| OOB-N03 | Low | ⚠️50 | ✅78 | ✅85 | ⚠️60 | ❌80 | ⚠️50 | **CONFLICT** | alignment() fetches textCursor() twice — stale cursor race |
| I18N-N01 | Low | ⚠️40 | ⚠️58 | ✅80 | ✅75 | ✅70 | ⚠️50 | split | Stale source-location line numbers in all 20 .ts files |
| I18N-N02 | Low | ⚠️40 | ⚠️58 | ✅80 | ✅75 | ✅70 | ⚠️50 | split | Vanished translation entries not purged across 13 language files |
| STR-N01 | High | ✅70 | ✅84 | ✅90 | ✅85 | ✅95 | ✅70 | AGREE | main.cpp:158 QLatin1String iterator-pair UB from two unrelated string literals |
| NOTIFY-01 | Medium | ✅75 | ✅78 | ✅95 | ✅80 | ✅95 | ✅75 | AGREE | setAutoReload doesn't emit autoReloadChanged NOTIFY signal |
| NOTIFY-02 | Low | ✅55 | ✅78 | ⚠️85 | ✅80 | ✅85 | ✅55 | split | availableDictionariesChanged NOTIFY signal never emitted |
| MIX-01 | Low | ⚠️40 | ✅78 | ✅90 | ✅75 | ✅70 | ⚠️50 | split | spellchecker.cpp:98 size_t→int narrowing in languages() reserve |
| ENUM-01 | Medium | ⚠️45 | ✅78 | ✅90 | ✅80 | ✅85 | ✅68 | split | documenthandler.cpp:1108 updateContents switch no default — silent data loss |
| DPI-01 | Medium | ⚠️40 | ⚠️58 | ✅80 | ⚠️65 | ✅85 | ✅68 | split | TimerClock.qml:127 devicePixelRatio in raw arithmetic with magic multiplier |
| DPI-02 | Low | ⚠️45 | ⚠️58 | ✅85 | ✅75 | ❌75 | ✅68 | **CONFLICT** | MarkersDrawer.qml:37 drawer minimumWidth hardcoded to 260px |
| DPI-03 | Low | ⚠️45 | ⚠️58 | ✅90 | ✅75 | ❌75 | ✅68 | **CONFLICT** | Find.qml:38 searchBarWidth:724 hardcoded in px |
| DPI-04 | Medium | ✅60 | ⚠️58 | ✅90 | ✅80 | ✅80 | ✅60 | split | InputsOverlay.qml:33 height:680 hardcoded |
| GEO-01 | Low | ⚠️45 | ⚠️58 | ✅80 | ✅75 | ❌80 | ✅68 | **CONFLICT** | main.qml initial 728px height too large for 1366x768 laptops |
| GEO-02 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅80 | ✅85 | ✅68 | split | main.qml persists x/y/width/height with zero validation |
| GEO-03 | Low | ⚠️40 | ⚠️58 | ✅90 | ✅75 | ✅70 | ✅68 | split | +android/main.qml no minimumWidth/minimumHeight |
| UNIT-01 | High | ⚠️55 | ✅84 | ✅95 | ✅80 | ✅95 | ✅68 | split | ProgressIndicator.qml:46 Units.ShortDuration with no Kirigami import |
| UNIT-02 | High | ⚠️55 | ✅84 | ✅95 | ✅80 | ✅95 | ✅68 | split | PrompterView.qml 7x Units.ShortDuration with no Kirigami import |
| UNIT-03 | Medium | ⚠️50 | ✅78 | ✅95 | ✅75 | ✅90 | ✅68 | split | PrompterBackground.qml:160 Units.LongDuration no Kirigami import |
| UNIT-04 | Medium | ⚠️50 | ✅78 | ✅95 | ✅75 | ✅90 | ✅68 | split | Flip.qml:34,41 two Units.LongDuration no Kirigami import |
| UNIT-05 | Low | ⚠️50 | ✅78 | ✅95 | ✅75 | ✅90 | ✅68 | split | pointer_0.qml:72 Units.VeryLongDuration no Kirigami import |
| UNIT-06 | Medium | ⚠️50 | ✅78 | ✅95 | ⚠️65 | ✅90 | ✅68 | split | Find.qml:92 Units.ShortDuration with namespaced Kirigami import |
| UNIT-07 | Medium | ⚠️50 | ✅78 | ✅90 | ⚠️65 | ✅90 | ✅68 | split | ReadRegionOverlay.qml 3x Units.ShortDuration with namespaced import |
| AR-01 | Low | ⚠️45 | ✅78 | ✅75 | ⚠️60 | ✅75 | ⚠️50 | split | PrompterView.qml:53-58 Rotation debug feature clips on extreme aspect ratios |
| SAFE-01 | Medium | ⚠️45 | ⚠️58 | ✅80 | ✅80 | ✅75 | ✅68 | split | +android/main.qml zero safe area insets |
| SAFE-02 | Medium | ⚠️45 | ⚠️58 | ✅80 | ✅75 | ✅75 | ✅68 | split | ReadRegionOverlay screenMiddle ignores notch/status bar height |
| SET-01 | High | ⚠️45 | ✅84 | ✅90 | ⚠️65 | ✅90 | ⚠️50 | split | macOS/iOS: QSettings split across two preference domains |
| SET-02 | High | ❔45 | ✅84 | ✅90 | ✅80 | ✅90 | ❔45 | split | factoryReset() incomplete on macOS/iOS — domain-path settings survive |
| SET-03 | Low | ⚠️50 | ✅78 | ✅85 | ✅75 | ❌75 | ❌72 | **CONFLICT** | QString "true" used as default for boolean QSettings value |
| SET-04 | Low | ⚠️45 | ✅78 | ✅85 | ✅75 | ❌75 | ⚠️50 | **CONFLICT** | spellCheckLanguages read without explicit default value |
| INV-N01 | Medium | ⚠️50 | ✅78 | ✅85 | ✅80 | ✅85 | ✅68 | split | QmlUtil::r() stores QML-owned QQuickItemGrabResult raw pointer — use-after-free |
| CMAKE-NEW-01 | Low | ⚠️45 | ✅78 | ✅90 | ✅75 | ✅80 | ✅68 | split | Remote.qml exists on disk but never listed in QML_FILES |
| CMAKE-NEW-02 | Medium | ✅55 | ✅92 | ✅90 | ✅80 | ✅90 | ✅55 | AGREE | Duplicate install() of appdata.xml/desktop in root and src/CMakeLists.txt |
| CMAKE-NEW-03 | Medium | ✅55 | ✅78 | ✅90 | ✅80 | ✅85 | ✅55 | AGREE | find_package(KF6Crash ... COMPONENTS) — COMPONENTS keyword with zero names |
| CMAKE-NEW-04 | Medium | ✅60 | ✅78 | ✅90 | ✅80 | ✅85 | ✅60 | AGREE | execute_process uses CMAKE_PREFIX_PATH (list) as scalar — broken command |
| DLG-N01 | High | ✅60 | ✅84 | ✅90 | ✅85 | ✅95 | ✅60 | AGREE | document.modified=false set BEFORE saveAs() — failed save loses unsaved flag |
| DLG-N02 | High | ✅65 | ✅84 | ✅95 | ✅85 | ✅95 | ✅65 | AGREE | onError handler clears document.modified on save failure |
| DLG-N03 | Low | ⚠️45 | ✅78 | ✅90 | ✅75 | ✅80 | ✅68 | split | errorDialog MessageDialog has no title |
| DLG-N04 | Medium | ✅60 | ✅78 | ✅90 | ✅80 | ✅90 | ✅60 | AGREE | load() silently fails with no notification when file missing or unreadable |
| DLG-N05 | Medium | ✅55 | ✅78 | ✅90 | ✅80 | ✅85 | ✅55 | AGREE | loadFromNetworkFinihed() silently ignores empty response |
| DLG-N06 | High | ✅65 | ✅84 | ✅90 | ✅80 | ✅90 | ✅65 | AGREE | import() error strings passed as document content via updateContents() |
| DLG-N07 | Low | ⚠️45 | ✅78 | ✅85 | ✅75 | ✅85 | ✅68 | split | 5 showPassiveNotification() calls ignore passiveNotifications preference |
| DLG-N08 | Low | ⚠️45 | ✅78 | ✅85 | ✅75 | ✅80 | ✅68 | split | 3 save-completion passive notifications lack passiveNotifications guard |
| IMP-NEW-01 | High | ❌65 | ❌76 | ✅90 | ❌80 | ✅95 | ❌65 | **CONFLICT** | #include \<qnativeinterface.h\> doesn't exist — breaks Android build |
| IMP-NEW-02 | Low | ⚠️45 | ⚠️58 | ⚠️80 | ⚠️60 | ❌80 | ⚠️50 | split | main.cpp:22 #include "qglobal.h" uses quotes + Qt5-era name |
| IMP-NEW-03 | Low | ⚠️40 | ⚠️58 | ✅95 | ✅75 | ❌70 | ⚠️50 | **CONFLICT** | main.cpp:38-39 redundant #include \<QtQml/qqml.h\> + #include \<QtQml\> |
| IMP-NEW-04 | Low | ⚠️40 | ⚠️58 | ✅90 | ⚠️60 | ❌75 | ❌72 | **CONFLICT** | AboutPage.qml imports Kirigami 2.9 vs 2.11 in all other files |
| IMP-NEW-05 | Low (orphaned QRC, never compiled) | ❔45 | ⚠️58 | ⚠️80 | ⚠️55 | ✅70 | ❔45 | split | pointers.qrc RESOURCE_PREFIX conflicts with qt_add_qml_module |
| MA-N01 | Low | ⚠️50 | ✅78 | ✅95 | ✅75 | ✅70 | ✅68 | split | overlayMouseArea permanently disabled — dead MouseArea |
| MA-N02 | Low | ✅55 | ✅78 | ✅85 | ✅75 | ✅85 | ✅55 | AGREE | textDragArea missing cursorShape — ArrowCursor over IBeamCursor on editor |
| CMT-N01 | Medium | ⚠️40 | ⚠️48 | ✅90 | ✅80 | ✅80 | ⚠️50 | split | Justify ToolButton comment says it's commented out — but it's active |
| CMT-N02 | Low | ⚠️35 | ⚠️48 | ✅90 | ✅75 | ❌70 | ⚠️50 | **CONFLICT** | Truncated comment in markersmodel.cpp:107-108 |
| CMT-N03 | Medium | ⚠️35 | ⚠️48 | ✅85 | ⚠️60 | ❌70 | ⚠️50 | **CONFLICT** | Misleading OpenGL workaround comment — scope of impact understated |
| CMT-N04 | Medium | ❌55 | ❌76 | ✅85 | ⚠️60 | ❌75 | ❌55 | **CONFLICT** | Comment masks invalid enum bug — 2 - value produces out-of-range LayoutDirection |
| CMT-N05 | High | ⚠️40 | ⚠️48 | ✅85 | ⚠️60 | ❌75 | ❌72 | **CONFLICT** | Missing security warning on QProcess RCE sink (sys://) |
| CMT-N06 | Medium | ⚠️40 | ⚠️48 | ✅80 | ⚠️60 | ❌70 | ❌72 | **CONFLICT** | Missing warning: re-entrant toggle() inside Behavior.onRunningChanged |
| CMT-N07 | Medium | ⚠️40 | ⚠️48 | ✅85 | ⚠️60 | ❌70 | ❌72 | **CONFLICT** | Missing warning: joinPreviousEditBlock() without beginEditBlock() |
| CMT-N08 | Medium | ✅50 | ⚠️48 | ✅90 | ✅75 | ✅75 | ✅50 | split | Entire Telemetry class is dead commented-out shell across 4 files |
| CMT-N09 | Medium | ⚠️40 | ⚠️48 | ✅85 | ⚠️60 | ❌70 | ⚠️50 | **CONFLICT** | Commented-out PropertyActions in active loop animation — stale state risk |
| CMT-N10 | Low | ⚠️35 | ⚠️48 | ✅90 | ✅75 | ✅90 | ⚠️50 | split | Obsolete Qt 5 qmlRegisterType calls as commented-out cruft |
| REGEX-N01 | Medium | ⚠️45 | ✅78 | ✅85 | ✅75 | ✅95 | ⚠️50 | split | All 13 QRegularExpression objects lack isValid() checks |
| REGEX-N02 | Medium | ✅55 | ✅78 | ✅80 | ✅80 | ✅95 | ✅55 | AGREE | regex_5 accidentally excludes 15+ HTML5 tags from background-color filtering |
| REGEX-N03 | Low | ✅65 | ✅78 | ✅85 | ✅75 | ✅85 | ✅65 | AGREE | Unescaped dot in font-size regex — matches any char instead of decimal |
| HK-N01 | High | ⚠️50 | ⚠️58 | ✅90 | ✅80 | ✅95 | ✅68 | split | Missing event.isAutoRepeat guard on main Keys.onPressed |
| HK-N02 | Medium | ✅80 | ✅92 | ✅95 | ✅85 | ✅98 | ✅80 | AGREE | Typo Qt.Key_VolumeDowm — "Dowm" instead of "Down" — volume-down hardware key dead |
| HK-N03 | High | ⚠️50 | ⚠️58 | ✅90 | ⚠️65 | ✅90 | ✅68 | split | platformName() != "wayland" fails on "wayland-egl" — global hotkeys dead |
| HK-N04 | Medium | ⚠️45 | ⚠️58 | ✅85 | ✅80 | ✅90 | ✅68 | split | No auto-repeat guard in key-binding configuration Keys.onPressed |
| HK-N05 | Medium | ✅60 | ✅78 | ✅85 | ✅80 | ✅92 | ✅60 | AGREE | Strict === equality on modifiers breaks user keybinds with NumLock |
| HK-N06 | Low | ⚠️45 | ⚠️58 | ✅80 | ✅75 | ✅85 | ✅68 | split | isValidInput checks local keybindings only — silent conflict with global hotkeys |
| LDR-N01 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅80 | ✅90 | ✅68 | split | InputsOverlay typeof null guard fails — null.item crash on rapid close |
| PARSE-N01 | Medium | ⚠️50 | ✅78 | ✅85 | ✅80 | ✅95 | ✅68 | split | insertImageAt() stores image resource with file:// key but looks up via plain path |
| PARSE-N02 | Medium | ✅60 | ✅78 | ✅85 | ✅80 | ✅95 | ✅60 | AGREE | MarkersModel::keySearch() hits=1 limits search to first marker only |
| PROP-N01 | High | ✅70 | ✅84 | ✅95 | ✅85 | ✅90 | ✅70 | AGREE | on__FullScreenChanged handler casing mismatch — never fires |
| PROP-N02 | Medium | ⚠️55 | ⚠️58 | ✅85 | ✅80 | ✅95 | ⚠️50 | split | setCursorPosition → reset() — 12-signal storm, no debounce |
| PROP-N03 | Low | ⚠️45 | ⚠️58 | ✅85 | ⚠️60 | ✅90 | ⚠️50 | split | setMarker/setKeyMarker/setMarkerHref silently trigger full document reparse |
| NET-N04 | Medium | ✅60 | ✅78 | ✅90 | ✅75 | ✅90 | ✅60 | AGREE | No transfer timeout on any QNetworkRequest |
| NET-N05 | Medium | ✅60 | ✅78 | ✅85 | ✅80 | ✅95 | ✅60 | AGREE | loadFromNetwork() hardcodes http:// scheme — never upgrades to HTTPS |
| NET-N06 | Low | ✅65 | ⚠️58 | ✅85 | ✅80 | ✅95 | ✅65 | split | loadFromNetwork() validates original URL, not constructed resultingUrl |
| URL-N01 | Medium | ✅60 | ⚠️58 | ✅65 | ✅80 | ✅90 | ✅60 | split | reload() constructs file:// URL by string concatenation without encoding |
| DISK-N01 | Low | ✅55 | ✅78 | ✅55 | ✅75 | ✅90 | ✅55 | AGREE | saveCustomWordsToDisk() non-atomic write — data loss on power failure |
| INIT-N01 | Medium | ✅90 | ✅78 | ✅90 | ✅80 | ✅95 | ✅90 | AGREE | Velocity modifier ComboBox model has 2 entries, switch handles 4 cases |
| INIT-N02 | Low | ✅50 | ✅78 | ✅85 | ✅75 | ✅90 | ✅50 | AGREE | Find.qml SearchField placeholderText always empty — no guidance text |
| INIT-N03 | Low | ⚠️40 | ⚠️58 | ⚠️40 | ⚠️60 | ✅85 | ❌72 | **CONFLICT** | ReadRegionOverlay screenMiddle uses root.y from cross-file id resolution |
| INIT-N04 | Low | ⚠️40 | ⚠️58 | ❌80 | ⚠️60 | ✅75 | ❌72 | **CONFLICT** | PrompterView ShaderEffectSource.sourceItem references prompter id declared later |
| CMB-N01 | Medium | ❔45 | ❔39 | ✅70 | ⚠️65 | ✅95 | ❔45 | split | autoReloadSeconds SpinBox from binding circular — clamps to 1 when all-zero |
| CMB-N02 | Low | ❔45 | ❔39 | ✅75 | ⚠️60 | ✅90 | ❔45 | split | autoReloadMinutes SpinBox from contains redundant circular self-reference |
| CMB-N03 | Medium | ✅85 | ✅78 | ✅85 | ✅80 | ✅95 | ✅85 | AGREE | LanguageSettingsOverlay ListView currentIndex always -1 — wrong indexOf() call |
| VIS-N04 | Low | ⚠️45 | ⚠️58 | ⚠️45 | ⚠️60 | ✅85 | ✅68 | split | Countdown crosshair frame renders orphan lines when enabled=false |
| VIS-N05 | Medium | ⚠️50 | ⚠️58 | ✅65 | ✅75 | ✅92 | ✅68 | split | velocityDragOverlay blocks all interaction during indicator fade-out (~500ms dead zone) |
| SCRL-N01 | Medium | ❔45 | ❔39 | ⚠️50 | ⚠️60 | ✅80 | ⚠️50 | split | __jitterMargin: fractional result from modulus violates 0/1 toggle design |
| SCRL-N02 | Medium | ⚠️50 | ⚠️58 | ✅65 | ✅75 | ✅90 | ✅68 | split | __destination typed int truncates real-valued position |
| SCRL-N03 | Medium | ❔45 | ❔39 | ✅55 | ✅75 | ✅95 | ❔45 | split | setVelocity() triggers two conflicting scroll animations with intermediate velocity |
| SCRL-N04 | Low | ✅55 | ✅78 | ✅85 | ✅75 | ✅95 | ✅55 | AGREE | __speed non-zero when __i=0 and __curvature=0 (Math.pow(0,0)===1) |
| SCRL-N05 | Low | ⚠️50 | ⚠️58 | ❌65 | ⚠️60 | ✅80 | ⚠️50 | **CONFLICT** | __speedLimit check is dead logic — always true |
| SCRL-N06 | Low | ⚠️40 | ⚠️58 | ❌60 | ⚠️55 | ✅75 | ❌72 | **CONFLICT** | __timeToEnd uses unexplained 2× factor |
| TYP-N01 | Low | ✅85 | ✅92 | ✅90 | ✅75 | ✅98 | ✅85 | AGREE | Misspelled method name: loadFromNetworkFinihed (missing 's') |
| TYP-N02 | Low | ✅90 | ✅92 | ✅90 | ✅75 | ✅98 | ✅90 | AGREE | Misspelled parameter: withoutFormating (missing 't') |
| TYP-N03 | Low | ⚠️35 | ⚠️58 | ✅80 | ✅75 | ✅90 | ⚠️50 | split | Inconsistent `_` vs `m_` member prefix: _markersModel, _fileSystemWatcher |
| TYP-N04 | Low | ⚠️35 | ⚠️58 | ✅75 | ✅70 | ❌85 | ⚠️50 | **CONFLICT** | Inconsistent m_ method naming: m_initializeSource — mixed underscore+camelCase |
| TYP-N05 | Low | ✅90 | ✅88 | ✅70 | ✅80 | ✅90 | ✅90 | AGREE | Uninitialized member m_documentComesFromNetwork |
| TYP-N06 | Low | ⚠️50 | ⚠️58 | ✅65 | ⚠️65 | ✅85 | ⚠️50 | split | 9 getters copy-paste double-textCursor() pattern — null check on stale cursor |
| CAST-N01 | Medium | ✅60 | ✅78 | ✅70 | ✅80 | ✅90 | ✅60 | AGREE | setFontCapitalization static_cast with no range validation — reachable from QML |
| IMG-N01 | Medium | ❔45 | ❔39 | ❔30 | ✅80 | ✅95 | ❔45 | split | Missing go-previous-symbolic.svg — back-navigation icon blank on Android/Windows |
| ACT-N05 | Medium | ❔45 | ⚠️58 | ⚠️45 | ✅80 | ✅85 | ❔45 | split | +windows main.qml Controls Settings submenu missing OBS Settings action |
| ACT-N06 | Low | ⚠️45 | ⚠️58 | ⚠️45 | ✅75 | ✅80 | ✅68 | split | +windows main.qml Performance tweaks missing enableBarsSetting |
| ACT-N07 | Medium | ✅60 | ⚠️58 | ✅65 | ✅75 | ✅90 | ✅60 | split | namedBookmarkButton: checkable button opens dialog — stale indicator after first click |
| ACT-N08 | Medium (masked — Labs.MenuBar dead per IMP-N01) | ✅55 | ⚠️58 | ⚠️50 | ⚠️65 | ✅75 | ✅55 | split | All checkable Labs.MenuItems inherit R2-EDT-03 binding-break pattern |
| RENDER-01 | Medium | ⚠️50 | ✅78 | ✅70 | ✅75 | ✅80 | ✅68 | split | ShaderEffectSource prompterShadowSource runs unconditionally — wastes GPU capture when shadows disabled |
| RENDER-02 | Medium | ⚠️50 | ✅78 | ✅70 | ✅75 | ✅80 | ✅68 | split | ShaderEffectSource pointerShadowSource runs unconditionally — same pattern |
| TXT-N01 | Low | ⚠️40 | ⚠️58 | ⚠️40 | ✅75 | ✅95 | ⚠️50 | split | Find/replace fields missing persistentSelection: true |
| TXT-N02 | Low | ⚠️40 | ✅78 | ✅75 | ✅75 | ❌90 | ✅68 | **CONFLICT** | TimerClock default text color #AAA on #131619 — fails WCAG AA contrast |
| PLAT-N01 | Medium | ⚠️45 | ✅78 | ❌85 | ✅80 | ✅75 | ⚠️50 | **CONFLICT** | qmlutil.hpp incorrectly excludes QNX from QProcess — run()/restartApplication() silently no-op |
| PLAT-N02 | Medium | ❔40 | ✅78 | ❌85 | ✅80 | ✅70 | ❌72 | **CONFLICT** | documenthandler.cpp incorrectly excludes QNX from import() — LibreOffice broken on QNX |
| PLAT-N03 | High | ❔45 | ❔39 | ❌80 | ✅80 | ✅90 | ❔45 | **CONFLICT** | Zero Q_OS_TVOS preprocessor guards in C++ despite 19 QML references — build failure |
| DECL-N01 | Low | ⚠️45 | ✅78 | ✅75 | ✅75 | ✅95 | ⚠️50 | split | MarkersModel::keySearch — default params in definition but not declaration |
| DECL-N02 | Low | ⚠️40 | ✅78 | ✅85 | ⚠️60 | ✅90 | ⚠️50 | split | SessionModel::resetInternalData() missing override keyword and Qt 6 version guard |
| COLOR-01 | Medium | ✅70 | ⚠️58 | ⚠️50 | ✅80 | ✅90 | ✅70 | split | ProjectionsManager.qml uses invalid "initial" color — repro of R4-ROOT-02 |
| COLOR-02 | Medium | ⚠️40 | ⚠️58 | ✅75 | ✅75 | ✅90 | ✅68 | split | Hardcoded #EED text invisible on light themes — WheelSettingsOverlay |
| COLOR-03 | Low | ⚠️40 | ⚠️58 | ⚠️45 | ⚠️60 | ✅90 | ✅68 | split | velocityText ColorAnimation flash: #BBB → #FFF → #CCC jump |
| COLOR-04 | Low | ⚠️45 | ⚠️58 | ✅65 | ⚠️55 | ✅90 | ✅68 | split | ReadRegionOverlay ColorAnimation tracks __fillColor that never changes |
| COLOR-05 | Low | ⚠️40 | ⚠️58 | ⚠️40 | ✅70 | ✅85 | ⚠️50 | split | Prompter scrollbar gradient hardcodes #CCC/#998/#665 — low contrast on light backgrounds |
| COLOR-06 | Low | ⚠️40 | ⚠️58 | ⚠️40 | ✅70 | ✅85 | ⚠️50 | split | Countdown #FFF digits on #333-at-0.48-overlay — insufficient contrast on light backgrounds |
| COLOR-07 | Low | ⚠️55 | ⚠️58 | ✅65 | ✅75 | ✅90 | ⚠️50 | split | CSS default stylesheet hardcodes #FFFFFF body text — ignores user text color |
| EVT-N10 | Medium | ❔45 | ⚠️58 | ✅70 | ✅75 | ❌60 | ❔45 | **CONFLICT** | Editor Ctrl+Letter shortcuts don't accept event — marker key-search double-fires |
| EVT-N11 | Low | ⚠️45 | ⚠️58 | ❌70 | ✅75 | ❌70 | ✅68 | **CONFLICT** | windowStayOnTopButton lacks focusPolicy — unreachable via keyboard |
| EVT-N12 | Low | ⚠️50 | ⚠️58 | ✅60 | ⚠️60 | ⚠️50 | ✅68 | split | velocityDragArea and viewport.mouse share z:5 — wheel dispatch ambiguous |
| STATE-N01 | High | ❔45 | ✅84 | ⚠️50 | ✅80 | ❌70 | ❔45 | **CONFLICT** | Shadowed Prompting→Editing transition — velocity default never saved |
| STATE-N02 | Medium | ⚠️50 | ✅78 | ✅75 | ✅80 | ✅80 | ✅68 | split | Find.toggle() uses !visible instead of !isOpen — can't close during Prompting |
| STATE-N03 | Low | ⚠️50 | ✅78 | ✅65 | ⚠️60 | ✅80 | ✅68 | split | Countdown Running restarts dissolveIn unnecessarily — visual dim-to-bright flash |
| STATE-N04 | Low | ❔45 | ✅78 | ✅70 | ⚠️55 | ✅75 | ❔45 | split | loop animation cancel() state change overridden by toggle() due to QML batching |
| SIZE-N01 | Medium | ✅60 | ✅78 | ✅80 | ✅75 | ✅95 | ✅60 | AGREE | concentricCircles Shape has conflicting anchors.fill + anchors.centerIn |
| SIZE-N02 | Low | ✅55 | ✅78 | ✅75 | ✅70 | ✅65 | ✅55 | AGREE | Three Button children of Row have dead anchors.bottom declarations |
| CONST-N01 | Low | ⚠️40 | ⚠️58 | ✅60 | ✅70 | ❌75 | ⚠️50 | **CONFLICT** | getMarkerKey() not const — pure reader without side effects |
| CONST-N02 | Low | ⚠️40 | ⚠️58 | ✅60 | ✅70 | ❌75 | ⚠️50 | **CONFLICT** | getMarkerHref() not const — identical pattern |
| CONST-N03 | Low | ⚠️40 | ⚠️58 | ✅55 | ✅70 | ❌70 | ⚠️50 | **CONFLICT** | MarkersModel::previousMarker(), nextMarker(), keySearch(), binarySearch() not const |
| CONST-N04 | Low | ⚠️40 | ⚠️58 | ✅60 | ✅70 | ❌70 | ⚠️50 | **CONFLICT** | GlobalHotkeys::globalShortcutKey(Action) not const — Q_INVOKABLE pure query |
| CONST-N05 | Low | ⚠️40 | ⚠️58 | ✅65 | ✅70 | ❌65 | ⚠️50 | **CONFLICT** | Unnecessary copy via const auto instead of const auto& in extendLastMarker |
| SAVE-N01 | Medium | ⚠️55 | ✅78 | ✅70 | ✅80 | ✅80 | ✅68 | split | loadFromNetworkFinihed sets m_fileUrl to phantom QTemporaryFile path |
| SAVE-N02 | High | ⚠️50 | ✅84 | ✅75 | ✅80 | ✅85 | ✅68 | split | iOS save flow never updates C++ m_fileUrl — file URL perpetually stale |
| SAVE-N03 | Medium | ✅55 | ✅78 | ✅75 | ✅80 | ✅85 | ✅55 | AGREE | saveAs() never updates _fileSystemWatcher — watches stale file after save-as |
| SAVE-N04 | Low | ⚠️45 | ✅78 | ✅65 | ✅75 | ✅70 | ⚠️50 | split | save() unnecessary QString→std::string→QString round-trip through locale encoding |
| SAVE-N05 | Low | ✅50 | ✅78 | ✅70 | ✅80 | ✅80 | ✅50 | AGREE | save() broken on Android content:// URIs — empty filename |
| LOAD-N01 | Medium | ⚠️50 | ✅78 | ✅65 | ✅75 | ✅70 | ✅68 | split | TOCTOU race between QFile::exists() and file.open() in load() |
| LOAD-N02 | Low | ⚠️50 | ✅78 | ❌75 | ✅75 | ❌75 | ✅68 | **CONFLICT** | reset() emits 12 NOTIFY signals when open() fails but exists() succeeds |
| SHDR-N01 | Medium | ✅65 | ✅78 | ✅85 | ✅75 | ✅90 | ✅65 | AGREE | Math.cos/Math.sin used with degrees value — shadow offset diagonal instead of horizontal |
| RAII-N01 | Medium | ⚠️50 | ✅78 | ✅60 | ✅80 | ✅85 | ⚠️50 | split | QDrag object never deleteLater'd after exec() — leaks on rejected drags |
| RAII-N02 | Low | ⚠️50 | ⚠️58 | ✅55 | ✅75 | ✅80 | ✅68 | split | IosSaveDialog::m_tempDir created unconditionally on all platforms — wasted I/O |
| RAII-N03 | Medium | ⚠️50 | ✅78 | ❌70 | ✅80 | ❌70 | ✅68 | **CONFLICT** | QProcess orphan — child process detached on waitForFinished() timeout |
| Z-N01 | Medium | ⚠️45 | ✅78 | ⚠️45 | ⚠️60 | ❌65 | ⚠️50 | **CONFLICT** | CursorAutoHide has no explicit z — hover detection fragile against Kirigami internals |
| Z-N02 | Low | ⚠️40 | ✅78 | ⚠️40 | ✅70 | ❌70 | ✅68 | **CONFLICT** | Two OverlaySheets have z:1 while nine others have none — inconsistent stacking |
| Z-N03 | Low | ⚠️40 | ✅78 | ⚠️40 | ⚠️55 | ❌60 | ✅68 | **CONFLICT** | ComboBox Popup z:103 inside OverlaySheets with z:1 — disconnected layering |
| Z-N04 | Low | ⚠️45 | ✅78 | ✅65 | ⚠️55 | ⚠️50 | ⚠️50 | split | PrompterBackground (z:0) renders above viewport.mouse (z:0) — latent input intercept |
| TIME-N01 | Low | ✅60 | ✅78 | ✅85 | ✅70 | ✅90 | ✅60 | AGREE | copyrightYear computed then discarded — stale "2020-2026" in About after 2026 |
| XFRM-N01 | Low | ❔45 | ❔39 | ⚠️45 | ⚠️60 | ✅85 | ❔45 | split | PrompterView.qml Rotation permanently overridden by PrompterPage.qml |
| API-N01 | Medium | ⚠️50 | ✅78 | ✅65 | ✅75 | ✅80 | ✅68 | split | setAlignment() missing null-cursor guard — crash risk with no document |
| API-N02 | Medium | ✅80 | ✅78 | ✅80 | ✅80 | ✅85 | ✅80 | AGREE | selectionIsLowerCase NOTIFY signal is wrong — fontCapitalizationChanged, never emitted for case changes |
| API-N03 | Medium | ⚠️50 | ✅78 | ✅75 | ✅75 | ✅85 | ✅68 | split | CursorAutoHide.qml unconditionally dereferences pageStack.currentItem.prompter |
| API-N04 | Low | ⚠️35 | ✅78 | ✅65 | ✅70 | ⚠️50 | ✅68 | split | setMarker(bool) misleadingly named — sets regular marker, not any marker |
| API-N05 | Low | ⚠️50 | ✅78 | ✅70 | ✅70 | ✅70 | ✅68 | split | fileName()/fileType() return fabricated defaults — can't distinguish "no file" from "untitled.html" |
| API-N06 | Low | ✅80 | ⚠️58 | ✅80 | ✅85 | ✅70 | ✅80 | split | SystemFontChooserDialog::show() calls setText() on same label twice — dead code |
| API-N07 | Low | ✅55 | ✅78 | ✅75 | ⚠️65 | ✅90 | ✅55 | split | SpellChecker::encode() fallback says "Latin-1" but calls toLocal8Bit() |
| ARC-01 |  | ⚠️35 | ⚠️48 | ❌50 | ⚠️55 | ✅60 | ⚠️50 | **CONFLICT** | Velocity physics engine entirely in QML (~20 readonly property bindings) |
| ARC-02 |  | ⚠️35 | ⚠️48 | ❌50 | ⚠️55 | ✅60 | ⚠️50 | **CONFLICT** | Arc-03 Search/replace state machine fully in QML (50+ lines) |
| ARC-03 |  | ⚠️35 | ⚠️48 | ❌50 | ⚠️55 | ✅60 | ⚠️50 | **CONFLICT** | OBS WebSocket v5 protocol in QML — opcode dispatch, auth, subscription |
| ARC-04 |  | ⚠️40 | ⚠️48 | ❌50 | ⚠️55 | ✅60 | ⚠️50 | **CONFLICT** | DocumentHandler is 2295-line god class spanning file I/O, network, HTML filtering, markers, spellcheck, drag-drop, images, search, undo, clipboard, sleep prevention, font dialog |
| ARC-05 |  | ⚠️35 | ⚠️48 | ❌50 | ⚠️55 | ✅60 | ⚠️50 | **CONFLICT** | Prompter.qml is 3139-line god component spanning velocity, state machine, keyboard, WebSocket, markers, spellcheck UI, file dialogs, WYSIWYG toggle, shadows |
| ARC-06 |  | ⚠️35 | ⚠️48 | ❌50 | ⚠️50 | ✅60 | ⚠️50 | **CONFLICT** | qmlutil.hpp is utility grab-bag with 10+ unrelated functions |
| KEY-N01 | Medium | ❔45 | ❔39 | ✅70 | ✅75 | ✅90 | ❔45 | split | Named marker key binding silently discards all modifier information |
| CLI-N01 | Medium | ⚠️50 | ✅78 | ⚠️55 | ⚠️65 | ✅90 | ✅68 | split | --version flag non-functional — version string empty when parser processes |
| DPR-N01 | Medium | ✅55 | ✅78 | ✅70 | ✅75 | ✅80 | ✅55 | AGREE | Prompter.qml uses Screen.devicePixelRatio (global) instead of screen.devicePixelRatio (window) |
| SCALE-N01 | Medium | ⚠️50 | ✅78 | ✅65 | ✅75 | ✅80 | ✅68 | split | Right pointer xScale: -1 mirrors text pointers — backwards/unreadable text |
| ORIENT-N01 | Low | ⚠️45 | ⚠️58 | ✅60 | ⚠️55 | ✅70 | ✅68 | split | TimerClock binary width>height orientation creates sharp 2x font jump at 1:1 |
| BIND-N01 | Low | ⚠️50 | ✅92 | ✅65 | ⚠️55 | ❌70 | ✅68 | **CONFLICT** | contentWidth undefined for Shape/Image pointer types — transform origin silently wrong |
| STR-CNV | Low | ⚠️45 | ✅78 | ✅60 | ✅75 | ❌60 | ⚠️50 | **CONFLICT** | 5 defensive validation gaps: toInt() without ok flag in getMarkerKey, parse(×2), setFontSize, and 32 hotkey reads |
| SHADOW-N03 | High | ✅70 | ✅84 | ❌75 | ✅75 | ✅95 | ✅70 | **CONFLICT** | id: stopwatch shadows property bool stopwatch — timersEnabled always true |
| SHADOW-N04 | Low | ⚠️50 | ✅78 | ✅65 | ⚠️60 | ❌65 | ✅68 | **CONFLICT** | id: frame shadows property bool frame — latent hazard |
| LINK-N01 | High | ✅65 | ✅84 | ✅80 | ✅80 | ✅85 | ✅65 | AGREE | Qt::Network not linked on iOS static build — unresolved symbols |
| LINK-N02 | High | ✅65 | ✅84 | ✅80 | ✅80 | ✅85 | ✅65 | AGREE | Qt::Network not linked on WASM static build — same as LINK-N01 |
| LINK-N03 | Medium | ⚠️50 | ✅78 | ✅85 | ✅75 | ✅80 | ✅68 | split | Qt::WebSockets found as REQUIRED but never explicitly linked |
| LINK-N04 | Medium | ❔45 | ✅78 | ❌85 | ✅75 | ✅75 | ❔45 | **CONFLICT** | KF6::GlobalAccel find_package/link mismatch on Haiku |
| COMP-N01 | Low | ✅55 | ✅92 | ✅95 | ✅75 | ✅80 | ✅55 | AGREE | Case-sensitive duplicate detection in setLanguages() |
| COMP-N02 | Medium | ✅50 | ✅78 | ✅90 | ✅80 | ✅85 | ✅50 | AGREE | Case-sensitive suffix check misses mixed-case extensions — silent format loss |
| COMP-N03 | Low | ⚠️50 | ✅78 | ✅95 | ⚠️60 | ✅70 | ⚠️50 | split | regularMarker() same double-textCursor anti-pattern as LOG-07 |
| LBL-N01 | Medium | ⚠️45 | ⚠️58 | ✅70 | ✅70 | ✅90 | ⚠️50 | split | All 12 Sliders in EditorToolbar missing Layout.fillWidth: true — cramped |
| LBL-N02 | Medium | ⚠️40 | ⚠️52 | ✅80 | ✅70 | ✅80 | ❌72 | **CONFLICT** | 11 Labels with Layout.bottomMargin: -14 — undefined behavior, overlap risk |
| LBL-N03 | Low | ⚠️40 | ⚠️58 | ✅85 | ⚠️55 | ✅70 | ✅68 | split | PrompterView 3× height overflow in theforce debug mode |
| LAY-N01 | Low | ⚠️45 | ⚠️58 | ❔50 | ✅70 | ✅80 | ⚠️50 | split | 10 Labels with Layout.margins but inside MouseArea, not direct layout child — dead |
| LAY-N02 | Low | ⚠️40 | ⚠️58 | ❔50 | ✅70 | ✅80 | ⚠️50 | split | WheelSettingsOverlay explanation text constrained to single column in 2-column GridLayout |
| DLG-N10 | Medium | ⚠️45 | ✅78 | ✅90 | ✅75 | ✅85 | ✅68 | split | TimerClock ColorDialog selectedColor never initialized from persisted settings |
| DLG-N11 | Low | ⚠️45 | ✅78 | ✅90 | ✅75 | ✅70 | ✅68 | split | PrompterPage ColorDialogs — dead acceptedColor property binding |
| QPROP-N02 | Medium | ❌50 | ❌76 | ✅95 | ✅75 | ✅80 | ❌50 | **CONFLICT** | comesFromNetwork Q_PROPERTY missing WRITE clause |
| PATH-N01 | Medium | ⚠️50 | ✅78 | ✅85 | ✅80 | ✅80 | ✅68 | split | save() fragile percent-encoding round-trip — broken for UNC paths |
| PATH-N02 | Medium | ✅60 | ✅78 | ✅95 | ✅80 | ✅85 | ✅60 | AGREE | reload() constructs file:// URL via raw string concat — #/? in filenames break URL |
| MOB-01 | Medium | ✅70 | ✅92 | ✅80 | ✅80 | ✅90 | ✅70 | AGREE | Android: projectionManager undefined — 3 unguarded reference sites |
| MOB-02 | Medium | ⚠️50 | ✅78 | ✅95 | ✅80 | ✅80 | ✅68 | split | No +ios/ QML selector — iOS inherits base main.qml with desktop-only components |
| MOB-03 | Medium | ⚠️50 | ✅92 | ✅95 | ✅75 | ✅85 | ✅68 | split | iOS: IosSaveDialog silently hangs QML caller when temp dir invalid |
| MOB-04 | Low | ✅65 | ✅78 | ✅95 | ✅75 | ✅90 | ✅65 | AGREE | Android: restartApplication() quits without restart |
| MOB-05 | Low | ✅85 | ✅78 | ✅95 | ✅80 | ✅85 | ✅85 | AGREE | Android: Missing INTERNET permission in manifest |
| MOB-06 | Low | ✅60 | ✅78 | ✅85 | ✅75 | ✅80 | ✅60 | AGREE | Android: PrompterPage display delegate Component.onCompleted references projectionManager — startup TypeError |
| MENU-N01 | Medium | ✅55 | ⚠️58 | ✅95 | ✅75 | ✅75 | ✅55 | split | contextMenu.popup(this) missing click coordinates — menu at wrong position |
| MENU-N02 | Medium | ✅60 | ⚠️58 | ✅95 | ✅80 | ✅90 | ✅60 | split | Mobile "Add to dictionary" missing %1 placeholder — word never shown |
| MENU-N03 | Medium | ⚠️55 | ⚠️58 | ✅95 | ✅75 | ✅85 | ✅68 | split | Text alignment menu RTL swap: labels swap but actions don't |
| MENU-N04 | Low | ✅50 | ⚠️58 | ✅75 | ✅70 | ✅70 | ✅50 | split | Trailing empty MenuSeparator at end of mobile context menu |
| MENU-N05 | Low | ⚠️45 | ⚠️58 | ✅95 | ✅70 | ✅70 | ✅68 | split | "Redo" context menu item missing & accelerator |
| MENU-N06 | Low | ⚠️50 | ⚠️58 | ⚠️70 | ⚠️60 | ✅85 | ✅68 | split | Paste behavior inconsistent between context menu and global Edit menu |
| DBG-N01 | Medium | ✅60 | ⚠️58 | ✅95 | ✅75 | ✅90 | ✅60 | split | OBS WebSocket auth challenge+salt logged to console in release builds |
| DBG-N02 | Low | ✅55 | ⚠️58 | ✅95 | ✅70 | ✅80 | ✅55 | split | Velocity debug logging active in production |
| DBG-N03 | Low | ⚠️45 | ⚠️52 | ⚠️60 | ⚠️60 | ❌60 | ✅68 | **CONFLICT** | Latent debug state leak: pointers/debug Setting persists Guides checkbox |
| DBG-N04 | Low | ✅60 | ⚠️58 | ✅90 | ✅70 | ✅80 | ✅60 | split | qDebug() in namedMarker()/setMarker() active in release |
| WARN-N01 | Low | ⚠️40 | ⚠️58 | ✅80 | ✅75 | ✅70 | ✅68 | split | SpellHighlighter::isEnabled() — dead code, never called |
| WARN-N02 | Low | ✅60 | ⚠️58 | ✅85 | ✅75 | ✅70 | ✅60 | split | SpellChecker::addWord() — dead public API, never called |
| WARN-N03 | Low | ⚠️45 | ⚠️58 | ✅90 | ✅70 | ✅70 | ⚠️50 | split | quint64→int implicit narrowing in nextMarker()/previousMarker() |
| WARN-N04 | Low | ✅55 | ⚠️58 | ✅95 | ✅70 | ✅70 | ✅55 | split | QProcess::startDetached() bool return silently ignored |
| FLOW-N01 | Medium | ✅65 | ✅78 | ✅90 | ✅80 | ✅90 | ✅65 | AGREE | setKeyMarker() calls setAnchor("#") — const char*→bool conversion, href never set |
| FLOW-N02 | Medium | ❔45 | ⚠️58 | ✅90 | ✅75 | ✅85 | ❔45 | split | increaseVelocity()/decreaseVelocity() skip velocity change when paused |
| DEF-N01 | Medium | ❌65 | ❌76 | ✅90 | ✅75 | ✅75 | ❌65 | **CONFLICT** | Flickable.flicking undefined in Qt 6 — wrong cursor during momentum scroll |
| DEF-N02 | Medium | ⚠️50 | ⚠️58 | ✅95 | ✅75 | ✅75 | ✅68 | split | DropArea internalDrag always false — internal drag handler dead code |
| TMR-N01 | Medium | ⚠️50 | ⚠️58 | ✅95 | ✅75 | ✅85 | ✅68 | split | resetBackground Timer not stopped when new background loaded — race erases new image |
| TMR-N02 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅80 | ✅85 | ✅68 | split | Windows onFrameSwapped missing qmlutil.r(p) — per-frame grab result leak |
| CMAKE-N05 | Low | ✅55 | ✅78 | ✅85 | ✅75 | ✅80 | ✅55 | AGREE | foreach(file IN LISTS icon_files doc) — "doc" never defined |
| PRE-N01 | Low | ⚠️55 | ⚠️58 | ⚠️75 | ❌80 | ✅85 | ✅68 | **CONFLICT** | Preprocessor uses `or` instead of `\|\|` in 6 #if directives — MSVC build break |
| CNTD-N01 | Low | ⚠️50 | ⚠️58 | ✅85 | ⚠️60 | ✅75 | ✅68 | split | Countdown Running: dissolveIn and dissolveOut compete for same opacity when __iterations===__disappearWithin===1 |
| QF-N02 | Low | ⚠️45 | ⚠️58 | ✅85 | ✅70 | ✅70 | ✅68 | split | QDir::entryList missing QDir::Readable in availableDictionaries() |
| QF-N03 | Low | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅75 | ✅68 | split | TOCTOU: QFile::exists() → QFile::copy() in resource cache extraction |
| TXT-CRIT | Critical | ❔45 | ❔39 | ✅85 | ✅80 | ✅95 | ❔45 | split | Plain 'v'/'V' keypress silently consumed — letter 'v' cannot be typed |
| TXT-N03 | Medium | ✅80 | ✅78 | ✅90 | ✅80 | ✅90 | ✅80 | AGREE | Toolbar paste and Edit menu paste bypass HTML sanitization |
| TXT-N04 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅75 | ✅80 | ✅68 | split | goToNextMarker() temporarily sets cursorPosition=-1 — corrupts cursor state |
| INT-N01 | Low | ⚠️45 | ⚠️58 | ✅90 | ✅70 | ✅70 | ⚠️50 | split | quint64→int narrowing at DocumentHandler→MarkersModel boundary (4 sites) |
| INT-N02 | Medium | ⚠️40 | ✅78 | ✅90 | ⚠️60 | ✅85 | ⚠️50 | split | replaceAll() returns long — 32-bit overflow on Windows x64 |
| INT-N03 | Low | ⚠️40 | ⚠️58 | ✅80 | ✅70 | ✅70 | ⚠️50 | split | 6 qsizetype→int narrowing conversions across models and loops |
| URL-N03 | Medium | ✅55 | ⚠️58 | ✅90 | ✅80 | ✅80 | ✅55 | split | Network-loaded HTML lacks base URL — relative resources broken |
| URL-N04 | Low | ✅60 | ⚠️58 | ✅90 | ✅75 | ✅85 | ✅60 | split | loadFromNetwork() validates wrong URL instance |
| URL-N05 | Medium | ✅55 | ⚠️58 | ✅90 | ✅80 | ✅85 | ✅55 | split | openFromRemote() blindly prepends http:// to non-HTTP schemes |
| PERF-N01 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅75 | ⚠️50 | split | onFrameSwapped calls markerCompare() unconditionally — wasted JS call every frame |
| PERF-N02 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅80 | ✅68 | split | RecentDocuments._load() blocks startup with N synchronous createObject() calls |
| PERF-N03 | Low | ⚠️50 | ⚠️58 | ✅85 | ⚠️60 | ✅75 | ⚠️50 | split | velocityDragOverlay hot-loop calls velocity functions without throttling |
| ERR-N01 | Medium | ✅60 | ✅78 | ✅90 | ✅75 | ✅80 | ✅60 | AGREE | removeCustomWord() silently drops dictionary languages on partial reload failure |
| ERR-N02 | Medium | ⚠️55 | ⚠️58 | ✅95 | ✅75 | ✅80 | ✅68 | split | insertImageAt() async callback silently discards 3 failure modes |
| PATH-N03 | High | ❔45 | ✅84 | ✅90 | ✅75 | ⚠️65 | ❔45 | split | Wrong ../fonts/ depth in +android and +windows FontLoader paths |
| SIG-N03 | Low | ⚠️40 | ✅78 | ✅75 | ✅70 | ✅70 | ⚠️50 | split | MessageDialog.onButtonClicked declares unused second parameter role |
| QOBJ-N01 | Low | ⚠️40 | ✅78 | ✅85 | ✅70 | ✅60 | ⚠️50 | split | QmlUtil missing constructor with parent parameter |
| TAB-N01 | Medium | ⚠️50 | ✅78 | ⚠️60 | ✅75 | ✅80 | ✅68 | split | PointerSettings TabButton onClicked skips currentIndex assignment |
| REGEX-CRIT-01 | High | ❔45 | ❔39 | ✅85 | ✅80 | ✅90 | ❔45 | split | regex_4 destroys <body> tag — removes opening tag instead of color attributes |
| REGEX-CRIT-02 | High | ✅55 | ✅84 | ✅95 | ✅85 | ✅90 | ✅55 | AGREE | searchRegEx.setPattern() from user input — isValid() never called |
| REGEX-N04 | Medium | ⚠️50 | ✅78 | ✅90 | ✅80 | ✅85 | ✅68 | split | ReDoS — user-supplied regex has no length limit, timeout, or backtracking guard |
| REGEX-N05 | Low | ✅70 | ✅78 | ✅85 | ✅70 | ✅80 | ✅70 | AGREE | regex_0 and regex_3 use . (any-char) instead of \. (literal dot) in decimal matching |
| REGEX-N06 | Medium | ✅55 | ✅78 | ✅90 | ✅75 | ✅85 | ✅55 | AGREE | imgSrcRegex captures wrong src when data-src follows real src |
| VCI-N01 | Low | ⚠️40 | ⚠️48 | ✅95 | ✅70 | ✅70 | ⚠️50 | split | At-end action buttons use inconsistent font scaling (1/1.5 vs 1/1.75) in same group |
| VCI-N02 | Low | ⚠️40 | ⚠️48 | ✅95 | ✅70 | ✅70 | ⚠️50 | split | upperControls and bottomControls fade to different opacity levels during Prompting |
| VCI-N03 | Low | ⚠️40 | ⚠️48 | ⚠️70 | ⚠️55 | ✅90 | ✅68 | split | Hardcoded divider/separator/border colors (#292929, #606060, #808080) break theme adaptation |
| UTF-N01 | Medium | ⚠️50 | ✅78 | ✅90 | ✅75 | ✅90 | ✅68 | split | text.truncate(64) can split UTF-16 surrogate pairs — corrupted display |
| AND-CRIT-01 | Critical | ✅85 | ✅84 | ✅95 | ✅85 | ✅95 | ✅85 | AGREE | Missing android.permission.INTERNET — all network silently fails |
| AND-HIGH-01 | High | ⚠️50 | ⚠️58 | ✅80 | ✅80 | ✅80 | ✅68 | split | Android back button doesn't dismiss overlays/drawers before close |
| AND-HIGH-02 | High | ✅60 | ✅84 | ✅90 | ✅80 | ✅90 | ✅60 | AGREE | Android screen never sleeps after prompter use |
| AND-HIGH-03 | High | ✅65 | ✅84 | ✅95 | ✅80 | ✅95 | ✅65 | AGREE | factoryReset() quits Android app without restarting |
| AND-MED-01 | Medium | ⚠️45 | ⚠️58 | ✅95 | ✅75 | ✅95 | ✅68 | split | Missing intent-filter for opening files from other apps |
| CLP-N01 | Medium | ⚠️50 | ✅78 | ⚠️70 | ✅75 | ✅85 | ✅68 | split | Copy/Cut exports unfiltered HTML to system clipboard |
| CLP-N02 | Medium | ⚠️50 | ⚠️58 | ✅95 | ✅75 | ✅90 | ✅68 | split | DropArea external drop never calls drop.accept() |
| CLP-N03 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅90 | ✅68 | split | DropArea external drop: URLs consumed preferentially — text silently lost |
| SWT-N01 | Medium | ✅60 | ✅78 | ✅95 | ✅75 | ✅90 | ✅60 | AGREE | OBS WebSocket Switch checked binding broken on first toggle |
| IMH-SYS | Medium | ⚠️40 | ⚠️58 | ⚠️65 | ✅75 | ✅95 | ❌72 | **CONFLICT** | Systemic absence of inputMethodHints on ALL TextFields (16 sites) |
| EKA-SYS | Low | ⚠️40 | ⚠️58 | ⚠️65 | ✅70 | ✅90 | ❌72 | **CONFLICT** | Systemic absence of EnterKeyAction on ALL TextFields (7 sites) |
| WINDOW-N01 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅75 | ✅85 | ✅68 | split | Projection windows not closed on main window close — orphaned on Linux |
| GSW-N01 | Medium | ⚠️45 | ⚠️58 | ✅90 | ✅70 | ✅80 | ✅68 | split | MarkersDrawer SwipeListItem navigates on swipe — gesture conflict on touch |
| GSW-N02 | Low | ❔45 | ❔39 | ✅85 | ⚠️60 | ✅80 | ❔45 | split | Flickable onDragStarted uses stale __iBackup after non-prompting drags |
| LVW-N01 | Low | ⚠️45 | ⚠️58 | ✅85 | ✅70 | ✅70 | ✅68 | split | InputsOverlay.qml ListView currentIndex: PointerSettings.States.Arrow — copy-paste error |
| META-N01 | Low | ⚠️45 | ⚠️58 | ✅95 | ✅70 | ✅75 | ✅68 | split | QMetaObject::invokeMethod return value unchecked — silent failure on WASM |
| LOG-N04 | Low | ❌70 | ✅78 | ✅90 | ✅70 | ❌90 | ❌70 | **CONFLICT** | qWarning("reloading") fires unconditionally — misleading when URL mismatches |
| LOG-N05 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅80 | ✅68 | split | Q_UNREACHABLE() in m_setGlobalShortcut() — UB in release on new enum value |
| LOG-N06 | Medium | ✅70 | ✅78 | ✅95 | ✅75 | ✅90 | ✅70 | AGREE | No error log when saveAs() write/flush fail — silent data loss |
| LOG-N07 | Medium | ✅55 | ⚠️58 | ✅95 | ✅75 | ✅90 | ✅55 | split | No error log in loadFromNetworkFinihed() — silent bad-data load |
| FONT-N01 | Medium | ⚠️45 | ❔39 | ✅95 | ✅75 | ✅70 | ❌72 | **CONFLICT** | font.family: "Monospace" never resolves — no such font on any OS |
| FONT-N02 | Low | ✅65 | ⚠️58 | ✅95 | ✅70 | ✅90 | ✅65 | split | FontLoader id typo: westernSeriousSansfFont — stray 'f' in "Sans" |
| XML-N01 | Medium | ✅55 | ✅92 | ✅90 | ✅75 | ✅90 | ✅55 | AGREE | android:background="#303030" invalid on \<activity\> — silently ignored |
| CMAKE-N02 | Low | ✅55 | ✅78 | ✅95 | ✅70 | ✅90 | ✅55 | AGREE | INTERFACE_LINK_LIBRARIES on executable target — no-op |
| CMAKE-N03 | Medium | ⚠️50 | ❌76 | ✅85 | ✅75 | ✅80 | ✅68 | **CONFLICT** | qt_wrap_ui conflicts with global AUTOUIC — double UI processing |
| CMAKE-N04 | Medium | ✅55 | ✅78 | ✅90 | ✅75 | ✅90 | ✅55 | AGREE | Relative ../build path in install rules — out-of-tree build failure |
| SETUP-N01 | Medium | ❔40 | ❔39 | ✅95 | ✅75 | ✅90 | ❔40 | split | setup.sh uses windeployqt.exe (Qt 5) — should be windeployqt6.exe (Qt 6) |
| POP-N01 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅90 | ✅68 | split | ESC cascade missing dictionariesSheet — undismissable by keyboard |
| POP-N02 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅90 | ✅68 | split | ESC cascade missing customWordsSheet — undismissable by keyboard |
| POP-N03 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅75 | ✅90 | ✅68 | split | ESC cascade missing obsConfiguration — undismissable by keyboard despite alias |
| POP-N04 | Medium | ✅65 | ⚠️58 | ✅95 | ✅75 | ✅90 | ✅65 | split | CountdownConfiguration SpinBoxes use focus: true (JS label) instead of focus = true |
| RND-N01 | Low | ⚠️50 | ⚠️58 | ✅95 | ✅70 | ❌70 | ✅68 | **CONFLICT** | forceQtTextRenderer dead on Apple platforms — unconditionally uses NativeRendering |
| RND-N02 | Low | ⚠️45 | ⚠️58 | ✅85 | ✅70 | ✅85 | ✅68 | split | Missing smooth: true on background Image — aliased upscale |
| RND-N03 | Low | ⚠️50 | ⚠️58 | ✅85 | ✅70 | ✅80 | ✅68 | split | Missing smooth: true on projection Image — aliased text on external displays |
| ST-N02 | Medium | ✅50 | ⚠️58 | ✅95 | ✅70 | ✅85 | ✅50 | split | Dead overlay.state PropertyChanges — overlay has no states array |
| CFG-N01 | Medium | ⚠️50 | ⚠️58 | ✅95 | ✅70 | ✅80 | ✅68 | split | Desktop MimeType incomplete — only text/html, missing text/plain and text/markdown |
| CFG-N02 | Low | ✅55 | ⚠️58 | ❔40 | ✅70 | ✅95 | ✅55 | split | v1.1.3 release date "2022-1-16" breaks chronological order — should be 2023-01-16 |
| CFG-N03 | Low | ✅60 | ⚠️58 | ✅95 | ✅70 | ✅95 | ✅60 | split | "fixedd" typo in v2.0.2 release description |
| TP-SYS | Medium | ⚠️40 | ⚠️58 | ⚠️70 | ✅70 | ✅75 | ⚠️50 | split | Systemic absence of ToolTip on ~60+ controls across entire application |
| TP-N01 | Medium | ⚠️55 | ⚠️58 | ✅90 | ✅70 | ✅80 | ✅68 | split | "Error loading file..." used as document content, not placeholderText |
| WATCH-N01 | Medium | ⚠️50 | ✅78 | ✅95 | ✅70 | ✅80 | ✅68 | split | addPath() return never checked — silent watch failure |
| WATCH-N02 | Medium | ⚠️50 | ✅78 | ✅90 | ✅70 | ✅80 | ✅68 | split | removePath() return never checked — stale path causes double-watch |
| WATCH-N03 | Medium | ❔45 | ✅78 | ✅90 | ✅75 | ✅70 | ❔45 | split | Watcher not refreshed after fileChanged — stale inotify on Linux atomic saves |
| WATCH-N04 | Low | ⚠️45 | ✅78 | ✅85 | ✅70 | ✅85 | ✅68 | split | unblockFileWatcher() dereferences _fileSystemWatcher without null guard |
| MODEL-N01 | Medium | ✅60 | ✅78 | ✅90 | ✅75 | ✅80 | ✅60 | AGREE | MarkersModel::rowCount ignores parent.isValid() — returns full size for child probe |
| MODEL-N02 | Low | ✅55 | ⚠️58 | ✅85 | ✅70 | ✅85 | ✅55 | split | SessionModel::clearDataPoints lacks empty-model guard before beginRemoveRows |
| COERC-N01 | High | ❔45 | ✅84 | ❌85 | ✅75 | ✅90 | ❔45 | **CONFLICT** | parseInt("") → NaN state bootstrap — first toggle() bricks state machine |
| COERC-N02 | Medium | ✅55 | ✅78 | ✅95 | ✅75 | ✅85 | ✅55 | AGREE | Unvalidated string-to-number injects NaN into root.__opacity — all opacity dead |
| COERC-N03 | Low | ⚠️50 | ⚠️58 | ✅80 | ✅70 | ✅80 | ✅68 | split | real→int truncation in WindowDragger position compounds drift |
| QLOAD-N01 | Medium | ⚠️50 | ✅78 | ✅95 | ✅75 | ✅85 | ✅68 | split | InputsOverlay toggleButtonsOff() null-check bypass — crash on slow async Loaders |
| DETACH-N01 | Low | ⚠️40 | ⚠️58 | ✅75 | ✅70 | ❌60 | ⚠️50 | **CONFLICT** | 4 non-const operator[] on QList in keySearch() — unnecessary implicit sharing detach |
| COLOR-CRIT-01 | High | ❔45 | ❔39 | ✅95 | ✅80 | ✅90 | ❌72 | **CONFLICT** | selectionColor #333d9ef3 — alpha channel reversed (#AARRGGBB vs #RRGGBBAA), selection invisible |
| SYM-N01 | Low-Medium | ⚠️40 | ⚠️58 | ✅85 | ⚠️55 | ✅65 | ⚠️50 | split | 6 RTL/symmetry issues across PointerSettings, Find, PrompterView, Prompter, PrompterPage |
| CLIP-CRIT-01 | Critical | ✅85 | ✅84 | ✅95 | ✅80 | ✅90 | ✅85 | AGREE | Paste via toolbar button and File menu bypasses HTML sanitization |
| CLIP-N04 | Medium | ✅65 | ⚠️58 | ✅90 | ✅75 | ✅80 | ✅65 | split | Image-only clipboard paste — button enabled but does nothing |
| INT-N04 | Medium | ✅55 | ⚠️58 | ✅85 | ✅75 | ✅85 | ✅55 | split | OBS URL/Password fields disabled when WebSocket enabled — inverted logic |
| INT-N05 | Medium | ✅55 | ⚠️58 | ✅90 | ✅75 | ✅85 | ✅55 | split | PropertyChanges permanently destroys CheckBox checked bindings on PointerSettings tab switch |
| FMT-N01 | Medium | ✅50 | ✅78 | ✅95 | ✅75 | ✅85 | ✅50 | AGREE | Step Speed onAccepted displays 100x correct value |
| FMT-N02 | Medium | ✅50 | ✅78 | ✅95 | ✅75 | ✅85 | ✅50 | AGREE | Step Acceleration onAccepted — identical 100x display bug |
| PLAT-N04 | Medium | ✅65 | ✅78 | ✅90 | ✅75 | ✅90 | ✅65 | AGREE | "ipados" is not valid Qt.platform.os string — 18 dead guards across 5 files |
| PLAT-N05 | Low | ⚠️45 | ⚠️58 | ✅85 | ✅70 | ✅75 | ✅68 | split | Base main.qml fullScreenPlatform missing "wasm" (inconsistent with +windows) |
| WYS-N01 | Medium | ✅60 | ✅78 | ✅90 | ✅75 | ✅85 | ✅60 | AGREE | Internal drag-and-drop copy inserts HTML as plain text — tags become visible |
| WYS-N02 | Low | ✅70 | ⚠️58 | ✅85 | ✅70 | ✅95 | ✅70 | split | Default stylesheet CSS errors: valign:top (not a CSS property) and border:1pt (missing style) |
| QP-N01 | High | ✅65 | ⚠️58 | ✅95 | ✅80 | ✅95 | ✅65 | split | restartApplication() quits even when startDetached fails — app dies with no replacement |
| QP-N02 | Medium | ✅65 | ✅78 | ✅90 | ✅75 | ✅95 | ✅65 | AGREE | convert.waitForFinished() blocks GUI thread up to 30s during LibreOffice import |
| QP-N03 | Medium | ✅55 | ✅78 | ✅90 | ✅75 | ✅90 | ✅55 | AGREE | convert.exitCode() never checked — LibreOffice error output becomes document content |
| IMG-N02 | High | ✅60 | ✅84 | ✅90 | ✅80 | ✅95 | ✅60 | AGREE | insertHtmlAt() silent blocking HTTP load for img src URLs — UI freeze |
| TRN-N01 | Low | ✅55 | ✅78 | ✅90 | ✅70 | ✅95 | ✅55 | AGREE | Dead ternary: both branches return Qt.OpenHandCursor |
| A11Y-SYS | Medium | ⚠️45 | ⚠️58 | ✅85 | ✅70 | ✅90 | ⚠️50 | split | Systemic absence of Accessible properties — app invisible to screen readers |
| EVT-N13 | High | ❔45 | ⚠️58 | ✅95 | ✅75 | ✅90 | ❔45 | split | rewind()/fastForward() event undefined — winding state permanently locked after first use |
| ANM-N02 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅70 | ✅85 | ✅68 | split | Standby→Ready countdown opacity flash — PropertyChanges opacity:1 conflicts with dissolveIn |
| RESO-N01 | Medium | ⚠️45 | ⚠️48 | ✅95 | ✅70 | ✅90 | ✅68 | split | Editing font size not viewport-scaled — text nearly unreadable on 4K |
| RESO-N02 | Low | ⚠️40 | ⚠️48 | ✅80 | ✅65 | ✅80 | ✅68 | split | Scrollbar width 6dp-13dp — below minimum 44dp touch target |
| RESO-N03 | Low | ⚠️40 | ⚠️48 | ✅75 | ⚠️55 | ✅70 | ⚠️50 | split | Control spacing hardcoded 8dp — cramped on large displays |
| RESO-N04 | Low | ⚠️40 | ⚠️48 | ✅75 | ⚠️55 | ✅70 | ⚠️50 | split | Projection-window margins fixed 10dp/5dp — near-flush on large screens |
| RESO-N05 | Low | ⚠️40 | ⚠️48 | ✅75 | ✅65 | ✅70 | ✅68 | split | PointerSettings ListView height hardcoded 180dp — doesn't fill available space |
| RESO-N06 | Low | ⚠️40 | ⚠️48 | ✅80 | ⚠️55 | ✅70 | ✅68 | split | ReadRegionOverlay pointer margin 3dp — overlap with text at large fonts |
| STK-N01 | Critical | ✅85 | ✅92 | ✅95 | ✅80 | ✅95 | ✅85 | AGREE | Android projectionManager undefined — crash on "Performance tweaks" submenu |
| JSON-N01 | High | ✅65 | ✅84 | ✅95 | ✅80 | ✅95 | ✅65 | AGREE | OBS WebSocket Hello auth fields accessed without null guard — crash on auth-disabled |
| QW-N01 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅75 | ✅85 | ✅68 | split | Projection Window onClosing references cleared model — spurious runtime errors |
| QW-N02 | Medium | ⚠️55 | ⚠️58 | ✅85 | ✅75 | ✅85 | ✅68 | split | Stale QScreen reference in projection model — dangling after monitor hot-unplug |
| JS-N01 | Low | ✅50 | ⚠️58 | ✅70 | ✅65 | ✅90 | ✅50 | split | TIMERCLOCK getTimeString() — redundant .toString() on already-string — 54 allocs/sec |
| JS-N02 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅75 | ✅90 | ✅68 | split | markerCompare() per-frame JSON.stringify() over OBS marker — 60 allocs/sec |
| THM-SYS | High | ⚠️55 | ⚠️58 | ✅90 | ✅70 | ✅85 | ✅68 | split | Complete theme deadlock — 50+ Material.theme: Dark hardcoded, theme toggle commented out |
| HSCROLL-N01 | Medium | ⚠️50 | ⚠️58 | ✅95 | ✅70 | ✅90 | ✅68 | split | InputsOverlay Flickables use contentWidth: width instead of implicitWidth — horizontal overflow clipped |
| HSCROLL-N02 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅70 | ✅80 | ✅68 | split | Inner Flickables missing flickableDirection: VerticalFlick — conflict with parent horizontal ListView |
| COLOR-N08 | Medium | ⚠️45 | ⚠️58 | ✅90 | ✅70 | ✅85 | ✅68 | split | textBackground() returns invalid QColor for body/paragraph text |
| COLOR-N09 | Medium | ⚠️55 | ⚠️58 | ✅90 | ✅70 | ✅85 | ✅68 | split | acceptedColor binds transparent QColor on startup — initial text invisible |
| PP-N01 | Medium | ✅55 | ⚠️58 | ✅95 | ✅75 | ✅95 | ✅55 | split | Q_OS_APPLE is not a Qt macro — KGlobalAccel block compiles on all Unix including macOS |
| TRF-N01 | High | ⚠️50 | ⚠️58 | ✅95 | ✅75 | ✅90 | ✅68 | split | rightWidthAdjustmentBar drag.maximumX formula broken — drag collapses to single point |
| TOG-N01 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅70 | ✅80 | ✅68 | split | WheelSettingsOverlay useScrollAsDialButton — cross-path stale checked state |
| RPL-N01 | Medium | ❌55 | ❌76 | ✅95 | ✅70 | ❌90 | ❌55 | **CONFLICT** | 6 additional files missing QtQuick.Controls.Material import — ~65 controls unthemed |
| VIS-FB-N01 | Low | ⚠️50 | ⚠️58 | ✅90 | ✅70 | ✅90 | ✅68 | split | bookmarkListButton and searchButton missing checkable: true — no checked background |
| DEB-N01 | High | ✅55 | ✅84 | ✅95 | ✅75 | ✅90 | ✅55 | AGREE | libvulkan-dev (dev package) listed as Debian runtime dependency |
| DEB-N02 | High | ❔45 | ✅84 | ✅95 | ✅80 | ❌90 | ❔45 | **CONFLICT** | qml6-module-qtcore is not a real Debian package — .deb uninstallable |
| DEB-N03 | High | ❔45 | ✅84 | ✅95 | ✅80 | ❌85 | ❔45 | **CONFLICT** | qml6-module-qt-labs-platform doesn't exist for Qt 6 — .deb uninstallable |
| RPM-N01 | Medium | ✅50 | ⚠️58 | ✅90 | ✅75 | ✅95 | ✅50 | split | RPM dependencies entirely commented out — zero automatic dependency resolution |
| TS-N07 | Medium | ❔40 | ❔39 | ❔40 | ❔50 | ✅95 | ❔40 | split | Wrong translations: Chinese "Undo"→"Open", "Bars"→"Toolbar"; French "Pointer Configuration"→"Prompter duration"; Korean "Line width"→"Line height" |
| META-N14 | Medium | ❔45 | ⚠️58 | ✅80 | ⚠️60 | ❔60 | ❔45 | split | ModernToolkit removed from AppStream spec — validation error |
| META-N15 | Medium | ⚠️45 | ⚠️58 | ✅90 | ✅70 | ✅80 | ✅68 | split | No StartupWMClass in desktop file — duplicate dock entries, missing icon |
| META-N16 | Low | ❔45 | ❔39 | ✅90 | ⚠️60 | ✅95 | ❔45 | split | README badges and links reference wrong repo Cuperino/QPrompt (should be QPrompt-Teleprompter) |
| META-N17 | Medium | ❔45 | ❔39 | ✅85 | ✅70 | ✅95 | ❔45 | split | README links to non-existent BUILD.md |
| AND-N08 | Medium | ✅60 | ✅78 | ✅95 | ✅75 | ✅95 | ✅60 | AGREE | Android saveAs() hardcodes isHtml=true — plain-text files saved with HTML markup |
| TMR-N05 | High | ❔45 | ❔39 | ✅90 | ✅75 | ⚠️70 | ❔45 | split | markerCompare() only fires on forward scroll — backward scroll + re-forward misses marker |
| TMR-N06 | Medium | ⚠️50 | ✅78 | ✅90 | ✅70 | ✅85 | ✅68 | split | Auto-reload Timer persists after network dialog close — background refetches |
| FONT-METRIC-01 | High | ❔40 | ❔39 | ✅90 | ✅75 | ✅75 | ❔40 | split | pixelSize used as line-height proxy — core scroll timing off by ~57% |
| FONT-METRIC-02 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅70 | ✅90 | ✅68 | split | FontLoader status never checked — font substitution silently fails |
| FONT-METRIC-03 | Low | ❔40 | ❔39 | ✅85 | ✅70 | ❌70 | ❌72 | **CONFLICT** | fontFamily() returns resolved-family not requested-family — substitution invisible |
| STC-N01 | Medium | ✅55 | ⚠️58 | ✅90 | ✅70 | ✅90 | ✅55 | split | closeAll() destroys user's per-screen projection flip configuration |
| STC-N02 | Low | ⚠️45 | ⚠️58 | ✅85 | ✅65 | ❌60 | ✅68 | **CONFLICT** | Find.qml close() doesn't reset replace-mode or regex-mode flags |
| STC-N03 | Medium | ❔45 | ⚠️58 | ✅90 | ✅70 | ❌65 | ❔45 | **CONFLICT** | velocityIndicator.firstResetDone never cleared on dismiss — second activation broken |
| STC-N04 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅70 | ✅75 | ✅68 | split | Projection window CursorAutoHide not reset on close — cursor permanently hidden |
| STC-N05 | Low | ⚠️50 | ⚠️58 | ✅85 | ✅65 | ✅80 | ✅68 | split | cancel() doesn't call timer.stopTimer() — elapsed time persists across sessions |
| TB-N01 | Medium | ⚠️45 | ⚠️58 | ✅85 | ✅70 | ✅80 | ✅68 | split | toolbar toggle timers produce stale state on rapid clicks |
| TB-N02 | Medium | ⚠️45 | ⚠️58 | ✅90 | ✅70 | ✅75 | ✅68 | split | baseSpeedSlider/baseAccelerationSlider onMoved yanks focus to prompter instead of restoreFocus() |
| TB-N03 | Low | ⚠️45 | ⚠️58 | ✅70 | ⚠️55 | ✅65 | ⚠️50 | split | Collapsible toolbar rows animate height but adjacent rows snap — no y-position animation |
| TB-N04 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅70 | ❌60 | ✅68 | **CONFLICT** | velocityDragArea accepts MiddleButton without propagateComposedEvents — scroll blocked |
| RESP-N01 | Low | ⚠️50 | ⚠️58 | ✅85 | ✅65 | ✅90 | ⚠️50 | split | minimumHeight: minimumWidth forces square aspect ratio — prevents landscape-strip windows |
| RESP-N02 | Medium | ❔45 | ⚠️58 | ✅90 | ✅70 | ✅85 | ❔45 | split | mobileOrSmallScreen threshold at 1231px activates on default 1220px launch |
| RESP-N03 | Low | ⚠️45 | ⚠️58 | ❌85 | ✅65 | ✅70 | ✅68 | **CONFLICT** | +android/main.qml omits all size declarations — transient zero-size layout on startup |
| QT-LC-N01 | High | ❌70 | ❌76 | ✅95 | ⚠️60 | ❌90 | ❌70 | **CONFLICT** | QQmlFileSelector never instantiated — platform QML file selectors dead |
| TC-N01 | Low | ✅60 | ✅78 | ✅80 | ✅65 | ✅60 | ✅60 | AGREE | Image.source assigned boolean false instead of empty string |
| TC-N02 | Low | ⚠️45 | ⚠️58 | ✅80 | ✅65 | ❌60 | ✅68 | **CONFLICT** | property color value assigned string expression — silent coercion |
| BLK-N01 | Medium | ✅70 | ⚠️58 | ✅85 | ✅70 | ❔55 | ✅70 | split | alignment() returns Qt::AlignCenter (includes vertical bit 0x0080) on null cursor |
| BLK-N02 | Medium | ✅55 | ⚠️58 | ✅90 | ✅70 | ✅80 | ✅55 | split | updateContents() fails to reset block formatting — stale formats contaminate new document |
| BLK-N03 | Medium | ✅60 | ⚠️58 | ✅90 | ✅70 | ✅90 | ✅60 | split | setLineHeight/setParagraphHeight apply document-wide — destroy per-block customization |
| SHT-N01 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅70 | ✅90 | ✅68 | split | markerToggle/namedMarkerToggle forwarded but never handled — dead hotkeys |
| SHT-N02 | Low | ⚠️45 | ⚠️58 | ⚠️75 | ✅65 | ✅75 | ✅68 | split | Missing StandardKey.FullScreen on Android |
| LAZY-N01 | Low | ⚠️45 | ⚠️58 | ✅85 | ✅65 | ✅85 | ✅68 | split | namedMarkerConfiguration Loader double-loads KeyInputButton — first load wasted |
| LAZY-N02 | Medium | ⚠️50 | ⚠️58 | ⚠️60 | ✅70 | ✅80 | ✅68 | split | InputsOverlay ObjectModel eagerly loads both tabs — hidden tab content loaded prematurely |
| LL-N01 | Medium | ⚠️50 | ⚠️58 | ✅80 | ✅65 | ✅75 | ✅68 | split | 10 EditorToolbar MouseArea/TextField width-depends-on-width binding loops |
| LL-N02 | Low | ✅55 | ✅78 | ❌95 | ✅65 | ❌55 | ✅55 | **CONFLICT** | ProgressIndicator stepSize divide-by-zero when prompter.height is 0 |
| SHDR-N02 | Medium | ✅60 | ⚠️58 | ❌85 | ✅65 | ✅85 | ✅60 | **CONFLICT** | id: shadow collides with property ShaderEffectSource shadow — ambiguous resolution in blur chain |
| KB-N01 | Medium | ⚠️45 | ⚠️58 | ✅85 | ✅65 | ❌70 | ✅68 | **CONFLICT** | Find.qml: 9 toolbar buttons missing focusPolicy — keyboard-invisible |
| KB-N02 | Medium | ⚠️55 | ⚠️58 | ✅85 | ✅65 | ❌65 | ✅68 | **CONFLICT** | InputsOverlay TabBar TabButtons have no focusPolicy + keyNavigationEnabled: false — keyboard dead |
| KB-N03 | Medium | ⚠️50 | ⚠️58 | ❌80 | ✅70 | ✅90 | ✅68 | **CONFLICT** | +windows and +android ESC handler uses .focus instead of .activeFocus — wrong boolean |
| DRAG-N01 | Low | ⚠️45 | ⚠️58 | ✅80 | ✅65 | ✅60 | ✅68 | split | Image resize body drag: cursor shows OpenHandCursor until drag threshold exceeded |
| DRAG-N02 | Low | ✅55 | ⚠️58 | ✅80 | ✅65 | ✅70 | ✅55 | split | textDragArea has no cursorShape — no cursor feedback during text drag |
| SHAPE-N01 | Medium | ✅60 | ✅92 | ✅80 | ✅70 | ✅85 | ✅60 | AGREE | pointer_0.qml PathLine parent.width resolves to undefined (ShapePath has no width) — arrow collapsed |
| SHAPE-N02 | Medium | ❔45 | ❔39 | ✅85 | ✅70 | ✅75 | ❔45 | split | concentricCircles Shape uses parent-space coordinates in local space — circles off-center |
| FD-N01 | Medium | ⚠️55 | ⚠️58 | ✅90 | ✅65 | ✅85 | ✅68 | split | \|\| should be && in autoReload guard — user preference ignored for non-binary files |
| TBND-N01 | Medium | ⚠️50 | ⚠️58 | ✅70 | ✅70 | ✅85 | ✅68 | split | SpellHighlighter regex excludes combining diacritical marks — NFD text misspelled |
| TBND-N02 | Medium | ⚠️50 | ⚠️58 | ✅90 | ✅70 | ❌55 | ✅68 | **CONFLICT** | All CJK text marked misspelled — ideographic characters not in Hunspell dictionaries |
| TBND-N03 | Low | ✅55 | ✅78 | ✅80 | ✅65 | ✅90 | ✅55 | AGREE | extendLastMarker() doesn't update Marker::length field — stale after appends |
| MIME-N01 | High | ⚠️45 | ⚠️58 | ❌95 | ⚠️60 | ❌75 | ❌72 | split | Temporary QMimeDatabase — QMimeType dangling on Qt 5 (undefined behavior) |
| MIME-N02 | Medium | ✅65 | ✅78 | ✅90 | ✅70 | ✅90 | ✅65 | AGREE | loadFromNetworkFinihed() ignores Content-Type header — all network content treated as HTML |
| MIME-N03 | Medium | ✅70 | ✅78 | ✅85 | ✅70 | ✅90 | ✅70 | AGREE | PDF/EPUB/MOBI/AZW MIME-detected but import is no-op — error text becomes content |
| TXT-FMT-N01 | Medium | ✅65 | ⚠️58 | ✅80 | ✅70 | ✅90 | ✅65 | split | setMarkerHref("") fails to clear QTextFormat::AnchorHref — stale href persists |
| SCR-N01 | High | ❔45 | ❔39 | ✅90 | ✅70 | ✅90 | ❔45 | split | Per-screen projection flip settings lost on restart — never serialized |
| SCR-N02 | Medium | ✅55 | ✅92 | ✅90 | ✅70 | ✅90 | ✅55 | AGREE | Duplicate entries in displayModel on first toggle — no clear() before setScreensModel() |
| SCR-N03 | Medium | ⚠️50 | ⚠️58 | ✅85 | ✅65 | ✅85 | ✅68 | split | No runtime screen plug/unplug handling — stale projection windows on disconnected screens |
