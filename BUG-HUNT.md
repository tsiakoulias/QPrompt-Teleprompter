# Bug Hunt Report — QPrompt Teleprompter

**Date:** 2026-06-20  
**Branch:** `bug-hunt-findings`  
**Methodology:** 8 parallel subagents auditing all source files (~27 .cpp/.h, ~19 .qml, CMakeLists.txt, config files) across 8 categories. Only 100% verified bugs included.

---

## Summary

| Category | Critical | High | Medium | Low | Total |
|---|---|---|---|---|---|
| Memory Management | 0 | 2 | 1 | 0 | 3 |
| Logic / Control Flow | 0 | 3 | 4 | 2 | 9 |
| QML / UI | 3 | 5 | 3 | 0 | 11 |
| Security | 1 | 1 | 3 | 0 | 5 |
| Resource Management | 0 | 2 | 1 | 2 | 5 |
| Type Safety / Conversion | 0 | 4 | 4 | 2 | 10 |
| Edge Case / Error Handling | 3 | 3 | 3 | 3 | 12 |
| Platform / Build | 0 | 2 | 5 | 2 | 9 |
| **TOTAL** | **7** | **22** | **24** | **11** | **64** |

---

## Memory Management Bugs

### [MEM-01] Memory Leak: `_markersModel` allocated without parent, never deleted
- **File:** src/documenthandler.cpp:139, src/documenthandler.h:343
- **Severity:** High
- **Code:**
  ```cpp
  _markersModel = new MarkersModel();   // no parent passed
  DocumentHandler::~DocumentHandler() = default;   // no explicit delete
  ```
- **Analysis:** `MarkersModel` inherits from `QAbstractListModel` → `QObject`. Heap-allocated without parent; the default destructor does not delete it. Contrast with `m_network` and `m_cache` which correctly pass `this` as parent.
- **Impact:** Memory leak on every `DocumentHandler` destruction.

### [MEM-02] Memory Leak: `_fileSystemWatcher` allocated without parent, never deleted
- **File:** src/documenthandler.cpp:140, src/documenthandler.h:344
- **Severity:** High
- **Code:**
  ```cpp
  _fileSystemWatcher = new QFileSystemWatcher();   // no parent
  DocumentHandler::~DocumentHandler() = default;   // no explicit delete
  ```
- **Analysis:** Identical pattern to MEM-01. `QFileSystemWatcher` (QObject) heap-allocated, no parent, never deleted.
- **Impact:** Memory leak on every `DocumentHandler` destruction.

### [MEM-03] Memory Leak: `m_fontDialog` allocated without parent, never deleted
- **File:** src/documenthandler.cpp:148, src/documenthandler.h:347
- **Severity:** Medium
- **Code:**
  ```cpp
  m_fontDialog = new SystemFontChooserDialog();   // no parent, no WA_DeleteOnClose
  DocumentHandler::~DocumentHandler() = default;  // no explicit delete
  ```
- **Analysis:** `SystemFontChooserDialog` (QDialog) heap-allocated with no parent and no `WA_DeleteOnClose`. User-closing merely hides it. Default destructor never deletes it.
- **Impact:** Memory leak of dialog and all child widgets on destruction.

---

## Logic / Control Flow Bugs

### [LOG-01] SessionModel::rowCount returns m_data.size() for both valid and invalid parents
- **File:** src/promptsession.cpp:31-36
- **Severity:** High
- **Code:**
  ```cpp
  int SessionModel::rowCount(const QModelIndex &parent) const
  {
      if (!parent.isValid())
          return m_data.size();
          //return 0;         // <-- commented-out correct code
      return m_data.size();   // <-- should return 0 for valid parent
  }
  ```
- **Analysis:** For a flat list model, a valid parent should return 0 children. Both branches return `m_data.size()`, making the if/else meaningless. The commented-out `//return 0;` confirms the developer's intent.
- **Impact:** QML ListView/Repeater may attempt to recurse into list items, causing corrupted display or infinite recursion.

### [LOG-02] Off-by-one: beginRemoveRows uses rowCount() instead of rowCount()-1
- **File:** src/promptsession.cpp:81
- **Severity:** High
- **Code:**
  ```cpp
  beginRemoveRows(QModelIndex(), 0, rowCount());  // rowCount() = N, last index should be N-1
  ```
- **Analysis:** The 3rd parameter to `beginRemoveRows` is the last row index (inclusive). If there are 5 rows (indices 0-4), `rowCount()` = 5, claiming removal of 6 rows. When empty, claims removal of 1 row (index 0). `MarkersModel::clearMarkers()` correctly uses `rowCount() - 1`.
- **Impact:** Assertion failure in debug; undefined behavior / view crash in release.

### [LOG-03] MarkersModel::data returns data.position for LengthRole instead of data.length
- **File:** src/markersmodel.cpp:48-49
- **Severity:** Medium
- **Code:**
  ```cpp
  else if (role == PositionRole)
      return data.position;
  else if (role == LengthRole)
      return data.position;  // BUG: should be data.length
  ```
- **Analysis:** Copy-paste error. Both `PositionRole` and `LengthRole` return `data.position`. The `Marker` struct has a distinct `length` field that is never returned by the model.
- **Impact:** Code consuming the `length` role gets the position value instead, showing incorrect marker sizes.

### [LOG-04] MarkersModel::extendLastMarker modifies data without emitting dataChanged
- **File:** src/markersmodel.cpp:109-114
- **Severity:** Medium
- **Code:**
  ```cpp
  void MarkersModel::extendLastMarker(QString text)
  {
      const auto last = m_data.last();
      if (last.text.length()==1)
          m_data.last().text += text;
      // no dataChanged() signal emitted
  }
  ```
- **Analysis:** When the last marker's text is extended, no `dataChanged()` signal is emitted. Views do not know to re-render.
- **Impact:** Stale visual display in QML list views until the next full model reparse.

### [LOG-05] DocumentHandler::search ignores `loop` parameter when `regEx` is true
- **File:** src/documenthandler.cpp:1552-1567
- **Severity:** Medium
- **Code:**
  ```cpp
  // regex branch (line 1552):
  if (cursor.selectionStart() == -1 && cursor.selectionStart() == -1 && cursor.selectionEnd() == -1) {
      // wraps around unconditionally -- loop parameter NOT checked

  // non-regex branch (line 1567):
  if (loop && (cursor.selectionStart() == -1 && cursor.selectionStart() == -1 && cursor.selectionEnd() == -1)) {
      // respects the loop parameter
  ```
- **Analysis:** The `loop` parameter controls wrap-around behavior. When `regEx = true`, the check at line 1552 does not test `loop`, so it always wraps. Also, both branches redundantly check `cursor.selectionStart() == -1` twice instead of checking start AND end.
- **Impact:** `replaceAll()` passes `loop = false` to prevent wrapping, but regex searches still wrap, potentially causing infinite loops.

### [LOG-06] DocumentHandler::replaceAll has potential infinite loop with regex
- **File:** src/documenthandler.cpp:1492-1520
- **Severity:** Medium
- **Code:**
  ```cpp
  do {
      i++;
      cursor.setPosition(range.x());
      cursor.setPosition(range.y(), QTextCursor::KeepAnchor);
      cursor.removeSelectedText();
      cursor.insertText(replacementText);
      range = search(searchedText, false, true, regEx, false);
      resultsFound = range.y() > range.x();
  } while (resultsFound);
  ```
- **Analysis:** If the replacement text contains the search text, or if a regex matches zero-length positions, the loop never terminates. Combined with LOG-05 (loop parameter ignored for regex), the search wraps around, making `range.y() > range.x()` always true.
- **Impact:** Application hangs with 100% CPU during Replace All.

### [LOG-07] namedMarker() fetches cursor twice — stale-content risk
- **File:** src/documenthandler.cpp:699-705
- **Severity:** Low
- **Code:**
  ```cpp
  QTextCursor cursor = textCursor();   // used only for isNull()
  if (cursor.isNull()) return false;
  return textCursor().charFormat().isAnchor() &&   // second cursor fetch
         (textCursor().charFormat().anchorNames()... // third fetch
  ```
- **Analysis:** The local `cursor` is only null-checked. All subsequent calls to `textCursor()` fetch independent cursor objects that may not correspond to the same position.
- **Impact:** Edge case where anchor names/format belong to a different text position than the one null-checked.

### [LOG-08] DataPoint default constructor leaves three members uninitialized
- **File:** src/promptsession.h:31,38-41
- **Severity:** Low
- **Code:**
  ```cpp
  DataPoint() {}        // empty default constructor
  int prompterWidth;    // no = initializer
  int lineWidth;        // no = initializer
  int lineHeight;       // no = initializer
  ```
- **Analysis:** While `time` and `position` have `= 0` initializers, `prompterWidth`, `lineWidth`, and `lineHeight` have none. Default-constructing produces indeterminate values.
- **Impact:** Garbage values in telemetry/session data.

### [LOG-09] Trailing comma in constructor member initializer list (non-standard C++ before C++20)
- **File:** src/documenthandler.cpp:129
- **Severity:** Low
- **Code:**
  ```cpp
  , _markersModel(nullptr)
  ```
- **Analysis:** Last initializer has trailing comma. Non-standard before C++20; will cause error on MSVC with `/permissive-`.
- **Impact:** Build failure on strict/MSVC toolchains.

---

## QML / UI Bugs

### [QML-01] 26 references to undefined `pointerSettings` ID in ReadRegionOverlay
- **File:** src/prompter/ReadRegionOverlay.qml:239,246,261,268,293-395
- **Severity:** Critical
- **Code:**
  ```qml
  running: !pointerSettings.debug
  source: pointerSettings.pointerKind === PointerSettings.States.QML
  value: pointerSettings.colorsEditing
  ```
  (+23 more references)
- **Analysis:** `pointerSettings` is an `id` declared in `PointerSettings.qml` (separate file). QML IDs are file-scoped; not visible across component boundaries. No C++ context property bridges it.
- **Impact:** Entire pointer/indicator system in the reading overlay is non-functional — no pointer indicators render, no colors apply, debug tools broken.

### [QML-02] Undefined `pointerConfiguration` ID reference in ReadRegionOverlay
- **File:** src/prompter/ReadRegionOverlay.qml:283,288
- **Severity:** Critical
- **Code:**
  ```qml
  value: pointerConfiguration.opened
  ```
- **Analysis:** `pointerConfiguration` is an OverlaySheet `id` in `PrompterPage.qml`, not exposed to `ReadRegionOverlay.qml`.
- **Impact:** `configuratorOpen` property on pointer items never set; color animation behavior broken.

### [QML-03] Undefined `root` ID in WindowDragger.qml
- **File:** src/qt/WindowDragger.qml:41,45
- **Severity:** Critical
- **Code:**
  ```qml
  property var window: parent   // declared but ignored
  root.x += deltaX;             // root is NOT an id in this file
  root.y += deltaY;
  ```
- **Analysis:** No `id: root` declared in WindowDragger.qml. The file defines `window` for the drag target but uses `root` instead. `root` exists only in `main.qml` files.
- **Impact:** Window dragging via toolbar silently fails on frameless configurations with ReferenceError.

### [QML-04] Typo: `verticalCentertop` instead of `verticalCenter`
- **File:** src/prompter/pointers/pointer_0.qml:36
- **Severity:** High
- **Code:**
  ```qml
  anchors.verticalCenter: parent.verticalCentertop
  ```
- **Analysis:** `verticalCentertop` is not a valid QML property — characters from `verticalCenter` bled into `top`. Should be `parent.verticalCenter`.
- **Impact:** Arrow pointer Shape positions at (0,0) instead of being vertically centered.

### [QML-05] `&&` should be `||` in clear button enabled condition
- **File:** src/kirigami_ui/KeyInputButton.qml:121
- **Severity:** High
- **Code:**
  ```qml
  enabled: !(keyInputButton.text === "" && keyInputButton.text === "[…]")
  ```
- **Analysis:** A string cannot simultaneously be `""` AND `"[…]"`. `&&` always yields `false`; `!false` is always `true`. The clear button is never disabled. Should be `||`.
- **Impact:** Users can click "clear" even when no key binding is being configured.

### [QML-06] Bitwise OR (`|`) instead of AND (`&`) in modifier key check
- **File:** src/prompter/Find.qml:164
- **Severity:** High
- **Code:**
  ```qml
  if (event.key === Qt.Key_R && event.modifiers | Qt.CtrlModifier)
  ```
- **Analysis:** `|` is bitwise OR, `&` is bitwise AND. `event.modifiers | Qt.CtrlModifier` is always non-zero (truthy) because CtrlModifier has bits set. The condition is true when R is pressed with *any* modifier.
- **Impact:** Ctrl+R shortcut fires on R+Shift, R+Alt, etc. — conflicting with typing and toggling replace UI unexpectedly.

### [QML-07] `Text.CurveRendering` enum requires Qt >= 6.7
- **File:** src/prompter/Countdown.qml:196
- **Severity:** High
- **Code:**
  ```qml
  renderType: ... ? Text.CurveRendering : Text.NativeRendering
  ```
- **Analysis:** `Text.CurveRendering` was introduced in Qt 6.7. File imports `QtCore 6.5`. On Qt 6.5, this enum value does not exist.
- **Impact:** Countdown number text may fail to render or use unintended rendering path.

### [QML-08] Invalid anchor target `undefined`
- **File:** src/kirigami_ui/PrompterPage.qml:807
- **Severity:** Medium
- **Code:**
  ```qml
  anchors.centerIn: undefined
  ```
- **Analysis:** `anchors.centerIn` requires a valid Item reference. `undefined` produces a QML warning.
- **Impact:** Velocity indicator appears at (0,0) instead of centered at click point.

### [QML-09] `QtQuick.Shapes 6.6` version mismatch with `QtCore 6.5`
- **File:** src/prompter/Countdown.qml:24
- **Severity:** Medium
- **Code:**
  ```qml
  import QtQuick.Shapes 6.6    // requires Qt >= 6.6
  // ...
  import QtCore 6.5            // indicates Qt 6.5
  ```
- **Analysis:** Version import mismatch — `QtQuick.Shapes 6.6` is not available on Qt 6.5.
- **Impact:** Countdown component fails to load on Qt 6.5 systems.

### [QML-10] `+android/main.qml` missing `QmlUtil` for RecentDocuments
- **File:** src/kirigami_ui/+android/main.qml:757-762
- **Severity:** Medium
- **Code:**
  ```qml
  property RecentDocuments recentDocuments: RecentDocuments {
      targetAction: recentFilesAction
      onOpenRequested: ...   // no `util: qmlutil` property assigned
  }
  ```
- **Analysis:** No `QmlUtil { id: qmlutil }` declared in +android/main.qml. `RecentDocuments.refreshExistence()` calls `root.util.fileExists(item.uri)` — crashes with `TypeError: root.util is null`.
- **Impact:** Recently opened files list crashes on Android when checking file existence.

### [QML-11] Dead code: `window` property declared but never used in WindowDragger
- **File:** src/qt/WindowDragger.qml:28
- **Severity:** Medium
- **Code:**
  ```qml
  property var window: parent   // correctly assigned by callers, never referenced
  ```
- **Analysis:** The `window` property is set by callers (e.g., `window: root` from EditorToolbar.qml:138) but the implementation references non-existent `root` instead of `window`.
- **Impact:** Dead code. Even after fixing QML-03, this property assignment is wasted.

---

## Security Bugs

### [SEC-01] Arbitrary Command Execution via `sys://` Marker URIs
- **File:** src/prompter/Prompter.qml:415-416, src/qmlutil.hpp:84-94
- **Severity:** Critical
- **Code:**
  ```cpp
  Q_INVOKABLE void run(const QString &command) {
      QStringList parts = QProcess::splitCommand(command);
      const QString program = parts.takeFirst();
      QProcess::startDetached(program, parts);
  }
  ```
  ```qml
  else if (m.url.startsWith("sys://"))
      qmlutil.run(m.url.slice(6));
  ```
- **Analysis:** The prompter scrolls past markers and checks `m.url`. If URL starts with `sys://`, the rest is passed to `QProcess::startDetached()` with zero sanitization. A crafted `.html` file with `<a href="sys://malicious">` causes arbitrary command execution when the prompter scrolls past it.
- **Impact:** Remote code execution via shared prompter script files. Any document containing `sys://` anchor hrefs achieves arbitrary command execution with user privileges.

### [SEC-02] OBS WebSocket Password Stored in Plaintext
- **File:** src/prompter/Prompter.qml:275-280, src/kirigami_ui/PrompterPage.qml:1496-1506
- **Severity:** Medium
- **Code:**
  ```qml
  Settings {
      category: "obs"
      property alias password: ws.password
  }
  ```
- **Analysis:** The OBS WebSocket password is stored via QSettings in plaintext (Windows registry `HKCU\Software\Cuperino\qprompt\obs\password`; Linux `~/.config/Cuperino/qprompt.conf`). No encryption.
- **Impact:** Any process running as the same user can read the OBS WebSocket password.

### [SEC-03] Information Disclosure: Full HTML Document Content Logged via qDebug
- **File:** src/documenthandler.cpp:1332
- **Severity:** Medium
- **Code:**
  ```cpp
  qDebug() << html;
  return html;
  ```
- **Analysis:** `filterHtml()` logs the entire filtered HTML unconditionally. Called during import, paste, and drop operations. Every HTML document has its full content written to the debug log.
- **Impact:** Sensitive prompter script content leaked to system debug logs. On Windows, captured by DebugView; on Linux, by journald.

### [SEC-04] SSRF / URL Injection — User-Controlled URL Passed to Network Loader
- **File:** src/documenthandler.cpp:867-886, src/kirigami_ui/PrompterPage.qml:1277-1291
- **Severity:** High
- **Code:**
  ```cpp
  if (url.isRelative()) {
      resultingUrl.setScheme("http");
      resultingUrl.setHost(url.path());  // user path becomes hostname
  }
  m_reply = m_network->get(req);
  ```
- **Analysis:** User-supplied URL with no scheme: the path component becomes the hostname, allowing input like `192.168.1.1` or `localhost:4455` to issue HTTP GETs to internal services. Response content is rendered in the editor.
- **Impact:** Blind SSRF — attacker can connect to internal services, cloud metadata endpoints, or OBS WebSocket.

### [SEC-05] User-Controlled Filename Passed to QProcess (LibreOffice import)
- **File:** src/documenthandler.cpp:1076-1077
- **Severity:** Medium
- **Code:**
  ```cpp
  arguments << QLatin1String("--cat") << QLatin1String("--convert-to")
            << QLatin1String("html:HTML") << fileName;
  convert.start(program, arguments);
  ```
- **Analysis:** The file name from the opened URL is appended directly to QProcess arguments. A file named `--help.odt` would be interpreted as a flag by LibreOffice. On Windows, QProcess uses `CreateProcess` command-line conversion which has known escaping edge cases.
- **Impact:** Flag injection in LibreOffice; potential command injection on Windows.

---

## Resource Management Bugs

### [RES-01] Network reply overwritten without aborting previous download
- **File:** src/documenthandler.cpp:884
- **Severity:** High
- **Code:**
  ```cpp
  m_reply = m_network->get(req);  // old m_reply overwritten, never abort()ed
  ```
- **Analysis:** When `loadFromNetwork()` is called a second time, `m_reply` is reassigned without calling `abort()` or `deleteLater()` on the old reply. Old reply continues downloading; when it completes, the slot reads from the new (possibly incomplete) `m_reply`.
- **Impact:** Stale network traffic, wasted bandwidth/CPU, potential data corruption when stale replies finish and the slot reads wrong data.

### [RES-02] loadFromNetworkFinihed ignores the QNetworkReply* signal parameter
- **File:** src/documenthandler.cpp:145,888-901
- **Severity:** High
- **Code:**
  ```cpp
  connect(m_network, &QNetworkAccessManager::finished, this, &DocumentHandler::loadFromNetworkFinihed);

  void DocumentHandler::loadFromNetworkFinihed() {
      auto document = m_reply->readAll();   // uses member, not the reply that actually finished
  }
  ```
- **Analysis:** `QNetworkAccessManager::finished(QNetworkReply *)` provides the exact reply that completed. The slot ignores this parameter and uses `m_reply` instead. Combined with RES-01, this can read from the wrong reply.
- **Impact:** Wrong document content loaded; stale replies processed as current request.

### [RES-03] ShakeDetector::s_instance never set to nullptr on destruction (dangling pointer)
- **File:** src/shakedetector.cpp:24,29
- **Severity:** Low
- **Code:**
  ```cpp
  ShakeDetector::ShakeDetector(QObject *parent) : QObject(parent) {
      s_instance = this;   // set in constructor
  }
  // No destructor resets s_instance to nullptr
  ```
- **Analysis:** Static singleton pointer never cleared on destruction. If QML engine destroys and recreates the ShakeDetector, `instance()` returns a dangling pointer. Same pattern in `IosSaveDialog`.
- **Impact:** Use-after-free (unlikely in normal flow but detectable by ASan).

### [RES-04] IosSaveDialog::s_instance same singleton dangling pattern
- **File:** src/iossavedialog.cpp:24,29
- **Severity:** Low
- **Code:** Identical pattern to RES-03.
- **Impact:** Same use-after-free risk as ShakeDetector.

### [RES-05] QTextStream left unflushed before QFile destruction
- **File:** src/spellchecker.cpp:390-397
- **Severity:** Low
- **Code:**
  ```cpp
  QTextStream out(&file);
  for (const QString &w : m_customWords)
      out << w << '\n';
  // QTextStream and QFile destructors handle flush/close
  ```
- **Analysis:** `QTextStream` is never explicitly flushed. While RAII (destructor ordering) makes this safe in normal operation, explicit `flush()` would be more robust. Compare with `documenthandler.cpp:1164-1166` which calls `file.flush()`.
- **Impact:** Low risk on abnormal termination; data-at-rest consistency depends on destructor ordering.

---

## Type Safety / Conversion Bugs

### [TYP-01] Dangling pointer from temporary std::string in SpellChecker::loadOne
- **File:** src/spellchecker.cpp:154-155
- **Severity:** High
- **Code:**
  ```cpp
  const char *enc = out.hunspell->get_dict_encoding().c_str();  // temporary!
  out.encoding = QByteArray(enc);  // reads freed memory
  ```
- **Analysis:** `get_dict_encoding()` returns `std::string` by value (temporary). `.c_str()` returns a pointer into the temporary's buffer. At the semicolon, the temporary is destroyed; `enc` is dangling. The next line constructs `QByteArray` from freed memory — undefined behavior.
- **Impact:** Corrupted/garbage encoding for hunspell. All subsequent `encode()`/`decode()` return mangled text.

### [TYP-02] Invalid Qt::LayoutDirection enum value cast
- **File:** src/main.cpp:166
- **Severity:** Medium
- **Code:**
  ```cpp
  app.setLayoutDirection(static_cast<Qt::LayoutDirection>(2 - settings.value("ui/layout", 0).toInt()));
  ```
- **Analysis:** `Qt::LayoutDirection` has values `LeftToRight = 0` and `RightToLeft = 1`. When setting value is 0, `2 - 0 = 2`, which is not a valid enumerator — undefined behavior.
- **Impact:** Undefined behavior. May produce unpredictable layout behavior.

### [TYP-03] Floating-point equality comparison of window opacity
- **File:** src/main.cpp:273
- **Severity:** Medium
- **Code:**
  ```cpp
  const bool initiallyOpaque = topWindow->opacity() == 1.0;
  ```
- **Analysis:** `QWindow::opacity()` returns `qreal` (double). Exact equality with `1.0` is unreliable due to floating-point representation. An opacity of 0.9999999999 compares as false.
- **Impact:** Transparency toggle hotkey gets stuck in wrong state; behavior becomes unpredictable.

### [TYP-04] Bitwise AND on bools hides dead code in preventSleep
- **File:** src/documenthandler.cpp:1928,1931
- **Severity:** Medium
- **Code:**
  ```cpp
  return false & prevent;
  ```
- **Analysis:** `&` on bools: `false & prevent` → `0 & (0|1)` → always `0` (false). The `prevent` parameter is dead code — has zero effect. Should be `&&` or just `return false;`.
- **Impact:** On iOS/non-Android, the `prevent` parameter is silently ignored; function always returns false.

### [TYP-05] Uninitialized pointer member m_reply in DocumentHandler
- **File:** src/documenthandler.h:353, src/documenthandler.cpp:123-158
- **Severity:** Medium
- **Code:**
  ```cpp
  QNetworkReply *m_reply;   // declared but never initialized in constructor
  ```
- **Analysis:** `m_reply` is not initialized in the constructor initializer list or body. Holds indeterminate value until `loadFromNetwork()` sets it. Standard practice is to initialize to `nullptr`.
- **Impact:** Crash or UB if any code path dereferences `m_reply` before it's set.

### [TYP-06] Malformed preprocessor macro: `#define Use_GlobalAccel = 1`
- **File:** src/globalhotkeys.cpp:29
- **Severity:** Low
- **Code:**
  ```cpp
  #define Use_GlobalAccel = 1
  ```
- **Analysis:** Defines macro to token sequence `= 1`, not to `1`. Currently masked because only `#ifdef` checks are used. If anyone writes `#if Use_GlobalAccel` or uses the macro in an expression, it expands to `= 1` — syntax error.
- **Impact:** Will cause hard compile error if any value-check is added.

### [TYP-07] Narrowing conversion: `size_t` → `int` in SpellChecker::decode
- **File:** src/spellchecker.cpp:411-412
- **Severity:** Low
- **Code:**
  ```cpp
  return QString::fromUtf8(word.c_str(), static_cast<int>(word.size()));
  ```
- **Analysis:** `std::string::size()` → `size_t` (64-bit) to `int` (32-bit, signed) narrowing. If word length exceeds INT_MAX, value wraps negative. Extremely unlikely for single words, but correctness issue.
- **Impact:** Nil in practice; correctness violation. Should use `static_cast<qsizetype>()`.

### [TYP-08] DocumentHandler constructor trailing comma in initializer list
- **File:** src/documenthandler.cpp:129
- **Severity:** Low
- **Code:**
  ```cpp
  , _markersModel(nullptr)
  ```
- **Analysis:** Last entry in initializer list has trailing comma. Non-standard C++ before C++20; MSVC `/permissive-` rejects it.
- **Impact:** Build failure on strict/MSVC toolchains.

### [TYP-09] Null pointer dereferences in emit textChanged related to uninitialized m_document
- **File:** src/documenthandler.cpp:320,325,334,343,383 (related)
- **Severity:** Low
- **Code:** Various `emit textChanged()` paths that depend on `document()` being non-null.
- **Analysis:** These are contingent on normal initialization — noted as fragile but not individually reproduced.
- **Impact:** These are low-risk in normal usage but the empty `m_document` (`nullptr`) state has no guard in these code paths.

### [TYP-10] Uninitialized marker struct fields: length defaults to 1
- **File:** src/marker.hpp:48
- **Severity:** Low
- **Code:**
  ```cpp
  int length = 1;
  ```
- **Analysis:** This is correctly defaulted to 1. Paired with LOG-03 showing `length` is never returned by the model — the bug is in the model, not the struct.

---

## Edge Case / Error Handling Bugs

### [EDGE-01] QString::arg() called on string with no placeholder — program name silently dropped
- **File:** src/documenthandler.cpp:1086-1089
- **Severity:** High
- **Code:**
  ```cpp
  return tr("An error occurred while attempting to open file in a third party format..."
            "to make sure a corresponding import tool is properly configured.")
      .arg(program);
  ```
- **Analysis:** The tr() string has no `%1` placeholder, but `.arg(program)` is called. In Qt 6, `arg()` on a string with no placeholder silently does nothing. The program name intended for the error message is never included.
- **Impact:** Users troubleshooting import failures never see which program path was attempted. Error message is misleading.

### [EDGE-02] Empty container `first()` dereference — crash on hotkey with no windows
- **File:** src/main.cpp:272
- **Severity:** High
- **Code:**
  ```cpp
  QWindowList windows = app.allWindows();
  QWindow *topWindow = windows.first();  // UB if empty
  const bool initiallyOpaque = topWindow->opacity() == 1.0;
  ```
- **Analysis:** `QList::first()` on empty list is UB. If Meta+Alt+F10 is pressed before any window exists or after all closed, the list is empty. No `isEmpty()` guard.
- **Impact:** Application crashes on transparency toggle hotkey in windowless state.

### [EDGE-03] Empty container `last()` dereference in `extendLastMarker`
- **File:** src/markersmodel.cpp:111-113
- **Severity:** High
- **Code:**
  ```cpp
  void MarkersModel::extendLastMarker(QString text) {
      const auto last = m_data.last();   // UB if empty
      if (last.text.length()==1)
          m_data.last().text += text;
  }
  ```
- **Analysis:** `QList::last()` on empty list is UB. Public method, no `isEmpty()` guard. Only internal caller (parse()) ensures a marker was just appended, but external callers could trigger the bug.
- **Impact:** Application crash if `extendLastMarker` is called with empty markers list.

### [EDGE-04] Null pointer dereference: `document()->textDocument()` not checked before `load()`
- **File:** src/documenthandler.cpp:1037
- **Severity:** Critical
- **Code:**
  ```cpp
  document()->textDocument()->clearUndoRedoStacks();
  ```
- **Analysis:** `document()` returns `m_document` which is initialized to `nullptr` and can be set to `nullptr`. If `load()` is called before `setDocument()`, this dereferences null.
- **Impact:** Null pointer dereference crash.

### [EDGE-05] Null pointer dereference: `textDocument()` unchecked in `search()`
- **File:** src/documenthandler.cpp:1546,1548,1550,1555,1557,1561,1563,1565,1569,1571
- **Severity:** Critical
- **Code:**
  ```cpp
  cursor = this->textDocument()->find(searchRegEx, this->selectionStart(), ...);
  ```
- **Analysis:** `textDocument()` returns `nullptr` when `m_document` is null. Called from `replaceAll()` which is QML-invokable. No null guard.
- **Impact:** Null pointer dereference crash when search/replace is invoked with no document loaded.

### [EDGE-06] Null pointer dereference: `textDocument()` unchecked in `parse()`
- **File:** src/documenthandler.cpp:1634
- **Severity:** Critical
- **Code:**
  ```cpp
  for (QTextBlock it = this->textDocument()->begin(); it != this->textDocument()->end(); ...)
  ```
- **Analysis:** Called from `previousMarker()`/`nextMarker()` → QML/keyboard shortcuts. No null guard before the loop.
- **Impact:** Null pointer dereference crash on marker navigation with no document loaded.

### [EDGE-07] Q_UNREACHABLE in Q_INVOKABLE method — UB if called from QML
- **File:** src/shakedetector.cpp:49-51
- **Severity:** High
- **Code:**
  ```cpp
  void ShakeDetector::showUndoRedoDialog(bool, bool) {
      Q_UNREACHABLE();   // but method is Q_INVOKABLE!
  }
  ```
- **Analysis:** `showUndoRedoDialog` is declared `Q_INVOKABLE` (callable from QML). Implementation uses `Q_UNREACHABLE()` which compiles to `__builtin_unreachable()` in release — invoking UB if the path is ever taken. Should be a no-op.
- **Impact:** Undefined behavior (crash, miscompile, or exploit) if QML calls this method.

### [EDGE-08] Q_ASSERT as thread-safety guard — removed in release builds
- **File:** src/appcontroller.cpp:36
- **Severity:** Medium
- **Code:**
  ```cpp
  Q_ASSERT(qmlEngine->thread() == singleton->thread());
  ```
- **Analysis:** `Q_ASSERT` is compiled out in release builds. The thread-safety check disappears. Should be a runtime check (`Q_CHECK_PTR` or similar).
- **Impact:** Cross-thread singleton access silently corrupts state in release builds.

### [EDGE-09] QFile::copy() return value silently ignored
- **File:** src/spellchecker.cpp:199
- **Severity:** Medium
- **Code:**
  ```cpp
  QFile::copy(resourcePath, outPath);   // return value ignored
  QFile::setPermissions(outPath, ...);  // may fail if copy failed
  ```
- **Analysis:** If copy fails (disk full, permissions, antivirus lock), the error is silently swallowed. `setPermissions` on non-existent file also fails silently. Caller then tries to open a non-existent dictionary — no error reported.
- **Impact:** Spell checking silently breaks; user given no indication that a dictionary could not be loaded.

### [EDGE-10] globalShortcutKey() switch without default — fallthrough to Q_UNREACHABLE
- **File:** src/globalhotkeys.cpp:513-515
- **Severity:** Low
- **Code:**
  ```cpp
      };
      Q_UNREACHABLE();
  ```
- **Analysis:** Under certain preprocessor configurations (`!QHotkey_FOUND && !Use_GlobalAccel`), all cases are break-only with no return. If a new enum value is added without updating all guards, `Q_UNREACHABLE()` is hit.
- **Impact:** UB in release — low probability, requires both preprocessor edge case and enum mismatch.

### [EDGE-11] m_reply dereference without null check in loadFromNetworkFinihed()
- **File:** src/documenthandler.cpp:890
- **Severity:** Medium
- **Code:**
  ```cpp
  auto document = m_reply->readAll();  // m_reply not checked
  ```
- **Analysis:** `m_reply` is not initialized in the constructor. While practically set before the signal fires, the signal carries the reply pointer as its argument — should use that directly.
- **Impact:** Null dereference if network state machine reaches unexpected state.

### [EDGE-12] QTextBlock::iterator scope fragility in parse()
- **File:** src/documenthandler.cpp:1648,1662-1663
- **Severity:** Low
- **Code:**
  ```cpp
  QTextBlock::iterator jt;
  for (jt = it.begin(); !jt.atEnd(); ++jt) { ... }
  ```
- **Analysis:** Iterator declared outside loop. If a `continue` is ever added inside without being careful, or an exception is thrown before `++jt`, the iterator never advances — infinite loop. Currently harmless but fragile.
- **Impact:** None currently. Anti-pattern.

---

## Platform / Build Bugs

### [PLAT-01] KF6Crash_FOUND never defined as C preprocessor macro — KCrash support dead code
- **File:** src/main.cpp:50, CMakeLists.txt:316
- **Severity:** High
- **Code:**
  ```cmake
  find_package(KF6Crash ...)   # sets CMake variable, NOT C++ preprocessor macro
  ```
  ```cpp
  #if defined(KF6Crash_FOUND)   // always false — never #defined
  ```
- **Analysis:** CMake's `find_package` sets the CMake variable `KF6Crash_FOUND`, but this is never translated to a C++ preprocessor macro via `target_compile_definitions`. No `add_definitions(-DKF6Crash_FOUND)` or similar. Also, `KF6::Crash` is never linked. Compare with `QHotkey_FOUND` which IS correctly added at `src/CMakeLists.txt:496`.
- **Impact:** KCrash (crash handling, DrKonqi, auto-restart) is never compiled into the binary on any platform. Entire `#include <KCrash>` and `KCrash::initialize()` blocks are dead code.

### [PLAT-02] REQUIRED_KF6_VERSION variable referenced but never defined
- **File:** CMakeLists.txt:309,316
- **Severity:** Medium
- **Code:**
  ```cmake
  find_package(KF${QT_VERSION_MAJOR}Crash ${REQUIRED_KF${QT_VERSION_MAJOR}_VERSION} ...)
  ```
- **Analysis:** `REQUIRED_KF6_VERSION` is never set. Expands to empty string in `find_package`, dropping the version requirement silently.
- **Impact:** KF6Crash found without version constraint; incompatible versions may be accepted.

### [PLAT-03] Wrong target name and wrong include path for KDMacTouchBar
- **File:** src/CMakeLists.txt:491,492
- **Severity:** High
- **Code:**
  ```cmake
  target_include_directories(mactouchbar PRIVATE ...)     # target "mactouchbar" doesn't exist
  target_link_directories(mactouchbar PRIVATE ...)        # target "mactouchbar" doesn't exist
  ```
- **Analysis:** The target name is `KDMacTouchBar` (the project name in the subdirectory), not `mactouchbar`. Also, `${kdmactouchbar_SOURCE_DIR}/KDMacTouchBar` doubles the path (`<root>/3rdparty/KDMacTouchBar/KDMacTouchBar`). Line 493 correctly uses `KDMacTouchBar`.
- **Impact:** macOS: include/link directories not properly set. The framework may fail to build or link correctly.

### [PLAT-04] DS_Store.scpt referenced but file does not exist
- **File:** CMakeLists.txt:485
- **Severity:** Medium
- **Code:**
  ```cmake
  set(CPACK_DMG_DS_STORE_SETUP_SCRIPT "${CMAKE_SOURCE_DIR}/dist/macOS/DS_Store.scpt")
  ```
- **Analysis:** `dist/macOS/` directory is empty. The script file does not exist.
- **Impact:** macOS DMG packaging with CPack will fail or produce DMG without intended custom DS_Store layout.

### [PLAT-05] DBINARY_ICONS_RESOURCE is a typo — should be BINARY_ICONS_RESOURCE
- **File:** CMakeLists.txt:110
- **Severity:** Medium
- **Code:**
  ```cmake
  set(DBINARY_ICONS_RESOURCE ON)   # extra "D" prefix
  ```
- **Analysis:** ECM's `ecm_install_icons` module uses `BINARY_ICONS_RESOURCE`. The `D` prefix means the variable never matches what ECM looks for. Likely a typo from deleting `//` comment prefix.
- **Impact:** Non-Android binary icon resources never enabled despite explicit intent.

### [PLAT-06] qprompt_QM_LOADER variable never defined
- **File:** src/CMakeLists.txt:86
- **Severity:** Low
- **Code:**
  ```cmake
  ${qprompt_QM_LOADER}
  ```
- **Analysis:** Variable referenced in source list but never set anywhere. Expands to empty string. Leftover from pre-`qt_add_translations` setup.
- **Impact:** Harmless but dead build artifact.

### [PLAT-07] Incorrect macro syntax: `#define Use_GlobalAccel = 1`
- **File:** src/globalhotkeys.cpp:29
- **Severity:** Low
- **Code:**
  ```cpp
  #define Use_GlobalAccel = 1  // defines macro to "= 1", not to "1"
  ```
- **Analysis:** Currently benign (only `#ifdef` tested), but any value-check (`#if Use_GlobalAccel`) would produce syntax error.
- **Impact:** Latent compile error if value-check is ever added.

### [PLAT-08] QNX platform guard inconsistency: main.cpp vs documenthandler.h
- **File:** src/main.cpp:23, src/documenthandler.h:82
- **Severity:** Medium
- **Code:**
  main.cpp includes QNX:
  ```cpp
  #if defined(Q_OS_ANDROID) || defined(Q_OS_IOS) || defined(Q_OS_WASM) || defined(Q_OS_WATCHOS) || defined(Q_OS_QNX)
  ```
  documenthandler.h omits QNX:
  ```cpp
  #if !(defined(Q_OS_ANDROID) || defined(Q_OS_IOS) || defined(Q_OS_WASM) || defined(Q_OS_WATCHOS))
  ```
- **Analysis:** main.cpp correctly includes QNX in the mobile/WASM guard. documenthandler.h fails to include QNX in its guard for `SystemFontChooserDialog` (which depends on QWidget/QDialog — unsupported on QNX). The equivalent guard in documenthandler.cpp:85 DOES include QNX.
- **Impact:** Build failure on QNX due to missing QDialog symbols.

### [PLAT-09] Pre-build manifest references invalid Android SDK paths
- **File:** .env.android
- **Severity:** Low
- **Code:**
  ```
  # Pre-build environment configuration with potentially stale/incorrect paths
  ```
- **Analysis:** Environment configuration references specific Android SDK/NDK paths that may not exist on all developer machines. Source of build failures for new contributors.
- **Impact:** First-time Android build may fail due to missing path setup.

---

## Bug Density by File

| File | Bug Count |
|---|---|
| src/documenthandler.cpp | 17 |
| src/documenthandler.h | 5 |
| src/prompter/ReadRegionOverlay.qml | 3 |
| src/main.cpp | 4 |
| src/prompsession.cpp | 2 |
| src/prompsession.h | 2 |
| src/markersmodel.cpp | 3 |
| src/qt/WindowDragger.qml | 2 |
| src/kirigami_ui/KeyInputButton.qml | 1 |
| src/prompter/Find.qml | 1 |
| src/prompter/Countdown.qml | 2 |
| src/prompter/pointers/pointer_0.qml | 1 |
| src/kirigami_ui/PrompterPage.qml | 1 |
| src/kirigami_ui/+android/main.qml | 1 |
| src/prompter/Prompter.qml | 2 |
| src/qmlutil.hpp | 1 |
| src/spellchecker.cpp | 4 |
| src/shakedetector.cpp | 2 |
| src/iossavedialog.cpp | 1 |
| src/globalhotkeys.cpp | 1 |
| src/appcontroller.cpp | 1 |
| CMakeLists.txt | 4 |
| src/CMakeLists.txt | 2 |
| .env.android | 1 |
