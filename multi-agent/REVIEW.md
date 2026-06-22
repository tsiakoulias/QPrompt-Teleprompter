# Multi-Agent Bug Review — QPrompt

_723 findings · agents: opus, gpt, deepseek · generated 2026-06-22_

Source of truth is `assessments.csv` (long format, grows by rows). Regenerate with `python build_review.py`. Full per-row rationales for unanimous findings live in `assessments.csv`; this file details only the rows where agents disagree.

## Summary

| Agent | FALSE | LEGIT | PARTIAL | UNSURE |
|---|---|---|---|---|
| opus | 49 | 288 | 319 | 67 |
| gpt | 44 | 333 | 299 | 47 |
| deepseek | 39 | 597 | 51 | 36 |

**Consensus** (3 agents): AGREE 250 · split 437 · CONFLICT 36

**Status:** OPEN 723

Legend: ✅ LEGIT · ❌ FALSE · ⚠️ PARTIAL · ❔ UNSURE · · = not assessed. Number = confidence.

## Matrix

| ID | Sev | opus | gpt | deepseek | Consensus | St | Title |
|---|---|---|---|---|---|---|---|
| MEM-01 | High | ✅100 | ✅88 | ✅90 | AGREE | · | Memory Leak: `_markersModel` allocated without parent, never deleted |
| MEM-02 | High | ✅100 | ✅88 | ✅90 | AGREE | · | Memory Leak: `_fileSystemWatcher` allocated without parent, never deleted |
| MEM-03 | Medium | ✅100 | ✅88 | ✅85 | AGREE | · | Memory Leak: `m_fontDialog` allocated without parent, never deleted |
| LOG-01 | High | ✅100 | ✅92 | ✅95 | AGREE | · | SessionModel::rowCount returns m_data.size() for both valid and invalid parents |
| LOG-02 | High | ✅95 | ✅92 | ✅95 | AGREE | · | Off-by-one: beginRemoveRows uses rowCount() instead of rowCount()-1 |
| LOG-03 | Medium | ✅100 | ✅78 | ✅98 | AGREE | · | MarkersModel::data returns data.position for LengthRole instead of data.length |
| LOG-04 | Medium | ✅100 | ✅78 | ⚠️60 | split | · | MarkersModel::extendLastMarker modifies data without emitting dataChanged |
| LOG-05 | Medium | ✅100 | ✅78 | ✅88 | AGREE | · | DocumentHandler::search ignores `loop` parameter when `regEx` is true |
| LOG-06 | Medium | ✅90 | ✅78 | ⚠️70 | split | · | DocumentHandler::replaceAll has potential infinite loop with regex |
| LOG-07 | Low | ⚠️60 | ⚠️52 | ⚠️50 | AGREE | · | namedMarker() fetches cursor twice — stale-content risk |
| LOG-08 | Low | ✅100 | ✅88 | ✅85 | AGREE | · | DataPoint default constructor leaves three members uninitialized |
| LOG-09 | Low | ❌95 | ❌76 | ❌80 | AGREE | · | Trailing comma in constructor member initializer list (non-standard C++ before C++20) |
| QML-01 | Critical | ❌90 | ❌90 | ❔30 | split | · | 26 references to undefined `pointerSettings` ID in ReadRegionOverlay |
| QML-02 | Critical | ❌90 | ❌90 | ❔30 | split | · | Undefined `pointerConfiguration` ID reference in ReadRegionOverlay |
| QML-03 | Critical | ✅95 | ✅92 | ✅75 | AGREE | · | Undefined `root` ID in WindowDragger.qml |
| QML-04 | High | ✅100 | ✅92 | ✅90 | AGREE | · | Typo: `verticalCentertop` instead of `verticalCenter` |
| QML-05 | High | ✅100 | ✅84 | ✅95 | AGREE | · | `&&` should be `\|\|` in clear button enabled condition |
| QML-06 | High | ✅100 | ✅84 | ✅90 | AGREE | · | Bitwise OR (`\|`) instead of AND (`&`) in modifier key check |
| QML-07 | High | ❌95 | ❌90 | ❌85 | AGREE | · | `Text.CurveRendering` enum requires Qt >= 6.7 |
| QML-08 | Medium | ❌80 | ❌76 | ❔40 | split | · | Invalid anchor target `undefined` |
| QML-09 | Medium | ❌95 | ❌90 | ❌85 | AGREE | · | `QtQuick.Shapes 6.6` version mismatch with `QtCore 6.5` |
| QML-10 | Medium | ❌85 | ❌76 | ❔45 | split | · | `+android/main.qml` missing `QmlUtil` for RecentDocuments |
| QML-11 | Medium | ✅90 | ⚠️58 | ✅85 | split | · | Dead code: `window` property declared but never used in WindowDragger |
| SEC-01 | Critical | ✅95 | ✅84 | ✅75 | AGREE | · | Arbitrary Command Execution via `sys://` Marker URIs |
| SEC-02 | Medium | ✅85 | ✅78 | ✅90 | AGREE | · | OBS WebSocket Password Stored in Plaintext |
| SEC-03 | Medium | ✅95 | ✅78 | ✅80 | AGREE | · | Information Disclosure: Full HTML Document Content Logged via qDebug |
| SEC-04 | High | ⚠️55 | ⚠️58 | ✅85 | split | · | SSRF / URL Injection — User-Controlled URL Passed to Network Loader |
| SEC-05 | Medium | ⚠️55 | ⚠️58 | ✅70 | split | · | User-Controlled Filename Passed to QProcess (LibreOffice import) |
| RES-01 | High | ✅95 | ✅84 | ✅90 | AGREE | · | Network reply overwritten without aborting previous download |
| RES-02 | High | ✅95 | ✅84 | ✅92 | AGREE | · | loadFromNetworkFinihed ignores the QNetworkReply* signal parameter |
| RES-03 | Low | ⚠️65 | ⚠️58 | ✅85 | split | · | ShakeDetector::s_instance never set to nullptr on destruction (dangling pointer) |
| RES-04 | Low | ⚠️65 | ⚠️58 | ✅85 | split | · | IosSaveDialog::s_instance same singleton dangling pattern |
| RES-05 | Low | ❌80 | ❌76 | ❌75 | AGREE | · | QTextStream left unflushed before QFile destruction |
| TYP-01 | High | ❌80 | ❔39 | ✅95 | **CONFLICT** | · | Dangling pointer from temporary std::string in SpellChecker::loadOne |
| TYP-02 | Medium | ❌90 | ❌76 | ✅90 | **CONFLICT** | · | Invalid Qt::LayoutDirection enum value cast |
| TYP-03 | Medium | ⚠️60 | ⚠️58 | ✅85 | split | · | Floating-point equality comparison of window opacity |
| TYP-04 | Medium | ✅95 | ⚠️58 | ✅90 | split | · | Bitwise AND on bools hides dead code in preventSleep |
| TYP-05 | Medium | ✅95 | ✅88 | ⚠️60 | split | · | Uninitialized pointer member m_reply in DocumentHandler |
| TYP-06 | Low | ✅95 | ⚠️58 | ✅85 | split | · | Malformed preprocessor macro: `#define Use_GlobalAccel = 1` |
| TYP-07 | Low | ✅90 | ⚠️58 | ⚠️30 | split | · | Narrowing conversion: `size_t` → `int` in SpellChecker::decode |
| TYP-08 | Low | ❌95 | ❌76 | ❌80 | AGREE | · | DocumentHandler constructor trailing comma in initializer list |
| TYP-09 | Low | ❌90 | ❌76 | ⚠️40 | split | · | Null pointer dereferences in emit textChanged related to uninitialized m_document |
| TYP-10 | Low | ❌55 | ❌76 | ❌60 | AGREE | · | Uninitialized marker struct fields: length defaults to 1 |
| EDGE-01 | High | ✅95 | ✅84 | ✅95 | AGREE | · | QString::arg() called on string with no placeholder — program name silently dropped |
| EDGE-02 | High | ✅95 | ✅84 | ✅90 | AGREE | · | Empty container `first()` dereference — crash on hotkey with no windows |
| EDGE-03 | High | ✅90 | ✅84 | ✅85 | AGREE | · | Empty container `last()` dereference in `extendLastMarker` |
| EDGE-04 | Critical | ✅90 | ✅88 | ✅92 | AGREE | · | Null pointer dereference: `document()->textDocument()` not checked before `load()` |
| EDGE-05 | Critical | ✅90 | ✅88 | ✅92 | AGREE | · | Null pointer dereference: `textDocument()` unchecked in `search()` |
| EDGE-06 | Critical | ✅90 | ✅88 | ✅92 | AGREE | · | Null pointer dereference: `textDocument()` unchecked in `parse()` |
| EDGE-07 | High | ⚠️60 | ⚠️58 | ✅85 | split | · | Q_UNREACHABLE in Q_INVOKABLE method — UB if called from QML |
| EDGE-08 | Medium | ❌80 | ❌76 | ✅75 | **CONFLICT** | · | Q_ASSERT as thread-safety guard — removed in release builds |
| EDGE-09 | Medium | ✅90 | ✅88 | ✅85 | AGREE | · | QFile::copy() return value silently ignored |
| EDGE-10 | Low | ❌85 | ⚠️58 | ⚠️50 | split | · | globalShortcutKey() switch without default — fallthrough to Q_UNREACHABLE |
| EDGE-11 | Medium | ⚠️60 | ⚠️58 | ✅85 | split | · | m_reply dereference without null check in loadFromNetworkFinihed() |
| EDGE-12 | Low | ⚠️40 | ⚠️58 | ❌40 | split | · | QTextBlock::iterator scope fragility in parse() |
| PLAT-01 | High | ✅90 | ⚠️58 | ✅90 | split | · | KF6Crash_FOUND never defined as C preprocessor macro — KCrash support dead code |
| PLAT-02 | Medium | ✅90 | ✅78 | ✅85 | AGREE | · | REQUIRED_KF6_VERSION variable referenced but never defined |
| PLAT-03 | High | ✅85 | ✅84 | ❔50 | split | · | Wrong target name and wrong include path for KDMacTouchBar |
| PLAT-04 | Medium | ❌95 | ❌90 | ❔40 | split | · | DS_Store.scpt referenced but file does not exist |
| PLAT-05 | Medium | ✅85 | ✅92 | ✅85 | AGREE | · | DBINARY_ICONS_RESOURCE is a typo — should be BINARY_ICONS_RESOURCE |
| PLAT-06 | Low | ✅90 | ✅78 | ✅80 | AGREE | · | qprompt_QM_LOADER variable never defined |
| PLAT-07 | Low | ✅95 | ⚠️58 | ✅85 | split | · | Incorrect macro syntax: `#define Use_GlobalAccel = 1` |
| PLAT-08 | Medium | ⚠️50 | ⚠️58 | ✅85 | split | · | QNX platform guard inconsistency: main.cpp vs documenthandler.h |
| PLAT-09 | Low | ❔45 | ❔39 | ❔30 | AGREE | · | Pre-build manifest references invalid Android SDK paths |
| R2-GH-01 | High | ❌80 | ❌76 | ✅80 | **CONFLICT** | · | Q_UNREACHABLE reachable when only QHotkey available on Wayland |
| R2-CMAKE-01 | Critical | ❌80 | ❌76 | ✅90 | **CONFLICT** | · | sphinx_add_docs silently ignores all keyword arguments due to empty cmake_parse_arguments prefix |
| R2-CMAKE-02 | High | ✅80 | ✅84 | ✅90 | AGREE | · | cmake_minimum_required inside find module pollutes parent project policy settings |
| R2-CMAKE-03 | Medium | ✅80 | ✅78 | ✅85 | AGREE | · | WORKING_DIRECTORY and COMMENT not parseable by callers of sphinx_add_docs |
| R2-CMAKE-04 | Medium | ✅80 | ✅78 | ✅80 | AGREE | · | QML icon file(GLOB_RECURSE) missing CONFIGURE_DEPENDS causes stale icon sets |
| R2-PRP-01 | Medium | ✅80 | ✅78 | ❔45 | split | · | Qt.LeftToRight used as bare boolean — RTL branch always dead |
| R2-PRP-02 | Medium | ✅85 | ✅92 | ❔40 | split | · | Kirigami.Units.SmallSpacing — uppercase S yields undefined |
| R2-PRP-03 | Medium | ❌75 | ⚠️58 | ❔40 | split | · | Units.LongDuration / Units.HumanMoment missing Kirigami. prefix |
| R2-PRP-04 | Low | ⚠️50 | ⚠️58 | ❔35 | split | · | Inconsistent focus restoration in decreaseVelocityButton |
| R2-PRP-05 | Low | ⚠️45 | ⚠️52 | ❔30 | split | · | Potential null-item access on async Loader in namedMarkerConfiguration.onOpened |
| R2-PTR-01 | Medium | ❌75 | ❌76 | ✅80 | **CONFLICT** | · | Type mismatch: textVerticalOffset declared int but fed a real |
| R2-PTR-02 | Medium | ❌75 | ❌76 | ✅80 | **CONFLICT** | · | Type mismatch: imageVerticalOffset declared int but fed a real |
| R2-PTR-03 | Medium | ✅80 | ✅78 | ❔40 | split | · | Casing error: Units.longDuration should be Units.LongDuration |
| R2-PTR-04 | Medium | ✅85 | ✅78 | ❔35 | split | · | Inverted indexOf truthiness in platform check for ColorDialog |
| R2-AND-01 | Critical | ✅90 | ⚠️58 | ❔35 | split | · | Android missing QmlUtil causes crash on factory reset and RecentDocuments |
| R2-AND-02 | Critical | ✅90 | ✅84 | ❔35 | split | · | Android missing restartDialog crashes LanguageSettingsOverlay and LayoutDirectionSettingsOverlay |
| R2-AND-03 | Medium | ✅80 | ✅78 | ❔35 | split | · | Android Settings missing fakeFullScreen persistence |
| R2-AND-04 | Low | ⚠️45 | ⚠️58 | ❔30 | split | · | Android Settings for "background" missing transparency persistence |
| R2-AND-05 | Low | ⚠️45 | ⚠️58 | ❔25 | split | · | Android loadTelemetryPage passes no properties object to pageStack push |
| R2-OVL-01 | Medium | ⚠️65 | ⚠️58 | ❔35 | split | · | InputsOverlay onOpened calls cursorAutoHide.restart() instead of reset() |
| R2-OVL-02 | Low | ✅85 | ✅78 | ❔35 | split | · | LanguageSettingsOverlay popup ListView currentIndex always resolves to -1 |
| R2-PTH-01 | Medium | ✅85 | ✅78 | ✅80 | AGREE | · | FileDialog filter matches all files on Linux due to stray glob |
| R2-PTH-02 | Medium | ✅85 | ✅78 | ✅80 | AGREE | · | File path from file:// URL preserves percent-encoding |
| R2-WHE-01 | High | ✅90 | ✅84 | ✅85 | AGREE | · | `focus: true` is JavaScript label, not assignment |
| R2-EDT-01 | Medium | ✅90 | ✅92 | ❔40 | split | · | Qt.AlignHustify typo — nonexistent enum value |
| R2-EDT-02 | High | ✅85 | ✅84 | ❔35 | split | · | wheelThrottleSettingsButton checked bound to completely unrelated document property |
| R2-EDT-03 | High | ✅80 | ✅84 | ⚠️55 | split | · | Checkable ToolButtons break checked property bindings on first click — systematic |
| R2-TEL-01 | Medium | ✅80 | ✅78 | ❔35 | split | · | Telemetry sub-toggles permanently disconnect from master toggle on click |
| R2-REC-01 | Low | ✅85 | ✅92 | ⚠️60 | split | · | File URI prefix strip off-by-one on Windows |
| R2-REC-02 | Medium | ⚠️50 | ⚠️58 | ❔30 | split | · | refreshExistence skips UI updates when dynamic children out of sync |
| R2-IOS-01 | High | ✅80 | ✅84 | ❔40 | split | · | Method swizzling re-entry causes infinite recursion on second invocation |
| R2-IOS-02 | Medium | ⚠️50 | ❔39 | ❔40 | split | · | Delegate block captures raw assign pointer — use-after-free risk |
| R2-IOS-03 | Medium | ✅85 | ✅78 | ✅75 | AGREE | · | UIApplication.keyWindow deprecated since iOS 13; breaks multi-window iPadOS |
| R2-WASM-01 | Medium | ✅85 | ✅78 | ❔35 | split | · | File input element never removed from DOM on user cancel |
| R2-WASM-02 | Medium | ✅85 | ✅78 | ❔35 | split | · | Insecure hostname validation via endsWith allows subdomain spoofing |
| R2-FONT-01 | Medium | ✅85 | ✅78 | ✅75 | AGREE | · | RichText label renders unescaped plain text — HTML metacharacters break display |
| R2-FONT-02 | Low | ✅85 | ✅92 | ✅95 | AGREE | · | Duplicate setText call on preview label |
| R2-ANDMAN-01 | Medium | ✅85 | ✅78 | ✅90 | AGREE | · | Ungrantable system/signature permissions bloating manifest |
| R2-ANDMAN-02 | Medium | ✅85 | ✅78 | ✅90 | AGREE | · | MANAGE_EXTERNAL_STORAGE likely triggers Play Store scrutiny |
| R3-CTX-01 | Critical | ✅90 | ✅92 | ✅95 | AGREE | · | AbstractUnits missing QML_ELEMENT — all duration constants resolve to undefined |
| R3-CTX-02 | High | ✅90 | ✅84 | ✅98 | AGREE | · | GlobalHotkeys.SkipForward enum value mismatch — trailing 's' missing |
| R3-DOC-01 | Critical | ✅90 | ✅92 | ✅85 | AGREE | · | m_reloading uninitialized — undefined behavior on first load |
| R3-DOC-02 | Critical | ❌85 | ❌76 | ✅90 | **CONFLICT** | · | Unbalanced edit block in setLineHeight/setParagraphHeight |
| R3-DOC-03 | High | ✅85 | ✅84 | ✅90 | AGREE | · | load() sets m_fileUrl and emits fileUrlChanged even on failed load |
| R3-DOC-04 | High | ✅90 | ✅84 | ✅95 | AGREE | · | saveAs() silently ignores write/flush failures |
| R3-DOC-05 | High | ✅85 | ✅84 | ✅90 | AGREE | · | updateContents() produces two separate undo entries — undo destroys document |
| R3-DOC-06 | Medium | ✅90 | ✅78 | ✅85 | AGREE | · | reload() leaks m_reloading=true on URL mismatch |
| R3-DOC-07 | High | ✅85 | ✅84 | ✅90 | AGREE | · | Inverted selection state after failed search() |
| R3-SPL-01 | Medium | ✅70 | ✅78 | ✅80 | AGREE | · | encode() uses toLocal8Bit() instead of dictionary-encoding-aware conversion |
| R3-SPL-02 | Medium | ✅70 | ✅78 | ✅80 | AGREE | · | decode() uses fromLocal8Bit() — suggestions show as mojibake |
| R3-SPL-03 | Medium | ❌80 | ❌76 | ✅90 | **CONFLICT** | · | removeCustomWord() silently discards all addWord() additions |
| R3-SPL-04 | Medium | ✅75 | ✅78 | ✅90 | AGREE | · | Corrupt cached dictionary file persists permanently after failed copy |
| R3-SPL-05 | Medium | ⚠️45 | ⚠️58 | ✅85 | split | · | SpellChecker has zero thread safety — all methods unprotected |
| R3-MAIN-01 | Medium | ❌75 | ✅78 | ✅85 | **CONFLICT** | · | Command-line positional argument description/syntax swapped |
| R3-MAIN-02 | High | ⚠️55 | ⚠️58 | ✅90 | split | · | Invalid locale string constructed for short language codes |
| R3-MAIN-03 | Medium | ✅85 | ✅78 | ✅95 | AGREE | · | System locale changed even when translation file fails to load |
| R3-MAIN-04 | Low | ❌85 | ❌76 | ⚠️60 | split | · | Stack-allocated QTranslator outlives QApplication on shutdown |
| R3-MAIN-05 | Medium | ✅80 | ⚠️58 | ✅98 | split | · | Hardcoded Homebrew version-specific Kirigami import path |
| R3-MAIN-06 | High | ✅90 | ✅84 | ✅90 | AGREE | · | Inconsistent Kirigami platform guards — missing WATCHOS and QNX |
| R3-MAIN-07 | Medium | ✅90 | ✅78 | ✅98 | AGREE | · | XDG_CURRENT_DESKTOP unconditionally forced to "KDE" on all Linux |
| R3-MAIN-08 | Low | ✅55 | ✅78 | ✅80 | AGREE | · | QFontDatabase::addApplicationFont return value discarded |
| R3-APP-01 | Low | ❌75 | ❌76 | ❌85 | AGREE | · | AppController singleton and children never deallocated |
| R3-PROP-01 | Medium | ✅80 | ✅78 | ✅80 | AGREE | · | selectionIsLowerCase bound to wrong NOTIFY signal |
| R3-SIG-01 | Low | ✅85 | ✅78 | ✅90 | AGREE | · | textChanged() signal declared but never emitted |
| R3-SIG-02 | Medium | ❌85 | ❌90 | ⚠️85 | split | · | ShakeDetector signals declared but never emitted — dead feature |
| R3-SIG-03 | Medium | ❌90 | ❌90 | ✅75 | **CONFLICT** | · | IosSaveDialog accepted/rejected signals declared but never emitted |
| R3-PMT-01 | High | ⚠️60 | ⚠️58 | ✅95 | split | · | OBS WebSocket JSON.parse without try/catch — crash on malformed input |
| R3-PMT-02 | Medium | ✅60 | ✅78 | ✅90 | AGREE | · | OBS WebSocket no onError handler, no reconnection logic |
| R3-PMT-03 | Medium | ⚠️50 | ⚠️58 | ✅85 | split | · | goToNextMarker fallback desynchronizes cursor from viewport |
| R3-TMR-01 | Medium | ❔45 | ❔39 | ✅80 | split | · | TimerClock ETA uses __iDefault instead of actual __i during reverse scroll |
| R4-QTV-01 | Critical | ❌90 | ❌76 | ✅95 | **CONFLICT** | · | QtQuick 2.13 import does not exist in Qt 6.5 |
| R4-QTV-02 | Critical | ❌90 | ❌76 | ❔60 | split | · | QtQuick.Window 2.0 import does not exist in Qt 6.5 |
| R4-QTV-03 | High | ❌90 | ❌76 | ❌98 | AGREE | · | QtQuick.Dialogs 6.6 imported in 9 files on Qt 6.5 target |
| R4-EXP-01 | Critical | ⚠️55 | ⚠️58 | ✅95 | split | · | No XSS sanitization — script tags, event handlers, javascript: URLs unfiltered |
| R4-EXP-02 | High | ✅90 | ✅84 | ✅95 | AGREE | · | insertHtmlAt() bypasses filterHtml() — unsanitized HTML from QML |
| R4-EXP-03 | High | ✅85 | ✅84 | ✅90 | AGREE | · | loadFromNetwork() destroys URL for relative URLs — host/path swapped |
| R4-EXP-04 | High | ✅80 | ✅84 | ✅90 | AGREE | · | AutoText inserts plain text as HTML — content corruption |
| R4-EXP-05 | Medium | ✅70 | ✅78 | ✅90 | AGREE | · | No encoding/charset detection — all imports assumed UTF-8 |
| R4-EXP-06 | Medium | ✅70 | ✅78 | ✅95 | AGREE | · | UTF-8 BOM not stripped — becomes phantom character at position 0 |
| R4-EXP-07 | Medium | ✅60 | ✅78 | ✅90 | AGREE | · | data: URI assumes base64 encoding without checking ;base64 token |
| R4-EXP-08 | Medium | ✅85 | ✅78 | ✅90 | AGREE | · | EPUB/MOBI/AZW import replaces document with error string |
| R4-EXP-09 | Low | ⚠️55 | ⚠️58 | ✅85 | split | · | LibreOffice import --cat and --convert-to flags are contradictory |
| R4-ROOT-01 | High | ✅90 | ✅84 | ✅95 | AGREE | · | Qt.openUrlExternally called with translation context string instead of URL |
| R4-ROOT-02 | Medium | ✅85 | ✅92 | ✅95 | AGREE | · | Invalid QML color value "initial" |
| R4-ROOT-03 | Medium | ❌80 | ❌76 | ✅90 | **CONFLICT** | · | ESC global shortcut skips single-layer pages — can't dismiss with keyboard |
| R4-ROOT-04 | Medium | ✅90 | ✅92 | ✅98 | AGREE | · | Duplicate "&Open" menu item in native File menu |
| R4-ROOT-05 | Low | ⚠️50 | ✅92 | ✅95 | split | · | loadRemoteControlPage/loadTelemetryPage reference undefined component IDs |
| R4-EVT-01 | Critical | ❌85 | ❌76 | ✅95 | **CONFLICT** | · | Missing braces on if/else — syntax error in alignRightButton |
| R4-EVT-02 | Medium | ✅90 | ⚠️58 | ✅95 | split | · | Velocity modifier ComboBox lists 2 options but switch handles 4 — dead code |
| R4-EVT-03 | High | ⚠️60 | ✅84 | ✅85 | split | · | CursorAutoHide null access on root.pageStack.currentItem during page transitions |
| R4-CMT-01 | Critical | ✅90 | ✅84 | ✅98 | AGREE | · | PDF import completely broken — converter invocation commented out |
| R4-PRJ-01 | High | ❌80 | ❌76 | ❌85 | AGREE | · | flip variable spuriously reset in project() inner loop else-branch |
| R4-PRJ-02 | High | ❔45 | ❔39 | ✅95 | split | · | displayModel.get().flipSetting writes to snapshot copy — never mutates model |
| R4-PRJ-03 | Medium | ✅55 | ✅92 | ✅90 | AGREE | · | setScreensModel() duplicates display entries on each toggle cycle |
| R4-PRJ-04 | Medium | ✅55 | ✅78 | ✅85 | AGREE | · | Division by zero in projection image height |
| R4-ROV-01 | High | ⚠️60 | ⚠️58 | ✅90 | split | · | Division by zero in __customPlacement when overlay full |
| R4-ROV-02 | High | ⚠️65 | ⚠️58 | ✅90 | split | · | Drag permanently breaks y property binding on readRegion |
| R4-ROV-03 | Medium | ✅90 | ✅78 | ✅95 | AGREE | · | Bitwise OR \| used for width fallback instead of logical OR |
| R4-BKG-01 | Medium | ✅85 | ✅78 | ✅85 | AGREE | · | Flip transform origin stays at (0,0) when Flip stored as property |
| R4-SHD-01 | Medium | ❌80 | ❌76 | ✅90 | **CONFLICT** | · | Duplicate class implementation between .cpp and .mm — ODR risk |
| R4-IOSCPP-01 | Low | ⚠️50 | ⚠️58 | ✅90 | split | · | QTemporaryDir created on all platforms including non-iOS where unused |
| R4-SIG-ADD-01 | Low | ⚠️45 | ⚠️58 | ⚠️60 | AGREE | · | SessionModel::appendDataPoint declared public slot but never connected |
| FINAL-01 | Critical | ✅90 | ✅92 | ✅98 | AGREE | · | TimerClock references undefined `timer` id — ETA and stopwatch completely broken |
| FINAL-02 | Critical | ❌85 | ❌90 | ❌90 | AGREE | · | Missing `QtQuick.Controls.Material` import — 3 Material references unresolved |
| FINAL-03 | Critical | ✅95 | ✅84 | ✅98 | AGREE | · | Missing breeze-icons submodule — fresh clone cannot build |
| FINAL-04 | High | ⚠️50 | ⚠️58 | ⚠️60 | AGREE | · | NSIS start-menu shortcut icon name mismatches actual binary name |
| FINAL-05 | High | ✅90 | ✅84 | ✅95 | AGREE | · | WindowDragger mouse delta accumulation error — window moves farther than cursor |
| FINAL-06 | High | ✅90 | ⚠️58 | ❌95 | **CONFLICT** | · | CMAKE_OSX_ARCHITECTURES contains literal quotes — universal binary broken |
| FINAL-07 | High | ❌80 | ❌76 | ❌98 | AGREE | · | CMake wrong variable name: InstallRequiredSystemLibraries instead of CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS |
| FINAL-08 | High | ✅85 | ✅84 | ✅95 | AGREE | · | setup.sh vcvarsall.bat executed from bash — MSVC env not propagated |
| FINAL-09 | Medium | ✅85 | ✅92 | ✅90 | AGREE | · | `on__IChanged` handler typo — never fires |
| FINAL-10 | High | ⚠️55 | ⚠️58 | ✅90 | split | · | Two animations target same `position` property — conflict |
| FINAL-11 | High | ✅85 | ✅84 | ✅95 | AGREE | · | onFrameSwapped calls grabToImage every frame — severe performance hit |
| FINAL-12 | Medium | ✅80 | ✅78 | ✅95 | AGREE | · | SystemFontChooserDialog setWindowFlags strips all decorations |
| FINAL-13 | Medium | ✅90 | ✅92 | ✅95 | AGREE | · | Invalid Korean locale code "ko_KO" — should be "ko_KR" |
| FINAL-14 | Medium | ⚠️55 | ⚠️58 | ✅98 | split | · | Wrong placeholder `%0` instead of `%1` — font name never displayed |
| FINAL-15 | High | ⚠️55 | ⚠️58 | ✅90 | split | · | Missing edit block wrapping in setLineHeight/setParagraphHeight |
| FINAL-16 | Critical | ❔50 | ⚠️58 | ✅80 | split | · | Countdown completion uses state++ bypassing toggle() entry actions |
| FINAL-17 | Medium | ✅85 | ✅78 | ✅90 | AGREE | · | ScriptAction references non-existent function `paintReady` |
| FINAL-18 | Medium | ✅100 | ✅78 | ✅95 | AGREE | · | MarkersModel extendLastMarker modifies data without emitting dataChanged |
| FINAL-19 | Medium | ✅70 | ✅78 | ✅85 | AGREE | · | Encoding fallback uses toLocal8Bit() instead of dictionary's actual encoding |
| FINAL-20 | High | ❌80 | ❌76 | ❌90 | AGREE | · | Dangling pointer from temporary QByteArray in marker anchor parsing |
| FINAL-21 | Medium | ✅75 | ✅78 | ✅70 | AGREE | · | clearProperty(AnchorHref/AnchorName) ineffective through mergeCharFormat |
| FINAL-22 | High | ⚠️50 | ⚠️58 | ✅85 | split | · | Behavior.onRunningChanged calls toggle() from within animation handler — re-entrant state change |
| CUR-N01 | Critical | ✅90 | ✅84 | ✅95 | AGREE | · | replaceAll() infinite loop when replacement contains search pattern |
| CUR-N02 | High | ✅95 | ✅84 | ✅98 | AGREE | · | search() regex path ignores loop parameter — unconditional wrap |
| CUR-N03 | Medium | ✅70 | ✅78 | ✅80 | AGREE | · | alignment() reads blockFormat on multi-block selection — returns wrong alignment |
| DCL-N01 | Medium | ✅55 | ✅78 | ✅95 | AGREE | · | filterHtml default parameter in .cpp but not in header — QML can't call with 1 arg |
| DCL-N02 | Medium | ✅55 | ✅78 | ✅95 | AGREE | · | setKeyMarker default parameter mismatch — same pattern |
| IMP-N01 | Critical | ❌60 | ❌76 | ⚠️75 | split | · | import Qt.labs.platform 1.1 — Menu/MenuBar/MenuItem dropped in Qt 6 |
| IMP-N02 | Critical | ❌65 | ❌76 | ✅80 | **CONFLICT** | · | import QtWebSockets 1.10 — wrong version for Qt 6.5 |
| MATH-N01 | High | ✅65 | ✅84 | ✅95 | AGREE | · | Division by zero in __timeToArival/__timeToEnd when speed=0 |
| MATH-N02 | Medium | ✅60 | ✅78 | ✅90 | AGREE | · | Bitwise << on floating-point in TimerClock — precision loss |
| LYR-N01 | High | ⚠️60 | ✅84 | ✅85 | split | · | InputsOverlay calls cursorAutoHide.restart() on open instead of reset() |
| LYR-N02 | Medium | ⚠️50 | ✅78 | ✅75 | split | · | Three OverlaySheets missing from ESC dismiss chain |
| LYR-N03 | Medium | ❔45 | ✅78 | ✅88 | split | · | ContextDrawer exposes prompter actions while viewing layer pages |
| LYR-N04 | Medium | ⚠️50 | ✅78 | ✅85 | split | · | ESC handler uses activeFocus in base but focus in platform variants — inconsistent |
| TRL-N01 | High | ⚠️55 | ✅84 | ✅95 | split | · | qsTr() uses %0 placeholder — should be %1 (font name never displayed) |
| TRL-N02 | Medium | ✅50 | ✅78 | ✅90 | AGREE | · | Application --help description not translatable |
| TRL-N03 | Medium | ⚠️45 | ✅78 | ✅90 | split | · | About-dialog credit roles not translatable |
| W10-HTK-01 | Critical | ❌70 | ❌76 | ✅92 | **CONFLICT** | · | autoRepeat=true for ALL QHotkey shortcuts — non-velocity actions broken when held |
| W10-HTK-02 | High | ✅65 | ✅88 | ✅88 | AGREE | · | QHotkey::setShortcut return value silently ignored — no failure detection |
| W10-PMV-01 | High | ⚠️50 | ⚠️58 | ⚠️70 | AGREE | · | font.pixelSize evaluates to 0 before first layout pass — crash hazard |
| W10-PMV-02 | Medium | ⚠️50 | ⚠️58 | ✅80 | split | · | Circular ShaderEffectSource dependency — shadow ghost on first frame |
| W10-CLP-01 | High | ⚠️55 | ⚠️58 | ❌80 | split | · | Paste-without-formatting fails when clipboard lacks text/plain |
| W10-CLP-02 | Medium | ⚠️50 | ⚠️58 | ✅90 | split | · | Remote image URLs in pasted HTML cause unsanctioned network requests |
| W10-CNV2-01 | High | ✅80 | ✅92 | ✅90 | AGREE | · | Default stylesheet has invalid CSS color quoting — exported HTML broken in browsers |
| W10-CNV2-02 | High | ✅55 | ✅84 | ✅92 | AGREE | · | No markdown export — round-trip silently destroys all formatting |
| W10-CNV2-03 | High | ⚠️45 | ⚠️58 | ⚠️65 | AGREE | · | import() uses fromStdString on non-Windows — encoding corruption |
| W10-SWT-01 | High | ⚠️55 | ⚠️58 | ✅90 | split | · | CloseActions switch drops RecentLocal/RecentRemote — recent document open silently lost after save |
| W10-SWT-02 | High | ⚠️55 | ⚠️58 | ✅90 | split | · | Same bug in IosSaveDialog.onAccepted path |
| W10-DEP-01 | Critical | ✅75 | ✅92 | ✅92 | AGREE | · | Missing vcpkg.json manifest — vcpkg manifest mode installs nothing |
| W10-WSM-01 | Critical | ⚠️55 | ⚠️58 | ✅88 | split | · | Infinite reload loop on unauthorized WASM host — app unusable |
| W10-WSM-02 | Medium | ⚠️50 | ⚠️58 | ✅88 | split | · | Global file-picker state overwritten by re-entrant calls — wrong file delivered |
| W10-PLF-01 | Critical | ✅70 | ✅84 | ✅95 | AGREE | · | BSD detection broken — FreeBSD enters wrong code paths |
| W10-PLF-02 | High | ⚠️50 | ⚠️58 | ✅95 | split | · | QHotkey_FOUND never set in FetchContent path — built but never linked |
| TS-01 |  | ❔40 | ⚠️58 | ✅88 | split | · | Finnish welcome guide → Dutch (not Finnish) |
| TS-02 |  | ⚠️50 | ⚠️58 | ✅90 | split | · | Arabic file `ar_EG` vs UI `ar_AE` mismatch |
| TS-03 |  | ✅90 | ✅78 | ✅90 | AGREE | · | Korean UI `ko_KO` vs file `ko_KR` mismatch |
| TS-04 |  | ❔40 | ❔39 | ✅85 | split | · | French "Saved" → verb "Enregistrer" (should be adjective "Enregistré") |
| TS-05 |  | ⚠️45 | ⚠️58 | ✅85 | split | · | Finnish/French/Korean/Italian "Saved" → verb with stray `&amp;` accelerator |
| TS-06 |  | ❔40 | ❔39 | ✅90 | split | · | Czech/French "Language settings" → "Pointer settings" (copy-paste error) |
| TS-07 |  | ❔40 | ❔39 | ✅85 | split | · | Finnish/French/Korean "Colors for prompter states" → "Toggle Prompter State" |
| TS-08 |  | ❔40 | ❔39 | ✅85 | split | · | French "Prompting:" → "Start prompter" |
| TS-09 |  | ❔40 | ❔39 | ✅85 | split | · | Finnish/French/Korean/Dutch "Vertical offset" → "Velocity" |
| TS-10 |  | ❔40 | ❔39 | ✅85 | split | · | Finnish/Korean "Next reload starts at" → "Step acceleration" |
| TS-11 |  | ❔40 | ❔39 | ✅90 | split | · | French/Finnish/Korean "No pointers" → "Both pointers" (opposite meaning) |
| TS-12 |  | ❔40 | ❔39 | ✅90 | split | · | French "Alt" key → "Tout" (means "All") |
| TS-13 |  | ❔40 | ❔39 | ✅90 | split | · | French "Set velocity to 0–10" (all 11) → identical "Vitesse de départ" |
| TS-14 |  | ❔40 | ❔39 | ✅85 | split | · | French "Clear color" → "Light color" |
| TS-15 |  | ❔40 | ❔39 | ✅85 | split | · | Finnish/Korean right pointer reuse → left pointer (swapped) |
| TS-16 |  | ⚠️45 | ⚠️58 | ✅90 | split | · | Paragraph spacing: 8 languages strip trailing `%` from `<pre>%1%</pre>` |
| TS-17 |  | ⚠️45 | ⚠️58 | ✅90 | split | · | Line width: 7 languages add spurious `%` to `<pre>%1</pre>` |
| TS-18 |  | ❔40 | ❔39 | ✅85 | split | · | Orphan files: Hebrew and Polish exist but UI entries commented out |
| HTK-01 | Critical | ❔45 | ❔39 | ✅95 | split | · | KGlobalAccel default permanently destroyed on first user customization |
| HTK-02 | High | ❔45 | ❔39 | ✅92 | split | · | User shortcuts never persisted when only Use_GlobalAccel defined (no QHotkey) |
| HTK-03 | High | ⚠️50 | ⚠️58 | ✅90 | split | · | KGlobalAccel defaults silently zeroed on non-Wayland when QHotkey co-exists |
| HTK-04 | Medium | ✅60 | ✅92 | ✅85 | AGREE | · | Wrong enum type `Qt::KeyboardModifier` (singular) for modifier variable |
| HTK-05 | Medium | ⚠️50 | ⚠️58 | ✅90 | split | · | VelocityTo0 default shortcut uses `Qt::Key_acute` — unreachable dead key |
| HTK-06 | Medium | ⚠️45 | ⚠️58 | ✅90 | split | · | Pause (Ctrl+Space) and Stop (Meta+Space) conflict — Meta+Space captured by OS |
| HTK-07 | Low | ⚠️45 | ⚠️58 | ✅88 | split | · | Double `removeAllShortcuts()` IPC round-trip in customization path |
| HTK-08 | Low | ⚠️50 | ⚠️58 | ✅85 | split | · | key/modifiers parameters silently discarded mid-function on non-Wayland |
| TMR-01 | High | ❔50 | ❔39 | ✅92 | split | · | Countdown→Prompting auto-transition via state++ bypasses toggle() entirely |
| TMR-02 | Medium | ❔45 | ❔39 | ✅80 | split | · | timer.updateTimer() runs before timer.startTimer() on Prompting entry |
| TMR-03 | Medium | ⚠️50 | ⚠️58 | ✅85 | split | · | dissolveIn animation re-triggered entering Running from Ready — flicker |
| TMR-04 | Low | ❔45 | ❔39 | ✅80 | split | · | Countdown arc hypotenuse uses geometric center instead of arc center |
| TMR-05 | Low | ✅85 | ✅78 | ✅88 | AGREE | · | ScriptAction `paintReady` references non-existent function |
| TMR-06 | Low | ❔45 | ❔39 | ✅85 | split | · | dissolveOut starts too early when disappearWithin > 1 |
| TMR-07 | Low | ✅55 | ⚠️58 | ⚠️65 | split | · | countdownAnimation restart uses non-idempotent running=true |
| TMR-08 | Low | ❔45 | ❔39 | ✅80 | split | · | timer.running not explicitly set in Countdown state — relies on revert behavior |
| SPL2-11 | Medium | ✅60 | ✅78 | ✅90 | AGREE | · | addCustomWord trims but removeCustomWord does not — asymmetry |
| SPL2-12 | Medium | ✅55 | ✅92 | ✅88 | AGREE | · | Case-sensitive contains/indexOf but case-insensitive sort — duplicates |
| SPL2-13 | Medium | ✅55 | ✅78 | ✅90 | AGREE | · | saveCustomWordsToDisk has void return — callers cannot detect I/O failure |
| SPL2-14 | Medium | ✅65 | ✅92 | ✅85 | AGREE | · | Cached QRC dicts never invalidated after app update |
| SPL2-15 | Medium | ✅60 | ✅78 | ✅90 | AGREE | · | spell() returns true when no dicts loaded — silent no-op |
| SPL2-16 | Low | ✅55 | ✅88 | ✅80 | AGREE | · | QDir::mkpath return unchecked — dict cache directory may silently not exist |
| SPL2-17 | Low | ✅55 | ✅88 | ✅80 | AGREE | · | QFile::setPermissions return unchecked — cached dict may be unreadable |
| SPL2-18 | Low | ✅55 | ✅88 | ✅85 | AGREE | · | Hunspell::add return value unchecked at 4 call sites |
| SPL2-19 | Low | ✅55 | ✅78 | ✅85 | AGREE | · | availableDictionaries enumerates .dic without verifying .aff exists |
| SPL2-20 | Low | ⚠️45 | ⚠️58 | ❌85 | split | · | loadCustomWordsFromDisk redundant exists() before open() |
| WSM-03 | High | ⚠️50 | ⚠️58 | ✅88 | split | · | readAsDataURL causes quadruple in-memory copy of file content |
| BLD-05 | Medium | ✅55 | ✅78 | ✅95 | AGREE | · | .env.android references Qt 5.15.2 — project requires Qt 6.8.2+ |
| EVT-01 | High | ⚠️50 | ⚠️58 | ⚠️60 | AGREE | · | velocityDragArea (z:5) blocks viewport.mouse (z:0) wheel events |
| EVT-02 | High | ❌55 | ⚠️58 | ✅88 | **CONFLICT** | · | Zero inputMethodHints on any TextField — IME broken for CJK/Indic |
| EVT-03 | High | ⚠️50 | ⚠️58 | ✅90 | split | · | velocityDragOverlay (z:7) steals clicks from control buttons (z:6) |
| EVT-04 | High | ⚠️50 | ⚠️58 | ✅92 | split | · | Drag breaks editor.x declarative binding permanently |
| EVT-05 | High | ⚠️50 | ⚠️58 | ✅92 | split | · | Drag breaks positionHandler.x declarative binding permanently |
| EVT-06 | Medium | ⚠️50 | ⚠️58 | ✅90 | split | · | Drag breaks stopwatch.x binding permanently |
| EVT-07 | Medium | ✅60 | ✅78 | ✅90 | AGREE | · | TabBar currentIndex binding broken on first TabButton click |
| EVT-08 | Medium | ✅60 | ✅78 | ✅88 | AGREE | · | Two additional checkable ToolButton binding breakage instances |
| EVT-09 | Low | ⚠️45 | ⚠️52 | ✅78 | split | · | Flow ToolSeparator visibility compares y of potentially invisible rows |
| EVT-10 | Low | ⚠️50 | ⚠️58 | ✅85 | split | · | Nested MouseAreas with hoverEnabled steal hover from parent Buttons |
| ENC-01 | Medium | ✅60 | ✅78 | ✅88 | AGREE | · | truncate(-1) when font preview text has no spaces |
| ENC-02 | Low | ✅55 | ✅78 | ✅85 | AGREE | · | getMarkerKey() mid(4) without length/startsWith guard |
| ANM-N01 | Medium | ✅70 | ✅78 | ✅92 | AGREE | · | Easing.EaseOut is not a valid Qt Quick easing type (2 instances) |
| NET-01 | High | ✅65 | ✅84 | ✅92 | AGREE | · | loadFromNetworkFinihed never checks m_reply->error() |
| NET-02 | Medium | ⚠️50 | ⚠️58 | ⚠️70 | AGREE | · | RedirectPolicyAttribute set to boolean true → NoLessSafeRedirectPolicy |
| THR-01 | Medium | ⚠️45 | ⚠️58 | ✅82 | split | · | IosSaveDialog::create() — unsynchronized singleton race |
| THR-02 | Medium | ⚠️45 | ⚠️58 | ✅82 | split | · | ShakeDetector::create() — identical unsynchronized singleton race |
| THR-03 | Low | ⚠️50 | ⚠️58 | ✅80 | split | · | search() — mutable static QRegularExpression shared across all callers |
| THR-04 | Medium | ⚠️45 | ✅78 | ⚠️72 | split | · | SpellChecker zero thread safety — explicit finding |
| DRW-01 | Medium | ⚠️50 | ⚠️58 | ✅88 | split | · | interalFocusElsewhere() misses 3 OverlaySheets + 2 Drawers — hotkeys pass through |
| DRW-02 | Medium | ⚠️50 | ⚠️58 | ✅88 | split | · | globalDrawer and contextDrawer missing from ESC dismiss chain |
| AND-BLD-01 | Critical | ✅80 | ✅92 | ✅95 | AGREE | · | Missing version.gradle — Gradle build fails |
| AND-RES-01 | Medium | ⚠️45 | ⚠️58 | ✅90 | split | · | Invalid android:scaleType on bitmap element |
| AND-MFT-01 | Medium (latent) | ⚠️45 | ⚠️58 | ✅85 | split | · | FileProvider resource @xml/qtprovider_paths — file named filepaths.xml |
| SHADOW-01 | Low | ✅60 | ✅78 | ✅85 | AGREE | · | id: rotation shadows Item.rotation property |
| SHADOW-02 | Low | ✅55 | ✅78 | ✅85 | AGREE | · | id: flow shadows Flow.flow property |
| FOC-N01 | Low | ✅65 | ✅78 | ✅88 | AGREE | · | focus: true is JS label in atEndLoopDelay SpinBox |
| FOC-N02 | Low | ✅65 | ✅78 | ✅88 | AGREE | · | Same JS label bug in countdownConfiguration SpinBoxes (2 instances) |
| FOC-N03 | Low | ⚠️50 | ✅78 | ✅85 | split | · | Tab/Backtab asymmetry — Backtab silently unhandled |
| VER-01 | Low | ⚠️45 | ✅78 | ✅85 | split | · | Qt::MarkdownText version guard 0x050F00 (5.15) — API added in 5.14 |
| CPY-01 | Low | ⚠️40 | ⚠️58 | ✅80 | split | · | 5 Q_INVOKABLE methods pass QString by value instead of const& |
| DSZ-01 | Medium | ✅60 | ⚠️58 | ✅88 | split | · | InputsOverlay hardcoded height:680 — overflows on phones |
| DSZ-02 | Medium | ⚠️45 | ✅78 | ✅88 | split | · | pointerConfiguration OverlaySheet no vertical ScrollView |
| DSZ-03 | Low | ⚠️40 | ⚠️58 | ✅85 | split | · | Magic number 68 in ListView height binding |
| JSN-01 | High | ✅65 | ✅92 | ✅90 | AGREE | · | i.d.authentication accessed without undefined guard |
| JSN-02 | Medium | ⚠️50 | ✅78 | ✅90 | split | · | ws.sendTextMessage() called without checking WebSocket status |
| QCN-01 | Low | ✅55 | ✅78 | ✅90 | AGREE | · | O(n²) contains()-in-loop during custom words file load |
| PC-01 | Medium | ❔45 | ❔39 | ✅70 | split | · | countdown.state not set in Prompting state — countdown visible during teleprompting |
| QTD-01 | Medium | ✅65 | ✅78 | ✅85 | AGREE | · | m_spellHighlighter not detached when setDocument(nullptr) |
| QTD-02 | Low-Medium | ❔40 | ✅78 | ✅85 | split | · | QQuickTextDocument destroyed without destroyed signal connection |
| OPC-01 | Medium | ⚠️50 | ✅78 | ✅90 | split | · | Right-click toggle desynchronizes velocityIndicator visible/opacity |
| HDR-N01 | Low | ✅60 | ⚠️58 | ✅95 | split | · | promptsession.h not in CMakeLists.txt — SessionModel/DataPoint dead code |
| HDR-N02 | Low | ✅60 | ⚠️58 | ✅95 | split | · | telemetry.h not in CMakeLists.txt — Telemetry dead code |
| IO-N01 | Medium | ⚠️45 | ✅78 | ✅90 | split | · | saveAs() leaves _fileSystemWatcher permanently blocked on open failure |
| IO-N02 | High | ✅50 | ✅84 | ✅85 | AGREE | · | save() constructs QUrl without file:// scheme — broken on non-Windows |
| IO-N03 | Medium | ✅55 | ✅88 | ✅90 | AGREE | · | iossavedialog.mm QFile::write() return value unchecked |
| QML-BND-01 | High | ✅60 | ✅84 | ✅90 | AGREE | · | countdownAnimation.running binding permanently broken after first iteration |
| QML-BND-02 | Medium | ✅55 | ✅78 | ✅90 | AGREE | · | clock.__iteration binding broken by post-decrement in animation handler |
| QML-BND-03 | None (info) | ⚠️40 | ⚠️58 | ✅95 | split | · | ReadRegionOverlay onDestruction — harmless dead code |
| WSM-N01 | High | ✅60 | ✅84 | ✅85 | AGREE | · | Synchronous QImage::load() from HTTP blocks WASM main thread |
| WSM-N02 | Low | ✅60 | ✅78 | ✅90 | AGREE | · | WASM preventSleep() falls through to desktop #else — always returns false |
| QRC-N01 | Low | ❔45 | ✅92 | ✅95 | split | · | icons.qrc contains duplicate \<file\> entry |
| QRC-N02 | Low | ⚠️45 | ⚠️58 | ✅90 | split | · | Four .qrc files are dead code — never referenced by CMakeLists.txt |
| CMAKE-N01 | Low | ⚠️45 | ⚠️58 | ❔60 | split | · | WASM build excludes TelemetryPage.qml and RemotePage.qml |
| OOB-N01 | Medium | ⚠️50 | ✅78 | ✅90 | split | · | MarkersModel::data() — m_data.at() without row < rowCount() guard |
| OOB-N02 | Medium | ⚠️45 | ✅78 | ✅90 | split | · | SessionModel::data() — same missing row bounds guard |
| OOB-N03 | Low | ⚠️50 | ✅78 | ✅85 | split | · | alignment() fetches textCursor() twice — stale cursor race |
| I18N-N01 | Low | ⚠️40 | ⚠️58 | ✅80 | split | · | Stale source-location line numbers in all 20 .ts files |
| I18N-N02 | Low | ⚠️40 | ⚠️58 | ✅80 | split | · | Vanished translation entries not purged across 13 language files |
| STR-N01 | High | ✅70 | ✅84 | ✅90 | AGREE | · | main.cpp:158 QLatin1String iterator-pair UB from two unrelated string literals |
| NOTIFY-01 | Medium | ✅75 | ✅78 | ✅95 | AGREE | · | setAutoReload doesn't emit autoReloadChanged NOTIFY signal |
| NOTIFY-02 | Low | ✅55 | ✅78 | ⚠️85 | split | · | availableDictionariesChanged NOTIFY signal never emitted |
| MIX-01 | Low | ⚠️40 | ✅78 | ✅90 | split | · | spellchecker.cpp:98 size_t→int narrowing in languages() reserve |
| ENUM-01 | Medium | ⚠️45 | ✅78 | ✅90 | split | · | documenthandler.cpp:1108 updateContents switch no default — silent data loss |
| DPI-01 | Medium | ⚠️40 | ⚠️58 | ✅80 | split | · | TimerClock.qml:127 devicePixelRatio in raw arithmetic with magic multiplier |
| DPI-02 | Low | ⚠️45 | ⚠️58 | ✅85 | split | · | MarkersDrawer.qml:37 drawer minimumWidth hardcoded to 260px |
| DPI-03 | Low | ⚠️45 | ⚠️58 | ✅90 | split | · | Find.qml:38 searchBarWidth:724 hardcoded in px |
| DPI-04 | Medium | ✅60 | ⚠️58 | ✅90 | split | · | InputsOverlay.qml:33 height:680 hardcoded |
| GEO-01 | Low | ⚠️45 | ⚠️58 | ✅80 | split | · | main.qml initial 728px height too large for 1366x768 laptops |
| GEO-02 | Medium | ⚠️50 | ⚠️58 | ✅90 | split | · | main.qml persists x/y/width/height with zero validation |
| GEO-03 | Low | ⚠️40 | ⚠️58 | ✅90 | split | · | +android/main.qml no minimumWidth/minimumHeight |
| UNIT-01 | High | ⚠️55 | ✅84 | ✅95 | split | · | ProgressIndicator.qml:46 Units.ShortDuration with no Kirigami import |
| UNIT-02 | High | ⚠️55 | ✅84 | ✅95 | split | · | PrompterView.qml 7x Units.ShortDuration with no Kirigami import |
| UNIT-03 | Medium | ⚠️50 | ✅78 | ✅95 | split | · | PrompterBackground.qml:160 Units.LongDuration no Kirigami import |
| UNIT-04 | Medium | ⚠️50 | ✅78 | ✅95 | split | · | Flip.qml:34,41 two Units.LongDuration no Kirigami import |
| UNIT-05 | Low | ⚠️50 | ✅78 | ✅95 | split | · | pointer_0.qml:72 Units.VeryLongDuration no Kirigami import |
| UNIT-06 | Medium | ⚠️50 | ✅78 | ✅95 | split | · | Find.qml:92 Units.ShortDuration with namespaced Kirigami import |
| UNIT-07 | Medium | ⚠️50 | ✅78 | ✅90 | split | · | ReadRegionOverlay.qml 3x Units.ShortDuration with namespaced import |
| AR-01 | Low | ⚠️45 | ✅78 | ✅75 | split | · | PrompterView.qml:53-58 Rotation debug feature clips on extreme aspect ratios |
| SAFE-01 | Medium | ⚠️45 | ⚠️58 | ✅80 | split | · | +android/main.qml zero safe area insets |
| SAFE-02 | Medium | ⚠️45 | ⚠️58 | ✅80 | split | · | ReadRegionOverlay screenMiddle ignores notch/status bar height |
| SET-01 | High | ⚠️45 | ✅84 | ✅90 | split | · | macOS/iOS: QSettings split across two preference domains |
| SET-02 | High | ❔45 | ✅84 | ✅90 | split | · | factoryReset() incomplete on macOS/iOS — domain-path settings survive |
| SET-03 | Low | ⚠️50 | ✅78 | ✅85 | split | · | QString "true" used as default for boolean QSettings value |
| SET-04 | Low | ⚠️45 | ✅78 | ✅85 | split | · | spellCheckLanguages read without explicit default value |
| INV-N01 | Medium | ⚠️50 | ✅78 | ✅85 | split | · | QmlUtil::r() stores QML-owned QQuickItemGrabResult raw pointer — use-after-free |
| CMAKE-NEW-01 | Low | ⚠️45 | ✅78 | ✅90 | split | · | Remote.qml exists on disk but never listed in QML_FILES |
| CMAKE-NEW-02 | Medium | ✅55 | ✅92 | ✅90 | AGREE | · | Duplicate install() of appdata.xml/desktop in root and src/CMakeLists.txt |
| CMAKE-NEW-03 | Medium | ✅55 | ✅78 | ✅90 | AGREE | · | find_package(KF6Crash ... COMPONENTS) — COMPONENTS keyword with zero names |
| CMAKE-NEW-04 | Medium | ✅60 | ✅78 | ✅90 | AGREE | · | execute_process uses CMAKE_PREFIX_PATH (list) as scalar — broken command |
| DLG-N01 | High | ✅60 | ✅84 | ✅90 | AGREE | · | document.modified=false set BEFORE saveAs() — failed save loses unsaved flag |
| DLG-N02 | High | ✅65 | ✅84 | ✅95 | AGREE | · | onError handler clears document.modified on save failure |
| DLG-N03 | Low | ⚠️45 | ✅78 | ✅90 | split | · | errorDialog MessageDialog has no title |
| DLG-N04 | Medium | ✅60 | ✅78 | ✅90 | AGREE | · | load() silently fails with no notification when file missing or unreadable |
| DLG-N05 | Medium | ✅55 | ✅78 | ✅90 | AGREE | · | loadFromNetworkFinihed() silently ignores empty response |
| DLG-N06 | High | ✅65 | ✅84 | ✅90 | AGREE | · | import() error strings passed as document content via updateContents() |
| DLG-N07 | Low | ⚠️45 | ✅78 | ✅85 | split | · | 5 showPassiveNotification() calls ignore passiveNotifications preference |
| DLG-N08 | Low | ⚠️45 | ✅78 | ✅85 | split | · | 3 save-completion passive notifications lack passiveNotifications guard |
| IMP-NEW-01 | High | ❌65 | ❌76 | ✅90 | **CONFLICT** | · | #include \<qnativeinterface.h\> doesn't exist — breaks Android build |
| IMP-NEW-02 | Low | ⚠️45 | ⚠️58 | ⚠️80 | AGREE | · | main.cpp:22 #include "qglobal.h" uses quotes + Qt5-era name |
| IMP-NEW-03 | Low | ⚠️40 | ⚠️58 | ✅95 | split | · | main.cpp:38-39 redundant #include \<QtQml/qqml.h\> + #include \<QtQml\> |
| IMP-NEW-04 | Low | ⚠️40 | ⚠️58 | ✅90 | split | · | AboutPage.qml imports Kirigami 2.9 vs 2.11 in all other files |
| IMP-NEW-05 | Low (orphaned QRC, never compiled) | ❔45 | ⚠️58 | ⚠️80 | split | · | pointers.qrc RESOURCE_PREFIX conflicts with qt_add_qml_module |
| MA-N01 | Low | ⚠️50 | ✅78 | ✅95 | split | · | overlayMouseArea permanently disabled — dead MouseArea |
| MA-N02 | Low | ✅55 | ✅78 | ✅85 | AGREE | · | textDragArea missing cursorShape — ArrowCursor over IBeamCursor on editor |
| CMT-N01 | Medium | ⚠️40 | ⚠️48 | ✅90 | split | · | Justify ToolButton comment says it's commented out — but it's active |
| CMT-N02 | Low | ⚠️35 | ⚠️48 | ✅90 | split | · | Truncated comment in markersmodel.cpp:107-108 |
| CMT-N03 | Medium | ⚠️35 | ⚠️48 | ✅85 | split | · | Misleading OpenGL workaround comment — scope of impact understated |
| CMT-N04 | Medium | ❌55 | ❌76 | ✅85 | **CONFLICT** | · | Comment masks invalid enum bug — 2 - value produces out-of-range LayoutDirection |
| CMT-N05 | High | ⚠️40 | ⚠️48 | ✅85 | split | · | Missing security warning on QProcess RCE sink (sys://) |
| CMT-N06 | Medium | ⚠️40 | ⚠️48 | ✅80 | split | · | Missing warning: re-entrant toggle() inside Behavior.onRunningChanged |
| CMT-N07 | Medium | ⚠️40 | ⚠️48 | ✅85 | split | · | Missing warning: joinPreviousEditBlock() without beginEditBlock() |
| CMT-N08 | Medium | ✅50 | ⚠️48 | ✅90 | split | · | Entire Telemetry class is dead commented-out shell across 4 files |
| CMT-N09 | Medium | ⚠️40 | ⚠️48 | ✅85 | split | · | Commented-out PropertyActions in active loop animation — stale state risk |
| CMT-N10 | Low | ⚠️35 | ⚠️48 | ✅90 | split | · | Obsolete Qt 5 qmlRegisterType calls as commented-out cruft |
| REGEX-N01 | Medium | ⚠️45 | ✅78 | ✅85 | split | · | All 13 QRegularExpression objects lack isValid() checks |
| REGEX-N02 | Medium | ✅55 | ✅78 | ✅80 | AGREE | · | regex_5 accidentally excludes 15+ HTML5 tags from background-color filtering |
| REGEX-N03 | Low | ✅65 | ✅78 | ✅85 | AGREE | · | Unescaped dot in font-size regex — matches any char instead of decimal |
| HK-N01 | High | ⚠️50 | ⚠️58 | ✅90 | split | · | Missing event.isAutoRepeat guard on main Keys.onPressed |
| HK-N02 | Medium | ✅80 | ✅92 | ✅95 | AGREE | · | Typo Qt.Key_VolumeDowm — "Dowm" instead of "Down" — volume-down hardware key dead |
| HK-N03 | High | ⚠️50 | ⚠️58 | ✅90 | split | · | platformName() != "wayland" fails on "wayland-egl" — global hotkeys dead |
| HK-N04 | Medium | ⚠️45 | ⚠️58 | ✅85 | split | · | No auto-repeat guard in key-binding configuration Keys.onPressed |
| HK-N05 | Medium | ✅60 | ✅78 | ✅85 | AGREE | · | Strict === equality on modifiers breaks user keybinds with NumLock |
| HK-N06 | Low | ⚠️45 | ⚠️58 | ✅80 | split | · | isValidInput checks local keybindings only — silent conflict with global hotkeys |
| LDR-N01 | Medium | ⚠️50 | ⚠️58 | ✅85 | split | · | InputsOverlay typeof null guard fails — null.item crash on rapid close |
| PARSE-N01 | Medium | ⚠️50 | ✅78 | ✅85 | split | · | insertImageAt() stores image resource with file:// key but looks up via plain path |
| PARSE-N02 | Medium | ✅60 | ✅78 | ✅85 | AGREE | · | MarkersModel::keySearch() hits=1 limits search to first marker only |
| PROP-N01 | High | ✅70 | ✅84 | ✅95 | AGREE | · | on__FullScreenChanged handler casing mismatch — never fires |
| PROP-N02 | Medium | ⚠️55 | ⚠️58 | ✅85 | split | · | setCursorPosition → reset() — 12-signal storm, no debounce |
| PROP-N03 | Low | ⚠️45 | ⚠️58 | ✅85 | split | · | setMarker/setKeyMarker/setMarkerHref silently trigger full document reparse |
| NET-N04 | Medium | ✅60 | ✅78 | ✅90 | AGREE | · | No transfer timeout on any QNetworkRequest |
| NET-N05 | Medium | ✅60 | ✅78 | ✅85 | AGREE | · | loadFromNetwork() hardcodes http:// scheme — never upgrades to HTTPS |
| NET-N06 | Low | ✅65 | ⚠️58 | ✅85 | split | · | loadFromNetwork() validates original URL, not constructed resultingUrl |
| URL-N01 | Medium | ✅60 | ⚠️58 | ✅65 | split | · | reload() constructs file:// URL by string concatenation without encoding |
| DISK-N01 | Low | ✅55 | ✅78 | ✅55 | AGREE | · | saveCustomWordsToDisk() non-atomic write — data loss on power failure |
| INIT-N01 | Medium | ✅90 | ✅78 | ✅90 | AGREE | · | Velocity modifier ComboBox model has 2 entries, switch handles 4 cases |
| INIT-N02 | Low | ✅50 | ✅78 | ✅85 | AGREE | · | Find.qml SearchField placeholderText always empty — no guidance text |
| INIT-N03 | Low | ⚠️40 | ⚠️58 | ⚠️40 | AGREE | · | ReadRegionOverlay screenMiddle uses root.y from cross-file id resolution |
| INIT-N04 | Low | ⚠️40 | ⚠️58 | ❌80 | split | · | PrompterView ShaderEffectSource.sourceItem references prompter id declared later |
| CMB-N01 | Medium | ❔45 | ❔39 | ✅70 | split | · | autoReloadSeconds SpinBox from binding circular — clamps to 1 when all-zero |
| CMB-N02 | Low | ❔45 | ❔39 | ✅75 | split | · | autoReloadMinutes SpinBox from contains redundant circular self-reference |
| CMB-N03 | Medium | ✅85 | ✅78 | ✅85 | AGREE | · | LanguageSettingsOverlay ListView currentIndex always -1 — wrong indexOf() call |
| VIS-N04 | Low | ⚠️45 | ⚠️58 | ⚠️45 | AGREE | · | Countdown crosshair frame renders orphan lines when enabled=false |
| VIS-N05 | Medium | ⚠️50 | ⚠️58 | ✅65 | split | · | velocityDragOverlay blocks all interaction during indicator fade-out (~500ms dead zone) |
| SCRL-N01 | Medium | ❔45 | ❔39 | ⚠️50 | split | · | __jitterMargin: fractional result from modulus violates 0/1 toggle design |
| SCRL-N02 | Medium | ⚠️50 | ⚠️58 | ✅65 | split | · | __destination typed int truncates real-valued position |
| SCRL-N03 | Medium | ❔45 | ❔39 | ✅55 | split | · | setVelocity() triggers two conflicting scroll animations with intermediate velocity |
| SCRL-N04 | Low | ✅55 | ✅78 | ✅85 | AGREE | · | __speed non-zero when __i=0 and __curvature=0 (Math.pow(0,0)===1) |
| SCRL-N05 | Low | ⚠️50 | ⚠️58 | ❌65 | split | · | __speedLimit check is dead logic — always true |
| SCRL-N06 | Low | ⚠️40 | ⚠️58 | ❌60 | split | · | __timeToEnd uses unexplained 2× factor |
| TYP-N01 | Low | ✅85 | ✅92 | ✅90 | AGREE | · | Misspelled method name: loadFromNetworkFinihed (missing 's') |
| TYP-N02 | Low | ✅90 | ✅92 | ✅90 | AGREE | · | Misspelled parameter: withoutFormating (missing 't') |
| TYP-N03 | Low | ⚠️35 | ⚠️58 | ✅80 | split | · | Inconsistent `_` vs `m_` member prefix: _markersModel, _fileSystemWatcher |
| TYP-N04 | Low | ⚠️35 | ⚠️58 | ✅75 | split | · | Inconsistent m_ method naming: m_initializeSource — mixed underscore+camelCase |
| TYP-N05 | Low | ✅90 | ✅88 | ✅70 | AGREE | · | Uninitialized member m_documentComesFromNetwork |
| TYP-N06 | Low | ⚠️50 | ⚠️58 | ✅65 | split | · | 9 getters copy-paste double-textCursor() pattern — null check on stale cursor |
| CAST-N01 | Medium | ✅60 | ✅78 | ✅70 | AGREE | · | setFontCapitalization static_cast with no range validation — reachable from QML |
| IMG-N01 | Medium | ❔45 | ❔39 | ❔30 | AGREE | · | Missing go-previous-symbolic.svg — back-navigation icon blank on Android/Windows |
| ACT-N05 | Medium | ❔45 | ⚠️58 | ⚠️45 | split | · | +windows main.qml Controls Settings submenu missing OBS Settings action |
| ACT-N06 | Low | ⚠️45 | ⚠️58 | ⚠️45 | AGREE | · | +windows main.qml Performance tweaks missing enableBarsSetting |
| ACT-N07 | Medium | ✅60 | ⚠️58 | ✅65 | split | · | namedBookmarkButton: checkable button opens dialog — stale indicator after first click |
| ACT-N08 | Medium (masked — Labs.MenuBar dead per IMP-N01) | ✅55 | ⚠️58 | ⚠️50 | split | · | All checkable Labs.MenuItems inherit R2-EDT-03 binding-break pattern |
| RENDER-01 | Medium | ⚠️50 | ✅78 | ✅70 | split | · | ShaderEffectSource prompterShadowSource runs unconditionally — wastes GPU capture when shadows disabled |
| RENDER-02 | Medium | ⚠️50 | ✅78 | ✅70 | split | · | ShaderEffectSource pointerShadowSource runs unconditionally — same pattern |
| TXT-N01 | Low | ⚠️40 | ⚠️58 | ⚠️40 | AGREE | · | Find/replace fields missing persistentSelection: true |
| TXT-N02 | Low | ⚠️40 | ✅78 | ✅75 | split | · | TimerClock default text color #AAA on #131619 — fails WCAG AA contrast |
| PLAT-N01 | Medium | ⚠️45 | ✅78 | ❌85 | **CONFLICT** | · | qmlutil.hpp incorrectly excludes QNX from QProcess — run()/restartApplication() silently no-op |
| PLAT-N02 | Medium | ❔40 | ✅78 | ❌85 | **CONFLICT** | · | documenthandler.cpp incorrectly excludes QNX from import() — LibreOffice broken on QNX |
| PLAT-N03 | High | ❔45 | ❔39 | ❌80 | split | · | Zero Q_OS_TVOS preprocessor guards in C++ despite 19 QML references — build failure |
| DECL-N01 | Low | ⚠️45 | ✅78 | ✅75 | split | · | MarkersModel::keySearch — default params in definition but not declaration |
| DECL-N02 | Low | ⚠️40 | ✅78 | ✅85 | split | · | SessionModel::resetInternalData() missing override keyword and Qt 6 version guard |
| COLOR-01 | Medium | ✅70 | ⚠️58 | ⚠️50 | split | · | ProjectionsManager.qml uses invalid "initial" color — repro of R4-ROOT-02 |
| COLOR-02 | Medium | ⚠️40 | ⚠️58 | ✅75 | split | · | Hardcoded #EED text invisible on light themes — WheelSettingsOverlay |
| COLOR-03 | Low | ⚠️40 | ⚠️58 | ⚠️45 | AGREE | · | velocityText ColorAnimation flash: #BBB → #FFF → #CCC jump |
| COLOR-04 | Low | ⚠️45 | ⚠️58 | ✅65 | split | · | ReadRegionOverlay ColorAnimation tracks __fillColor that never changes |
| COLOR-05 | Low | ⚠️40 | ⚠️58 | ⚠️40 | AGREE | · | Prompter scrollbar gradient hardcodes #CCC/#998/#665 — low contrast on light backgrounds |
| COLOR-06 | Low | ⚠️40 | ⚠️58 | ⚠️40 | AGREE | · | Countdown #FFF digits on #333-at-0.48-overlay — insufficient contrast on light backgrounds |
| COLOR-07 | Low | ⚠️55 | ⚠️58 | ✅65 | split | · | CSS default stylesheet hardcodes #FFFFFF body text — ignores user text color |
| EVT-N10 | Medium | ❔45 | ⚠️58 | ✅70 | split | · | Editor Ctrl+Letter shortcuts don't accept event — marker key-search double-fires |
| EVT-N11 | Low | ⚠️45 | ⚠️58 | ❌70 | split | · | windowStayOnTopButton lacks focusPolicy — unreachable via keyboard |
| EVT-N12 | Low | ⚠️50 | ⚠️58 | ✅60 | split | · | velocityDragArea and viewport.mouse share z:5 — wheel dispatch ambiguous |
| STATE-N01 | High | ❔45 | ✅84 | ⚠️50 | split | · | Shadowed Prompting→Editing transition — velocity default never saved |
| STATE-N02 | Medium | ⚠️50 | ✅78 | ✅75 | split | · | Find.toggle() uses !visible instead of !isOpen — can't close during Prompting |
| STATE-N03 | Low | ⚠️50 | ✅78 | ✅65 | split | · | Countdown Running restarts dissolveIn unnecessarily — visual dim-to-bright flash |
| STATE-N04 | Low | ❔45 | ✅78 | ✅70 | split | · | loop animation cancel() state change overridden by toggle() due to QML batching |
| SIZE-N01 | Medium | ✅60 | ✅78 | ✅80 | AGREE | · | concentricCircles Shape has conflicting anchors.fill + anchors.centerIn |
| SIZE-N02 | Low | ✅55 | ✅78 | ✅75 | AGREE | · | Three Button children of Row have dead anchors.bottom declarations |
| CONST-N01 | Low | ⚠️40 | ⚠️58 | ✅60 | split | · | getMarkerKey() not const — pure reader without side effects |
| CONST-N02 | Low | ⚠️40 | ⚠️58 | ✅60 | split | · | getMarkerHref() not const — identical pattern |
| CONST-N03 | Low | ⚠️40 | ⚠️58 | ✅55 | split | · | MarkersModel::previousMarker(), nextMarker(), keySearch(), binarySearch() not const |
| CONST-N04 | Low | ⚠️40 | ⚠️58 | ✅60 | split | · | GlobalHotkeys::globalShortcutKey(Action) not const — Q_INVOKABLE pure query |
| CONST-N05 | Low | ⚠️40 | ⚠️58 | ✅65 | split | · | Unnecessary copy via const auto instead of const auto& in extendLastMarker |
| SAVE-N01 | Medium | ⚠️55 | ✅78 | ✅70 | split | · | loadFromNetworkFinihed sets m_fileUrl to phantom QTemporaryFile path |
| SAVE-N02 | High | ⚠️50 | ✅84 | ✅75 | split | · | iOS save flow never updates C++ m_fileUrl — file URL perpetually stale |
| SAVE-N03 | Medium | ✅55 | ✅78 | ✅75 | AGREE | · | saveAs() never updates _fileSystemWatcher — watches stale file after save-as |
| SAVE-N04 | Low | ⚠️45 | ✅78 | ✅65 | split | · | save() unnecessary QString→std::string→QString round-trip through locale encoding |
| SAVE-N05 | Low | ✅50 | ✅78 | ✅70 | AGREE | · | save() broken on Android content:// URIs — empty filename |
| LOAD-N01 | Medium | ⚠️50 | ✅78 | ✅65 | split | · | TOCTOU race between QFile::exists() and file.open() in load() |
| LOAD-N02 | Low | ⚠️50 | ✅78 | ❌75 | **CONFLICT** | · | reset() emits 12 NOTIFY signals when open() fails but exists() succeeds |
| SHDR-N01 | Medium | ✅65 | ✅78 | ✅85 | AGREE | · | Math.cos/Math.sin used with degrees value — shadow offset diagonal instead of horizontal |
| RAII-N01 | Medium | ⚠️50 | ✅78 | ✅60 | split | · | QDrag object never deleteLater'd after exec() — leaks on rejected drags |
| RAII-N02 | Low | ⚠️50 | ⚠️58 | ✅55 | split | · | IosSaveDialog::m_tempDir created unconditionally on all platforms — wasted I/O |
| RAII-N03 | Medium | ⚠️50 | ✅78 | ❌70 | **CONFLICT** | · | QProcess orphan — child process detached on waitForFinished() timeout |
| Z-N01 | Medium | ⚠️45 | ✅78 | ⚠️45 | split | · | CursorAutoHide has no explicit z — hover detection fragile against Kirigami internals |
| Z-N02 | Low | ⚠️40 | ✅78 | ⚠️40 | split | · | Two OverlaySheets have z:1 while nine others have none — inconsistent stacking |
| Z-N03 | Low | ⚠️40 | ✅78 | ⚠️40 | split | · | ComboBox Popup z:103 inside OverlaySheets with z:1 — disconnected layering |
| Z-N04 | Low | ⚠️45 | ✅78 | ✅65 | split | · | PrompterBackground (z:0) renders above viewport.mouse (z:0) — latent input intercept |
| TIME-N01 | Low | ✅60 | ✅78 | ✅85 | AGREE | · | copyrightYear computed then discarded — stale "2020-2026" in About after 2026 |
| XFRM-N01 | Low | ❔45 | ❔39 | ⚠️45 | split | · | PrompterView.qml Rotation permanently overridden by PrompterPage.qml |
| API-N01 | Medium | ⚠️50 | ✅78 | ✅65 | split | · | setAlignment() missing null-cursor guard — crash risk with no document |
| API-N02 | Medium | ✅80 | ✅78 | ✅80 | AGREE | · | selectionIsLowerCase NOTIFY signal is wrong — fontCapitalizationChanged, never emitted for case changes |
| API-N03 | Medium | ⚠️50 | ✅78 | ✅75 | split | · | CursorAutoHide.qml unconditionally dereferences pageStack.currentItem.prompter |
| API-N04 | Low | ⚠️35 | ✅78 | ✅65 | split | · | setMarker(bool) misleadingly named — sets regular marker, not any marker |
| API-N05 | Low | ⚠️50 | ✅78 | ✅70 | split | · | fileName()/fileType() return fabricated defaults — can't distinguish "no file" from "untitled.html" |
| API-N06 | Low | ✅80 | ⚠️58 | ✅80 | split | · | SystemFontChooserDialog::show() calls setText() on same label twice — dead code |
| API-N07 | Low | ✅55 | ✅78 | ✅75 | AGREE | · | SpellChecker::encode() fallback says "Latin-1" but calls toLocal8Bit() |
| ARC-01 |  | ⚠️35 | ⚠️48 | ❌50 | split | · | Velocity physics engine entirely in QML (~20 readonly property bindings) |
| ARC-02 |  | ⚠️35 | ⚠️48 | ❌50 | split | · | Arc-03 Search/replace state machine fully in QML (50+ lines) |
| ARC-03 |  | ⚠️35 | ⚠️48 | ❌50 | split | · | OBS WebSocket v5 protocol in QML — opcode dispatch, auth, subscription |
| ARC-04 |  | ⚠️40 | ⚠️48 | ❌50 | split | · | DocumentHandler is 2295-line god class spanning file I/O, network, HTML filtering, markers, spellcheck, drag-drop, images, search, undo, clipboard, sleep prevention, font dialog |
| ARC-05 |  | ⚠️35 | ⚠️48 | ❌50 | split | · | Prompter.qml is 3139-line god component spanning velocity, state machine, keyboard, WebSocket, markers, spellcheck UI, file dialogs, WYSIWYG toggle, shadows |
| ARC-06 |  | ⚠️35 | ⚠️48 | ❌50 | split | · | qmlutil.hpp is utility grab-bag with 10+ unrelated functions |
| KEY-N01 | Medium | ❔45 | ❔39 | ✅70 | split | · | Named marker key binding silently discards all modifier information |
| CLI-N01 | Medium | ⚠️50 | ✅78 | ⚠️55 | split | · | --version flag non-functional — version string empty when parser processes |
| DPR-N01 | Medium | ✅55 | ✅78 | ✅70 | AGREE | · | Prompter.qml uses Screen.devicePixelRatio (global) instead of screen.devicePixelRatio (window) |
| SCALE-N01 | Medium | ⚠️50 | ✅78 | ✅65 | split | · | Right pointer xScale: -1 mirrors text pointers — backwards/unreadable text |
| ORIENT-N01 | Low | ⚠️45 | ⚠️58 | ✅60 | split | · | TimerClock binary width>height orientation creates sharp 2x font jump at 1:1 |
| BIND-N01 | Low | ⚠️50 | ✅92 | ✅65 | split | · | contentWidth undefined for Shape/Image pointer types — transform origin silently wrong |
| STR-CNV | Low | ⚠️45 | ✅78 | ✅60 | split | · | 5 defensive validation gaps: toInt() without ok flag in getMarkerKey, parse(×2), setFontSize, and 32 hotkey reads |
| SHADOW-N03 | High | ✅70 | ✅84 | ❌75 | **CONFLICT** | · | id: stopwatch shadows property bool stopwatch — timersEnabled always true |
| SHADOW-N04 | Low | ⚠️50 | ✅78 | ✅65 | split | · | id: frame shadows property bool frame — latent hazard |
| LINK-N01 | High | ✅65 | ✅84 | ✅80 | AGREE | · | Qt::Network not linked on iOS static build — unresolved symbols |
| LINK-N02 | High | ✅65 | ✅84 | ✅80 | AGREE | · | Qt::Network not linked on WASM static build — same as LINK-N01 |
| LINK-N03 | Medium | ⚠️50 | ✅78 | ✅85 | split | · | Qt::WebSockets found as REQUIRED but never explicitly linked |
| LINK-N04 | Medium | ❔45 | ✅78 | ❌85 | **CONFLICT** | · | KF6::GlobalAccel find_package/link mismatch on Haiku |
| COMP-N01 | Low | ✅55 | ✅92 | ✅95 | AGREE | · | Case-sensitive duplicate detection in setLanguages() |
| COMP-N02 | Medium | ✅50 | ✅78 | ✅90 | AGREE | · | Case-sensitive suffix check misses mixed-case extensions — silent format loss |
| COMP-N03 | Low | ⚠️50 | ✅78 | ✅95 | split | · | regularMarker() same double-textCursor anti-pattern as LOG-07 |
| LBL-N01 | Medium | ⚠️45 | ⚠️58 | ✅70 | split | · | All 12 Sliders in EditorToolbar missing Layout.fillWidth: true — cramped |
| LBL-N02 | Medium | ⚠️40 | ⚠️52 | ✅80 | split | · | 11 Labels with Layout.bottomMargin: -14 — undefined behavior, overlap risk |
| LBL-N03 | Low | ⚠️40 | ⚠️58 | ✅85 | split | · | PrompterView 3× height overflow in theforce debug mode |
| LAY-N01 | Low | ⚠️45 | ⚠️58 | ❔50 | split | · | 10 Labels with Layout.margins but inside MouseArea, not direct layout child — dead |
| LAY-N02 | Low | ⚠️40 | ⚠️58 | ❔50 | split | · | WheelSettingsOverlay explanation text constrained to single column in 2-column GridLayout |
| DLG-N10 | Medium | ⚠️45 | ✅78 | ✅90 | split | · | TimerClock ColorDialog selectedColor never initialized from persisted settings |
| DLG-N11 | Low | ⚠️45 | ✅78 | ✅90 | split | · | PrompterPage ColorDialogs — dead acceptedColor property binding |
| QPROP-N02 | Medium | ❌50 | ❌76 | ✅95 | **CONFLICT** | · | comesFromNetwork Q_PROPERTY missing WRITE clause |
| PATH-N01 | Medium | ⚠️50 | ✅78 | ✅85 | split | · | save() fragile percent-encoding round-trip — broken for UNC paths |
| PATH-N02 | Medium | ✅60 | ✅78 | ✅95 | AGREE | · | reload() constructs file:// URL via raw string concat — #/? in filenames break URL |
| MOB-01 | Medium | ✅70 | ✅92 | ✅80 | AGREE | · | Android: projectionManager undefined — 3 unguarded reference sites |
| MOB-02 | Medium | ⚠️50 | ✅78 | ✅95 | split | · | No +ios/ QML selector — iOS inherits base main.qml with desktop-only components |
| MOB-03 | Medium | ⚠️50 | ✅92 | ✅95 | split | · | iOS: IosSaveDialog silently hangs QML caller when temp dir invalid |
| MOB-04 | Low | ✅65 | ✅78 | ✅95 | AGREE | · | Android: restartApplication() quits without restart |
| MOB-05 | Low | ✅85 | ✅78 | ✅95 | AGREE | · | Android: Missing INTERNET permission in manifest |
| MOB-06 | Low | ✅60 | ✅78 | ✅85 | AGREE | · | Android: PrompterPage display delegate Component.onCompleted references projectionManager — startup TypeError |
| MENU-N01 | Medium | ✅55 | ⚠️58 | ✅95 | split | · | contextMenu.popup(this) missing click coordinates — menu at wrong position |
| MENU-N02 | Medium | ✅60 | ⚠️58 | ✅95 | split | · | Mobile "Add to dictionary" missing %1 placeholder — word never shown |
| MENU-N03 | Medium | ⚠️55 | ⚠️58 | ✅95 | split | · | Text alignment menu RTL swap: labels swap but actions don't |
| MENU-N04 | Low | ✅50 | ⚠️58 | ✅75 | split | · | Trailing empty MenuSeparator at end of mobile context menu |
| MENU-N05 | Low | ⚠️45 | ⚠️58 | ✅95 | split | · | "Redo" context menu item missing & accelerator |
| MENU-N06 | Low | ⚠️50 | ⚠️58 | ⚠️70 | AGREE | · | Paste behavior inconsistent between context menu and global Edit menu |
| DBG-N01 | Medium | ✅60 | ⚠️58 | ✅95 | split | · | OBS WebSocket auth challenge+salt logged to console in release builds |
| DBG-N02 | Low | ✅55 | ⚠️58 | ✅95 | split | · | Velocity debug logging active in production |
| DBG-N03 | Low | ⚠️45 | ⚠️52 | ⚠️60 | AGREE | · | Latent debug state leak: pointers/debug Setting persists Guides checkbox |
| DBG-N04 | Low | ✅60 | ⚠️58 | ✅90 | split | · | qDebug() in namedMarker()/setMarker() active in release |
| WARN-N01 | Low | ⚠️40 | ⚠️58 | ✅80 | split | · | SpellHighlighter::isEnabled() — dead code, never called |
| WARN-N02 | Low | ✅60 | ⚠️58 | ✅85 | split | · | SpellChecker::addWord() — dead public API, never called |
| WARN-N03 | Low | ⚠️45 | ⚠️58 | ✅90 | split | · | quint64→int implicit narrowing in nextMarker()/previousMarker() |
| WARN-N04 | Low | ✅55 | ⚠️58 | ✅95 | split | · | QProcess::startDetached() bool return silently ignored |
| FLOW-N01 | Medium | ✅65 | ✅78 | ✅90 | AGREE | · | setKeyMarker() calls setAnchor("#") — const char*→bool conversion, href never set |
| FLOW-N02 | Medium | ❔45 | ⚠️58 | ✅90 | split | · | increaseVelocity()/decreaseVelocity() skip velocity change when paused |
| DEF-N01 | Medium | ❌65 | ❌76 | ✅90 | **CONFLICT** | · | Flickable.flicking undefined in Qt 6 — wrong cursor during momentum scroll |
| DEF-N02 | Medium | ⚠️50 | ⚠️58 | ✅95 | split | · | DropArea internalDrag always false — internal drag handler dead code |
| TMR-N01 | Medium | ⚠️50 | ⚠️58 | ✅95 | split | · | resetBackground Timer not stopped when new background loaded — race erases new image |
| TMR-N02 | Medium | ⚠️50 | ⚠️58 | ✅90 | split | · | Windows onFrameSwapped missing qmlutil.r(p) — per-frame grab result leak |
| CMAKE-N05 | Low | ✅55 | ✅78 | ✅85 | AGREE | · | foreach(file IN LISTS icon_files doc) — "doc" never defined |
| PRE-N01 | Low | ⚠️55 | ⚠️58 | ⚠️75 | AGREE | · | Preprocessor uses `or` instead of `\|\|` in 6 #if directives — MSVC build break |
| CNTD-N01 | Low | ⚠️50 | ⚠️58 | ✅85 | split | · | Countdown Running: dissolveIn and dissolveOut compete for same opacity when __iterations===__disappearWithin===1 |
| QF-N02 | Low | ⚠️45 | ⚠️58 | ✅85 | split | · | QDir::entryList missing QDir::Readable in availableDictionaries() |
| QF-N03 | Low | ⚠️50 | ⚠️58 | ✅90 | split | · | TOCTOU: QFile::exists() → QFile::copy() in resource cache extraction |
| TXT-CRIT | Critical | ❔45 | ❔39 | ✅85 | split | · | Plain 'v'/'V' keypress silently consumed — letter 'v' cannot be typed |
| TXT-N03 | Medium | ✅80 | ✅78 | ✅90 | AGREE | · | Toolbar paste and Edit menu paste bypass HTML sanitization |
| TXT-N04 | Medium | ⚠️50 | ⚠️58 | ✅85 | split | · | goToNextMarker() temporarily sets cursorPosition=-1 — corrupts cursor state |
| INT-N01 | Low | ⚠️45 | ⚠️58 | ✅90 | split | · | quint64→int narrowing at DocumentHandler→MarkersModel boundary (4 sites) |
| INT-N02 | Medium | ⚠️40 | ✅78 | ✅90 | split | · | replaceAll() returns long — 32-bit overflow on Windows x64 |
| INT-N03 | Low | ⚠️40 | ⚠️58 | ✅80 | split | · | 6 qsizetype→int narrowing conversions across models and loops |
| URL-N03 | Medium | ✅55 | ⚠️58 | ✅90 | split | · | Network-loaded HTML lacks base URL — relative resources broken |
| URL-N04 | Low | ✅60 | ⚠️58 | ✅90 | split | · | loadFromNetwork() validates wrong URL instance |
| URL-N05 | Medium | ✅55 | ⚠️58 | ✅90 | split | · | openFromRemote() blindly prepends http:// to non-HTTP schemes |
| PERF-N01 | Medium | ⚠️50 | ⚠️58 | ✅90 | split | · | onFrameSwapped calls markerCompare() unconditionally — wasted JS call every frame |
| PERF-N02 | Medium | ⚠️50 | ⚠️58 | ✅90 | split | · | RecentDocuments._load() blocks startup with N synchronous createObject() calls |
| PERF-N03 | Low | ⚠️50 | ⚠️58 | ✅85 | split | · | velocityDragOverlay hot-loop calls velocity functions without throttling |
| ERR-N01 | Medium | ✅60 | ✅78 | ✅90 | AGREE | · | removeCustomWord() silently drops dictionary languages on partial reload failure |
| ERR-N02 | Medium | ⚠️55 | ⚠️58 | ✅95 | split | · | insertImageAt() async callback silently discards 3 failure modes |
| PATH-N03 | High | ❔45 | ✅84 | ✅90 | split | · | Wrong ../fonts/ depth in +android and +windows FontLoader paths |
| SIG-N03 | Low | ⚠️40 | ✅78 | ✅75 | split | · | MessageDialog.onButtonClicked declares unused second parameter role |
| QOBJ-N01 | Low | ⚠️40 | ✅78 | ✅85 | split | · | QmlUtil missing constructor with parent parameter |
| TAB-N01 | Medium | ⚠️50 | ✅78 | ⚠️60 | split | · | PointerSettings TabButton onClicked skips currentIndex assignment |
| REGEX-CRIT-01 | High | ❔45 | ❔39 | ✅85 | split | · | regex_4 destroys <body> tag — removes opening tag instead of color attributes |
| REGEX-CRIT-02 | High | ✅55 | ✅84 | ✅95 | AGREE | · | searchRegEx.setPattern() from user input — isValid() never called |
| REGEX-N04 | Medium | ⚠️50 | ✅78 | ✅90 | split | · | ReDoS — user-supplied regex has no length limit, timeout, or backtracking guard |
| REGEX-N05 | Low | ✅70 | ✅78 | ✅85 | AGREE | · | regex_0 and regex_3 use . (any-char) instead of \. (literal dot) in decimal matching |
| REGEX-N06 | Medium | ✅55 | ✅78 | ✅90 | AGREE | · | imgSrcRegex captures wrong src when data-src follows real src |
| VCI-N01 | Low | ⚠️40 | ⚠️48 | ✅95 | split | · | At-end action buttons use inconsistent font scaling (1/1.5 vs 1/1.75) in same group |
| VCI-N02 | Low | ⚠️40 | ⚠️48 | ✅95 | split | · | upperControls and bottomControls fade to different opacity levels during Prompting |
| VCI-N03 | Low | ⚠️40 | ⚠️48 | ⚠️70 | AGREE | · | Hardcoded divider/separator/border colors (#292929, #606060, #808080) break theme adaptation |
| UTF-N01 | Medium | ⚠️50 | ✅78 | ✅90 | split | · | text.truncate(64) can split UTF-16 surrogate pairs — corrupted display |
| AND-CRIT-01 | Critical | ✅85 | ✅84 | ✅95 | AGREE | · | Missing android.permission.INTERNET — all network silently fails |
| AND-HIGH-01 | High | ⚠️50 | ⚠️58 | ✅80 | split | · | Android back button doesn't dismiss overlays/drawers before close |
| AND-HIGH-02 | High | ✅60 | ✅84 | ✅90 | AGREE | · | Android screen never sleeps after prompter use |
| AND-HIGH-03 | High | ✅65 | ✅84 | ✅95 | AGREE | · | factoryReset() quits Android app without restarting |
| AND-MED-01 | Medium | ⚠️45 | ⚠️58 | ✅95 | split | · | Missing intent-filter for opening files from other apps |
| CLP-N01 | Medium | ⚠️50 | ✅78 | ⚠️70 | split | · | Copy/Cut exports unfiltered HTML to system clipboard |
| CLP-N02 | Medium | ⚠️50 | ⚠️58 | ✅95 | split | · | DropArea external drop never calls drop.accept() |
| CLP-N03 | Medium | ⚠️50 | ⚠️58 | ✅90 | split | · | DropArea external drop: URLs consumed preferentially — text silently lost |
| SWT-N01 | Medium | ✅60 | ✅78 | ✅95 | AGREE | · | OBS WebSocket Switch checked binding broken on first toggle |
| IMH-SYS | Medium | ⚠️40 | ⚠️58 | ⚠️65 | AGREE | · | Systemic absence of inputMethodHints on ALL TextFields (16 sites) |
| EKA-SYS | Low | ⚠️40 | ⚠️58 | ⚠️65 | AGREE | · | Systemic absence of EnterKeyAction on ALL TextFields (7 sites) |
| WINDOW-N01 | Medium | ⚠️50 | ⚠️58 | ✅85 | split | · | Projection windows not closed on main window close — orphaned on Linux |
| GSW-N01 | Medium | ⚠️45 | ⚠️58 | ✅90 | split | · | MarkersDrawer SwipeListItem navigates on swipe — gesture conflict on touch |
| GSW-N02 | Low | ❔45 | ❔39 | ✅85 | split | · | Flickable onDragStarted uses stale __iBackup after non-prompting drags |
| LVW-N01 | Low | ⚠️45 | ⚠️58 | ✅85 | split | · | InputsOverlay.qml ListView currentIndex: PointerSettings.States.Arrow — copy-paste error |
| META-N01 | Low | ⚠️45 | ⚠️58 | ✅95 | split | · | QMetaObject::invokeMethod return value unchecked — silent failure on WASM |
| LOG-N04 | Low | ❌70 | ✅78 | ✅90 | **CONFLICT** | · | qWarning("reloading") fires unconditionally — misleading when URL mismatches |
| LOG-N05 | Medium | ⚠️50 | ⚠️58 | ✅90 | split | · | Q_UNREACHABLE() in m_setGlobalShortcut() — UB in release on new enum value |
| LOG-N06 | Medium | ✅70 | ✅78 | ✅95 | AGREE | · | No error log when saveAs() write/flush fail — silent data loss |
| LOG-N07 | Medium | ✅55 | ⚠️58 | ✅95 | split | · | No error log in loadFromNetworkFinihed() — silent bad-data load |
| FONT-N01 | Medium | ⚠️45 | ❔39 | ✅95 | split | · | font.family: "Monospace" never resolves — no such font on any OS |
| FONT-N02 | Low | ✅65 | ⚠️58 | ✅95 | split | · | FontLoader id typo: westernSeriousSansfFont — stray 'f' in "Sans" |
| XML-N01 | Medium | ✅55 | ✅92 | ✅90 | AGREE | · | android:background="#303030" invalid on \<activity\> — silently ignored |
| CMAKE-N02 | Low | ✅55 | ✅78 | ✅95 | AGREE | · | INTERFACE_LINK_LIBRARIES on executable target — no-op |
| CMAKE-N03 | Medium | ⚠️50 | ❌76 | ✅85 | **CONFLICT** | · | qt_wrap_ui conflicts with global AUTOUIC — double UI processing |
| CMAKE-N04 | Medium | ✅55 | ✅78 | ✅90 | AGREE | · | Relative ../build path in install rules — out-of-tree build failure |
| SETUP-N01 | Medium | ❔40 | ❔39 | ✅95 | split | · | setup.sh uses windeployqt.exe (Qt 5) — should be windeployqt6.exe (Qt 6) |
| POP-N01 | Medium | ⚠️50 | ⚠️58 | ✅90 | split | · | ESC cascade missing dictionariesSheet — undismissable by keyboard |
| POP-N02 | Medium | ⚠️50 | ⚠️58 | ✅90 | split | · | ESC cascade missing customWordsSheet — undismissable by keyboard |
| POP-N03 | Medium | ⚠️50 | ⚠️58 | ✅85 | split | · | ESC cascade missing obsConfiguration — undismissable by keyboard despite alias |
| POP-N04 | Medium | ✅65 | ⚠️58 | ✅95 | split | · | CountdownConfiguration SpinBoxes use focus: true (JS label) instead of focus = true |
| RND-N01 | Low | ⚠️50 | ⚠️58 | ✅95 | split | · | forceQtTextRenderer dead on Apple platforms — unconditionally uses NativeRendering |
| RND-N02 | Low | ⚠️45 | ⚠️58 | ✅85 | split | · | Missing smooth: true on background Image — aliased upscale |
| RND-N03 | Low | ⚠️50 | ⚠️58 | ✅85 | split | · | Missing smooth: true on projection Image — aliased text on external displays |
| ST-N02 | Medium | ✅50 | ⚠️58 | ✅95 | split | · | Dead overlay.state PropertyChanges — overlay has no states array |
| CFG-N01 | Medium | ⚠️50 | ⚠️58 | ✅95 | split | · | Desktop MimeType incomplete — only text/html, missing text/plain and text/markdown |
| CFG-N02 | Low | ✅55 | ⚠️58 | ❔40 | split | · | v1.1.3 release date "2022-1-16" breaks chronological order — should be 2023-01-16 |
| CFG-N03 | Low | ✅60 | ⚠️58 | ✅95 | split | · | "fixedd" typo in v2.0.2 release description |
| TP-SYS | Medium | ⚠️40 | ⚠️58 | ⚠️70 | AGREE | · | Systemic absence of ToolTip on ~60+ controls across entire application |
| TP-N01 | Medium | ⚠️55 | ⚠️58 | ✅90 | split | · | "Error loading file..." used as document content, not placeholderText |
| WATCH-N01 | Medium | ⚠️50 | ✅78 | ✅95 | split | · | addPath() return never checked — silent watch failure |
| WATCH-N02 | Medium | ⚠️50 | ✅78 | ✅90 | split | · | removePath() return never checked — stale path causes double-watch |
| WATCH-N03 | Medium | ❔45 | ✅78 | ✅90 | split | · | Watcher not refreshed after fileChanged — stale inotify on Linux atomic saves |
| WATCH-N04 | Low | ⚠️45 | ✅78 | ✅85 | split | · | unblockFileWatcher() dereferences _fileSystemWatcher without null guard |
| MODEL-N01 | Medium | ✅60 | ✅78 | ✅90 | AGREE | · | MarkersModel::rowCount ignores parent.isValid() — returns full size for child probe |
| MODEL-N02 | Low | ✅55 | ⚠️58 | ✅85 | split | · | SessionModel::clearDataPoints lacks empty-model guard before beginRemoveRows |
| COERC-N01 | High | ❔45 | ✅84 | ❌85 | **CONFLICT** | · | parseInt("") → NaN state bootstrap — first toggle() bricks state machine |
| COERC-N02 | Medium | ✅55 | ✅78 | ✅95 | AGREE | · | Unvalidated string-to-number injects NaN into root.__opacity — all opacity dead |
| COERC-N03 | Low | ⚠️50 | ⚠️58 | ✅80 | split | · | real→int truncation in WindowDragger position compounds drift |
| QLOAD-N01 | Medium | ⚠️50 | ✅78 | ✅95 | split | · | InputsOverlay toggleButtonsOff() null-check bypass — crash on slow async Loaders |
| DETACH-N01 | Low | ⚠️40 | ⚠️58 | ✅75 | split | · | 4 non-const operator[] on QList in keySearch() — unnecessary implicit sharing detach |
| COLOR-CRIT-01 | High | ❔45 | ❔39 | ✅95 | split | · | selectionColor #333d9ef3 — alpha channel reversed (#AARRGGBB vs #RRGGBBAA), selection invisible |
| SYM-N01 | Low-Medium | ⚠️40 | ⚠️58 | ✅85 | split | · | 6 RTL/symmetry issues across PointerSettings, Find, PrompterView, Prompter, PrompterPage |
| CLIP-CRIT-01 | Critical | ✅85 | ✅84 | ✅95 | AGREE | · | Paste via toolbar button and File menu bypasses HTML sanitization |
| CLIP-N04 | Medium | ✅65 | ⚠️58 | ✅90 | split | · | Image-only clipboard paste — button enabled but does nothing |
| INT-N04 | Medium | ✅55 | ⚠️58 | ✅85 | split | · | OBS URL/Password fields disabled when WebSocket enabled — inverted logic |
| INT-N05 | Medium | ✅55 | ⚠️58 | ✅90 | split | · | PropertyChanges permanently destroys CheckBox checked bindings on PointerSettings tab switch |
| FMT-N01 | Medium | ✅50 | ✅78 | ✅95 | AGREE | · | Step Speed onAccepted displays 100x correct value |
| FMT-N02 | Medium | ✅50 | ✅78 | ✅95 | AGREE | · | Step Acceleration onAccepted — identical 100x display bug |
| PLAT-N04 | Medium | ✅65 | ✅78 | ✅90 | AGREE | · | "ipados" is not valid Qt.platform.os string — 18 dead guards across 5 files |
| PLAT-N05 | Low | ⚠️45 | ⚠️58 | ✅85 | split | · | Base main.qml fullScreenPlatform missing "wasm" (inconsistent with +windows) |
| WYS-N01 | Medium | ✅60 | ✅78 | ✅90 | AGREE | · | Internal drag-and-drop copy inserts HTML as plain text — tags become visible |
| WYS-N02 | Low | ✅70 | ⚠️58 | ✅85 | split | · | Default stylesheet CSS errors: valign:top (not a CSS property) and border:1pt (missing style) |
| QP-N01 | High | ✅65 | ⚠️58 | ✅95 | split | · | restartApplication() quits even when startDetached fails — app dies with no replacement |
| QP-N02 | Medium | ✅65 | ✅78 | ✅90 | AGREE | · | convert.waitForFinished() blocks GUI thread up to 30s during LibreOffice import |
| QP-N03 | Medium | ✅55 | ✅78 | ✅90 | AGREE | · | convert.exitCode() never checked — LibreOffice error output becomes document content |
| IMG-N02 | High | ✅60 | ✅84 | ✅90 | AGREE | · | insertHtmlAt() silent blocking HTTP load for img src URLs — UI freeze |
| TRN-N01 | Low | ✅55 | ✅78 | ✅90 | AGREE | · | Dead ternary: both branches return Qt.OpenHandCursor |
| A11Y-SYS | Medium | ⚠️45 | ⚠️58 | ✅85 | split | · | Systemic absence of Accessible properties — app invisible to screen readers |
| EVT-N13 | High | ❔45 | ⚠️58 | ✅95 | split | · | rewind()/fastForward() event undefined — winding state permanently locked after first use |
| ANM-N02 | Medium | ⚠️50 | ⚠️58 | ✅90 | split | · | Standby→Ready countdown opacity flash — PropertyChanges opacity:1 conflicts with dissolveIn |
| RESO-N01 | Medium | ⚠️45 | ⚠️48 | ✅95 | split | · | Editing font size not viewport-scaled — text nearly unreadable on 4K |
| RESO-N02 | Low | ⚠️40 | ⚠️48 | ✅80 | split | · | Scrollbar width 6dp-13dp — below minimum 44dp touch target |
| RESO-N03 | Low | ⚠️40 | ⚠️48 | ✅75 | split | · | Control spacing hardcoded 8dp — cramped on large displays |
| RESO-N04 | Low | ⚠️40 | ⚠️48 | ✅75 | split | · | Projection-window margins fixed 10dp/5dp — near-flush on large screens |
| RESO-N05 | Low | ⚠️40 | ⚠️48 | ✅75 | split | · | PointerSettings ListView height hardcoded 180dp — doesn't fill available space |
| RESO-N06 | Low | ⚠️40 | ⚠️48 | ✅80 | split | · | ReadRegionOverlay pointer margin 3dp — overlap with text at large fonts |
| STK-N01 | Critical | ✅85 | ✅92 | ✅95 | AGREE | · | Android projectionManager undefined — crash on "Performance tweaks" submenu |
| JSON-N01 | High | ✅65 | ✅84 | ✅95 | AGREE | · | OBS WebSocket Hello auth fields accessed without null guard — crash on auth-disabled |
| QW-N01 | Medium | ⚠️50 | ⚠️58 | ✅90 | split | · | Projection Window onClosing references cleared model — spurious runtime errors |
| QW-N02 | Medium | ⚠️55 | ⚠️58 | ✅85 | split | · | Stale QScreen reference in projection model — dangling after monitor hot-unplug |
| JS-N01 | Low | ✅50 | ⚠️58 | ✅70 | split | · | TIMERCLOCK getTimeString() — redundant .toString() on already-string — 54 allocs/sec |
| JS-N02 | Medium | ⚠️50 | ⚠️58 | ✅85 | split | · | markerCompare() per-frame JSON.stringify() over OBS marker — 60 allocs/sec |
| THM-SYS | High | ⚠️55 | ⚠️58 | ✅90 | split | · | Complete theme deadlock — 50+ Material.theme: Dark hardcoded, theme toggle commented out |
| HSCROLL-N01 | Medium | ⚠️50 | ⚠️58 | ✅95 | split | · | InputsOverlay Flickables use contentWidth: width instead of implicitWidth — horizontal overflow clipped |
| HSCROLL-N02 | Medium | ⚠️50 | ⚠️58 | ✅90 | split | · | Inner Flickables missing flickableDirection: VerticalFlick — conflict with parent horizontal ListView |
| COLOR-N08 | Medium | ⚠️45 | ⚠️58 | ✅90 | split | · | textBackground() returns invalid QColor for body/paragraph text |
| COLOR-N09 | Medium | ⚠️55 | ⚠️58 | ✅90 | split | · | acceptedColor binds transparent QColor on startup — initial text invisible |
| PP-N01 | Medium | ✅55 | ⚠️58 | ✅95 | split | · | Q_OS_APPLE is not a Qt macro — KGlobalAccel block compiles on all Unix including macOS |
| TRF-N01 | High | ⚠️50 | ⚠️58 | ✅95 | split | · | rightWidthAdjustmentBar drag.maximumX formula broken — drag collapses to single point |
| TOG-N01 | Medium | ⚠️50 | ⚠️58 | ✅85 | split | · | WheelSettingsOverlay useScrollAsDialButton — cross-path stale checked state |
| RPL-N01 | Medium | ❌55 | ❌76 | ✅95 | **CONFLICT** | · | 6 additional files missing QtQuick.Controls.Material import — ~65 controls unthemed |
| VIS-FB-N01 | Low | ⚠️50 | ⚠️58 | ✅90 | split | · | bookmarkListButton and searchButton missing checkable: true — no checked background |
| DEB-N01 | High | ✅55 | ✅84 | ✅95 | AGREE | · | libvulkan-dev (dev package) listed as Debian runtime dependency |
| DEB-N02 | High | ❔45 | ✅84 | ✅95 | split | · | qml6-module-qtcore is not a real Debian package — .deb uninstallable |
| DEB-N03 | High | ❔45 | ✅84 | ✅95 | split | · | qml6-module-qt-labs-platform doesn't exist for Qt 6 — .deb uninstallable |
| RPM-N01 | Medium | ✅50 | ⚠️58 | ✅90 | split | · | RPM dependencies entirely commented out — zero automatic dependency resolution |
| TS-N07 | Medium | ❔40 | ❔39 | ❔40 | AGREE | · | Wrong translations: Chinese "Undo"→"Open", "Bars"→"Toolbar"; French "Pointer Configuration"→"Prompter duration"; Korean "Line width"→"Line height" |
| META-N14 | Medium | ❔45 | ⚠️58 | ✅80 | split | · | ModernToolkit removed from AppStream spec — validation error |
| META-N15 | Medium | ⚠️45 | ⚠️58 | ✅90 | split | · | No StartupWMClass in desktop file — duplicate dock entries, missing icon |
| META-N16 | Low | ❔45 | ❔39 | ✅90 | split | · | README badges and links reference wrong repo Cuperino/QPrompt (should be QPrompt-Teleprompter) |
| META-N17 | Medium | ❔45 | ❔39 | ✅85 | split | · | README links to non-existent BUILD.md |
| AND-N08 | Medium | ✅60 | ✅78 | ✅95 | AGREE | · | Android saveAs() hardcodes isHtml=true — plain-text files saved with HTML markup |
| TMR-N05 | High | ❔45 | ❔39 | ✅90 | split | · | markerCompare() only fires on forward scroll — backward scroll + re-forward misses marker |
| TMR-N06 | Medium | ⚠️50 | ✅78 | ✅90 | split | · | Auto-reload Timer persists after network dialog close — background refetches |
| FONT-METRIC-01 | High | ❔40 | ❔39 | ✅90 | split | · | pixelSize used as line-height proxy — core scroll timing off by ~57% |
| FONT-METRIC-02 | Medium | ⚠️50 | ⚠️58 | ✅85 | split | · | FontLoader status never checked — font substitution silently fails |
| FONT-METRIC-03 | Low | ❔40 | ❔39 | ✅85 | split | · | fontFamily() returns resolved-family not requested-family — substitution invisible |
| STC-N01 | Medium | ✅55 | ⚠️58 | ✅90 | split | · | closeAll() destroys user's per-screen projection flip configuration |
| STC-N02 | Low | ⚠️45 | ⚠️58 | ✅85 | split | · | Find.qml close() doesn't reset replace-mode or regex-mode flags |
| STC-N03 | Medium | ❔45 | ⚠️58 | ✅90 | split | · | velocityIndicator.firstResetDone never cleared on dismiss — second activation broken |
| STC-N04 | Medium | ⚠️50 | ⚠️58 | ✅85 | split | · | Projection window CursorAutoHide not reset on close — cursor permanently hidden |
| STC-N05 | Low | ⚠️50 | ⚠️58 | ✅85 | split | · | cancel() doesn't call timer.stopTimer() — elapsed time persists across sessions |
| TB-N01 | Medium | ⚠️45 | ⚠️58 | ✅85 | split | · | toolbar toggle timers produce stale state on rapid clicks |
| TB-N02 | Medium | ⚠️45 | ⚠️58 | ✅90 | split | · | baseSpeedSlider/baseAccelerationSlider onMoved yanks focus to prompter instead of restoreFocus() |
| TB-N03 | Low | ⚠️45 | ⚠️58 | ✅70 | split | · | Collapsible toolbar rows animate height but adjacent rows snap — no y-position animation |
| TB-N04 | Medium | ⚠️50 | ⚠️58 | ✅85 | split | · | velocityDragArea accepts MiddleButton without propagateComposedEvents — scroll blocked |
| RESP-N01 | Low | ⚠️50 | ⚠️58 | ✅85 | split | · | minimumHeight: minimumWidth forces square aspect ratio — prevents landscape-strip windows |
| RESP-N02 | Medium | ❔45 | ⚠️58 | ✅90 | split | · | mobileOrSmallScreen threshold at 1231px activates on default 1220px launch |
| RESP-N03 | Low | ⚠️45 | ⚠️58 | ❌85 | split | · | +android/main.qml omits all size declarations — transient zero-size layout on startup |
| QT-LC-N01 | High | ❌70 | ❌76 | ✅95 | **CONFLICT** | · | QQmlFileSelector never instantiated — platform QML file selectors dead |
| TC-N01 | Low | ✅60 | ✅78 | ✅80 | AGREE | · | Image.source assigned boolean false instead of empty string |
| TC-N02 | Low | ⚠️45 | ⚠️58 | ✅80 | split | · | property color value assigned string expression — silent coercion |
| BLK-N01 | Medium | ✅70 | ⚠️58 | ✅85 | split | · | alignment() returns Qt::AlignCenter (includes vertical bit 0x0080) on null cursor |
| BLK-N02 | Medium | ✅55 | ⚠️58 | ✅90 | split | · | updateContents() fails to reset block formatting — stale formats contaminate new document |
| BLK-N03 | Medium | ✅60 | ⚠️58 | ✅90 | split | · | setLineHeight/setParagraphHeight apply document-wide — destroy per-block customization |
| SHT-N01 | Medium | ⚠️50 | ⚠️58 | ✅90 | split | · | markerToggle/namedMarkerToggle forwarded but never handled — dead hotkeys |
| SHT-N02 | Low | ⚠️45 | ⚠️58 | ⚠️75 | AGREE | · | Missing StandardKey.FullScreen on Android |
| LAZY-N01 | Low | ⚠️45 | ⚠️58 | ✅85 | split | · | namedMarkerConfiguration Loader double-loads KeyInputButton — first load wasted |
| LAZY-N02 | Medium | ⚠️50 | ⚠️58 | ⚠️60 | AGREE | · | InputsOverlay ObjectModel eagerly loads both tabs — hidden tab content loaded prematurely |
| LL-N01 | Medium | ⚠️50 | ⚠️58 | ✅80 | split | · | 10 EditorToolbar MouseArea/TextField width-depends-on-width binding loops |
| LL-N02 | Low | ✅55 | ✅78 | ❌95 | **CONFLICT** | · | ProgressIndicator stepSize divide-by-zero when prompter.height is 0 |
| SHDR-N02 | Medium | ✅60 | ⚠️58 | ❌85 | **CONFLICT** | · | id: shadow collides with property ShaderEffectSource shadow — ambiguous resolution in blur chain |
| KB-N01 | Medium | ⚠️45 | ⚠️58 | ✅85 | split | · | Find.qml: 9 toolbar buttons missing focusPolicy — keyboard-invisible |
| KB-N02 | Medium | ⚠️55 | ⚠️58 | ✅85 | split | · | InputsOverlay TabBar TabButtons have no focusPolicy + keyNavigationEnabled: false — keyboard dead |
| KB-N03 | Medium | ⚠️50 | ⚠️58 | ❌80 | split | · | +windows and +android ESC handler uses .focus instead of .activeFocus — wrong boolean |
| DRAG-N01 | Low | ⚠️45 | ⚠️58 | ✅80 | split | · | Image resize body drag: cursor shows OpenHandCursor until drag threshold exceeded |
| DRAG-N02 | Low | ✅55 | ⚠️58 | ✅80 | split | · | textDragArea has no cursorShape — no cursor feedback during text drag |
| SHAPE-N01 | Medium | ✅60 | ✅92 | ✅80 | AGREE | · | pointer_0.qml PathLine parent.width resolves to undefined (ShapePath has no width) — arrow collapsed |
| SHAPE-N02 | Medium | ❔45 | ❔39 | ✅85 | split | · | concentricCircles Shape uses parent-space coordinates in local space — circles off-center |
| FD-N01 | Medium | ⚠️55 | ⚠️58 | ✅90 | split | · | \|\| should be && in autoReload guard — user preference ignored for non-binary files |
| TBND-N01 | Medium | ⚠️50 | ⚠️58 | ✅70 | split | · | SpellHighlighter regex excludes combining diacritical marks — NFD text misspelled |
| TBND-N02 | Medium | ⚠️50 | ⚠️58 | ✅90 | split | · | All CJK text marked misspelled — ideographic characters not in Hunspell dictionaries |
| TBND-N03 | Low | ✅55 | ✅78 | ✅80 | AGREE | · | extendLastMarker() doesn't update Marker::length field — stale after appends |
| MIME-N01 | High | ⚠️45 | ⚠️58 | ❌95 | split | · | Temporary QMimeDatabase — QMimeType dangling on Qt 5 (undefined behavior) |
| MIME-N02 | Medium | ✅65 | ✅78 | ✅90 | AGREE | · | loadFromNetworkFinihed() ignores Content-Type header — all network content treated as HTML |
| MIME-N03 | Medium | ✅70 | ✅78 | ✅85 | AGREE | · | PDF/EPUB/MOBI/AZW MIME-detected but import is no-op — error text becomes content |
| TXT-FMT-N01 | Medium | ✅65 | ⚠️58 | ✅80 | split | · | setMarkerHref("") fails to clear QTextFormat::AnchorHref — stale href persists |
| SCR-N01 | High | ❔45 | ❔39 | ✅90 | split | · | Per-screen projection flip settings lost on restart — never serialized |
| SCR-N02 | Medium | ✅55 | ✅92 | ✅90 | AGREE | · | Duplicate entries in displayModel on first toggle — no clear() before setScreensModel() |
| SCR-N03 | Medium | ⚠️50 | ⚠️58 | ✅85 | split | · | No runtime screen plug/unplug handling — stale projection windows on disconnected screens |

## Divergences

Rows where the agents do not unanimously agree (CONFLICT first, then split).

### [CMAKE-N03] qt_wrap_ui conflicts with global AUTOUIC — double UI processing  ·  _CONFLICT_  ·  Medium
`src/CMakeLists.txt:43-46 vs CMakeLists.txt:45`
- **opus:** ⚠️ PARTIAL (50) — qt_wrap_ui + AUTOUIC may double-process .ui (CMakeLists.txt:43)
- **gpt:** ❌ FALSE (76) — AUTOUIC can coexist with qt_wrap_ui; duplicate processing is not shown (src/CMakeLists.txt:43)
- **deepseek:** ✅ LEGIT (85) — src/CMakeLists.txt:43-46 vs CMakeLists.txt:45: qt_wrap_ui + AUTOUIC both process systemfontchooserdialog.ui; double code generation — race in parallel builds

### [CMT-N04] Comment masks invalid enum bug — 2 - value produces out-of-range LayoutDirection  ·  _CONFLICT_  ·  Medium
`main.cpp:165`
- **opus:** ❌ FALSE (55) — claims invalid enum but 2=LayoutDirectionAuto is valid (dup TYP-02) (main.cpp:165)
- **gpt:** ❌ FALSE (76) — the value 2 is Qt::LayoutDirectionAuto not an invalid enum (src/main.cpp:165)
- **deepseek:** ✅ LEGIT (85) — 'Substract from 2' comment at main.cpp:165 masks that 2-0=2 is out-of-range LayoutDirection enum

### [COERC-N01] parseInt("") → NaN state bootstrap — first toggle() bricks state machine  ·  _CONFLICT_  ·  High
`Prompter.qml:448`
- **opus:** ❔ UNSURE (45) — parseInt('') NaN only if initial state unset; depends on default state (Prompter.qml:448)
- **gpt:** ✅ LEGIT (84) — parseInt("") -> NaN state bootstrap - first toggle() bricks state machine (src/prompter/Prompter.qml:448)
- **deepseek:** ❌ FALSE (85) — Prompter.qml:3088 explicitly sets state: Prompter.States.Editing(=0); parseInt('0')=0 not NaN; state is never empty string

### [DEF-N01] Flickable.flicking undefined in Qt 6 — wrong cursor during momentum scroll  ·  _CONFLICT_  ·  Medium
`Prompter.qml:1981,2024`
- **opus:** ❌ FALSE (65) — Flickable.flicking exists in Qt6; not undefined (Prompter.qml:1981)
- **gpt:** ❌ FALSE (76) — Flickable.flicking is a real Qt Quick property (src/prompter/Prompter.qml:1981)
- **deepseek:** ✅ LEGIT (90) — Prompter.qml:1981/2024: Flickable.flicking property renamed to moving in Qt6; resolves to undefined (falsy) — wrong cursor branch during momentum scroll

### [EDGE-08] Q_ASSERT as thread-safety guard — removed in release builds  ·  _CONFLICT_  ·  Medium
`src/appcontroller.cpp:36`
- **opus:** ❌ FALSE (80) — Q_ASSERT debug sanity check is normal (appcontroller.cpp:36)
- **gpt:** ❌ FALSE (76) — Q_ASSERT is only an invariant check after singleton creation (src/appcontroller.cpp:36)
- **deepseek:** ✅ LEGIT (75) — Q_ASSERT thread guard at appcontroller.cpp:36 removed in release builds; cross-thread singleton access silently corrupts — should be Q_CHECK_PTR or runtime assert

### [EVT-02] Zero inputMethodHints on any TextField — IME broken for CJK/Indic  ·  _CONFLICT_  ·  High
`Prompter.qml:936, PrompterPage.qml, EditorToolbar.qml (15+ TextFields)`
- **opus:** ❌ FALSE (55) — zero inputMethodHints = ImhNone = default; IME works, not broken (Prompter.qml:936)
- **gpt:** ⚠️ PARTIAL (58) — observed Zero inputMethodHints on any TextField - IME broken for CJK/Indic (src/prompter/Prompter.qml:936)
- **deepseek:** ✅ LEGIT (88) — zero inputMethodHints on all TextFields; CJK/Indic IME composition broken (Prompter.qml:936 EditorToolbar PrompterPage)

### [FINAL-06] CMAKE_OSX_ARCHITECTURES contains literal quotes — universal binary broken  ·  _CONFLICT_  ·  High
`CMakeLists.txt:418, src/CMakeLists.txt:29`
- **opus:** ✅ LEGIT (90) — set(CMAKE_OSX_ARCHITECTURES=) quote bug (CMakeLists.txt:418)
- **gpt:** ⚠️ PARTIAL (58) — observed CMAKE_OSX_ARCHITECTURES contains literal quotes - universal binary broken (CMakeLists.txt:418)
- **deepseek:** ❌ FALSE (95) — CMakeLists.txt:418 set() with double-quoted value strips quotes per CMake parser rules — value is x86_64;arm64 without literal quotes

### [IMP-N02] import QtWebSockets 1.10 — wrong version for Qt 6.5  ·  _CONFLICT_  ·  Critical
`src/prompter/Prompter.qml:80`
- **opus:** ❌ FALSE (65) — QtWebSockets 1.x import resolves on Qt6 target; OBS feature ships (Prompter.qml:80)
- **gpt:** ❌ FALSE (76) — QtWebSockets QML import version is not the project Qt version (src/prompter/Prompter.qml:80)
- **deepseek:** ✅ LEGIT (80) — Prompter.qml:80 imports QtWebSockets 1.10 — Qt6 registers WebSocket under 6.x only; 1.10 not registered per Qt6 module versioning

### [IMP-NEW-01] #include \<qnativeinterface.h\> doesn't exist — breaks Android build  ·  _CONFLICT_  ·  High
`documenthandler.cpp:83`
- **opus:** ❌ FALSE (65) — qnativeinterface.h exists in Qt6 QtCore; Android builds ship (documenthandler.cpp:83)
- **gpt:** ❌ FALSE (76) — qnativeinterface.h is a Qt 6 header (src/documenthandler.cpp:83)
- **deepseek:** ✅ LEGIT (90) — #include <qnativeinterface.h> at documenthandler.cpp:83 — header doesn't exist in Qt 5 or 6

### [LINK-N04] KF6::GlobalAccel find_package/link mismatch on Haiku  ·  _CONFLICT_  ·  Medium
`CMakeLists.txt:303-308, src/CMakeLists.txt:446-460`
- **opus:** ❔ UNSURE (45) — KF6::GlobalAccel Haiku find/link mismatch; domain (CMakeLists.txt:303)
- **gpt:** ✅ LEGIT (78) — KF6::GlobalAccel findpackage/link mismatch on Haiku (CMakeLists.txt:303)
- **deepseek:** ❌ FALSE (85) — CMakeLists.txt:242-247 already finds KF6::GlobalAccel for non-Win/Apple/Android/WASM which includes Haiku; Haiku-specific block (304-312) adds IconThemes only but GlobalAccel already resolved

### [LL-N02] ProgressIndicator stepSize divide-by-zero when prompter.height is 0  ·  _CONFLICT_  ·  Low
`ProgressIndicator.qml:35`
- **opus:** ✅ LEGIT (55) — stepSize divide-by-zero when prompter.height=0 (ProgressIndicator.qml:35)
- **gpt:** ✅ LEGIT (78) — ProgressIndicator stepSize divide-by-zero when prompter.height is 0 (src/prompter/ProgressIndicator.qml:35)
- **deepseek:** ❌ FALSE (95) — stepSize=prompter.height/(4*(editor.height+...)); prompter.height=0->stepSize=0 not division by zero; denominator uses editor.height

### [LOAD-N02] reset() emits 12 NOTIFY signals when open() fails but exists() succeeds  ·  _CONFLICT_  ·  Low
`documenthandler.cpp:1017-1018`
- **opus:** ⚠️ PARTIAL (50) — reset() emits ~12 signals when open fails after exists() (documenthandler.cpp:1017)
- **gpt:** ✅ LEGIT (78) — reset() emits 12 NOTIFY signals when open() fails but exists() succeeds (src/documenthandler.cpp:1017)
- **deepseek:** ❌ FALSE (75) — reset() is inside if(file.open()) block; not called when open fails (documenthandler.cpp:1017-1018)

### [LOG-N04] qWarning("reloading") fires unconditionally — misleading when URL mismatches  ·  _CONFLICT_  ·  Low
`documenthandler.cpp:862`
- **opus:** ❌ FALSE (70) — qWarning('reloading') is inside if(url==m_fileUrl), not unconditional (documenthandler.cpp:862)
- **gpt:** ✅ LEGIT (78) — qWarning("reloading") fires unconditionally - misleading when URL mismatches (src/documenthandler.cpp:862)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:862: qWarning('reloading') fires at top of reload() before url==m_fileUrl check at line 861; incorrectly claims reload on URL mismatch

### [PLAT-N01] qmlutil.hpp incorrectly excludes QNX from QProcess — run()/restartApplication() silently no-op  ·  _CONFLICT_  ·  Medium
`qmlutil.hpp:35,86,99`
- **opus:** ⚠️ PARTIAL (45) — qmlutil excludes QNX from QProcess; exotic (qmlutil.hpp:35)
- **gpt:** ✅ LEGIT (78) — qmlutil.hpp incorrectly excludes QNX from QProcess - run()/restartApplication() silently no-op (src/qmlutil.hpp:35)
- **deepseek:** ❌ FALSE (85) — QNX NOT excluded from QProcess guard at line 35; QProcess included for QNX (qmlutil.hpp:35)

### [PLAT-N02] documenthandler.cpp incorrectly excludes QNX from import() — LibreOffice broken on QNX  ·  _CONFLICT_  ·  Medium
`documenthandler.h:330, documenthandler.cpp:964,1012,1043`
- **opus:** ❔ UNSURE (40) — import() guard does NOT exclude QNX; LibreOffice-on-QNX claim ambiguous (documenthandler.cpp:964)
- **gpt:** ✅ LEGIT (78) — documenthandler.cpp incorrectly excludes QNX from import() - LibreOffice broken on QNX (src/documenthandler.h:330)
- **deepseek:** ❌ FALSE (85) — QNX NOT in exclusion guard at line 964; import function included for QNX (documenthandler.cpp:964)

### [QPROP-N02] comesFromNetwork Q_PROPERTY missing WRITE clause  ·  _CONFLICT_  ·  Medium
`documenthandler.h:121`
- **opus:** ❌ FALSE (50) — comesFromNetwork is intentionally read-only; WRITE not needed (documenthandler.h:121)
- **gpt:** ❌ FALSE (76) — comesFromNetwork is exposed read-only; no WRITE is required (src/documenthandler.h:121)
- **deepseek:** ✅ LEGIT (95) — documenthandler.h:121: Q_PROPERTY comesFromNetwork missing WRITE; setDocumentComesFromNetwork() exists (called at cpp:896) but QML property system sees read-only

### [QT-LC-N01] QQmlFileSelector never instantiated — platform QML file selectors dead  ·  _CONFLICT_  ·  High
`main.cpp:33`
- **opus:** ❌ FALSE (70) — QQmlApplicationEngine auto-installs a file selector; +variants demonstrably load (main.cpp:33)
- **gpt:** ❌ FALSE (76) — QQmlApplicationEngine applies file selectors for +android/+windows (src/main.cpp:33)
- **deepseek:** ✅ LEGIT (95) — main.cpp:33: #include <QQmlFileSelector> present but never instantiated/attached; +windows/+android variants dead; base main.qml loads on all platforms

### [R2-CMAKE-01] sphinx_add_docs silently ignores all keyword arguments due to empty cmake_parse_arguments prefix  ·  _CONFLICT_  ·  Critical
`cmake/FindSphinx.cmake:54-56`
- **opus:** ❌ FALSE (80) — empty prefix yields _ALL matching access (FindSphinx.cmake:55)
- **gpt:** ❌ FALSE (76) — empty cmake_parse_arguments prefix intentionally creates _ALL etc. (cmake/FindSphinx.cmake:54)
- **deepseek:** ✅ LEGIT (90) — cmake_parse_arguments empty prefix '' at FindSphinx.cmake:54; all accesses use _ prefixed vars; ALL/BUILDER etc parsed to unprefixed name — all args silently ignored

### [R2-GH-01] Q_UNREACHABLE reachable when only QHotkey available on Wayland  ·  _CONFLICT_  ·  High
`src/globalhotkeys.cpp:514`
- **opus:** ❌ FALSE (80) — Use_GlobalAccel defined on all Unix -> unreachable (globalhotkeys.cpp:514)
- **gpt:** ❌ FALSE (76) — Use_GlobalAccel is defined, so the claimed QHotkey-only branch is not built (src/globalhotkeys.cpp:514)
- **deepseek:** ✅ LEGIT (80) — Q_UNREACHABLE at globalhotkeys.cpp:514 reachable when QHotkey_FOUND defined Use_GlobalAccel not defined platform is non-KDE Wayland; confirmed fallthrough path

### [R2-PTR-01] Type mismatch: textVerticalOffset declared int but fed a real  ·  _CONFLICT_  ·  Medium
`src/prompter/pointers/pointer_1.qml:33`
- **opus:** ❌ FALSE (75) — int gets scaled readRegion.height*offset/2 not raw slider (pointer_1.qml:33)
- **gpt:** ❌ FALSE (76) — value is scaled before assignment; int truncation is minor (src/prompter/pointers/pointer_1.qml:33)
- **deepseek:** ✅ LEGIT (80) — textVerticalOffset declared int at pointer_1.qml:33; fed real from slider -1.0..1.0 step 0.01; truncation means only +/-1 survive — confirmed type mismatch

### [R2-PTR-02] Type mismatch: imageVerticalOffset declared int but fed a real  ·  _CONFLICT_  ·  Medium
`src/prompter/pointers/pointer_2.qml:28`
- **opus:** ❌ FALSE (75) — same scaled-value reasoning (pointer_2.qml:28)
- **gpt:** ❌ FALSE (76) — value is scaled before assignment; int truncation is minor (src/prompter/pointers/pointer_2.qml:28)
- **deepseek:** ✅ LEGIT (80) — imageVerticalOffset same pattern at pointer_2.qml:28; int truncation from real slider — confirmed type mismatch

### [R3-DOC-02] Unbalanced edit block in setLineHeight/setParagraphHeight  ·  _CONFLICT_  ·  Critical
`src/documenthandler.cpp:1596-1601, 1610-1615`
- **opus:** ❌ FALSE (85) — joinPreviousEditBlock balances endEditBlock; no crash
- **gpt:** ❌ FALSE (76) — joinPreviousEditBlock is later closed by endEditBlock (src/documenthandler.cpp:1596)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:1596/1610 cursor.joinPreviousEditBlock() is no-op without active edit block; endEditBlock() without matching beginEditBlock() — unbalanced

### [R3-MAIN-01] Command-line positional argument description/syntax swapped  ·  _CONFLICT_  ·  Medium
`src/main.cpp:158`
- **opus:** ❌ FALSE (75) — not swapped args; malformed QLatin1String(char*,char*) (main.cpp:158)
- **gpt:** ✅ LEGIT (78) — Command-line positional argument description/syntax swapped (src/main.cpp:158)
- **deepseek:** ✅ LEGIT (85) — main.cpp:158 addPositionalArgument signature is(name description syntax); passes('source' 'file' 'File to copy.') — description and syntax swapped

### [R3-SIG-03] IosSaveDialog accepted/rejected signals declared but never emitted  ·  _CONFLICT_  ·  Medium
`src/iossavedialog.h:44-45, iossavedialog.cpp:44-47`
- **opus:** ❌ FALSE (90) — accepted/rejected emitted in iossavedialog.mm:43,51
- **gpt:** ❌ FALSE (90) — iOS .mm emits accepted and rejected (src/iossavedialog.h:44)
- **deepseek:** ✅ LEGIT (75) — iossavedialog.cpp:44-47 saveDocument no-op with zero emits of accepted()/rejected() signals — iOS save-as flow broken

### [R3-SPL-03] removeCustomWord() silently discards all addWord() additions  ·  _CONFLICT_  ·  Medium
`src/spellchecker.cpp:134-140 vs 338-344`
- **opus:** ❌ FALSE (80) — addWord dead/uncalled; addCustomWord persists correctly (spellchecker.cpp:134)
- **gpt:** ❌ FALSE (76) — addWord is the transient API; persisted custom words use addCustomWord (src/spellchecker.cpp:134)
- **deepseek:** ✅ LEGIT (90) — spellchecker.cpp:134-140 addWord() calls hunspell->add() but never appends to m_customWords; spellchecker.cpp:338-344 removeCustomWord() reloads losing those words

### [R4-EVT-01] Missing braces on if/else — syntax error in alignRightButton  ·  _CONFLICT_  ·  Critical
`src/kirigami_ui/EditorToolbar.qml:755-758`
- **opus:** ❌ FALSE (85) — brace-less if/else is valid JS (EditorToolbar.qml:755)
- **gpt:** ❌ FALSE (76) — JavaScript if/else without braces is syntactically valid (src/kirigami_ui/EditorToolbar.qml:755)
- **deepseek:** ✅ LEGIT (95) — EditorToolbar.qml:755-758 if without braces controls only next statement; else orphaned — JS syntax error prevents QML load

### [R4-QTV-01] QtQuick 2.13 import does not exist in Qt 6.5  ·  _CONFLICT_  ·  Critical
`src/prompter/ProjectionsManager.qml:22`
- **opus:** ❌ FALSE (90) — QtQuick 2.13 valid on Qt 6; target 6.8.2
- **gpt:** ❌ FALSE (76) — QtQuick 2.x import remains valid on Qt 6.8.2 (src/prompter/ProjectionsManager.qml:22)
- **deepseek:** ✅ LEGIT (95) — ProjectionsManager.qml:22 imports QtQuick 2.13 — Qt 6 registers QtQuick only as 6.x and 2.15 backward compat; 2.13 not registered

### [R4-ROOT-03] ESC global shortcut skips single-layer pages — can't dismiss with keyboard  ·  _CONFLICT_  ·  Medium
`src/kirigami_ui/main.qml:481`
- **opus:** ❌ FALSE (80) — layers.depth>1 is correct Kirigami idiom (main.qml:481)
- **gpt:** ❌ FALSE (76) — layers.depth > 1 is the expected Kirigami layer-pop guard (src/kirigami_ui/main.qml:481)
- **deepseek:** ✅ LEGIT (90) — main.qml:481 checks layers.depth>1 before clear(); single layer(depth===1) skipped — ESC doesn't dismiss About/Paths/Remote pages

### [R4-SHD-01] Duplicate class implementation between .cpp and .mm — ODR risk  ·  _CONFLICT_  ·  Medium
`src/shakedetector.cpp:24-43 and shakedetector.mm:45-64`
- **opus:** ❌ FALSE (80) — one TU per platform; no ODR (src/CMakeLists.txt:94)
- **gpt:** ❌ FALSE (76) — CMake selects either .cpp or .mm per platform, not both (src/shakedetector.cpp:24)
- **deepseek:** ✅ LEGIT (90) — shakedetector.cpp:24-43 and shakedetector.mm:45-64 duplicate constructor/instance/create/s_instance — CMake compiles one per platform but maintenance hazard

### [RAII-N03] QProcess orphan — child process detached on waitForFinished() timeout  ·  _CONFLICT_  ·  Medium
`documenthandler.cpp:1083-1089`
- **opus:** ⚠️ PARTIAL (50) — QProcess child may linger if waitForFinished times out (documenthandler.cpp:1083)
- **gpt:** ✅ LEGIT (78) — QProcess orphan - child process detached on waitForFinished() timeout (src/documenthandler.cpp:1083)
- **deepseek:** ❌ FALSE (70) — QProcess stack object destructor calls close()/kill() in Qt6; no orphan on timeout (documenthandler.cpp:1083-1089)

### [RPL-N01] 6 additional files missing QtQuick.Controls.Material import — ~65 controls unthemed  ·  _CONFLICT_  ·  Medium
`Find.qml, PrompterView.qml, Prompter.qml, PrompterPage.qml, EditorToolbar.qml, InputsOverlay.qml`
- **opus:** ❌ FALSE (55) — Material provided module-wide via qt_add_qml_module IMPORTS (dup FINAL-02)
- **gpt:** ❌ FALSE (76) — Material is supplied by module imports, not each individual QML file (src/prompter/Find.qml:1)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml/Find.qml/EditorToolbar.qml all use Material.theme without importing QtQuick.Controls.Material; ~65 controls unthemed

### [SHADOW-N03] id: stopwatch shadows property bool stopwatch — timersEnabled always true  ·  _CONFLICT_  ·  High
`TimerClock.qml:38,122,100`
- **opus:** ✅ LEGIT (70) — id: stopwatch (Item) shadows property bool stopwatch -> timersEnabled always true (TimerClock.qml:38)
- **gpt:** ✅ LEGIT (84) — id: stopwatch shadows property bool stopwatch - timersEnabled always true (src/prompter/TimerClock.qml:38)
- **deepseek:** ❌ FALSE (75) — property bool stopwatch resolves before child Item id; timersEnabled correctly depends on property (TimerClock.qml:38 100 122)

### [SHDR-N02] id: shadow collides with property ShaderEffectSource shadow — ambiguous resolution in blur chain  ·  _CONFLICT_  ·  Medium
`Prompter.qml:746,752,754,759,762`
- **opus:** ✅ LEGIT (60) — id: shadow collides with property ShaderEffectSource shadow (Prompter.qml:746)
- **gpt:** ⚠️ PARTIAL (58) — observed id: shadow collides with property ShaderEffectSource shadow - ambiguous resolution in blur chai (src/prompter/Prompter.qml:746)
- **deepseek:** ❌ FALSE (85) — id:shadow takes priority over property shadow in QML scope; shadow.source correctly resolves to prompterShadowSource not self-ref

### [TYP-01] Dangling pointer from temporary std::string in SpellChecker::loadOne  ·  _CONFLICT_  ·  High
`src/spellchecker.cpp:154-155`
- **opus:** ❌ FALSE (80) — get_dict_encoding returns const std::string& -> not dangling (spellchecker.cpp:154)
- **gpt:** ❔ UNSURE (39) — Hunspell header is not in-tree, so return lifetime cannot be proven here (src/spellchecker.cpp:154)
- **deepseek:** ✅ LEGIT (95) — get_dict_encoding().c_str() at spellchecker.cpp:154 returns temp std::string; enc dangles at semicolon; QByteArray(enc) reads freed memory — UB confirmed

### [TYP-02] Invalid Qt::LayoutDirection enum value cast  ·  _CONFLICT_  ·  Medium
`src/main.cpp:166`
- **opus:** ❌ FALSE (90) — LayoutDirectionAuto=2 valid; no UB (main.cpp:166)
- **gpt:** ❌ FALSE (76) — 2 maps to Qt layout auto, not an out-of-range enum value (src/main.cpp:166)
- **deepseek:** ✅ LEGIT (90) — static_cast<Qt::LayoutDirection>(2-setting) at main.cpp:166; when setting=0 -> 2 is not valid enum value (only 0=LeftToRight 1=RightToLeft) — UB

### [W10-HTK-01] autoRepeat=true for ALL QHotkey shortcuts — non-velocity actions broken when held  ·  _CONFLICT_  ·  Critical
`src/globalhotkeys.cpp:1116`
- **opus:** ❌ FALSE (70) — 3rd arg of QHotkey::setShortcut is autoRegister, not autoRepeat (globalhotkeys.cpp:1116)
- **gpt:** ❌ FALSE (76) — third QHotkey setShortcut argument is autoRegister, not autoRepeat (src/globalhotkeys.cpp:1116)
- **deepseek:** ✅ LEGIT (92) — autoRepeat=true unconditional; toggle-type actions flood on hold rapid state flips (globalhotkeys.cpp:1116)

### [A11Y-SYS] Systemic absence of Accessible properties — app invisible to screen readers  ·  _SPLIT_  ·  Medium
`All .qml files`
- **opus:** ⚠️ PARTIAL (45) — systemic absence of Accessible properties; real a11y gap
- **gpt:** ⚠️ PARTIAL (58) — observed Systemic absence of Accessible properties - app invisible to screen readers (src/kirigami_ui/main.qml:1)
- **deepseek:** ✅ LEGIT (85) — Zero Accessible.name/description/role in Prompter.qml and EditorToolbar.qml; no screen reader support across codebase

### [ACT-N05] +windows main.qml Controls Settings submenu missing OBS Settings action  ·  _SPLIT_  ·  Medium
`+windows/main.qml vs main.qml:261-270`
- **opus:** ❔ UNSURE (45) — +windows Controls submenu missing OBS Settings action; menu-specific (main.qml:261)
- **gpt:** ⚠️ PARTIAL (58) — observed +windows main.qml Controls Settings submenu missing OBS Settings action (src/kirigami_ui/main.qml:261)
- **deepseek:** ⚠️ PARTIAL (45) — missing OBS Settings action in +windows may be intentional per-platform feature gating

### [ACT-N07] namedBookmarkButton: checkable button opens dialog — stale indicator after first click  ·  _SPLIT_  ·  Medium
`EditorToolbar.qml:225-236`
- **opus:** ✅ LEGIT (60) — namedBookmarkButton checkable opens dialog -> stale indicator (R2-EDT-03 family) (EditorToolbar.qml:225)
- **gpt:** ⚠️ PARTIAL (58) — observed namedBookmarkButton: checkable button opens dialog - stale indicator after first click (src/kirigami_ui/EditorToolbar.qml:225)
- **deepseek:** ✅ LEGIT (65) — checkable button opens dialog instead of toggling; checked binding desyncs after first click (EditorToolbar.qml:225-236)

### [ACT-N08] All checkable Labs.MenuItems inherit R2-EDT-03 binding-break pattern  ·  _SPLIT_  ·  Medium (masked — Labs.MenuBar dead per IMP-N01)
`main.qml:617-922`
- **opus:** ✅ LEGIT (55) — checkable Labs.MenuItems inherit checked-binding-break (R2-EDT-03 family) (main.qml:617)
- **gpt:** ⚠️ PARTIAL (58) — observed All checkable Labs.MenuItems inherit R2-EDT-03 binding-break pattern (src/kirigami_ui/main.qml:617)
- **deepseek:** ⚠️ PARTIAL (50) — claims Labs.MenuBar binding-break pattern; Labs.MenuBar already dead per IMP-N01 (main.qml:617-922)

### [AND-HIGH-01] Android back button doesn't dismiss overlays/drawers before close  ·  _SPLIT_  ·  High
`+android/main.qml:144-150, PrompterPage.qml:64`
- **opus:** ⚠️ PARTIAL (50) — Android back button overlay-dismissal claim; domain (main.qml:144)
- **gpt:** ⚠️ PARTIAL (58) — observed Android back button doesn't dismiss overlays/drawers before close (src/kirigami_ui/+android/main.qml:144)
- **deepseek:** ✅ LEGIT (80) — +android/main.qml:144-150: onClosing only handles save dialog (modified check); ESC dismiss cascades (layers->drawers->overlays->find) absent from back button — cannot dismiss overlays

### [AND-MED-01] Missing intent-filter for opening files from other apps  ·  _SPLIT_  ·  Medium
`AndroidManifest.xml:29-32`
- **opus:** ⚠️ PARTIAL (45) — missing intent-filter for opening files (AndroidManifest.xml:29)
- **gpt:** ⚠️ PARTIAL (58) — observed Missing intent-filter for opening files from other apps (android/AndroidManifest.xml:29)
- **deepseek:** ✅ LEGIT (95) — AndroidManifest.xml:29-32: only LAUNCHER intent-filter; no VIEW filter for text/html or text/plain — cannot open .html scripts from file managers/email/downloads

### [AND-MFT-01] FileProvider resource @xml/qtprovider_paths — file named filepaths.xml  ·  _SPLIT_  ·  Medium (latent)
`AndroidManifest.xml:43 vs res/xml/filepaths.xml`
- **opus:** ⚠️ PARTIAL (45) — FileProvider @xml/qtprovider_paths vs filepaths.xml; needs res check (AndroidManifest.xml:43)
- **gpt:** ⚠️ PARTIAL (58) — observed FileProvider resource @xml/qtproviderpaths - file named filepaths.xml (android/AndroidManifest.xml:43)
- **deepseek:** ✅ LEGIT (85) — commented FileProvider refs @xml/qtprovider_paths but actual file is filepaths.xml; resource-not-found if activated (AndroidManifest.xml:43)

### [AND-RES-01] Invalid android:scaleType on bitmap element  ·  _SPLIT_  ·  Medium
`android/res/drawable/splash.xml:7`
- **opus:** ⚠️ PARTIAL (45) — invalid android:scaleType on bitmap; needs res check (splash.xml:7)
- **gpt:** ⚠️ PARTIAL (58) — observed Invalid android:scaleType on bitmap element (android/res/drawable/splash.xml:7)
- **deepseek:** ✅ LEGIT (90) — android:scaleType is ImageView attribute not valid on <bitmap> drawable; AAPT2 error (android/res/drawable/splash.xml:7)

### [ANM-N02] Standby→Ready countdown opacity flash — PropertyChanges opacity:1 conflicts with dissolveIn  ·  _SPLIT_  ·  Medium
`Countdown.qml:265-276`
- **opus:** ⚠️ PARTIAL (50) — Standby->Ready opacity PropertyChanges flash (Countdown.qml:265)
- **gpt:** ⚠️ PARTIAL (58) — observed Standby->Ready countdown opacity flash - PropertyChanges opacity:1 conflicts with dissolveIn (src/prompter/Countdown.qml:265)
- **deepseek:** ✅ LEGIT (90) — Countdown.qml:265-276: Ready state sets opacity:1 AND starts dissolveIn(0->1); PropertyChanges applied first causes visible 1->0->1 flash

### [API-N01] setAlignment() missing null-cursor guard — crash risk with no document  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:557-558`
- **opus:** ⚠️ PARTIAL (50) — setAlignment no null guard; null-cursor ops are Qt no-ops, crash unlikely (documenthandler.cpp:557)
- **gpt:** ✅ LEGIT (78) — setAlignment() missing null-cursor guard - crash risk with no document (src/documenthandler.cpp:557)
- **deepseek:** ✅ LEGIT (65) — setAlignment lacks null-cursor guard unlike alignment() getter (documenthandler.cpp:557-558)

### [API-N03] CursorAutoHide.qml unconditionally dereferences pageStack.currentItem.prompter  ·  _SPLIT_  ·  Medium
`CursorAutoHide.qml:31`
- **opus:** ⚠️ PARTIAL (50) — CursorAutoHide derefs pageStack.currentItem.prompter (R4-EVT-03 family) (CursorAutoHide.qml:31)
- **gpt:** ✅ LEGIT (78) — CursorAutoHide.qml unconditionally dereferences pageStack.currentItem.prompter (src/prompter/CursorAutoHide.qml:31)
- **deepseek:** ✅ LEGIT (75) — unconditional deref of pageStack.currentItem.prompter without null guard (CursorAutoHide.qml:31)

### [API-N04] setMarker(bool) misleadingly named — sets regular marker, not any marker  ·  _SPLIT_  ·  Low
`documenthandler.h:123,212`
- **opus:** ⚠️ PARTIAL (35) — setMarker(bool) naming; cosmetic (documenthandler.h:123)
- **gpt:** ✅ LEGIT (78) — setMarker(bool) misleadingly named - sets regular marker, not any marker (src/documenthandler.h:123)
- **deepseek:** ✅ LEGIT (65) — setMarker(bool) only toggles regular marker despite generic name (documenthandler.h:123 212)

### [API-N05] fileName()/fileType() return fabricated defaults — can't distinguish "no file" from "untitled.html"  ·  _SPLIT_  ·  Low
`documenthandler.cpp:838-850`
- **opus:** ⚠️ PARTIAL (50) — fileName/fileType return 'untitled.html' default; can't signal no-file (documenthandler.cpp:838)
- **gpt:** ✅ LEGIT (78) — fileName()/fileType() return fabricated defaults - can't distinguish "no file" from "untitled.html" (src/documenthandler.cpp:838)
- **deepseek:** ✅ LEGIT (70) — fileName returns 'untitled.html' default; no way to distinguish no-file state (documenthandler.cpp:838-843)

### [API-N06] SystemFontChooserDialog::show() calls setText() on same label twice — dead code  ·  _SPLIT_  ·  Low
`systemfontchooserdialog.cpp:55-56`
- **opus:** ✅ LEGIT (80) — setText called twice; dead duplicate (dup R2-FONT-02) (systemfontchooserdialog.cpp:55)
- **gpt:** ⚠️ PARTIAL (58) — observed SystemFontChooserDialog::show() calls setText() on same label twice - dead code (src/systemfontchooserdialog.cpp:55)
- **deepseek:** ✅ LEGIT (80) — setText called twice on same label consecutively; dead duplicate (systemfontchooserdialog.cpp:55-56)

### [AR-01] PrompterView.qml:53-58 Rotation debug feature clips on extreme aspect ratios  ·  _SPLIT_  ·  Low
`PrompterView.qml:53-58`
- **opus:** ⚠️ PARTIAL (45) — rotation debug feature clips on extreme aspect (PrompterView.qml:53)
- **gpt:** ✅ LEGIT (78) — PrompterView.qml:53-58 Rotation debug feature clips on extreme aspect ratios (src/prompter/PrompterView.qml:53)
- **deepseek:** ✅ LEGIT (75) — Rotation debug at PrompterView.qml:53 wraps at angles — clips on ultrawide/tablet aspect ratios

### [ARC-01] Velocity physics engine entirely in QML (~20 readonly property bindings)  ·  _SPLIT_  ·  
`Prompter.qml:113-129`
- **opus:** ⚠️ PARTIAL (35) — velocity physics in QML; architectural (Prompter.qml:113)
- **gpt:** ⚠️ PARTIAL (48) — maintainability issue observed, but no direct runtime bug shown (src/prompter/Prompter.qml:113)
- **deepseek:** ❌ FALSE (50) — architectural observation; readonly property bindings are a valid QML design pattern

### [ARC-02] Arc-03 Search/replace state machine fully in QML (50+ lines)  ·  _SPLIT_  ·  
`Find.qml:112-161`
- **opus:** ⚠️ PARTIAL (35) — search state machine in QML; architectural (Find.qml:112)
- **gpt:** ⚠️ PARTIAL (48) — maintainability issue observed, but no direct runtime bug shown (src/prompter/Find.qml:112)
- **deepseek:** ❌ FALSE (50) — architectural observation; state machine in QML is a valid Qt design pattern

### [ARC-03] OBS WebSocket v5 protocol in QML — opcode dispatch, auth, subscription  ·  _SPLIT_  ·  
`Prompter.qml:366-388`
- **opus:** ⚠️ PARTIAL (35) — OBS WS protocol in QML; architectural (Prompter.qml:366)
- **gpt:** ⚠️ PARTIAL (48) — maintainability issue observed, but no direct runtime bug shown (src/prompter/Prompter.qml:366)
- **deepseek:** ❌ FALSE (50) — architectural observation; WebSocket protocol in QML is a valid Qt design pattern

### [ARC-04] DocumentHandler is 2295-line god class spanning file I/O, network, HTML filtering, markers, spellcheck, drag-drop, images, search, undo, clipboard, sleep prevention, font dialog  ·  _SPLIT_  ·  
`documenthandler.cpp (2295 lines)`
- **opus:** ⚠️ PARTIAL (40) — DocumentHandler god-class; architectural/subjective
- **gpt:** ⚠️ PARTIAL (48) — maintainability issue observed, but no direct runtime bug shown (src/documenthandler.cpp:1)
- **deepseek:** ❌ FALSE (50) — architectural observation; large class is maintainability concern not a code defect

### [ARC-05] Prompter.qml is 3139-line god component spanning velocity, state machine, keyboard, WebSocket, markers, spellcheck UI, file dialogs, WYSIWYG toggle, shadows  ·  _SPLIT_  ·  
`Prompter.qml (3139 lines)`
- **opus:** ⚠️ PARTIAL (35) — Prompter.qml 3139-line god component; architectural
- **gpt:** ⚠️ PARTIAL (48) — maintainability issue observed, but no direct runtime bug shown (src/prompter/Prompter.qml:1)
- **deepseek:** ❌ FALSE (50) — architectural observation; large QML component is maintainability concern not defect

### [ARC-06] qmlutil.hpp is utility grab-bag with 10+ unrelated functions  ·  _SPLIT_  ·  
`qmlutil.hpp (184 lines)`
- **opus:** ⚠️ PARTIAL (35) — qmlutil grab-bag; architectural
- **gpt:** ⚠️ PARTIAL (48) — maintainability issue observed, but no direct runtime bug shown (src/qmlutil.hpp:1)
- **deepseek:** ❌ FALSE (50) — architectural observation; utility grab-bag is style concern not code defect

### [BIND-N01] contentWidth undefined for Shape/Image pointer types — transform origin silently wrong  ·  _SPLIT_  ·  Low
`ReadRegionOverlay.qml:396`
- **opus:** ⚠️ PARTIAL (50) — contentWidth undefined for Shape/Image pointer (R4-ROV-03 family) (ReadRegionOverlay.qml:396)
- **gpt:** ✅ LEGIT (92) — contentWidth undefined for Shape/Image pointer types - transform origin silently wrong (src/prompter/ReadRegionOverlay.qml:396)
- **deepseek:** ✅ LEGIT (65) — contentWidth undefined for Shape/Image pointer types; transform origin silently wrong (ReadRegionOverlay.qml:396)

### [BLK-N01] alignment() returns Qt::AlignCenter (includes vertical bit 0x0080) on null cursor  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:549`
- **opus:** ✅ LEGIT (70) — null-cursor returns Qt::AlignCenter incl vertical bit 0x80 (documenthandler.cpp:549)
- **gpt:** ⚠️ PARTIAL (58) — observed alignment() returns Qt::AlignCenter (includes vertical bit 0x0080) on null cursor (src/documenthandler.cpp:549)
- **deepseek:** ✅ LEGIT (85) — documenthandler.cpp:549: alignment() returns Qt::AlignCenter(AlignHCenter|AlignVCenter) on null cursor; AlignVCenter meaningless for blocks

### [BLK-N02] updateContents() fails to reset block formatting — stale formats contaminate new document  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1104-1122`
- **opus:** ✅ LEGIT (55) — updateContents doesn't reset block format; stale formats can persist (documenthandler.cpp:1104)
- **gpt:** ⚠️ PARTIAL (58) — observed updateContents() fails to reset block formatting - stale formats contaminate new document (src/documenthandler.cpp:1104)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:1104-1122: removeSelectedText preserves first block format; insertText inherits old formatting; no QTextBlockFormat reset on load

### [BLK-N03] setLineHeight/setParagraphHeight apply document-wide — destroy per-block customization  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1597,1611`
- **opus:** ✅ LEGIT (60) — setLineHeight/setParagraphHeight select Document -> apply to all blocks (documenthandler.cpp:1597)
- **gpt:** ⚠️ PARTIAL (58) — observed setLineHeight/setParagraphHeight apply document-wide - destroy per-block customization (src/documenthandler.cpp:1597)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:1597 1611: setLineHeight/setParagraphHeight select entire document via cursor.select(Document); destroy per-block customization

### [CFG-N01] Desktop MimeType incomplete — only text/html, missing text/plain and text/markdown  ·  _SPLIT_  ·  Medium
`com.cuperino.qprompt.desktop (both copies)`
- **opus:** ⚠️ PARTIAL (50) — desktop MimeType only text/html, missing text/plain/markdown
- **gpt:** ⚠️ PARTIAL (58) — observed Desktop MimeType incomplete - only text/html, missing text/plain and text/markdown (com.cuperino.qprompt.desktop:1)
- **deepseek:** ✅ LEGIT (95) — com.cuperino.qprompt.desktop (both copies): MimeType=text/html only; appdata.xml also declares text/plain and text/markdown

### [CFG-N02] v1.1.3 release date "2022-1-16" breaks chronological order — should be 2023-01-16  ·  _SPLIT_  ·  Low
`appdata.xml line 202`
- **opus:** ✅ LEGIT (55) — appdata v1.1.3 date 2022-1-16 breaks chronological order (appdata.xml)
- **gpt:** ⚠️ PARTIAL (58) — observed v1.1.3 release date "2022-1-16" breaks chronological order - should be 2023-01-16 (com.cuperino.qprompt.appdata.xml:202)
- **deepseek:** ❔ UNSURE (40) — 'appdata.xml:202 date "2022-1-16"; cannot independently verify correct year from source alone'

### [CFG-N03] "fixedd" typo in v2.0.2 release description  ·  _SPLIT_  ·  Low
`appdata.xml line 72`
- **opus:** ✅ LEGIT (60) — 'fixedd' typo in v2.0.2 release description (appdata.xml)
- **gpt:** ⚠️ PARTIAL (58) — observed "fixedd" typo in v2.0.2 release description (com.cuperino.qprompt.appdata.xml:72)
- **deepseek:** ✅ LEGIT (95) — 'appdata.xml:72: "issues were fixedd in this release" — verified typo in source'

### [CLI-N01] --version flag non-functional — version string empty when parser processes  ·  _SPLIT_  ·  Medium
`main.cpp:159,214`
- **opus:** ⚠️ PARTIAL (50) — --version may be empty: addVersionOption before setApplicationData (main.cpp:159)
- **gpt:** ✅ LEGIT (78) — --version flag non-functional - version string empty when parser processes (src/main.cpp:159)
- **deepseek:** ⚠️ PARTIAL (55) — addVersionOption before applicationData set; version may be empty depending on flow (main.cpp:159)

### [CLIP-N04] Image-only clipboard paste — button enabled but does nothing  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1356-1359`
- **opus:** ✅ LEGIT (65) — image-only paste is a no-op (commented) but button is enabled (documenthandler.cpp:1356)
- **gpt:** ⚠️ PARTIAL (58) — observed Image-only clipboard paste - button enabled but does nothing (src/documenthandler.cpp:1356)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:1356-1359: hasImage() branch entirely commented out; paste button remains enabled but does nothing for images

### [CLP-N01] Copy/Cut exports unfiltered HTML to system clipboard  ·  _SPLIT_  ·  Medium
`Prompter.qml, EditorToolbar.qml, main.qml`
- **opus:** ⚠️ PARTIAL (50) — copy/cut exports unfiltered HTML to clipboard (Prompter.qml)
- **gpt:** ✅ LEGIT (78) — Copy/Cut exports unfiltered HTML to system clipboard (src/prompter/Prompter.qml:1)
- **deepseek:** ⚠️ PARTIAL (70) — Prompter.qml/EditorToolbar.qml/main.qml: copy/cut paths use editor.copy()/cut() placing raw QTextDocument HTML on clipboard; filterHtml() doesn't strip scripts — verified pattern but not all sites

### [CLP-N02] DropArea external drop never calls drop.accept()  ·  _SPLIT_  ·  Medium
`Prompter.qml:1369-1379`
- **opus:** ⚠️ PARTIAL (50) — external drop never calls drop.accept() (Prompter.qml:1369)
- **gpt:** ⚠️ PARTIAL (58) — observed DropArea external drop never calls drop.accept() (src/prompter/Prompter.qml:1369)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:1369-1379: external drop branch (hasUrls/hasHtml/hasText) processes content but never calls drop.accept(); internal drag at 1354 correctly accepts

### [CLP-N03] DropArea external drop: URLs consumed preferentially — text silently lost  ·  _SPLIT_  ·  Medium
`Prompter.qml:1370-1378`
- **opus:** ⚠️ PARTIAL (50) — external drop consumes URLs preferentially, text lost (Prompter.qml:1370)
- **gpt:** ⚠️ PARTIAL (58) — observed DropArea external drop: URLs consumed preferentially - text silently lost (src/prompter/Prompter.qml:1370)
- **deepseek:** ✅ LEGIT (90) — Prompter.qml:1370-1378: hasUrls branch processes ONLY images via insertImageAt(); else-if chain prevents fallthrough to hasHtml/hasText — drag from browser loses all text

### [CMAKE-N01] WASM build excludes TelemetryPage.qml and RemotePage.qml  ·  _SPLIT_  ·  Low
`src/CMakeLists.txt:106-121, main.qml:175-181`
- **opus:** ⚠️ PARTIAL (45) — WASM omits TelemetryPage/RemotePage; both commented out anyway (CMakeLists.txt:106)
- **gpt:** ⚠️ PARTIAL (58) — observed WASM build excludes TelemetryPage.qml and RemotePage.qml (src/CMakeLists.txt:106)
- **deepseek:** ❔ UNSURE (60) — DUPLICATE-ID — WASM exclusion real at src/CMakeLists.txt:106 but refs in main.qml:175 are commented out

### [CMAKE-NEW-01] Remote.qml exists on disk but never listed in QML_FILES  ·  _SPLIT_  ·  Low
`src/CMakeLists.txt, src/prompter/Remote.qml`
- **opus:** ⚠️ PARTIAL (45) — Remote.qml on disk but not in QML_FILES (CMakeLists.txt)
- **gpt:** ✅ LEGIT (78) — Remote.qml exists on disk but never listed in QMLFILES (src/CMakeLists.txt:260)
- **deepseek:** ✅ LEGIT (90) — Remote.qml on disk but not in any CMake QML_FILES — orphaned dead code

### [CMB-N01] autoReloadSeconds SpinBox from binding circular — clamps to 1 when all-zero  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:1381`
- **opus:** ❔ UNSURE (45) — autoReloadSeconds SpinBox circular binding clamps to 1; domain (PrompterPage.qml:1381)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/kirigami_ui/PrompterPage.qml:1381)
- **deepseek:** ✅ LEGIT (70) — SpinBox from binding evaluates to 1 when all three spinners are zero (PrompterPage.qml:1381)

### [CMB-N02] autoReloadMinutes SpinBox from contains redundant circular self-reference  ·  _SPLIT_  ·  Low
`PrompterPage.qml:1356`
- **opus:** ❔ UNSURE (45) — autoReloadMinutes SpinBox circular from binding; domain (PrompterPage.qml:1356)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/kirigami_ui/PrompterPage.qml:1356)
- **deepseek:** ✅ LEGIT (75) — autoReloadMinutes.from self-references autoReloadMinutes.value causing binding loop (PrompterPage.qml:1356)

### [CMT-N01] Justify ToolButton comment says it's commented out — but it's active  ·  _SPLIT_  ·  Medium
`EditorToolbar.qml:761-773`
- **opus:** ⚠️ PARTIAL (40) — comment claims Justify button commented out but it's active (EditorToolbar.qml:761)
- **gpt:** ⚠️ PARTIAL (48) — comment problem observed, but defect impact is limited (src/kirigami_ui/EditorToolbar.qml:761)
- **deepseek:** ✅ LEGIT (90) — Comment says justify is commented out at EditorToolbar.qml:761 but code is active via toolbar.showJustify

### [CMT-N02] Truncated comment in markersmodel.cpp:107-108  ·  _SPLIT_  ·  Low
`markersmodel.cpp:107-108`
- **opus:** ⚠️ PARTIAL (35) — truncated comment; cosmetic (markersmodel.cpp:107)
- **gpt:** ⚠️ PARTIAL (48) — comment problem observed, but defect impact is limited (src/markersmodel.cpp:107)
- **deepseek:** ✅ LEGIT (90) — Truncated comment at markersmodel.cpp:107 — 'after' ends mid-sentence workaround rationale lost

### [CMT-N03] Misleading OpenGL workaround comment — scope of impact understated  ·  _SPLIT_  ·  Medium
`main.cpp:79`
- **opus:** ⚠️ PARTIAL (35) — OpenGL workaround comment scope; meta (main.cpp:79)
- **gpt:** ⚠️ PARTIAL (48) — comment problem observed, but defect impact is limited (src/main.cpp:79)
- **deepseek:** ✅ LEGIT (85) — Comment at main.cpp:79 mentions only 'opacity bug' — omits that opengl backend forces deprecated path on all Windows

### [CMT-N05] Missing security warning on QProcess RCE sink (sys://)  ·  _SPLIT_  ·  High
`qmlutil.hpp:84-95`
- **opus:** ⚠️ PARTIAL (40) — only a missing security-comment note on the sys:// RCE sink (qmlutil.hpp:84)
- **gpt:** ⚠️ PARTIAL (48) — comment problem observed, but defect impact is limited (src/qmlutil.hpp:84)
- **deepseek:** ✅ LEGIT (85) — No security comment on QProcess::startDetached at qmlutil.hpp:91 — sys:// RCE sink unannotated

### [CMT-N06] Missing warning: re-entrant toggle() inside Behavior.onRunningChanged  ·  _SPLIT_  ·  Medium
`Prompter.qml:855-856`
- **opus:** ⚠️ PARTIAL (40) — only a missing-warning note re re-entrant toggle (Prompter.qml:855)
- **gpt:** ⚠️ PARTIAL (48) — comment problem observed, but defect impact is limited (src/prompter/Prompter.qml:855)
- **deepseek:** ✅ LEGIT (80) — toggle() at Prompter.qml:855 inside Behavior.onRunningChanged — re-entrant no warning comment

### [CMT-N07] Missing warning: joinPreviousEditBlock() without beginEditBlock()  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1596,1610`
- **opus:** ⚠️ PARTIAL (40) — only a missing-comment note re joinPreviousEditBlock (documenthandler.cpp:1596)
- **gpt:** ⚠️ PARTIAL (48) — comment problem observed, but defect impact is limited (src/documenthandler.cpp:1596)
- **deepseek:** ✅ LEGIT (85) — joinPreviousEditBlock() at documenthandler.cpp:1596 without beginEditBlock() — no warning comment

### [CMT-N08] Entire Telemetry class is dead commented-out shell across 4 files  ·  _SPLIT_  ·  Medium
`telemetry.h, telemetry.cpp, promptsession.h, promptsession.cpp`
- **opus:** ✅ LEGIT (50) — Telemetry class is dead commented-out shell (telemetry.h)
- **gpt:** ⚠️ PARTIAL (48) — comment problem observed, but defect impact is limited (src/telemetry.h:1)
- **deepseek:** ✅ LEGIT (90) — All Telemetry methods commented out across 4 files — dead shell creates false expectations

### [CMT-N09] Commented-out PropertyActions in active loop animation — stale state risk  ·  _SPLIT_  ·  Medium
`Prompter.qml:866-871`
- **opus:** ⚠️ PARTIAL (40) — commented-out PropertyActions; stale-state note (Prompter.qml:866)
- **gpt:** ⚠️ PARTIAL (48) — comment problem observed, but defect impact is limited (src/prompter/Prompter.qml:866)
- **deepseek:** ✅ LEGIT (85) — PropertyActions resetting __i/position commented out at Prompter.qml:866-871 — stale state risk

### [CMT-N10] Obsolete Qt 5 qmlRegisterType calls as commented-out cruft  ·  _SPLIT_  ·  Low
`main.cpp:68-69,215-223`
- **opus:** ⚠️ PARTIAL (35) — commented-out Qt5 qmlRegisterType cruft; cosmetic (main.cpp:68)
- **gpt:** ⚠️ PARTIAL (48) — comment problem observed, but defect impact is limited (src/main.cpp:68)
- **deepseek:** ✅ LEGIT (90) — Qt 5 qmlRegisterType calls commented out at main.cpp — cruft misleads about QML_ELEMENT registration

### [CNTD-N01] Countdown Running: dissolveIn and dissolveOut compete for same opacity when __iterations===__disappearWithin===1  ·  _SPLIT_  ·  Low
`Countdown.qml:289-291,308`
- **opus:** ⚠️ PARTIAL (50) — dissolveIn/dissolveOut compete for opacity (Countdown.qml:289)
- **gpt:** ⚠️ PARTIAL (58) — observed Countdown Running: dissolveIn and dissolveOut compete for same opacity when iterations===disapp (src/prompter/Countdown.qml:289)
- **deepseek:** ✅ LEGIT (85) — Countdown.qml:289-291/308: Running state sets dissolveIn.running=true (fade-in) AND dissolveOut.running when __iterations===__disappearWithin===1 — both animate same opacity

### [COERC-N03] real→int truncation in WindowDragger position compounds drift  ·  _SPLIT_  ·  Low
`WindowDragger.qml:28-34`
- **opus:** ⚠️ PARTIAL (50) — real->int truncation in WindowDragger compounds drift (FINAL-05 family) (WindowDragger.qml:28)
- **gpt:** ⚠️ PARTIAL (58) — observed real->int truncation in WindowDragger position compounds drift (src/qt/WindowDragger.qml:28)
- **deepseek:** ✅ LEGIT (80) — WindowDragger.qml:28-34: mouse.x (qreal) stored to prevX (int) losing fractional precision; compounds drift on each drag start

### [COLOR-01] ProjectionsManager.qml uses invalid "initial" color — repro of R4-ROOT-02  ·  _SPLIT_  ·  Medium
`ProjectionsManager.qml:195`
- **opus:** ✅ LEGIT (70) — invalid 'initial' color (dup R4-ROOT-02) (ProjectionsManager.qml:195)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/prompter/ProjectionsManager.qml:195)
- **deepseek:** ⚠️ PARTIAL (50) — 'initial' CSS keyword may be valid in Qt6 but is non-standard QML color name (ProjectionsManager.qml:195)

### [COLOR-02] Hardcoded #EED text invisible on light themes — WheelSettingsOverlay  ·  _SPLIT_  ·  Medium
`WheelSettingsOverlay.qml:105`
- **opus:** ⚠️ PARTIAL (40) — #EED text invisible on light themes (WheelSettingsOverlay.qml:105)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/kirigami_ui/WheelSettingsOverlay.qml:105)
- **deepseek:** ✅ LEGIT (75) — #EED nearly invisible on light themes; hardcoded without theme awareness (WheelSettingsOverlay.qml:105)

### [COLOR-04] ReadRegionOverlay ColorAnimation tracks __fillColor that never changes  ·  _SPLIT_  ·  Low
`ReadRegionOverlay.qml:204,616`
- **opus:** ⚠️ PARTIAL (45) — ColorAnimation tracks __fillColor that never changes (ReadRegionOverlay.qml:204)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/prompter/ReadRegionOverlay.qml:204)
- **deepseek:** ✅ LEGIT (65) — ColorAnimation tracks __fillColor='#00000000' constant; never produces visible change (ReadRegionOverlay.qml:204 616)

### [COLOR-07] CSS default stylesheet hardcodes #FFFFFF body text — ignores user text color  ·  _SPLIT_  ·  Low
`documenthandler.cpp:185-189`
- **opus:** ⚠️ PARTIAL (55) — body color hardcoded #FFFFFF; per-span user colors still override (documenthandler.cpp:185)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/documenthandler.cpp:185)
- **deepseek:** ✅ LEGIT (65) — CSS body{color:#FFFFFF} hardcoded; overrides user text color for HTML docs (documenthandler.cpp:185-189)

### [COLOR-CRIT-01] selectionColor #333d9ef3 — alpha channel reversed (#AARRGGBB vs #RRGGBBAA), selection invisible  ·  _SPLIT_  ·  High
`Prompter.qml:973-974`
- **opus:** ❔ UNSURE (45) — #333d9ef3 is valid #AARRGGBB (20% blue); 'reversed alpha' likely intentional (Prompter.qml:973)
- **gpt:** ❔ UNSURE (39) — #333d9ef3 is syntactically AARRGGBB; intent is uncertain (src/prompter/Prompter.qml:973)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:973-974: #333d9ef3 uses #AARRGGBB format but dev likely intended #RRGGBBAA; AA=0x33=20% alpha nearly invisible

### [COLOR-N08] textBackground() returns invalid QColor for body/paragraph text  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:528-534`
- **opus:** ⚠️ PARTIAL (45) — textBackground().color() yields black for unset bg, not 'invalid' (documenthandler.cpp:534)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/documenthandler.cpp:528)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:528-534: textBackground() returns format.background().color(); QBrush::color() on NoBrush returns invalid QColor

### [COLOR-N09] acceptedColor binds transparent QColor on startup — initial text invisible  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:1010,1025, PrompterView.qml:240-241`
- **opus:** ⚠️ PARTIAL (55) — acceptedColor transparent on startup -> initial text invisible (PrompterPage.qml:1010)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/kirigami_ui/PrompterPage.qml:1010)
- **deepseek:** ✅ LEGIT (90) — PrompterPage.qml:1010 1025: acceptedColor uninitialized defaults to Qt.rgba(0 0 0 0); PrompterView.qml:240-241 binds transparent; initial text invisible

### [COMP-N03] regularMarker() same double-textCursor anti-pattern as LOG-07  ·  _SPLIT_  ·  Low
`documenthandler.cpp:693-696`
- **opus:** ⚠️ PARTIAL (50) — regularMarker double textCursor() (LOG-07 family) (documenthandler.cpp:693)
- **gpt:** ✅ LEGIT (78) — regularMarker() same double-textCursor anti-pattern as LOG-07 (src/documenthandler.cpp:693)
- **deepseek:** ✅ LEGIT (95) — documenthandler.cpp:693-696: fetches textCursor() 3 extra times after null-checked local copy; same anti-pattern as namedMarker() at 701-704 — stale formatting reads

### [CONST-N01] getMarkerKey() not const — pure reader without side effects  ·  _SPLIT_  ·  Low
`documenthandler.h:214, documenthandler.cpp:746`
- **opus:** ⚠️ PARTIAL (40) — getMarkerKey not const; style only (documenthandler.cpp:746)
- **gpt:** ⚠️ PARTIAL (58) — observed getMarkerKey() not const - pure reader without side effects (src/documenthandler.h:214)
- **deepseek:** ✅ LEGIT (60) — getMarkerKey pure reader method missing const qualifier (documenthandler.cpp:746)

### [CONST-N02] getMarkerHref() not const — identical pattern  ·  _SPLIT_  ·  Low
`documenthandler.h:216, documenthandler.cpp:779`
- **opus:** ⚠️ PARTIAL (40) — getMarkerHref not const; style only (documenthandler.cpp:779)
- **gpt:** ⚠️ PARTIAL (58) — observed getMarkerHref() not const - identical pattern (src/documenthandler.h:216)
- **deepseek:** ✅ LEGIT (60) — getMarkerHref pure reader method missing const qualifier (documenthandler.cpp:779)

### [CONST-N03] MarkersModel::previousMarker(), nextMarker(), keySearch(), binarySearch() not const  ·  _SPLIT_  ·  Low
`markersmodel.h:62,63,64,78, markersmodel.cpp:117,151,205,217`
- **opus:** ⚠️ PARTIAL (40) — marker query methods not const (markersmodel.h:62)
- **gpt:** ⚠️ PARTIAL (58) — observed MarkersModel::previousMarker(), nextMarker(), keySearch(), binarySearch() not const (src/markersmodel.h:62)
- **deepseek:** ✅ LEGIT (55) — four marker query methods lack const qualifier (markersmodel.h:62-64 78)

### [CONST-N04] GlobalHotkeys::globalShortcutKey(Action) not const — Q_INVOKABLE pure query  ·  _SPLIT_  ·  Low
`globalhotkeys.h:147, globalhotkeys.cpp:108`
- **opus:** ⚠️ PARTIAL (40) — globalShortcutKey not const; Q_INVOKABLE query (globalhotkeys.h:147)
- **gpt:** ⚠️ PARTIAL (58) — observed GlobalHotkeys::globalShortcutKey(Action) not const - Q_INVOKABLE pure query (src/globalhotkeys.h:147)
- **deepseek:** ✅ LEGIT (60) — Q_INVOKABLE globalShortcutKey pure query method missing const (globalhotkeys.cpp:108)

### [CONST-N05] Unnecessary copy via const auto instead of const auto& in extendLastMarker  ·  _SPLIT_  ·  Low
`markersmodel.cpp:111`
- **opus:** ⚠️ PARTIAL (40) — const auto copy vs const auto& in extendLastMarker (markersmodel.cpp:111)
- **gpt:** ⚠️ PARTIAL (58) — observed Unnecessary copy via const auto instead of const auto& in extendLastMarker (src/markersmodel.cpp:111)
- **deepseek:** ✅ LEGIT (65) — const auto copies Marker object; should be const auto& to avoid copy (markersmodel.cpp:111)

### [CPY-01] 5 Q_INVOKABLE methods pass QString by value instead of const&  ·  _SPLIT_  ·  Low
`markersmodel.h:68, documenthandler.h:213,215,227, systemfontchooserdialog.h:53`
- **opus:** ⚠️ PARTIAL (40) — 5 Q_INVOKABLE pass QString by value (markersmodel.h:68)
- **gpt:** ⚠️ PARTIAL (58) — observed 5 Q_INVOKABLE methods pass QString by value instead of const& (src/markersmodel.h:68)
- **deepseek:** ✅ LEGIT (80) — 5 Q_INVOKABLE methods pass QString by value instead of const&; unnecessary heap copies (documenthandler.h:213 215 227 markersmodel.h:68)

### [DBG-N01] OBS WebSocket auth challenge+salt logged to console in release builds  ·  _SPLIT_  ·  Medium
`Prompter.qml:364,372,386`
- **opus:** ✅ LEGIT (60) — console.log(m) logs OBS auth challenge+salt in release (Prompter.qml:372)
- **gpt:** ⚠️ PARTIAL (58) — observed OBS WebSocket auth challenge+salt logged to console in release builds (src/prompter/Prompter.qml:364)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:364 372 386: console.log(status) + console.log(m) logs full WebSocket Hello including auth challenge+salt; console.info maps to unsuppressed qInfo()

### [DBG-N02] Velocity debug logging active in production  ·  _SPLIT_  ·  Low
`Prompter.qml:606, InputsOverlay.qml:441`
- **opus:** ✅ LEGIT (55) — velocity debug console.log active in production (Prompter.qml:606)
- **gpt:** ⚠️ PARTIAL (58) — observed Velocity debug logging active in production (src/prompter/Prompter.qml:606)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:606: console.log('velocity: ' velocity) every velocity change; InputsOverlay.qml:441: console.log(setVelocityModifier) every ComboBox change; no debug guard

### [DBG-N04] qDebug() in namedMarker()/setMarker() active in release  ·  _SPLIT_  ·  Low
`documenthandler.cpp:760,793`
- **opus:** ✅ LEGIT (60) — qDebug in namedMarker/setMarker active in release builds (documenthandler.cpp:760)
- **gpt:** ⚠️ PARTIAL (58) — observed qDebug() in namedMarker()/setMarker() active in release (src/documenthandler.cpp:760)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:760 793: qDebug() in getMarkerKey() line 760 and setMarker() line 793 active in release builds; CMake does not define QT_NO_DEBUG_OUTPUT

### [DEB-N02] qml6-module-qtcore is not a real Debian package — .deb uninstallable  ·  _SPLIT_  ·  High
`CMakeLists.txt:446`
- **opus:** ❔ UNSURE (45) — qml6-module-qtcore package-existence claim; Debian-specific (CMakeLists.txt:446)
- **gpt:** ✅ LEGIT (84) — qml6-module-qtcore is not a real Debian package - .deb uninstallable (CMakeLists.txt:446)
- **deepseek:** ✅ LEGIT (95) — CMakeLists.txt:446: qml6-module-qtcore not a real Debian package; QtCore has no QML module; apt resolution fails

### [DEB-N03] qml6-module-qt-labs-platform doesn't exist for Qt 6 — .deb uninstallable  ·  _SPLIT_  ·  High
`CMakeLists.txt:446`
- **opus:** ❔ UNSURE (45) — qml6-module-qt-labs-platform package-existence claim; Debian-specific (CMakeLists.txt:446)
- **gpt:** ✅ LEGIT (84) — qml6-module-qt-labs-platform doesn't exist for Qt 6 - .deb uninstallable (CMakeLists.txt:446)
- **deepseek:** ✅ LEGIT (95) — CMakeLists.txt:446: qml6-module-qt-labs-platform doesn't exist for Qt 6; qt.labs.platform was dropped; package unsatisfiable

### [DECL-N01] MarkersModel::keySearch — default params in definition but not declaration  ·  _SPLIT_  ·  Low
`markersmodel.h:64 vs markersmodel.cpp:117`
- **opus:** ⚠️ PARTIAL (45) — keySearch default params in def not decl (markersmodel.h:64)
- **gpt:** ✅ LEGIT (78) — MarkersModel::keySearch - default params in definition but not declaration (src/markersmodel.h:64)
- **deepseek:** ✅ LEGIT (75) — keySearch has default params in definition but not declaration (markersmodel.h:64 vs markersmodel.cpp:117)

### [DECL-N02] SessionModel::resetInternalData() missing override keyword and Qt 6 version guard  ·  _SPLIT_  ·  Low
`promptsession.h:74-75`
- **opus:** ⚠️ PARTIAL (40) — resetInternalData missing override (promptsession.h:74)
- **gpt:** ✅ LEGIT (78) — SessionModel::resetInternalData() missing override keyword and Qt 6 version guard (src/promptsession.h:74)
- **deepseek:** ✅ LEGIT (85) — resetInternalData missing override keyword; no Qt6 version guard in SessionModel (promptsession.h:74-75)

### [DEF-N02] DropArea internalDrag always false — internal drag handler dead code  ·  _SPLIT_  ·  Medium
`Prompter.qml:1331,1350`
- **opus:** ⚠️ PARTIAL (50) — DropArea internalDrag always false -> handler dead code (Prompter.qml:1331)
- **gpt:** ⚠️ PARTIAL (58) — observed DropArea internalDrag always false - internal drag handler dead code (src/prompter/Prompter.qml:1331)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:1331/1350: internalDrag always false never set true; startTextDrag/startRangeDrag never called from QML — internal drag handler dead code

### [DETACH-N01] 4 non-const operator[] on QList in keySearch() — unnecessary implicit sharing detach  ·  _SPLIT_  ·  Low
`markersmodel.cpp:126,133,137,144`
- **opus:** ⚠️ PARTIAL (40) — non-const operator[] detaches QList (markersmodel.cpp:126)
- **gpt:** ⚠️ PARTIAL (58) — observed 4 non-const operator[] on QList in keySearch() - unnecessary implicit sharing detach (src/markersmodel.cpp:126)
- **deepseek:** ✅ LEGIT (75) — markersmodel.cpp:126 133 137 144: non-const operator[] on QModelIndexList forces implicit sharing detach; all uses read-only

### [DLG-N03] errorDialog MessageDialog has no title  ·  _SPLIT_  ·  Low
`Prompter.qml:2510-2513`
- **opus:** ⚠️ PARTIAL (45) — errorDialog MessageDialog has no title (Prompter.qml:2510)
- **gpt:** ✅ LEGIT (78) — errorDialog MessageDialog has no title (src/prompter/Prompter.qml:2510)
- **deepseek:** ✅ LEGIT (90) — errorDialog at Prompter.qml:2510 has no title — blank title bar

### [DLG-N07] 5 showPassiveNotification() calls ignore passiveNotifications preference  ·  _SPLIT_  ·  Low
`Find.qml:133,135,160, EditorToolbar.qml:627, PrompterPage.qml:890`
- **opus:** ⚠️ PARTIAL (45) — 5 showPassiveNotification ignore preference (Find.qml:133)
- **gpt:** ✅ LEGIT (78) — 5 showPassiveNotification() calls ignore passiveNotifications preference (src/prompter/Find.qml:133)
- **deepseek:** ✅ LEGIT (85) — 5 showPassiveNotification calls lack root.passiveNotifications guard — fire even when disabled

### [DLG-N08] 3 save-completion passive notifications lack passiveNotifications guard  ·  _SPLIT_  ·  Low
`Prompter.qml:2294,2296,2474,2499`
- **opus:** ⚠️ PARTIAL (45) — save notifications lack passiveNotifications guard (Prompter.qml:2294)
- **gpt:** ✅ LEGIT (78) — 3 save-completion passive notifications lack passiveNotifications guard (src/prompter/Prompter.qml:2294)
- **deepseek:** ✅ LEGIT (85) — Save notifications at Prompter.qml:2294 2296 2474 2499 lack passiveNotifications guard

### [DLG-N10] TimerClock ColorDialog selectedColor never initialized from persisted settings  ·  _SPLIT_  ·  Medium
`TimerClock.qml:198-210`
- **opus:** ⚠️ PARTIAL (45) — ColorDialog selectedColor not init from settings (TimerClock.qml:198)
- **gpt:** ✅ LEGIT (78) — TimerClock ColorDialog selectedColor never initialized from persisted settings (src/prompter/TimerClock.qml:198)
- **deepseek:** ✅ LEGIT (90) — TimerClock.qml:198-210: onVisibleChanged sets custom 'color' prop but never selectedColor (the dialog's actual display property); dialog shows Qt default on first open

### [DLG-N11] PrompterPage ColorDialogs — dead acceptedColor property binding  ·  _SPLIT_  ·  Low
`PrompterPage.qml:1010,1025, PrompterView.qml:240-241`
- **opus:** ⚠️ PARTIAL (45) — ColorDialogs dead acceptedColor binding (PrompterPage.qml:1010)
- **gpt:** ✅ LEGIT (78) — PrompterPage ColorDialogs - dead acceptedColor property binding (src/kirigami_ui/PrompterPage.qml:1010)
- **deepseek:** ✅ LEGIT (90) — PrompterPage.qml:1010/1025: acceptedColor declared but never assigned; PrompterView.qml:240-241 binds prompter.textColor/textBackground to dead property — masked by direct setTextColor() in onAccepted

### [DPI-01] TimerClock.qml:127 devicePixelRatio in raw arithmetic with magic multiplier  ·  _SPLIT_  ·  Medium
`TimerClock.qml:127`
- **opus:** ⚠️ PARTIAL (40) — devicePixelRatio raw arithmetic magic multiplier (TimerClock.qml:127)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/prompter/TimerClock.qml:127)
- **deepseek:** ✅ LEGIT (80) — <<3 multiplier at TimerClock.qml:127 produces inconsistent scaling on fractional HiDPI

### [DPI-02] MarkersDrawer.qml:37 drawer minimumWidth hardcoded to 260px  ·  _SPLIT_  ·  Low
`MarkersDrawer.qml:37`
- **opus:** ⚠️ PARTIAL (45) — drawer minimumWidth hardcoded 260px (MarkersDrawer.qml:37)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/kirigami_ui/MarkersDrawer.qml:37)
- **deepseek:** ✅ LEGIT (85) — Hardcoded 260px width at MarkersDrawer.qml:37 — ignores DPI scaling

### [DPI-03] Find.qml:38 searchBarWidth:724 hardcoded in px  ·  _SPLIT_  ·  Low
`Find.qml:38`
- **opus:** ⚠️ PARTIAL (45) — searchBarWidth:724 hardcoded px (Find.qml:38)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/prompter/Find.qml:38)
- **deepseek:** ✅ LEGIT (90) — Hardcoded 724px searchBarWidth at Find.qml:38 — ignores DPI

### [DPI-04] InputsOverlay.qml:33 height:680 hardcoded  ·  _SPLIT_  ·  Medium
`InputsOverlay.qml:33`
- **opus:** ✅ LEGIT (60) — InputsOverlay height:680 hardcoded (InputsOverlay.qml:33)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/kirigami_ui/InputsOverlay.qml:33)
- **deepseek:** ✅ LEGIT (90) — Hardcoded 680px height at InputsOverlay.qml:33 — exceeds screen on HiDPI at 1080p

### [DRAG-N01] Image resize body drag: cursor shows OpenHandCursor until drag threshold exceeded  ·  _SPLIT_  ·  Low
`Prompter.qml:1651`
- **opus:** ⚠️ PARTIAL (45) — image-resize body drag cursor until threshold (Prompter.qml:1651)
- **gpt:** ⚠️ PARTIAL (58) — observed Image resize body drag: cursor shows OpenHandCursor until drag threshold exceeded (src/prompter/Prompter.qml:1651)
- **deepseek:** ✅ LEGIT (80) — dragTarget.manualDrag=false until threshold; cursorShape shows OpenHandCursor during press-to-drag phase at Prompter.qml:1651

### [DRAG-N02] textDragArea has no cursorShape — no cursor feedback during text drag  ·  _SPLIT_  ·  Low
`Prompter.qml:1429-1431`
- **opus:** ✅ LEGIT (55) — textDragArea no cursorShape; no drag cursor feedback (Prompter.qml:1429)
- **gpt:** ⚠️ PARTIAL (58) — observed textDragArea has no cursorShape - no cursor feedback during text drag (src/prompter/Prompter.qml:1429)
- **deepseek:** ✅ LEGIT (80) — textDragArea MouseArea lacks cursorShape at Prompter.qml:1429-1431; no visual cursor change during text drag

### [DRW-01] interalFocusElsewhere() misses 3 OverlaySheets + 2 Drawers — hotkeys pass through  ·  _SPLIT_  ·  Medium
`Prompter.qml:283-296`
- **opus:** ⚠️ PARTIAL (50) — interalFocusElsewhere() misses sheets/drawers -> hotkey passthrough (Prompter.qml:283)
- **gpt:** ⚠️ PARTIAL (58) — observed interalFocusElsewhere() misses 3 OverlaySheets + 2 Drawers - hotkeys pass through (src/prompter/Prompter.qml:283)
- **deepseek:** ✅ LEGIT (88) — hotkey guard misses obsConfiguration dictionariesSheet customWordsSheet contextDrawer globalMenu (Prompter.qml:283-296)

### [DRW-02] globalDrawer and contextDrawer missing from ESC dismiss chain  ·  _SPLIT_  ·  Medium
`main.qml:481-504, +windows:452-487, +android:391-426`
- **opus:** ⚠️ PARTIAL (50) — globalDrawer/contextDrawer not in ESC dismiss chain (main.qml:481)
- **gpt:** ⚠️ PARTIAL (58) — observed globalDrawer and contextDrawer missing from ESC dismiss chain (src/kirigami_ui/main.qml:481)
- **deepseek:** ✅ LEGIT (88) — ESC handler checks 8 sheets but not contextDrawer.drawerOpen nor globalMenu.drawerOpen; drawer stays (main.qml:481-504)

### [DSZ-01] InputsOverlay hardcoded height:680 — overflows on phones  ·  _SPLIT_  ·  Medium
`InputsOverlay.qml:33`
- **opus:** ✅ LEGIT (60) — hardcoded height:680 overflows small phones (dup DPI-04) (InputsOverlay.qml:33)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/kirigami_ui/InputsOverlay.qml:33)
- **deepseek:** ✅ LEGIT (88) — hardcoded height:680 no Math.min; on phones(~500dp usable) content exceeds viewport (InputsOverlay.qml:33)

### [DSZ-02] pointerConfiguration OverlaySheet no vertical ScrollView  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:1426-1445`
- **opus:** ⚠️ PARTIAL (45) — pointerConfiguration sheet lacks vertical ScrollView (PrompterPage.qml:1426)
- **gpt:** ✅ LEGIT (78) — pointerConfiguration OverlaySheet no vertical ScrollView (src/kirigami_ui/PrompterPage.qml:1426)
- **deepseek:** ✅ LEGIT (88) — PointerSettings inside OverlaySheet no ScrollView/Flickable; ~600-800px implicit height overflows small screens (PrompterPage.qml:1426-1445)

### [DSZ-03] Magic number 68 in ListView height binding  ·  _SPLIT_  ·  Low
`InputsOverlay.qml:83`
- **opus:** ⚠️ PARTIAL (40) — magic number 68 in ListView height (InputsOverlay.qml:83)
- **gpt:** ⚠️ PARTIAL (58) — observed Magic number 68 in ListView height binding (src/kirigami_ui/InputsOverlay.qml:83)
- **deepseek:** ✅ LEGIT (85) — Hardcoded 68px offset at InputsOverlay.qml:83 — brittle vs Kirigami units

### [EDGE-07] Q_UNREACHABLE in Q_INVOKABLE method — UB if called from QML  ·  _SPLIT_  ·  High
`src/shakedetector.cpp:49-51`
- **opus:** ⚠️ PARTIAL (60) — Q_UNREACHABLE in Q_INVOKABLE but only caller fires on iOS (shakedetector.cpp:51)
- **gpt:** ⚠️ PARTIAL (58) — observed Q_UNREACHABLE in Q_INVOKABLE method - UB if called from QML (src/shakedetector.cpp:49)
- **deepseek:** ✅ LEGIT (85) — Q_UNREACHABLE() at shakedetector.cpp:49-51 in Q_INVOKABLE showUndoRedoDialog; compiles to __builtin_unreachable() in release — UB if QML calls this

### [EDGE-10] globalShortcutKey() switch without default — fallthrough to Q_UNREACHABLE  ·  _SPLIT_  ·  Low
`src/globalhotkeys.cpp:513-515`
- **opus:** ❌ FALSE (85) — early return guards it; switch not compiled (globalhotkeys.cpp:111)
- **gpt:** ⚠️ PARTIAL (58) — Q_UNREACHABLE is after compiled switch cases; only future enums matter (src/globalhotkeys.cpp:513)
- **deepseek:** ⚠️ PARTIAL (50) — Q_UNREACHABLE at globalhotkeys.cpp:514 reachable when only QHotkey on Wayland; but depends on specific preprocessor+platform combo — plausible but narrow

### [EDGE-11] m_reply dereference without null check in loadFromNetworkFinihed()  ·  _SPLIT_  ·  Medium
`src/documenthandler.cpp:890`
- **opus:** ⚠️ PARTIAL (60) — m_reply->readAll no null check; fires after get() (documenthandler.cpp:890)
- **gpt:** ⚠️ PARTIAL (58) — observed m_reply dereference without null check in loadFromNetworkFinihed() (src/documenthandler.cpp:890)
- **deepseek:** ✅ LEGIT (85) — m_reply->readAll() at doc.cpp:890 w/o null check; m_reply uninitialized in constructor; signal-carried reply pointer ignored — null deref risk

### [EDGE-12] QTextBlock::iterator scope fragility in parse()  ·  _SPLIT_  ·  Low
`src/documenthandler.cpp:1648,1662-1663`
- **opus:** ⚠️ PARTIAL (40) — iterator-outside-loop anti-pattern; report admits 'None currently' (documenthandler.cpp:1648)
- **gpt:** ⚠️ PARTIAL (58) — observed QTextBlock::iterator scope fragility in parse() (src/documenthandler.cpp:1648)
- **deepseek:** ❌ FALSE (40) — Iterator declared outside loop at doc.cpp:1648/1662 is C++ pattern; no continue inside for-body currently; fragile but not a bug without evidence of misuse

### [ENUM-01] documenthandler.cpp:1108 updateContents switch no default — silent data loss  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1108`
- **opus:** ⚠️ PARTIAL (45) — updateContents switch has no default but covers all TextFormat values (documenthandler.cpp:1108)
- **gpt:** ✅ LEGIT (78) — documenthandler.cpp:1108 updateContents switch no default - silent data loss (src/documenthandler.cpp:1108)
- **deepseek:** ✅ LEGIT (90) — No default case in switch(format) at documenthandler.cpp:1108 — doc cleared with zero content inserted

### [ERR-N02] insertImageAt() async callback silently discards 3 failure modes  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1744-1752`
- **opus:** ⚠️ PARTIAL (55) — insertImageAt async callback returns silently on 3 failure modes (documenthandler.cpp:1744)
- **gpt:** ⚠️ PARTIAL (58) — observed insertImageAt() async callback silently discards 3 failure modes (src/documenthandler.cpp:1744)
- **deepseek:** ✅ LEGIT (95) — documenthandler.cpp:1744-1752: async callback three silent returns — reply error (1744) null image (1748) null doc (1751); none emit error() — user sees nothing

### [EVT-03] velocityDragOverlay (z:7) steals clicks from control buttons (z:6)  ·  _SPLIT_  ·  High
`PrompterPage.qml:914 vs PrompterView.qml:61`
- **opus:** ⚠️ PARTIAL (50) — velocityDragOverlay z:7 may steal clicks from z:6 buttons (PrompterPage.qml:914)
- **gpt:** ⚠️ PARTIAL (58) — observed velocityDragOverlay (z:7) steals clicks from control buttons (z:6) (src/kirigami_ui/PrompterPage.qml:914)
- **deepseek:** ✅ LEGIT (90) — velocityDragOverlay z:7 above upperControls z:6; left-click buttons requires double-click when indicator on (PrompterPage.qml:914 PrompterView.qml:61)

### [EVT-04] Drag breaks editor.x declarative binding permanently  ·  _SPLIT_  ·  High
`Prompter.qml:1984,958`
- **opus:** ⚠️ PARTIAL (50) — width-handle drag.target editor may break editor.x binding (Prompter.qml:1984)
- **gpt:** ⚠️ PARTIAL (58) — observed Drag breaks editor.x declarative binding permanently (src/prompter/Prompter.qml:1984)
- **deepseek:** ✅ LEGIT (92) — drag.target:editor writes x imperatively breaking x:contentsPlacement*(prompter.width)+20 binding (Prompter.qml:1984 958)

### [EVT-05] Drag breaks positionHandler.x declarative binding permanently  ·  _SPLIT_  ·  High
`Prompter.qml:2018,926`
- **opus:** ⚠️ PARTIAL (50) — drag.target positionHandler may break its x binding (Prompter.qml:2018)
- **gpt:** ⚠️ PARTIAL (58) — observed Drag breaks positionHandler.x declarative binding permanently (src/prompter/Prompter.qml:2018)
- **deepseek:** ✅ LEGIT (92) — drag.target:positionHandler writes x imperatively breaking declarative x binding (Prompter.qml:2018 926)

### [EVT-06] Drag breaks stopwatch.x binding permanently  ·  _SPLIT_  ·  Medium
`TimerClock.qml:178,130`
- **opus:** ⚠️ PARTIAL (50) — drag breaks stopwatch.x binding (TimerClock.qml:178)
- **gpt:** ⚠️ PARTIAL (58) — observed Drag breaks stopwatch.x binding permanently (src/prompter/TimerClock.qml:178)
- **deepseek:** ✅ LEGIT (90) — drag.target:parent writes x imperatively; stopwatch no longer re-centers on resize after one drag (TimerClock.qml:178 130)

### [EVT-09] Flow ToolSeparator visibility compares y of potentially invisible rows  ·  _SPLIT_  ·  Low
`EditorToolbar.qml:246-249,284-287,309-312,347-350,433-437,549-552,710-713,774-777`
- **opus:** ⚠️ PARTIAL (45) — Flow ToolSeparator visibility compares y of invisible rows (EditorToolbar.qml:246)
- **gpt:** ⚠️ PARTIAL (52) — observed Flow ToolSeparator visibility compares y of potentially invisible rows (src/kirigami_ui/EditorToolbar.qml:246)
- **deepseek:** ✅ LEGIT (78) — ToolSeparator visibility compares row.y when row may be invisible(y=0); false positive match (EditorToolbar.qml:246-249)

### [EVT-10] Nested MouseAreas with hoverEnabled steal hover from parent Buttons  ·  _SPLIT_  ·  Low
`ProjectionsManager.qml:347-354,376-383,405-412`
- **opus:** ⚠️ PARTIAL (50) — nested hoverEnabled MouseAreas steal hover (ProjectionsManager.qml:347)
- **gpt:** ⚠️ PARTIAL (58) — observed Nested MouseAreas with hoverEnabled steal hover from parent Buttons (src/prompter/ProjectionsManager.qml:347)
- **deepseek:** ✅ LEGIT (85) — nested MouseArea hoverEnabled:true fills parent Button; Button.hovered never fires (ProjectionsManager.qml:347-354)

### [EVT-N10] Editor Ctrl+Letter shortcuts don't accept event — marker key-search double-fires  ·  _SPLIT_  ·  Medium
`Prompter.qml:2123-2161`
- **opus:** ❔ UNSURE (45) — editor Ctrl+Letter doesn't accept event; double-handling claim (Prompter.qml:2123)
- **gpt:** ⚠️ PARTIAL (58) — observed Editor Ctrl+Letter shortcuts don't accept event - marker key-search double-fires (src/prompter/Prompter.qml:2123)
- **deepseek:** ✅ LEGIT (70) — Ctrl+Letter shortcuts return without event.accepted=true; secondary handlers fire (Prompter.qml:2123-2161)

### [EVT-N11] windowStayOnTopButton lacks focusPolicy — unreachable via keyboard  ·  _SPLIT_  ·  Low
`EditorToolbar.qml:794-804`
- **opus:** ⚠️ PARTIAL (45) — windowStayOnTopButton lacks focusPolicy (EditorToolbar.qml:794)
- **gpt:** ⚠️ PARTIAL (58) — observed windowStayOnTopButton lacks focusPolicy - unreachable via keyboard (src/kirigami_ui/EditorToolbar.qml:794)
- **deepseek:** ❌ FALSE (70) — ToolButton implicit default focusPolicy is Qt.StrongFocus; reachable via Tab key (EditorToolbar.qml:794-804)

### [EVT-N12] velocityDragArea and viewport.mouse share z:5 — wheel dispatch ambiguous  ·  _SPLIT_  ·  Low
`PrompterPage.qml:875-877 vs PrompterView.qml:3083`
- **opus:** ⚠️ PARTIAL (50) — velocityDragArea/viewport.mouse share z:5; wheel ambiguous (PrompterPage.qml:875)
- **gpt:** ⚠️ PARTIAL (58) — observed velocityDragArea and viewport.mouse share z:5 - wheel dispatch ambiguous (src/kirigami_ui/PrompterPage.qml:875)
- **deepseek:** ✅ LEGIT (60) — velocityDragArea and viewport.mouse share z:5; wheel event dispatch ambiguous (PrompterPage.qml:875-877 vs PrompterView.qml:249)

### [EVT-N13] rewind()/fastForward() event undefined — winding state permanently locked after first use  ·  _SPLIT_  ·  High
`Prompter.qml:547-571`
- **opus:** ❔ UNSURE (45) — rewind()/fastForward() event-undefined claim; needs function body (Prompter.qml:547)
- **gpt:** ⚠️ PARTIAL (58) — observed rewind()/fastForward() event undefined - winding state permanently locked after first use (src/prompter/Prompter.qml:547)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:547-571: rewind/fastForward access 'event.key' but accept no event parameter; event=undefined; winding permanently locked

### [FD-N01] || should be && in autoReload guard — user preference ignored for non-binary files  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1025`
- **opus:** ⚠️ PARTIAL (55) — !skipAutoReload || autoReload() likely should be &&; ambiguous (documenthandler.cpp:1025)
- **gpt:** ⚠️ PARTIAL (58) — observed || should be && in autoReload guard - user preference ignored for non-binary files (src/documenthandler.cpp:1025)
- **deepseek:** ✅ LEGIT (90) — !skipAutoReload||autoReload() always true when skipAutoReload=false; user autoReload setting ignored at documenthandler.cpp:1025

### [FINAL-10] Two animations target same `position` property — conflict  ·  _SPLIT_  ·  High
`src/prompter/Prompter.qml:839,909`
- **opus:** ⚠️ PARTIAL (55) — Behavior + NumberAnimation both on position (Prompter.qml:839,909)
- **gpt:** ⚠️ PARTIAL (58) — observed Two animations target same position property - conflict (src/prompter/Prompter.qml:839)
- **deepseek:** ✅ LEGIT (90) — Prompter.qml:839 Behavior on position AND line 909 NumberAnimation on position both target prompter.position — conflicting animations

### [FINAL-14] Wrong placeholder `%0` instead of `%1` — font name never displayed  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/EditorToolbar.qml:588`
- **opus:** ⚠️ PARTIAL (55) — qsTr('Active font: %0'); %0 unconventional, Qt arg() handling uncertain (EditorToolbar.qml:588)
- **gpt:** ⚠️ PARTIAL (58) — Qt arg can substitute %0; this is unconventional, not proven broken (src/kirigami_ui/EditorToolbar.qml:588)
- **deepseek:** ✅ LEGIT (98) — EditorToolbar.qml:588 qsTr('Active font: %0').arg() — Qt arg() uses 1-based placeholders(%1); %0 treated as literal font name never displayed

### [FINAL-15] Missing edit block wrapping in setLineHeight/setParagraphHeight  ·  _SPLIT_  ·  High
`src/documenthandler.cpp:1596,1610`
- **opus:** ⚠️ PARTIAL (55) — joinPreviousEditBlock undo-grouping; restatement of R3-DOC-02 (documenthandler.cpp:1596)
- **gpt:** ⚠️ PARTIAL (58) — observed Missing edit block wrapping in setLineHeight/setParagraphHeight (src/documenthandler.cpp:1596)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:1596/1610 joinPreviousEditBlock() no-op without beginEditBlock; endEditBlock() unmatched — same as R3-DOC-02(duplicate finding)

### [FINAL-16] Countdown completion uses state++ bypassing toggle() entry actions  ·  _SPLIT_  ·  Critical
`src/prompter/Countdown.qml:122-123`
- **opus:** ❔ UNSURE (50) — state++ bypasses toggle() side-effects; state-machine claim (Countdown.qml:122)
- **gpt:** ⚠️ PARTIAL (58) — observed Countdown completion uses state++ bypassing toggle() entry actions (src/prompter/Countdown.qml:122)
- **deepseek:** ✅ LEGIT (80) — Countdown.qml:122-123 prompter.state++ increments enum int directly — bypasses toggle() entry/exit actions and state transition guards

### [FINAL-22] Behavior.onRunningChanged calls toggle() from within animation handler — re-entrant state change  ·  _SPLIT_  ·  High
`src/prompter/Prompter.qml:855`
- **opus:** ⚠️ PARTIAL (50) — toggle() in animation onRunningChanged; likely intended end-of-scroll (Prompter.qml:855)
- **gpt:** ⚠️ PARTIAL (58) — observed Behavior.onRunningChanged calls toggle() from within animation handler - re-entrant state chang (src/prompter/Prompter.qml:855)
- **deepseek:** ✅ LEGIT (85) — Prompter.qml:855 return prompter.toggle() inside Behavior.onRunningChanged animation handler — re-entrant state change during animation callback

### [FLOW-N02] increaseVelocity()/decreaseVelocity() skip velocity change when paused  ·  _SPLIT_  ·  Medium
`Prompter.qml:494-497,510-513`
- **opus:** ❔ UNSURE (45) — increase/decreaseVelocity skip change when paused; domain (Prompter.qml:494)
- **gpt:** ⚠️ PARTIAL (58) — observed increaseVelocity()/decreaseVelocity() skip velocity change when paused (src/prompter/Prompter.qml:494)
- **deepseek:** ✅ LEGIT (90) — Prompter.qml:494-497/510-513: increaseVelocity/decreaseVelocity gate __i modification on this.__play; when paused __i never changes but __play=true & position updated — behavioral inconsistency

### [FOC-N03] Tab/Backtab asymmetry — Backtab silently unhandled  ·  _SPLIT_  ·  Low
`Prompter.qml:2170-2173`
- **opus:** ⚠️ PARTIAL (50) — Tab/Backtab asymmetry; Backtab unhandled (Prompter.qml:2170)
- **gpt:** ✅ LEGIT (78) — Tab/Backtab asymmetry - Backtab silently unhandled (src/prompter/Prompter.qml:2170)
- **deepseek:** ✅ LEGIT (85) — Keys.onPressed handles Qt.Key_Tab but not Qt.Key_Backtab; Shift+Tab silently unhandled (Prompter.qml:2170-2173)

### [FONT-METRIC-01] pixelSize used as line-height proxy — core scroll timing off by ~57%  ·  _SPLIT_  ·  High
`Prompter.qml:119-122,125,128`
- **opus:** ❔ UNSURE (40) — pixelSize-as-lineheight scroll-timing heuristic; '57%' unverifiable (Prompter.qml:119)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Prompter.qml:119)
- **deepseek:** ✅ LEGIT (90) — Prompter.qml:119-122: fontSize (pixelSize=em-size) used as line-height proxy; actual height ~1.57x; __relativeSpeed ~57% off

### [FONT-METRIC-02] FontLoader status never checked — font substitution silently fails  ·  _SPLIT_  ·  Medium
`Prompter.qml:995-998`
- **opus:** ⚠️ PARTIAL (50) — FontLoader status never checked; substitution silent (Prompter.qml:995)
- **gpt:** ⚠️ PARTIAL (58) — observed FontLoader status never checked - font substitution silently fails (src/prompter/Prompter.qml:995)
- **deepseek:** ✅ LEGIT (85) — Prompter.qml:995-998: FontLoader source set but status never checked; corrupted/missing font silently substituted with no error

### [FONT-METRIC-03] fontFamily() returns resolved-family not requested-family — substitution invisible  ·  _SPLIT_  ·  Low
`documenthandler.cpp:493-501`
- **opus:** ❔ UNSURE (40) — fontFamily returns the format's family list; resolved-vs-requested unclear (documenthandler.cpp:500)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/documenthandler.cpp:493)
- **deepseek:** ✅ LEGIT (85) — documenthandler.cpp:493-501: fontFamilies() returns resolved-family list; if user selects unavailable font getter returns substitution name

### [FONT-N01] font.family: "Monospace" never resolves — no such font on any OS  ·  _SPLIT_  ·  Medium
`TimerClock.qml:149,161`
- **opus:** ⚠️ PARTIAL (45) — 'Monospace' resolves via Qt font matching on most OS (TimerClock.qml:149)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/TimerClock.qml:149)
- **deepseek:** ✅ LEGIT (95) — TimerClock.qml:149/161: font.family:'Monospace' does exact case-insensitive matching; no font named Monospace on any OS — should use families:['monospace'] for CSS generic resolution

### [FONT-N02] FontLoader id typo: westernSeriousSansfFont — stray 'f' in "Sans"  ·  _SPLIT_  ·  Low
`EditorToolbar.qml:558, Prompter.qml:996`
- **opus:** ✅ LEGIT (65) — FontLoader id typo westernSeriousSansfFont stray f (EditorToolbar.qml:558)
- **gpt:** ⚠️ PARTIAL (58) — observed FontLoader id typo: westernSeriousSansFont - stray 'f' in "Sans" (src/kirigami_ui/EditorToolbar.qml:558)
- **deepseek:** ✅ LEGIT (95) — EditorToolbar.qml:558/Prompter.qml:996: FontLoader id westernSeriousSansfFont — stray f in Sansf; zero runtime impact (only id) but confusing for maintainers

### [GEO-01] main.qml initial 728px height too large for 1366x768 laptops  ·  _SPLIT_  ·  Low
`main.qml:77-78, +windows/main.qml`
- **opus:** ⚠️ PARTIAL (45) — initial 728px height large for 1366x768 (main.qml:77)
- **gpt:** ⚠️ PARTIAL (58) — observed main.qml initial 728px height too large for 1366x768 laptops (src/kirigami_ui/main.qml:77)
- **deepseek:** ✅ LEGIT (80) — 728px initial height at main.qml:78 + taskbar exceeds 1366x768 desktop area

### [GEO-02] main.qml persists x/y/width/height with zero validation  ·  _SPLIT_  ·  Medium
`main.qml:85-91, +windows/main.qml`
- **opus:** ⚠️ PARTIAL (50) — persists x/y/w/h with no on-restore validation; can restore off-screen (main.qml:85)
- **gpt:** ⚠️ PARTIAL (58) — observed main.qml persists x/y/width/height with zero validation (src/kirigami_ui/main.qml:85)
- **deepseek:** ✅ LEGIT (90) — Settings alias x/y/width/height at main.qml:87-90 — no screen bounds validation on restore

### [GEO-03] +android/main.qml no minimumWidth/minimumHeight  ·  _SPLIT_  ·  Low
`+android/main.qml`
- **opus:** ⚠️ PARTIAL (40) — +android no minimumWidth/Height (main.qml)
- **gpt:** ⚠️ PARTIAL (58) — observed +android/main.qml no minimumWidth/minimumHeight (src/kirigami_ui/+android/main.qml:1)
- **deepseek:** ✅ LEGIT (90) — +android/main.qml lacks minimumWidth/minimumHeight — base variant has 351/291

### [GSW-N01] MarkersDrawer SwipeListItem navigates on swipe — gesture conflict on touch  ·  _SPLIT_  ·  Medium
`MarkersDrawer.qml:70-74`
- **opus:** ⚠️ PARTIAL (45) — SwipeListItem navigates on swipe; gesture conflict (MarkersDrawer.qml:70)
- **gpt:** ⚠️ PARTIAL (58) — observed MarkersDrawer SwipeListItem navigates on swipe - gesture conflict on touch (src/kirigami_ui/MarkersDrawer.qml:70)
- **deepseek:** ✅ LEGIT (90) — MarkersDrawer.qml:70-74: SwipeListItem onPressed fires at start of every touch including swipe; navigating to marker+closing drawer on swipe-to-reveal gesture conflict

### [GSW-N02] Flickable onDragStarted uses stale __iBackup after non-prompting drags  ·  _SPLIT_  ·  Low
`Prompter.qml:773-781,788-798`
- **opus:** ❔ UNSURE (45) — onDragStarted stale __iBackup; domain (Prompter.qml:773)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Prompter.qml:773)
- **deepseek:** ✅ LEGIT (85) — Prompter.qml:773-781/788-798: onMovementEnded leaves __iBackup non-zero in editing mode; second drag guard (line 776) prevents backup — stale first-drag velocity restored

### [HDR-N01] promptsession.h not in CMakeLists.txt — SessionModel/DataPoint dead code  ·  _SPLIT_  ·  Low
`src/promptsession.h, src/promptsess.cpp, src/CMakeLists.txt`
- **opus:** ✅ LEGIT (60) — promptsession.h/cpp not in CMakeLists; SessionModel dead code (promptsession.h)
- **gpt:** ⚠️ PARTIAL (58) — observed promptsession.h not in CMakeLists.txt - SessionModel/DataPoint dead code (src/promptsession.h:1)
- **deepseek:** ✅ LEGIT (95) — prompsession.h/cpp not in src/CMakeLists.txt — never MOC-processed never compiled dead code

### [HDR-N02] telemetry.h not in CMakeLists.txt — Telemetry dead code  ·  _SPLIT_  ·  Low
`src/telemetry.h, src/telemetry.cpp, src/CMakeLists.txt`
- **opus:** ✅ LEGIT (60) — telemetry.h not in CMakeLists; Telemetry dead code (telemetry.h)
- **gpt:** ⚠️ PARTIAL (58) — observed telemetry.h not in CMakeLists.txt - Telemetry dead code (src/telemetry.h:1)
- **deepseek:** ✅ LEGIT (95) — telemetry.h/cpp not in src/CMakeLists.txt — Q_OBJECT class never compiled dead code

### [HK-N01] Missing event.isAutoRepeat guard on main Keys.onPressed  ·  _SPLIT_  ·  High
`Prompter.qml:2672`
- **opus:** ⚠️ PARTIAL (50) — no event.isAutoRepeat guard on main Keys.onPressed; impact varies (Prompter.qml:2672)
- **gpt:** ⚠️ PARTIAL (58) — observed Missing event.isAutoRepeat guard on main Keys.onPressed (src/prompter/Prompter.qml:2672)
- **deepseek:** ✅ LEGIT (90) — Keys.onPressed at Prompter.qml:2672 — no event.isAutoRepeat guard repeat-fire on held keys

### [HK-N03] platformName() != "wayland" fails on "wayland-egl" — global hotkeys dead  ·  _SPLIT_  ·  High
`globalhotkeys.cpp:16 sites`
- **opus:** ⚠️ PARTIAL (50) — platformName()!='wayland' could miss 'wayland-egl'; Qt usually reports 'wayland' (globalhotkeys.cpp)
- **gpt:** ⚠️ PARTIAL (58) — observed platformName() != "wayland" fails on "wayland-egl" - global hotkeys dead (src/globalhotkeys.cpp:822)
- **deepseek:** ✅ LEGIT (90) — platform!='wayland' at globalhotkeys.cpp:119 fails on 'wayland-egl' — all global hotkeys dead

### [HK-N04] No auto-repeat guard in key-binding configuration Keys.onPressed  ·  _SPLIT_  ·  Medium
`KeyInputButton.qml:103`
- **opus:** ⚠️ PARTIAL (45) — no auto-repeat guard in key-binding Keys.onPressed (KeyInputButton.qml:103)
- **gpt:** ⚠️ PARTIAL (58) — observed No auto-repeat guard in key-binding configuration Keys.onPressed (src/kirigami_ui/KeyInputButton.qml:103)
- **deepseek:** ✅ LEGIT (85) — Keys.onPressed at KeyInputButton.qml:103 — no auto-repeat guard races with toggleButtonsOff

### [HK-N06] isValidInput checks local keybindings only — silent conflict with global hotkeys  ·  _SPLIT_  ·  Low
`KeyInputButton.qml:62-85`
- **opus:** ⚠️ PARTIAL (45) — isValidInput checks local keybinds only (KeyInputButton.qml:62)
- **gpt:** ⚠️ PARTIAL (58) — observed isValidInput checks local keybindings only - silent conflict with global hotkeys (src/kirigami_ui/KeyInputButton.qml:62)
- **deepseek:** ✅ LEGIT (80) — isValidInput at KeyInputButton.qml:62 checks only local prompter.keys — silent conflict with global hotkeys

### [HSCROLL-N01] InputsOverlay Flickables use contentWidth: width instead of implicitWidth — horizontal overflow clipped  ·  _SPLIT_  ·  Medium
`InputsOverlay.qml:95,552`
- **opus:** ⚠️ PARTIAL (50) — Flickable contentWidth:width vs implicitWidth (InputsOverlay.qml:95)
- **gpt:** ⚠️ PARTIAL (58) — observed InputsOverlay Flickables use contentWidth: width instead of implicitWidth - horizontal overflow (src/kirigami_ui/InputsOverlay.qml:95)
- **deepseek:** ✅ LEGIT (95) — InputsOverlay.qml:95 552: contentWidth set to Flickable's own width via buttonGrid.width/hotkeyGrid.width; horizontal overflow clipped

### [HSCROLL-N02] Inner Flickables missing flickableDirection: VerticalFlick — conflict with parent horizontal ListView  ·  _SPLIT_  ·  Medium
`InputsOverlay.qml:92,549`
- **opus:** ⚠️ PARTIAL (50) — inner Flickables missing flickableDirection (InputsOverlay.qml:92)
- **gpt:** ⚠️ PARTIAL (58) — observed Inner Flickables missing flickableDirection: VerticalFlick - conflict with parent horizontal Li (src/kirigami_ui/InputsOverlay.qml:92)
- **deepseek:** ✅ LEGIT (90) — InputsOverlay.qml:92 549: inner Flickables lack flickableDirection:VerticalFlick; default AutoFlickDirection intercepts horizontal tab swipes

### [HTK-01] KGlobalAccel default permanently destroyed on first user customization  ·  _SPLIT_  ·  Critical
`globalhotkeys.cpp:1130,1138`
- **opus:** ❔ UNSURE (45) — KGlobalAccel default/override logic; needs customization-path trace (globalhotkeys.cpp:1130)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/globalhotkeys.cpp:1130)
- **deepseek:** ✅ LEGIT (95) — removeAllShortcuts at 1130 clears default+user then reads already-cleared default at 1138; defaults lost (globalhotkeys.cpp:1130 1138)

### [HTK-02] User shortcuts never persisted when only Use_GlobalAccel defined (no QHotkey)  ·  _SPLIT_  ·  High
`globalhotkeys.cpp:831`
- **opus:** ❔ UNSURE (45) — QSettings save under #ifdef QHotkey; KGlobalAccel persists itself (globalhotkeys.cpp:831)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/globalhotkeys.cpp:831)
- **deepseek:** ✅ LEGIT (92) — QSettings save gated on #ifdef QHotkey_FOUND; KDE-only builds never persist shortcuts (globalhotkeys.cpp:831)

### [HTK-03] KGlobalAccel defaults silently zeroed on non-Wayland when QHotkey co-exists  ·  _SPLIT_  ·  High
`globalhotkeys.cpp:1123-1127,1132`
- **opus:** ⚠️ PARTIAL (50) — KGlobalAccel shortcut zeroed on non-Wayland when QHotkey co-exists; by-design (globalhotkeys.cpp:1123)
- **gpt:** ⚠️ PARTIAL (58) — observed KGlobalAccel defaults silently zeroed on non-Wayland when QHotkey co-exists (src/globalhotkeys.cpp:1123)
- **deepseek:** ✅ LEGIT (90) — on non-Wayland key->unknown/modifiers->NoModifier before setDefault; zeroed fallback (globalhotkeys.cpp:1123-1127)

### [HTK-05] VelocityTo0 default shortcut uses `Qt::Key_acute` — unreachable dead key  ·  _SPLIT_  ·  Medium
`globalhotkeys.cpp:657`
- **opus:** ⚠️ PARTIAL (50) — Qt::Key_acute default; obscure but intentional (globalhotkeys.cpp:657)
- **gpt:** ⚠️ PARTIAL (58) — observed VelocityTo0 default shortcut uses Qt::Keyacute - unreachable dead key (src/globalhotkeys.cpp:657)
- **deepseek:** ✅ LEGIT (90) — Qt::Key_acute is combining dead key unreachable via physical US/ANSI keyboard (globalhotkeys.cpp:657)

### [HTK-06] Pause (Ctrl+Space) and Stop (Meta+Space) conflict — Meta+Space captured by OS  ·  _SPLIT_  ·  Medium
`globalhotkeys.cpp:581,586`
- **opus:** ⚠️ PARTIAL (45) — Ctrl/Meta+Space shortcut OS-conflict; environment (globalhotkeys.cpp:581)
- **gpt:** ⚠️ PARTIAL (58) — observed Pause (Ctrl+Space) and Stop (Meta+Space) conflict - Meta+Space captured by OS (src/globalhotkeys.cpp:581)
- **deepseek:** ✅ LEGIT (90) — Stop uses Meta/Win+Space captured by Windows Start Menu/GNOME/macOS Spotlight (globalhotkeys.cpp:581 586)

### [HTK-07] Double `removeAllShortcuts()` IPC round-trip in customization path  ·  _SPLIT_  ·  Low
`globalhotkeys.cpp:1130,1139`
- **opus:** ⚠️ PARTIAL (45) — double removeAllShortcuts() IPC round-trip (globalhotkeys.cpp:1130)
- **gpt:** ⚠️ PARTIAL (58) — observed Double removeAllShortcuts() IPC round-trip in customization path (src/globalhotkeys.cpp:1130)
- **deepseek:** ✅ LEGIT (88) — removeAllShortcuts called unconditionally at 1130 then again at 1139; redundant D-Bus round-trip (globalhotkeys.cpp:1130 1139)

### [HTK-08] key/modifiers parameters silently discarded mid-function on non-Wayland  ·  _SPLIT_  ·  Low
`globalhotkeys.cpp:1123-1127`
- **opus:** ⚠️ PARTIAL (50) — key/modifiers zeroed mid-function on non-Wayland; by-design (globalhotkeys.cpp:1123)
- **gpt:** ⚠️ PARTIAL (58) — observed key/modifiers parameters silently discarded mid-function on non-Wayland (src/globalhotkeys.cpp:1123)
- **deepseek:** ✅ LEGIT (85) — key/modifiers by-value params overwritten mid-function; misleading signature obscured HTK-01/03 (globalhotkeys.cpp:1123-1127)

### [I18N-N01] Stale source-location line numbers in all 20 .ts files  ·  _SPLIT_  ·  Low
`po/*.ts (20 files)`
- **opus:** ⚠️ PARTIAL (40) — stale source-location line numbers in .ts files; harmless
- **gpt:** ⚠️ PARTIAL (58) — observed Stale source-location line numbers in all 20 .ts files (po/qprompt_en.ts:1)
- **deepseek:** ✅ LEGIT (80) — lupdate not re-run — source line numbers in 20 .ts files stale Qt Linguist navigation broken

### [I18N-N02] Vanished translation entries not purged across 13 language files  ·  _SPLIT_  ·  Low
`13 of 20 .ts files (de:14, es:14, pt_PT:13, ru:13, uk:13, zh:13, pt_BR:10, cs:8, fr:8, fi:4, ko:4, nl:4, oc:2)`
- **opus:** ⚠️ PARTIAL (40) — vanished translation entries not purged; harmless
- **gpt:** ⚠️ PARTIAL (58) — observed Vanished translation entries not purged across 13 language files (po/qprompt_de.ts:14)
- **deepseek:** ✅ LEGIT (80) — 13 .ts files contain type='vanished' entries — not cleaned with lupdate -no-obsolete

### [IMP-N01] import Qt.labs.platform 1.1 — Menu/MenuBar/MenuItem dropped in Qt 6  ·  _SPLIT_  ·  Critical
`src/kirigami_ui/main.qml:29,617-922`
- **opus:** ❌ FALSE (60) — Qt.labs.platform Menu/MenuBar/MenuItem still exist in Qt 6; ships & works (main.qml:29)
- **gpt:** ❌ FALSE (76) — Qt.labs.platform types are still used here under Qt 6 (src/kirigami_ui/main.qml:29)
- **deepseek:** ⚠️ PARTIAL (75) — main.qml:29 imports Qt.labs.platform 1.1 — Qt6.2+ re-added Labs Platform module with version mapping; but exact 1.1->6.x mapping depends on Qt build

### [IMP-NEW-03] main.cpp:38-39 redundant #include \<QtQml/qqml.h\> + #include \<QtQml\>  ·  _SPLIT_  ·  Low
`main.cpp:38-39`
- **opus:** ⚠️ PARTIAL (40) — redundant QtQml/qqml.h + QtQml includes (main.cpp:38)
- **gpt:** ⚠️ PARTIAL (58) — observed main.cpp:38-39 redundant #include \QtQml/qqml.h\ + #include \QtQml\ (src/main.cpp:38)
- **deepseek:** ✅ LEGIT (95) — <QtQml/qqml.h> at main.cpp:38 redundant with <QtQml> at line 39 — umbrella already includes it

### [IMP-NEW-04] AboutPage.qml imports Kirigami 2.9 vs 2.11 in all other files  ·  _SPLIT_  ·  Low
`AboutPage.qml:22`
- **opus:** ⚠️ PARTIAL (40) — AboutPage imports Kirigami 2.9 vs 2.11; works (AboutPage.qml:22)
- **gpt:** ⚠️ PARTIAL (58) — observed AboutPage.qml imports Kirigami 2.9 vs 2.11 in all other files (src/kirigami_ui/AboutPage.qml:22)
- **deepseek:** ✅ LEGIT (90) — AboutPage.qml:22 imports Kirigami 2.9 — all other files use 2.11 CMake requires 6.9.0=2.11+

### [IMP-NEW-05] pointers.qrc RESOURCE_PREFIX conflicts with qt_add_qml_module  ·  _SPLIT_  ·  Low (orphaned QRC, never compiled)
`pointers.qrc:2, src/CMakeLists.txt:253`
- **opus:** ❔ UNSURE (45) — pointers.qrc RESOURCE_PREFIX vs qt_add_qml_module; domain (CMakeLists.txt:2)
- **gpt:** ⚠️ PARTIAL (58) — observed pointers.qrc RESOURCEPREFIX conflicts with qtaddqmlmodule (src/prompter/pointers/pointers.qrc:2)
- **deepseek:** ⚠️ PARTIAL (80) — pointers.qrc prefix conflicts with qt_add_qml_module at src/CMakeLists.txt:253 but QRC is orphaned never compiled

### [INIT-N04] PrompterView ShaderEffectSource.sourceItem references prompter id declared later  ·  _SPLIT_  ·  Low
`PrompterView.qml:230-236`
- **opus:** ⚠️ PARTIAL (40) — sourceItem refs prompter id; QML id resolution is order-independent (PrompterView.qml:230)
- **gpt:** ⚠️ PARTIAL (58) — observed PrompterView ShaderEffectSource.sourceItem references prompter id declared later (src/prompter/PrompterView.qml:230)
- **deepseek:** ❌ FALSE (80) — QML id resolution is order-independent across component scope (PrompterView.qml:230-236)

### [INT-N01] quint64→int narrowing at DocumentHandler→MarkersModel boundary (4 sites)  ·  _SPLIT_  ·  Low
`documenthandler.cpp:1713,1721, markersmodel.h:62-63`
- **opus:** ⚠️ PARTIAL (45) — quint64->int narrowing at marker boundary; docs never exceed INT_MAX (documenthandler.cpp:1713)
- **gpt:** ⚠️ PARTIAL (58) — observed quint64->int narrowing at DocumentHandler->MarkersModel boundary (4 sites) (src/documenthandler.cpp:1713)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:1713/1721: quint64->int narrowing when Q_INVOKABLE passes position to MarkersModel (takes int); markersmodel.h:62-63 confirm int params — 4 sites

### [INT-N02] replaceAll() returns long — 32-bit overflow on Windows x64  ·  _SPLIT_  ·  Medium
`documenthandler.h:228, documenthandler.cpp:1494`
- **opus:** ⚠️ PARTIAL (40) — replaceAll long is 32-bit on Win64; overflow practically impossible (documenthandler.cpp:1494)
- **gpt:** ✅ LEGIT (78) — replaceAll() returns long - 32-bit overflow on Windows x64 (src/documenthandler.h:228)
- **deepseek:** ✅ LEGIT (90) — documenthandler.h:228 / cpp:1494: replaceAll() returns long which is 32-bit on Windows x64 (LLP64); replacement counter overflows at 2^31 matches — use qlonglong

### [INT-N03] 6 qsizetype→int narrowing conversions across models and loops  ·  _SPLIT_  ·  Low
`markersmodel.cpp:101,121, promptsession.cpp:88, main.cpp:274, spellchecker.cpp:98,328`
- **opus:** ⚠️ PARTIAL (40) — qsizetype->int narrowing 6 sites (markersmodel.cpp:101)
- **gpt:** ⚠️ PARTIAL (58) — observed 6 qsize_type->int narrowing conversions across models and loops (src/markersmodel.cpp:101)
- **deepseek:** ✅ LEGIT (80) — markersmodel.cpp:101/121 promptsession.cpp:88 main.cpp:274 spellchecker.cpp:98/328: qsizetype size()/length()/indexOf() narrowed to int (32-bit); practical docs within range

### [INT-N04] OBS URL/Password fields disabled when WebSocket enabled — inverted logic  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:1478,1500`
- **opus:** ✅ LEGIT (55) — OBS URL/Password fields disabled when WebSocket enabled; inverted (PrompterPage.qml:1478)
- **gpt:** ⚠️ PARTIAL (58) — observed OBS URL/Password fields disabled when WebSocket enabled - inverted logic (src/kirigami_ui/PrompterPage.qml:1478)
- **deepseek:** ✅ LEGIT (85) — PrompterPage.qml:1484: wsUrlField.enabled: !enabledToggle.checked; fields disabled when WebSocket on; cannot reconfigure without disconnect

### [INT-N05] PropertyChanges permanently destroys CheckBox checked bindings on PointerSettings tab switch  ·  _SPLIT_  ·  Medium
`PointerSettings.qml:70-83`
- **opus:** ✅ LEGIT (55) — PropertyChanges destroys CheckBox checked bindings (PointerSettings.qml:70)
- **gpt:** ⚠️ PARTIAL (58) — observed PropertyChanges permanently destroys CheckBox checked bindings on PointerSettings tab switch (src/prompter/PointerSettings.qml:70)
- **deepseek:** ✅ LEGIT (90) — PointerSettings.qml:70-83: Arrow state PropertyChanges overwrites checked/enabled bindings; checkboxes permanently desync after tab switch

### [INV-N01] QmlUtil::r() stores QML-owned QQuickItemGrabResult raw pointer — use-after-free  ·  _SPLIT_  ·  Medium
`qmlutil.hpp:175-180, main.qml:1045`
- **opus:** ⚠️ PARTIAL (50) — r() stores QML-owned grab-result raw ptr + deleteLater; UAF risk (qmlutil.hpp:175)
- **gpt:** ✅ LEGIT (78) — QmlUtil::r() stores QML-owned QQuickItemGrabResult raw pointer - use-after-free (src/qmlutil.hpp:175)
- **deepseek:** ✅ LEGIT (85) — Raw QQuickItemGrabResult* store at qmlutil.hpp:179 — QML GC may free while C++ holds pointer

### [IO-N01] saveAs() leaves _fileSystemWatcher permanently blocked on open failure  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1143,1161`
- **opus:** ⚠️ PARTIAL (45) — saveAs open-failure path may skip watcher unblock (documenthandler.cpp:1143)
- **gpt:** ✅ LEGIT (78) — saveAs() leaves _fileSystemWatcher permanently blocked on open failure (src/documenthandler.cpp:1143)
- **deepseek:** ✅ LEGIT (90) — _fileSystemWatcher->blockSignals(true) at documenthandler.cpp:1143; early return skips unblock at 1170

### [JS-N01] TIMERCLOCK getTimeString() — redundant .toString() on already-string — 54 allocs/sec  ·  _SPLIT_  ·  Low
`TimerClock.qml:46-50`
- **opus:** ✅ LEGIT (50) — redundant .toString() on toFixed() result (TimerClock.qml:46)
- **gpt:** ⚠️ PARTIAL (58) — observed TIMERCLOCK getTimeString() - redundant .toString() on already-string - 54 allocs/sec (src/prompter/TimerClock.qml:46)
- **deepseek:** ✅ LEGIT (70) — TimerClock.qml:50: toFixed(2) already returns String; redundant .toString() creates extra allocs; minor GC pressure

### [JS-N02] markerCompare() per-frame JSON.stringify() over OBS marker — 60 allocs/sec  ·  _SPLIT_  ·  Medium
`Prompter.qml:401-413`
- **opus:** ⚠️ PARTIAL (50) — per-frame JSON.stringify over OBS marker; allocations (Prompter.qml:401)
- **gpt:** ⚠️ PARTIAL (58) — observed markerCompare() per-frame JSON.stringify() over OBS marker - 60 allocs/sec (src/prompter/Prompter.qml:401)
- **deepseek:** ✅ LEGIT (85) — Prompter.qml:401-413: markerCompare fires every frame; JSON.stringify + object creation 60fps; severe GC pressure during OBS prompting

### [JSN-02] ws.sendTextMessage() called without checking WebSocket status  ·  _SPLIT_  ·  Medium
`Prompter.qml:383,413`
- **opus:** ⚠️ PARTIAL (50) — sendTextMessage without checking ws.status (Prompter.qml:383)
- **gpt:** ✅ LEGIT (78) — ws.sendTextMessage() called without checking WebSocket status (src/prompter/Prompter.qml:383)
- **deepseek:** ✅ LEGIT (90) — ws.sendTextMessage() at Prompter.qml:383 413 without ws.status===WebSocket.Open guard

### [KB-N01] Find.qml: 9 toolbar buttons missing focusPolicy — keyboard-invisible  ·  _SPLIT_  ·  Medium
`Find.qml`
- **opus:** ⚠️ PARTIAL (45) — 9 Find buttons missing focusPolicy; keyboard (Find.qml)
- **gpt:** ⚠️ PARTIAL (58) — observed Find.qml: 9 toolbar buttons missing focusPolicy - keyboard-invisible (src/prompter/Find.qml:1)
- **deepseek:** ✅ LEGIT (85) — Find.qml ToolButtons lack focusPolicy:Qt.TabFocus; keyboard Tab navigation skips Find toolbar entirely

### [KB-N02] InputsOverlay TabBar TabButtons have no focusPolicy + keyNavigationEnabled: false — keyboard dead  ·  _SPLIT_  ·  Medium
`InputsOverlay.qml:57-63,85`
- **opus:** ⚠️ PARTIAL (55) — TabButtons no focusPolicy + keyNavigationEnabled:false (InputsOverlay.qml:57)
- **gpt:** ⚠️ PARTIAL (58) — observed InputsOverlay TabBar TabButtons have no focusPolicy + keyNavigationEnabled: false - keyboard de (src/kirigami_ui/InputsOverlay.qml:57)
- **deepseek:** ✅ LEGIT (85) — TabButtons default Qt.NoFocus + keyNavigationEnabled:false; keyboard users cannot switch tabs

### [KB-N03] +windows and +android ESC handler uses .focus instead of .activeFocus — wrong boolean  ·  _SPLIT_  ·  Medium
`+windows/main.qml:483, +android/main.qml:422`
- **opus:** ⚠️ PARTIAL (50) — +windows/+android ESC uses .focus where .activeFocus intended (main.qml:483)
- **gpt:** ⚠️ PARTIAL (58) — observed +windows and +android ESC handler uses .focus instead of .activeFocus - wrong boolean (src/kirigami_ui/+windows/main.qml:483)
- **deepseek:** ❌ FALSE (80) — Claim states 'Base main.qml correctly uses activeFocus' but base also uses .focus at lines 509 511 — factually wrong

### [KEY-N01] Named marker key binding silently discards all modifier information  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:1187, documenthandler.h:213, documenthandler.cpp:707-715, markersmodel.cpp:117-120`
- **opus:** ❔ UNSURE (45) — named-marker stores key_<code>; modifier-loss is a domain claim (documenthandler.cpp:707)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/kirigami_ui/PrompterPage.qml:1187)
- **deepseek:** ✅ LEGIT (70) — keyCode stored as bare int via toInt; Ctrl/Shift/Alt/Meta modifier info lost (documenthandler.cpp:757)

### [LAY-N01] 10 Labels with Layout.margins but inside MouseArea, not direct layout child — dead  ·  _SPLIT_  ·  Low
`EditorToolbar.qml (10 Labels)`
- **opus:** ⚠️ PARTIAL (45) — Labels with Layout.margins inside MouseArea not layout child; dead (EditorToolbar.qml)
- **gpt:** ⚠️ PARTIAL (58) — observed 10 Labels with Layout.margins but inside MouseArea, not direct layout child - dead (src/kirigami_ui/EditorToolbar.qml:1)
- **deepseek:** ❔ UNSURE (50) — LAY-N01: labels inside MouseArea children not direct RowLayout children so Layout.margins dead; structure plausible but not fully traced in EditorToolbar.qml hierarchy

### [LAY-N02] WheelSettingsOverlay explanation text constrained to single column in 2-column GridLayout  ·  _SPLIT_  ·  Low
`WheelSettingsOverlay.qml:100-109`
- **opus:** ⚠️ PARTIAL (40) — explanation text constrained to single column (WheelSettingsOverlay.qml:100)
- **gpt:** ⚠️ PARTIAL (58) — observed WheelSettingsOverlay explanation text constrained to single column in 2-column GridLayout (src/kirigami_ui/WheelSettingsOverlay.qml:100)
- **deepseek:** ❔ UNSURE (50) — LAY-N02: WheelSettingsOverlay.qml not fully read; claim about 1-column text in 2-column GridLayout cannot be verified without inspecting actual element hierarchy

### [LAZY-N01] namedMarkerConfiguration Loader double-loads KeyInputButton — first load wasted  ·  _SPLIT_  ·  Low
`PrompterPage.qml:1172-1179`
- **opus:** ⚠️ PARTIAL (45) — namedMarkerConfiguration Loader double-loads KeyInputButton (PrompterPage.qml:1172)
- **gpt:** ⚠️ PARTIAL (58) — observed namedMarkerConfiguration Loader double-loads KeyInputButton - first load wasted (src/kirigami_ui/PrompterPage.qml:1172)
- **deepseek:** ✅ LEGIT (85) — source:'KeyInputButton.qml' starts async load; Component.onCompleted setSource() cancels+reloads — first load wasted

### [LBL-N01] All 12 Sliders in EditorToolbar missing Layout.fillWidth: true — cramped  ·  _SPLIT_  ·  Medium
`EditorToolbar.qml (12 Slider instances)`
- **opus:** ⚠️ PARTIAL (45) — 12 Sliders missing Layout.fillWidth (EditorToolbar.qml)
- **gpt:** ⚠️ PARTIAL (58) — observed All 12 Sliders in EditorToolbar missing Layout.fillWidth: true - cramped (src/kirigami_ui/EditorToolbar.qml:1)
- **deepseek:** ✅ LEGIT (70) — EditorToolbar.qml: Sliders in RowLayout lack Layout.fillWidth — render at ~100px implicit width regardless of toolbar size; cramped controls on wide displays

### [LBL-N02] 11 Labels with Layout.bottomMargin: -14 — undefined behavior, overlap risk  ·  _SPLIT_  ·  Medium
`EditorToolbar.qml (11 Label instances)`
- **opus:** ⚠️ PARTIAL (40) — negative Layout.bottomMargin is valid (overlap) not UB (EditorToolbar.qml)
- **gpt:** ⚠️ PARTIAL (52) — observed 11 Labels with Layout.bottomMargin: -14 - undefined behavior, overlap risk (src/kirigami_ui/EditorToolbar.qml:1)
- **deepseek:** ✅ LEGIT (80) — EditorToolbar.qml: negative Layout.bottomMargin (-14) on RowLayout children is undefined per Qt docs; relies on accidental layout engine behavior

### [LBL-N03] PrompterView 3× height overflow in theforce debug mode  ·  _SPLIT_  ·  Low
`PrompterPage.qml:739`
- **opus:** ⚠️ PARTIAL (40) — PrompterView height overflow in theforce debug mode (PrompterPage.qml:739)
- **gpt:** ⚠️ PARTIAL (58) — observed PrompterView 3× height overflow in theforce debug mode (src/kirigami_ui/PrompterPage.qml:739)
- **deepseek:** ✅ LEGIT (85) — PrompterPage.qml:739: when root.theforce debug mode active height=3*parent.height; at min window (291px) produces 873px — off-screen render overhead

### [LDR-N01] InputsOverlay typeof null guard fails — null.item crash on rapid close  ·  _SPLIT_  ·  Medium
`InputsOverlay.qml:105-112,562-569`
- **opus:** ⚠️ PARTIAL (50) — typeof null guard can still hit null.item on rapid close (InputsOverlay.qml:105)
- **gpt:** ⚠️ PARTIAL (58) — observed InputsOverlay typeof null guard fails - null.item crash on rapid close (src/kirigami_ui/InputsOverlay.qml:105)
- **deepseek:** ✅ LEGIT (85) — typeof null==='object' at InputsOverlay.qml:107 — guard passes when Loader.item is null TypeError on .checked

### [LINK-N03] Qt::WebSockets found as REQUIRED but never explicitly linked  ·  _SPLIT_  ·  Medium
`CMakeLists.txt:145, all target_link_libraries blocks`
- **opus:** ⚠️ PARTIAL (50) — Qt::WebSockets found REQUIRED but not explicitly linked; QML plugin pulls it (CMakeLists.txt:145)
- **gpt:** ✅ LEGIT (78) — Qt::WebSockets found as REQUIRED but never explicitly linked (CMakeLists.txt:145)
- **deepseek:** ✅ LEGIT (85) — src/CMakeLists.txt: all target_link_libraries blocks lack Qt6::WebSockets; find_package REQUIRED but never linked — breaks static builds if qmlimportscanner misses it

### [LL-N01] 10 EditorToolbar MouseArea/TextField width-depends-on-width binding loops  ·  _SPLIT_  ·  Medium
`EditorToolbar.qml (10 instances, lines 924-2053)`
- **opus:** ⚠️ PARTIAL (50) — width-depends-on-width MouseArea/TextField binding-loop risk (EditorToolbar.qml)
- **gpt:** ⚠️ PARTIAL (58) — observed 10 EditorToolbar MouseArea/TextField width-depends-on-width binding loops (src/kirigami_ui/EditorToolbar.qml:924)
- **deepseek:** ✅ LEGIT (80) — MouseArea.width->TextField.width(anchors.fill:parent)->MouseArea.width binding loop; QML engine breaks loop->TextField width=0

### [LOAD-N01] TOCTOU race between QFile::exists() and file.open() in load()  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:944-947`
- **opus:** ⚠️ PARTIAL (50) — TOCTOU between exists() and open(); minor for desktop (documenthandler.cpp:944)
- **gpt:** ✅ LEGIT (78) — TOCTOU race between QFile::exists() and file.open() in load() (src/documenthandler.cpp:944)
- **deepseek:** ✅ LEGIT (65) — classic TOCTOU race between QFile::exists and file.open (documenthandler.cpp:944-947)

### [LOG-04] MarkersModel::extendLastMarker modifies data without emitting dataChanged  ·  _SPLIT_  ·  Medium
`src/markersmodel.cpp:109-114`
- **opus:** ✅ LEGIT (100) — extendLastMarker no dataChanged (markersmodel.cpp:109)
- **gpt:** ✅ LEGIT (78) — extendLastMarker changes the last row without dataChanged (src/markersmodel.cpp:109)
- **deepseek:** ⚠️ PARTIAL (60) — extendLastMarker mutates m_data w/o dataChanged at markersmodel.cpp:112; but method only called from parse() which rebuilds model — may be intentional internal helper

### [LOG-06] DocumentHandler::replaceAll has potential infinite loop with regex  ·  _SPLIT_  ·  Medium
`src/documenthandler.cpp:1492-1520`
- **opus:** ✅ LEGIT (90) — replaceAll regex infinite-loop risk (documenthandler.cpp:1504)
- **gpt:** ✅ LEGIT (78) — DocumentHandler::replaceAll has potential infinite loop with regex (src/documenthandler.cpp:1492)
- **deepseek:** ⚠️ PARTIAL (70) — replaceAll at doc.cpp:1504-1515 wraps in beginEditBlock; insertion length change shifts search; infinite if replacement contains searchPattern but edge-case dependent

### [LOG-N05] Q_UNREACHABLE() in m_setGlobalShortcut() — UB in release on new enum value  ·  _SPLIT_  ·  Medium
`globalhotkeys.cpp:1109`
- **opus:** ⚠️ PARTIAL (50) — Q_UNREACHABLE in m_setGlobalShortcut; reachability like EDGE-10 (globalhotkeys.cpp:1109)
- **gpt:** ⚠️ PARTIAL (58) — observed Q_UNREACHABLE() in m_setGlobalShortcut() - UB in release on new enum value (src/globalhotkeys.cpp:1109)
- **deepseek:** ✅ LEGIT (90) — globalhotkeys.cpp:1109: 33-case switch with no default + Q_UNREACHABLE(); if GlobalHotkeys::Action enum extended -> undefined behavior in release builds

### [LOG-N07] No error log in loadFromNetworkFinihed() — silent bad-data load  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:888-901`
- **opus:** ✅ LEGIT (55) — no error log on bad/empty network data (documenthandler.cpp:888)
- **gpt:** ⚠️ PARTIAL (58) — observed No error log in loadFromNetworkFinihed() - silent bad-data load (src/documenthandler.cpp:888)
- **deepseek:** ✅ LEGIT (95) — documenthandler.cpp:888-901: m_reply->readAll() without checking m_reply->error(); HTTP errors silently become document content with no warning log

### [LVW-N01] InputsOverlay.qml ListView currentIndex: PointerSettings.States.Arrow — copy-paste error  ·  _SPLIT_  ·  Low
`InputsOverlay.qml:77`
- **opus:** ⚠️ PARTIAL (45) — ListView currentIndex copy-paste PointerSettings.States.Arrow (InputsOverlay.qml:77)
- **gpt:** ⚠️ PARTIAL (58) — observed InputsOverlay.qml ListView currentIndex: PointerSettings.States.Arrow - copy-paste error (src/kirigami_ui/InputsOverlay.qml:77)
- **deepseek:** ✅ LEGIT (85) — InputsOverlay.qml:77: currentIndex: PointerSettings.States.Arrow — copy-paste from PointerSettings.qml; resolves to 0 accidentally but semantically wrong for 2-tab InputsOverlay

### [LYR-N01] InputsOverlay calls cursorAutoHide.restart() on open instead of reset()  ·  _SPLIT_  ·  High
`src/kirigami_ui/InputsOverlay.qml:41`
- **opus:** ⚠️ PARTIAL (60) — cursorAutoHide.restart() on open vs reset() elsewhere (dup R2-OVL-01) (InputsOverlay.qml:41)
- **gpt:** ✅ LEGIT (84) — InputsOverlay calls cursorAutoHide.restart() on open instead of reset() (src/kirigami_ui/InputsOverlay.qml:41)
- **deepseek:** ✅ LEGIT (85) — InputsOverlay.qml:41 onOpened calls cursorAutoHide.restart() instead of reset() — cursor auto-hides after 1s during key binding configuration

### [LYR-N02] Three OverlaySheets missing from ESC dismiss chain  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/main.qml:489-504`
- **opus:** ⚠️ PARTIAL (50) — three OverlaySheets missing from ESC dismiss chain (main.qml:489)
- **gpt:** ✅ LEGIT (78) — Three OverlaySheets missing from ESC dismiss chain (src/kirigami_ui/main.qml:489)
- **deepseek:** ✅ LEGIT (75) — main.qml:489-504 ESC if-else chain missing obsConfiguration/dictionariesSheet/customWordsSheet — these 3 sheets never dismissed by ESC

### [LYR-N03] ContextDrawer exposes prompter actions while viewing layer pages  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/main.qml:929`
- **opus:** ❔ UNSURE (45) — ContextDrawer exposes prompter actions on layer pages; UX (main.qml:929)
- **gpt:** ✅ LEGIT (78) — ContextDrawer exposes prompter actions while viewing layer pages (src/kirigami_ui/main.qml:929)
- **deepseek:** ✅ LEGIT (88) — depth<=1 true after clear; prompter actions shown on About/Paths pages should be depth<1 (main.qml:929)

### [LYR-N04] ESC handler uses activeFocus in base but focus in platform variants — inconsistent  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/main.qml:512 vs +windows:483 vs +android:422`
- **opus:** ⚠️ PARTIAL (50) — ESC uses activeFocus in base vs focus in variants; inconsistent (main.qml:512)
- **gpt:** ✅ LEGIT (78) — ESC handler uses activeFocus in base but focus in platform variants - inconsistent (src/kirigami_ui/main.qml:512)
- **deepseek:** ✅ LEGIT (85) — base uses prompter.activeFocus(512) windows/android use .focus(483/422); FocusScope activeFocus vs focus divergence (main.qml:512 +windows:483 +android:422)

### [MA-N01] overlayMouseArea permanently disabled — dead MouseArea  ·  _SPLIT_  ·  Low
`ReadRegionOverlay.qml:116-122`
- **opus:** ⚠️ PARTIAL (50) — overlayMouseArea permanently disabled; dead (ReadRegionOverlay.qml:116)
- **gpt:** ✅ LEGIT (78) — overlayMouseArea permanently disabled - dead MouseArea (src/prompter/ReadRegionOverlay.qml:116)
- **deepseek:** ✅ LEGIT (95) — overlayMouseArea at ReadRegionOverlay.qml:116 has enabled:false hardcoded — dead MouseArea

### [MENU-N01] contextMenu.popup(this) missing click coordinates — menu at wrong position  ·  _SPLIT_  ·  Medium
`Prompter.qml:1402`
- **opus:** ✅ LEGIT (55) — contextMenu.popup(this) without coordinates -> wrong position (Prompter.qml:1402)
- **gpt:** ⚠️ PARTIAL (58) — observed contextMenu.popup(this) missing click coordinates - menu at wrong position (src/prompter/Prompter.qml:1402)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:1402: contextMenu.popup(this) equivalent to popup(parent 0 0); mouse parameter with actual coordinates available but ignored — menu at wrong position on mobile/WASM

### [MENU-N02] Mobile "Add to dictionary" missing %1 placeholder — word never shown  ·  _SPLIT_  ·  Medium
`Prompter.qml:2620`
- **opus:** ✅ LEGIT (60) — mobile 'Add to dictionary' qsTr missing %1; word never shown (Prompter.qml:2620)
- **gpt:** ⚠️ PARTIAL (58) — observed Mobile "Add to dictionary" missing %1 placeholder - word never shown (src/prompter/Prompter.qml:2620)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:2620: qsTr('Add to dictionary') has no %1 placeholder; .arg(prompter.spellMisspelledWord) silently does nothing — word never shown to user

### [MENU-N03] Text alignment menu RTL swap: labels swap but actions don't  ·  _SPLIT_  ·  Medium
`EditorToolbar.qml:362-374`
- **opus:** ⚠️ PARTIAL (55) — RTL alignment menu: labels swap but actions don't (EditorToolbar.qml:362)
- **gpt:** ⚠️ PARTIAL (58) — observed Text alignment menu RTL swap: labels swap but actions don't (src/kirigami_ui/EditorToolbar.qml:362)
- **deepseek:** ✅ LEGIT (95) — EditorToolbar.qml:362-374: text labels swap for RTL (Left<->Right) but onTriggered actions hardcoded AlignLeft/AlignRight unconditionally; RTL clicking Right sets AlignLeft

### [MENU-N04] Trailing empty MenuSeparator at end of mobile context menu  ·  _SPLIT_  ·  Low
`Prompter.qml:2662`
- **opus:** ✅ LEGIT (50) — trailing empty MenuSeparator at end of context menu (Prompter.qml:2662)
- **gpt:** ⚠️ PARTIAL (58) — observed Trailing empty MenuSeparator at end of mobile context menu (src/prompter/Prompter.qml:2662)
- **deepseek:** ✅ LEGIT (75) — Prompter.qml:2662: trailing MenuSeparator with no items after it creates dangling separator line at bottom of mobile context menu

### [MENU-N05] "Redo" context menu item missing & accelerator  ·  _SPLIT_  ·  Low
`Prompter.qml:2633`
- **opus:** ⚠️ PARTIAL (45) — Redo menu item missing & accelerator (Prompter.qml:2633)
- **gpt:** ⚠️ PARTIAL (58) — observed "Redo" context menu item missing & accelerator (src/prompter/Prompter.qml:2633)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:2633: 'Redo' text lacks & accelerator prefix; all other menu items (&Undo line 2628 &Copy line 2639) have it — keyboard cycling skips Redo

### [META-N01] QMetaObject::invokeMethod return value unchecked — silent failure on WASM  ·  _SPLIT_  ·  Low
`wasmintegration.cpp:71`
- **opus:** ⚠️ PARTIAL (45) — invokeMethod return unchecked (wasmintegration.cpp:71)
- **gpt:** ⚠️ PARTIAL (58) — observed QMetaObject::invokeMethod return value unchecked - silent failure on WASM (src/wasmintegration.cpp:71)
- **deepseek:** ✅ LEGIT (95) — wasmintegration.cpp:71: QMetaObject::invokeMethod returns bool — discarded; if QML function renamed/removed background image upload silently breaks on WASM

### [META-N14] ModernToolkit removed from AppStream spec — validation error  ·  _SPLIT_  ·  Medium
`appdata.xml:66`
- **opus:** ❔ UNSURE (45) — ModernToolkit removed from AppStream spec; needs validator (appdata.xml:66)
- **gpt:** ⚠️ PARTIAL (58) — observed ModernToolkit removed from AppStream spec - validation error (com.cuperino.qprompt.appdata.xml:66)
- **deepseek:** ✅ LEGIT (80) — appdata.xml:66 uses ModernToolkit kudo; ModernToolkit removed from AppStream spec checklist in recent versions; validator may reject

### [META-N15] No StartupWMClass in desktop file — duplicate dock entries, missing icon  ·  _SPLIT_  ·  Medium
`com.cuperino.qprompt.desktop`
- **opus:** ⚠️ PARTIAL (45) — no StartupWMClass in desktop file
- **gpt:** ⚠️ PARTIAL (58) — observed No StartupWMClass in desktop file - duplicate dock entries, missing icon (com.cuperino.qprompt.desktop:1)
- **deepseek:** ✅ LEGIT (90) — com.cuperino.qprompt.desktop (both copies): no StartupWMClass entry; causes duplicate dock entries and missing icon on Linux

### [META-N16] README badges and links reference wrong repo Cuperino/QPrompt (should be QPrompt-Teleprompter)  ·  _SPLIT_  ·  Low
`README.md`
- **opus:** ❔ UNSURE (45) — README repo URL Cuperino/QPrompt; needs repo check
- **gpt:** ❔ UNSURE (39) — repo rename claim needs external project history, not code (README.md:1)
- **deepseek:** ✅ LEGIT (90) — README.md:1-6: badges reference Cuperino/QPrompt not QPrompt-Teleprompter; line 18 BUILD.md link points to Cuperino/QPrompt

### [META-N17] README links to non-existent BUILD.md  ·  _SPLIT_  ·  Medium
`README.md:18`
- **opus:** ❔ UNSURE (45) — README links to BUILD.md; needs file check
- **gpt:** ❔ UNSURE (39) — README link target needs packaging/release context (README.md:18)
- **deepseek:** ✅ LEGIT (85) — README.md:18 links to BUILD.md at Cuperino/QPrompt/blob/main/BUILD.md; file likely nonexistent after repo rename

### [MIME-N01] Temporary QMimeDatabase — QMimeType dangling on Qt 5 (undefined behavior)  ·  _SPLIT_  ·  High
`documenthandler.cpp:945`
- **opus:** ⚠️ PARTIAL (45) — temp QMimeDatabase; QMimeType-dangling is Qt5-only, target is Qt6 (documenthandler.cpp:945)
- **gpt:** ⚠️ PARTIAL (58) — observed Temporary QMimeDatabase - QMimeType dangling on Qt 5 (undefined behavior) (src/documenthandler.cpp:945)
- **deepseek:** ❌ FALSE (95) — QT_MIN_VERSION=6.8.2 per CMakeLists.txt:57; Qt 5 not supported. QMimeType independent of QMimeDatabase in Qt 6

### [MIX-01] spellchecker.cpp:98 size_t→int narrowing in languages() reserve  ·  _SPLIT_  ·  Low
`spellchecker.cpp:98`
- **opus:** ⚠️ PARTIAL (40) — size_t->int narrowing in languages() reserve (spellchecker.cpp:98)
- **gpt:** ✅ LEGIT (78) — spellchecker.cpp:98 size_t->int narrowing in languages() reserve (src/spellchecker.cpp:98)
- **deepseek:** ✅ LEGIT (90) — static_cast<int>(m_dicts.size()) at spellchecker.cpp:98 — size_t to int narrowing

### [MOB-02] No +ios/ QML selector — iOS inherits base main.qml with desktop-only components  ·  _SPLIT_  ·  Medium
`Missing +ios/main.qml`
- **opus:** ⚠️ PARTIAL (50) — no +ios selector; iOS inherits base with desktop-only bits (main.qml)
- **gpt:** ✅ LEGIT (78) — No +ios/ QML selector - iOS inherits base main.qml with desktop-only components (src/kirigami_ui/main.qml:1)
- **deepseek:** ✅ LEGIT (95) — No +ios/main.qml exists; iOS inherits base main.qml with ProjectionsManager (QWindow) onFrameSwapped grabToImage and desktop-only components

### [MOB-03] iOS: IosSaveDialog silently hangs QML caller when temp dir invalid  ·  _SPLIT_  ·  Medium
`iossavedialog.mm:79-81`
- **opus:** ⚠️ PARTIAL (50) — iOS save hangs QML caller when temp dir invalid (iossavedialog.mm:79)
- **gpt:** ✅ LEGIT (92) — iOS: IosSaveDialog silently hangs QML caller when temp dir invalid (src/iossavedialog.mm:79)
- **deepseek:** ✅ LEGIT (95) — iossavedialog.mm:79-81: early return on !m_tempDir.isValid() without emitting rejected() or accepted(); QML caller hangs waiting for signal

### [MODEL-N02] SessionModel::clearDataPoints lacks empty-model guard before beginRemoveRows  ·  _SPLIT_  ·  Low
`promptsession.cpp:79-84`
- **opus:** ✅ LEGIT (55) — clearDataPoints no empty guard before beginRemoveRows; dead code (promptsession.cpp:79)
- **gpt:** ⚠️ PARTIAL (58) — observed SessionModel::clearDataPoints lacks empty-model guard before beginRemoveRows (src/promptsession.cpp:79)
- **deepseek:** ✅ LEGIT (85) — promptsession.cpp:79-84: clearDataPoints calls beginRemoveRows(0 rowCount()) without empty-model guard; signals removal from empty model

### [NET-N06] loadFromNetwork() validates original URL, not constructed resultingUrl  ·  _SPLIT_  ·  Low
`documenthandler.cpp:881`
- **opus:** ✅ LEGIT (65) — if(url.isValid()) validates original url not resultingUrl (documenthandler.cpp:881)
- **gpt:** ⚠️ PARTIAL (58) — observed loadFromNetwork() validates original URL, not constructed resultingUrl (src/documenthandler.cpp:881)
- **deepseek:** ✅ LEGIT (85) — url.isValid() at documenthandler.cpp:881 checks input URL not constructed resultingUrl — masked construction errors

### [NOTIFY-02] availableDictionariesChanged NOTIFY signal never emitted  ·  _SPLIT_  ·  Low
`documenthandler.h:137,318`
- **opus:** ✅ LEGIT (55) — availableDictionariesChanged NOTIFY never emitted (documenthandler.h:137)
- **gpt:** ✅ LEGIT (78) — availableDictionariesChanged NOTIFY signal never emitted (src/documenthandler.h:137)
- **deepseek:** ⚠️ PARTIAL (85) — availableDictionariesChanged at documenthandler.h:137 never emitted; but method is static disk-scan can't change

### [OOB-N01] MarkersModel::data() — m_data.at() without row < rowCount() guard  ·  _SPLIT_  ·  Medium
`markersmodel.cpp:40-43`
- **opus:** ⚠️ PARTIAL (50) — data() m_data.at() relies on isValid() not rowCount bound (markersmodel.cpp:40)
- **gpt:** ✅ LEGIT (78) — MarkersModel::data() - mdata.at() without row rowCount() guard (src/markersmodel.cpp:40)
- **deepseek:** ✅ LEGIT (90) — m_data.at(row) at markersmodel.cpp:43 — isValid() doesn't enforce row<rowCount()

### [OOB-N02] SessionModel::data() — same missing row bounds guard  ·  _SPLIT_  ·  Medium
`promptsession.cpp:40-43`
- **opus:** ⚠️ PARTIAL (45) — SessionModel::data missing bounds guard; dead code (promptsession.cpp:40)
- **gpt:** ✅ LEGIT (78) — SessionModel::data() - same missing row bounds guard (src/promptsession.cpp:40)
- **deepseek:** ✅ LEGIT (90) — m_data.at(row) at promptsession.cpp:43 — same missing rowCount guard as OOB-N01

### [OOB-N03] alignment() fetches textCursor() twice — stale cursor race  ·  _SPLIT_  ·  Low
`documenthandler.cpp:547-550`
- **opus:** ⚠️ PARTIAL (50) — alignment() double textCursor() fetch; harmless (LOG-07 family) (documenthandler.cpp:547)
- **gpt:** ✅ LEGIT (78) — alignment() fetches textCursor() twice - stale cursor race (src/documenthandler.cpp:547)
- **deepseek:** ✅ LEGIT (85) — textCursor() called twice at documenthandler.cpp:547+550 — second fetch may return different cursor

### [OPC-01] Right-click toggle desynchronizes velocityIndicator visible/opacity  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:906,979-980`
- **opus:** ⚠️ PARTIAL (50) — right-click toggle desyncs indicator visible/opacity (PrompterPage.qml:906)
- **gpt:** ✅ LEGIT (78) — Right-click toggle desynchronizes velocityIndicator visible/opacity (src/kirigami_ui/PrompterPage.qml:906)
- **deepseek:** ✅ LEGIT (90) — Only opacity toggled at PrompterPage.qml:906; visible stays true — breaks middle-click reactivation

### [ORIENT-N01] TimerClock binary width>height orientation creates sharp 2x font jump at 1:1  ·  _SPLIT_  ·  Low
`TimerClock.qml:127`
- **opus:** ⚠️ PARTIAL (45) — binary width>height -> 2x font jump at 1:1 (TimerClock.qml:127)
- **gpt:** ⚠️ PARTIAL (58) — observed TimerClock binary widthheight orientation creates sharp 2x font jump at 1:1 (src/prompter/TimerClock.qml:127)
- **deepseek:** ✅ LEGIT (60) — binary width>height check creates 2x font size jump at exact square 1:1 aspect (TimerClock.qml:127)

### [PARSE-N01] insertImageAt() stores image resource with file:// key but looks up via plain path  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1766-1769`
- **opus:** ⚠️ PARTIAL (50) — image resource keyed by QUrl but format name=path string; possible mismatch (documenthandler.cpp:1766)
- **gpt:** ✅ LEGIT (78) — insertImageAt() stores image resource with file:// key but looks up via plain path (src/documenthandler.cpp:1766)
- **deepseek:** ✅ LEGIT (85) — addResource with file:// QUrl at documenthandler.cpp:1766 but imageFormat.setName uses plain path at 1769

### [PATH-N01] save() fragile percent-encoding round-trip — broken for UNC paths  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1183`
- **opus:** ⚠️ PARTIAL (50) — save() percent-encoding round-trip fragile for UNC (documenthandler.cpp:1183)
- **gpt:** ✅ LEGIT (78) — save() fragile percent-encoding round-trip - broken for UNC paths (src/documenthandler.cpp:1183)
- **deepseek:** ✅ LEGIT (85) — documenthandler.cpp:1183: toPercentEncoding->toStdString->fromStdString->setUrl() round-trip fragile; UNC paths (//server/share) mangled because setUrl interprets leading // as authority

### [PATH-N03] Wrong ../fonts/ depth in +android and +windows FontLoader paths  ·  _SPLIT_  ·  High
`+android/main.qml:465, +windows/main.qml:531`
- **opus:** ❔ UNSURE (45) — FontLoader ../fonts depth in +android/+windows; needs path trace (main.qml:465)
- **gpt:** ✅ LEGIT (84) — Wrong ../fonts/ depth in +android and +windows FontLoader paths (src/kirigami_ui/+android/main.qml:465)
- **deepseek:** ✅ LEGIT (90) — +android/main.qml:465 / +windows/main.qml:531: FontLoader source '../fonts/...' one level too shallow; files in qrc at different depth than base main.qml — font fails to load

### [PC-01] countdown.state not set in Prompting state — countdown visible during teleprompting  ·  _SPLIT_  ·  Medium
`Prompter.qml:3027-3086`
- **opus:** ❔ UNSURE (45) — countdown.state not set in Prompting; visibility claim; domain (Prompter.qml:3027)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Prompter.qml:3027)
- **deepseek:** ✅ LEGIT (70) — Prompting state (Prompter.qml:3027) has no countdown.state PropertyChanges — countdown may stay visible

### [PERF-N01] onFrameSwapped calls markerCompare() unconditionally — wasted JS call every frame  ·  _SPLIT_  ·  Medium
`main.qml:1038`
- **opus:** ⚠️ PARTIAL (50) — markerCompare() every onFrameSwapped; by-design per comment (main.qml:1038)
- **gpt:** ⚠️ PARTIAL (58) — observed onFrameSwapped calls markerCompare() unconditionally - wasted JS call every frame (src/kirigami_ui/main.qml:1038)
- **deepseek:** ✅ LEGIT (90) — main.qml:1038: markerCompare() called every display frame (60-144Hz) even when not prompting; internal guard returns immediately but JS call overhead wasted — should hoist state check

### [PERF-N02] RecentDocuments._load() blocks startup with N synchronous createObject() calls  ·  _SPLIT_  ·  Medium
`RecentDocuments.qml:221,82-107`
- **opus:** ⚠️ PARTIAL (50) — _load blocks startup with N sync createObject (RecentDocuments.qml:221)
- **gpt:** ⚠️ PARTIAL (58) — observed RecentDocuments.load() blocks startup with N synchronous createObject() calls (src/kirigami_ui/RecentDocuments.qml:221)
- **deepseek:** ✅ LEGIT (90) — RecentDocuments.qml:221/82-107: _load() triggers _rebuildChildren() on Component.onCompleted; creates up to 30 Kirigami.Action synchronously on main thread — startup delay

### [PERF-N03] velocityDragOverlay hot-loop calls velocity functions without throttling  ·  _SPLIT_  ·  Low
`PrompterPage.qml:939-976`
- **opus:** ⚠️ PARTIAL (50) — velocityDragOverlay calls velocity fns without throttle (PrompterPage.qml:939)
- **gpt:** ⚠️ PARTIAL (58) — observed velocityDragOverlay hot-loop calls velocity functions without throttling (src/kirigami_ui/PrompterPage.qml:939)
- **deepseek:** ✅ LEGIT (85) — PrompterPage.qml:939-976: onPositionChanged for-loop calls increaseVelocity/decreaseVelocity N=floor(deltaY/20) times per mouse event; dozens of full binding cascade+navigation per event

### [PLAT-01] KF6Crash_FOUND never defined as C preprocessor macro — KCrash support dead code  ·  _SPLIT_  ·  High
`src/main.cpp:50, CMakeLists.txt:316`
- **opus:** ✅ LEGIT (90) — KF6Crash_FOUND never -D; KF6::Crash never linked (main.cpp:50)
- **gpt:** ⚠️ PARTIAL (58) — observed KF6Crash_FOUND never defined as C preprocessor macro - KCrash support dead code (src/main.cpp:50)
- **deepseek:** ✅ LEGIT (90) — KF6Crash_FOUND at main.cpp:50 checked via #if defined but CMake never adds compile definition; KCrash code dead; confirmed at CMakeLists.txt:316 — find_package sets CMake var not C++ macro

### [PLAT-03] Wrong target name and wrong include path for KDMacTouchBar  ·  _SPLIT_  ·  High
`src/CMakeLists.txt:491,492`
- **opus:** ✅ LEGIT (85) — mactouchbar wrong target; 493 uses KDMacTouchBar (src/CMakeLists.txt:491)
- **gpt:** ✅ LEGIT (84) — Wrong target name and wrong include path for KDMacTouchBar (src/CMakeLists.txt:491)
- **deepseek:** ❔ UNSURE (50) — KDMacTouchBar target name wrong at src/CMakeLists.txt:491-492; need to verify actual target name from 3rdparty/KDMacTouchBar/CMakeLists.txt

### [PLAT-04] DS_Store.scpt referenced but file does not exist  ·  _SPLIT_  ·  Medium
`CMakeLists.txt:485`
- **opus:** ❌ FALSE (95) — dist/macOS/DS_Store.scpt exists (7260 bytes)
- **gpt:** ❌ FALSE (90) — the referenced DS_Store.scpt file exists in dist/macOS (CMakeLists.txt:485)
- **deepseek:** ❔ UNSURE (40) — DS_Store.scpt referenced at CMakeLists.txt:485; cannot verify file existence from source code analysis alone

### [PLAT-07] Incorrect macro syntax: `#define Use_GlobalAccel = 1`  ·  _SPLIT_  ·  Low
`src/globalhotkeys.cpp:29`
- **opus:** ✅ LEGIT (95) — #define Use_GlobalAccel = 1 malformed (dup TYP-06) (globalhotkeys.cpp:29)
- **gpt:** ⚠️ PARTIAL (58) — bad macro expansion is latent; existing preprocessor tests are presence-only (src/globalhotkeys.cpp:29)
- **deepseek:** ✅ LEGIT (85) — Same as TYP-06; #define Use_GlobalAccel = 1 at globalhotkeys.cpp:29 defines to = 1 not 1; latent compile error if #if value-check used

### [PLAT-08] QNX platform guard inconsistency: main.cpp vs documenthandler.h  ·  _SPLIT_  ·  Medium
`src/main.cpp:23, src/documenthandler.h:82`
- **opus:** ⚠️ PARTIAL (50) — documenthandler.h:82 guard omits QNX vs main.cpp:23; exotic target (main.cpp:23)
- **gpt:** ⚠️ PARTIAL (58) — observed QNX platform guard inconsistency: main.cpp vs documenthandler.h (src/main.cpp:23)
- **deepseek:** ✅ LEGIT (85) — documenthandler.h:82 omits Q_OS_QNX from guard but main.cpp:23 and doc.cpp:85 include it; QNX build would fail on missing QDialog symbols

### [PLAT-N03] Zero Q_OS_TVOS preprocessor guards in C++ despite 19 QML references — build failure  ·  _SPLIT_  ·  High
`All .cpp/.h/.mm (zero Q_OS_TVOS); 19 QML references to "tvos"`
- **opus:** ❔ UNSURE (45) — Q_OS_TVOS C++ guard gap vs QML refs; tvOS not a shipping target (multi-file)
- **gpt:** ❔ UNSURE (39) — tvOS support is unclear; QML strings alone do not prove C++ build failure (src/kirigami_ui/main.qml:45)
- **deepseek:** ❌ FALSE (80) — tvOS is not a shipping target in CMake; no C++ guards needed for unsupported platform

### [PLAT-N05] Base main.qml fullScreenPlatform missing "wasm" (inconsistent with +windows)  ·  _SPLIT_  ·  Low
`main.qml:45`
- **opus:** ⚠️ PARTIAL (45) — fullScreenPlatform missing 'wasm' vs +windows (main.qml:45)
- **gpt:** ⚠️ PARTIAL (58) — observed Base main.qml fullScreenPlatform missing "wasm" (inconsistent with +windows) (src/kirigami_ui/main.qml:45)
- **deepseek:** ✅ LEGIT (85) — 'main.qml:45 fullScreenPlatform array lacks "wasm"; +windows variant includes it; wasm shows own fullscreen button alongside browser''s'

### [POP-N01] ESC cascade missing dictionariesSheet — undismissable by keyboard  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:1512, all 3 main.qml ESC handlers`
- **opus:** ⚠️ PARTIAL (50) — ESC cascade omits dictionariesSheet (PrompterPage.qml:1512)
- **gpt:** ⚠️ PARTIAL (58) — observed ESC cascade missing dictionariesSheet - undismissable by keyboard (src/kirigami_ui/PrompterPage.qml:1512)
- **deepseek:** ✅ LEGIT (90) — ESC handler at main.qml:476-518 checks 9 sheets but omits dictionariesSheet (PrompterPage.qml:1512); no alias no ESC chain entry

### [POP-N02] ESC cascade missing customWordsSheet — undismissable by keyboard  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:1589, all 3 main.qml ESC handlers`
- **opus:** ⚠️ PARTIAL (50) — ESC cascade omits customWordsSheet (PrompterPage.qml:1589)
- **gpt:** ⚠️ PARTIAL (58) — observed ESC cascade missing customWordsSheet - undismissable by keyboard (src/kirigami_ui/PrompterPage.qml:1589)
- **deepseek:** ✅ LEGIT (90) — ESC handler at main.qml:476-518 omits customWordsSheet (PrompterPage.qml:1589); identical to POP-N01

### [POP-N03] ESC cascade missing obsConfiguration — undismissable by keyboard despite alias  ·  _SPLIT_  ·  Medium
`All 3 main.qml ESC handlers`
- **opus:** ⚠️ PARTIAL (50) — ESC cascade omits obsConfiguration sheet (main.qml)
- **gpt:** ⚠️ PARTIAL (58) — observed ESC cascade missing obsConfiguration - undismissable by keyboard despite alias (src/kirigami_ui/main.qml:481)
- **deepseek:** ✅ LEGIT (85) — obsConfiguration IS aliased at PrompterPage.qml:53 but ESC handler main.qml:489-504 never checks obsConfiguration.opened

### [POP-N04] CountdownConfiguration SpinBoxes use focus: true (JS label) instead of focus = true  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:1092,1114`
- **opus:** ✅ LEGIT (65) — CountdownConfiguration SpinBox focus: true is a JS label not assignment (PrompterPage.qml:1092)
- **gpt:** ⚠️ PARTIAL (58) — observed CountdownConfiguration SpinBoxes use focus: true (JS label) instead of focus = true (src/kirigami_ui/PrompterPage.qml:1092)
- **deepseek:** ✅ LEGIT (95) — PrompterPage.qml:1092 1114: 'focus: true' inside onValueModified is a JS label not assignment; correct would be 'focus = true'

### [PP-N01] Q_OS_APPLE is not a Qt macro — KGlobalAccel block compiles on all Unix including macOS  ·  _SPLIT_  ·  Medium
`globalhotkeys.cpp:26`
- **opus:** ✅ LEGIT (55) — Q_OS_APPLE not a Qt macro; should be Q_OS_DARWIN/defined check (globalhotkeys.cpp:26)
- **gpt:** ⚠️ PARTIAL (58) — observed Q_OS_APPLE is not a Qt macro - KGlobalAccel block compiles on all Unix including macOS (src/globalhotkeys.cpp:26)
- **deepseek:** ✅ LEGIT (95) — globalhotkeys.cpp:26: Q_OS_APPLE not defined by Qt (correct macro: Q_OS_DARWIN); !defined always true; KGlobalAccel compiles on all Unix

### [PROP-N02] setCursorPosition → reset() — 12-signal storm, no debounce  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:455-463,1187-1201`
- **opus:** ⚠️ PARTIAL (55) — setCursorPosition->reset() emits ~12 signals per move; by-design, no debounce (documenthandler.cpp:461)
- **gpt:** ⚠️ PARTIAL (58) — observed setCursorPosition -> reset() - 12-signal storm, no debounce (src/documenthandler.cpp:455)
- **deepseek:** ✅ LEGIT (85) — setCursorPosition->reset() at documenthandler.cpp:461 emits 12 signals no debounce — 720 emissions/sec on scroll

### [PROP-N03] setMarker/setKeyMarker/setMarkerHref silently trigger full document reparse  ·  _SPLIT_  ·  Low
`documenthandler.cpp:720,775,804`
- **opus:** ⚠️ PARTIAL (45) — marker setters dirty the list -> reparse on next nav; by-design (documenthandler.cpp:720)
- **gpt:** ⚠️ PARTIAL (58) — observed setMarker/setKeyMarker/setMarkerHref silently trigger full document reparse (src/documenthandler.cpp:720)
- **deepseek:** ✅ LEGIT (85) — setMarker/setKeyMarker/setMarkerHref at documenthandler.cpp:720 775 804 all trigger full parse() via setMarkersListDirty

### [QF-N02] QDir::entryList missing QDir::Readable in availableDictionaries()  ·  _SPLIT_  ·  Low
`spellchecker.cpp:254`
- **opus:** ⚠️ PARTIAL (45) — entryList missing QDir::Readable filter (spellchecker.cpp:254)
- **gpt:** ⚠️ PARTIAL (58) — observed QDir::entryList missing QDir::Readable in availableDictionaries() (src/spellchecker.cpp:254)
- **deepseek:** ✅ LEGIT (85) — spellchecker.cpp:254: QDir::entryList uses QDir::Files without QDir::Readable; unreadable .dic files pollute available list causing Hunspell open failure with only qWarning

### [QF-N03] TOCTOU: QFile::exists() → QFile::copy() in resource cache extraction  ·  _SPLIT_  ·  Low
`spellchecker.cpp:198-199`
- **opus:** ⚠️ PARTIAL (50) — TOCTOU exists()->copy() in cache extraction (spellchecker.cpp:198)
- **gpt:** ⚠️ PARTIAL (58) — observed TOCTOU: QFile::exists() -> QFile::copy() in resource cache extraction (src/spellchecker.cpp:198)
- **deepseek:** ✅ LEGIT (90) — spellchecker.cpp:198-199: QFile::exists() then QFile::copy() — TOCTOU race; another process creating outPath between check and copy silently corrupts dictionary cache

### [QLOAD-N01] InputsOverlay toggleButtonsOff() null-check bypass — crash on slow async Loaders  ·  _SPLIT_  ·  Medium
`InputsOverlay.qml:107,564`
- **opus:** ⚠️ PARTIAL (50) — toggleButtonsOff null-check bypass on slow async Loader (InputsOverlay.qml:107)
- **gpt:** ✅ LEGIT (78) — InputsOverlay toggleButtonsOff() null-check bypass - crash on slow async Loaders (src/kirigami_ui/InputsOverlay.qml:107)
- **deepseek:** ✅ LEGIT (95) — InputsOverlay.qml:107 564: typeof null==='object' bypasses guard; null.checked=false throws TypeError on slow async Loader completion

### [QML-01] 26 references to undefined `pointerSettings` ID in ReadRegionOverlay  ·  _SPLIT_  ·  Critical
`src/prompter/ReadRegionOverlay.qml:239,246,261,268,293-395`
- **opus:** ❌ FALSE (90) — pointerSettings resolves via context hierarchy (PrompterPage.qml:1442)
- **gpt:** ❌ FALSE (90) — id exists in PrompterPage; overlay uses same parent context (src/prompter/ReadRegionOverlay.qml:239)
- **deepseek:** ❔ UNSURE (30) — pointerSettings id in ReadRegionOverlay.qml may be resolved via C++ context property or parent hierarchy; cannot verify cross-file QML id scope without full component tree

### [QML-02] Undefined `pointerConfiguration` ID reference in ReadRegionOverlay  ·  _SPLIT_  ·  Critical
`src/prompter/ReadRegionOverlay.qml:283,288`
- **opus:** ❌ FALSE (90) — pointerConfiguration resolves via context (PrompterPage.qml:1427)
- **gpt:** ❌ FALSE (90) — pointerConfiguration is declared beside the overlay owner (src/prompter/ReadRegionOverlay.qml:283)
- **deepseek:** ❔ UNSURE (30) — pointerConfiguration id likewise depends on instantiation context; ReadRegionOverlay may be instantiated inside PrompterPage scope making id visible

### [QML-08] Invalid anchor target `undefined`  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/PrompterPage.qml:807`
- **opus:** ❌ FALSE (80) — anchors.centerIn: undefined is a valid clear-anchor idiom (PrompterPage.qml:807)
- **gpt:** ❌ FALSE (76) — undefined is used here to clear centerIn, not as a target (src/kirigami_ui/PrompterPage.qml:807)
- **deepseek:** ❔ UNSURE (40) — anchors.centerIn:undefined at PrompterPage.qml:807 may be placeholder/default; need full QML context to assess if this line actually executes or is dead

### [QML-10] `+android/main.qml` missing `QmlUtil` for RecentDocuments  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/+android/main.qml:757-762`
- **opus:** ❌ FALSE (85) — existence check null-guarded root.util ? : true (RecentDocuments.qml:164)
- **gpt:** ❌ FALSE (76) — RecentDocuments checks util before fileExists; this part is guarded (src/kirigami_ui/+android/main.qml:757)
- **deepseek:** ❔ UNSURE (45) — +android/main.qml missing QmlUtil for RecentDocuments — depends on whether Android platform variant defines qmlutil elsewhere or inherits from base

### [QML-11] Dead code: `window` property declared but never used in WindowDragger  ·  _SPLIT_  ·  Medium
`src/qt/WindowDragger.qml:28`
- **opus:** ✅ LEGIT (90) — window property dead; impl uses root (WindowDragger.qml:27)
- **gpt:** ⚠️ PARTIAL (58) — observed Dead code: window property declared but never used in WindowDragger (src/qt/WindowDragger.qml:28)
- **deepseek:** ✅ LEGIT (85) — WindowDragger.qml:28 declares window:parent property but implementation uses undefined root instead at lines 41,45 — window is dead code

### [QML-BND-03] ReadRegionOverlay onDestruction — harmless dead code  ·  _SPLIT_  ·  None (info)
`ReadRegionOverlay.qml:86-89`
- **opus:** ⚠️ PARTIAL (40) — onDestruction harmless dead code; report admits (ReadRegionOverlay.qml:86)
- **gpt:** ⚠️ PARTIAL (58) — observed ReadRegionOverlay onDestruction - harmless dead code (src/prompter/ReadRegionOverlay.qml:86)
- **deepseek:** ✅ LEGIT (95) — Component.onDestruction at ReadRegionOverlay.qml:86 sets state during teardown — harmless dead code

### [QOBJ-N01] QmlUtil missing constructor with parent parameter  ·  _SPLIT_  ·  Low
`qmlutil.hpp:47`
- **opus:** ⚠️ PARTIAL (40) — QmlUtil missing parent-arg constructor (qmlutil.hpp:47)
- **gpt:** ✅ LEGIT (78) — QmlUtil missing constructor with parent parameter (src/qmlutil.hpp:47)
- **deepseek:** ✅ LEGIT (85) — qmlutil.hpp:47: QML_ELEMENT class with all methods inline; no explicit parent-taking constructor; new QmlUtil from C++ would leak (currently only QML singleton instantiated)

### [QP-N01] restartApplication() quits even when startDetached fails — app dies with no replacement  ·  _SPLIT_  ·  High
`qmlutil.hpp:97-102`
- **opus:** ✅ LEGIT (65) — restartApplication quits even if startDetached fails (return ignored) (qmlutil.hpp:97)
- **gpt:** ⚠️ PARTIAL (58) — observed restartApplication() quits even when startDetached fails - app dies with no replacement (src/qmlutil.hpp:97)
- **deepseek:** ✅ LEGIT (95) — qmlutil.hpp:97-102: QProcess::startDetached return bool discarded; quit() fires unconditionally; app dies if restart fails

### [QRC-N01] icons.qrc contains duplicate \<file\> entry  ·  _SPLIT_  ·  Low
`src/icons/icons.qrc:45,47`
- **opus:** ❔ UNSURE (45) — icons.qrc duplicate <file> entry; needs file read
- **gpt:** ✅ LEGIT (92) — icons.qrc contains duplicate \file\ entry (src/icons/icons.qrc:45)
- **deepseek:** ✅ LEGIT (95) — Identical <file> entry at icons.qrc:45 and :47 — same SVG embedded twice

### [QRC-N02] Four .qrc files are dead code — never referenced by CMakeLists.txt  ·  _SPLIT_  ·  Low
`src/icons/icons.qrc, src/fonts/fonts.qrc, src/fonts/chinese.qrc, src/prompter/pointers/pointers.qrc`
- **opus:** ⚠️ PARTIAL (45) — four .qrc files unreferenced by CMake; dead
- **gpt:** ⚠️ PARTIAL (58) — observed Four .qrc files are dead code - never referenced by CMakeLists.txt (src/icons/icons.qrc:1)
- **deepseek:** ✅ LEGIT (90) — .qrc files orphaned — resources compiled via qt_add_qml_module/Resources in src/CMakeLists.txt instead

### [QTD-02] QQuickTextDocument destroyed without destroyed signal connection  ·  _SPLIT_  ·  Low-Medium
`documenthandler.h:334, documenthandler.cpp:175-202`
- **opus:** ❔ UNSURE (40) — QQuickTextDocument destroyed-signal not connected; lifetime QML-managed (documenthandler.cpp:175)
- **gpt:** ✅ LEGIT (78) — QQuickTextDocument destroyed without destroyed signal connection (src/documenthandler.h:334)
- **deepseek:** ✅ LEGIT (85) — Raw QQuickTextDocument* m_document at documenthandler.h:334 — no destroyed signal dangles on QML teardown

### [QW-N01] Projection Window onClosing references cleared model — spurious runtime errors  ·  _SPLIT_  ·  Medium
`ProjectionsManager.qml:130-133,196-201`
- **opus:** ⚠️ PARTIAL (50) — onClosing references cleared model (ProjectionsManager.qml:130)
- **gpt:** ⚠️ PARTIAL (58) — observed Projection Window onClosing references cleared model - spurious runtime errors (src/prompter/ProjectionsManager.qml:130)
- **deepseek:** ✅ LEGIT (90) — ProjectionsManager.qml:130-133: closeAll clears projectionModel; async Instantiator destruction triggers onClosing remove on cleared model

### [QW-N02] Stale QScreen reference in projection model — dangling after monitor hot-unplug  ·  _SPLIT_  ·  Medium
`ProjectionsManager.qml:119,177`
- **opus:** ⚠️ PARTIAL (55) — stores QScreen ref; dangling after hot-unplug (ProjectionsManager.qml:119)
- **gpt:** ⚠️ PARTIAL (58) — observed Stale QScreen reference in projection model - dangling after monitor hot-unplug (src/prompter/ProjectionsManager.qml:119)
- **deepseek:** ✅ LEGIT (85) — ProjectionsManager.qml:119 177: QScreen objects captured into ListModel at project(); monitor unplug -> dangling pointer; wrong coords

### [R2-AND-01] Android missing QmlUtil causes crash on factory reset and RecentDocuments  ·  _SPLIT_  ·  Critical
`src/kirigami_ui/+android/main.qml (absent object), line 684`
- **opus:** ✅ LEGIT (90) — no qmlutil -> factoryReset crash (+android/main.qml:684)
- **gpt:** ⚠️ PARTIAL (58) — factory reset uses missing qmlutil, but RecentDocuments has a null guard (src/kirigami_ui/+android/main.qml:684)
- **deepseek:** ❔ UNSURE (35) — Android QmlUtil absence — depends on whether +android/main.qml inherits from base qml or is standalone; need file analysis

### [R2-AND-02] Android missing restartDialog crashes LanguageSettingsOverlay and LayoutDirectionSettingsOverlay  ·  _SPLIT_  ·  Critical
`src/kirigami_ui/+android/main.qml (absent object)`
- **opus:** ✅ LEGIT (90) — no restartDialog -> overlay crash (+android)
- **gpt:** ✅ LEGIT (84) — Android missing restartDialog crashes LanguageSettingsOverlay and LayoutDirectionSettingsOverlay (src/kirigami_ui/+android/main.qml:1)
- **deepseek:** ❔ UNSURE (35) — Android restartDialog absence — same inheritance question as R2-AND-01

### [R2-AND-03] Android Settings missing fakeFullScreen persistence  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/+android/main.qml:72-77`
- **opus:** ✅ LEGIT (80) — no fakeFullScreen persistence alias (+android)
- **gpt:** ✅ LEGIT (78) — Android Settings missing fakeFullScreen persistence (src/kirigami_ui/+android/main.qml:72)
- **deepseek:** ❔ UNSURE (35) — Android fakeFullScreen persistence — need to verify Settings block structure in +android/main.qml

### [R2-AND-04] Android Settings for "background" missing transparency persistence  ·  _SPLIT_  ·  Low
`src/kirigami_ui/+android/main.qml:96-100`
- **opus:** ⚠️ PARTIAL (45) — +android background Settings missing transparency alias; no current impact (main.qml:96)
- **gpt:** ⚠️ PARTIAL (58) — observed Android Settings for "background" missing transparency persistence (src/kirigami_ui/+android/main.qml:96)
- **deepseek:** ❔ UNSURE (30) — Android transparency persistence — future compat issue minimal current impact

### [R2-AND-05] Android loadTelemetryPage passes no properties object to pageStack push  ·  _SPLIT_  ·  Low
`src/kirigami_ui/+android/main.qml:162`
- **opus:** ⚠️ PARTIAL (45) — +android loadTelemetryPage push no properties obj (main.qml:162)
- **gpt:** ⚠️ PARTIAL (58) — observed Android loadTelemetryPage passes no properties object to pageStack push (src/kirigami_ui/+android/main.qml:162)
- **deepseek:** ❔ UNSURE (25) — Telemetry page push missing props — commented-out component; no current impact

### [R2-EDT-01] Qt.AlignHustify typo — nonexistent enum value  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/EditorToolbar.qml:380`
- **opus:** ✅ LEGIT (90) — Qt.AlignHustify typo -> enabled always true (EditorToolbar.qml:380)
- **gpt:** ✅ LEGIT (92) — Qt.AlignHustify typo - nonexistent enum value (src/kirigami_ui/EditorToolbar.qml:380)
- **deepseek:** ❔ UNSURE (40) — Qt.AlignHustify typo at EditorToolbar.qml:380; need to verify Qt namespace enums; likely genuine typo but requires Qt API confirmation

### [R2-EDT-02] wheelThrottleSettingsButton checked bound to completely unrelated document property  ·  _SPLIT_  ·  High
`src/kirigami_ui/EditorToolbar.qml:790`
- **opus:** ✅ LEGIT (85) — wheel button checked bound to document.namedMarker (EditorToolbar.qml:790)
- **gpt:** ✅ LEGIT (84) — wheelThrottleSettingsButton checked bound to completely unrelated document property (src/kirigami_ui/EditorToolbar.qml:790)
- **deepseek:** ❔ UNSURE (35) — wheelThrottleSettingsButton checked bound to namedMarker at EditorToolbar.qml:790; need full QML to verify if this is intentional or copy-paste

### [R2-EDT-03] Checkable ToolButtons break checked property bindings on first click — systematic  ·  _SPLIT_  ·  High
`src/kirigami_ui/EditorToolbar.qml:223-224,233-236,380-381,392-394,404-406,416-418,429-431,449-452,460-463,471-474,482-485,493-503,513-525,725-727,741-743,751-753,769-772,790-792,836`
- **opus:** ✅ LEGIT (80) — checkable + checked:binding -> click destroys binding (EditorToolbar.qml:223)
- **gpt:** ✅ LEGIT (84) — Checkable ToolButtons break checked property bindings on first click - systematic (src/kirigami_ui/EditorToolbar.qml:223)
- **deepseek:** ⚠️ PARTIAL (55) — Checkable ToolButtons breaking declarative bindings is well-known QtQuick behavior; ~20 buttons affected — binding breakage is real but intentional by Qt design

### [R2-IOS-01] Method swizzling re-entry causes infinite recursion on second invocation  ·  _SPLIT_  ·  High
`src/shakedetector.mm:74-78`
- **opus:** ✅ LEGIT (80) — swizzle re-entry captures self -> recursion (shakedetector.mm:74)
- **gpt:** ✅ LEGIT (84) — Method swizzling re-entry causes infinite recursion on second invocation (src/shakedetector.mm:74)
- **deepseek:** ❔ UNSURE (40) — Method swizzling re-entry at shakedetector.mm:74-78; .mm file not read; plausible iOS ObjC runtime bug but cannot verify without .mm source

### [R2-IOS-02] Delegate block captures raw assign pointer — use-after-free risk  ·  _SPLIT_  ·  Medium
`src/iossavedialog.mm:42-44,50-52`
- **opus:** ⚠️ PARTIAL (50) — delegate captures assign raw ptr; UAF needs singleton destroyed (iossavedialog.mm:42)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/iossavedialog.mm:42)
- **deepseek:** ❔ UNSURE (40) — Delegate block captures assign pointer at iossavedialog.mm:42-44; .mm file not read; plausible but need ObjC source verification

### [R2-OVL-01] InputsOverlay onOpened calls cursorAutoHide.restart() instead of reset()  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/InputsOverlay.qml:41`
- **opus:** ⚠️ PARTIAL (65) — cursorAutoHide.restart() on open vs reset() elsewhere (InputsOverlay.qml:41)
- **gpt:** ⚠️ PARTIAL (58) — observed InputsOverlay onOpened calls cursorAutoHide.restart() instead of reset() (src/kirigami_ui/InputsOverlay.qml:41)
- **deepseek:** ❔ UNSURE (35) — restart vs reset at InputsOverlay.qml:41 — need to verify Timer API and intended behavior

### [R2-OVL-02] LanguageSettingsOverlay popup ListView currentIndex always resolves to -1  ·  _SPLIT_  ·  Low
`src/kirigami_ui/LanguageSettingsOverlay.qml:73`
- **opus:** ✅ LEGIT (85) — popup currentIndex indexOf(int) over object array -> -1 (LanguageSettingsOverlay.qml:73)
- **gpt:** ✅ LEGIT (78) — LanguageSettingsOverlay popup ListView currentIndex always resolves to -1 (src/kirigami_ui/LanguageSettingsOverlay.qml:73)
- **deepseek:** ❔ UNSURE (35) — ListView currentIndex=-1 at LanguageSettingsOverlay.qml:73 — need to verify model structure and indexOf semantics

### [R2-PRP-01] Qt.LeftToRight used as bare boolean — RTL branch always dead  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/PrompterPage.qml:189,193,659`
- **opus:** ✅ LEGIT (80) — bare Qt.LeftToRight used as condition (PrompterPage.qml:189)
- **gpt:** ✅ LEGIT (78) — Qt.LeftToRight used as bare boolean - RTL branch always dead (src/kirigami_ui/PrompterPage.qml:189)
- **deepseek:** ❔ UNSURE (45) — Qt.LeftToRight used as bare boolean at PrompterPage.qml:189/193/659 — need to verify QML context; Qt.LeftToRight is non-zero enum but usage pattern unclear without full file

### [R2-PRP-02] Kirigami.Units.SmallSpacing — uppercase S yields undefined  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/PrompterPage.qml:1331,1332,1352,1353,1377,1378`
- **opus:** ✅ LEGIT (85) — Units.SmallSpacing should be smallSpacing (PrompterPage.qml:1331)
- **gpt:** ✅ LEGIT (92) — Kirigami.Units.SmallSpacing - uppercase S yields undefined (src/kirigami_ui/PrompterPage.qml:1331)
- **deepseek:** ❔ UNSURE (40) — Kirigami.Units.SmallSpacing uppercase S claimed undefined; depends on Kirigami 2.x API; need to verify actual property name in Kirigami's Units singleton

### [R2-PRP-03] Units.LongDuration / Units.HumanMoment missing Kirigami. prefix  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/PrompterPage.qml:853,860,870,1202`
- **opus:** ❌ FALSE (75) — misdiagnosed; AbstractUnits refs not Kirigami.Units
- **gpt:** ⚠️ PARTIAL (58) — bare Units is broken by AbstractUnits registration, not by Kirigami prefix (src/kirigami_ui/PrompterPage.qml:853)
- **deepseek:** ❔ UNSURE (40) — Units.LongDuration without Kirigami. prefix; depends on import aliasing in PrompterPage.qml; need file's import statements to verify

### [R2-PRP-04] Inconsistent focus restoration in decreaseVelocityButton  ·  _SPLIT_  ·  Low
`src/kirigami_ui/PrompterPage.qml:89`
- **opus:** ⚠️ PARTIAL (50) — decreaseVelocityButton focus assign vs restoreFocus() (PrompterPage.qml:89)
- **gpt:** ⚠️ PARTIAL (58) — observed Inconsistent focus restoration in decreaseVelocityButton (src/kirigami_ui/PrompterPage.qml:89)
- **deepseek:** ❔ UNSURE (35) — Inconsistent focus restoration at PrompterPage.qml:89; need full QML context to verify intent vs bug

### [R2-PRP-05] Potential null-item access on async Loader in namedMarkerConfiguration.onOpened  ·  _SPLIT_  ·  Low
`src/kirigami_ui/PrompterPage.qml:1144,1146`
- **opus:** ⚠️ PARTIAL (45) — async Loader null-item in namedMarkerConfiguration.onOpened (PrompterPage.qml:1144)
- **gpt:** ⚠️ PARTIAL (52) — observed Potential null-item access on async Loader in namedMarkerConfiguration.onOpened (src/kirigami_ui/PrompterPage.qml:1144)
- **deepseek:** ❔ UNSURE (30) — Async Loader null-item access depends on timing and QML engine behavior; cannot verify without runtime test

### [R2-PTR-03] Casing error: Units.longDuration should be Units.LongDuration  ·  _SPLIT_  ·  Medium
`src/prompter/ProjectionsManager.qml:329`
- **opus:** ✅ LEGIT (80) — Units.longDuration casing (ProjectionsManager.qml:329)
- **gpt:** ✅ LEGIT (78) — Casing error: Units.longDuration should be Units.LongDuration (src/prompter/ProjectionsManager.qml:329)
- **deepseek:** ❔ UNSURE (40) — Units.longDuration lowercase vs LongDuration at ProjectionsManager.qml:329; depends on Kirigami Units property case — need API reference

### [R2-PTR-04] Inverted indexOf truthiness in platform check for ColorDialog  ·  _SPLIT_  ·  Medium
`src/prompter/PointerSettings.qml:653`
- **opus:** ✅ LEGIT (85) — indexOf truthiness bug (PointerSettings.qml:653)
- **gpt:** ✅ LEGIT (78) — Inverted indexOf truthiness in platform check for ColorDialog (src/prompter/PointerSettings.qml:653)
- **deepseek:** ❔ UNSURE (35) — indexOf truthiness inversion at PointerSettings.qml:653; JS logic analysis correct on paper but need to verify actual runtime context

### [R2-REC-01] File URI prefix strip off-by-one on Windows  ·  _SPLIT_  ·  Low
`src/kirigami_ui/RecentDocuments.qml:70`
- **opus:** ✅ LEGIT (85) — substring(7) leaves leading / on Windows (RecentDocuments.qml:70)
- **gpt:** ✅ LEGIT (92) — File URI prefix strip off-by-one on Windows (src/kirigami_ui/RecentDocuments.qml:70)
- **deepseek:** ⚠️ PARTIAL (60) — Windows file:// URL has 3 slashes (file:///C:...); substring(7) strips 7 chars leaving /C: — off-by-one for 3-slash URIs confirmed

### [R2-REC-02] refreshExistence skips UI updates when dynamic children out of sync  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/RecentDocuments.qml:171`
- **opus:** ⚠️ PARTIAL (50) — refreshExistence skips when counts diverge (RecentDocuments.qml:171)
- **gpt:** ⚠️ PARTIAL (58) — observed refreshExistence skips UI updates when dynamic children out of sync (src/kirigami_ui/RecentDocuments.qml:171)
- **deepseek:** ❔ UNSURE (30) — refreshExistence count synchronization — race condition plausible but need dynamic analysis

### [R2-TEL-01] Telemetry sub-toggles permanently disconnect from master toggle on click  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/TelemetryPage.qml:80-88,101-110,123-132,149-158`
- **opus:** ✅ LEGIT (80) — telemetry sub-toggles break from master on click (TelemetryPage.qml:80)
- **gpt:** ✅ LEGIT (78) — Telemetry sub-toggles permanently disconnect from master toggle on click (src/kirigami_ui/TelemetryPage.qml:80)
- **deepseek:** ❔ UNSURE (35) — Telemetry sub-toggles disconnect from master — commented-out code; need verification of active code paths

### [R2-WASM-01] File input element never removed from DOM on user cancel  ·  _SPLIT_  ·  Medium
`src/wasmintegration.cpp:148-149`
- **opus:** ✅ LEGIT (85) — input element leaked in DOM on cancel (wasmintegration.cpp:148)
- **gpt:** ✅ LEGIT (78) — File input element never removed from DOM on user cancel (src/wasmintegration.cpp:148)
- **deepseek:** ❔ UNSURE (35) — DOM input element leak at wasmintegration.cpp:148-149; need wasmintegration.cpp source verification

### [R2-WASM-02] Insecure hostname validation via endsWith allows subdomain spoofing  ·  _SPLIT_  ·  Medium
`src/wasmintegration.cpp:192`
- **opus:** ✅ LEGIT (85) — endsWith host spoofing (wasmintegration.cpp:192)
- **gpt:** ✅ LEGIT (78) — Insecure hostname validation via endsWith allows subdomain spoofing (src/wasmintegration.cpp:192)
- **deepseek:** ❔ UNSURE (35) — endsWith hostname validation at wasmintegration.cpp:192; need source verification of officialHost() implementation

### [R3-MAIN-02] Invalid locale string constructed for short language codes  ·  _SPLIT_  ·  High
`src/main.cpp:141-143`
- **opus:** ⚠️ PARTIAL (55) — language+.UTF-8 invalid only for 2-letter codes (main.cpp:141)
- **gpt:** ⚠️ PARTIAL (58) — observed Invalid locale string constructed for short language codes (src/main.cpp:141)
- **deepseek:** ✅ LEGIT (90) — main.cpp:141 language.toUtf8()+'.UTF-8' for short codes like 'es' produces 'es.UTF-8' — not valid POSIX locale; setlocale silently fails

### [R3-MAIN-04] Stack-allocated QTranslator outlives QApplication on shutdown  ·  _SPLIT_  ·  Low
`src/main.cpp:133,107/109,138/149`
- **opus:** ❌ FALSE (85) — translator-after-app is standard Qt idiom
- **gpt:** ❌ FALSE (76) — translator lifetime follows normal stack order after QApplication (src/main.cpp:133)
- **deepseek:** ⚠️ PARTIAL (60) — main.cpp:133 QTranslator declared after app(line 107/109) destroyed before app — violates installTranslator contract but Qt gracefully handles during teardown

### [R3-MAIN-05] Hardcoded Homebrew version-specific Kirigami import path  ·  _SPLIT_  ·  Medium
`src/main.cpp:314`
- **opus:** ✅ LEGIT (80) — hardcoded Homebrew Cellar Kirigami path (main.cpp:314)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/main.cpp:314)
- **deepseek:** ✅ LEGIT (98) — main.cpp:314 hardcoded /opt/homebrew/Cellar/kf5-kirigami2/5.95.0/lib/qt6/qml — every brew upgrade breaks path

### [R3-PMT-01] OBS WebSocket JSON.parse without try/catch — crash on malformed input  ·  _SPLIT_  ·  High
`src/prompter/Prompter.qml:368`
- **opus:** ⚠️ PARTIAL (60) — JSON.parse no try/catch; crash-to-desktop overstated (Prompter.qml:367)
- **gpt:** ⚠️ PARTIAL (58) — observed OBS WebSocket JSON.parse without try/catch - crash on malformed input (src/prompter/Prompter.qml:368)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:368 JSON.parse(m) in onTextMessageReceived has no try/catch — malformed OBS WebSocket JSON causes unhandled exception/crash

### [R3-PMT-03] goToNextMarker fallback desynchronizes cursor from viewport  ·  _SPLIT_  ·  Medium
`src/prompter/Prompter.qml:658-659`
- **opus:** ⚠️ PARTIAL (50) — goToNextMarker fallback desyncs cursor/viewport; domain (Prompter.qml:658)
- **gpt:** ⚠️ PARTIAL (58) — observed goToNextMarker fallback desynchronizes cursor from viewport (src/prompter/Prompter.qml:658)
- **deepseek:** ✅ LEGIT (85) — Prompter.qml:658-659 fallback scrolls viewport to document end but does NOT update editor.cursorPosition — cursor/viewport desynchronized

### [R3-SIG-02] ShakeDetector signals declared but never emitted — dead feature  ·  _SPLIT_  ·  Medium
`src/shakedetector.h:40-42, shakedetector.cpp:45-47`
- **opus:** ❌ FALSE (85) — signals emitted in shakedetector.mm (iOS)
- **gpt:** ❌ FALSE (90) — iOS implementation invokes the shake/undo/redo signals (src/shakedetector.h:40)
- **deepseek:** ⚠️ PARTIAL (85) — shakedetector.cpp:45-47 setupShakeDetection empty on non-iOS but shakedetector.mm:35/96/105 properly emits via QMetaObject::invokeMethod on iOS — broken non-iOS only

### [R3-SPL-05] SpellChecker has zero thread safety — all methods unprotected  ·  _SPLIT_  ·  Medium
`src/spellchecker.h:32-77`
- **opus:** ⚠️ PARTIAL (45) — SpellChecker no mutexes; speculative single-threaded (spellchecker.h:32)
- **gpt:** ⚠️ PARTIAL (58) — observed SpellChecker has zero thread safety - all methods unprotected (src/spellchecker.h:32)
- **deepseek:** ✅ LEGIT (85) — spellchecker.h:32-77 no QMutex/std::mutex anywhere; m_dicts iterated by highlightBlock while mutated by setLanguage/removeCustomWord — iterator invalidation risk

### [R3-TMR-01] TimerClock ETA uses __iDefault instead of actual __i during reverse scroll  ·  _SPLIT_  ·  Medium
`src/prompter/TimerClock.qml:66`
- **opus:** ❔ UNSURE (45) — __iDefault vs __i in ETA fallback; domain call (TimerClock.qml:66)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/TimerClock.qml:66)
- **deepseek:** ✅ LEGIT (80) — TimerClock.qml:66 ETA fallback uses prompter.__iDefault(static default) instead of actual __i — wrong ETA after mid-session velocity change

### [R4-EVT-02] Velocity modifier ComboBox lists 2 options but switch handles 4 — dead code  ·  _SPLIT_  ·  Medium
`src/kirigami_ui/InputsOverlay.qml:425-441`
- **opus:** ✅ LEGIT (90) — ComboBox 2 items, switch 0-3 (InputsOverlay.qml:425)
- **gpt:** ⚠️ PARTIAL (58) — observed Velocity modifier ComboBox lists 2 options but switch handles 4 - dead code (src/kirigami_ui/InputsOverlay.qml:425)
- **deepseek:** ✅ LEGIT (95) — InputsOverlay.qml:425-428 ComboBox model has 2 items(Alt Ctrl) but switch onActivated handles cases 0-3 — Shift/Meta unreachable

### [R4-EVT-03] CursorAutoHide null access on root.pageStack.currentItem during page transitions  ·  _SPLIT_  ·  High
`src/prompter/CursorAutoHide.qml:28,31,43,56`
- **opus:** ⚠️ PARTIAL (60) — pageStack.currentItem null during transitions; plausible (CursorAutoHide.qml:28)
- **gpt:** ✅ LEGIT (84) — CursorAutoHide null access on root.pageStack.currentItem during page transitions (src/prompter/CursorAutoHide.qml:28)
- **deepseek:** ✅ LEGIT (85) — CursorAutoHide.qml:28/31/43/56 dereference root.pageStack.currentItem without null guard — during page transitions currentItem briefly null

### [R4-EXP-01] No XSS sanitization — script tags, event handlers, javascript: URLs unfiltered  ·  _SPLIT_  ·  Critical
`src/documenthandler.cpp:1246-1334`
- **opus:** ⚠️ PARTIAL (55) — filterHtml doesn't strip scripts but Qt richtext runs no JS (documenthandler.cpp:1246)
- **gpt:** ⚠️ PARTIAL (58) — observed No XSS sanitization - script tags, event handlers, javascript: URLs unfiltered (src/documenthandler.cpp:1246)
- **deepseek:** ✅ LEGIT (95) — documenthandler.cpp:1246-1334 filterHtml applies 6 CSS-property regexes only; no removal of script/iframe/object/embed/event-handlers or javascript: URLs

### [R4-EXP-09] LibreOffice import --cat and --convert-to flags are contradictory  ·  _SPLIT_  ·  Low
`src/documenthandler.cpp:1076`
- **opus:** ⚠️ PARTIAL (55) — --cat and --convert-to are contradictory soffice flags (documenthandler.cpp:1076)
- **gpt:** ⚠️ PARTIAL (58) — observed LibreOffice import --cat and --convert-to flags are contradictory (src/documenthandler.cpp:1076)
- **deepseek:** ✅ LEGIT (85) — documenthandler.cpp:1076 --cat(pipe to stdout) and --convert-to(write file) are contradictory flags — LibreOffice may produce empty stdout

### [R4-IOSCPP-01] QTemporaryDir created on all platforms including non-iOS where unused  ·  _SPLIT_  ·  Low
`src/iossavedialog.h:49`
- **opus:** ⚠️ PARTIAL (50) — QTemporaryDir by-value member on all platforms (iossavedialog.h:49)
- **gpt:** ⚠️ PARTIAL (58) — observed QTemporaryDir created on all platforms including non-iOS where unused (src/iossavedialog.h:49)
- **deepseek:** ✅ LEGIT (90) — iossavedialog.h:49 QTemporaryDir m_tempDir by-value member — default constructor creates temp dir on ALL platforms even non-iOS

### [R4-PRJ-02] displayModel.get().flipSetting writes to snapshot copy — never mutates model  ·  _SPLIT_  ·  High
`src/prompter/ProjectionsManager.qml:83,141,150`
- **opus:** ❔ UNSURE (45) — ListModel.get() mutation is version-dependent (ProjectionsManager.qml:83)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/ProjectionsManager.qml:83)
- **deepseek:** ✅ LEGIT (95) — ProjectionsManager.qml:83/141/150 ListModel.get() returns JS snapshot not live ref — flipSetting writes to copy never mutate model

### [R4-QTV-02] QtQuick.Window 2.0 import does not exist in Qt 6.5  ·  _SPLIT_  ·  Critical
`src/prompter/ReadRegionOverlay.qml:25`
- **opus:** ❌ FALSE (90) — QtQuick.Window 2.0 valid on Qt 6.8.2
- **gpt:** ❌ FALSE (76) — QtQuick.Window 2.0 is valid with the 6.8.2 target (src/prompter/ReadRegionOverlay.qml:25)
- **deepseek:** ❔ UNSURE (60) — ReadRegionOverlay.qml:25 imports QtQuick.Window 2.0 — Qt6 may provide version-mapping for 2.x imports but 2.0 predates 2.15 compat; cannot confirm

### [R4-ROOT-05] loadRemoteControlPage/loadTelemetryPage reference undefined component IDs  ·  _SPLIT_  ·  Low
`src/kirigami_ui/main.qml:175-181`
- **opus:** ⚠️ PARTIAL (50) — loadRemoteControl/Telemetry reference commented-out components (main.qml:175)
- **gpt:** ✅ LEGIT (92) — loadRemoteControlPage/loadTelemetryPage reference undefined component IDs (src/kirigami_ui/main.qml:175)
- **deepseek:** ✅ LEGIT (95) — main.qml:175-181 loadRemoteControlPage/loadTelemetryPage reference commented-out components(1072-1079) — ReferenceError if C++ calls these

### [R4-ROV-01] Division by zero in __customPlacement when overlay full  ·  _SPLIT_  ·  High
`src/prompter/ReadRegionOverlay.qml:189`
- **opus:** ⚠️ PARTIAL (60) — div-by-zero only when readRegion fills overlay (ReadRegionOverlay.qml:189)
- **gpt:** ⚠️ PARTIAL (58) — observed Division by zero in __customPlacement when overlay full (src/prompter/ReadRegionOverlay.qml:189)
- **deepseek:** ✅ LEGIT (90) — ReadRegionOverlay.qml:189 readRegion.y/(overlay.height-readRegion.height) — when readRegion fills overlay denominator=0 — Infinity/NaN

### [R4-ROV-02] Drag permanently breaks y property binding on readRegion  ·  _SPLIT_  ·  High
`src/prompter/ReadRegionOverlay.qml:181-182,141`
- **opus:** ⚠️ PARTIAL (65) — drag breaks y binding; impact partial (ReadRegionOverlay.qml:141,181)
- **gpt:** ⚠️ PARTIAL (58) — observed Drag permanently breaks y property binding on readRegion (src/prompter/ReadRegionOverlay.qml:181)
- **deepseek:** ✅ LEGIT (90) — ReadRegionOverlay.qml:181-182 drag.target assigns y directly breaking declarative y binding at line 141; no re-establishment after drag

### [RAII-N01] QDrag object never deleteLater'd after exec() — leaks on rejected drags  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1486-1489`
- **opus:** ⚠️ PARTIAL (50) — QDrag parented to this; accumulates per drag rather than leaks outright (documenthandler.cpp:1486)
- **gpt:** ✅ LEGIT (78) — QDrag object never deleteLater'd after exec() - leaks on rejected drags (src/documenthandler.cpp:1486)
- **deepseek:** ✅ LEGIT (60) — QDrag new'd per drag operation with parent this; accumulates over session (documenthandler.cpp:1486-1489)

### [RAII-N02] IosSaveDialog::m_tempDir created unconditionally on all platforms — wasted I/O  ·  _SPLIT_  ·  Low
`iossavedialog.h:49`
- **opus:** ⚠️ PARTIAL (50) — m_tempDir created unconditionally; wasted I/O (dup R4-IOSCPP-01) (iossavedialog.h:49)
- **gpt:** ⚠️ PARTIAL (58) — observed IosSaveDialog::mtempDir created unconditionally on all platforms - wasted I/O (src/iossavedialog.h:49)
- **deepseek:** ✅ LEGIT (55) — QTemporaryDir m_tempDir constructed unconditionally on all platforms (iossavedialog.h:49)

### [REGEX-CRIT-01] regex_4 destroys <body> tag — removes opening tag instead of color attributes  ·  _SPLIT_  ·  High
`documenthandler.cpp:1287`
- **opus:** ❔ UNSURE (45) — regex_4 may strip <body> opening tag; complex regex, hard to confirm (documenthandler.cpp:1287)
- **gpt:** ❔ UNSURE (39) — the body-tag regex is complex; impact needs sample HTML (src/documenthandler.cpp:1287)
- **deepseek:** ✅ LEGIT (85) — documenthandler.cpp:1287: regex_4 matches <body through last color attribute quote but stops before >; replace removes opening tag leaving orphaned >content</body> — corrupted HTML

### [REGEX-N01] All 13 QRegularExpression objects lack isValid() checks  ·  _SPLIT_  ·  Medium
`documenthandler.cpp, spellhighlighter.cpp (13 regex objects)`
- **opus:** ⚠️ PARTIAL (45) — 13 regexes lack isValid(); all but search are author-literal (always valid)
- **gpt:** ✅ LEGIT (78) — All 13 QRegularExpression objects lack isValid() checks (src/documenthandler.cpp:893)
- **deepseek:** ✅ LEGIT (85) — 13 QRegularExpression objects lack isValid() checks — pattern typo silently matches nothing

### [REGEX-N04] ReDoS — user-supplied regex has no length limit, timeout, or backtracking guard  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1543-1557`
- **opus:** ⚠️ PARTIAL (50) — ReDoS: user regex no length/timeout guard; user's own input (documenthandler.cpp:1543)
- **gpt:** ✅ LEGIT (78) — ReDoS - user-supplied regex has no length limit, timeout, or backtracking guard (src/documenthandler.cpp:1543)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:1543-1557: user-supplied regex has no length limit no MatchTimeout no optimize(); evil regex like (a+)+b causes exponential backtracking — 100% CPU hang

### [RENDER-01] ShaderEffectSource prompterShadowSource runs unconditionally — wastes GPU capture when shadows disabled  ·  _SPLIT_  ·  Medium
`PrompterView.qml:230-233`
- **opus:** ⚠️ PARTIAL (50) — prompterShadowSource runs unconditionally; GPU waste (PrompterView.qml:230)
- **gpt:** ✅ LEGIT (78) — ShaderEffectSource prompterShadowSource runs unconditionally - wastes GPU capture when shadows disabled (src/prompter/PrompterView.qml:230)
- **deepseek:** ✅ LEGIT (70) — ShaderEffectSource unconditionally captures GPU regardless of shadows setting (PrompterView.qml:230-233)

### [RENDER-02] ShaderEffectSource pointerShadowSource runs unconditionally — same pattern  ·  _SPLIT_  ·  Medium
`ReadRegionOverlay.qml:123-126`
- **opus:** ⚠️ PARTIAL (50) — pointerShadowSource runs unconditionally (ReadRegionOverlay.qml:123)
- **gpt:** ✅ LEGIT (78) — ShaderEffectSource pointerShadowSource runs unconditionally - same pattern (src/prompter/ReadRegionOverlay.qml:123)
- **deepseek:** ✅ LEGIT (70) — pointerShadowSource ShaderEffectSource captures unconditionally (ReadRegionOverlay.qml:123-126)

### [RES-03] ShakeDetector::s_instance never set to nullptr on destruction (dangling pointer)  ·  _SPLIT_  ·  Low
`src/shakedetector.cpp:24,29`
- **opus:** ⚠️ PARTIAL (65) — s_instance not reset; singleton lifetime low (shakedetector.cpp:24)
- **gpt:** ⚠️ PARTIAL (58) — observed ShakeDetector::s_instance never set to nullptr on destruction (dangling pointer) (src/shakedetector.cpp:24)
- **deepseek:** ✅ LEGIT (85) — s_instance set in ctor at shakedetector.cpp:29 but never reset to nullptr on destruction; dangling pointer after QML engine recreate

### [RES-04] IosSaveDialog::s_instance same singleton dangling pattern  ·  _SPLIT_  ·  Low
`src/iossavedialog.cpp:24,29`
- **opus:** ⚠️ PARTIAL (65) — same singleton pattern (iossavedialog.cpp:24)
- **gpt:** ⚠️ PARTIAL (58) — observed IosSaveDialog::s_instance same singleton dangling pattern (src/iossavedialog.cpp:24)
- **deepseek:** ✅ LEGIT (85) — Identical s_instance dangling pattern at iossavedialog.cpp:29; never reset to nullptr; use-after-free risk on singleton destruction

### [RESO-N01] Editing font size not viewport-scaled — text nearly unreadable on 4K  ·  _SPLIT_  ·  Medium
`PrompterView.qml:242`
- **opus:** ⚠️ PARTIAL (45) — editing font size not viewport-scaled on 4K (PrompterView.qml:242)
- **gpt:** ⚠️ PARTIAL (48) — visual issue is plausible but depends on theme or device (src/prompter/PrompterView.qml:242)
- **deepseek:** ✅ LEGIT (95) — PrompterView.qml:242: editing branch lacks *prompter.__vw/10 multiplier present in WYSIWYG branch; font disproportionately small on 4K

### [RESO-N02] Scrollbar width 6dp-13dp — below minimum 44dp touch target  ·  _SPLIT_  ·  Low
`ProgressIndicator.qml:39`
- **opus:** ⚠️ PARTIAL (40) — scrollbar 6-13dp below 44dp touch target (ProgressIndicator.qml:39)
- **gpt:** ⚠️ PARTIAL (48) — visual issue is plausible but depends on theme or device (src/prompter/ProgressIndicator.qml:39)
- **deepseek:** ✅ LEGIT (80) — ProgressIndicator.qml:39: implicitWidth 6-13dp; well below minimum 44dp touch target per accessibility guidelines

### [RESO-N03] Control spacing hardcoded 8dp — cramped on large displays  ·  _SPLIT_  ·  Low
`PrompterView.qml:63,64,113, Prompter.qml:1047`
- **opus:** ⚠️ PARTIAL (40) — control spacing hardcoded 8dp (PrompterView.qml:63)
- **gpt:** ⚠️ PARTIAL (48) — visual issue is plausible but depends on theme or device (src/prompter/PrompterView.qml:63)
- **deepseek:** ✅ LEGIT (75) — PrompterView.qml:63 64: spacing/padding hardcoded 8dp; cramped on large displays; minor observation

### [RESO-N04] Projection-window margins fixed 10dp/5dp — near-flush on large screens  ·  _SPLIT_  ·  Low
`ProjectionsManager.qml:324-325`
- **opus:** ⚠️ PARTIAL (40) — projection margins fixed 10/5dp (ProjectionsManager.qml:324)
- **gpt:** ⚠️ PARTIAL (48) — visual issue is plausible but depends on theme or device (src/prompter/ProjectionsManager.qml:324)
- **deepseek:** ✅ LEGIT (75) — ProjectionsManager.qml:324-325: margins fixed 10dp/5dp; near-flush on large projection screens; minor

### [RESO-N05] PointerSettings ListView height hardcoded 180dp — doesn't fill available space  ·  _SPLIT_  ·  Low
`PointerSettings.qml:254`
- **opus:** ⚠️ PARTIAL (40) — ListView height hardcoded 180dp (PointerSettings.qml:254)
- **gpt:** ⚠️ PARTIAL (48) — visual issue is plausible but depends on theme or device (src/prompter/PointerSettings.qml:254)
- **deepseek:** ✅ LEGIT (75) — PointerSettings.qml:254: ListView height hardcoded 180dp; doesn't fill available space

### [RESO-N06] ReadRegionOverlay pointer margin 3dp — overlap with text at large fonts  ·  _SPLIT_  ·  Low
`ReadRegionOverlay.qml:260,267`
- **opus:** ⚠️ PARTIAL (40) — pointer margin 3dp overlap at large fonts (ReadRegionOverlay.qml:260)
- **gpt:** ⚠️ PARTIAL (48) — visual issue is plausible but depends on theme or device (src/prompter/ReadRegionOverlay.qml:260)
- **deepseek:** ✅ LEGIT (80) — ReadRegionOverlay.qml:260 267: pointer margin 3dp; overlaps text at large font sizes

### [RESP-N01] minimumHeight: minimumWidth forces square aspect ratio — prevents landscape-strip windows  ·  _SPLIT_  ·  Low
`main.qml:83, +windows:78`
- **opus:** ⚠️ PARTIAL (50) — minimumHeight: minimumWidth forces square aspect (main.qml:83)
- **gpt:** ⚠️ PARTIAL (58) — observed minimumHeight: minimumWidth forces square aspect ratio - prevents landscape-strip windows (src/kirigami_ui/main.qml:83)
- **deepseek:** ✅ LEGIT (85) — main.qml:83: minimumHeight: minimumWidth forces square minimum; prevents landscape-strip window shapes that layout would handle

### [RESP-N02] mobileOrSmallScreen threshold at 1231px activates on default 1220px launch  ·  _SPLIT_  ·  Medium
`main.qml:54,77`
- **opus:** ❔ UNSURE (45) — mobileOrSmallScreen 1231px vs 1220px launch; heuristic threshold (main.qml:54)
- **gpt:** ⚠️ PARTIAL (58) — observed mobileOrSmallScreen threshold at 1231px activates on default 1220px launch (src/kirigami_ui/main.qml:54)
- **deepseek:** ✅ LEGIT (90) — main.qml:54 77: mobileOrSmallScreen threshold 1231px vs default width 1220px; every fresh launch starts in mobile/compact toolbar mode

### [RESP-N03] +android/main.qml omits all size declarations — transient zero-size layout on startup  ·  _SPLIT_  ·  Low
`+android/main.qml`
- **opus:** ⚠️ PARTIAL (45) — +android omits size declarations; transient zero-size (main.qml)
- **gpt:** ⚠️ PARTIAL (58) — observed +android/main.qml omits all size declarations - transient zero-size layout on startup (src/kirigami_ui/+android/main.qml:1)
- **deepseek:** ❌ FALSE (85) — +android/main.qml is dead code (QML file selectors never instantiated per QT-LC-N01); base main.qml always loads with proper width/height

### [RND-N01] forceQtTextRenderer dead on Apple platforms — unconditionally uses NativeRendering  ·  _SPLIT_  ·  Low
`Prompter.qml:994`
- **opus:** ⚠️ PARTIAL (50) — forceQtTextRenderer dead on Apple (always NativeRendering) (Prompter.qml:994)
- **gpt:** ⚠️ PARTIAL (58) — observed forceQtTextRenderer dead on Apple platforms - unconditionally uses NativeRendering (src/prompter/Prompter.qml:994)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:994: iOS/osx short-circuit to NativeRendering unconditionally before evaluating root.forceQtTextRenderer

### [RND-N02] Missing smooth: true on background Image — aliased upscale  ·  _SPLIT_  ·  Low
`PrompterBackground.qml:79-87`
- **opus:** ⚠️ PARTIAL (45) — missing smooth:true on background Image (PrompterBackground.qml:79)
- **gpt:** ⚠️ PARTIAL (58) — observed Missing smooth: true on background Image - aliased upscale (src/prompter/PrompterBackground.qml:79)
- **deepseek:** ✅ LEGIT (85) — PrompterBackground.qml:79-87: Image with PreserveAspectCrop fillMode lacks smooth:true; nearest-neighbor scaling

### [RND-N03] Missing smooth: true on projection Image — aliased text on external displays  ·  _SPLIT_  ·  Low
`ProjectionsManager.qml:284-304`
- **opus:** ⚠️ PARTIAL (50) — missing smooth:true on projection Image; aliased (ProjectionsManager.qml:284)
- **gpt:** ⚠️ PARTIAL (58) — observed Missing smooth: true on projection Image - aliased text on external displays (src/prompter/ProjectionsManager.qml:284)
- **deepseek:** ✅ LEGIT (85) — ProjectionsManager.qml:284-304: projection Image lacks smooth:true; text aliased on scaled external displays

### [RPM-N01] RPM dependencies entirely commented out — zero automatic dependency resolution  ·  _SPLIT_  ·  Medium
`CMakeLists.txt:450`
- **opus:** ✅ LEGIT (50) — RPM dependencies entirely commented out (CMakeLists.txt:450)
- **gpt:** ⚠️ PARTIAL (58) — observed RPM dependencies entirely commented out - zero automatic dependency resolution (CMakeLists.txt:450)
- **deepseek:** ✅ LEGIT (90) — CMakeLists.txt:450: CPACK_RPM_PACKAGE_REQUIRES entirely commented out; generated RPMs have empty Requires; dnf installs without Qt/KDE

### [SAFE-01] +android/main.qml zero safe area insets  ·  _SPLIT_  ·  Medium
`+android/main.qml`
- **opus:** ⚠️ PARTIAL (45) — +android no safe-area insets; notch handling (main.qml)
- **gpt:** ⚠️ PARTIAL (58) — observed +android/main.qml zero safe area insets (src/kirigami_ui/+android/main.qml:1)
- **deepseek:** ✅ LEGIT (80) — +android/main.qml full-screen — zero safe area margins for notch/gesture pill

### [SAFE-02] ReadRegionOverlay screenMiddle ignores notch/status bar height  ·  _SPLIT_  ·  Medium
`ReadRegionOverlay.qml:132-134`
- **opus:** ⚠️ PARTIAL (45) — screenMiddle ignores notch/status bar (ReadRegionOverlay.qml:132)
- **gpt:** ⚠️ PARTIAL (58) — observed ReadRegionOverlay screenMiddle ignores notch/status bar height (src/prompter/ReadRegionOverlay.qml:132)
- **deepseek:** ✅ LEGIT (80) — screenMiddle at ReadRegionOverlay.qml:132 uses raw screen.height — ignores notch/status bar

### [SAVE-N01] loadFromNetworkFinihed sets m_fileUrl to phantom QTemporaryFile path  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:897,144`
- **opus:** ⚠️ PARTIAL (55) — network doc m_fileUrl set to QTemporaryFile path (documenthandler.cpp:897)
- **gpt:** ✅ LEGIT (78) — loadFromNetworkFinihed sets m_fileUrl to phantom QTemporaryFile path (src/documenthandler.cpp:897)
- **deepseek:** ✅ LEGIT (70) — network docs set m_fileUrl to QTemporaryFile path not source network URL (documenthandler.cpp:897)

### [SAVE-N02] iOS save flow never updates C++ m_fileUrl — file URL perpetually stale  ·  _SPLIT_  ·  High
`Prompter.qml:2493-2506, iossavedialog.mm:36-46`
- **opus:** ⚠️ PARTIAL (50) — iOS onAccepted doesn't refresh C++ m_fileUrl; domain (Prompter.qml:2493)
- **gpt:** ✅ LEGIT (84) — iOS save flow never updates C++ m_fileUrl - file URL perpetually stale (src/prompter/Prompter.qml:2493)
- **deepseek:** ✅ LEGIT (75) — iOS save flow in QML never calls C++ method to update m_fileUrl (Prompter.qml:2493-2506)

### [SAVE-N04] save() unnecessary QString→std::string→QString round-trip through locale encoding  ·  _SPLIT_  ·  Low
`documenthandler.cpp:1183`
- **opus:** ⚠️ PARTIAL (45) — save() needless QString->std::string->QString round-trip (documenthandler.cpp:1183)
- **gpt:** ✅ LEGIT (78) — save() unnecessary QString->std::string->QString round-trip through locale encoding (src/documenthandler.cpp:1183)
- **deepseek:** ✅ LEGIT (65) — unnecessary QString->std::string->QString round-trip via locale encoding (documenthandler.cpp:1183)

### [SCALE-N01] Right pointer xScale: -1 mirrors text pointers — backwards/unreadable text  ·  _SPLIT_  ·  Medium
`ReadRegionOverlay.qml:391-398`
- **opus:** ⚠️ PARTIAL (50) — right pointer xScale:-1 mirrors text; domain (ReadRegionOverlay.qml:391)
- **gpt:** ✅ LEGIT (78) — Right pointer xScale: -1 mirrors text pointers - backwards/unreadable text (src/prompter/ReadRegionOverlay.qml:391)
- **deepseek:** ✅ LEGIT (65) — right pointer xScale:-1 mirrors Arrow/sameAsLeft text making it backwards (ReadRegionOverlay.qml:391-398)

### [SCR-N01] Per-screen projection flip settings lost on restart — never serialized  ·  _SPLIT_  ·  High
`ProjectionsManager.qml:39,168-173`
- **opus:** ❔ UNSURE (45) — per-screen flip persistence; ties to R4-PRJ-02 snapshot issue (ProjectionsManager.qml:39)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/ProjectionsManager.qml:39)
- **deepseek:** ✅ LEGIT (90) — screensStringified Settings alias commented out at ProjectionsManager.qml:172; per-screen flip config never persisted across restart

### [SCR-N03] No runtime screen plug/unplug handling — stale projection windows on disconnected screens  ·  _SPLIT_  ·  Medium
`ProjectionsManager.qml:157-166`
- **opus:** ⚠️ PARTIAL (50) — no runtime screen plug/unplug handling (ProjectionsManager.qml:157)
- **gpt:** ⚠️ PARTIAL (58) — observed No runtime screen plug/unplug handling - stale projection windows on disconnected screens (src/prompter/ProjectionsManager.qml:157)
- **deepseek:** ✅ LEGIT (85) — ProjectionsManager.qml:157-166: no connection to screenAdded/screenRemoved signals; monitor hotplug requires manual toggle to refresh

### [SCRL-N01] __jitterMargin: fractional result from modulus violates 0/1 toggle design  ·  _SPLIT_  ·  Medium
`Prompter.qml:114`
- **opus:** ❔ UNSURE (45) — __jitterMargin fractional from modulus; scroll-toggle design claim (Prompter.qml:114)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Prompter.qml:114)
- **deepseek:** ⚠️ PARTIAL (50) — modulus on mixed int/real types yields fractional; depends on jitter design intent (Prompter.qml:114)

### [SCRL-N02] __destination typed int truncates real-valued position  ·  _SPLIT_  ·  Medium
`Prompter.qml:125`
- **opus:** ⚠️ PARTIAL (50) — __destination int truncates real position; sub-pixel (Prompter.qml:125)
- **gpt:** ⚠️ PARTIAL (58) — observed destination typed int truncates real-valued position (src/prompter/Prompter.qml:125)
- **deepseek:** ✅ LEGIT (65) — real-valued destination assigned to int property truncates sub-pixel position (Prompter.qml:125)

### [SCRL-N03] setVelocity() triggers two conflicting scroll animations with intermediate velocity  ·  _SPLIT_  ·  Medium
`Prompter.qml:605-613`
- **opus:** ❔ UNSURE (45) — setVelocity two conflicting animations; domain (Prompter.qml:605)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Prompter.qml:605)
- **deepseek:** ✅ LEGIT (55) — setVelocity sets position to __destination twice with __i changed between stmts causing two scrolls (Prompter.qml:605-613)

### [SCRL-N05] __speedLimit check is dead logic — always true  ·  _SPLIT_  ·  Low
`Prompter.qml:129,494,510`
- **opus:** ⚠️ PARTIAL (50) — __speedLimit check claimed always-true; needs full expr (Prompter.qml:129)
- **gpt:** ⚠️ PARTIAL (58) — observed speedLimit check is dead logic - always true (src/prompter/Prompter.qml:129)
- **deepseek:** ❌ FALSE (65) — __speedLimit=__vw*100=width pixels; velocity reachable at high __i values (Prompter.qml:129 494 510)

### [SCRL-N06] __timeToEnd uses unexplained 2× factor  ·  _SPLIT_  ·  Low
`Prompter.qml:122, TimerClock.qml:66`
- **opus:** ⚠️ PARTIAL (40) — __timeToEnd 2x factor is documented intent, not a bug (Prompter.qml:122)
- **gpt:** ⚠️ PARTIAL (58) — observed timeToEnd uses unexplained 2× factor (src/prompter/Prompter.qml:122)
- **deepseek:** ❌ FALSE (60) — 2x factor consistent with identical fallback calc at TimerClock.qml:66 (Prompter.qml:122)

### [SEC-04] SSRF / URL Injection — User-Controlled URL Passed to Network Loader  ·  _SPLIT_  ·  High
`src/documenthandler.cpp:867-886, src/kirigami_ui/PrompterPage.qml:1277-1291`
- **opus:** ⚠️ PARTIAL (55) — user-initiated load; SSRF framing weak but host/path bug real (documenthandler.cpp:873)
- **gpt:** ⚠️ PARTIAL (58) — observed SSRF / URL Injection - User-Controlled URL Passed to Network Loader (src/documenthandler.cpp:867)
- **deepseek:** ✅ LEGIT (85) — Relative URL path becomes host at doc.cpp:873; user-supplied URL like 'localhost:4455' -> HTTP GET to internal service — genuine SSRF vector

### [SEC-05] User-Controlled Filename Passed to QProcess (LibreOffice import)  ·  _SPLIT_  ·  Medium
`src/documenthandler.cpp:1076-1077`
- **opus:** ⚠️ PARTIAL (55) — filename to LibreOffice args; flag injection minor (documenthandler.cpp:1076)
- **gpt:** ⚠️ PARTIAL (58) — observed User-Controlled Filename Passed to QProcess (LibreOffice import) (src/documenthandler.cpp:1076)
- **deepseek:** ✅ LEGIT (70) — User-controlled fileName appended to QProcess args at doc.cpp:1076-1077; file named --help.odt would inject flags into LibreOffice — flag injection confirmed

### [SET-01] macOS/iOS: QSettings split across two preference domains  ·  _SPLIT_  ·  High
`documenthandler.cpp, globalhotkeys.cpp`
- **opus:** ⚠️ PARTIAL (45) — macOS/iOS QSettings uses different domain combo but consistent within platform
- **gpt:** ✅ LEGIT (84) — macOS/iOS: QSettings split across two preference domains (src/documenthandler.cpp:132)
- **deepseek:** ✅ LEGIT (90) — C++ QSettings uses organizationDomain() (com.cuperino.qprompt) QML uses default (Cuperino/qprompt) — split domains

### [SET-02] factoryReset() incomplete on macOS/iOS — domain-path settings survive  ·  _SPLIT_  ·  High
`qmlutil.hpp:135-137`
- **opus:** ❔ UNSURE (45) — factoryReset default QSettings; appName already lowercase so likely matches (qmlutil.hpp:135)
- **gpt:** ✅ LEGIT (84) — factoryReset() incomplete on macOS/iOS - domain-path settings survive (src/qmlutil.hpp:135)
- **deepseek:** ✅ LEGIT (90) — factoryReset() at qmlutil.hpp:135 clears only default QSettings domain — C++ domain settings survive

### [SET-03] QString "true" used as default for boolean QSettings value  ·  _SPLIT_  ·  Low
`documenthandler.cpp:137`
- **opus:** ⚠️ PARTIAL (50) — string 'true' default for bool toBool() works correctly; cosmetic (documenthandler.cpp:137)
- **gpt:** ✅ LEGIT (78) — QString "true" used as default for boolean QSettings value (src/documenthandler.cpp:137)
- **deepseek:** ✅ LEGIT (85) — Default 'true' (QString) for bool QSettings at documenthandler.cpp:137 — fragile cross-type conversion

### [SET-04] spellCheckLanguages read without explicit default value  ·  _SPLIT_  ·  Low
`documenthandler.cpp:153`
- **opus:** ⚠️ PARTIAL (45) — spellCheckLanguages read; empty-list default is fine (documenthandler.cpp:153)
- **gpt:** ✅ LEGIT (78) — spellCheckLanguages read without explicit default value (src/documenthandler.cpp:153)
- **deepseek:** ✅ LEGIT (85) — settings.value() without default at documenthandler.cpp:153 — inconsistent with all other calls

### [SETUP-N01] setup.sh uses windeployqt.exe (Qt 5) — should be windeployqt6.exe (Qt 6)  ·  _SPLIT_  ·  Medium
`setup.sh:233`
- **opus:** ❔ UNSURE (40) — setup.sh windeployqt; Qt6 tool is still 'windeployqt' not '6' (setup.sh:233)
- **gpt:** ❔ UNSURE (39) — Qt 6 still ships windeployqt, so the tool name alone is not wrong (setup.sh:233)
- **deepseek:** ✅ LEGIT (95) — setup.sh:233: windeployqt.exe is Qt5 tool; Qt6 ships windeployqt6.exe — on Qt6-only machines tool not found mixed Qt5+6 deploys wrong DLLs

### [SHADOW-N04] id: frame shadows property bool frame — latent hazard  ·  _SPLIT_  ·  Low
`Countdown.qml:42,152`
- **opus:** ⚠️ PARTIAL (50) — id: frame may shadow property bool frame; latent (Countdown.qml:42)
- **gpt:** ✅ LEGIT (78) — id: frame shadows property bool frame - latent hazard (src/prompter/Countdown.qml:42)
- **deepseek:** ✅ LEGIT (65) — Shape id:frame shadows property bool frame; access within Countdown ambiguous (Countdown.qml:42 152)

### [SHAPE-N02] concentricCircles Shape uses parent-space coordinates in local space — circles off-center  ·  _SPLIT_  ·  Medium
`Countdown.qml:202-239`
- **opus:** ❔ UNSURE (45) — concentricCircles parent-space coords; domain (Countdown.qml:202)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Countdown.qml:202)
- **deepseek:** ✅ LEGIT (85) — offsetCentre/prompter.centreY parent-space(~640px) in Shape local coords(84px); circles render far offscreen at Countdown.qml:202-239

### [SHT-N01] markerToggle/namedMarkerToggle forwarded but never handled — dead hotkeys  ·  _SPLIT_  ·  Medium
`Prompter.qml:2097-2098,2118,2672-2870`
- **opus:** ⚠️ PARTIAL (50) — markerToggle/namedMarkerToggle forwarded but unhandled (Prompter.qml:2097)
- **gpt:** ⚠️ PARTIAL (58) — observed markerToggle/namedMarkerToggle forwarded but never handled - dead hotkeys (src/prompter/Prompter.qml:2097)
- **deepseek:** ✅ LEGIT (90) — Prompter.qml:2097-2098 editor forwards markerToggle/namedMarkerToggle to prompter.Keys.onPressed:2672-2870 which never handles either key

### [SIG-N03] MessageDialog.onButtonClicked declares unused second parameter role  ·  _SPLIT_  ·  Low
`main.qml:1088, +windows:757,777,797, +android:681,701`
- **opus:** ⚠️ PARTIAL (40) — MessageDialog.onButtonClicked unused 2nd param; harmless (main.qml:1088)
- **gpt:** ✅ LEGIT (78) — MessageDialog.onButtonClicked declares unused second parameter role (src/kirigami_ui/main.qml:1088)
- **deepseek:** ✅ LEGIT (75) — main.qml:1088 +windows:757 777 797 +android:681 701: MessageDialog buttonClicked signal has 1 param (StandardButton) but handlers declare (button role) — role always undefined

### [SPL2-20] loadCustomWordsFromDisk redundant exists() before open()  ·  _SPLIT_  ·  Low
`spellchecker.cpp:365-368`
- **opus:** ⚠️ PARTIAL (45) — loadCustomWordsFromDisk redundant exists() before open() (spellchecker.cpp:365)
- **gpt:** ⚠️ PARTIAL (58) — observed loadCustomWordsFromDisk redundant exists() before open() (src/spellchecker.cpp:365)
- **deepseek:** ❌ FALSE (85) — exists() before open() is defensive programming preventing TOCTOU race; not redundant best practice (spellchecker.cpp:365-368)

### [ST-N02] Dead overlay.state PropertyChanges — overlay has no states array  ·  _SPLIT_  ·  Medium
`ReadRegionOverlay.qml:34-37, Prompter.qml:2899-3032`
- **opus:** ✅ LEGIT (50) — dead overlay.state PropertyChanges; overlay has no states (ReadRegionOverlay.qml:34)
- **gpt:** ⚠️ PARTIAL (58) — observed Dead overlay.state PropertyChanges - overlay has no states array (src/prompter/ReadRegionOverlay.qml:34)
- **deepseek:** ✅ LEGIT (95) — ReadRegionOverlay.qml:34-37 has enum States but no states: array; Prompter.qml:2899 overlay.state PropertyChanges is dead property assignment

### [STATE-N01] Shadowed Prompting→Editing transition — velocity default never saved  ·  _SPLIT_  ·  High
`Prompter.qml:3119-3137`
- **opus:** ❔ UNSURE (45) — shadowed Prompting->Editing transition claim; needs state-machine trace (Prompter.qml:3119)
- **gpt:** ✅ LEGIT (84) — Shadowed Prompting->Editing transition - velocity default never saved (src/prompter/Prompter.qml:3119)
- **deepseek:** ⚠️ PARTIAL (50) — specific Prompting->Editing transition(line 3129) takes priority over general(line 3119) per QML rules (Prompter.qml:3119-3137)

### [STATE-N02] Find.toggle() uses !visible instead of !isOpen — can't close during Prompting  ·  _SPLIT_  ·  Medium
`Find.qml:51`
- **opus:** ⚠️ PARTIAL (50) — toggle() uses !visible vs !isOpen; can desync (Find.qml:51)
- **gpt:** ✅ LEGIT (78) — Find.toggle() uses !visible instead of !isOpen - can't close during Prompting (src/prompter/Find.qml:51)
- **deepseek:** ✅ LEGIT (75) — toggle() uses !visible which desyncs from isOpen state machine flag (Find.qml:51)

### [STATE-N03] Countdown Running restarts dissolveIn unnecessarily — visual dim-to-bright flash  ·  _SPLIT_  ·  Low
`Countdown.qml:289`
- **opus:** ⚠️ PARTIAL (50) — Running re-runs dissolveIn; visual flash (Countdown.qml:289)
- **gpt:** ✅ LEGIT (78) — Countdown Running restarts dissolveIn unnecessarily - visual dim-to-bright flash (src/prompter/Countdown.qml:289)
- **deepseek:** ✅ LEGIT (65) — Running state always restarts dissolveIn when re-entered causing visual flash (Countdown.qml:289)

### [STATE-N04] loop animation cancel() state change overridden by toggle() due to QML batching  ·  _SPLIT_  ·  Low
`Prompter.qml:900-907`
- **opus:** ❔ UNSURE (45) — loop cancel() vs toggle() QML batching; domain (Prompter.qml:900)
- **gpt:** ✅ LEGIT (78) — loop animation cancel() state change overridden by toggle() due to QML batching (src/prompter/Prompter.qml:900)
- **deepseek:** ✅ LEGIT (70) — cancel() then toggle() in same ScriptAction batch; QML batching may override cancel (Prompter.qml:900-907)

### [STC-N01] closeAll() destroys user's per-screen projection flip configuration  ·  _SPLIT_  ·  Medium
`ProjectionsManager.qml:130-132`
- **opus:** ✅ LEGIT (55) — closeAll() displayModel.clear() wipes per-screen flip config (ProjectionsManager.qml:130)
- **gpt:** ⚠️ PARTIAL (58) — observed closeAll() destroys user's per-screen projection flip configuration (src/prompter/ProjectionsManager.qml:130)
- **deepseek:** ✅ LEGIT (90) — ProjectionsManager.qml:130-132: closeAll clears displayModel holding per-screen flipSetting values; toggling projections off discards all custom config

### [STC-N02] Find.qml close() doesn't reset replace-mode or regex-mode flags  ·  _SPLIT_  ·  Low
`Find.qml:58-62`
- **opus:** ⚠️ PARTIAL (45) — close() doesn't reset replace/regex flags (Find.qml:58)
- **gpt:** ⚠️ PARTIAL (58) — observed Find.qml close() doesn't reset replace-mode or regex-mode flags (src/prompter/Find.qml:58)
- **deepseek:** ✅ LEGIT (85) — Find.qml:58-62: close() sets isOpen=false focusSearch() but doesn't reset find.replace or find.regEx; stale mode carried to next session

### [STC-N03] velocityIndicator.firstResetDone never cleared on dismiss — second activation broken  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:799-872,928-937`
- **opus:** ❔ UNSURE (45) — velocityIndicator.firstResetDone not cleared on dismiss; domain (PrompterPage.qml:799)
- **gpt:** ⚠️ PARTIAL (58) — observed velocityIndicator.firstResetDone never cleared on dismiss - second activation broken (src/kirigami_ui/PrompterPage.qml:799)
- **deepseek:** ✅ LEGIT (90) — PrompterPage.qml:928-937: dismiss() never clears firstResetDone/originX/Y; second activation cursor warps to page-middle not indicator-center

### [STC-N04] Projection window CursorAutoHide not reset on close — cursor permanently hidden  ·  _SPLIT_  ·  Medium
`ProjectionsManager.qml:202-206,196-200`
- **opus:** ⚠️ PARTIAL (50) — projection CursorAutoHide not reset on close (ProjectionsManager.qml:202)
- **gpt:** ⚠️ PARTIAL (58) — observed Projection window CursorAutoHide not reset on close - cursor permanently hidden (src/prompter/ProjectionsManager.qml:202)
- **deepseek:** ✅ LEGIT (85) — ProjectionsManager.qml:202-206 196-200: onClosing never calls cursorAutoHide.reset(); cursor stays hidden system-wide after window destruction

### [STC-N05] cancel() doesn't call timer.stopTimer() — elapsed time persists across sessions  ·  _SPLIT_  ·  Low
`Prompter.qml:460-466`
- **opus:** ⚠️ PARTIAL (50) — cancel() doesn't stopTimer(); elapsed persists (Prompter.qml:460)
- **gpt:** ⚠️ PARTIAL (58) — observed cancel() doesn't call timer.stopTimer() - elapsed time persists across sessions (src/prompter/Prompter.qml:460)
- **deepseek:** ✅ LEGIT (85) — Prompter.qml:432-435: cancel() sets state to Editing but doesn't call timer.stopTimer(); elapsed time persists across prompting sessions

### [STR-CNV] 5 defensive validation gaps: toInt() without ok flag in getMarkerKey, parse(×2), setFontSize, and 32 hotkey reads  ·  _SPLIT_  ·  Low
`documenthandler.cpp:757,1667,1675,829, globalhotkeys.cpp:569-698`
- **opus:** ⚠️ PARTIAL (45) — several toInt() without ok flag; defensive gap (documenthandler.cpp:757)
- **gpt:** ✅ LEGIT (78) — 5 defensive validation gaps: toInt() without ok flag in getMarkerKey, parse(×2), setFontSize, and 32 hotkey reads (src/documenthandler.cpp:757)
- **deepseek:** ✅ LEGIT (60) — multiple toInt() calls without ok flag silently discard parse failures (documenthandler.cpp:757 829)

### [SYM-N01] 6 RTL/symmetry issues across PointerSettings, Find, PrompterView, Prompter, PrompterPage  ·  _SPLIT_  ·  Low-Medium
`PointerSettings.qml:380 (right pointer label not RTL-mirrored), Find.qml:63-66 (search bar always left-pinned), PrompterView.qml:74-76 (upper controls not RTL-aware), Prompter.qml:658-659 (goToNextMarker has end-fallback but goToPreviousMarker lacks start-fallback), PrompterPage.qml:266,278 (pointer tooltips not RTL-mirrored, contradict button labels)`
- **opus:** ⚠️ PARTIAL (40) — 6 RTL/symmetry issues (PointerSettings.qml:380)
- **gpt:** ⚠️ PARTIAL (58) — observed 6 RTL/symmetry issues across PointerSettings, Find, PrompterView, Prompter, PrompterPage (src/prompter/PointerSettings.qml:380)
- **deepseek:** ✅ LEGIT (85) — 6 RTL issues: PointerSettings.qml:380 label not mirrored; Find.qml:63-66 left-pinned; PrompterView.qml:74-76 not RTL-aware; Prompter.qml:658-659 one-sided fallback; PrompterPage.qml:266 tooltip not RTL-mirrored

### [TAB-N01] PointerSettings TabButton onClicked skips currentIndex assignment  ·  _SPLIT_  ·  Medium
`PointerSettings.qml:268-289`
- **opus:** ⚠️ PARTIAL (50) — TabButton onClicked skips currentIndex assignment (PointerSettings.qml:268)
- **gpt:** ✅ LEGIT (78) — PointerSettings TabButton onClicked skips currentIndex assignment (src/prompter/PointerSettings.qml:268)
- **deepseek:** ⚠️ PARTIAL (60) — PointerSettings.qml:268-289: TabButtons set positionViewAtIndex but never TabBar.currentIndex; however TabBar.currentIndex is bound to pointerSettings.pointerKind at line 266

### [TB-N01] toolbar toggle timers produce stale state on rapid clicks  ·  _SPLIT_  ·  Medium
`EditorToolbar.qml:816-851`
- **opus:** ⚠️ PARTIAL (45) — toggle timers stale state on rapid clicks (EditorToolbar.qml:816)
- **gpt:** ⚠️ PARTIAL (58) — observed toolbar toggle timers produce stale state on rapid clicks (src/kirigami_ui/EditorToolbar.qml:816)
- **deepseek:** ✅ LEGIT (85) — EditorToolbar.qml:816-851: 250ms delayed Timer toggles showFontSpacingOptions/showAnimationConfigOptions with stale pre-click state on rapid clicks

### [TB-N02] baseSpeedSlider/baseAccelerationSlider onMoved yanks focus to prompter instead of restoreFocus()  ·  _SPLIT_  ·  Medium
`EditorToolbar.qml:2009-2010,2128-2129`
- **opus:** ⚠️ PARTIAL (45) — slider onMoved yanks focus to prompter (EditorToolbar.qml:2009)
- **gpt:** ⚠️ PARTIAL (58) — observed baseSpeedSlider/baseAccelerationSlider onMoved yanks focus to prompter instead of restoreFocus( (src/kirigami_ui/EditorToolbar.qml:2009)
- **deepseek:** ✅ LEGIT (90) — EditorToolbar.qml:2009-2010 2128-2129: baseSpeed/AccelerationSlider onMoved sets viewport.prompter.focus=true instead of restoreFocus(); editor loses focus

### [TB-N03] Collapsible toolbar rows animate height but adjacent rows snap — no y-position animation  ·  _SPLIT_  ·  Low
`EditorToolbar.qml:1175-1906 (8 collapsible rows)`
- **opus:** ⚠️ PARTIAL (45) — collapsible rows animate height but neighbors snap (EditorToolbar.qml:1175)
- **gpt:** ⚠️ PARTIAL (58) — observed Collapsible toolbar rows animate height but adjacent rows snap - no y-position animation (src/kirigami_ui/EditorToolbar.qml:1175)
- **deepseek:** ✅ LEGIT (70) — EditorToolbar.qml: collapsible rows have Behavior on height but Flow recalculates siblings immediately; rows below snap without animation

### [TB-N04] velocityDragArea accepts MiddleButton without propagateComposedEvents — scroll blocked  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:875-884`
- **opus:** ⚠️ PARTIAL (50) — velocityDragArea accepts MiddleButton without propagateComposedEvents (PrompterPage.qml:875)
- **gpt:** ⚠️ PARTIAL (58) — observed velocityDragArea accepts MiddleButton without propagateComposedEvents - scroll blocked (src/kirigami_ui/PrompterPage.qml:875)
- **deepseek:** ✅ LEGIT (85) — PrompterPage.qml:875-884: velocityDragArea accepts MiddleButton without propagateComposedEvents; middle-click consumed scroll through viewport blocked

### [TBND-N01] SpellHighlighter regex excludes combining diacritical marks — NFD text misspelled  ·  _SPLIT_  ·  Medium
`spellhighlighter.cpp:53-54`
- **opus:** ⚠️ PARTIAL (50) — highlighter regex excludes combining diacritics; NFD text (spellhighlighter.cpp:53)
- **gpt:** ⚠️ PARTIAL (58) — observed SpellHighlighter regex excludes combining diacritical marks - NFD text misspelled (src/spellhighlighter.cpp:53)
- **deepseek:** ✅ LEGIT (70) — Regex \p{L}+ excludes \p{M} combining marks; NFD text cafe->cafe without accent->incorrect spellcheck at spellhighlighter.cpp:53-54

### [TBND-N02] All CJK text marked misspelled — ideographic characters not in Hunspell dictionaries  ·  _SPLIT_  ·  Medium
`spellhighlighter.cpp:53-54`
- **opus:** ⚠️ PARTIAL (50) — CJK marked misspelled; ideographs not in hunspell (spellhighlighter.cpp:53)
- **gpt:** ⚠️ PARTIAL (58) — observed All CJK text marked misspelled - ideographic characters not in Hunspell dictionaries (src/spellhighlighter.cpp:53)
- **deepseek:** ✅ LEGIT (90) — \p{L} matches CJK chars individually; Hunspell has zero ideograph entries->all CJK flagged misspelled at spellhighlighter.cpp:53-54

### [TC-N02] property color value assigned string expression — silent coercion  ·  _SPLIT_  ·  Low
`PointerSettings.qml:146,178,209`
- **opus:** ⚠️ PARTIAL (45) — property color assigned string expression; coercion (PointerSettings.qml:146)
- **gpt:** ⚠️ PARTIAL (58) — observed property color value assigned string expression - silent coercion (src/prompter/PointerSettings.qml:146)
- **deepseek:** ✅ LEGIT (80) — PointerSettings.qml:146 178 209: property color value assigned from text (string) via ternary; silent string->color coercion

### [THM-SYS] Complete theme deadlock — 50+ Material.theme: Dark hardcoded, theme toggle commented out  ·  _SPLIT_  ·  High
`14 QML files`
- **opus:** ⚠️ PARTIAL (55) — 50+ hardcoded Material.theme:Dark means runtime theme toggle is effectively dead (multi-file)
- **gpt:** ⚠️ PARTIAL (58) — visual issue is plausible but depends on theme or device (src/kirigami_ui/main.qml:122)
- **deepseek:** ✅ LEGIT (90) — Material.theme: Material.Dark hardcoded across ~50 controls in 14+ QML files; theme toggle commented out; no light mode support

### [THR-01] IosSaveDialog::create() — unsynchronized singleton race  ·  _SPLIT_  ·  Medium
`iossavedialog.cpp:37-42`
- **opus:** ⚠️ PARTIAL (45) — IosSaveDialog::create unsynchronized singleton race; single-threaded (iossavedialog.cpp:37)
- **gpt:** ⚠️ PARTIAL (58) — observed IosSaveDialog::create() - unsynchronized singleton race (src/iossavedialog.cpp:37)
- **deepseek:** ✅ LEGIT (82) — QML singleton create() runs on main thread; check-then-act pattern is sloppy but not currently racy (iossavedialog.cpp:37-42)

### [THR-02] ShakeDetector::create() — identical unsynchronized singleton race  ·  _SPLIT_  ·  Medium
`shakedetector.cpp:38-43`
- **opus:** ⚠️ PARTIAL (45) — ShakeDetector::create singleton race (dup THR-01) (shakedetector.cpp:38)
- **gpt:** ⚠️ PARTIAL (58) — observed ShakeDetector::create() - identical unsynchronized singleton race (src/shakedetector.cpp:38)
- **deepseek:** ✅ LEGIT (82) — same QML singleton pattern as THR-01; main-thread creation no actual concurrency (shakedetector.cpp:38-43)

### [THR-03] search() — mutable static QRegularExpression shared across all callers  ·  _SPLIT_  ·  Low
`documenthandler.cpp:1543-1544`
- **opus:** ⚠️ PARTIAL (50) — static QRegularExpression shared/mutated; OK single-threaded (documenthandler.cpp:1543)
- **gpt:** ⚠️ PARTIAL (58) — observed search() - mutable static QRegularExpression shared across all callers (src/documenthandler.cpp:1543)
- **deepseek:** ✅ LEGIT (80) — mutable static QRegularExpression shared across calls; main-thread only currently no actual data race (documenthandler.cpp:1543-1544)

### [THR-04] SpellChecker zero thread safety — explicit finding  ·  _SPLIT_  ·  Medium
`spellchecker.h:76-77, spellchecker.cpp`
- **opus:** ⚠️ PARTIAL (45) — SpellChecker zero thread safety (dup R3-SPL-05) (spellchecker.h:76)
- **gpt:** ✅ LEGIT (78) — SpellChecker zero thread safety - explicit finding (src/spellchecker.h:76)
- **deepseek:** ⚠️ PARTIAL (72) — m_dicts+m_customWords no mutex; Qt6.7+ async QSyntaxHighlighter could cause concurrent spell/suggest vs mutate (spellchecker.h:76-77)

### [TMR-01] Countdown→Prompting auto-transition via state++ bypasses toggle() entirely  ·  _SPLIT_  ·  High
`Countdown.qml:123`
- **opus:** ❔ UNSURE (50) — state++ bypasses toggle() side-effects (dup FINAL-16); state-machine claim (Countdown.qml:123)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Countdown.qml:123)
- **deepseek:** ✅ LEGIT (92) — prompter.state++ skips toggle():timer.reset document.parse preventSleep projections fix (Countdown.qml:123)

### [TMR-02] timer.updateTimer() runs before timer.startTimer() on Prompting entry  ·  _SPLIT_  ·  Medium
`Prompter.qml:3093 vs :3113`
- **opus:** ❔ UNSURE (45) — updateTimer before startTimer on Prompting entry; domain (Prompter.qml:3093)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Prompter.qml:3093)
- **deepseek:** ✅ LEGIT (80) — updateTimer runs before startTimer in Prompting transition; computes elapsed with stale startTime (Prompter.qml:3093 vs 3113)

### [TMR-03] dissolveIn animation re-triggered entering Running from Ready — flicker  ·  _SPLIT_  ·  Medium
`Countdown.qml:274-276,289-291`
- **opus:** ⚠️ PARTIAL (50) — dissolveIn re-triggered Ready->Running; flicker (Countdown.qml:274)
- **gpt:** ⚠️ PARTIAL (58) — observed dissolveIn animation re-triggered entering Running from Ready - flicker (src/prompter/Countdown.qml:274)
- **deepseek:** ✅ LEGIT (85) — dissolveIn.running:true in both Ready and Running states; Ready->Running restarts from 0 causing flicker (Countdown.qml:274-276 289-291)

### [TMR-04] Countdown arc hypotenuse uses geometric center instead of arc center  ·  _SPLIT_  ·  Low
`Countdown.qml:79`
- **opus:** ❔ UNSURE (45) — arc hypotenuse 1.4333 magic geometry (Countdown.qml:79)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Countdown.qml:79)
- **deepseek:** ✅ LEGIT (80) — hypotenuse uses prompter.centreX/Y but arc drawn at offsetCentre; radius mismatch when scrolled (Countdown.qml:79)

### [TMR-06] dissolveOut starts too early when disappearWithin > 1  ·  _SPLIT_  ·  Low
`Countdown.qml:110-113,145`
- **opus:** ❔ UNSURE (45) — dissolveOut early when disappearWithin>1; domain (Countdown.qml:110)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Countdown.qml:110)
- **deepseek:** ✅ LEGIT (85) — dissolveOut 1000ms duration starts disappearWithin-1 iterations early; visible text prematurely (Countdown.qml:110-113 145)

### [TMR-07] countdownAnimation restart uses non-idempotent running=true  ·  _SPLIT_  ·  Low
`Countdown.qml:119`
- **opus:** ✅ LEGIT (55) — countdownAnimation running=true imperative breaks binding (Countdown.qml:119)
- **gpt:** ⚠️ PARTIAL (58) — observed countdownAnimation restart uses non-idempotent running=true (src/prompter/Countdown.qml:119)
- **deepseek:** ⚠️ PARTIAL (65) — running=true on already-running animation; some Qt versions accept restart Qt Quick docs ambiguous (Countdown.qml:119)

### [TMR-08] timer.running not explicitly set in Countdown state — relies on revert behavior  ·  _SPLIT_  ·  Low
`Prompter.qml:2980-3026`
- **opus:** ❔ UNSURE (45) — timer.running relies on state revert; domain (Prompter.qml:2980)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Prompter.qml:2980)
- **deepseek:** ✅ LEGIT (80) — timer.running not set in Countdown State(2980-3026); relies on revert; interrupted transition leaves stale (Prompter.qml:2980-3026)

### [TMR-N01] resetBackground Timer not stopped when new background loaded — race erases new image  ·  _SPLIT_  ·  Medium
`PrompterBackground.qml:47-57,73-76`
- **opus:** ⚠️ PARTIAL (50) — resetBackground Timer not stopped on new bg; race (PrompterBackground.qml:47)
- **gpt:** ⚠️ PARTIAL (58) — observed resetBackground Timer not stopped when new background loaded - race erases new image (src/prompter/PrompterBackground.qml:47)
- **deepseek:** ✅ LEGIT (95) — PrompterBackground.qml:47-57/73-76: clearBackground() starts 2.8s resetBackground timer; setBackgroundImage() never stops it — race erases new image after ~2.8s

### [TMR-N02] Windows onFrameSwapped missing qmlutil.r(p) — per-frame grab result leak  ·  _SPLIT_  ·  Medium
`+windows/main.qml:706-716 vs main.qml:1036-1047`
- **opus:** ⚠️ PARTIAL (50) — +windows onFrameSwapped omits qmlutil.r(p); grab result not released (main.qml:706)
- **gpt:** ⚠️ PARTIAL (58) — observed Windows onFrameSwapped missing qmlutil.r(p) - per-frame grab result leak (src/kirigami_ui/+windows/main.qml:706)
- **deepseek:** ✅ LEGIT (90) — +windows/main.qml:706-716 vs main.qml:1036-1047: Windows variant missing qmlutil.r(p) call after grabToImage — per-frame QQuickItemGrabResult leak at 60fps

### [TMR-N05] markerCompare() only fires on forward scroll — backward scroll + re-forward misses marker  ·  _SPLIT_  ·  High
`Prompter.qml:391-420`
- **opus:** ❔ UNSURE (45) — markerCompare forward-only claim; needs full function (Prompter.qml:391)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Prompter.qml:391)
- **deepseek:** ✅ LEGIT (90) — Prompter.qml:391-420: if(prompter.q<p) only triggers on forward scroll; after overshoot+backward q stays stale; re-forward q==p skips marker

### [TMR-N06] Auto-reload Timer persists after network dialog close — background refetches  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:1246-1253,1415-1420`
- **opus:** ⚠️ PARTIAL (50) — auto-reload Timer persists after network dialog close (PrompterPage.qml:1246)
- **gpt:** ✅ LEGIT (78) — Auto-reload Timer persists after network dialog close - background refetches (src/kirigami_ui/PrompterPage.qml:1246)
- **deepseek:** ✅ LEGIT (90) — PrompterPage.qml:1246-1253 1415-1420: onClosed doesn't set autoReloadRunning=false; Timer keeps firing openFromRemote() without visible UI

### [TOG-N01] WheelSettingsOverlay useScrollAsDialButton — cross-path stale checked state  ·  _SPLIT_  ·  Medium
`WheelSettingsOverlay.qml:50-60`
- **opus:** ⚠️ PARTIAL (50) — useScrollAsDialButton cross-path stale checked (WheelSettingsOverlay.qml:50)
- **gpt:** ⚠️ PARTIAL (58) — observed WheelSettingsOverlay useScrollAsDialButton - cross-path stale checked state (src/kirigami_ui/WheelSettingsOverlay.qml:50)
- **deepseek:** ✅ LEGIT (85) — WheelSettingsOverlay.qml:50-60: checked: root.__scrollAsDial binding breaks on click; changing via 3 other paths leaves stale state

### [TP-N01] "Error loading file..." used as document content, not placeholderText  ·  _SPLIT_  ·  Medium
`Prompter.qml:969`
- **opus:** ⚠️ PARTIAL (55) — 'Error loading file' shown as document content not placeholder (Prompter.qml:969)
- **gpt:** ⚠️ PARTIAL (58) — observed "Error loading file..." used as document content, not placeholderText (src/prompter/Prompter.qml:969)
- **deepseek:** ✅ LEGIT (90) — Prompter.qml:969: qsTr('Error loading file...') assigned as TextArea.text content not placeholderText; shows as editable document body

### [TRF-N01] rightWidthAdjustmentBar drag.maximumX formula broken — drag collapses to single point  ·  _SPLIT_  ·  High
`Prompter.qml:2022`
- **opus:** ⚠️ PARTIAL (50) — rightWidthAdjustmentBar maximumX collapses when minimumX>=maxX (Prompter.qml:2022)
- **gpt:** ⚠️ PARTIAL (58) — observed rightWidthAdjustmentBar drag.maximumX formula broken - drag collapses to single point (src/prompter/Prompter.qml:2022)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:2022: maxX=prompter.width-editor.x-parent.width-LM-13; with parent.width~=prompter.width: maxX ~= -editor.x-LM-13 < drag.minimumX always

### [TRL-N01] qsTr() uses %0 placeholder — should be %1 (font name never displayed)  ·  _SPLIT_  ·  High
`src/kirigami_ui/EditorToolbar.qml:588`
- **opus:** ⚠️ PARTIAL (55) — qsTr('Active font: %0'); %0 unconventional, Qt arg() handling uncertain (EditorToolbar.qml:588)
- **gpt:** ✅ LEGIT (84) — qsTr() uses %0 placeholder - should be %1 (font name never displayed) (src/kirigami_ui/EditorToolbar.qml:588)
- **deepseek:** ✅ LEGIT (95) — Qt arg() uses 1-based %1 %2; %0 treated as literal font name never displayed (EditorToolbar.qml:588)

### [TRL-N03] About-dialog credit roles not translatable  ·  _SPLIT_  ·  Medium
`src/main.cpp:194,202,205-206`
- **opus:** ⚠️ PARTIAL (45) — About credit roles not translatable (main.cpp:194)
- **gpt:** ✅ LEGIT (78) — About-dialog credit roles not translatable (src/main.cpp:194)
- **deepseek:** ✅ LEGIT (90) — credit roles use QLatin1String not tr(); About dialog always English (main.cpp:194 202 205-206)

### [TS-01] Finnish welcome guide → Dutch (not Finnish)  ·  _SPLIT_  ·  
`po/qprompt_fi.ts:656 — `welcome_nl.html` should be `welcome_fi.html``
- **opus:** ❔ UNSURE (40) — Finnish welcome -> Dutch html ref; translation/structural (qprompt_fi.ts:656)
- **gpt:** ⚠️ PARTIAL (58) — observed Finnish welcome guide -> Dutch (not Finnish) (po/qprompt_fi.ts:656)
- **deepseek:** ✅ LEGIT (88) — Finnish welcome_en.html->welcome_nl.html(Dutch) should be welcome_fi.html (po/qprompt_fi.ts:656)

### [TS-02] Arabic file `ar_EG` vs UI `ar_AE` mismatch  ·  _SPLIT_  ·  
`po/qprompt_ar.ts:3 — `language="ar_EG"` but LanguageSettingsOverlay.qml uses `ar_AE``
- **opus:** ⚠️ PARTIAL (50) — ar_EG file vs ar_AE UI locale mismatch; structural (qprompt_ar.ts:3)
- **gpt:** ⚠️ PARTIAL (58) — observed Arabic file arEG vs UI arAE mismatch (po/qprompt_ar.ts:3)
- **deepseek:** ✅ LEGIT (90) — Arabic .ts declares ar_EG but LanguageSettingsOverlay uses ar_AE; locale mismatch (po/qprompt_ar.ts:3)

### [TS-04] French "Saved" → verb "Enregistrer" (should be adjective "Enregistré")  ·  _SPLIT_  ·  
`po/qprompt_fr.ts:679`
- **opus:** ❔ UNSURE (40) — French Saved verb-vs-adjective; semantic (qprompt_fr.ts:679)
- **gpt:** ❔ UNSURE (39) — semantic translation nuance needs French review (po/qprompt_fr.ts:679)
- **deepseek:** ✅ LEGIT (85) — French Saved->Enregistrer(verb to save) should be Enregistré(adjective saved) (po/qprompt_fr.ts:679)

### [TS-05] Finnish/French/Korean/Italian "Saved" → verb with stray `&amp;` accelerator  ·  _SPLIT_  ·  
`po/qprompt_fi.ts:678, po/qprompt_ko.ts:677, po/qprompt_it.ts:679`
- **opus:** ⚠️ PARTIAL (45) — stray &amp; accelerator in 'Saved'; structural (qprompt_fi.ts:678)
- **gpt:** ⚠️ PARTIAL (58) — observed Finnish/French/Korean/Italian "Saved" -> verb with stray &amp; accelerator (po/qprompt_fi.ts:678)
- **deepseek:** ✅ LEGIT (85) — Finnish Saved->&amp;Tallenna with stray &amp; accelerator; same in ko/it (po/qprompt_fi.ts:678)

### [TS-06] Czech/French "Language settings" → "Pointer settings" (copy-paste error)  ·  _SPLIT_  ·  
`po/qprompt_cs.ts:354, po/qprompt_fr.ts:353`
- **opus:** ❔ UNSURE (40) — Language settings->Pointer settings copy-paste; semantic (qprompt_cs.ts:354)
- **gpt:** ❔ UNSURE (39) — translation meaning cannot be verified from code alone (po/qprompt_cs.ts:354)
- **deepseek:** ✅ LEGIT (90) — Czech Language settings->Nastavení ukazatele(Pointer settings); copy-paste error (po/qprompt_cs.ts:354)

### [TS-07] Finnish/French/Korean "Colors for prompter states" → "Toggle Prompter State"  ·  _SPLIT_  ·  
`po/qprompt_fi.ts:462, po/qprompt_fr.ts:463`
- **opus:** ❔ UNSURE (40) — semantic mistranslation claim; needs language expertise (qprompt_fi.ts:462)
- **gpt:** ❔ UNSURE (39) — wrong-word translation claim is semantic, not structurally provable (po/qprompt_fi.ts:462)
- **deepseek:** ✅ LEGIT (85) — Colors for prompter states->Toggle Prompter State in fi/fr/ko; wrong meaning (po/qprompt_fi.ts:462)

### [TS-08] French "Prompting:" → "Start prompter"  ·  _SPLIT_  ·  
`po/qprompt_fr.ts:478`
- **opus:** ❔ UNSURE (40) — semantic mistranslation claim (qprompt_fr.ts:478)
- **gpt:** ❔ UNSURE (39) — translation meaning cannot be verified from code alone (po/qprompt_fr.ts:478)
- **deepseek:** ✅ LEGIT (85) — French Prompting:->Démarrer prompter(Start prompter); semantic error (po/qprompt_fr.ts:478)

### [TS-09] Finnish/French/Korean/Dutch "Vertical offset" → "Velocity"  ·  _SPLIT_  ·  
`po/qprompt_fi.ts:560, po/qprompt_fr.ts:561, po/qprompt_ko.ts:559, po/qprompt_nl.ts:561`
- **opus:** ❔ UNSURE (40) — semantic mistranslation claim (qprompt_fi.ts:560)
- **gpt:** ❔ UNSURE (39) — translation meaning cannot be verified from code alone (po/qprompt_fi.ts:560)
- **deepseek:** ✅ LEGIT (85) — Vertical offset->Velocity in fi/fr/ko/nl; wrong term translated (po/qprompt_fi.ts:560)

### [TS-10] Finnish/Korean "Next reload starts at" → "Step acceleration"  ·  _SPLIT_  ·  
`po/qprompt_fi.ts:158, po/qprompt_ko.ts:158`
- **opus:** ❔ UNSURE (40) — semantic mistranslation claim (qprompt_fi.ts:158)
- **gpt:** ❔ UNSURE (39) — translation meaning cannot be verified from code alone (po/qprompt_fi.ts:158)
- **deepseek:** ✅ LEGIT (85) — Next reload starts at->Step acceleration in fi/ko; wrong meaning (po/qprompt_fi.ts:158)

### [TS-11] French/Finnish/Korean "No pointers" → "Both pointers" (opposite meaning)  ·  _SPLIT_  ·  
`po/qprompt_fr.ts:1003, po/qprompt_fi.ts:981, po/qprompt_ko.ts:980`
- **opus:** ❔ UNSURE (40) — opposite-meaning translation claim (qprompt_fr.ts:1003)
- **gpt:** ❔ UNSURE (39) — translation meaning cannot be verified from code alone (po/qprompt_fr.ts:1003)
- **deepseek:** ✅ LEGIT (90) — No pointers->Both pointers in fr/fi/ko; opposite meaning (po/qprompt_fr.ts:1003)

### [TS-12] French "Alt" key → "Tout" (means "All")  ·  _SPLIT_  ·  
`po/qprompt_fr.ts:270`
- **opus:** ❔ UNSURE (40) — French Alt->Tout semantic claim (qprompt_fr.ts:270)
- **gpt:** ❔ UNSURE (39) — translation meaning cannot be verified from code alone (po/qprompt_fr.ts:270)
- **deepseek:** ✅ LEGIT (90) — French Alt->Tout(means All); clearly wrong translation (po/qprompt_fr.ts:270)

### [TS-13] French "Set velocity to 0–10" (all 11) → identical "Vitesse de départ"  ·  _SPLIT_  ·  
`po/qprompt_fr.ts:276-337`
- **opus:** ❔ UNSURE (40) — 11 identical 'Vitesse de depart'; semantic (qprompt_fr.ts:276)
- **gpt:** ❔ UNSURE (39) — translation meaning cannot be verified from code alone (po/qprompt_fr.ts:276)
- **deepseek:** ✅ LEGIT (90) — French all 11 Set velocity X->identical Vitesse de départ; no distinction (po/qprompt_fr.ts:276-337)

### [TS-14] French "Clear color" → "Light color"  ·  _SPLIT_  ·  
`po/qprompt_fr.ts:1048`
- **opus:** ❔ UNSURE (40) — French Clear color->Light color; semantic (qprompt_fr.ts:1048)
- **gpt:** ❔ UNSURE (39) — translation meaning cannot be verified from code alone (po/qprompt_fr.ts:1048)
- **deepseek:** ✅ LEGIT (85) — French Clear color->Couleur claire(Light color); wrong translation (po/qprompt_fr.ts:1048)

### [TS-15] Finnish/Korean right pointer reuse → left pointer (swapped)  ·  _SPLIT_  ·  
`po/qprompt_fi.ts:494, po/qprompt_ko.ts:493`
- **opus:** ❔ UNSURE (40) — semantic mistranslation claim (qprompt_fi.ts:494)
- **gpt:** ❔ UNSURE (39) — translation meaning cannot be verified from code alone (po/qprompt_fi.ts:494)
- **deepseek:** ✅ LEGIT (85) — right pointer translations reuse left pointer text in fi/ko; swapped (po/qprompt_fi.ts:494 po/qprompt_ko.ts:493)

### [TS-16] Paragraph spacing: 8 languages strip trailing `%` from `<pre>%1%</pre>`  ·  _SPLIT_  ·  
`po/qprompt_cs.ts:128, po/qprompt_de.ts:132, po/qprompt_es.ts:132, po/qprompt_fr.ts:128, po/qprompt_fi.ts:128, po/qprompt_ko.ts:128, po/qprompt_nl.ts:128, po/qprompt_zh.ts:128`
- **opus:** ⚠️ PARTIAL (45) — <pre>%1%</pre> trailing % stripped; placeholder/structural (qprompt_cs.ts:128)
- **gpt:** ⚠️ PARTIAL (58) — observed Paragraph spacing: 8 languages strip trailing % from pre%1%/pre (po/qprompt_cs.ts:128)
- **deepseek:** ✅ LEGIT (90) — 8 languages strip trailing % from <pre>%1%</pre> markup; format broken (po/qprompt_cs.ts:128)

### [TS-17] Line width: 7 languages add spurious `%` to `<pre>%1</pre>`  ·  _SPLIT_  ·  
`po/qprompt_de.ts:539, po/qprompt_es.ts:543, po/qprompt_fi.ts:529, po/qprompt_fr.ts:530, po/qprompt_ko.ts:528, po/qprompt_nl.ts:530, po/qprompt_pt_BR.ts:539, po/qprompt_zh.ts:539`
- **opus:** ⚠️ PARTIAL (45) — <pre>%1</pre> spurious % in 7 langs; placeholder/structural (qprompt_de.ts:539)
- **gpt:** ⚠️ PARTIAL (58) — observed Line width: 7 languages add spurious % to pre%1/pre (po/qprompt_de.ts:539)
- **deepseek:** ✅ LEGIT (90) — 7 languages add spurious % to <pre>%1</pre> markup; format broken (po/qprompt_de.ts:539)

### [TS-18] Orphan files: Hebrew and Polish exist but UI entries commented out  ·  _SPLIT_  ·  
`po/qprompt_he.ts, po/qprompt_pl.ts`
- **opus:** ❔ UNSURE (40) — Hebrew/Polish orphan files; UI entries commented out (qprompt_he.ts)
- **gpt:** ❔ UNSURE (39) — translation meaning cannot be verified from code alone (po/qprompt_he.ts:1)
- **deepseek:** ✅ LEGIT (85) — Hebrew/Polish .ts files exist but UI entries commented out; orphaned (po/qprompt_he.ts po/qprompt_pl.ts)

### [TXT-CRIT] Plain 'v'/'V' keypress silently consumed — letter 'v' cannot be typed  ·  _SPLIT_  ·  Critical
`Prompter.qml:2163-2168`
- **opus:** ❔ UNSURE (45) — Key_V consumed only matters if handler active in editing mode; likely state-gated (Prompter.qml:2166)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/Prompter.qml:2163)
- **deepseek:** ✅ LEGIT (85) — Prompter.qml:2163-2168: no-modifiers branch case Qt.Key_V forwards to prompter handler which only handles Ctrl+V paste; plain v keypress silently discarded — cannot type letter v

### [TXT-FMT-N01] setMarkerHref("") fails to clear QTextFormat::AnchorHref — stale href persists  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:769-774`
- **opus:** ✅ LEGIT (65) — setMarkerHref('') doesn't clear AnchorHref via mergeCharFormat (FINAL-21 family) (documenthandler.cpp:769)
- **gpt:** ⚠️ PARTIAL (58) — observed setMarkerHref("") fails to clear QTextFormat::AnchorHref - stale href persists (src/documenthandler.cpp:769)
- **deepseek:** ✅ LEGIT (80) — setMarkerHref('') sets setAnchor(false) but skips clearProperty(AnchorHref) at documenthandler.cpp:769-774; stale href persists

### [TXT-N02] TimerClock default text color #AAA on #131619 — fails WCAG AA contrast  ·  _SPLIT_  ·  Low
`TimerClock.qml:93,138,151,163`
- **opus:** ⚠️ PARTIAL (40) — #AAA on #131619 contrast (TimerClock.qml:93)
- **gpt:** ✅ LEGIT (78) — TimerClock default text color #AAA on #131619 - fails WCAG AA contrast (src/prompter/TimerClock.qml:93)
- **deepseek:** ✅ LEGIT (75) — #AAA on #131619 yields ~2.5:1 contrast ratio failing WCAG AA 4.5:1 minimum (TimerClock.qml:93 138)

### [TXT-N04] goToNextMarker() temporarily sets cursorPosition=-1 — corrupts cursor state  ·  _SPLIT_  ·  Medium
`Prompter.qml:656-659`
- **opus:** ⚠️ PARTIAL (50) — goToNextMarker temporarily sets cursorPosition=-1 (Prompter.qml:656)
- **gpt:** ⚠️ PARTIAL (58) — observed goToNextMarker() temporarily sets cursorPosition=-1 - corrupts cursor state (src/prompter/Prompter.qml:656)
- **deepseek:** ✅ LEGIT (85) — Prompter.qml:656-659: editor.cursorPosition set to nextMarker().position which is -1 when no markers exist; cursorPosition=-1 fires onChange signals before guard corrects

### [TYP-03] Floating-point equality comparison of window opacity  ·  _SPLIT_  ·  Medium
`src/main.cpp:273`
- **opus:** ⚠️ PARTIAL (60) — float ==1.0 but only 1.0/0.2 ever set (main.cpp:273)
- **gpt:** ⚠️ PARTIAL (58) — observed Floating-point equality comparison of window opacity (src/main.cpp:273)
- **deepseek:** ✅ LEGIT (85) — opacity()==1.0 at main.cpp:273 is exact floating-point equality on qreal(double); 0.9999999999!=1.0 — unreliable should use qFuzzyCompare

### [TYP-04] Bitwise AND on bools hides dead code in preventSleep  ·  _SPLIT_  ·  Medium
`src/documenthandler.cpp:1928,1931`
- **opus:** ✅ LEGIT (95) — false & prevent -> prevent dead (documenthandler.cpp:1928)
- **gpt:** ⚠️ PARTIAL (58) — observed Bitwise AND on bools hides dead code in preventSleep (src/documenthandler.cpp:1928)
- **deepseek:** ✅ LEGIT (90) — return false & prevent at doc.cpp:1928/1931; bitwise & on bool always 0(false) — prevent param dead code; should be && or just return false

### [TYP-05] Uninitialized pointer member m_reply in DocumentHandler  ·  _SPLIT_  ·  Medium
`src/documenthandler.h:353, src/documenthandler.cpp:123-158`
- **opus:** ✅ LEGIT (95) — m_reply uninitialized (documenthandler.h:353)
- **gpt:** ✅ LEGIT (88) — Uninitialized pointer member m_reply in DocumentHandler (src/documenthandler.h:353)
- **deepseek:** ⚠️ PARTIAL (60) — m_reply in doc.h:353 declared as raw pointer; not in constructor init list at doc.cpp:123-130; holds indeterminate value until loadFromNetwork sets it — real but low risk

### [TYP-06] Malformed preprocessor macro: `#define Use_GlobalAccel = 1`  ·  _SPLIT_  ·  Low
`src/globalhotkeys.cpp:29`
- **opus:** ✅ LEGIT (95) — #define Use_GlobalAccel = 1 malformed (globalhotkeys.cpp:29)
- **gpt:** ⚠️ PARTIAL (58) — macro value is malformed but current uses are #ifdef/defined only (src/globalhotkeys.cpp:29)
- **deepseek:** ✅ LEGIT (85) — #define Use_GlobalAccel = 1 at globalhotkeys.cpp:29 defines to = 1 not 1; currently only #ifdef tested so benign but any #if value check would fail

### [TYP-07] Narrowing conversion: `size_t` → `int` in SpellChecker::decode  ·  _SPLIT_  ·  Low
`src/spellchecker.cpp:411-412`
- **opus:** ✅ LEGIT (90) — size_t->int narrowing; trivial (spellchecker.cpp:411)
- **gpt:** ⚠️ PARTIAL (58) — observed Narrowing conversion: size_t -> int in SpellChecker::decode (src/spellchecker.cpp:411)
- **deepseek:** ⚠️ PARTIAL (30) — Narrowing size_t->int at spellchecker.cpp:411; max word length < INT_MAX in practice — correctness nit zero practical impact

### [TYP-09] Null pointer dereferences in emit textChanged related to uninitialized m_document  ·  _SPLIT_  ·  Low
`src/documenthandler.cpp:320,325,334,343,383 (related)`
- **opus:** ❌ FALSE (90) — cited lines are #ifdef; textChanged never emitted anywhere
- **gpt:** ❌ FALSE (76) — cited setters emit member signals; m_document is not dereferenced there (src/documenthandler.cpp:320)
- **deepseek:** ⚠️ PARTIAL (40) — Various emit textChanged() paths depend on document() non-null at doc.cpp:320-383; but gated by m_document checks in callers — fragile but currently guarded

### [TYP-N03] Inconsistent `_` vs `m_` member prefix: _markersModel, _fileSystemWatcher  ·  _SPLIT_  ·  Low
`documenthandler.h:343-344`
- **opus:** ⚠️ PARTIAL (35) — _ vs m_ member prefix inconsistency; cosmetic (documenthandler.h:343)
- **gpt:** ⚠️ PARTIAL (58) — observed Inconsistent vs m member prefix: markersModel, _fileSystemWatcher (src/documenthandler.h:343)
- **deepseek:** ✅ LEGIT (80) — _markersModel and _fileSystemWatcher use _ prefix vs m_ for other members (documenthandler.h:343-344)

### [TYP-N04] Inconsistent m_ method naming: m_initializeSource — mixed underscore+camelCase  ·  _SPLIT_  ·  Low
`abstractinputsource.h:50, globalhotkeys.h:150`
- **opus:** ⚠️ PARTIAL (35) — m_ method naming inconsistency; cosmetic (abstractinputsource.h:50)
- **gpt:** ⚠️ PARTIAL (58) — observed Inconsistent m method naming: minitializeSource - mixed underscore+camelCase (src/abstractinputsource.h:50)
- **deepseek:** ✅ LEGIT (75) — m_initializeSource uses m_ member prefix on a method not member (abstractinputsource.h:50)

### [TYP-N06] 9 getters copy-paste double-textCursor() pattern — null check on stale cursor  ·  _SPLIT_  ·  Low
`documenthandler.cpp: alignment(548), bold(565), italic(581), underline(597), strike(613), subscript(629), superscript(648), fontCapitalization(669), regularMarker(694)`
- **opus:** ⚠️ PARTIAL (50) — 9 getters share the double-textCursor() pattern (LOG-07 family)
- **gpt:** ⚠️ PARTIAL (58) — observed 9 getters copy-paste double-textCursor() pattern - null check on stale cursor (src/documenthandler.cpp:1)
- **deepseek:** ✅ LEGIT (65) — alignment() null-checks first textCursor() but reads second stale textCursor() (documenthandler.cpp:548-550)

### [UNIT-01] ProgressIndicator.qml:46 Units.ShortDuration with no Kirigami import  ·  _SPLIT_  ·  High
`ProgressIndicator.qml:46`
- **opus:** ⚠️ PARTIAL (55) — Units.ShortDuration broken via R3-CTX-01, 'no Kirigami import' misdiagnoses cause (ProgressIndicator.qml:46)
- **gpt:** ✅ LEGIT (84) — ProgressIndicator.qml:46 Units.ShortDuration with no Kirigami import (src/prompter/ProgressIndicator.qml:46)
- **deepseek:** ✅ LEGIT (95) — Units.ShortDuration at ProgressIndicator.qml:46 — no Kirigami import Units undefined

### [UNIT-02] PrompterView.qml 7x Units.ShortDuration with no Kirigami import  ·  _SPLIT_  ·  High
`PrompterView.qml:80,87,103,132,139,155,185`
- **opus:** ⚠️ PARTIAL (55) — Units.ShortDuration broken via R3-CTX-01, but 'no Kirigami import' misdiagnoses cause (PrompterView.qml:80)
- **gpt:** ✅ LEGIT (84) — PrompterView.qml 7x Units.ShortDuration with no Kirigami import (src/prompter/PrompterView.qml:80)
- **deepseek:** ✅ LEGIT (95) — 7x Units.ShortDuration in PrompterView.qml — no Kirigami import at all

### [UNIT-03] PrompterBackground.qml:160 Units.LongDuration no Kirigami import  ·  _SPLIT_  ·  Medium
`PrompterBackground.qml:160`
- **opus:** ⚠️ PARTIAL (50) — Units.LongDuration broken via R3-CTX-01 (PrompterBackground.qml:160)
- **gpt:** ✅ LEGIT (78) — PrompterBackground.qml:160 Units.LongDuration no Kirigami import (src/prompter/PrompterBackground.qml:160)
- **deepseek:** ✅ LEGIT (95) — Units.LongDuration at PrompterBackground.qml:160 — no Kirigami import

### [UNIT-04] Flip.qml:34,41 two Units.LongDuration no Kirigami import  ·  _SPLIT_  ·  Medium
`Flip.qml:34,41`
- **opus:** ⚠️ PARTIAL (50) — Units.LongDuration broken via R3-CTX-01 (Flip.qml:34)
- **gpt:** ✅ LEGIT (78) — Flip.qml:34,41 two Units.LongDuration no Kirigami import (src/prompter/Flip.qml:34)
- **deepseek:** ✅ LEGIT (95) — 2x Units.LongDuration at Flip.qml — no Kirigami import (only QtQuick+com.cuperino)

### [UNIT-05] pointer_0.qml:72 Units.VeryLongDuration no Kirigami import  ·  _SPLIT_  ·  Low
`pointer_0.qml:72`
- **opus:** ⚠️ PARTIAL (50) — Units.VeryLongDuration broken via R3-CTX-01 (pointer_0.qml:72)
- **gpt:** ✅ LEGIT (78) — pointer_0.qml:72 Units.VeryLongDuration no Kirigami import (src/prompter/pointers/pointer_0.qml:72)
- **deepseek:** ✅ LEGIT (95) — Units.VeryLongDuration at pointer_0.qml:72 — no Kirigami import

### [UNIT-06] Find.qml:92 Units.ShortDuration with namespaced Kirigami import  ·  _SPLIT_  ·  Medium
`Find.qml:92`
- **opus:** ⚠️ PARTIAL (50) — Units.ShortDuration broken via R3-CTX-01 (Find.qml:92)
- **gpt:** ✅ LEGIT (78) — Find.qml:92 Units.ShortDuration with namespaced Kirigami import (src/prompter/Find.qml:92)
- **deepseek:** ✅ LEGIT (95) — Units.ShortDuration at Find.qml:92 — imported as Kirigami should be Kirigami.Units

### [UNIT-07] ReadRegionOverlay.qml 3x Units.ShortDuration with namespaced import  ·  _SPLIT_  ·  Medium
`ReadRegionOverlay.qml:546,610,616`
- **opus:** ⚠️ PARTIAL (50) — Units.ShortDuration broken via R3-CTX-01 (ReadRegionOverlay.qml:546)
- **gpt:** ✅ LEGIT (78) — ReadRegionOverlay.qml 3x Units.ShortDuration with namespaced import (src/prompter/ReadRegionOverlay.qml:546)
- **deepseek:** ✅ LEGIT (90) — 3x Units.ShortDuration at ReadRegionOverlay.qml:546 610 616 — NO Kirigami import at all (bug said namespaced)

### [URL-N01] reload() constructs file:// URL by string concatenation without encoding  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:860`
- **opus:** ✅ LEGIT (60) — reload file:// URL by concat without encoding (dup PATH-N02) (documenthandler.cpp:860)
- **gpt:** ⚠️ PARTIAL (58) — observed reload() constructs file:// URL by string concatenation without encoding (src/documenthandler.cpp:860)
- **deepseek:** ✅ LEGIT (65) — file:// URL built by string concatenation without percent-encoding (documenthandler.cpp:860)

### [URL-N03] Network-loaded HTML lacks base URL — relative resources broken  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:888-901`
- **opus:** ✅ LEGIT (55) — network HTML lacks base URL; relative resources break (documenthandler.cpp:888)
- **gpt:** ⚠️ PARTIAL (58) — observed Network-loaded HTML lacks base URL - relative resources broken (src/documenthandler.cpp:888)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:888-901: loadFromNetworkFinihed never calls doc->setBaseUrl(); original network URL discarded — relative resources (images/stylesheets) in HTML cannot resolve

### [URL-N04] loadFromNetwork() validates wrong URL instance  ·  _SPLIT_  ·  Low
`documenthandler.cpp:881`
- **opus:** ✅ LEGIT (60) — validates wrong URL instance (dup NET-N06) (documenthandler.cpp:881)
- **gpt:** ⚠️ PARTIAL (58) — observed loadFromNetwork() validates wrong URL instance (src/documenthandler.cpp:881)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:881: url.isValid() validates original url not constructed resultingUrl; valid relative URL can produce invalid resultingUrl that passes unchecked

### [URL-N05] openFromRemote() blindly prepends http:// to non-HTTP schemes  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:1279-1282`
- **opus:** ✅ LEGIT (55) — openFromRemote blindly prepends http:// to non-HTTP schemes (PrompterPage.qml:1279)
- **gpt:** ⚠️ PARTIAL (58) — observed openFromRemote() blindly prepends http:// to non-HTTP schemes (src/kirigami_ui/PrompterPage.qml:1279)
- **deepseek:** ✅ LEGIT (90) — PrompterPage.qml:1279-1282: any URL not starting http:// or https:// gets http:// prepended; file:// becomes http://file:// case variants like HTTP:// missed

### [UTF-N01] text.truncate(64) can split UTF-16 surrogate pairs — corrupted display  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:736`
- **opus:** ⚠️ PARTIAL (50) — truncate(64) can split a UTF-16 surrogate pair; rare (documenthandler.cpp:736)
- **gpt:** ✅ LEGIT (78) — text.truncate(64) can split UTF-16 surrogate pairs - corrupted display (src/documenthandler.cpp:736)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:736: text.truncate(64) cuts at UTF-16 code unit 64; supplementary-plane chars (emoji rare CJK) straddling boundary -> orphaned high surrogate — corrupted preview

### [VCI-N01] At-end action buttons use inconsistent font scaling (1/1.5 vs 1/1.75) in same group  ·  _SPLIT_  ·  Low
`Prompter.qml:1158,1185,1212 vs 1256,1269,1309`
- **opus:** ⚠️ PARTIAL (40) — at-end buttons inconsistent font scaling (Prompter.qml:1158)
- **gpt:** ⚠️ PARTIAL (48) — visual issue is plausible but depends on theme or device (src/prompter/Prompter.qml:1158)
- **deepseek:** ✅ LEGIT (95) — Prompter.qml:1158/1185/1212 vs 1256/1269/1309: Stop/Exit/Loop buttons scale font /1.5 while adjacent Flipable/SpinBox scale /1.75 — visible 16.7% size mismatch

### [VCI-N02] upperControls and bottomControls fade to different opacity levels during Prompting  ·  _SPLIT_  ·  Low
`PrompterView.qml:70 vs 120`
- **opus:** ⚠️ PARTIAL (40) — upper/bottom controls fade to different opacity (PrompterView.qml:70)
- **gpt:** ⚠️ PARTIAL (48) — visual issue is plausible but depends on theme or device (src/prompter/PrompterView.qml:70)
- **deepseek:** ✅ LEGIT (95) — PrompterView.qml:70 vs 120: upperControls fades to 0.1 during Prompting; bottomControls to 0.2 — top controls nearly invisible while bottom twice as visible

### [VER-01] Qt::MarkdownText version guard 0x050F00 (5.15) — API added in 5.14  ·  _SPLIT_  ·  Low
`documenthandler.cpp:958`
- **opus:** ⚠️ PARTIAL (45) — MarkdownText guard 0x050F00; insertMarkdown was 5.14 but target is Qt6 (documenthandler.cpp:958)
- **gpt:** ✅ LEGIT (78) — Qt::MarkdownText version guard 0x050F00 (5.15) - API added in 5.14 (src/documenthandler.cpp:958)
- **deepseek:** ✅ LEGIT (85) — guard 0x050F00(Qt5.15) but MarkdownText added in Qt5.14; 5.14 users get plain text (documenthandler.cpp:958)

### [VIS-FB-N01] bookmarkListButton and searchButton missing checkable: true — no checked background  ·  _SPLIT_  ·  Low
`EditorToolbar.qml:188,202`
- **opus:** ⚠️ PARTIAL (50) — bookmarkListButton/searchButton missing checkable:true (EditorToolbar.qml:188)
- **gpt:** ⚠️ PARTIAL (58) — observed bookmarkListButton and searchButton missing checkable: true - no checked background (src/kirigami_ui/EditorToolbar.qml:188)
- **deepseek:** ✅ LEGIT (90) — EditorToolbar.qml:188 202: bookmarkListButton.searchButton declare checked binding but omit checkable:true; no Material checked background

### [VIS-N05] velocityDragOverlay blocks all interaction during indicator fade-out (~500ms dead zone)  ·  _SPLIT_  ·  Medium
`PrompterPage.qml:913-919,865-872`
- **opus:** ⚠️ PARTIAL (50) — velocityDragOverlay blocks interaction during ~500ms fade (PrompterPage.qml:913)
- **gpt:** ⚠️ PARTIAL (58) — observed velocityDragOverlay blocks all interaction during indicator fade-out (~500ms dead zone) (src/kirigami_ui/PrompterPage.qml:913)
- **deepseek:** ✅ LEGIT (65) — velocityDragOverlay stays visible during fade animation blocking input for Units.LongDuration (PrompterPage.qml:913-919)

### [W10-CLP-01] Paste-without-formatting fails when clipboard lacks text/plain  ·  _SPLIT_  ·  High
`src/documenthandler.cpp:1346-1348`
- **opus:** ⚠️ PARTIAL (55) — paste-without-formatting uses mimeData->text(); empty if no text/plain (documenthandler.cpp:1346)
- **gpt:** ⚠️ PARTIAL (58) — observed Paste-without-formatting fails when clipboard lacks text/plain (src/documenthandler.cpp:1346)
- **deepseek:** ❌ FALSE (80) — QMimeData::text() auto-extracts plain text from HTML when text/plain missing; returns content not empty (documenthandler.cpp:1346-1348)

### [W10-CLP-02] Remote image URLs in pasted HTML cause unsanctioned network requests  ·  _SPLIT_  ·  Medium
`src/documenthandler.cpp:1246-1334, 1425-1455`
- **opus:** ⚠️ PARTIAL (50) — pasted remote img URLs can trigger network fetch via richtext engine (documenthandler.cpp:1246)
- **gpt:** ⚠️ PARTIAL (58) — observed Remote image URLs in pasted HTML cause unsanctioned network requests (src/documenthandler.cpp:1246)
- **deepseek:** ✅ LEGIT (90) — filterHtml never strips img remote src; insertHtmlAt downloads via image.load(src) leaking user IP (documenthandler.cpp:1449-1451)

### [W10-PLF-02] QHotkey_FOUND never set in FetchContent path — built but never linked  ·  _SPLIT_  ·  High
`CMakeLists.txt:252-258, src/CMakeLists.txt:495-500`
- **opus:** ⚠️ PARTIAL (50) — FetchContent may not set QHotkey_FOUND; unconfirmed whether set manually (CMakeLists.txt:252)
- **gpt:** ⚠️ PARTIAL (58) — observed QHotkeyFOUND never set in FetchContent path - built but never linked (CMakeLists.txt:252)
- **deepseek:** ✅ LEGIT (95) — FetchContent_MakeAvailable doesn't set QHotkey_FOUND; add_def+target_link_libraries gated library never linked (CMakeLists.txt:252 src/CMakeLists.txt:495-500)

### [W10-PMV-02] Circular ShaderEffectSource dependency — shadow ghost on first frame  ·  _SPLIT_  ·  Medium
`src/prompter/PrompterView.qml:230-233, Prompter.qml:744-770`
- **opus:** ⚠️ PARTIAL (50) — circular ShaderEffectSource; shadow ghost first frame (PrompterView.qml:230)
- **gpt:** ⚠️ PARTIAL (58) — observed Circular ShaderEffectSource dependency - shadow ghost on first frame (src/prompter/PrompterView.qml:230)
- **deepseek:** ✅ LEGIT (80) — ShaderEffectSource captures prompter with layer applied feeds back as shadow texture one-frame ghost (PrompterView.qml:230-233)

### [W10-SWT-01] CloseActions switch drops RecentLocal/RecentRemote — recent document open silently lost after save  ·  _SPLIT_  ·  High
`src/prompter/Prompter.qml:2479`
- **opus:** ⚠️ PARTIAL (55) — CloseActions switch omits RecentLocal/RecentRemote cases (Prompter.qml:2479)
- **gpt:** ⚠️ PARTIAL (58) — observed CloseActions switch drops RecentLocal/RecentRemote - recent document open silently lost after s (src/prompter/Prompter.qml:2479)
- **deepseek:** ✅ LEGIT (90) — switch misses RecentLocal/RecentRemote; recent document intent silently lost after save (Prompter.qml:2479-2486)

### [W10-SWT-02] Same bug in IosSaveDialog.onAccepted path  ·  _SPLIT_  ·  High
`src/prompter/Prompter.qml:2500`
- **opus:** ⚠️ PARTIAL (55) — same omission in IosSaveDialog.onAccepted (Prompter.qml:2500)
- **gpt:** ⚠️ PARTIAL (58) — observed Same bug in IosSaveDialog.onAccepted path (src/prompter/Prompter.qml:2500)
- **deepseek:** ✅ LEGIT (90) — same omission in IosSaveDialog.onAccepted switch; identical bug on iOS (Prompter.qml:2500-2506)

### [W10-WSM-01] Infinite reload loop on unauthorized WASM host — app unusable  ·  _SPLIT_  ·  Critical
`src/prompter/Prompter.qml:439, src/wasmintegration.cpp:189-194`
- **opus:** ⚠️ PARTIAL (55) — officialHost()->quit()->reload real, but called in toggle() not startup; 'infinite' overstated (Prompter.qml:439)
- **gpt:** ⚠️ PARTIAL (58) — observed Infinite reload loop on unauthorized WASM host - app unusable (src/prompter/Prompter.qml:439)
- **deepseek:** ✅ LEGIT (88) — toggle->officialHost->quit->aboutToQuit->location.reload->same unauthorized host; inescapable loop (wasmintegration.cpp:189-194)

### [W10-WSM-02] Global file-picker state overwritten by re-entrant calls — wrong file delivered  ·  _SPLIT_  ·  Medium
`src/wasmintegration.cpp:37-40, 64-88, 164-171`
- **opus:** ⚠️ PARTIAL (50) — global picker state overwritten by re-entrant calls (wasmintegration.cpp:37)
- **gpt:** ⚠️ PARTIAL (58) — observed Global file-picker state overwritten by re-entrant calls - wrong file delivered (src/wasmintegration.cpp:37)
- **deepseek:** ✅ LEGIT (88) — static s_pending* globals no re-entrancy guard; second call overwrites first delivers to wrong target (wasmintegration.cpp:37-40)

### [WARN-N01] SpellHighlighter::isEnabled() — dead code, never called  ·  _SPLIT_  ·  Low
`spellhighlighter.h:36`
- **opus:** ⚠️ PARTIAL (40) — SpellHighlighter::isEnabled dead, never called (spellhighlighter.h:36)
- **gpt:** ⚠️ PARTIAL (58) — observed SpellHighlighter::isEnabled() - dead code, never called (src/spellhighlighter.h:36)
- **deepseek:** ✅ LEGIT (80) — spellhighlighter.h:36: isEnabled() public method never called anywhere in codebase; setEnabled() is called but isEnabled() is dead code

### [WARN-N02] SpellChecker::addWord() — dead public API, never called  ·  _SPLIT_  ·  Low
`spellchecker.h:48, spellchecker.cpp:134-140`
- **opus:** ✅ LEGIT (60) — addWord() is dead public API never called (spellchecker.h:48)
- **gpt:** ⚠️ PARTIAL (58) — observed SpellChecker::addWord() - dead public API, never called (src/spellchecker.h:48)
- **deepseek:** ✅ LEGIT (85) — spellchecker.h:48 / spellchecker.cpp:134-140: addWord() full implementation exists but never invoked; DocumentHandler uses addCustomWord() instead — dead public API

### [WARN-N03] quint64→int implicit narrowing in nextMarker()/previousMarker()  ·  _SPLIT_  ·  Low
`documenthandler.cpp:1713,1721`
- **opus:** ⚠️ PARTIAL (45) — quint64->int narrowing (dup INT-N01) (documenthandler.cpp:1713)
- **gpt:** ⚠️ PARTIAL (58) — observed quint64->int implicit narrowing in nextMarker()/previousMarker() (src/documenthandler.cpp:1713)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:1713/1721: Q_INVOKABLE takes quint64 position but MarkersModel::nextMarker/previousMarker accept int (markersmodel.h:62-63); 64->32 bit unsigned->signed truncation

### [WARN-N04] QProcess::startDetached() bool return silently ignored  ·  _SPLIT_  ·  Low
`qmlutil.hpp:91`
- **opus:** ✅ LEGIT (55) — startDetached bool return ignored (qmlutil.hpp:91)
- **gpt:** ⚠️ PARTIAL (58) — observed QProcess::startDetached() bool return silently ignored (src/qmlutil.hpp:91)
- **deepseek:** ✅ LEGIT (95) — qmlutil.hpp:91: QProcess::startDetached() returns bool — discarded; if program not found failure is silent with no error log or QML notification

### [WATCH-N01] addPath() return never checked — silent watch failure  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1026`
- **opus:** ⚠️ PARTIAL (50) — addPath() return value unchecked (documenthandler.cpp:1026)
- **gpt:** ✅ LEGIT (78) — addPath() return never checked - silent watch failure (src/documenthandler.cpp:1026)
- **deepseek:** ✅ LEGIT (95) — documenthandler.cpp:1026: addPath() bool return discarded; silent failure on unsupported filesystems

### [WATCH-N02] removePath() return never checked — stale path causes double-watch  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:1024`
- **opus:** ⚠️ PARTIAL (50) — removePath() return value unchecked (documenthandler.cpp:1024)
- **gpt:** ✅ LEGIT (78) — removePath() return never checked - stale path causes double-watch (src/documenthandler.cpp:1024)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:1024: removePath() return unchecked; stale path stays watched causing double-watch on fileChanged

### [WATCH-N03] Watcher not refreshed after fileChanged — stale inotify on Linux atomic saves  ·  _SPLIT_  ·  Medium
`documenthandler.cpp:857-864,1020-1027`
- **opus:** ❔ UNSURE (45) — watcher stale after atomic-save inotify swap; Linux-specific (documenthandler.cpp:857)
- **gpt:** ✅ LEGIT (78) — Watcher not refreshed after fileChanged - stale inotify on Linux atomic saves (src/documenthandler.cpp:857)
- **deepseek:** ✅ LEGIT (90) — documenthandler.cpp:857-864: reload() loads document but watcher not re-added after fileChanged; next atomic save undetected

### [WATCH-N04] unblockFileWatcher() dereferences _fileSystemWatcher without null guard  ·  _SPLIT_  ·  Low
`documenthandler.cpp:1125-1128`
- **opus:** ⚠️ PARTIAL (45) — _fileSystemWatcher always constructed in ctor; null-deref unlikely (documenthandler.cpp:1125)
- **gpt:** ✅ LEGIT (78) — unblockFileWatcher() dereferences _fileSystemWatcher without null guard (src/documenthandler.cpp:1125)
- **deepseek:** ✅ LEGIT (85) — documenthandler.cpp:1125-1128: _fileSystemWatcher dereferenced without null guard; reachable via QTimer::singleShot from saveAs()

### [WINDOW-N01] Projection windows not closed on main window close — orphaned on Linux  ·  _SPLIT_  ·  Medium
`main.qml:159-165, +windows:154-160, +android:144-150`
- **opus:** ⚠️ PARTIAL (50) — projection windows may orphan on main-window close; lifecycle (main.qml:159)
- **gpt:** ⚠️ PARTIAL (58) — observed Projection windows not closed on main window close - orphaned on Linux (src/kirigami_ui/main.qml:159)
- **deepseek:** ✅ LEGIT (85) — main.qml:159-165/+android:144-150/+windows:154-160: onClosing only handles save dialog; no projectionManager.closeAll() or isEnabled=false — orphaned projection windows on Linux

### [WSM-03] readAsDataURL causes quadruple in-memory copy of file content  ·  _SPLIT_  ·  High
`wasmintegration.cpp:129-144`
- **opus:** ⚠️ PARTIAL (50) — readAsDataURL -> base64+encode+malloc multiple copies; large-file memory (wasmintegration.cpp:129)
- **gpt:** ⚠️ PARTIAL (58) — observed readAsDataURL causes quadruple in-memory copy of file content (src/wasmintegration.cpp:129)
- **deepseek:** ✅ LEGIT (88) — readAsDataURL base64(+33%)->TextEncoder->malloc+HEAPU8->QString::fromUtf8; quadruple copy high memory (wasmintegration.cpp:129-144)

### [WYS-N02] Default stylesheet CSS errors: valign:top (not a CSS property) and border:1pt (missing style)  ·  _SPLIT_  ·  Low
`documenthandler.cpp:188`
- **opus:** ✅ LEGIT (70) — valign:top not a CSS prop; border:1pt malformed in default stylesheet (documenthandler.cpp:188)
- **gpt:** ⚠️ PARTIAL (58) — observed Default stylesheet CSS errors: valign:top (not a CSS property) and border:1pt (missing style) (src/documenthandler.cpp:188)
- **deepseek:** ✅ LEGIT (85) — documenthandler.cpp:188: valign:top not valid CSS (should be vertical-align:top); border:1pt missing style keyword (e.g. solid)

### [XFRM-N01] PrompterView.qml Rotation permanently overridden by PrompterPage.qml  ·  _SPLIT_  ·  Low
`PrompterView.qml:53-58 vs PrompterPage.qml:750-765`
- **opus:** ❔ UNSURE (45) — PrompterView Rotation overridden by PrompterPage; domain (PrompterView.qml:53)
- **gpt:** ❔ UNSURE (39) — runtime/platform behavior is not decidable from the cited snippet (src/prompter/PrompterView.qml:53)
- **deepseek:** ⚠️ PARTIAL (45) — Rotation overridden by PrompterPage is expected parent-child transform layering (PrompterView.qml:53-58)

### [Z-N01] CursorAutoHide has no explicit z — hover detection fragile against Kirigami internals  ·  _SPLIT_  ·  Medium
`main.qml:954, +windows/main.qml:618, +android/main.qml:562`
- **opus:** ⚠️ PARTIAL (45) — CursorAutoHide no explicit z; hover detection fragile (main.qml:954)
- **gpt:** ✅ LEGIT (78) — CursorAutoHide has no explicit z - hover detection fragile against Kirigami internals (src/kirigami_ui/main.qml:954)
- **deepseek:** ⚠️ PARTIAL (45) — no explicit z on CursorAutoHide; stacking fragile against Kirigami internals (main.qml:954)

### [Z-N02] Two OverlaySheets have z:1 while nine others have none — inconsistent stacking  ·  _SPLIT_  ·  Low
`LanguageSettingsOverlay.qml:36, LayoutDirectionSettingsOverlay.qml:36`
- **opus:** ⚠️ PARTIAL (40) — two OverlaySheets z:1 while others none; inconsistent (LanguageSettingsOverlay.qml:36)
- **gpt:** ✅ LEGIT (78) — Two OverlaySheets have z:1 while nine others have none - inconsistent stacking (src/kirigami_ui/LanguageSettingsOverlay.qml:36)
- **deepseek:** ⚠️ PARTIAL (40) — two OverlaySheets have z:1 while others have none; inconsistent but functional

### [Z-N03] ComboBox Popup z:103 inside OverlaySheets with z:1 — disconnected layering  ·  _SPLIT_  ·  Low
`LanguageSettingsOverlay.qml:67, LayoutDirectionSettingsOverlay.qml:70`
- **opus:** ⚠️ PARTIAL (40) — ComboBox Popup z:103 inside z:1 sheets (LanguageSettingsOverlay.qml:67)
- **gpt:** ✅ LEGIT (78) — ComboBox Popup z:103 inside OverlaySheets with z:1 - disconnected layering (src/kirigami_ui/LanguageSettingsOverlay.qml:67)
- **deepseek:** ⚠️ PARTIAL (40) — ComboBox popup z:103 inside z:1 sheet; popup has own stacking context

### [Z-N04] PrompterBackground (z:0) renders above viewport.mouse (z:0) — latent input intercept  ·  _SPLIT_  ·  Low
`PrompterView.qml:249,320`
- **opus:** ⚠️ PARTIAL (45) — PrompterBackground z:0 vs viewport.mouse z:0; order-dependent (PrompterView.qml:249)
- **gpt:** ✅ LEGIT (78) — PrompterBackground (z:0) renders above viewport.mouse (z:0) - latent input intercept (src/prompter/PrompterView.qml:249)
- **deepseek:** ✅ LEGIT (65) — PrompterBackground(z:0) declared after MouseArea(z:0) renders on top intercepting input (PrompterView.qml:249 320)

