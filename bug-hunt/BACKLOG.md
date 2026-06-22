# Bug-Hunt Backlog

Work queue: OPEN tickets the max-rigor reviewer (`opus-ultra`) confirms as LEGIT, ranked by severity then corroboration (number of the 6 agents that also called it LEGIT). Each row links to its full ticket in `findings/`.

Status tally: FIXED 1 · NEEDS-INFO 63 · OPEN 589 · REJECTED 70.

**495 actionable OPEN findings.**

| # | Sev | Corrob. | ID | Title |
|---|---|---|---|---|
| 1 | Critical | 6/6 | [CLIP-CRIT-01](findings/CLIP-CRIT-01.md) | Paste via toolbar button and File menu bypasses HTML sanitization |
| 2 | Critical | 6/6 | [CUR-N01](findings/CUR-N01.md) | replaceAll() infinite loop when replacement contains search pattern |
| 3 | Critical | 6/6 | [EDGE-04](findings/EDGE-04.md) | Null pointer dereference: `document()->textDocument()` not checked before `load()` |
| 4 | Critical | 6/6 | [EDGE-05](findings/EDGE-05.md) | Null pointer dereference: `textDocument()` unchecked in `search()` |
| 5 | Critical | 6/6 | [EDGE-06](findings/EDGE-06.md) | Null pointer dereference: `textDocument()` unchecked in `parse()` |
| 6 | Critical | 6/6 | [FINAL-01](findings/FINAL-01.md) | TimerClock references undefined `timer` id — ETA and stopwatch completely broken |
| 7 | Critical | 6/6 | [FINAL-03](findings/FINAL-03.md) | Missing breeze-icons submodule — fresh clone cannot build |
| 8 | Critical | 6/6 | [R3-CTX-01](findings/R3-CTX-01.md) | AbstractUnits missing QML_ELEMENT — all duration constants resolve to undefined |
| 9 | Critical | 6/6 | [R3-DOC-01](findings/R3-DOC-01.md) | m_reloading uninitialized — undefined behavior on first load |
| 10 | Critical | 6/6 | [R4-CMT-01](findings/R4-CMT-01.md) | PDF import completely broken — converter invocation commented out |
| 11 | Critical | 6/6 | [SEC-01](findings/SEC-01.md) | Arbitrary Command Execution via `sys://` Marker URIs |
| 12 | Critical | 6/6 | [STK-N01](findings/STK-N01.md) | Android projectionManager undefined — crash on "Performance tweaks" submenu |
| 13 | Critical | 6/6 | [W10-PLF-01](findings/W10-PLF-01.md) | BSD detection broken — FreeBSD enters wrong code paths |
| 14 | Critical | 5/6 | [AND-BLD-01](findings/AND-BLD-01.md) | Missing version.gradle — Gradle build fails |
| 15 | Critical | 5/6 | [QML-03](findings/QML-03.md) | Undefined `root` ID in WindowDragger.qml |
| 16 | Critical | 5/6 | [R2-AND-02](findings/R2-AND-02.md) | Android missing restartDialog crashes LanguageSettingsOverlay and LayoutDirectionSettingsOverlay |
| 17 | Critical | 5/6 | [W10-DEP-01](findings/W10-DEP-01.md) | Missing vcpkg.json manifest — vcpkg manifest mode installs nothing |
| 18 | Critical | 4/6 | [R2-AND-01](findings/R2-AND-01.md) | Android missing QmlUtil causes crash on factory reset and RecentDocuments |
| 19 | Critical | 4/6 | [R4-EXP-01](findings/R4-EXP-01.md) | No XSS sanitization — script tags, event handlers, javascript: URLs unfiltered |
| 20 | Critical | 4/6 | [W10-WSM-01](findings/W10-WSM-01.md) | Infinite reload loop on unauthorized WASM host — app unusable |
| 21 | High | 6/6 | [AND-HIGH-02](findings/AND-HIGH-02.md) | Android screen never sleeps after prompter use |
| 22 | High | 6/6 | [AND-HIGH-03](findings/AND-HIGH-03.md) | factoryReset() quits Android app without restarting |
| 23 | High | 6/6 | [CUR-N02](findings/CUR-N02.md) | search() regex path ignores loop parameter — unconditional wrap |
| 24 | High | 6/6 | [DEB-N01](findings/DEB-N01.md) | libvulkan-dev (dev package) listed as Debian runtime dependency |
| 25 | High | 6/6 | [DLG-N01](findings/DLG-N01.md) | document.modified=false set BEFORE saveAs() — failed save loses unsaved flag |
| 26 | High | 6/6 | [DLG-N02](findings/DLG-N02.md) | onError handler clears document.modified on save failure |
| 27 | High | 6/6 | [DLG-N06](findings/DLG-N06.md) | import() error strings passed as document content via updateContents() |
| 28 | High | 6/6 | [EDGE-01](findings/EDGE-01.md) | QString::arg() called on string with no placeholder — program name silently dropped |
| 29 | High | 6/6 | [EDGE-02](findings/EDGE-02.md) | Empty container `first()` dereference — crash on hotkey with no windows |
| 30 | High | 6/6 | [EDGE-03](findings/EDGE-03.md) | Empty container `last()` dereference in `extendLastMarker` |
| 31 | High | 6/6 | [FINAL-05](findings/FINAL-05.md) | WindowDragger mouse delta accumulation error — window moves farther than cursor |
| 32 | High | 6/6 | [FINAL-08](findings/FINAL-08.md) | setup.sh vcvarsall.bat executed from bash — MSVC env not propagated |
| 33 | High | 6/6 | [FINAL-11](findings/FINAL-11.md) | onFrameSwapped calls grabToImage every frame — severe performance hit |
| 34 | High | 6/6 | [IMG-N02](findings/IMG-N02.md) | insertHtmlAt() silent blocking HTTP load for img src URLs — UI freeze |
| 35 | High | 6/6 | [IO-N02](findings/IO-N02.md) | save() constructs QUrl without file:// scheme — broken on non-Windows |
| 36 | High | 6/6 | [JSN-01](findings/JSN-01.md) | i.d.authentication accessed without undefined guard |
| 37 | High | 6/6 | [JSON-N01](findings/JSON-N01.md) | OBS WebSocket Hello auth fields accessed without null guard — crash on auth-disabled |
| 38 | High | 6/6 | [LINK-N01](findings/LINK-N01.md) | Qt::Network not linked on iOS static build — unresolved symbols |
| 39 | High | 6/6 | [LINK-N02](findings/LINK-N02.md) | Qt::Network not linked on WASM static build — same as LINK-N01 |
| 40 | High | 6/6 | [LOG-01](findings/LOG-01.md) | SessionModel::rowCount returns m_data.size() for both valid and invalid parents |
| 41 | High | 6/6 | [LOG-02](findings/LOG-02.md) | Off-by-one: beginRemoveRows uses rowCount() instead of rowCount()-1 |
| 42 | High | 6/6 | [MATH-N01](findings/MATH-N01.md) | Division by zero in __timeToArival/__timeToEnd when speed=0 |
| 43 | High | 6/6 | [MEM-01](findings/MEM-01.md) | Memory Leak: `_markersModel` allocated without parent, never deleted |
| 44 | High | 6/6 | [MEM-02](findings/MEM-02.md) | Memory Leak: `_fileSystemWatcher` allocated without parent, never deleted |
| 45 | High | 6/6 | [NET-01](findings/NET-01.md) | loadFromNetworkFinihed never checks m_reply->error() |
| 46 | High | 6/6 | [PROP-N01](findings/PROP-N01.md) | on__FullScreenChanged handler casing mismatch — never fires |
| 47 | High | 6/6 | [QML-04](findings/QML-04.md) | Typo: `verticalCentertop` instead of `verticalCenter` |
| 48 | High | 6/6 | [QML-05](findings/QML-05.md) | `&&` should be `\|\|` in clear button enabled condition |
| 49 | High | 6/6 | [QML-06](findings/QML-06.md) | Bitwise OR (`\|`) instead of AND (`&`) in modifier key check |
| 50 | High | 6/6 | [QML-BND-01](findings/QML-BND-01.md) | countdownAnimation.running binding permanently broken after first iteration |
| 51 | High | 6/6 | [R2-WHE-01](findings/R2-WHE-01.md) | `focus: true` is JavaScript label, not assignment |
| 52 | High | 6/6 | [R3-CTX-02](findings/R3-CTX-02.md) | GlobalHotkeys.SkipForward enum value mismatch — trailing 's' missing |
| 53 | High | 6/6 | [R3-DOC-03](findings/R3-DOC-03.md) | load() sets m_fileUrl and emits fileUrlChanged even on failed load |
| 54 | High | 6/6 | [R3-DOC-04](findings/R3-DOC-04.md) | saveAs() silently ignores write/flush failures |
| 55 | High | 6/6 | [R3-DOC-05](findings/R3-DOC-05.md) | updateContents() produces two separate undo entries — undo destroys document |
| 56 | High | 6/6 | [R3-DOC-07](findings/R3-DOC-07.md) | Inverted selection state after failed search() |
| 57 | High | 6/6 | [R4-EXP-02](findings/R4-EXP-02.md) | insertHtmlAt() bypasses filterHtml() — unsanitized HTML from QML |
| 58 | High | 6/6 | [R4-EXP-03](findings/R4-EXP-03.md) | loadFromNetwork() destroys URL for relative URLs — host/path swapped |
| 59 | High | 6/6 | [R4-EXP-04](findings/R4-EXP-04.md) | AutoText inserts plain text as HTML — content corruption |
| 60 | High | 6/6 | [R4-ROOT-01](findings/R4-ROOT-01.md) | Qt.openUrlExternally called with translation context string instead of URL |
| 61 | High | 6/6 | [REGEX-CRIT-02](findings/REGEX-CRIT-02.md) | searchRegEx.setPattern() from user input — isValid() never called |
| 62 | High | 6/6 | [RES-01](findings/RES-01.md) | Network reply overwritten without aborting previous download |
| 63 | High | 6/6 | [RES-02](findings/RES-02.md) | loadFromNetworkFinihed ignores the QNetworkReply* signal parameter |
| 64 | High | 6/6 | [STR-N01](findings/STR-N01.md) | main.cpp:158 QLatin1String iterator-pair UB from two unrelated string literals |
| 65 | High | 6/6 | [W10-CNV2-01](findings/W10-CNV2-01.md) | Default stylesheet has invalid CSS color quoting — exported HTML broken in browsers |
| 66 | High | 6/6 | [W10-CNV2-02](findings/W10-CNV2-02.md) | No markdown export — round-trip silently destroys all formatting |
| 67 | High | 6/6 | [W10-HTK-02](findings/W10-HTK-02.md) | QHotkey::setShortcut return value silently ignored — no failure detection |
| 68 | High | 6/6 | [WSM-N01](findings/WSM-N01.md) | Synchronous QImage::load() from HTTP blocks WASM main thread |
| 69 | High | 5/6 | [LYR-N01](findings/LYR-N01.md) | InputsOverlay calls cursorAutoHide.restart() on open instead of reset() |
| 70 | High | 5/6 | [PLAT-03](findings/PLAT-03.md) | Wrong target name and wrong include path for KDMacTouchBar |
| 71 | High | 5/6 | [QP-N01](findings/QP-N01.md) | restartApplication() quits even when startDetached fails — app dies with no replacement |
| 72 | High | 5/6 | [R2-CMAKE-02](findings/R2-CMAKE-02.md) | cmake_minimum_required inside find module pollutes parent project policy settings |
| 73 | High | 5/6 | [R2-EDT-02](findings/R2-EDT-02.md) | wheelThrottleSettingsButton checked bound to completely unrelated document property |
| 74 | High | 5/6 | [R2-EDT-03](findings/R2-EDT-03.md) | Checkable ToolButtons break checked property bindings on first click — systematic |
| 75 | High | 5/6 | [R3-MAIN-06](findings/R3-MAIN-06.md) | Inconsistent Kirigami platform guards — missing WATCHOS and QNX |
| 76 | High | 5/6 | [R4-EVT-03](findings/R4-EVT-03.md) | CursorAutoHide null access on root.pageStack.currentItem during page transitions |
| 77 | High | 5/6 | [SAVE-N02](findings/SAVE-N02.md) | iOS save flow never updates C++ m_fileUrl — file URL perpetually stale |
| 78 | High | 5/6 | [SHADOW-N03](findings/SHADOW-N03.md) | id: stopwatch shadows property bool stopwatch — timersEnabled always true |
| 79 | High | 5/6 | [UNIT-01](findings/UNIT-01.md) | ProgressIndicator.qml:46 Units.ShortDuration with no Kirigami import |
| 80 | High | 5/6 | [UNIT-02](findings/UNIT-02.md) | PrompterView.qml 7x Units.ShortDuration with no Kirigami import |
| 81 | High | 4/6 | [AND-HIGH-01](findings/AND-HIGH-01.md) | Android back button doesn't dismiss overlays/drawers before close |
| 82 | High | 4/6 | [EVT-03](findings/EVT-03.md) | velocityDragOverlay (z:7) steals clicks from control buttons (z:6) |
| 83 | High | 4/6 | [EVT-04](findings/EVT-04.md) | Drag breaks editor.x declarative binding permanently |
| 84 | High | 4/6 | [EVT-05](findings/EVT-05.md) | Drag breaks positionHandler.x declarative binding permanently |
| 85 | High | 4/6 | [FINAL-06](findings/FINAL-06.md) | CMAKE_OSX_ARCHITECTURES contains literal quotes — universal binary broken |
| 86 | High | 4/6 | [HK-N01](findings/HK-N01.md) | Missing event.isAutoRepeat guard on main Keys.onPressed |
| 87 | High | 4/6 | [HTK-03](findings/HTK-03.md) | KGlobalAccel defaults silently zeroed on non-Wayland when QHotkey co-exists |
| 88 | High | 4/6 | [PLAT-01](findings/PLAT-01.md) | KF6Crash_FOUND never defined as C preprocessor macro — KCrash support dead code |
| 89 | High | 4/6 | [R2-IOS-01](findings/R2-IOS-01.md) | Method swizzling re-entry causes infinite recursion on second invocation |
| 90 | High | 4/6 | [R3-MAIN-02](findings/R3-MAIN-02.md) | Invalid locale string constructed for short language codes |
| 91 | High | 4/6 | [R3-PMT-01](findings/R3-PMT-01.md) | OBS WebSocket JSON.parse without try/catch — crash on malformed input |
| 92 | High | 4/6 | [R4-ROV-01](findings/R4-ROV-01.md) | Division by zero in __customPlacement when overlay full |
| 93 | High | 4/6 | [R4-ROV-02](findings/R4-ROV-02.md) | Drag permanently breaks y property binding on readRegion |
| 94 | High | 4/6 | [THM-SYS](findings/THM-SYS.md) | Complete theme deadlock — 50+ Material.theme: Dark hardcoded, theme toggle commented out |
| 95 | High | 4/6 | [TRF-N01](findings/TRF-N01.md) | rightWidthAdjustmentBar drag.maximumX formula broken — drag collapses to single point |
| 96 | High | 4/6 | [W10-PLF-02](findings/W10-PLF-02.md) | QHotkey_FOUND never set in FetchContent path — built but never linked |
| 97 | High | 4/6 | [W10-SWT-01](findings/W10-SWT-01.md) | CloseActions switch drops RecentLocal/RecentRemote — recent document open silently lost after save |
| 98 | High | 4/6 | [W10-SWT-02](findings/W10-SWT-02.md) | Same bug in IosSaveDialog.onAccepted path |
| 99 | High | 3/6 | [EVT-01](findings/EVT-01.md) | velocityDragArea (z:5) blocks viewport.mouse (z:0) wheel events |
| 100 | High | 3/6 | [FINAL-04](findings/FINAL-04.md) | NSIS start-menu shortcut icon name mismatches actual binary name |
| 101 | High | 3/6 | [HK-N03](findings/HK-N03.md) | platformName() != "wayland" fails on "wayland-egl" — global hotkeys dead |
| 102 | High | 3/6 | [W10-CLP-01](findings/W10-CLP-01.md) | Paste-without-formatting fails when clipboard lacks text/plain |
| 103 | High | 3/6 | [W10-CNV2-03](findings/W10-CNV2-03.md) | import() uses fromStdString on non-Windows — encoding corruption |
| 104 | High | 3/6 | [WSM-03](findings/WSM-03.md) | readAsDataURL causes quadruple in-memory copy of file content |
| 105 | High | 2/6 | [W10-PMV-01](findings/W10-PMV-01.md) | font.pixelSize evaluates to 0 before first layout pass — crash hazard |
| 106 | Medium | 6/6 | [AND-N08](findings/AND-N08.md) | Android saveAs() hardcodes isHtml=true — plain-text files saved with HTML markup |
| 107 | Medium | 6/6 | [ANM-N01](findings/ANM-N01.md) | Easing.EaseOut is not a valid Qt Quick easing type (2 instances) |
| 108 | Medium | 6/6 | [API-N02](findings/API-N02.md) | selectionIsLowerCase NOTIFY signal is wrong — fontCapitalizationChanged, never emitted for case changes |
| 109 | Medium | 6/6 | [BLD-05](findings/BLD-05.md) | .env.android references Qt 5.15.2 — project requires Qt 6.8.2+ |
| 110 | Medium | 6/6 | [CAST-N01](findings/CAST-N01.md) | setFontCapitalization static_cast with no range validation — reachable from QML |
| 111 | Medium | 6/6 | [CMAKE-N04](findings/CMAKE-N04.md) | Relative ../build path in install rules — out-of-tree build failure |
| 112 | Medium | 6/6 | [CMAKE-NEW-02](findings/CMAKE-NEW-02.md) | Duplicate install() of appdata.xml/desktop in root and src/CMakeLists.txt |
| 113 | Medium | 6/6 | [CMAKE-NEW-03](findings/CMAKE-NEW-03.md) | find_package(KF6Crash ... COMPONENTS) — COMPONENTS keyword with zero names |
| 114 | Medium | 6/6 | [CMAKE-NEW-04](findings/CMAKE-NEW-04.md) | execute_process uses CMAKE_PREFIX_PATH (list) as scalar — broken command |
| 115 | Medium | 6/6 | [CMB-N03](findings/CMB-N03.md) | LanguageSettingsOverlay ListView currentIndex always -1 — wrong indexOf() call |
| 116 | Medium | 6/6 | [COERC-N02](findings/COERC-N02.md) | Unvalidated string-to-number injects NaN into root.__opacity — all opacity dead |
| 117 | Medium | 6/6 | [COMP-N02](findings/COMP-N02.md) | Case-sensitive suffix check misses mixed-case extensions — silent format loss |
| 118 | Medium | 6/6 | [CUR-N03](findings/CUR-N03.md) | alignment() reads blockFormat on multi-block selection — returns wrong alignment |
| 119 | Medium | 6/6 | [DCL-N01](findings/DCL-N01.md) | filterHtml default parameter in .cpp but not in header — QML can't call with 1 arg |
| 120 | Medium | 6/6 | [DCL-N02](findings/DCL-N02.md) | setKeyMarker default parameter mismatch — same pattern |
| 121 | Medium | 6/6 | [DLG-N04](findings/DLG-N04.md) | load() silently fails with no notification when file missing or unreadable |
| 122 | Medium | 6/6 | [DLG-N05](findings/DLG-N05.md) | loadFromNetworkFinihed() silently ignores empty response |
| 123 | Medium | 6/6 | [DPR-N01](findings/DPR-N01.md) | Prompter.qml uses Screen.devicePixelRatio (global) instead of screen.devicePixelRatio (window) |
| 124 | Medium | 6/6 | [EDGE-09](findings/EDGE-09.md) | QFile::copy() return value silently ignored |
| 125 | Medium | 6/6 | [ENC-01](findings/ENC-01.md) | truncate(-1) when font preview text has no spaces |
| 126 | Medium | 6/6 | [ERR-N01](findings/ERR-N01.md) | removeCustomWord() silently drops dictionary languages on partial reload failure |
| 127 | Medium | 6/6 | [EVT-07](findings/EVT-07.md) | TabBar currentIndex binding broken on first TabButton click |
| 128 | Medium | 6/6 | [EVT-08](findings/EVT-08.md) | Two additional checkable ToolButton binding breakage instances |
| 129 | Medium | 6/6 | [FINAL-12](findings/FINAL-12.md) | SystemFontChooserDialog setWindowFlags strips all decorations |
| 130 | Medium | 6/6 | [FINAL-13](findings/FINAL-13.md) | Invalid Korean locale code "ko_KO" — should be "ko_KR" |
| 131 | Medium | 6/6 | [FINAL-17](findings/FINAL-17.md) | ScriptAction references non-existent function `paintReady` |
| 132 | Medium | 6/6 | [FINAL-18](findings/FINAL-18.md) | MarkersModel extendLastMarker modifies data without emitting dataChanged |
| 133 | Medium | 6/6 | [FINAL-21](findings/FINAL-21.md) | clearProperty(AnchorHref/AnchorName) ineffective through mergeCharFormat |
| 134 | Medium | 6/6 | [FLOW-N01](findings/FLOW-N01.md) | setKeyMarker() calls setAnchor("#") — const char*→bool conversion, href never set |
| 135 | Medium | 6/6 | [FMT-N01](findings/FMT-N01.md) | Step Speed onAccepted displays 100x correct value |
| 136 | Medium | 6/6 | [FMT-N02](findings/FMT-N02.md) | Step Acceleration onAccepted — identical 100x display bug |
| 137 | Medium | 6/6 | [HK-N02](findings/HK-N02.md) | Typo Qt.Key_VolumeDowm — "Dowm" instead of "Down" — volume-down hardware key dead |
| 138 | Medium | 6/6 | [HK-N05](findings/HK-N05.md) | Strict === equality on modifiers breaks user keybinds with NumLock |
| 139 | Medium | 6/6 | [HTK-04](findings/HTK-04.md) | Wrong enum type `Qt::KeyboardModifier` (singular) for modifier variable |
| 140 | Medium | 6/6 | [INIT-N01](findings/INIT-N01.md) | Velocity modifier ComboBox model has 2 entries, switch handles 4 cases |
| 141 | Medium | 6/6 | [IO-N03](findings/IO-N03.md) | iossavedialog.mm QFile::write() return value unchecked |
| 142 | Medium | 6/6 | [LOG-03](findings/LOG-03.md) | MarkersModel::data returns data.position for LengthRole instead of data.length |
| 143 | Medium | 6/6 | [LOG-05](findings/LOG-05.md) | DocumentHandler::search ignores `loop` parameter when `regEx` is true |
| 144 | Medium | 6/6 | [LOG-N06](findings/LOG-N06.md) | No error log when saveAs() write/flush fail — silent data loss |
| 145 | Medium | 6/6 | [MATH-N02](findings/MATH-N02.md) | Bitwise << on floating-point in TimerClock — precision loss |
| 146 | Medium | 6/6 | [MEM-03](findings/MEM-03.md) | Memory Leak: `m_fontDialog` allocated without parent, never deleted |
| 147 | Medium | 6/6 | [MIME-N02](findings/MIME-N02.md) | loadFromNetworkFinihed() ignores Content-Type header — all network content treated as HTML |
| 148 | Medium | 6/6 | [MIME-N03](findings/MIME-N03.md) | PDF/EPUB/MOBI/AZW MIME-detected but import is no-op — error text becomes content |
| 149 | Medium | 6/6 | [MOB-01](findings/MOB-01.md) | Android: projectionManager undefined — 3 unguarded reference sites |
| 150 | Medium | 6/6 | [MODEL-N01](findings/MODEL-N01.md) | MarkersModel::rowCount ignores parent.isValid() — returns full size for child probe |
| 151 | Medium | 6/6 | [NET-N04](findings/NET-N04.md) | No transfer timeout on any QNetworkRequest |
| 152 | Medium | 6/6 | [NET-N05](findings/NET-N05.md) | loadFromNetwork() hardcodes http:// scheme — never upgrades to HTTPS |
| 153 | Medium | 6/6 | [NOTIFY-01](findings/NOTIFY-01.md) | setAutoReload doesn't emit autoReloadChanged NOTIFY signal |
| 154 | Medium | 6/6 | [PARSE-N02](findings/PARSE-N02.md) | MarkersModel::keySearch() hits=1 limits search to first marker only |
| 155 | Medium | 6/6 | [PATH-N02](findings/PATH-N02.md) | reload() constructs file:// URL via raw string concat — #/? in filenames break URL |
| 156 | Medium | 6/6 | [PLAT-02](findings/PLAT-02.md) | REQUIRED_KF6_VERSION variable referenced but never defined |
| 157 | Medium | 6/6 | [PLAT-N04](findings/PLAT-N04.md) | "ipados" is not valid Qt.platform.os string — 18 dead guards across 5 files |
| 158 | Medium | 6/6 | [QML-BND-02](findings/QML-BND-02.md) | clock.__iteration binding broken by post-decrement in animation handler |
| 159 | Medium | 6/6 | [QP-N02](findings/QP-N02.md) | convert.waitForFinished() blocks GUI thread up to 30s during LibreOffice import |
| 160 | Medium | 6/6 | [QP-N03](findings/QP-N03.md) | convert.exitCode() never checked — LibreOffice error output becomes document content |
| 161 | Medium | 6/6 | [QTD-01](findings/QTD-01.md) | m_spellHighlighter not detached when setDocument(nullptr) |
| 162 | Medium | 6/6 | [R2-ANDMAN-01](findings/R2-ANDMAN-01.md) | Ungrantable system/signature permissions bloating manifest |
| 163 | Medium | 6/6 | [R2-CMAKE-04](findings/R2-CMAKE-04.md) | QML icon file(GLOB_RECURSE) missing CONFIGURE_DEPENDS causes stale icon sets |
| 164 | Medium | 6/6 | [R2-FONT-01](findings/R2-FONT-01.md) | RichText label renders unescaped plain text — HTML metacharacters break display |
| 165 | Medium | 6/6 | [R2-IOS-03](findings/R2-IOS-03.md) | UIApplication.keyWindow deprecated since iOS 13; breaks multi-window iPadOS |
| 166 | Medium | 6/6 | [R2-PTH-01](findings/R2-PTH-01.md) | FileDialog filter matches all files on Linux due to stray glob |
| 167 | Medium | 6/6 | [R2-PTH-02](findings/R2-PTH-02.md) | File path from file:// URL preserves percent-encoding |
| 168 | Medium | 6/6 | [R3-DOC-06](findings/R3-DOC-06.md) | reload() leaks m_reloading=true on URL mismatch |
| 169 | Medium | 6/6 | [R3-MAIN-03](findings/R3-MAIN-03.md) | System locale changed even when translation file fails to load |
| 170 | Medium | 6/6 | [R3-MAIN-07](findings/R3-MAIN-07.md) | XDG_CURRENT_DESKTOP unconditionally forced to "KDE" on all Linux |
| 171 | Medium | 6/6 | [R3-PMT-02](findings/R3-PMT-02.md) | OBS WebSocket no onError handler, no reconnection logic |
| 172 | Medium | 6/6 | [R3-SPL-04](findings/R3-SPL-04.md) | Corrupt cached dictionary file persists permanently after failed copy |
| 173 | Medium | 6/6 | [R4-EXP-05](findings/R4-EXP-05.md) | No encoding/charset detection — all imports assumed UTF-8 |
| 174 | Medium | 6/6 | [R4-EXP-06](findings/R4-EXP-06.md) | UTF-8 BOM not stripped — becomes phantom character at position 0 |
| 175 | Medium | 6/6 | [R4-EXP-07](findings/R4-EXP-07.md) | data: URI assumes base64 encoding without checking ;base64 token |
| 176 | Medium | 6/6 | [R4-EXP-08](findings/R4-EXP-08.md) | EPUB/MOBI/AZW import replaces document with error string |
| 177 | Medium | 6/6 | [R4-PRJ-03](findings/R4-PRJ-03.md) | setScreensModel() duplicates display entries on each toggle cycle |
| 178 | Medium | 6/6 | [R4-PRJ-04](findings/R4-PRJ-04.md) | Division by zero in projection image height |
| 179 | Medium | 6/6 | [R4-ROOT-02](findings/R4-ROOT-02.md) | Invalid QML color value "initial" |
| 180 | Medium | 6/6 | [R4-ROOT-04](findings/R4-ROOT-04.md) | Duplicate "&Open" menu item in native File menu |
| 181 | Medium | 6/6 | [REGEX-N02](findings/REGEX-N02.md) | regex_5 accidentally excludes 15+ HTML5 tags from background-color filtering |
| 182 | Medium | 6/6 | [REGEX-N06](findings/REGEX-N06.md) | imgSrcRegex captures wrong src when data-src follows real src |
| 183 | Medium | 6/6 | [SAVE-N03](findings/SAVE-N03.md) | saveAs() never updates _fileSystemWatcher — watches stale file after save-as |
| 184 | Medium | 6/6 | [SCR-N02](findings/SCR-N02.md) | Duplicate entries in displayModel on first toggle — no clear() before setScreensModel() |
| 185 | Medium | 6/6 | [SEC-02](findings/SEC-02.md) | OBS WebSocket Password Stored in Plaintext |
| 186 | Medium | 6/6 | [SEC-03](findings/SEC-03.md) | Information Disclosure: Full HTML Document Content Logged via qDebug |
| 187 | Medium | 6/6 | [SHAPE-N01](findings/SHAPE-N01.md) | pointer_0.qml PathLine parent.width resolves to undefined (ShapePath has no width) — arrow collapsed |
| 188 | Medium | 6/6 | [SHDR-N01](findings/SHDR-N01.md) | Math.cos/Math.sin used with degrees value — shadow offset diagonal instead of horizontal |
| 189 | Medium | 6/6 | [SIZE-N01](findings/SIZE-N01.md) | concentricCircles Shape has conflicting anchors.fill + anchors.centerIn |
| 190 | Medium | 6/6 | [SPL2-11](findings/SPL2-11.md) | addCustomWord trims but removeCustomWord does not — asymmetry |
| 191 | Medium | 6/6 | [SPL2-12](findings/SPL2-12.md) | Case-sensitive contains/indexOf but case-insensitive sort — duplicates |
| 192 | Medium | 6/6 | [SPL2-13](findings/SPL2-13.md) | saveCustomWordsToDisk has void return — callers cannot detect I/O failure |
| 193 | Medium | 6/6 | [SPL2-14](findings/SPL2-14.md) | Cached QRC dicts never invalidated after app update |
| 194 | Medium | 6/6 | [SPL2-15](findings/SPL2-15.md) | spell() returns true when no dicts loaded — silent no-op |
| 195 | Medium | 6/6 | [SWT-N01](findings/SWT-N01.md) | OBS WebSocket Switch checked binding broken on first toggle |
| 196 | Medium | 6/6 | [TRL-N02](findings/TRL-N02.md) | Application --help description not translatable |
| 197 | Medium | 6/6 | [TXT-N03](findings/TXT-N03.md) | Toolbar paste and Edit menu paste bypass HTML sanitization |
| 198 | Medium | 6/6 | [WYS-N01](findings/WYS-N01.md) | Internal drag-and-drop copy inserts HTML as plain text — tags become visible |
| 199 | Medium | 6/6 | [XML-N01](findings/XML-N01.md) | android:background="#303030" invalid on \<activity\> — silently ignored |
| 200 | Medium | 5/6 | [ACT-N07](findings/ACT-N07.md) | namedBookmarkButton: checkable button opens dialog — stale indicator after first click |
| 201 | Medium | 5/6 | [API-N01](findings/API-N01.md) | setAlignment() missing null-cursor guard — crash risk with no document |
| 202 | Medium | 5/6 | [API-N03](findings/API-N03.md) | CursorAutoHide.qml unconditionally dereferences pageStack.currentItem.prompter |
| 203 | Medium | 5/6 | [BLK-N02](findings/BLK-N02.md) | updateContents() fails to reset block formatting — stale formats contaminate new document |
| 204 | Medium | 5/6 | [BLK-N03](findings/BLK-N03.md) | setLineHeight/setParagraphHeight apply document-wide — destroy per-block customization |
| 205 | Medium | 5/6 | [CLIP-N04](findings/CLIP-N04.md) | Image-only clipboard paste — button enabled but does nothing |
| 206 | Medium | 5/6 | [CMT-N08](findings/CMT-N08.md) | Entire Telemetry class is dead commented-out shell across 4 files |
| 207 | Medium | 5/6 | [DBG-N01](findings/DBG-N01.md) | OBS WebSocket auth challenge+salt logged to console in release builds |
| 208 | Medium | 5/6 | [DLG-N10](findings/DLG-N10.md) | TimerClock ColorDialog selectedColor never initialized from persisted settings |
| 209 | Medium | 5/6 | [DPI-04](findings/DPI-04.md) | InputsOverlay.qml:33 height:680 hardcoded |
| 210 | Medium | 5/6 | [DSZ-01](findings/DSZ-01.md) | InputsOverlay hardcoded height:680 — overflows on phones |
| 211 | Medium | 5/6 | [DSZ-02](findings/DSZ-02.md) | pointerConfiguration OverlaySheet no vertical ScrollView |
| 212 | Medium | 5/6 | [ENUM-01](findings/ENUM-01.md) | documenthandler.cpp:1108 updateContents switch no default — silent data loss |
| 213 | Medium | 5/6 | [FINAL-09](findings/FINAL-09.md) | `on__IChanged` handler typo — never fires |
| 214 | Medium | 5/6 | [FINAL-19](findings/FINAL-19.md) | Encoding fallback uses toLocal8Bit() instead of dictionary's actual encoding |
| 215 | Medium | 5/6 | [INT-N04](findings/INT-N04.md) | OBS URL/Password fields disabled when WebSocket enabled — inverted logic |
| 216 | Medium | 5/6 | [INT-N05](findings/INT-N05.md) | PropertyChanges permanently destroys CheckBox checked bindings on PointerSettings tab switch |
| 217 | Medium | 5/6 | [INV-N01](findings/INV-N01.md) | QmlUtil::r() stores QML-owned QQuickItemGrabResult raw pointer — use-after-free |
| 218 | Medium | 5/6 | [IO-N01](findings/IO-N01.md) | saveAs() leaves _fileSystemWatcher permanently blocked on open failure |
| 219 | Medium | 5/6 | [JSN-02](findings/JSN-02.md) | ws.sendTextMessage() called without checking WebSocket status |
| 220 | Medium | 5/6 | [LINK-N03](findings/LINK-N03.md) | Qt::WebSockets found as REQUIRED but never explicitly linked |
| 221 | Medium | 5/6 | [LOAD-N01](findings/LOAD-N01.md) | TOCTOU race between QFile::exists() and file.open() in load() |
| 222 | Medium | 5/6 | [LOG-04](findings/LOG-04.md) | MarkersModel::extendLastMarker modifies data without emitting dataChanged |
| 223 | Medium | 5/6 | [LOG-06](findings/LOG-06.md) | DocumentHandler::replaceAll has potential infinite loop with regex |
| 224 | Medium | 5/6 | [LOG-N07](findings/LOG-N07.md) | No error log in loadFromNetworkFinihed() — silent bad-data load |
| 225 | Medium | 5/6 | [LYR-N04](findings/LYR-N04.md) | ESC handler uses activeFocus in base but focus in platform variants — inconsistent |
| 226 | Medium | 5/6 | [MENU-N01](findings/MENU-N01.md) | contextMenu.popup(this) missing click coordinates — menu at wrong position |
| 227 | Medium | 5/6 | [MENU-N02](findings/MENU-N02.md) | Mobile "Add to dictionary" missing %1 placeholder — word never shown |
| 228 | Medium | 5/6 | [MOB-02](findings/MOB-02.md) | No +ios/ QML selector — iOS inherits base main.qml with desktop-only components |
| 229 | Medium | 5/6 | [MOB-03](findings/MOB-03.md) | iOS: IosSaveDialog silently hangs QML caller when temp dir invalid |
| 230 | Medium | 5/6 | [OOB-N01](findings/OOB-N01.md) | MarkersModel::data() — m_data.at() without row < rowCount() guard |
| 231 | Medium | 5/6 | [OOB-N02](findings/OOB-N02.md) | SessionModel::data() — same missing row bounds guard |
| 232 | Medium | 5/6 | [OPC-01](findings/OPC-01.md) | Right-click toggle desynchronizes velocityIndicator visible/opacity |
| 233 | Medium | 5/6 | [PARSE-N01](findings/PARSE-N01.md) | insertImageAt() stores image resource with file:// key but looks up via plain path |
| 234 | Medium | 5/6 | [PATH-N01](findings/PATH-N01.md) | save() fragile percent-encoding round-trip — broken for UNC paths |
| 235 | Medium | 5/6 | [PLAT-05](findings/PLAT-05.md) | DBINARY_ICONS_RESOURCE is a typo — should be BINARY_ICONS_RESOURCE |
| 236 | Medium | 5/6 | [POP-N04](findings/POP-N04.md) | CountdownConfiguration SpinBoxes use focus: true (JS label) instead of focus = true |
| 237 | Medium | 5/6 | [PP-N01](findings/PP-N01.md) | Q_OS_APPLE is not a Qt macro — KGlobalAccel block compiles on all Unix including macOS |
| 238 | Medium | 5/6 | [QLOAD-N01](findings/QLOAD-N01.md) | InputsOverlay toggleButtonsOff() null-check bypass — crash on slow async Loaders |
| 239 | Medium | 5/6 | [R2-AND-03](findings/R2-AND-03.md) | Android Settings missing fakeFullScreen persistence |
| 240 | Medium | 5/6 | [R2-ANDMAN-02](findings/R2-ANDMAN-02.md) | MANAGE_EXTERNAL_STORAGE likely triggers Play Store scrutiny |
| 241 | Medium | 5/6 | [R2-CMAKE-03](findings/R2-CMAKE-03.md) | WORKING_DIRECTORY and COMMENT not parseable by callers of sphinx_add_docs |
| 242 | Medium | 5/6 | [R2-EDT-01](findings/R2-EDT-01.md) | Qt.AlignHustify typo — nonexistent enum value |
| 243 | Medium | 5/6 | [R2-PRP-01](findings/R2-PRP-01.md) | Qt.LeftToRight used as bare boolean — RTL branch always dead |
| 244 | Medium | 5/6 | [R2-PRP-02](findings/R2-PRP-02.md) | Kirigami.Units.SmallSpacing — uppercase S yields undefined |
| 245 | Medium | 5/6 | [R2-PTR-03](findings/R2-PTR-03.md) | Casing error: Units.longDuration should be Units.LongDuration |
| 246 | Medium | 5/6 | [R2-PTR-04](findings/R2-PTR-04.md) | Inverted indexOf truthiness in platform check for ColorDialog |
| 247 | Medium | 5/6 | [R2-TEL-01](findings/R2-TEL-01.md) | Telemetry sub-toggles permanently disconnect from master toggle on click |
| 248 | Medium | 5/6 | [R2-WASM-02](findings/R2-WASM-02.md) | Insecure hostname validation via endsWith allows subdomain spoofing |
| 249 | Medium | 5/6 | [R3-MAIN-05](findings/R3-MAIN-05.md) | Hardcoded Homebrew version-specific Kirigami import path |
| 250 | Medium | 5/6 | [R3-PROP-01](findings/R3-PROP-01.md) | selectionIsLowerCase bound to wrong NOTIFY signal |
| 251 | Medium | 5/6 | [R3-SPL-01](findings/R3-SPL-01.md) | encode() uses toLocal8Bit() instead of dictionary-encoding-aware conversion |
| 252 | Medium | 5/6 | [R3-SPL-02](findings/R3-SPL-02.md) | decode() uses fromLocal8Bit() — suggestions show as mojibake |
| 253 | Medium | 5/6 | [R4-BKG-01](findings/R4-BKG-01.md) | Flip transform origin stays at (0,0) when Flip stored as property |
| 254 | Medium | 5/6 | [R4-EVT-02](findings/R4-EVT-02.md) | Velocity modifier ComboBox lists 2 options but switch handles 4 — dead code |
| 255 | Medium | 5/6 | [R4-ROV-03](findings/R4-ROV-03.md) | Bitwise OR \| used for width fallback instead of logical OR |
| 256 | Medium | 5/6 | [REGEX-N04](findings/REGEX-N04.md) | ReDoS — user-supplied regex has no length limit, timeout, or backtracking guard |
| 257 | Medium | 5/6 | [RENDER-01](findings/RENDER-01.md) | ShaderEffectSource prompterShadowSource runs unconditionally — wastes GPU capture when shadows disabled |
| 258 | Medium | 5/6 | [RENDER-02](findings/RENDER-02.md) | ShaderEffectSource pointerShadowSource runs unconditionally — same pattern |
| 259 | Medium | 5/6 | [RPM-N01](findings/RPM-N01.md) | RPM dependencies entirely commented out — zero automatic dependency resolution |
| 260 | Medium | 5/6 | [SAVE-N01](findings/SAVE-N01.md) | loadFromNetworkFinihed sets m_fileUrl to phantom QTemporaryFile path |
| 261 | Medium | 5/6 | [SCALE-N01](findings/SCALE-N01.md) | Right pointer xScale: -1 mirrors text pointers — backwards/unreadable text |
| 262 | Medium | 5/6 | [ST-N02](findings/ST-N02.md) | Dead overlay.state PropertyChanges — overlay has no states array |
| 263 | Medium | 5/6 | [STATE-N02](findings/STATE-N02.md) | Find.toggle() uses !visible instead of !isOpen — can't close during Prompting |
| 264 | Medium | 5/6 | [STC-N01](findings/STC-N01.md) | closeAll() destroys user's per-screen projection flip configuration |
| 265 | Medium | 5/6 | [TMR-N06](findings/TMR-N06.md) | Auto-reload Timer persists after network dialog close — background refetches |
| 266 | Medium | 5/6 | [TRL-N03](findings/TRL-N03.md) | About-dialog credit roles not translatable |
| 267 | Medium | 5/6 | [TXT-FMT-N01](findings/TXT-FMT-N01.md) | setMarkerHref("") fails to clear QTextFormat::AnchorHref — stale href persists |
| 268 | Medium | 5/6 | [TYP-04](findings/TYP-04.md) | Bitwise AND on bools hides dead code in preventSleep |
| 269 | Medium | 5/6 | [TYP-05](findings/TYP-05.md) | Uninitialized pointer member m_reply in DocumentHandler |
| 270 | Medium | 5/6 | [UNIT-03](findings/UNIT-03.md) | PrompterBackground.qml:160 Units.LongDuration no Kirigami import |
| 271 | Medium | 5/6 | [UNIT-04](findings/UNIT-04.md) | Flip.qml:34,41 two Units.LongDuration no Kirigami import |
| 272 | Medium | 5/6 | [URL-N01](findings/URL-N01.md) | reload() constructs file:// URL by string concatenation without encoding |
| 273 | Medium | 5/6 | [URL-N03](findings/URL-N03.md) | Network-loaded HTML lacks base URL — relative resources broken |
| 274 | Medium | 5/6 | [URL-N05](findings/URL-N05.md) | openFromRemote() blindly prepends http:// to non-HTTP schemes |
| 275 | Medium | 5/6 | [UTF-N01](findings/UTF-N01.md) | text.truncate(64) can split UTF-16 surrogate pairs — corrupted display |
| 276 | Medium | 5/6 | [WATCH-N01](findings/WATCH-N01.md) | addPath() return never checked — silent watch failure |
| 277 | Medium | 5/6 | [WATCH-N02](findings/WATCH-N02.md) | removePath() return never checked — stale path causes double-watch |
| 278 | Medium | 4/6 | [AND-MED-01](findings/AND-MED-01.md) | Missing intent-filter for opening files from other apps |
| 279 | Medium | 4/6 | [AND-RES-01](findings/AND-RES-01.md) | Invalid android:scaleType on bitmap element |
| 280 | Medium | 4/6 | [ANM-N02](findings/ANM-N02.md) | Standby→Ready countdown opacity flash — PropertyChanges opacity:1 conflicts with dissolveIn |
| 281 | Medium | 4/6 | [BLK-N01](findings/BLK-N01.md) | alignment() returns Qt::AlignCenter (includes vertical bit 0x0080) on null cursor |
| 282 | Medium | 4/6 | [CFG-N01](findings/CFG-N01.md) | Desktop MimeType incomplete — only text/html, missing text/plain and text/markdown |
| 283 | Medium | 4/6 | [CLP-N01](findings/CLP-N01.md) | Copy/Cut exports unfiltered HTML to system clipboard |
| 284 | Medium | 4/6 | [CLP-N02](findings/CLP-N02.md) | DropArea external drop never calls drop.accept() |
| 285 | Medium | 4/6 | [CLP-N03](findings/CLP-N03.md) | DropArea external drop: URLs consumed preferentially — text silently lost |
| 286 | Medium | 4/6 | [CMAKE-N03](findings/CMAKE-N03.md) | qt_wrap_ui conflicts with global AUTOUIC — double UI processing |
| 287 | Medium | 4/6 | [COLOR-01](findings/COLOR-01.md) | ProjectionsManager.qml uses invalid "initial" color — repro of R4-ROOT-02 |
| 288 | Medium | 4/6 | [COLOR-02](findings/COLOR-02.md) | Hardcoded #EED text invisible on light themes — WheelSettingsOverlay |
| 289 | Medium | 4/6 | [COLOR-N08](findings/COLOR-N08.md) | textBackground() returns invalid QColor for body/paragraph text |
| 290 | Medium | 4/6 | [COLOR-N09](findings/COLOR-N09.md) | acceptedColor binds transparent QColor on startup — initial text invisible |
| 291 | Medium | 4/6 | [DEF-N02](findings/DEF-N02.md) | DropArea internalDrag always false — internal drag handler dead code |
| 292 | Medium | 4/6 | [ERR-N02](findings/ERR-N02.md) | insertImageAt() async callback silently discards 3 failure modes |
| 293 | Medium | 4/6 | [EVT-06](findings/EVT-06.md) | Drag breaks stopwatch.x binding permanently |
| 294 | Medium | 4/6 | [FD-N01](findings/FD-N01.md) | \|\| should be && in autoReload guard — user preference ignored for non-binary files |
| 295 | Medium | 4/6 | [FONT-METRIC-02](findings/FONT-METRIC-02.md) | FontLoader status never checked — font substitution silently fails |
| 296 | Medium | 4/6 | [GEO-02](findings/GEO-02.md) | main.qml persists x/y/width/height with zero validation |
| 297 | Medium | 4/6 | [GSW-N01](findings/GSW-N01.md) | MarkersDrawer SwipeListItem navigates on swipe — gesture conflict on touch |
| 298 | Medium | 4/6 | [HK-N04](findings/HK-N04.md) | No auto-repeat guard in key-binding configuration Keys.onPressed |
| 299 | Medium | 4/6 | [HSCROLL-N01](findings/HSCROLL-N01.md) | InputsOverlay Flickables use contentWidth: width instead of implicitWidth — horizontal overflow clipped |
| 300 | Medium | 4/6 | [HSCROLL-N02](findings/HSCROLL-N02.md) | Inner Flickables missing flickableDirection: VerticalFlick — conflict with parent horizontal ListView |
| 301 | Medium | 4/6 | [JS-N02](findings/JS-N02.md) | markerCompare() per-frame JSON.stringify() over OBS marker — 60 allocs/sec |
| 302 | Medium | 4/6 | [LDR-N01](findings/LDR-N01.md) | InputsOverlay typeof null guard fails — null.item crash on rapid close |
| 303 | Medium | 4/6 | [LL-N01](findings/LL-N01.md) | 10 EditorToolbar MouseArea/TextField width-depends-on-width binding loops |
| 304 | Medium | 4/6 | [LOG-N05](findings/LOG-N05.md) | Q_UNREACHABLE() in m_setGlobalShortcut() — UB in release on new enum value |
| 305 | Medium | 4/6 | [LYR-N02](findings/LYR-N02.md) | Three OverlaySheets missing from ESC dismiss chain |
| 306 | Medium | 4/6 | [MENU-N03](findings/MENU-N03.md) | Text alignment menu RTL swap: labels swap but actions don't |
| 307 | Medium | 4/6 | [META-N15](findings/META-N15.md) | No StartupWMClass in desktop file — duplicate dock entries, missing icon |
| 308 | Medium | 4/6 | [PERF-N02](findings/PERF-N02.md) | RecentDocuments._load() blocks startup with N synchronous createObject() calls |
| 309 | Medium | 4/6 | [POP-N01](findings/POP-N01.md) | ESC cascade missing dictionariesSheet — undismissable by keyboard |
| 310 | Medium | 4/6 | [POP-N02](findings/POP-N02.md) | ESC cascade missing customWordsSheet — undismissable by keyboard |
| 311 | Medium | 4/6 | [POP-N03](findings/POP-N03.md) | ESC cascade missing obsConfiguration — undismissable by keyboard despite alias |
| 312 | Medium | 4/6 | [QML-11](findings/QML-11.md) | Dead code: `window` property declared but never used in WindowDragger |
| 313 | Medium | 4/6 | [QW-N01](findings/QW-N01.md) | Projection Window onClosing references cleared model — spurious runtime errors |
| 314 | Medium | 4/6 | [QW-N02](findings/QW-N02.md) | Stale QScreen reference in projection model — dangling after monitor hot-unplug |
| 315 | Medium | 4/6 | [R2-WASM-01](findings/R2-WASM-01.md) | File input element never removed from DOM on user cancel |
| 316 | Medium | 4/6 | [RESO-N01](findings/RESO-N01.md) | Editing font size not viewport-scaled — text nearly unreadable on 4K |
| 317 | Medium | 4/6 | [SAFE-01](findings/SAFE-01.md) | +android/main.qml zero safe area insets |
| 318 | Medium | 4/6 | [SAFE-02](findings/SAFE-02.md) | ReadRegionOverlay screenMiddle ignores notch/status bar height |
| 319 | Medium | 4/6 | [SCR-N03](findings/SCR-N03.md) | No runtime screen plug/unplug handling — stale projection windows on disconnected screens |
| 320 | Medium | 4/6 | [SCRL-N02](findings/SCRL-N02.md) | __destination typed int truncates real-valued position |
| 321 | Medium | 4/6 | [SHDR-N02](findings/SHDR-N02.md) | id: shadow collides with property ShaderEffectSource shadow — ambiguous resolution in blur chain |
| 322 | Medium | 4/6 | [SHT-N01](findings/SHT-N01.md) | markerToggle/namedMarkerToggle forwarded but never handled — dead hotkeys |
| 323 | Medium | 4/6 | [STC-N04](findings/STC-N04.md) | Projection window CursorAutoHide not reset on close — cursor permanently hidden |
| 324 | Medium | 4/6 | [TAB-N01](findings/TAB-N01.md) | PointerSettings TabButton onClicked skips currentIndex assignment |
| 325 | Medium | 4/6 | [TB-N01](findings/TB-N01.md) | toolbar toggle timers produce stale state on rapid clicks |
| 326 | Medium | 4/6 | [TB-N02](findings/TB-N02.md) | baseSpeedSlider/baseAccelerationSlider onMoved yanks focus to prompter instead of restoreFocus() |
| 327 | Medium | 4/6 | [TBND-N01](findings/TBND-N01.md) | SpellHighlighter regex excludes combining diacritical marks — NFD text misspelled |
| 328 | Medium | 4/6 | [TMR-03](findings/TMR-03.md) | dissolveIn animation re-triggered entering Running from Ready — flicker |
| 329 | Medium | 4/6 | [TMR-N01](findings/TMR-N01.md) | resetBackground Timer not stopped when new background loaded — race erases new image |
| 330 | Medium | 4/6 | [TMR-N02](findings/TMR-N02.md) | Windows onFrameSwapped missing qmlutil.r(p) — per-frame grab result leak |
| 331 | Medium | 4/6 | [TOG-N01](findings/TOG-N01.md) | WheelSettingsOverlay useScrollAsDialButton — cross-path stale checked state |
| 332 | Medium | 4/6 | [TP-N01](findings/TP-N01.md) | "Error loading file..." used as document content, not placeholderText |
| 333 | Medium | 4/6 | [TXT-N04](findings/TXT-N04.md) | goToNextMarker() temporarily sets cursorPosition=-1 — corrupts cursor state |
| 334 | Medium | 4/6 | [UNIT-06](findings/UNIT-06.md) | Find.qml:92 Units.ShortDuration with namespaced Kirigami import |
| 335 | Medium | 4/6 | [UNIT-07](findings/UNIT-07.md) | ReadRegionOverlay.qml 3x Units.ShortDuration with namespaced import |
| 336 | Medium | 4/6 | [VIS-N05](findings/VIS-N05.md) | velocityDragOverlay blocks all interaction during indicator fade-out (~500ms dead zone) |
| 337 | Medium | 4/6 | [W10-CLP-02](findings/W10-CLP-02.md) | Remote image URLs in pasted HTML cause unsanctioned network requests |
| 338 | Medium | 4/6 | [W10-WSM-02](findings/W10-WSM-02.md) | Global file-picker state overwritten by re-entrant calls — wrong file delivered |
| 339 | Medium | 4/6 | [WINDOW-N01](findings/WINDOW-N01.md) | Projection windows not closed on main window close — orphaned on Linux |
| 340 | Medium (masked — Labs.MenuBar dead per IMP-N01) | 3/6 | [ACT-N08](findings/ACT-N08.md) | All checkable Labs.MenuItems inherit R2-EDT-03 binding-break pattern |
| 341 | Medium (latent) | 3/6 | [AND-MFT-01](findings/AND-MFT-01.md) | FileProvider resource @xml/qtprovider_paths — file named filepaths.xml |
| 342 | Medium | 3/6 | [CLI-N01](findings/CLI-N01.md) | --version flag non-functional — version string empty when parser processes |
| 343 | Medium | 3/6 | [DPI-01](findings/DPI-01.md) | TimerClock.qml:127 devicePixelRatio in raw arithmetic with magic multiplier |
| 344 | Medium | 3/6 | [DRW-01](findings/DRW-01.md) | interalFocusElsewhere() misses 3 OverlaySheets + 2 Drawers — hotkeys pass through |
| 345 | Medium | 3/6 | [DRW-02](findings/DRW-02.md) | globalDrawer and contextDrawer missing from ESC dismiss chain |
| 346 | Medium | 3/6 | [KB-N01](findings/KB-N01.md) | Find.qml: 9 toolbar buttons missing focusPolicy — keyboard-invisible |
| 347 | Medium | 3/6 | [KB-N02](findings/KB-N02.md) | InputsOverlay TabBar TabButtons have no focusPolicy + keyNavigationEnabled: false — keyboard dead |
| 348 | Medium | 3/6 | [KB-N03](findings/KB-N03.md) | +windows and +android ESC handler uses .focus instead of .activeFocus — wrong boolean |
| 349 | Medium | 3/6 | [LAZY-N02](findings/LAZY-N02.md) | InputsOverlay ObjectModel eagerly loads both tabs — hidden tab content loaded prematurely |
| 350 | Medium | 3/6 | [R2-OVL-01](findings/R2-OVL-01.md) | InputsOverlay onOpened calls cursorAutoHide.restart() instead of reset() |
| 351 | Medium | 3/6 | [R2-REC-02](findings/R2-REC-02.md) | refreshExistence skips UI updates when dynamic children out of sync |
| 352 | Medium | 3/6 | [RAII-N03](findings/RAII-N03.md) | QProcess orphan — child process detached on waitForFinished() timeout |
| 353 | Medium | 3/6 | [TB-N04](findings/TB-N04.md) | velocityDragArea accepts MiddleButton without propagateComposedEvents — scroll blocked |
| 354 | Medium | 3/6 | [TBND-N02](findings/TBND-N02.md) | All CJK text marked misspelled — ideographic characters not in Hunspell dictionaries |
| 355 | Medium | 3/6 | [W10-PMV-02](findings/W10-PMV-02.md) | Circular ShaderEffectSource dependency — shadow ghost on first frame |
| 356 | Low | 6/6 | [CMAKE-N02](findings/CMAKE-N02.md) | INTERFACE_LINK_LIBRARIES on executable target — no-op |
| 357 | Low | 6/6 | [CMAKE-N05](findings/CMAKE-N05.md) | foreach(file IN LISTS icon_files doc) — "doc" never defined |
| 358 | Low | 6/6 | [COMP-N01](findings/COMP-N01.md) | Case-sensitive duplicate detection in setLanguages() |
| 359 | Low | 6/6 | [DISK-N01](findings/DISK-N01.md) | saveCustomWordsToDisk() non-atomic write — data loss on power failure |
| 360 | Low | 6/6 | [ENC-02](findings/ENC-02.md) | getMarkerKey() mid(4) without length/startsWith guard |
| 361 | Low | 6/6 | [FOC-N01](findings/FOC-N01.md) | focus: true is JS label in atEndLoopDelay SpinBox |
| 362 | Low | 6/6 | [FOC-N02](findings/FOC-N02.md) | Same JS label bug in countdownConfiguration SpinBoxes (2 instances) |
| 363 | Low | 6/6 | [INIT-N02](findings/INIT-N02.md) | Find.qml SearchField placeholderText always empty — no guidance text |
| 364 | Low | 6/6 | [MA-N02](findings/MA-N02.md) | textDragArea missing cursorShape — ArrowCursor over IBeamCursor on editor |
| 365 | Low | 6/6 | [MOB-04](findings/MOB-04.md) | Android: restartApplication() quits without restart |
| 366 | Low | 6/6 | [MOB-05](findings/MOB-05.md) | Android: Missing INTERNET permission in manifest |
| 367 | Low | 6/6 | [MOB-06](findings/MOB-06.md) | Android: PrompterPage display delegate Component.onCompleted references projectionManager — startup TypeError |
| 368 | Low | 6/6 | [PLAT-06](findings/PLAT-06.md) | qprompt_QM_LOADER variable never defined |
| 369 | Low | 6/6 | [QCN-01](findings/QCN-01.md) | O(n²) contains()-in-loop during custom words file load |
| 370 | Low | 6/6 | [R2-FONT-02](findings/R2-FONT-02.md) | Duplicate setText call on preview label |
| 371 | Low | 6/6 | [R3-SIG-01](findings/R3-SIG-01.md) | textChanged() signal declared but never emitted |
| 372 | Low | 6/6 | [REGEX-N03](findings/REGEX-N03.md) | Unescaped dot in font-size regex — matches any char instead of decimal |
| 373 | Low | 6/6 | [REGEX-N05](findings/REGEX-N05.md) | regex_0 and regex_3 use . (any-char) instead of \. (literal dot) in decimal matching |
| 374 | Low | 6/6 | [SAVE-N05](findings/SAVE-N05.md) | save() broken on Android content:// URIs — empty filename |
| 375 | Low | 6/6 | [SCRL-N04](findings/SCRL-N04.md) | __speed non-zero when __i=0 and __curvature=0 (Math.pow(0,0)===1) |
| 376 | Low | 6/6 | [SIZE-N02](findings/SIZE-N02.md) | Three Button children of Row have dead anchors.bottom declarations |
| 377 | Low | 6/6 | [SPL2-16](findings/SPL2-16.md) | QDir::mkpath return unchecked — dict cache directory may silently not exist |
| 378 | Low | 6/6 | [SPL2-17](findings/SPL2-17.md) | QFile::setPermissions return unchecked — cached dict may be unreadable |
| 379 | Low | 6/6 | [SPL2-19](findings/SPL2-19.md) | availableDictionaries enumerates .dic without verifying .aff exists |
| 380 | Low | 6/6 | [TBND-N03](findings/TBND-N03.md) | extendLastMarker() doesn't update Marker::length field — stale after appends |
| 381 | Low | 6/6 | [TC-N01](findings/TC-N01.md) | Image.source assigned boolean false instead of empty string |
| 382 | Low | 6/6 | [TIME-N01](findings/TIME-N01.md) | copyrightYear computed then discarded — stale "2020-2026" in About after 2026 |
| 383 | Low | 6/6 | [TMR-05](findings/TMR-05.md) | ScriptAction `paintReady` references non-existent function |
| 384 | Low | 6/6 | [TRN-N01](findings/TRN-N01.md) | Dead ternary: both branches return Qt.OpenHandCursor |
| 385 | Low | 6/6 | [TYP-N01](findings/TYP-N01.md) | Misspelled method name: loadFromNetworkFinihed (missing 's') |
| 386 | Low | 6/6 | [TYP-N02](findings/TYP-N02.md) | Misspelled parameter: withoutFormating (missing 't') |
| 387 | Low | 6/6 | [TYP-N05](findings/TYP-N05.md) | Uninitialized member m_documentComesFromNetwork |
| 388 | Low | 6/6 | [WSM-N02](findings/WSM-N02.md) | WASM preventSleep() falls through to desktop #else — always returns false |
| 389 | Low | 5/6 | [API-N05](findings/API-N05.md) | fileName()/fileType() return fabricated defaults — can't distinguish "no file" from "untitled.html" |
| 390 | Low | 5/6 | [API-N06](findings/API-N06.md) | SystemFontChooserDialog::show() calls setText() on same label twice — dead code |
| 391 | Low | 5/6 | [API-N07](findings/API-N07.md) | SpellChecker::encode() fallback says "Latin-1" but calls toLocal8Bit() |
| 392 | Low | 5/6 | [CFG-N03](findings/CFG-N03.md) | "fixedd" typo in v2.0.2 release description |
| 393 | Low | 5/6 | [CMAKE-NEW-01](findings/CMAKE-NEW-01.md) | Remote.qml exists on disk but never listed in QML_FILES |
| 394 | Low | 5/6 | [DBG-N02](findings/DBG-N02.md) | Velocity debug logging active in production |
| 395 | Low | 5/6 | [DBG-N04](findings/DBG-N04.md) | qDebug() in namedMarker()/setMarker() active in release |
| 396 | Low | 5/6 | [DLG-N03](findings/DLG-N03.md) | errorDialog MessageDialog has no title |
| 397 | Low | 5/6 | [DLG-N07](findings/DLG-N07.md) | 5 showPassiveNotification() calls ignore passiveNotifications preference |
| 398 | Low | 5/6 | [DLG-N08](findings/DLG-N08.md) | 3 save-completion passive notifications lack passiveNotifications guard |
| 399 | Low | 5/6 | [DLG-N11](findings/DLG-N11.md) | PrompterPage ColorDialogs — dead acceptedColor property binding |
| 400 | Low | 5/6 | [DRAG-N02](findings/DRAG-N02.md) | textDragArea has no cursorShape — no cursor feedback during text drag |
| 401 | Low | 5/6 | [FONT-N02](findings/FONT-N02.md) | FontLoader id typo: westernSeriousSansfFont — stray 'f' in "Sans" |
| 402 | Low | 5/6 | [HDR-N01](findings/HDR-N01.md) | promptsession.h not in CMakeLists.txt — SessionModel/DataPoint dead code |
| 403 | Low | 5/6 | [HDR-N02](findings/HDR-N02.md) | telemetry.h not in CMakeLists.txt — Telemetry dead code |
| 404 | Low | 5/6 | [JS-N01](findings/JS-N01.md) | TIMERCLOCK getTimeString() — redundant .toString() on already-string — 54 allocs/sec |
| 405 | Low | 5/6 | [LOG-08](findings/LOG-08.md) | DataPoint default constructor leaves three members uninitialized |
| 406 | Low | 5/6 | [MA-N01](findings/MA-N01.md) | overlayMouseArea permanently disabled — dead MouseArea |
| 407 | Low | 5/6 | [MENU-N04](findings/MENU-N04.md) | Trailing empty MenuSeparator at end of mobile context menu |
| 408 | Low | 5/6 | [MODEL-N02](findings/MODEL-N02.md) | SessionModel::clearDataPoints lacks empty-model guard before beginRemoveRows |
| 409 | Low | 5/6 | [NET-N06](findings/NET-N06.md) | loadFromNetwork() validates original URL, not constructed resultingUrl |
| 410 | Low | 5/6 | [NOTIFY-02](findings/NOTIFY-02.md) | availableDictionariesChanged NOTIFY signal never emitted |
| 411 | Low | 5/6 | [R2-OVL-02](findings/R2-OVL-02.md) | LanguageSettingsOverlay popup ListView currentIndex always resolves to -1 |
| 412 | Low | 5/6 | [R3-MAIN-08](findings/R3-MAIN-08.md) | QFontDatabase::addApplicationFont return value discarded |
| 413 | Low | 5/6 | [SPL2-18](findings/SPL2-18.md) | Hunspell::add return value unchecked at 4 call sites |
| 414 | Low | 5/6 | [UNIT-05](findings/UNIT-05.md) | pointer_0.qml:72 Units.VeryLongDuration no Kirigami import |
| 415 | Low | 5/6 | [URL-N04](findings/URL-N04.md) | loadFromNetwork() validates wrong URL instance |
| 416 | Low | 5/6 | [WARN-N02](findings/WARN-N02.md) | SpellChecker::addWord() — dead public API, never called |
| 417 | Low | 5/6 | [WARN-N04](findings/WARN-N04.md) | QProcess::startDetached() bool return silently ignored |
| 418 | Low | 5/6 | [WATCH-N04](findings/WATCH-N04.md) | unblockFileWatcher() dereferences _fileSystemWatcher without null guard |
| 419 | Low | 5/6 | [WYS-N02](findings/WYS-N02.md) | Default stylesheet CSS errors: valign:top (not a CSS property) and border:1pt (missing style) |
| 420 | Low | 4/6 | [API-N04](findings/API-N04.md) | setMarker(bool) misleadingly named — sets regular marker, not any marker |
| 421 | Low | 4/6 | [CFG-N02](findings/CFG-N02.md) | v1.1.3 release date "2022-1-16" breaks chronological order — should be 2023-01-16 |
| 422 | Low | 4/6 | [COERC-N03](findings/COERC-N03.md) | real→int truncation in WindowDragger position compounds drift |
| 423 | Low | 4/6 | [DRAG-N01](findings/DRAG-N01.md) | Image resize body drag: cursor shows OpenHandCursor until drag threshold exceeded |
| 424 | Low | 4/6 | [FOC-N03](findings/FOC-N03.md) | Tab/Backtab asymmetry — Backtab silently unhandled |
| 425 | Low | 4/6 | [GEO-03](findings/GEO-03.md) | +android/main.qml no minimumWidth/minimumHeight |
| 426 | Low | 4/6 | [HK-N06](findings/HK-N06.md) | isValidInput checks local keybindings only — silent conflict with global hotkeys |
| 427 | Low | 4/6 | [LAZY-N01](findings/LAZY-N01.md) | namedMarkerConfiguration Loader double-loads KeyInputButton — first load wasted |
| 428 | Low | 4/6 | [LL-N02](findings/LL-N02.md) | ProgressIndicator stepSize divide-by-zero when prompter.height is 0 |
| 429 | Low | 4/6 | [LVW-N01](findings/LVW-N01.md) | InputsOverlay.qml ListView currentIndex: PointerSettings.States.Arrow — copy-paste error |
| 430 | Low | 4/6 | [MENU-N05](findings/MENU-N05.md) | "Redo" context menu item missing & accelerator |
| 431 | Low | 4/6 | [META-N01](findings/META-N01.md) | QMetaObject::invokeMethod return value unchecked — silent failure on WASM |
| 432 | Low | 4/6 | [PLAT-07](findings/PLAT-07.md) | Incorrect macro syntax: `#define Use_GlobalAccel = 1` |
| 433 | Low | 4/6 | [PLAT-N05](findings/PLAT-N05.md) | Base main.qml fullScreenPlatform missing "wasm" (inconsistent with +windows) |
| 434 | Low | 4/6 | [QF-N02](findings/QF-N02.md) | QDir::entryList missing QDir::Readable in availableDictionaries() |
| 435 | Low | 4/6 | [QF-N03](findings/QF-N03.md) | TOCTOU: QFile::exists() → QFile::copy() in resource cache extraction |
| 436 | Low | 4/6 | [QRC-N02](findings/QRC-N02.md) | Four .qrc files are dead code — never referenced by CMakeLists.txt |
| 437 | Low | 4/6 | [R2-REC-01](findings/R2-REC-01.md) | File URI prefix strip off-by-one on Windows |
| 438 | Low | 4/6 | [RAII-N02](findings/RAII-N02.md) | IosSaveDialog::m_tempDir created unconditionally on all platforms — wasted I/O |
| 439 | Low | 4/6 | [RESO-N02](findings/RESO-N02.md) | Scrollbar width 6dp-13dp — below minimum 44dp touch target |
| 440 | Low | 4/6 | [RESO-N05](findings/RESO-N05.md) | PointerSettings ListView height hardcoded 180dp — doesn't fill available space |
| 441 | Low | 4/6 | [RND-N02](findings/RND-N02.md) | Missing smooth: true on background Image — aliased upscale |
| 442 | Low | 4/6 | [RND-N03](findings/RND-N03.md) | Missing smooth: true on projection Image — aliased text on external displays |
| 443 | Low | 4/6 | [SHADOW-01](findings/SHADOW-01.md) | id: rotation shadows Item.rotation property |
| 444 | Low | 4/6 | [SHADOW-02](findings/SHADOW-02.md) | id: flow shadows Flow.flow property |
| 445 | Low | 4/6 | [STATE-N03](findings/STATE-N03.md) | Countdown Running restarts dissolveIn unnecessarily — visual dim-to-bright flash |
| 446 | Low | 4/6 | [STC-N05](findings/STC-N05.md) | cancel() doesn't call timer.stopTimer() — elapsed time persists across sessions |
| 447 | Low | 4/6 | [TXT-N02](findings/TXT-N02.md) | TimerClock default text color #AAA on #131619 — fails WCAG AA contrast |
| 448 | Low | 4/6 | [TYP-06](findings/TYP-06.md) | Malformed preprocessor macro: `#define Use_GlobalAccel = 1` |
| 449 | Low | 4/6 | [TYP-07](findings/TYP-07.md) | Narrowing conversion: `size_t` → `int` in SpellChecker::decode |
| 450 | Low | 4/6 | [VIS-FB-N01](findings/VIS-FB-N01.md) | bookmarkListButton and searchButton missing checkable: true — no checked background |
| 451 | Low | 4/6 | [WARN-N01](findings/WARN-N01.md) | SpellHighlighter::isEnabled() — dead code, never called |
| 452 | Low | 3/6 | [ACT-N06](findings/ACT-N06.md) | +windows main.qml Performance tweaks missing enableBarsSetting |
| 453 | Low | 3/6 | [BIND-N01](findings/BIND-N01.md) | contentWidth undefined for Shape/Image pointer types — transform origin silently wrong |
| 454 | Low | 3/6 | [CNTD-N01](findings/CNTD-N01.md) | Countdown Running: dissolveIn and dissolveOut compete for same opacity when __iterations===__disappearWithin===1 |
| 455 | Low | 3/6 | [COLOR-04](findings/COLOR-04.md) | ReadRegionOverlay ColorAnimation tracks __fillColor that never changes |
| 456 | Low | 3/6 | [DPI-02](findings/DPI-02.md) | MarkersDrawer.qml:37 drawer minimumWidth hardcoded to 260px |
| 457 | Low | 3/6 | [DPI-03](findings/DPI-03.md) | Find.qml:38 searchBarWidth:724 hardcoded in px |
| 458 | Low | 3/6 | [EVT-09](findings/EVT-09.md) | Flow ToolSeparator visibility compares y of potentially invisible rows |
| 459 | Low | 3/6 | [EVT-10](findings/EVT-10.md) | Nested MouseAreas with hoverEnabled steal hover from parent Buttons |
| 460 | Low | 3/6 | [GEO-01](findings/GEO-01.md) | main.qml initial 728px height too large for 1366x768 laptops |
| 461 | Low | 3/6 | [LBL-N03](findings/LBL-N03.md) | PrompterView 3× height overflow in theforce debug mode |
| 462 | Low | 3/6 | [LOAD-N02](findings/LOAD-N02.md) | reset() emits 12 NOTIFY signals when open() fails but exists() succeeds |
| 463 | Low | 3/6 | [ORIENT-N01](findings/ORIENT-N01.md) | TimerClock binary width>height orientation creates sharp 2x font jump at 1:1 |
| 464 | Low | 3/6 | [R2-AND-04](findings/R2-AND-04.md) | Android Settings for "background" missing transparency persistence |
| 465 | Low | 3/6 | [R2-AND-05](findings/R2-AND-05.md) | Android loadTelemetryPage passes no properties object to pageStack push |
| 466 | Low | 3/6 | [R2-PRP-05](findings/R2-PRP-05.md) | Potential null-item access on async Loader in namedMarkerConfiguration.onOpened |
| 467 | Low | 3/6 | [R4-EXP-09](findings/R4-EXP-09.md) | LibreOffice import --cat and --convert-to flags are contradictory |
| 468 | Low | 3/6 | [R4-IOSCPP-01](findings/R4-IOSCPP-01.md) | QTemporaryDir created on all platforms including non-iOS where unused |
| 469 | Low | 3/6 | [R4-SIG-ADD-01](findings/R4-SIG-ADD-01.md) | SessionModel::appendDataPoint declared public slot but never connected |
| 470 | Low | 3/6 | [RESO-N06](findings/RESO-N06.md) | ReadRegionOverlay pointer margin 3dp — overlap with text at large fonts |
| 471 | Low | 3/6 | [RESP-N03](findings/RESP-N03.md) | +android/main.qml omits all size declarations — transient zero-size layout on startup |
| 472 | Low | 3/6 | [RND-N01](findings/RND-N01.md) | forceQtTextRenderer dead on Apple platforms — unconditionally uses NativeRendering |
| 473 | Low | 3/6 | [SHADOW-N04](findings/SHADOW-N04.md) | id: frame shadows property bool frame — latent hazard |
| 474 | Low | 3/6 | [SHT-N02](findings/SHT-N02.md) | Missing StandardKey.FullScreen on Android |
| 475 | Low | 3/6 | [SPL2-20](findings/SPL2-20.md) | loadCustomWordsFromDisk redundant exists() before open() |
| 476 | Low | 3/6 | [STC-N02](findings/STC-N02.md) | Find.qml close() doesn't reset replace-mode or regex-mode flags |
| 477 | Low | 3/6 | [TC-N02](findings/TC-N02.md) | property color value assigned string expression — silent coercion |
| 478 | Low | 3/6 | [TMR-07](findings/TMR-07.md) | countdownAnimation restart uses non-idempotent running=true |
| 479 | Low | 3/6 | [Z-N02](findings/Z-N02.md) | Two OverlaySheets have z:1 while nine others have none — inconsistent stacking |
| 480 | Low | 2/6 | [COLOR-03](findings/COLOR-03.md) | velocityText ColorAnimation flash: #BBB → #FFF → #CCC jump |
| 481 | Low | 2/6 | [DSZ-03](findings/DSZ-03.md) | Magic number 68 in ListView height binding |
| 482 | Low | 2/6 | [EVT-N11](findings/EVT-N11.md) | windowStayOnTopButton lacks focusPolicy — unreachable via keyboard |
| 483 | Low | 2/6 | [EVT-N12](findings/EVT-N12.md) | velocityDragArea and viewport.mouse share z:5 — wheel dispatch ambiguous |
| 484 | Low | 2/6 | [MENU-N06](findings/MENU-N06.md) | Paste behavior inconsistent between context menu and global Edit menu |
| 485 | Low | 2/6 | [PRE-N01](findings/PRE-N01.md) | Preprocessor uses `or` instead of `\|\|` in 6 #if directives — MSVC build break |
| 486 | Low | 2/6 | [R2-PRP-04](findings/R2-PRP-04.md) | Inconsistent focus restoration in decreaseVelocityButton |
| 487 | Low | 2/6 | [VCI-N03](findings/VCI-N03.md) | Hardcoded divider/separator/border colors (#292929, #606060, #808080) break theme adaptation |
| 488 | Low | 2/6 | [VIS-N04](findings/VIS-N04.md) | Countdown crosshair frame renders orphan lines when enabled=false |
| 489 | Low | 2/6 | [Z-N03](findings/Z-N03.md) | ComboBox Popup z:103 inside OverlaySheets with z:1 — disconnected layering |
| 490 | Low | 1/6 | [DBG-N03](findings/DBG-N03.md) | Latent debug state leak: pointers/debug Setting persists Guides checkbox |
| 491 |  | 6/6 | [TS-03](findings/TS-03.md) | Korean UI `ko_KO` vs file `ko_KR` mismatch |
| 492 |  | 4/6 | [TS-02](findings/TS-02.md) | Arabic file `ar_EG` vs UI `ar_AE` mismatch |
| 493 |  | 4/6 | [TS-05](findings/TS-05.md) | Finnish/French/Korean/Italian "Saved" → verb with stray `&amp;` accelerator |
| 494 |  | 4/6 | [TS-16](findings/TS-16.md) | Paragraph spacing: 8 languages strip trailing `%` from `<pre>%1%</pre>` |
| 495 |  | 4/6 | [TS-17](findings/TS-17.md) | Line width: 7 languages add spurious `%` to `<pre>%1</pre>` |

<details><summary>Minor / non-behavioral (opus-ultra = PARTIAL) — 94</summary>

[LOG-07](findings/LOG-07.md), [SEC-04](findings/SEC-04.md), [SEC-05](findings/SEC-05.md), [RES-03](findings/RES-03.md), [RES-04](findings/RES-04.md), [TYP-03](findings/TYP-03.md), [EDGE-07](findings/EDGE-07.md), [EDGE-11](findings/EDGE-11.md), [PLAT-08](findings/PLAT-08.md), [R2-IOS-02](findings/R2-IOS-02.md), [R3-SPL-05](findings/R3-SPL-05.md), [R3-PMT-03](findings/R3-PMT-03.md), [R4-ROOT-05](findings/R4-ROOT-05.md), [FINAL-10](findings/FINAL-10.md), [FINAL-14](findings/FINAL-14.md), [FINAL-15](findings/FINAL-15.md), [FINAL-22](findings/FINAL-22.md), [TRL-N01](findings/TRL-N01.md), [HTK-05](findings/HTK-05.md), [HTK-06](findings/HTK-06.md), [HTK-07](findings/HTK-07.md), [HTK-08](findings/HTK-08.md), [THR-01](findings/THR-01.md), [THR-02](findings/THR-02.md), [THR-03](findings/THR-03.md), [THR-04](findings/THR-04.md), [CPY-01](findings/CPY-01.md), [OOB-N03](findings/OOB-N03.md), [I18N-N01](findings/I18N-N01.md), [I18N-N02](findings/I18N-N02.md), [MIX-01](findings/MIX-01.md), [AR-01](findings/AR-01.md), [SET-01](findings/SET-01.md), [SET-04](findings/SET-04.md), [IMP-NEW-02](findings/IMP-NEW-02.md), [IMP-NEW-03](findings/IMP-NEW-03.md), [CMT-N01](findings/CMT-N01.md), [CMT-N02](findings/CMT-N02.md), [CMT-N03](findings/CMT-N03.md), [CMT-N09](findings/CMT-N09.md), [CMT-N10](findings/CMT-N10.md), [REGEX-N01](findings/REGEX-N01.md), [PROP-N02](findings/PROP-N02.md), [PROP-N03](findings/PROP-N03.md), [SCRL-N01](findings/SCRL-N01.md), [SCRL-N05](findings/SCRL-N05.md), [TYP-N03](findings/TYP-N03.md), [TYP-N04](findings/TYP-N04.md), [TYP-N06](findings/TYP-N06.md), [TXT-N01](findings/TXT-N01.md), [PLAT-N01](findings/PLAT-N01.md), [DECL-N01](findings/DECL-N01.md), [DECL-N02](findings/DECL-N02.md), [COLOR-05](findings/COLOR-05.md), [COLOR-06](findings/COLOR-06.md), [COLOR-07](findings/COLOR-07.md), [CONST-N01](findings/CONST-N01.md), [CONST-N02](findings/CONST-N02.md), [CONST-N03](findings/CONST-N03.md), [CONST-N04](findings/CONST-N04.md), [CONST-N05](findings/CONST-N05.md), [SAVE-N04](findings/SAVE-N04.md), [RAII-N01](findings/RAII-N01.md), [Z-N01](findings/Z-N01.md), [Z-N04](findings/Z-N04.md), [ARC-01](findings/ARC-01.md), [ARC-02](findings/ARC-02.md), [ARC-03](findings/ARC-03.md), [ARC-04](findings/ARC-04.md), [ARC-05](findings/ARC-05.md), [ARC-06](findings/ARC-06.md), [STR-CNV](findings/STR-CNV.md), [COMP-N03](findings/COMP-N03.md), [LBL-N01](findings/LBL-N01.md), [LAY-N01](findings/LAY-N01.md), [LAY-N02](findings/LAY-N02.md), [WARN-N03](findings/WARN-N03.md), [INT-N01](findings/INT-N01.md), [INT-N02](findings/INT-N02.md), [INT-N03](findings/INT-N03.md), [PERF-N01](findings/PERF-N01.md), [PERF-N03](findings/PERF-N03.md), [SIG-N03](findings/SIG-N03.md), [QOBJ-N01](findings/QOBJ-N01.md), [VCI-N01](findings/VCI-N01.md), [VCI-N02](findings/VCI-N02.md), [TP-SYS](findings/TP-SYS.md), [DETACH-N01](findings/DETACH-N01.md), [SYM-N01](findings/SYM-N01.md), [A11Y-SYS](findings/A11Y-SYS.md), [RESO-N03](findings/RESO-N03.md), [RESO-N04](findings/RESO-N04.md), [TB-N03](findings/TB-N03.md), [RESP-N01](findings/RESP-N01.md)

</details>

<details><summary>Rejected (opus-ultra = FALSE) — 70</summary>

[LOG-09](findings/LOG-09.md), [QML-01](findings/QML-01.md), [QML-02](findings/QML-02.md), [QML-07](findings/QML-07.md), [QML-08](findings/QML-08.md), [QML-09](findings/QML-09.md), [QML-10](findings/QML-10.md), [RES-05](findings/RES-05.md), [TYP-01](findings/TYP-01.md), [TYP-02](findings/TYP-02.md), [TYP-08](findings/TYP-08.md), [TYP-09](findings/TYP-09.md), [TYP-10](findings/TYP-10.md), [EDGE-08](findings/EDGE-08.md), [EDGE-10](findings/EDGE-10.md), [EDGE-12](findings/EDGE-12.md), [PLAT-04](findings/PLAT-04.md), [R2-GH-01](findings/R2-GH-01.md), [R2-CMAKE-01](findings/R2-CMAKE-01.md), [R2-PRP-03](findings/R2-PRP-03.md), [R2-PTR-01](findings/R2-PTR-01.md), [R2-PTR-02](findings/R2-PTR-02.md), [R3-DOC-02](findings/R3-DOC-02.md), [R3-SPL-03](findings/R3-SPL-03.md), [R3-MAIN-01](findings/R3-MAIN-01.md), [R3-MAIN-04](findings/R3-MAIN-04.md), [R3-APP-01](findings/R3-APP-01.md), [R3-SIG-02](findings/R3-SIG-02.md), [R3-SIG-03](findings/R3-SIG-03.md), [R4-QTV-01](findings/R4-QTV-01.md), [R4-QTV-02](findings/R4-QTV-02.md), [R4-QTV-03](findings/R4-QTV-03.md), [R4-ROOT-03](findings/R4-ROOT-03.md), [R4-EVT-01](findings/R4-EVT-01.md), [R4-PRJ-01](findings/R4-PRJ-01.md), [R4-SHD-01](findings/R4-SHD-01.md), [FINAL-02](findings/FINAL-02.md), [FINAL-07](findings/FINAL-07.md), [FINAL-20](findings/FINAL-20.md), [IMP-N01](findings/IMP-N01.md), [IMP-N02](findings/IMP-N02.md), [W10-HTK-01](findings/W10-HTK-01.md), [EVT-02](findings/EVT-02.md), [NET-02](findings/NET-02.md), [VER-01](findings/VER-01.md), [QML-BND-03](findings/QML-BND-03.md), [CMAKE-N01](findings/CMAKE-N01.md), [SET-03](findings/SET-03.md), [IMP-NEW-01](findings/IMP-NEW-01.md), [IMP-NEW-04](findings/IMP-NEW-04.md), [CMT-N04](findings/CMT-N04.md), [CMT-N05](findings/CMT-N05.md), [CMT-N06](findings/CMT-N06.md), [CMT-N07](findings/CMT-N07.md), [INIT-N03](findings/INIT-N03.md), [INIT-N04](findings/INIT-N04.md), [SCRL-N06](findings/SCRL-N06.md), [PLAT-N02](findings/PLAT-N02.md), [LBL-N02](findings/LBL-N02.md), [QPROP-N02](findings/QPROP-N02.md), [DEF-N01](findings/DEF-N01.md), [IMH-SYS](findings/IMH-SYS.md), [EKA-SYS](findings/EKA-SYS.md), [LOG-N04](findings/LOG-N04.md), [FONT-N01](findings/FONT-N01.md), [COLOR-CRIT-01](findings/COLOR-CRIT-01.md), [RPL-N01](findings/RPL-N01.md), [FONT-METRIC-03](findings/FONT-METRIC-03.md), [QT-LC-N01](findings/QT-LC-N01.md), [MIME-N01](findings/MIME-N01.md)

</details>

<details><summary>Needs info (opus-ultra = UNSURE) — 63</summary>

[PLAT-09](findings/PLAT-09.md), [R3-TMR-01](findings/R3-TMR-01.md), [R4-PRJ-02](findings/R4-PRJ-02.md), [FINAL-16](findings/FINAL-16.md), [LYR-N03](findings/LYR-N03.md), [TS-01](findings/TS-01.md), [TS-04](findings/TS-04.md), [TS-06](findings/TS-06.md), [TS-07](findings/TS-07.md), [TS-08](findings/TS-08.md), [TS-09](findings/TS-09.md), [TS-10](findings/TS-10.md), [TS-11](findings/TS-11.md), [TS-12](findings/TS-12.md), [TS-13](findings/TS-13.md), [TS-14](findings/TS-14.md), [TS-15](findings/TS-15.md), [TS-18](findings/TS-18.md), [HTK-01](findings/HTK-01.md), [HTK-02](findings/HTK-02.md), [TMR-01](findings/TMR-01.md), [TMR-02](findings/TMR-02.md), [TMR-04](findings/TMR-04.md), [TMR-06](findings/TMR-06.md), [TMR-08](findings/TMR-08.md), [PC-01](findings/PC-01.md), [QTD-02](findings/QTD-02.md), [QRC-N01](findings/QRC-N01.md), [SET-02](findings/SET-02.md), [IMP-NEW-05](findings/IMP-NEW-05.md), [CMB-N01](findings/CMB-N01.md), [CMB-N02](findings/CMB-N02.md), [SCRL-N03](findings/SCRL-N03.md), [IMG-N01](findings/IMG-N01.md), [ACT-N05](findings/ACT-N05.md), [PLAT-N03](findings/PLAT-N03.md), [EVT-N10](findings/EVT-N10.md), [STATE-N01](findings/STATE-N01.md), [STATE-N04](findings/STATE-N04.md), [XFRM-N01](findings/XFRM-N01.md), [KEY-N01](findings/KEY-N01.md), [LINK-N04](findings/LINK-N04.md), [FLOW-N02](findings/FLOW-N02.md), [TXT-CRIT](findings/TXT-CRIT.md), [PATH-N03](findings/PATH-N03.md), [REGEX-CRIT-01](findings/REGEX-CRIT-01.md), [GSW-N02](findings/GSW-N02.md), [SETUP-N01](findings/SETUP-N01.md), [WATCH-N03](findings/WATCH-N03.md), [COERC-N01](findings/COERC-N01.md), [EVT-N13](findings/EVT-N13.md), [DEB-N02](findings/DEB-N02.md), [DEB-N03](findings/DEB-N03.md), [TS-N07](findings/TS-N07.md), [META-N14](findings/META-N14.md), [META-N16](findings/META-N16.md), [META-N17](findings/META-N17.md), [TMR-N05](findings/TMR-N05.md), [FONT-METRIC-01](findings/FONT-METRIC-01.md), [STC-N03](findings/STC-N03.md), [RESP-N02](findings/RESP-N02.md), [SHAPE-N02](findings/SHAPE-N02.md), [SCR-N01](findings/SCR-N01.md)

</details>

<details><summary>Done — 1</summary>

[AND-CRIT-01](findings/AND-CRIT-01.md)

</details>
