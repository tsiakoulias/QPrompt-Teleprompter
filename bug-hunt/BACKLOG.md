# Bug-Hunt Backlog

Work queue: OPEN tickets the max-rigor reviewer (`opus-ultra`) confirms as LEGIT, ranked by severity then corroboration (number of the 6 agents that also called it LEGIT). Each row links to its full ticket in `findings/`.

Status tally: FIXED 2 · NEEDS-INFO 63 · OPEN 588 · REJECTED 70.

**494 actionable OPEN findings.**

| # | Sev | Corrob. | ID | Title |
|---|---|---|---|---|
| 1 | Critical | 6/6 | [001-CUR-N01](findings/001-CUR-N01.md) | replaceAll() infinite loop when replacement contains search pattern |
| 2 | Critical | 6/6 | [002-EDGE-04](findings/002-EDGE-04.md) | Null pointer dereference: `document()->textDocument()` not checked before `load()` |
| 3 | Critical | 6/6 | [003-EDGE-05](findings/003-EDGE-05.md) | Null pointer dereference: `textDocument()` unchecked in `search()` |
| 4 | Critical | 6/6 | [004-EDGE-06](findings/004-EDGE-06.md) | Null pointer dereference: `textDocument()` unchecked in `parse()` |
| 5 | Critical | 6/6 | [005-FINAL-01](findings/005-FINAL-01.md) | TimerClock references undefined `timer` id — ETA and stopwatch completely broken |
| 6 | Critical | 6/6 | [006-FINAL-03](findings/006-FINAL-03.md) | Missing breeze-icons submodule — fresh clone cannot build |
| 7 | Critical | 6/6 | [007-R3-CTX-01](findings/007-R3-CTX-01.md) | AbstractUnits missing QML_ELEMENT — all duration constants resolve to undefined |
| 8 | Critical | 6/6 | [008-R3-DOC-01](findings/008-R3-DOC-01.md) | m_reloading uninitialized — undefined behavior on first load |
| 9 | Critical | 6/6 | [009-R4-CMT-01](findings/009-R4-CMT-01.md) | PDF import completely broken — converter invocation commented out |
| 10 | Critical | 6/6 | [010-SEC-01](findings/010-SEC-01.md) | Arbitrary Command Execution via `sys://` Marker URIs |
| 11 | Critical | 6/6 | [011-STK-N01](findings/011-STK-N01.md) | Android projectionManager undefined — crash on "Performance tweaks" submenu |
| 12 | Critical | 6/6 | [012-W10-PLF-01](findings/012-W10-PLF-01.md) | BSD detection broken — FreeBSD enters wrong code paths |
| 13 | Critical | 5/6 | [013-AND-BLD-01](findings/013-AND-BLD-01.md) | Missing version.gradle — Gradle build fails |
| 14 | Critical | 5/6 | [014-QML-03](findings/014-QML-03.md) | Undefined `root` ID in WindowDragger.qml |
| 15 | Critical | 5/6 | [015-R2-AND-02](findings/015-R2-AND-02.md) | Android missing restartDialog crashes LanguageSettingsOverlay and LayoutDirectionSettingsOverlay |
| 16 | Critical | 5/6 | [016-W10-DEP-01](findings/016-W10-DEP-01.md) | Missing vcpkg.json manifest — vcpkg manifest mode installs nothing |
| 17 | Critical | 4/6 | [017-R2-AND-01](findings/017-R2-AND-01.md) | Android missing QmlUtil causes crash on factory reset and RecentDocuments |
| 18 | Critical | 4/6 | [018-R4-EXP-01](findings/018-R4-EXP-01.md) | No XSS sanitization — script tags, event handlers, javascript: URLs unfiltered |
| 19 | Critical | 4/6 | [019-W10-WSM-01](findings/019-W10-WSM-01.md) | Infinite reload loop on unauthorized WASM host — app unusable |
| 20 | High | 6/6 | [020-AND-HIGH-02](findings/020-AND-HIGH-02.md) | Android screen never sleeps after prompter use |
| 21 | High | 6/6 | [021-AND-HIGH-03](findings/021-AND-HIGH-03.md) | factoryReset() quits Android app without restarting |
| 22 | High | 6/6 | [022-CUR-N02](findings/022-CUR-N02.md) | search() regex path ignores loop parameter — unconditional wrap |
| 23 | High | 6/6 | [023-DEB-N01](findings/023-DEB-N01.md) | libvulkan-dev (dev package) listed as Debian runtime dependency |
| 24 | High | 6/6 | [024-DLG-N01](findings/024-DLG-N01.md) | document.modified=false set BEFORE saveAs() — failed save loses unsaved flag |
| 25 | High | 6/6 | [025-DLG-N02](findings/025-DLG-N02.md) | onError handler clears document.modified on save failure |
| 26 | High | 6/6 | [026-DLG-N06](findings/026-DLG-N06.md) | import() error strings passed as document content via updateContents() |
| 27 | High | 6/6 | [027-EDGE-01](findings/027-EDGE-01.md) | QString::arg() called on string with no placeholder — program name silently dropped |
| 28 | High | 6/6 | [028-EDGE-02](findings/028-EDGE-02.md) | Empty container `first()` dereference — crash on hotkey with no windows |
| 29 | High | 6/6 | [029-EDGE-03](findings/029-EDGE-03.md) | Empty container `last()` dereference in `extendLastMarker` |
| 30 | High | 6/6 | [030-FINAL-05](findings/030-FINAL-05.md) | WindowDragger mouse delta accumulation error — window moves farther than cursor |
| 31 | High | 6/6 | [031-FINAL-08](findings/031-FINAL-08.md) | setup.sh vcvarsall.bat executed from bash — MSVC env not propagated |
| 32 | High | 6/6 | [032-FINAL-11](findings/032-FINAL-11.md) | onFrameSwapped calls grabToImage every frame — severe performance hit |
| 33 | High | 6/6 | [033-IMG-N02](findings/033-IMG-N02.md) | insertHtmlAt() silent blocking HTTP load for img src URLs — UI freeze |
| 34 | High | 6/6 | [034-IO-N02](findings/034-IO-N02.md) | save() constructs QUrl without file:// scheme — broken on non-Windows |
| 35 | High | 6/6 | [035-JSN-01](findings/035-JSN-01.md) | i.d.authentication accessed without undefined guard |
| 36 | High | 6/6 | [036-JSON-N01](findings/036-JSON-N01.md) | OBS WebSocket Hello auth fields accessed without null guard — crash on auth-disabled |
| 37 | High | 6/6 | [037-LINK-N01](findings/037-LINK-N01.md) | Qt::Network not linked on iOS static build — unresolved symbols |
| 38 | High | 6/6 | [038-LINK-N02](findings/038-LINK-N02.md) | Qt::Network not linked on WASM static build — same as LINK-N01 |
| 39 | High | 6/6 | [039-LOG-01](findings/039-LOG-01.md) | SessionModel::rowCount returns m_data.size() for both valid and invalid parents |
| 40 | High | 6/6 | [040-LOG-02](findings/040-LOG-02.md) | Off-by-one: beginRemoveRows uses rowCount() instead of rowCount()-1 |
| 41 | High | 6/6 | [041-MATH-N01](findings/041-MATH-N01.md) | Division by zero in __timeToArival/__timeToEnd when speed=0 |
| 42 | High | 6/6 | [042-MEM-01](findings/042-MEM-01.md) | Memory Leak: `_markersModel` allocated without parent, never deleted |
| 43 | High | 6/6 | [043-MEM-02](findings/043-MEM-02.md) | Memory Leak: `_fileSystemWatcher` allocated without parent, never deleted |
| 44 | High | 6/6 | [044-NET-01](findings/044-NET-01.md) | loadFromNetworkFinihed never checks m_reply->error() |
| 45 | High | 6/6 | [045-PROP-N01](findings/045-PROP-N01.md) | on__FullScreenChanged handler casing mismatch — never fires |
| 46 | High | 6/6 | [046-QML-04](findings/046-QML-04.md) | Typo: `verticalCentertop` instead of `verticalCenter` |
| 47 | High | 6/6 | [047-QML-05](findings/047-QML-05.md) | `&&` should be `\|\|` in clear button enabled condition |
| 48 | High | 6/6 | [048-QML-06](findings/048-QML-06.md) | Bitwise OR (`\|`) instead of AND (`&`) in modifier key check |
| 49 | High | 6/6 | [049-QML-BND-01](findings/049-QML-BND-01.md) | countdownAnimation.running binding permanently broken after first iteration |
| 50 | High | 6/6 | [050-R2-WHE-01](findings/050-R2-WHE-01.md) | `focus: true` is JavaScript label, not assignment |
| 51 | High | 6/6 | [051-R3-CTX-02](findings/051-R3-CTX-02.md) | GlobalHotkeys.SkipForward enum value mismatch — trailing 's' missing |
| 52 | High | 6/6 | [052-R3-DOC-03](findings/052-R3-DOC-03.md) | load() sets m_fileUrl and emits fileUrlChanged even on failed load |
| 53 | High | 6/6 | [053-R3-DOC-04](findings/053-R3-DOC-04.md) | saveAs() silently ignores write/flush failures |
| 54 | High | 6/6 | [054-R3-DOC-05](findings/054-R3-DOC-05.md) | updateContents() produces two separate undo entries — undo destroys document |
| 55 | High | 6/6 | [055-R3-DOC-07](findings/055-R3-DOC-07.md) | Inverted selection state after failed search() |
| 56 | High | 6/6 | [056-R4-EXP-02](findings/056-R4-EXP-02.md) | insertHtmlAt() bypasses filterHtml() — unsanitized HTML from QML |
| 57 | High | 6/6 | [057-R4-EXP-03](findings/057-R4-EXP-03.md) | loadFromNetwork() destroys URL for relative URLs — host/path swapped |
| 58 | High | 6/6 | [058-R4-EXP-04](findings/058-R4-EXP-04.md) | AutoText inserts plain text as HTML — content corruption |
| 59 | High | 6/6 | [059-R4-ROOT-01](findings/059-R4-ROOT-01.md) | Qt.openUrlExternally called with translation context string instead of URL |
| 60 | High | 6/6 | [060-REGEX-CRIT-02](findings/060-REGEX-CRIT-02.md) | searchRegEx.setPattern() from user input — isValid() never called |
| 61 | High | 6/6 | [061-RES-01](findings/061-RES-01.md) | Network reply overwritten without aborting previous download |
| 62 | High | 6/6 | [062-RES-02](findings/062-RES-02.md) | loadFromNetworkFinihed ignores the QNetworkReply* signal parameter |
| 63 | High | 6/6 | [063-STR-N01](findings/063-STR-N01.md) | main.cpp:158 QLatin1String iterator-pair UB from two unrelated string literals |
| 64 | High | 6/6 | [064-W10-CNV2-01](findings/064-W10-CNV2-01.md) | Default stylesheet has invalid CSS color quoting — exported HTML broken in browsers |
| 65 | High | 6/6 | [065-W10-CNV2-02](findings/065-W10-CNV2-02.md) | No markdown export — round-trip silently destroys all formatting |
| 66 | High | 6/6 | [066-W10-HTK-02](findings/066-W10-HTK-02.md) | QHotkey::setShortcut return value silently ignored — no failure detection |
| 67 | High | 6/6 | [067-WSM-N01](findings/067-WSM-N01.md) | Synchronous QImage::load() from HTTP blocks WASM main thread |
| 68 | High | 5/6 | [068-LYR-N01](findings/068-LYR-N01.md) | InputsOverlay calls cursorAutoHide.restart() on open instead of reset() |
| 69 | High | 5/6 | [069-PLAT-03](findings/069-PLAT-03.md) | Wrong target name and wrong include path for KDMacTouchBar |
| 70 | High | 5/6 | [070-QP-N01](findings/070-QP-N01.md) | restartApplication() quits even when startDetached fails — app dies with no replacement |
| 71 | High | 5/6 | [071-R2-CMAKE-02](findings/071-R2-CMAKE-02.md) | cmake_minimum_required inside find module pollutes parent project policy settings |
| 72 | High | 5/6 | [072-R2-EDT-02](findings/072-R2-EDT-02.md) | wheelThrottleSettingsButton checked bound to completely unrelated document property |
| 73 | High | 5/6 | [073-R2-EDT-03](findings/073-R2-EDT-03.md) | Checkable ToolButtons break checked property bindings on first click — systematic |
| 74 | High | 5/6 | [074-R3-MAIN-06](findings/074-R3-MAIN-06.md) | Inconsistent Kirigami platform guards — missing WATCHOS and QNX |
| 75 | High | 5/6 | [075-R4-EVT-03](findings/075-R4-EVT-03.md) | CursorAutoHide null access on root.pageStack.currentItem during page transitions |
| 76 | High | 5/6 | [076-SAVE-N02](findings/076-SAVE-N02.md) | iOS save flow never updates C++ m_fileUrl — file URL perpetually stale |
| 77 | High | 5/6 | [077-SHADOW-N03](findings/077-SHADOW-N03.md) | id: stopwatch shadows property bool stopwatch — timersEnabled always true |
| 78 | High | 5/6 | [078-UNIT-01](findings/078-UNIT-01.md) | ProgressIndicator.qml:46 Units.ShortDuration with no Kirigami import |
| 79 | High | 5/6 | [079-UNIT-02](findings/079-UNIT-02.md) | PrompterView.qml 7x Units.ShortDuration with no Kirigami import |
| 80 | High | 4/6 | [080-AND-HIGH-01](findings/080-AND-HIGH-01.md) | Android back button doesn't dismiss overlays/drawers before close |
| 81 | High | 4/6 | [081-EVT-03](findings/081-EVT-03.md) | velocityDragOverlay (z:7) steals clicks from control buttons (z:6) |
| 82 | High | 4/6 | [082-EVT-04](findings/082-EVT-04.md) | Drag breaks editor.x declarative binding permanently |
| 83 | High | 4/6 | [083-EVT-05](findings/083-EVT-05.md) | Drag breaks positionHandler.x declarative binding permanently |
| 84 | High | 4/6 | [084-FINAL-06](findings/084-FINAL-06.md) | CMAKE_OSX_ARCHITECTURES contains literal quotes — universal binary broken |
| 85 | High | 4/6 | [085-HK-N01](findings/085-HK-N01.md) | Missing event.isAutoRepeat guard on main Keys.onPressed |
| 86 | High | 4/6 | [086-HTK-03](findings/086-HTK-03.md) | KGlobalAccel defaults silently zeroed on non-Wayland when QHotkey co-exists |
| 87 | High | 4/6 | [087-PLAT-01](findings/087-PLAT-01.md) | KF6Crash_FOUND never defined as C preprocessor macro — KCrash support dead code |
| 88 | High | 4/6 | [088-R2-IOS-01](findings/088-R2-IOS-01.md) | Method swizzling re-entry causes infinite recursion on second invocation |
| 89 | High | 4/6 | [089-R3-MAIN-02](findings/089-R3-MAIN-02.md) | Invalid locale string constructed for short language codes |
| 90 | High | 4/6 | [090-R3-PMT-01](findings/090-R3-PMT-01.md) | OBS WebSocket JSON.parse without try/catch — crash on malformed input |
| 91 | High | 4/6 | [091-R4-ROV-01](findings/091-R4-ROV-01.md) | Division by zero in __customPlacement when overlay full |
| 92 | High | 4/6 | [092-R4-ROV-02](findings/092-R4-ROV-02.md) | Drag permanently breaks y property binding on readRegion |
| 93 | High | 4/6 | [093-THM-SYS](findings/093-THM-SYS.md) | Complete theme deadlock — 50+ Material.theme: Dark hardcoded, theme toggle commented out |
| 94 | High | 4/6 | [094-TRF-N01](findings/094-TRF-N01.md) | rightWidthAdjustmentBar drag.maximumX formula broken — drag collapses to single point |
| 95 | High | 4/6 | [095-W10-PLF-02](findings/095-W10-PLF-02.md) | QHotkey_FOUND never set in FetchContent path — built but never linked |
| 96 | High | 4/6 | [096-W10-SWT-01](findings/096-W10-SWT-01.md) | CloseActions switch drops RecentLocal/RecentRemote — recent document open silently lost after save |
| 97 | High | 4/6 | [097-W10-SWT-02](findings/097-W10-SWT-02.md) | Same bug in IosSaveDialog.onAccepted path |
| 98 | High | 3/6 | [098-EVT-01](findings/098-EVT-01.md) | velocityDragArea (z:5) blocks viewport.mouse (z:0) wheel events |
| 99 | High | 3/6 | [099-FINAL-04](findings/099-FINAL-04.md) | NSIS start-menu shortcut icon name mismatches actual binary name |
| 100 | High | 3/6 | [100-HK-N03](findings/100-HK-N03.md) | platformName() != "wayland" fails on "wayland-egl" — global hotkeys dead |
| 101 | High | 3/6 | [101-W10-CLP-01](findings/101-W10-CLP-01.md) | Paste-without-formatting fails when clipboard lacks text/plain |
| 102 | High | 3/6 | [102-W10-CNV2-03](findings/102-W10-CNV2-03.md) | import() uses fromStdString on non-Windows — encoding corruption |
| 103 | High | 3/6 | [103-WSM-03](findings/103-WSM-03.md) | readAsDataURL causes quadruple in-memory copy of file content |
| 104 | High | 2/6 | [104-W10-PMV-01](findings/104-W10-PMV-01.md) | font.pixelSize evaluates to 0 before first layout pass — crash hazard |
| 105 | Medium | 6/6 | [105-AND-N08](findings/105-AND-N08.md) | Android saveAs() hardcodes isHtml=true — plain-text files saved with HTML markup |
| 106 | Medium | 6/6 | [106-ANM-N01](findings/106-ANM-N01.md) | Easing.EaseOut is not a valid Qt Quick easing type (2 instances) |
| 107 | Medium | 6/6 | [107-API-N02](findings/107-API-N02.md) | selectionIsLowerCase NOTIFY signal is wrong — fontCapitalizationChanged, never emitted for case changes |
| 108 | Medium | 6/6 | [108-BLD-05](findings/108-BLD-05.md) | .env.android references Qt 5.15.2 — project requires Qt 6.8.2+ |
| 109 | Medium | 6/6 | [109-CAST-N01](findings/109-CAST-N01.md) | setFontCapitalization static_cast with no range validation — reachable from QML |
| 110 | Medium | 6/6 | [110-CMAKE-N04](findings/110-CMAKE-N04.md) | Relative ../build path in install rules — out-of-tree build failure |
| 111 | Medium | 6/6 | [111-CMAKE-NEW-02](findings/111-CMAKE-NEW-02.md) | Duplicate install() of appdata.xml/desktop in root and src/CMakeLists.txt |
| 112 | Medium | 6/6 | [112-CMAKE-NEW-03](findings/112-CMAKE-NEW-03.md) | find_package(KF6Crash ... COMPONENTS) — COMPONENTS keyword with zero names |
| 113 | Medium | 6/6 | [113-CMAKE-NEW-04](findings/113-CMAKE-NEW-04.md) | execute_process uses CMAKE_PREFIX_PATH (list) as scalar — broken command |
| 114 | Medium | 6/6 | [114-CMB-N03](findings/114-CMB-N03.md) | LanguageSettingsOverlay ListView currentIndex always -1 — wrong indexOf() call |
| 115 | Medium | 6/6 | [115-COERC-N02](findings/115-COERC-N02.md) | Unvalidated string-to-number injects NaN into root.__opacity — all opacity dead |
| 116 | Medium | 6/6 | [116-COMP-N02](findings/116-COMP-N02.md) | Case-sensitive suffix check misses mixed-case extensions — silent format loss |
| 117 | Medium | 6/6 | [117-CUR-N03](findings/117-CUR-N03.md) | alignment() reads blockFormat on multi-block selection — returns wrong alignment |
| 118 | Medium | 6/6 | [118-DCL-N01](findings/118-DCL-N01.md) | filterHtml default parameter in .cpp but not in header — QML can't call with 1 arg |
| 119 | Medium | 6/6 | [119-DCL-N02](findings/119-DCL-N02.md) | setKeyMarker default parameter mismatch — same pattern |
| 120 | Medium | 6/6 | [120-DLG-N04](findings/120-DLG-N04.md) | load() silently fails with no notification when file missing or unreadable |
| 121 | Medium | 6/6 | [121-DLG-N05](findings/121-DLG-N05.md) | loadFromNetworkFinihed() silently ignores empty response |
| 122 | Medium | 6/6 | [122-DPR-N01](findings/122-DPR-N01.md) | Prompter.qml uses Screen.devicePixelRatio (global) instead of screen.devicePixelRatio (window) |
| 123 | Medium | 6/6 | [123-EDGE-09](findings/123-EDGE-09.md) | QFile::copy() return value silently ignored |
| 124 | Medium | 6/6 | [124-ENC-01](findings/124-ENC-01.md) | truncate(-1) when font preview text has no spaces |
| 125 | Medium | 6/6 | [125-ERR-N01](findings/125-ERR-N01.md) | removeCustomWord() silently drops dictionary languages on partial reload failure |
| 126 | Medium | 6/6 | [126-EVT-07](findings/126-EVT-07.md) | TabBar currentIndex binding broken on first TabButton click |
| 127 | Medium | 6/6 | [127-EVT-08](findings/127-EVT-08.md) | Two additional checkable ToolButton binding breakage instances |
| 128 | Medium | 6/6 | [128-FINAL-12](findings/128-FINAL-12.md) | SystemFontChooserDialog setWindowFlags strips all decorations |
| 129 | Medium | 6/6 | [129-FINAL-13](findings/129-FINAL-13.md) | Invalid Korean locale code "ko_KO" — should be "ko_KR" |
| 130 | Medium | 6/6 | [130-FINAL-17](findings/130-FINAL-17.md) | ScriptAction references non-existent function `paintReady` |
| 131 | Medium | 6/6 | [131-FINAL-18](findings/131-FINAL-18.md) | MarkersModel extendLastMarker modifies data without emitting dataChanged |
| 132 | Medium | 6/6 | [132-FINAL-21](findings/132-FINAL-21.md) | clearProperty(AnchorHref/AnchorName) ineffective through mergeCharFormat |
| 133 | Medium | 6/6 | [133-FLOW-N01](findings/133-FLOW-N01.md) | setKeyMarker() calls setAnchor("#") — const char*→bool conversion, href never set |
| 134 | Medium | 6/6 | [134-FMT-N01](findings/134-FMT-N01.md) | Step Speed onAccepted displays 100x correct value |
| 135 | Medium | 6/6 | [135-FMT-N02](findings/135-FMT-N02.md) | Step Acceleration onAccepted — identical 100x display bug |
| 136 | Medium | 6/6 | [136-HK-N02](findings/136-HK-N02.md) | Typo Qt.Key_VolumeDowm — "Dowm" instead of "Down" — volume-down hardware key dead |
| 137 | Medium | 6/6 | [137-HK-N05](findings/137-HK-N05.md) | Strict === equality on modifiers breaks user keybinds with NumLock |
| 138 | Medium | 6/6 | [138-HTK-04](findings/138-HTK-04.md) | Wrong enum type `Qt::KeyboardModifier` (singular) for modifier variable |
| 139 | Medium | 6/6 | [139-INIT-N01](findings/139-INIT-N01.md) | Velocity modifier ComboBox model has 2 entries, switch handles 4 cases |
| 140 | Medium | 6/6 | [140-IO-N03](findings/140-IO-N03.md) | iossavedialog.mm QFile::write() return value unchecked |
| 141 | Medium | 6/6 | [141-LOG-03](findings/141-LOG-03.md) | MarkersModel::data returns data.position for LengthRole instead of data.length |
| 142 | Medium | 6/6 | [142-LOG-05](findings/142-LOG-05.md) | DocumentHandler::search ignores `loop` parameter when `regEx` is true |
| 143 | Medium | 6/6 | [143-LOG-N06](findings/143-LOG-N06.md) | No error log when saveAs() write/flush fail — silent data loss |
| 144 | Medium | 6/6 | [144-MATH-N02](findings/144-MATH-N02.md) | Bitwise << on floating-point in TimerClock — precision loss |
| 145 | Medium | 6/6 | [145-MEM-03](findings/145-MEM-03.md) | Memory Leak: `m_fontDialog` allocated without parent, never deleted |
| 146 | Medium | 6/6 | [146-MIME-N02](findings/146-MIME-N02.md) | loadFromNetworkFinihed() ignores Content-Type header — all network content treated as HTML |
| 147 | Medium | 6/6 | [147-MIME-N03](findings/147-MIME-N03.md) | PDF/EPUB/MOBI/AZW MIME-detected but import is no-op — error text becomes content |
| 148 | Medium | 6/6 | [148-MOB-01](findings/148-MOB-01.md) | Android: projectionManager undefined — 3 unguarded reference sites |
| 149 | Medium | 6/6 | [149-MODEL-N01](findings/149-MODEL-N01.md) | MarkersModel::rowCount ignores parent.isValid() — returns full size for child probe |
| 150 | Medium | 6/6 | [150-NET-N04](findings/150-NET-N04.md) | No transfer timeout on any QNetworkRequest |
| 151 | Medium | 6/6 | [151-NET-N05](findings/151-NET-N05.md) | loadFromNetwork() hardcodes http:// scheme — never upgrades to HTTPS |
| 152 | Medium | 6/6 | [152-NOTIFY-01](findings/152-NOTIFY-01.md) | setAutoReload doesn't emit autoReloadChanged NOTIFY signal |
| 153 | Medium | 6/6 | [153-PARSE-N02](findings/153-PARSE-N02.md) | MarkersModel::keySearch() hits=1 limits search to first marker only |
| 154 | Medium | 6/6 | [154-PATH-N02](findings/154-PATH-N02.md) | reload() constructs file:// URL via raw string concat — #/? in filenames break URL |
| 155 | Medium | 6/6 | [155-PLAT-02](findings/155-PLAT-02.md) | REQUIRED_KF6_VERSION variable referenced but never defined |
| 156 | Medium | 6/6 | [156-PLAT-N04](findings/156-PLAT-N04.md) | "ipados" is not valid Qt.platform.os string — 18 dead guards across 5 files |
| 157 | Medium | 6/6 | [157-QML-BND-02](findings/157-QML-BND-02.md) | clock.__iteration binding broken by post-decrement in animation handler |
| 158 | Medium | 6/6 | [158-QP-N02](findings/158-QP-N02.md) | convert.waitForFinished() blocks GUI thread up to 30s during LibreOffice import |
| 159 | Medium | 6/6 | [159-QP-N03](findings/159-QP-N03.md) | convert.exitCode() never checked — LibreOffice error output becomes document content |
| 160 | Medium | 6/6 | [160-QTD-01](findings/160-QTD-01.md) | m_spellHighlighter not detached when setDocument(nullptr) |
| 161 | Medium | 6/6 | [161-R2-ANDMAN-01](findings/161-R2-ANDMAN-01.md) | Ungrantable system/signature permissions bloating manifest |
| 162 | Medium | 6/6 | [162-R2-CMAKE-04](findings/162-R2-CMAKE-04.md) | QML icon file(GLOB_RECURSE) missing CONFIGURE_DEPENDS causes stale icon sets |
| 163 | Medium | 6/6 | [163-R2-FONT-01](findings/163-R2-FONT-01.md) | RichText label renders unescaped plain text — HTML metacharacters break display |
| 164 | Medium | 6/6 | [164-R2-IOS-03](findings/164-R2-IOS-03.md) | UIApplication.keyWindow deprecated since iOS 13; breaks multi-window iPadOS |
| 165 | Medium | 6/6 | [165-R2-PTH-01](findings/165-R2-PTH-01.md) | FileDialog filter matches all files on Linux due to stray glob |
| 166 | Medium | 6/6 | [166-R2-PTH-02](findings/166-R2-PTH-02.md) | File path from file:// URL preserves percent-encoding |
| 167 | Medium | 6/6 | [167-R3-DOC-06](findings/167-R3-DOC-06.md) | reload() leaks m_reloading=true on URL mismatch |
| 168 | Medium | 6/6 | [168-R3-MAIN-03](findings/168-R3-MAIN-03.md) | System locale changed even when translation file fails to load |
| 169 | Medium | 6/6 | [169-R3-MAIN-07](findings/169-R3-MAIN-07.md) | XDG_CURRENT_DESKTOP unconditionally forced to "KDE" on all Linux |
| 170 | Medium | 6/6 | [170-R3-PMT-02](findings/170-R3-PMT-02.md) | OBS WebSocket no onError handler, no reconnection logic |
| 171 | Medium | 6/6 | [171-R3-SPL-04](findings/171-R3-SPL-04.md) | Corrupt cached dictionary file persists permanently after failed copy |
| 172 | Medium | 6/6 | [172-R4-EXP-05](findings/172-R4-EXP-05.md) | No encoding/charset detection — all imports assumed UTF-8 |
| 173 | Medium | 6/6 | [173-R4-EXP-06](findings/173-R4-EXP-06.md) | UTF-8 BOM not stripped — becomes phantom character at position 0 |
| 174 | Medium | 6/6 | [174-R4-EXP-07](findings/174-R4-EXP-07.md) | data: URI assumes base64 encoding without checking ;base64 token |
| 175 | Medium | 6/6 | [175-R4-EXP-08](findings/175-R4-EXP-08.md) | EPUB/MOBI/AZW import replaces document with error string |
| 176 | Medium | 6/6 | [176-R4-PRJ-03](findings/176-R4-PRJ-03.md) | setScreensModel() duplicates display entries on each toggle cycle |
| 177 | Medium | 6/6 | [177-R4-PRJ-04](findings/177-R4-PRJ-04.md) | Division by zero in projection image height |
| 178 | Medium | 6/6 | [178-R4-ROOT-02](findings/178-R4-ROOT-02.md) | Invalid QML color value "initial" |
| 179 | Medium | 6/6 | [179-R4-ROOT-04](findings/179-R4-ROOT-04.md) | Duplicate "&Open" menu item in native File menu |
| 180 | Medium | 6/6 | [180-REGEX-N02](findings/180-REGEX-N02.md) | regex_5 accidentally excludes 15+ HTML5 tags from background-color filtering |
| 181 | Medium | 6/6 | [181-REGEX-N06](findings/181-REGEX-N06.md) | imgSrcRegex captures wrong src when data-src follows real src |
| 182 | Medium | 6/6 | [182-SAVE-N03](findings/182-SAVE-N03.md) | saveAs() never updates _fileSystemWatcher — watches stale file after save-as |
| 183 | Medium | 6/6 | [183-SCR-N02](findings/183-SCR-N02.md) | Duplicate entries in displayModel on first toggle — no clear() before setScreensModel() |
| 184 | Medium | 6/6 | [184-SEC-02](findings/184-SEC-02.md) | OBS WebSocket Password Stored in Plaintext |
| 185 | Medium | 6/6 | [185-SEC-03](findings/185-SEC-03.md) | Information Disclosure: Full HTML Document Content Logged via qDebug |
| 186 | Medium | 6/6 | [186-SHAPE-N01](findings/186-SHAPE-N01.md) | pointer_0.qml PathLine parent.width resolves to undefined (ShapePath has no width) — arrow collapsed |
| 187 | Medium | 6/6 | [187-SHDR-N01](findings/187-SHDR-N01.md) | Math.cos/Math.sin used with degrees value — shadow offset diagonal instead of horizontal |
| 188 | Medium | 6/6 | [188-SIZE-N01](findings/188-SIZE-N01.md) | concentricCircles Shape has conflicting anchors.fill + anchors.centerIn |
| 189 | Medium | 6/6 | [189-SPL2-11](findings/189-SPL2-11.md) | addCustomWord trims but removeCustomWord does not — asymmetry |
| 190 | Medium | 6/6 | [190-SPL2-12](findings/190-SPL2-12.md) | Case-sensitive contains/indexOf but case-insensitive sort — duplicates |
| 191 | Medium | 6/6 | [191-SPL2-13](findings/191-SPL2-13.md) | saveCustomWordsToDisk has void return — callers cannot detect I/O failure |
| 192 | Medium | 6/6 | [192-SPL2-14](findings/192-SPL2-14.md) | Cached QRC dicts never invalidated after app update |
| 193 | Medium | 6/6 | [193-SPL2-15](findings/193-SPL2-15.md) | spell() returns true when no dicts loaded — silent no-op |
| 194 | Medium | 6/6 | [194-SWT-N01](findings/194-SWT-N01.md) | OBS WebSocket Switch checked binding broken on first toggle |
| 195 | Medium | 6/6 | [195-TRL-N02](findings/195-TRL-N02.md) | Application --help description not translatable |
| 196 | Medium | 6/6 | [196-TXT-N03](findings/196-TXT-N03.md) | Toolbar paste and Edit menu paste bypass HTML sanitization |
| 197 | Medium | 6/6 | [197-WYS-N01](findings/197-WYS-N01.md) | Internal drag-and-drop copy inserts HTML as plain text — tags become visible |
| 198 | Medium | 6/6 | [198-XML-N01](findings/198-XML-N01.md) | android:background="#303030" invalid on \<activity\> — silently ignored |
| 199 | Medium | 5/6 | [199-ACT-N07](findings/199-ACT-N07.md) | namedBookmarkButton: checkable button opens dialog — stale indicator after first click |
| 200 | Medium | 5/6 | [200-API-N01](findings/200-API-N01.md) | setAlignment() missing null-cursor guard — crash risk with no document |
| 201 | Medium | 5/6 | [201-API-N03](findings/201-API-N03.md) | CursorAutoHide.qml unconditionally dereferences pageStack.currentItem.prompter |
| 202 | Medium | 5/6 | [202-BLK-N02](findings/202-BLK-N02.md) | updateContents() fails to reset block formatting — stale formats contaminate new document |
| 203 | Medium | 5/6 | [203-BLK-N03](findings/203-BLK-N03.md) | setLineHeight/setParagraphHeight apply document-wide — destroy per-block customization |
| 204 | Medium | 5/6 | [204-CLIP-N04](findings/204-CLIP-N04.md) | Image-only clipboard paste — button enabled but does nothing |
| 205 | Medium | 5/6 | [205-CMT-N08](findings/205-CMT-N08.md) | Entire Telemetry class is dead commented-out shell across 4 files |
| 206 | Medium | 5/6 | [206-DBG-N01](findings/206-DBG-N01.md) | OBS WebSocket auth challenge+salt logged to console in release builds |
| 207 | Medium | 5/6 | [207-DLG-N10](findings/207-DLG-N10.md) | TimerClock ColorDialog selectedColor never initialized from persisted settings |
| 208 | Medium | 5/6 | [208-DPI-04](findings/208-DPI-04.md) | InputsOverlay.qml:33 height:680 hardcoded |
| 209 | Medium | 5/6 | [209-DSZ-01](findings/209-DSZ-01.md) | InputsOverlay hardcoded height:680 — overflows on phones |
| 210 | Medium | 5/6 | [210-DSZ-02](findings/210-DSZ-02.md) | pointerConfiguration OverlaySheet no vertical ScrollView |
| 211 | Medium | 5/6 | [211-ENUM-01](findings/211-ENUM-01.md) | documenthandler.cpp:1108 updateContents switch no default — silent data loss |
| 212 | Medium | 5/6 | [212-FINAL-09](findings/212-FINAL-09.md) | `on__IChanged` handler typo — never fires |
| 213 | Medium | 5/6 | [213-FINAL-19](findings/213-FINAL-19.md) | Encoding fallback uses toLocal8Bit() instead of dictionary's actual encoding |
| 214 | Medium | 5/6 | [214-INT-N04](findings/214-INT-N04.md) | OBS URL/Password fields disabled when WebSocket enabled — inverted logic |
| 215 | Medium | 5/6 | [215-INT-N05](findings/215-INT-N05.md) | PropertyChanges permanently destroys CheckBox checked bindings on PointerSettings tab switch |
| 216 | Medium | 5/6 | [216-INV-N01](findings/216-INV-N01.md) | QmlUtil::r() stores QML-owned QQuickItemGrabResult raw pointer — use-after-free |
| 217 | Medium | 5/6 | [217-IO-N01](findings/217-IO-N01.md) | saveAs() leaves _fileSystemWatcher permanently blocked on open failure |
| 218 | Medium | 5/6 | [218-JSN-02](findings/218-JSN-02.md) | ws.sendTextMessage() called without checking WebSocket status |
| 219 | Medium | 5/6 | [219-LINK-N03](findings/219-LINK-N03.md) | Qt::WebSockets found as REQUIRED but never explicitly linked |
| 220 | Medium | 5/6 | [220-LOAD-N01](findings/220-LOAD-N01.md) | TOCTOU race between QFile::exists() and file.open() in load() |
| 221 | Medium | 5/6 | [221-LOG-04](findings/221-LOG-04.md) | MarkersModel::extendLastMarker modifies data without emitting dataChanged |
| 222 | Medium | 5/6 | [222-LOG-06](findings/222-LOG-06.md) | DocumentHandler::replaceAll has potential infinite loop with regex |
| 223 | Medium | 5/6 | [223-LOG-N07](findings/223-LOG-N07.md) | No error log in loadFromNetworkFinihed() — silent bad-data load |
| 224 | Medium | 5/6 | [224-LYR-N04](findings/224-LYR-N04.md) | ESC handler uses activeFocus in base but focus in platform variants — inconsistent |
| 225 | Medium | 5/6 | [225-MENU-N01](findings/225-MENU-N01.md) | contextMenu.popup(this) missing click coordinates — menu at wrong position |
| 226 | Medium | 5/6 | [226-MENU-N02](findings/226-MENU-N02.md) | Mobile "Add to dictionary" missing %1 placeholder — word never shown |
| 227 | Medium | 5/6 | [227-MOB-02](findings/227-MOB-02.md) | No +ios/ QML selector — iOS inherits base main.qml with desktop-only components |
| 228 | Medium | 5/6 | [228-MOB-03](findings/228-MOB-03.md) | iOS: IosSaveDialog silently hangs QML caller when temp dir invalid |
| 229 | Medium | 5/6 | [229-OOB-N01](findings/229-OOB-N01.md) | MarkersModel::data() — m_data.at() without row < rowCount() guard |
| 230 | Medium | 5/6 | [230-OOB-N02](findings/230-OOB-N02.md) | SessionModel::data() — same missing row bounds guard |
| 231 | Medium | 5/6 | [231-OPC-01](findings/231-OPC-01.md) | Right-click toggle desynchronizes velocityIndicator visible/opacity |
| 232 | Medium | 5/6 | [232-PARSE-N01](findings/232-PARSE-N01.md) | insertImageAt() stores image resource with file:// key but looks up via plain path |
| 233 | Medium | 5/6 | [233-PATH-N01](findings/233-PATH-N01.md) | save() fragile percent-encoding round-trip — broken for UNC paths |
| 234 | Medium | 5/6 | [234-PLAT-05](findings/234-PLAT-05.md) | DBINARY_ICONS_RESOURCE is a typo — should be BINARY_ICONS_RESOURCE |
| 235 | Medium | 5/6 | [235-POP-N04](findings/235-POP-N04.md) | CountdownConfiguration SpinBoxes use focus: true (JS label) instead of focus = true |
| 236 | Medium | 5/6 | [236-PP-N01](findings/236-PP-N01.md) | Q_OS_APPLE is not a Qt macro — KGlobalAccel block compiles on all Unix including macOS |
| 237 | Medium | 5/6 | [237-QLOAD-N01](findings/237-QLOAD-N01.md) | InputsOverlay toggleButtonsOff() null-check bypass — crash on slow async Loaders |
| 238 | Medium | 5/6 | [238-R2-AND-03](findings/238-R2-AND-03.md) | Android Settings missing fakeFullScreen persistence |
| 239 | Medium | 5/6 | [239-R2-ANDMAN-02](findings/239-R2-ANDMAN-02.md) | MANAGE_EXTERNAL_STORAGE likely triggers Play Store scrutiny |
| 240 | Medium | 5/6 | [240-R2-CMAKE-03](findings/240-R2-CMAKE-03.md) | WORKING_DIRECTORY and COMMENT not parseable by callers of sphinx_add_docs |
| 241 | Medium | 5/6 | [241-R2-EDT-01](findings/241-R2-EDT-01.md) | Qt.AlignHustify typo — nonexistent enum value |
| 242 | Medium | 5/6 | [242-R2-PRP-01](findings/242-R2-PRP-01.md) | Qt.LeftToRight used as bare boolean — RTL branch always dead |
| 243 | Medium | 5/6 | [243-R2-PRP-02](findings/243-R2-PRP-02.md) | Kirigami.Units.SmallSpacing — uppercase S yields undefined |
| 244 | Medium | 5/6 | [244-R2-PTR-03](findings/244-R2-PTR-03.md) | Casing error: Units.longDuration should be Units.LongDuration |
| 245 | Medium | 5/6 | [245-R2-PTR-04](findings/245-R2-PTR-04.md) | Inverted indexOf truthiness in platform check for ColorDialog |
| 246 | Medium | 5/6 | [246-R2-TEL-01](findings/246-R2-TEL-01.md) | Telemetry sub-toggles permanently disconnect from master toggle on click |
| 247 | Medium | 5/6 | [247-R2-WASM-02](findings/247-R2-WASM-02.md) | Insecure hostname validation via endsWith allows subdomain spoofing |
| 248 | Medium | 5/6 | [248-R3-MAIN-05](findings/248-R3-MAIN-05.md) | Hardcoded Homebrew version-specific Kirigami import path |
| 249 | Medium | 5/6 | [249-R3-PROP-01](findings/249-R3-PROP-01.md) | selectionIsLowerCase bound to wrong NOTIFY signal |
| 250 | Medium | 5/6 | [250-R3-SPL-01](findings/250-R3-SPL-01.md) | encode() uses toLocal8Bit() instead of dictionary-encoding-aware conversion |
| 251 | Medium | 5/6 | [251-R3-SPL-02](findings/251-R3-SPL-02.md) | decode() uses fromLocal8Bit() — suggestions show as mojibake |
| 252 | Medium | 5/6 | [252-R4-BKG-01](findings/252-R4-BKG-01.md) | Flip transform origin stays at (0,0) when Flip stored as property |
| 253 | Medium | 5/6 | [253-R4-EVT-02](findings/253-R4-EVT-02.md) | Velocity modifier ComboBox lists 2 options but switch handles 4 — dead code |
| 254 | Medium | 5/6 | [254-R4-ROV-03](findings/254-R4-ROV-03.md) | Bitwise OR \| used for width fallback instead of logical OR |
| 255 | Medium | 5/6 | [255-REGEX-N04](findings/255-REGEX-N04.md) | ReDoS — user-supplied regex has no length limit, timeout, or backtracking guard |
| 256 | Medium | 5/6 | [256-RENDER-01](findings/256-RENDER-01.md) | ShaderEffectSource prompterShadowSource runs unconditionally — wastes GPU capture when shadows disabled |
| 257 | Medium | 5/6 | [257-RENDER-02](findings/257-RENDER-02.md) | ShaderEffectSource pointerShadowSource runs unconditionally — same pattern |
| 258 | Medium | 5/6 | [258-RPM-N01](findings/258-RPM-N01.md) | RPM dependencies entirely commented out — zero automatic dependency resolution |
| 259 | Medium | 5/6 | [259-SAVE-N01](findings/259-SAVE-N01.md) | loadFromNetworkFinihed sets m_fileUrl to phantom QTemporaryFile path |
| 260 | Medium | 5/6 | [260-SCALE-N01](findings/260-SCALE-N01.md) | Right pointer xScale: -1 mirrors text pointers — backwards/unreadable text |
| 261 | Medium | 5/6 | [261-ST-N02](findings/261-ST-N02.md) | Dead overlay.state PropertyChanges — overlay has no states array |
| 262 | Medium | 5/6 | [262-STATE-N02](findings/262-STATE-N02.md) | Find.toggle() uses !visible instead of !isOpen — can't close during Prompting |
| 263 | Medium | 5/6 | [263-STC-N01](findings/263-STC-N01.md) | closeAll() destroys user's per-screen projection flip configuration |
| 264 | Medium | 5/6 | [264-TMR-N06](findings/264-TMR-N06.md) | Auto-reload Timer persists after network dialog close — background refetches |
| 265 | Medium | 5/6 | [265-TRL-N03](findings/265-TRL-N03.md) | About-dialog credit roles not translatable |
| 266 | Medium | 5/6 | [266-TXT-FMT-N01](findings/266-TXT-FMT-N01.md) | setMarkerHref("") fails to clear QTextFormat::AnchorHref — stale href persists |
| 267 | Medium | 5/6 | [267-TYP-04](findings/267-TYP-04.md) | Bitwise AND on bools hides dead code in preventSleep |
| 268 | Medium | 5/6 | [268-TYP-05](findings/268-TYP-05.md) | Uninitialized pointer member m_reply in DocumentHandler |
| 269 | Medium | 5/6 | [269-UNIT-03](findings/269-UNIT-03.md) | PrompterBackground.qml:160 Units.LongDuration no Kirigami import |
| 270 | Medium | 5/6 | [270-UNIT-04](findings/270-UNIT-04.md) | Flip.qml:34,41 two Units.LongDuration no Kirigami import |
| 271 | Medium | 5/6 | [271-URL-N01](findings/271-URL-N01.md) | reload() constructs file:// URL by string concatenation without encoding |
| 272 | Medium | 5/6 | [272-URL-N03](findings/272-URL-N03.md) | Network-loaded HTML lacks base URL — relative resources broken |
| 273 | Medium | 5/6 | [273-URL-N05](findings/273-URL-N05.md) | openFromRemote() blindly prepends http:// to non-HTTP schemes |
| 274 | Medium | 5/6 | [274-UTF-N01](findings/274-UTF-N01.md) | text.truncate(64) can split UTF-16 surrogate pairs — corrupted display |
| 275 | Medium | 5/6 | [275-WATCH-N01](findings/275-WATCH-N01.md) | addPath() return never checked — silent watch failure |
| 276 | Medium | 5/6 | [276-WATCH-N02](findings/276-WATCH-N02.md) | removePath() return never checked — stale path causes double-watch |
| 277 | Medium | 4/6 | [277-AND-MED-01](findings/277-AND-MED-01.md) | Missing intent-filter for opening files from other apps |
| 278 | Medium | 4/6 | [278-AND-RES-01](findings/278-AND-RES-01.md) | Invalid android:scaleType on bitmap element |
| 279 | Medium | 4/6 | [279-ANM-N02](findings/279-ANM-N02.md) | Standby→Ready countdown opacity flash — PropertyChanges opacity:1 conflicts with dissolveIn |
| 280 | Medium | 4/6 | [280-BLK-N01](findings/280-BLK-N01.md) | alignment() returns Qt::AlignCenter (includes vertical bit 0x0080) on null cursor |
| 281 | Medium | 4/6 | [281-CFG-N01](findings/281-CFG-N01.md) | Desktop MimeType incomplete — only text/html, missing text/plain and text/markdown |
| 282 | Medium | 4/6 | [282-CLP-N01](findings/282-CLP-N01.md) | Copy/Cut exports unfiltered HTML to system clipboard |
| 283 | Medium | 4/6 | [283-CLP-N02](findings/283-CLP-N02.md) | DropArea external drop never calls drop.accept() |
| 284 | Medium | 4/6 | [284-CLP-N03](findings/284-CLP-N03.md) | DropArea external drop: URLs consumed preferentially — text silently lost |
| 285 | Medium | 4/6 | [285-CMAKE-N03](findings/285-CMAKE-N03.md) | qt_wrap_ui conflicts with global AUTOUIC — double UI processing |
| 286 | Medium | 4/6 | [286-COLOR-01](findings/286-COLOR-01.md) | ProjectionsManager.qml uses invalid "initial" color — repro of R4-ROOT-02 |
| 287 | Medium | 4/6 | [287-COLOR-02](findings/287-COLOR-02.md) | Hardcoded #EED text invisible on light themes — WheelSettingsOverlay |
| 288 | Medium | 4/6 | [288-COLOR-N08](findings/288-COLOR-N08.md) | textBackground() returns invalid QColor for body/paragraph text |
| 289 | Medium | 4/6 | [289-COLOR-N09](findings/289-COLOR-N09.md) | acceptedColor binds transparent QColor on startup — initial text invisible |
| 290 | Medium | 4/6 | [290-DEF-N02](findings/290-DEF-N02.md) | DropArea internalDrag always false — internal drag handler dead code |
| 291 | Medium | 4/6 | [291-ERR-N02](findings/291-ERR-N02.md) | insertImageAt() async callback silently discards 3 failure modes |
| 292 | Medium | 4/6 | [292-EVT-06](findings/292-EVT-06.md) | Drag breaks stopwatch.x binding permanently |
| 293 | Medium | 4/6 | [293-FD-N01](findings/293-FD-N01.md) | \|\| should be && in autoReload guard — user preference ignored for non-binary files |
| 294 | Medium | 4/6 | [294-FONT-METRIC-02](findings/294-FONT-METRIC-02.md) | FontLoader status never checked — font substitution silently fails |
| 295 | Medium | 4/6 | [295-GEO-02](findings/295-GEO-02.md) | main.qml persists x/y/width/height with zero validation |
| 296 | Medium | 4/6 | [296-GSW-N01](findings/296-GSW-N01.md) | MarkersDrawer SwipeListItem navigates on swipe — gesture conflict on touch |
| 297 | Medium | 4/6 | [297-HK-N04](findings/297-HK-N04.md) | No auto-repeat guard in key-binding configuration Keys.onPressed |
| 298 | Medium | 4/6 | [298-HSCROLL-N01](findings/298-HSCROLL-N01.md) | InputsOverlay Flickables use contentWidth: width instead of implicitWidth — horizontal overflow clipped |
| 299 | Medium | 4/6 | [299-HSCROLL-N02](findings/299-HSCROLL-N02.md) | Inner Flickables missing flickableDirection: VerticalFlick — conflict with parent horizontal ListView |
| 300 | Medium | 4/6 | [300-JS-N02](findings/300-JS-N02.md) | markerCompare() per-frame JSON.stringify() over OBS marker — 60 allocs/sec |
| 301 | Medium | 4/6 | [301-LDR-N01](findings/301-LDR-N01.md) | InputsOverlay typeof null guard fails — null.item crash on rapid close |
| 302 | Medium | 4/6 | [302-LL-N01](findings/302-LL-N01.md) | 10 EditorToolbar MouseArea/TextField width-depends-on-width binding loops |
| 303 | Medium | 4/6 | [303-LOG-N05](findings/303-LOG-N05.md) | Q_UNREACHABLE() in m_setGlobalShortcut() — UB in release on new enum value |
| 304 | Medium | 4/6 | [304-LYR-N02](findings/304-LYR-N02.md) | Three OverlaySheets missing from ESC dismiss chain |
| 305 | Medium | 4/6 | [305-MENU-N03](findings/305-MENU-N03.md) | Text alignment menu RTL swap: labels swap but actions don't |
| 306 | Medium | 4/6 | [306-META-N15](findings/306-META-N15.md) | No StartupWMClass in desktop file — duplicate dock entries, missing icon |
| 307 | Medium | 4/6 | [307-PERF-N02](findings/307-PERF-N02.md) | RecentDocuments._load() blocks startup with N synchronous createObject() calls |
| 308 | Medium | 4/6 | [308-POP-N01](findings/308-POP-N01.md) | ESC cascade missing dictionariesSheet — undismissable by keyboard |
| 309 | Medium | 4/6 | [309-POP-N02](findings/309-POP-N02.md) | ESC cascade missing customWordsSheet — undismissable by keyboard |
| 310 | Medium | 4/6 | [310-POP-N03](findings/310-POP-N03.md) | ESC cascade missing obsConfiguration — undismissable by keyboard despite alias |
| 311 | Medium | 4/6 | [311-QML-11](findings/311-QML-11.md) | Dead code: `window` property declared but never used in WindowDragger |
| 312 | Medium | 4/6 | [312-QW-N01](findings/312-QW-N01.md) | Projection Window onClosing references cleared model — spurious runtime errors |
| 313 | Medium | 4/6 | [313-QW-N02](findings/313-QW-N02.md) | Stale QScreen reference in projection model — dangling after monitor hot-unplug |
| 314 | Medium | 4/6 | [314-R2-WASM-01](findings/314-R2-WASM-01.md) | File input element never removed from DOM on user cancel |
| 315 | Medium | 4/6 | [315-RESO-N01](findings/315-RESO-N01.md) | Editing font size not viewport-scaled — text nearly unreadable on 4K |
| 316 | Medium | 4/6 | [316-SAFE-01](findings/316-SAFE-01.md) | +android/main.qml zero safe area insets |
| 317 | Medium | 4/6 | [317-SAFE-02](findings/317-SAFE-02.md) | ReadRegionOverlay screenMiddle ignores notch/status bar height |
| 318 | Medium | 4/6 | [318-SCR-N03](findings/318-SCR-N03.md) | No runtime screen plug/unplug handling — stale projection windows on disconnected screens |
| 319 | Medium | 4/6 | [319-SCRL-N02](findings/319-SCRL-N02.md) | __destination typed int truncates real-valued position |
| 320 | Medium | 4/6 | [320-SHDR-N02](findings/320-SHDR-N02.md) | id: shadow collides with property ShaderEffectSource shadow — ambiguous resolution in blur chain |
| 321 | Medium | 4/6 | [321-SHT-N01](findings/321-SHT-N01.md) | markerToggle/namedMarkerToggle forwarded but never handled — dead hotkeys |
| 322 | Medium | 4/6 | [322-STC-N04](findings/322-STC-N04.md) | Projection window CursorAutoHide not reset on close — cursor permanently hidden |
| 323 | Medium | 4/6 | [323-TAB-N01](findings/323-TAB-N01.md) | PointerSettings TabButton onClicked skips currentIndex assignment |
| 324 | Medium | 4/6 | [324-TB-N01](findings/324-TB-N01.md) | toolbar toggle timers produce stale state on rapid clicks |
| 325 | Medium | 4/6 | [325-TB-N02](findings/325-TB-N02.md) | baseSpeedSlider/baseAccelerationSlider onMoved yanks focus to prompter instead of restoreFocus() |
| 326 | Medium | 4/6 | [326-TBND-N01](findings/326-TBND-N01.md) | SpellHighlighter regex excludes combining diacritical marks — NFD text misspelled |
| 327 | Medium | 4/6 | [327-TMR-03](findings/327-TMR-03.md) | dissolveIn animation re-triggered entering Running from Ready — flicker |
| 328 | Medium | 4/6 | [328-TMR-N01](findings/328-TMR-N01.md) | resetBackground Timer not stopped when new background loaded — race erases new image |
| 329 | Medium | 4/6 | [329-TMR-N02](findings/329-TMR-N02.md) | Windows onFrameSwapped missing qmlutil.r(p) — per-frame grab result leak |
| 330 | Medium | 4/6 | [330-TOG-N01](findings/330-TOG-N01.md) | WheelSettingsOverlay useScrollAsDialButton — cross-path stale checked state |
| 331 | Medium | 4/6 | [331-TP-N01](findings/331-TP-N01.md) | "Error loading file..." used as document content, not placeholderText |
| 332 | Medium | 4/6 | [332-TXT-N04](findings/332-TXT-N04.md) | goToNextMarker() temporarily sets cursorPosition=-1 — corrupts cursor state |
| 333 | Medium | 4/6 | [333-UNIT-06](findings/333-UNIT-06.md) | Find.qml:92 Units.ShortDuration with namespaced Kirigami import |
| 334 | Medium | 4/6 | [334-UNIT-07](findings/334-UNIT-07.md) | ReadRegionOverlay.qml 3x Units.ShortDuration with namespaced import |
| 335 | Medium | 4/6 | [335-VIS-N05](findings/335-VIS-N05.md) | velocityDragOverlay blocks all interaction during indicator fade-out (~500ms dead zone) |
| 336 | Medium | 4/6 | [336-W10-CLP-02](findings/336-W10-CLP-02.md) | Remote image URLs in pasted HTML cause unsanctioned network requests |
| 337 | Medium | 4/6 | [337-W10-WSM-02](findings/337-W10-WSM-02.md) | Global file-picker state overwritten by re-entrant calls — wrong file delivered |
| 338 | Medium | 4/6 | [338-WINDOW-N01](findings/338-WINDOW-N01.md) | Projection windows not closed on main window close — orphaned on Linux |
| 339 | Medium (masked — Labs.MenuBar dead per IMP-N01) | 3/6 | [339-ACT-N08](findings/339-ACT-N08.md) | All checkable Labs.MenuItems inherit R2-EDT-03 binding-break pattern |
| 340 | Medium (latent) | 3/6 | [340-AND-MFT-01](findings/340-AND-MFT-01.md) | FileProvider resource @xml/qtprovider_paths — file named filepaths.xml |
| 341 | Medium | 3/6 | [341-CLI-N01](findings/341-CLI-N01.md) | --version flag non-functional — version string empty when parser processes |
| 342 | Medium | 3/6 | [342-DPI-01](findings/342-DPI-01.md) | TimerClock.qml:127 devicePixelRatio in raw arithmetic with magic multiplier |
| 343 | Medium | 3/6 | [343-DRW-01](findings/343-DRW-01.md) | interalFocusElsewhere() misses 3 OverlaySheets + 2 Drawers — hotkeys pass through |
| 344 | Medium | 3/6 | [344-DRW-02](findings/344-DRW-02.md) | globalDrawer and contextDrawer missing from ESC dismiss chain |
| 345 | Medium | 3/6 | [345-KB-N01](findings/345-KB-N01.md) | Find.qml: 9 toolbar buttons missing focusPolicy — keyboard-invisible |
| 346 | Medium | 3/6 | [346-KB-N02](findings/346-KB-N02.md) | InputsOverlay TabBar TabButtons have no focusPolicy + keyNavigationEnabled: false — keyboard dead |
| 347 | Medium | 3/6 | [347-KB-N03](findings/347-KB-N03.md) | +windows and +android ESC handler uses .focus instead of .activeFocus — wrong boolean |
| 348 | Medium | 3/6 | [348-LAZY-N02](findings/348-LAZY-N02.md) | InputsOverlay ObjectModel eagerly loads both tabs — hidden tab content loaded prematurely |
| 349 | Medium | 3/6 | [349-R2-OVL-01](findings/349-R2-OVL-01.md) | InputsOverlay onOpened calls cursorAutoHide.restart() instead of reset() |
| 350 | Medium | 3/6 | [350-R2-REC-02](findings/350-R2-REC-02.md) | refreshExistence skips UI updates when dynamic children out of sync |
| 351 | Medium | 3/6 | [351-RAII-N03](findings/351-RAII-N03.md) | QProcess orphan — child process detached on waitForFinished() timeout |
| 352 | Medium | 3/6 | [352-TB-N04](findings/352-TB-N04.md) | velocityDragArea accepts MiddleButton without propagateComposedEvents — scroll blocked |
| 353 | Medium | 3/6 | [353-TBND-N02](findings/353-TBND-N02.md) | All CJK text marked misspelled — ideographic characters not in Hunspell dictionaries |
| 354 | Medium | 3/6 | [354-W10-PMV-02](findings/354-W10-PMV-02.md) | Circular ShaderEffectSource dependency — shadow ghost on first frame |
| 355 | Low | 6/6 | [355-CMAKE-N02](findings/355-CMAKE-N02.md) | INTERFACE_LINK_LIBRARIES on executable target — no-op |
| 356 | Low | 6/6 | [356-CMAKE-N05](findings/356-CMAKE-N05.md) | foreach(file IN LISTS icon_files doc) — "doc" never defined |
| 357 | Low | 6/6 | [357-COMP-N01](findings/357-COMP-N01.md) | Case-sensitive duplicate detection in setLanguages() |
| 358 | Low | 6/6 | [358-DISK-N01](findings/358-DISK-N01.md) | saveCustomWordsToDisk() non-atomic write — data loss on power failure |
| 359 | Low | 6/6 | [359-ENC-02](findings/359-ENC-02.md) | getMarkerKey() mid(4) without length/startsWith guard |
| 360 | Low | 6/6 | [360-FOC-N01](findings/360-FOC-N01.md) | focus: true is JS label in atEndLoopDelay SpinBox |
| 361 | Low | 6/6 | [361-FOC-N02](findings/361-FOC-N02.md) | Same JS label bug in countdownConfiguration SpinBoxes (2 instances) |
| 362 | Low | 6/6 | [362-INIT-N02](findings/362-INIT-N02.md) | Find.qml SearchField placeholderText always empty — no guidance text |
| 363 | Low | 6/6 | [363-MA-N02](findings/363-MA-N02.md) | textDragArea missing cursorShape — ArrowCursor over IBeamCursor on editor |
| 364 | Low | 6/6 | [364-MOB-04](findings/364-MOB-04.md) | Android: restartApplication() quits without restart |
| 365 | Low | 6/6 | [365-MOB-05](findings/365-MOB-05.md) | Android: Missing INTERNET permission in manifest |
| 366 | Low | 6/6 | [366-MOB-06](findings/366-MOB-06.md) | Android: PrompterPage display delegate Component.onCompleted references projectionManager — startup TypeError |
| 367 | Low | 6/6 | [367-PLAT-06](findings/367-PLAT-06.md) | qprompt_QM_LOADER variable never defined |
| 368 | Low | 6/6 | [368-QCN-01](findings/368-QCN-01.md) | O(n²) contains()-in-loop during custom words file load |
| 369 | Low | 6/6 | [369-R2-FONT-02](findings/369-R2-FONT-02.md) | Duplicate setText call on preview label |
| 370 | Low | 6/6 | [370-R3-SIG-01](findings/370-R3-SIG-01.md) | textChanged() signal declared but never emitted |
| 371 | Low | 6/6 | [371-REGEX-N03](findings/371-REGEX-N03.md) | Unescaped dot in font-size regex — matches any char instead of decimal |
| 372 | Low | 6/6 | [372-REGEX-N05](findings/372-REGEX-N05.md) | regex_0 and regex_3 use . (any-char) instead of \. (literal dot) in decimal matching |
| 373 | Low | 6/6 | [373-SAVE-N05](findings/373-SAVE-N05.md) | save() broken on Android content:// URIs — empty filename |
| 374 | Low | 6/6 | [374-SCRL-N04](findings/374-SCRL-N04.md) | __speed non-zero when __i=0 and __curvature=0 (Math.pow(0,0)===1) |
| 375 | Low | 6/6 | [375-SIZE-N02](findings/375-SIZE-N02.md) | Three Button children of Row have dead anchors.bottom declarations |
| 376 | Low | 6/6 | [376-SPL2-16](findings/376-SPL2-16.md) | QDir::mkpath return unchecked — dict cache directory may silently not exist |
| 377 | Low | 6/6 | [377-SPL2-17](findings/377-SPL2-17.md) | QFile::setPermissions return unchecked — cached dict may be unreadable |
| 378 | Low | 6/6 | [378-SPL2-19](findings/378-SPL2-19.md) | availableDictionaries enumerates .dic without verifying .aff exists |
| 379 | Low | 6/6 | [379-TBND-N03](findings/379-TBND-N03.md) | extendLastMarker() doesn't update Marker::length field — stale after appends |
| 380 | Low | 6/6 | [380-TC-N01](findings/380-TC-N01.md) | Image.source assigned boolean false instead of empty string |
| 381 | Low | 6/6 | [381-TIME-N01](findings/381-TIME-N01.md) | copyrightYear computed then discarded — stale "2020-2026" in About after 2026 |
| 382 | Low | 6/6 | [382-TMR-05](findings/382-TMR-05.md) | ScriptAction `paintReady` references non-existent function |
| 383 | Low | 6/6 | [383-TRN-N01](findings/383-TRN-N01.md) | Dead ternary: both branches return Qt.OpenHandCursor |
| 384 | Low | 6/6 | [384-TYP-N01](findings/384-TYP-N01.md) | Misspelled method name: loadFromNetworkFinihed (missing 's') |
| 385 | Low | 6/6 | [385-TYP-N02](findings/385-TYP-N02.md) | Misspelled parameter: withoutFormating (missing 't') |
| 386 | Low | 6/6 | [386-TYP-N05](findings/386-TYP-N05.md) | Uninitialized member m_documentComesFromNetwork |
| 387 | Low | 6/6 | [387-WSM-N02](findings/387-WSM-N02.md) | WASM preventSleep() falls through to desktop #else — always returns false |
| 388 | Low | 5/6 | [388-API-N05](findings/388-API-N05.md) | fileName()/fileType() return fabricated defaults — can't distinguish "no file" from "untitled.html" |
| 389 | Low | 5/6 | [389-API-N06](findings/389-API-N06.md) | SystemFontChooserDialog::show() calls setText() on same label twice — dead code |
| 390 | Low | 5/6 | [390-API-N07](findings/390-API-N07.md) | SpellChecker::encode() fallback says "Latin-1" but calls toLocal8Bit() |
| 391 | Low | 5/6 | [391-CFG-N03](findings/391-CFG-N03.md) | "fixedd" typo in v2.0.2 release description |
| 392 | Low | 5/6 | [392-CMAKE-NEW-01](findings/392-CMAKE-NEW-01.md) | Remote.qml exists on disk but never listed in QML_FILES |
| 393 | Low | 5/6 | [393-DBG-N02](findings/393-DBG-N02.md) | Velocity debug logging active in production |
| 394 | Low | 5/6 | [394-DBG-N04](findings/394-DBG-N04.md) | qDebug() in namedMarker()/setMarker() active in release |
| 395 | Low | 5/6 | [395-DLG-N03](findings/395-DLG-N03.md) | errorDialog MessageDialog has no title |
| 396 | Low | 5/6 | [396-DLG-N07](findings/396-DLG-N07.md) | 5 showPassiveNotification() calls ignore passiveNotifications preference |
| 397 | Low | 5/6 | [397-DLG-N08](findings/397-DLG-N08.md) | 3 save-completion passive notifications lack passiveNotifications guard |
| 398 | Low | 5/6 | [398-DLG-N11](findings/398-DLG-N11.md) | PrompterPage ColorDialogs — dead acceptedColor property binding |
| 399 | Low | 5/6 | [399-DRAG-N02](findings/399-DRAG-N02.md) | textDragArea has no cursorShape — no cursor feedback during text drag |
| 400 | Low | 5/6 | [400-FONT-N02](findings/400-FONT-N02.md) | FontLoader id typo: westernSeriousSansfFont — stray 'f' in "Sans" |
| 401 | Low | 5/6 | [401-HDR-N01](findings/401-HDR-N01.md) | promptsession.h not in CMakeLists.txt — SessionModel/DataPoint dead code |
| 402 | Low | 5/6 | [402-HDR-N02](findings/402-HDR-N02.md) | telemetry.h not in CMakeLists.txt — Telemetry dead code |
| 403 | Low | 5/6 | [403-JS-N01](findings/403-JS-N01.md) | TIMERCLOCK getTimeString() — redundant .toString() on already-string — 54 allocs/sec |
| 404 | Low | 5/6 | [404-LOG-08](findings/404-LOG-08.md) | DataPoint default constructor leaves three members uninitialized |
| 405 | Low | 5/6 | [405-MA-N01](findings/405-MA-N01.md) | overlayMouseArea permanently disabled — dead MouseArea |
| 406 | Low | 5/6 | [406-MENU-N04](findings/406-MENU-N04.md) | Trailing empty MenuSeparator at end of mobile context menu |
| 407 | Low | 5/6 | [407-MODEL-N02](findings/407-MODEL-N02.md) | SessionModel::clearDataPoints lacks empty-model guard before beginRemoveRows |
| 408 | Low | 5/6 | [408-NET-N06](findings/408-NET-N06.md) | loadFromNetwork() validates original URL, not constructed resultingUrl |
| 409 | Low | 5/6 | [409-NOTIFY-02](findings/409-NOTIFY-02.md) | availableDictionariesChanged NOTIFY signal never emitted |
| 410 | Low | 5/6 | [410-R2-OVL-02](findings/410-R2-OVL-02.md) | LanguageSettingsOverlay popup ListView currentIndex always resolves to -1 |
| 411 | Low | 5/6 | [411-R3-MAIN-08](findings/411-R3-MAIN-08.md) | QFontDatabase::addApplicationFont return value discarded |
| 412 | Low | 5/6 | [412-SPL2-18](findings/412-SPL2-18.md) | Hunspell::add return value unchecked at 4 call sites |
| 413 | Low | 5/6 | [413-UNIT-05](findings/413-UNIT-05.md) | pointer_0.qml:72 Units.VeryLongDuration no Kirigami import |
| 414 | Low | 5/6 | [414-URL-N04](findings/414-URL-N04.md) | loadFromNetwork() validates wrong URL instance |
| 415 | Low | 5/6 | [415-WARN-N02](findings/415-WARN-N02.md) | SpellChecker::addWord() — dead public API, never called |
| 416 | Low | 5/6 | [416-WARN-N04](findings/416-WARN-N04.md) | QProcess::startDetached() bool return silently ignored |
| 417 | Low | 5/6 | [417-WATCH-N04](findings/417-WATCH-N04.md) | unblockFileWatcher() dereferences _fileSystemWatcher without null guard |
| 418 | Low | 5/6 | [418-WYS-N02](findings/418-WYS-N02.md) | Default stylesheet CSS errors: valign:top (not a CSS property) and border:1pt (missing style) |
| 419 | Low | 4/6 | [419-API-N04](findings/419-API-N04.md) | setMarker(bool) misleadingly named — sets regular marker, not any marker |
| 420 | Low | 4/6 | [420-CFG-N02](findings/420-CFG-N02.md) | v1.1.3 release date "2022-1-16" breaks chronological order — should be 2023-01-16 |
| 421 | Low | 4/6 | [421-COERC-N03](findings/421-COERC-N03.md) | real→int truncation in WindowDragger position compounds drift |
| 422 | Low | 4/6 | [422-DRAG-N01](findings/422-DRAG-N01.md) | Image resize body drag: cursor shows OpenHandCursor until drag threshold exceeded |
| 423 | Low | 4/6 | [423-FOC-N03](findings/423-FOC-N03.md) | Tab/Backtab asymmetry — Backtab silently unhandled |
| 424 | Low | 4/6 | [424-GEO-03](findings/424-GEO-03.md) | +android/main.qml no minimumWidth/minimumHeight |
| 425 | Low | 4/6 | [425-HK-N06](findings/425-HK-N06.md) | isValidInput checks local keybindings only — silent conflict with global hotkeys |
| 426 | Low | 4/6 | [426-LAZY-N01](findings/426-LAZY-N01.md) | namedMarkerConfiguration Loader double-loads KeyInputButton — first load wasted |
| 427 | Low | 4/6 | [427-LL-N02](findings/427-LL-N02.md) | ProgressIndicator stepSize divide-by-zero when prompter.height is 0 |
| 428 | Low | 4/6 | [428-LVW-N01](findings/428-LVW-N01.md) | InputsOverlay.qml ListView currentIndex: PointerSettings.States.Arrow — copy-paste error |
| 429 | Low | 4/6 | [429-MENU-N05](findings/429-MENU-N05.md) | "Redo" context menu item missing & accelerator |
| 430 | Low | 4/6 | [430-META-N01](findings/430-META-N01.md) | QMetaObject::invokeMethod return value unchecked — silent failure on WASM |
| 431 | Low | 4/6 | [431-PLAT-07](findings/431-PLAT-07.md) | Incorrect macro syntax: `#define Use_GlobalAccel = 1` |
| 432 | Low | 4/6 | [432-PLAT-N05](findings/432-PLAT-N05.md) | Base main.qml fullScreenPlatform missing "wasm" (inconsistent with +windows) |
| 433 | Low | 4/6 | [433-QF-N02](findings/433-QF-N02.md) | QDir::entryList missing QDir::Readable in availableDictionaries() |
| 434 | Low | 4/6 | [434-QF-N03](findings/434-QF-N03.md) | TOCTOU: QFile::exists() → QFile::copy() in resource cache extraction |
| 435 | Low | 4/6 | [435-QRC-N02](findings/435-QRC-N02.md) | Four .qrc files are dead code — never referenced by CMakeLists.txt |
| 436 | Low | 4/6 | [436-R2-REC-01](findings/436-R2-REC-01.md) | File URI prefix strip off-by-one on Windows |
| 437 | Low | 4/6 | [437-RAII-N02](findings/437-RAII-N02.md) | IosSaveDialog::m_tempDir created unconditionally on all platforms — wasted I/O |
| 438 | Low | 4/6 | [438-RESO-N02](findings/438-RESO-N02.md) | Scrollbar width 6dp-13dp — below minimum 44dp touch target |
| 439 | Low | 4/6 | [439-RESO-N05](findings/439-RESO-N05.md) | PointerSettings ListView height hardcoded 180dp — doesn't fill available space |
| 440 | Low | 4/6 | [440-RND-N02](findings/440-RND-N02.md) | Missing smooth: true on background Image — aliased upscale |
| 441 | Low | 4/6 | [441-RND-N03](findings/441-RND-N03.md) | Missing smooth: true on projection Image — aliased text on external displays |
| 442 | Low | 4/6 | [442-SHADOW-01](findings/442-SHADOW-01.md) | id: rotation shadows Item.rotation property |
| 443 | Low | 4/6 | [443-SHADOW-02](findings/443-SHADOW-02.md) | id: flow shadows Flow.flow property |
| 444 | Low | 4/6 | [444-STATE-N03](findings/444-STATE-N03.md) | Countdown Running restarts dissolveIn unnecessarily — visual dim-to-bright flash |
| 445 | Low | 4/6 | [445-STC-N05](findings/445-STC-N05.md) | cancel() doesn't call timer.stopTimer() — elapsed time persists across sessions |
| 446 | Low | 4/6 | [446-TXT-N02](findings/446-TXT-N02.md) | TimerClock default text color #AAA on #131619 — fails WCAG AA contrast |
| 447 | Low | 4/6 | [447-TYP-06](findings/447-TYP-06.md) | Malformed preprocessor macro: `#define Use_GlobalAccel = 1` |
| 448 | Low | 4/6 | [448-TYP-07](findings/448-TYP-07.md) | Narrowing conversion: `size_t` → `int` in SpellChecker::decode |
| 449 | Low | 4/6 | [449-VIS-FB-N01](findings/449-VIS-FB-N01.md) | bookmarkListButton and searchButton missing checkable: true — no checked background |
| 450 | Low | 4/6 | [450-WARN-N01](findings/450-WARN-N01.md) | SpellHighlighter::isEnabled() — dead code, never called |
| 451 | Low | 3/6 | [451-ACT-N06](findings/451-ACT-N06.md) | +windows main.qml Performance tweaks missing enableBarsSetting |
| 452 | Low | 3/6 | [452-BIND-N01](findings/452-BIND-N01.md) | contentWidth undefined for Shape/Image pointer types — transform origin silently wrong |
| 453 | Low | 3/6 | [453-CNTD-N01](findings/453-CNTD-N01.md) | Countdown Running: dissolveIn and dissolveOut compete for same opacity when __iterations===__disappearWithin===1 |
| 454 | Low | 3/6 | [454-COLOR-04](findings/454-COLOR-04.md) | ReadRegionOverlay ColorAnimation tracks __fillColor that never changes |
| 455 | Low | 3/6 | [455-DPI-02](findings/455-DPI-02.md) | MarkersDrawer.qml:37 drawer minimumWidth hardcoded to 260px |
| 456 | Low | 3/6 | [456-DPI-03](findings/456-DPI-03.md) | Find.qml:38 searchBarWidth:724 hardcoded in px |
| 457 | Low | 3/6 | [457-EVT-09](findings/457-EVT-09.md) | Flow ToolSeparator visibility compares y of potentially invisible rows |
| 458 | Low | 3/6 | [458-EVT-10](findings/458-EVT-10.md) | Nested MouseAreas with hoverEnabled steal hover from parent Buttons |
| 459 | Low | 3/6 | [459-GEO-01](findings/459-GEO-01.md) | main.qml initial 728px height too large for 1366x768 laptops |
| 460 | Low | 3/6 | [460-LBL-N03](findings/460-LBL-N03.md) | PrompterView 3× height overflow in theforce debug mode |
| 461 | Low | 3/6 | [461-LOAD-N02](findings/461-LOAD-N02.md) | reset() emits 12 NOTIFY signals when open() fails but exists() succeeds |
| 462 | Low | 3/6 | [462-ORIENT-N01](findings/462-ORIENT-N01.md) | TimerClock binary width>height orientation creates sharp 2x font jump at 1:1 |
| 463 | Low | 3/6 | [463-R2-AND-04](findings/463-R2-AND-04.md) | Android Settings for "background" missing transparency persistence |
| 464 | Low | 3/6 | [464-R2-AND-05](findings/464-R2-AND-05.md) | Android loadTelemetryPage passes no properties object to pageStack push |
| 465 | Low | 3/6 | [465-R2-PRP-05](findings/465-R2-PRP-05.md) | Potential null-item access on async Loader in namedMarkerConfiguration.onOpened |
| 466 | Low | 3/6 | [466-R4-EXP-09](findings/466-R4-EXP-09.md) | LibreOffice import --cat and --convert-to flags are contradictory |
| 467 | Low | 3/6 | [467-R4-IOSCPP-01](findings/467-R4-IOSCPP-01.md) | QTemporaryDir created on all platforms including non-iOS where unused |
| 468 | Low | 3/6 | [468-R4-SIG-ADD-01](findings/468-R4-SIG-ADD-01.md) | SessionModel::appendDataPoint declared public slot but never connected |
| 469 | Low | 3/6 | [469-RESO-N06](findings/469-RESO-N06.md) | ReadRegionOverlay pointer margin 3dp — overlap with text at large fonts |
| 470 | Low | 3/6 | [470-RESP-N03](findings/470-RESP-N03.md) | +android/main.qml omits all size declarations — transient zero-size layout on startup |
| 471 | Low | 3/6 | [471-RND-N01](findings/471-RND-N01.md) | forceQtTextRenderer dead on Apple platforms — unconditionally uses NativeRendering |
| 472 | Low | 3/6 | [472-SHADOW-N04](findings/472-SHADOW-N04.md) | id: frame shadows property bool frame — latent hazard |
| 473 | Low | 3/6 | [473-SHT-N02](findings/473-SHT-N02.md) | Missing StandardKey.FullScreen on Android |
| 474 | Low | 3/6 | [474-SPL2-20](findings/474-SPL2-20.md) | loadCustomWordsFromDisk redundant exists() before open() |
| 475 | Low | 3/6 | [475-STC-N02](findings/475-STC-N02.md) | Find.qml close() doesn't reset replace-mode or regex-mode flags |
| 476 | Low | 3/6 | [476-TC-N02](findings/476-TC-N02.md) | property color value assigned string expression — silent coercion |
| 477 | Low | 3/6 | [477-TMR-07](findings/477-TMR-07.md) | countdownAnimation restart uses non-idempotent running=true |
| 478 | Low | 3/6 | [478-Z-N02](findings/478-Z-N02.md) | Two OverlaySheets have z:1 while nine others have none — inconsistent stacking |
| 479 | Low | 2/6 | [479-COLOR-03](findings/479-COLOR-03.md) | velocityText ColorAnimation flash: #BBB → #FFF → #CCC jump |
| 480 | Low | 2/6 | [480-DSZ-03](findings/480-DSZ-03.md) | Magic number 68 in ListView height binding |
| 481 | Low | 2/6 | [481-EVT-N11](findings/481-EVT-N11.md) | windowStayOnTopButton lacks focusPolicy — unreachable via keyboard |
| 482 | Low | 2/6 | [482-EVT-N12](findings/482-EVT-N12.md) | velocityDragArea and viewport.mouse share z:5 — wheel dispatch ambiguous |
| 483 | Low | 2/6 | [483-MENU-N06](findings/483-MENU-N06.md) | Paste behavior inconsistent between context menu and global Edit menu |
| 484 | Low | 2/6 | [484-PRE-N01](findings/484-PRE-N01.md) | Preprocessor uses `or` instead of `\|\|` in 6 #if directives — MSVC build break |
| 485 | Low | 2/6 | [485-R2-PRP-04](findings/485-R2-PRP-04.md) | Inconsistent focus restoration in decreaseVelocityButton |
| 486 | Low | 2/6 | [486-VCI-N03](findings/486-VCI-N03.md) | Hardcoded divider/separator/border colors (#292929, #606060, #808080) break theme adaptation |
| 487 | Low | 2/6 | [487-VIS-N04](findings/487-VIS-N04.md) | Countdown crosshair frame renders orphan lines when enabled=false |
| 488 | Low | 2/6 | [488-Z-N03](findings/488-Z-N03.md) | ComboBox Popup z:103 inside OverlaySheets with z:1 — disconnected layering |
| 489 | Low | 1/6 | [489-DBG-N03](findings/489-DBG-N03.md) | Latent debug state leak: pointers/debug Setting persists Guides checkbox |
| 490 |  | 6/6 | [490-TS-03](findings/490-TS-03.md) | Korean UI `ko_KO` vs file `ko_KR` mismatch |
| 491 |  | 4/6 | [491-TS-02](findings/491-TS-02.md) | Arabic file `ar_EG` vs UI `ar_AE` mismatch |
| 492 |  | 4/6 | [492-TS-05](findings/492-TS-05.md) | Finnish/French/Korean/Italian "Saved" → verb with stray `&amp;` accelerator |
| 493 |  | 4/6 | [493-TS-16](findings/493-TS-16.md) | Paragraph spacing: 8 languages strip trailing `%` from `<pre>%1%</pre>` |
| 494 |  | 4/6 | [494-TS-17](findings/494-TS-17.md) | Line width: 7 languages add spurious `%` to `<pre>%1</pre>` |

<details><summary>Minor / non-behavioral (opus-ultra = PARTIAL) — 94</summary>

[690-LOG-07](findings/690-LOG-07.md), [529-SEC-04](findings/529-SEC-04.md), [600-SEC-05](findings/600-SEC-05.md), [672-RES-03](findings/672-RES-03.md), [673-RES-04](findings/673-RES-04.md), [580-TYP-03](findings/580-TYP-03.md), [533-EDGE-07](findings/533-EDGE-07.md), [554-EDGE-11](findings/554-EDGE-11.md), [589-PLAT-08](findings/589-PLAT-08.md), [591-R2-IOS-02](findings/591-R2-IOS-02.md), [596-R3-SPL-05](findings/596-R3-SPL-05.md), [571-R3-PMT-03](findings/571-R3-PMT-03.md), [637-R4-ROOT-05](findings/637-R4-ROOT-05.md), [519-FINAL-10](findings/519-FINAL-10.md), [555-FINAL-14](findings/555-FINAL-14.md), [520-FINAL-15](findings/520-FINAL-15.md), [521-FINAL-22](findings/521-FINAL-22.md), [512-TRL-N01](findings/512-TRL-N01.md), [558-HTK-05](findings/558-HTK-05.md), [559-HTK-06](findings/559-HTK-06.md), [630-HTK-07](findings/630-HTK-07.md), [631-HTK-08](findings/631-HTK-08.md), [602-THR-01](findings/602-THR-01.md), [603-THR-02](findings/603-THR-02.md), [643-THR-03](findings/643-THR-03.md), [578-THR-04](findings/578-THR-04.md), [658-CPY-01](findings/658-CPY-01.md), [668-OOB-N03](findings/668-OOB-N03.md), [632-I18N-N01](findings/632-I18N-N01.md), [633-I18N-N02](findings/633-I18N-N02.md), [620-MIX-01](findings/620-MIX-01.md), [625-AR-01](findings/625-AR-01.md), [530-SET-01](findings/530-SET-01.md), [640-SET-04](findings/640-SET-04.md), [698-IMP-NEW-02](findings/698-IMP-NEW-02.md), [664-IMP-NEW-03](findings/664-IMP-NEW-03.md), [551-CMT-N01](findings/551-CMT-N01.md), [650-CMT-N02](findings/650-CMT-N02.md), [606-CMT-N03](findings/606-CMT-N03.md), [610-CMT-N09](findings/610-CMT-N09.md), [626-CMT-N10](findings/626-CMT-N10.md), [548-REGEX-N01](findings/548-REGEX-N01.md), [569-PROP-N02](findings/569-PROP-N02.md), [671-PROP-N03](findings/671-PROP-N03.md), [615-SCRL-N01](findings/615-SCRL-N01.md), [693-SCRL-N05](findings/693-SCRL-N05.md), [644-TYP-N03](findings/644-TYP-N03.md), [681-TYP-N04](findings/681-TYP-N04.md), [682-TYP-N06](findings/682-TYP-N06.md), [680-TXT-N01](findings/680-TXT-N01.md), [567-PLAT-N01](findings/567-PLAT-N01.md), [619-DECL-N01](findings/619-DECL-N01.md), [629-DECL-N02](findings/629-DECL-N02.md), [651-COLOR-05](findings/651-COLOR-05.md), [652-COLOR-06](findings/652-COLOR-06.md), [627-COLOR-07](findings/627-COLOR-07.md), [653-CONST-N01](findings/653-CONST-N01.md), [654-CONST-N02](findings/654-CONST-N02.md), [655-CONST-N03](findings/655-CONST-N03.md), [656-CONST-N04](findings/656-CONST-N04.md), [657-CONST-N05](findings/657-CONST-N05.md), [623-SAVE-N04](findings/623-SAVE-N04.md), [547-RAII-N01](findings/547-RAII-N01.md), [617-Z-N01](findings/617-Z-N01.md), [684-Z-N04](findings/684-Z-N04.md), [717-ARC-01](findings/717-ARC-01.md), [718-ARC-02](findings/718-ARC-02.md), [719-ARC-03](findings/719-ARC-03.md), [720-ARC-04](findings/720-ARC-04.md), [721-ARC-05](findings/721-ARC-05.md), [722-ARC-06](findings/722-ARC-06.md), [642-STR-CNV](findings/642-STR-CNV.md), [628-COMP-N03](findings/628-COMP-N03.md), [562-LBL-N01](findings/562-LBL-N01.md), [665-LAY-N01](findings/665-LAY-N01.md), [666-LAY-N02](findings/666-LAY-N02.md), [647-WARN-N03](findings/647-WARN-N03.md), [634-INT-N01](findings/634-INT-N01.md), [560-INT-N02](findings/560-INT-N02.md), [635-INT-N03](findings/635-INT-N03.md), [566-PERF-N01](findings/566-PERF-N01.md), [669-PERF-N03](findings/669-PERF-N03.md), [624-SIG-N03](findings/624-SIG-N03.md), [621-QOBJ-N01](findings/621-QOBJ-N01.md), [645-VCI-N01](findings/645-VCI-N01.md), [646-VCI-N02](findings/646-VCI-N02.md), [604-TP-SYS](findings/604-TP-SYS.md), [659-DETACH-N01](findings/659-DETACH-N01.md), [705-SYM-N01](findings/705-SYM-N01.md), [550-A11Y-SYS](findings/550-A11Y-SYS.md), [674-RESO-N03](findings/674-RESO-N03.md), [675-RESO-N04](findings/675-RESO-N04.md), [676-TB-N03](findings/676-TB-N03.md), [638-RESP-N01](findings/638-RESP-N01.md)

</details>

<details><summary>Rejected (opus-ultra = FALSE) — 70</summary>

[691-LOG-09](findings/691-LOG-09.md), [506-QML-01](findings/506-QML-01.md), [507-QML-02](findings/507-QML-02.md), [543-QML-07](findings/543-QML-07.md), [613-QML-08](findings/613-QML-08.md), [618-QML-09](findings/618-QML-09.md), [590-QML-10](findings/590-QML-10.md), [700-RES-05](findings/700-RES-05.md), [532-TYP-01](findings/532-TYP-01.md), [605-TYP-02](findings/605-TYP-02.md), [695-TYP-08](findings/695-TYP-08.md), [701-TYP-09](findings/701-TYP-09.md), [696-TYP-10](findings/696-TYP-10.md), [553-EDGE-08](findings/553-EDGE-08.md), [660-EDGE-10](findings/660-EDGE-10.md), [685-EDGE-12](findings/685-EDGE-12.md), [612-PLAT-04](findings/612-PLAT-04.md), [525-R2-GH-01](findings/525-R2-GH-01.md), [498-R2-CMAKE-01](findings/498-R2-CMAKE-01.md), [592-R2-PRP-03](findings/592-R2-PRP-03.md), [593-R2-PTR-01](findings/593-R2-PTR-01.md), [594-R2-PTR-02](findings/594-R2-PTR-02.md), [504-R3-DOC-02](findings/504-R3-DOC-02.md), [572-R3-SPL-03](findings/572-R3-SPL-03.md), [546-R3-MAIN-01](findings/546-R3-MAIN-01.md), [699-R3-MAIN-04](findings/699-R3-MAIN-04.md), [692-R3-APP-01](findings/692-R3-APP-01.md), [614-R3-SIG-02](findings/614-R3-SIG-02.md), [595-R3-SIG-03](findings/595-R3-SIG-03.md), [505-R4-QTV-01](findings/505-R4-QTV-01.md), [509-R4-QTV-02](findings/509-R4-QTV-02.md), [545-R4-QTV-03](findings/545-R4-QTV-03.md), [597-R4-ROOT-03](findings/597-R4-ROOT-03.md), [508-R4-EVT-01](findings/508-R4-EVT-01.md), [544-R4-PRJ-01](findings/544-R4-PRJ-01.md), [598-R4-SHD-01](findings/598-R4-SHD-01.md), [501-FINAL-02](findings/501-FINAL-02.md), [540-FINAL-07](findings/540-FINAL-07.md), [534-FINAL-20](findings/534-FINAL-20.md), [510-IMP-N01](findings/510-IMP-N01.md), [503-IMP-N02](findings/503-IMP-N02.md), [500-W10-HTK-01](findings/500-W10-HTK-01.md), [517-EVT-02](findings/517-EVT-02.md), [587-NET-02](findings/587-NET-02.md), [683-VER-01](findings/683-VER-01.md), [723-QML-BND-03](findings/723-QML-BND-03.md), [648-CMAKE-N01](findings/648-CMAKE-N01.md), [639-SET-03](findings/639-SET-03.md), [535-IMP-NEW-01](findings/535-IMP-NEW-01.md), [686-IMP-NEW-04](findings/686-IMP-NEW-04.md), [607-CMT-N04](findings/607-CMT-N04.md), [539-CMT-N05](findings/539-CMT-N05.md), [608-CMT-N06](findings/608-CMT-N06.md), [609-CMT-N07](findings/609-CMT-N07.md), [688-INIT-N03](findings/688-INIT-N03.md), [689-INIT-N04](findings/689-INIT-N04.md), [694-SCRL-N06](findings/694-SCRL-N06.md), [568-PLAT-N02](findings/568-PLAT-N02.md), [563-LBL-N02](findings/563-LBL-N02.md), [570-QPROP-N02](findings/570-QPROP-N02.md), [552-DEF-N01](findings/552-DEF-N01.md), [585-IMH-SYS](findings/585-IMH-SYS.md), [661-EKA-SYS](findings/661-EKA-SYS.md), [636-LOG-N04](findings/636-LOG-N04.md), [557-FONT-N01](findings/557-FONT-N01.md), [514-COLOR-CRIT-01](findings/514-COLOR-CRIT-01.md), [599-RPL-N01](findings/599-RPL-N01.md), [662-FONT-METRIC-03](findings/662-FONT-METRIC-03.md), [541-QT-LC-N01](findings/541-QT-LC-N01.md), [542-MIME-N01](findings/542-MIME-N01.md)

</details>

<details><summary>Needs info (opus-ultra = UNSURE) — 63</summary>

[670-PLAT-09](findings/670-PLAT-09.md), [573-R3-TMR-01](findings/573-R3-TMR-01.md), [526-R4-PRJ-02](findings/526-R4-PRJ-02.md), [497-FINAL-16](findings/497-FINAL-16.md), [586-LYR-N03](findings/586-LYR-N03.md), [703-TS-01](findings/703-TS-01.md), [706-TS-04](findings/706-TS-04.md), [707-TS-06](findings/707-TS-06.md), [708-TS-07](findings/708-TS-07.md), [709-TS-08](findings/709-TS-08.md), [710-TS-09](findings/710-TS-09.md), [711-TS-10](findings/711-TS-10.md), [712-TS-11](findings/712-TS-11.md), [713-TS-12](findings/713-TS-12.md), [714-TS-13](findings/714-TS-13.md), [715-TS-14](findings/715-TS-14.md), [716-TS-15](findings/716-TS-15.md), [704-TS-18](findings/704-TS-18.md), [502-HTK-01](findings/502-HTK-01.md), [523-HTK-02](findings/523-HTK-02.md), [531-TMR-01](findings/531-TMR-01.md), [579-TMR-02](findings/579-TMR-02.md), [677-TMR-04](findings/677-TMR-04.md), [678-TMR-06](findings/678-TMR-06.md), [679-TMR-08](findings/679-TMR-08.md), [588-PC-01](findings/588-PC-01.md), [702-QTD-02](findings/702-QTD-02.md), [622-QRC-N01](findings/622-QRC-N01.md), [511-SET-02](findings/511-SET-02.md), [687-IMP-NEW-05](findings/687-IMP-NEW-05.md), [582-CMB-N01](findings/582-CMB-N01.md), [649-CMB-N02](findings/649-CMB-N02.md), [575-SCRL-N03](findings/575-SCRL-N03.md), [584-IMG-N01](findings/584-IMG-N01.md), [581-ACT-N05](findings/581-ACT-N05.md), [536-PLAT-N03](findings/536-PLAT-N03.md), [583-EVT-N10](findings/583-EVT-N10.md), [537-STATE-N01](findings/537-STATE-N01.md), [641-STATE-N04](findings/641-STATE-N04.md), [697-XFRM-N01](findings/697-XFRM-N01.md), [561-KEY-N01](findings/561-KEY-N01.md), [564-LINK-N04](findings/564-LINK-N04.md), [556-FLOW-N02](findings/556-FLOW-N02.md), [499-TXT-CRIT](findings/499-TXT-CRIT.md), [524-PATH-N03](findings/524-PATH-N03.md), [527-REGEX-CRIT-01](findings/527-REGEX-CRIT-01.md), [663-GSW-N02](findings/663-GSW-N02.md), [576-SETUP-N01](findings/576-SETUP-N01.md), [549-WATCH-N03](findings/549-WATCH-N03.md), [513-COERC-N01](findings/513-COERC-N01.md), [518-EVT-N13](findings/518-EVT-N13.md), [515-DEB-N02](findings/515-DEB-N02.md), [516-DEB-N03](findings/516-DEB-N03.md), [616-TS-N07](findings/616-TS-N07.md), [611-META-N14](findings/611-META-N14.md), [667-META-N16](findings/667-META-N16.md), [565-META-N17](findings/565-META-N17.md), [538-TMR-N05](findings/538-TMR-N05.md), [522-FONT-METRIC-01](findings/522-FONT-METRIC-01.md), [601-STC-N03](findings/601-STC-N03.md), [574-RESP-N02](findings/574-RESP-N02.md), [577-SHAPE-N02](findings/577-SHAPE-N02.md), [528-SCR-N01](findings/528-SCR-N01.md)

</details>

<details><summary>Done — 2</summary>

[495-AND-CRIT-01](findings/495-AND-CRIT-01.md), [496-CLIP-CRIT-01](findings/496-CLIP-CRIT-01.md)

</details>
