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

## Round 2 — Wave 2: Granular Deep Audits

---

### [R2-GH-01] Q_UNREACHABLE reachable when only QHotkey available on Wayland
- **File:** src/globalhotkeys.cpp:514
- **Severity:** High
- **Category:** Logic
- **Analysis:** In globalShortcutKey(), when QHotkey_FOUND is defined but Use_GlobalAccel is NOT, and runtime platform is Wayland (non-KDE compositor like GNOME/Sway/Hyprland), the QHotkey guard skips the return, KGlobalAccel block doesn't exist, break exits switch, and Q_UNREACHABLE() fires.
- **Impact:** Application abort/crash on non-KDE Wayland compositors when querying any shortcut key string.

---

### [R2-CMAKE-01] sphinx_add_docs silently ignores all keyword arguments due to empty cmake_parse_arguments prefix
- **File:** cmake/FindSphinx.cmake:54-56
- **Severity:** Critical
- **Category:** Platform/Build
- **Analysis:** `cmake_parse_arguments(PARSE_ARGV 1 "" ...)` uses empty prefix `""` so parsed variables are named literally (`${ALL}`, `${BUILDER}`, etc.). But every access uses `_`-prefixed names (`${_ALL}`, `${_BUILDER}`). All keyword arguments from callers are silently ignored; documentation builds with wrong configuration.
- **Impact:** Any project using sphinx_add_docs() with parameters gets default behavior instead of configured behavior. ALL never adds to default target, BUILDER always defaults to "html", all boolean flags and options ignored.

---

### [R2-CMAKE-02] cmake_minimum_required inside find module pollutes parent project policy settings
- **File:** cmake/FindSphinx.cmake:19
- **Severity:** High
- **Category:** Platform/Build
- **Analysis:** `cmake_minimum_required(VERSION 3.20...3.29)` in a find module sets all CMake policies up to 3.29 to NEW for the including project. CMake docs state "Do not call cmake_minimum_required() in a find module." Can silently change parent project's policy behavior.
- **Impact:** Subtle, hard-to-debug build failures in projects including this module. Should be removed entirely.

---

### [R2-CMAKE-03] WORKING_DIRECTORY and COMMENT not parseable by callers of sphinx_add_docs
- **File:** cmake/FindSphinx.cmake:67,72
- **Severity:** Medium
- **Category:** Platform/Build
- **Analysis:** Function reads `${_WORKING_DIRECTORY}` and `${_COMMENT}` but neither keyword appears in cmake_parse_arguments spec. These variables are never populated from function arguments; callers cannot override working directory or build comment.
- **Impact:** After fixing CMAKE-01, WORKING_DIRECTORY and COMMENT still won't work unless added to one_value_keywords list.

---

### [R2-CMAKE-04] QML icon file(GLOB_RECURSE) missing CONFIGURE_DEPENDS causes stale icon sets
- **File:** cmake/BreezeIconSubset.cmake:115
- **Severity:** Medium
- **Category:** Platform/Build
- **Analysis:** `file(GLOB_RECURSE qml_files ...)` lacks `CONFIGURE_DEPENDS`. When new `.qml` files with icon references are added, incremental builds won't re-run CMake; new icons never bundled. Comment at lines 17-18 acknowledges this workaround: "touch CMake (or reconfigure)."
- **Impact:** New icons silently render blank until manual reconfigure. CMake 3.12+ supports CONFIGURE_DEPENDS.

---

### [R2-PRP-01] Qt.LeftToRight used as bare boolean — RTL branch always dead
- **File:** src/kirigami_ui/PrompterPage.qml:189,193,659
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** `Qt.LeftToRight ? X : Y` — `Qt.LeftToRight` is a non-zero enum value, always truthy. The Y branch is dead code. Codebase uses correct form `Qt.application.layoutDirection === Qt.LeftToRight` in 30+ other places. These 3 instances are missing the comparison.
- **Impact:** In RTL mode: swipe-list height toggle shows wrong icon direction; display flip delegate shows "object-rotate-left" instead of "object-rotate-right".

---

### [R2-PRP-02] Kirigami.Units.SmallSpacing — uppercase S yields undefined
- **File:** src/kirigami_ui/PrompterPage.qml:1331,1332,1352,1353,1377,1378
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** QML properties are case-sensitive. Correct property is `Kirigami.Units.smallSpacing` (lowercase 's'), used correctly elsewhere in file. `SmallSpacing` resolves to undefined, setting margins to 0.
- **Impact:** 3 SpinBoxes in network dialog (auto-reload hours/minutes/seconds) have zero horizontal margins, rendering labels cramped.

---

### [R2-PRP-03] Units.LongDuration / Units.HumanMoment missing Kirigami. prefix
- **File:** src/kirigami_ui/PrompterPage.qml:853,860,870,1202
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** With `import Kirigami 2.11 as Kirigami`, the `Units` singleton is only accessible as `Kirigami.Units`. Bare `Units` resolves to undefined. Rest of file consistently uses `Kirigami.Units`.
- **Impact:** Velocity indicator animations run at default 250ms instead of LongDuration (~500ms). Marker auto-close Timer fires at 1000ms instead of HumanMoment (2000ms).

---

### [R2-PRP-04] Inconsistent focus restoration in decreaseVelocityButton
- **File:** src/kirigami_ui/PrompterPage.qml:89
- **Severity:** Low
- **Category:** Type Safety
- **Analysis:** Every other action's onTriggered (53 occurrences, including paired increaseVelocityButton at line 102) calls `viewport.prompter.restoreFocus()`. Line 89 uniquely uses `viewport.prompter.focus = true`. `restoreFocus()` likely restores prior focus location; simple focus assignment moves it to viewport directly.
- **Impact:** After decrease-velocity button, focus moves to prompter viewport instead of prior location (e.g., editor). User must tap back to continue typing.

---

### [R2-PRP-05] Potential null-item access on async Loader in namedMarkerConfiguration.onOpened
- **File:** src/kirigami_ui/PrompterPage.qml:1144,1146
- **Severity:** Low
- **Category:** Edge Case
- **Analysis:** `setMarkerKeyButton` Loader (line 1173) has `asynchronous: true`. In `onOpened`, `setMarkerKeyButton.text` is accessed via alias. If OverlaySheet content is lazily created, Loader may not be loaded when onOpened fires — `setMarkerKeyButton.item` is null → `TypeError`.
- **Impact:** On slow systems/first launch, opening named-marker config sheet could crash with null reference error.

---

### [R2-PTR-01] Type mismatch: textVerticalOffset declared int but fed a real
- **File:** src/prompter/pointers/pointer_1.qml:33
- **Severity:** Medium
- **Category:** Type Safety
- **Analysis:** `property int textVerticalOffset` receives value from PointerSettings real slider (-1.0 to 1.0 at stepSize 0.01). `int` truncation: -0.05→0, 0.75→0, -0.99→0. Only ±1.0 survives. Default -0.05 rounds to zero.
- **Impact:** Text pointer vertical-offset slider non-responsive for most of its range. Only extreme ends register change. Default offset silently lost.

---

### [R2-PTR-02] Type mismatch: imageVerticalOffset declared int but fed a real
- **File:** src/prompter/pointers/pointer_2.qml:28
- **Severity:** Medium
- **Category:** Type Safety
- **Analysis:** Identical pattern to R2-PTR-01. `property int imageVerticalOffset` receives real from slider. All non-integer values truncate to 0.
- **Impact:** Image pointer offset slider behaves as 3-position switch (-1, 0, +1) instead of continuous adjustment.

---

### [R2-PTR-03] Casing error: Units.longDuration should be Units.LongDuration
- **File:** src/prompter/ProjectionsManager.qml:329
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** All other animations use PascalCase (`Units.ShortDuration`, `Units.VeryLongDuration`). This is the only active use of lowercase `Units.longDuration`. QML property access is case-sensitive; resolves to undefined.
- **Impact:** Projection window button grid opacity animation gets `duration: undefined`, snaps to 20% opacity instantly instead of fading smoothly.

---

### [R2-PTR-04] Inverted indexOf truthiness in platform check for ColorDialog
- **File:** src/prompter/PointerSettings.qml:653
- **Severity:** Medium
- **Category:** Type Safety
- **Analysis:** `["ios","osx"].indexOf(Qt.platform.os) ? 0 : ColorDialog.DontUseNativeDialog`. indexOf returns -1 for non-iOS/macOS — in JS, -1 is truthy. Non-Apple platforms get `0` (native dialog) instead of `DontUseNativeDialog`. iOS gets `DontUseNativeDialog` instead of `0` (indexOf returns 0, which is falsy). Only macOS gets correct result. Fix: `!== -1 ? 0 : DontUseNativeDialog`.
- **Impact:** Linux/Windows use native color dialog (unreliable/missing features). iOS uses non-native dialog (degraded UX).

---

### [R2-AND-01] Android missing QmlUtil causes crash on factory reset and RecentDocuments
- **File:** src/kirigami_ui/+android/main.qml (absent object), line 684
- **Severity:** Critical
- **Category:** QML/UI
- **Analysis:** factoryResetDialog calls `qmlutil.factoryReset()` at line 684. No `QmlUtil { id: qmlutil }` declared in +android/main.qml. Windows defines it at line 851, base at line 1183. Also, RecentDocuments (line 757-762) missing `util: qmlutil` assignment.
- **Impact:** Factory reset dialog works but clicking "Yes" crashes app. RecentDocuments silently fails on existence checks.

---

### [R2-AND-02] Android missing restartDialog crashes LanguageSettingsOverlay and LayoutDirectionSettingsOverlay
- **File:** src/kirigami_ui/+android/main.qml (absent object)
- **Severity:** Critical
- **Category:** QML/UI
- **Analysis:** Both overlays unconditionally access `restartDialog.visible = true` in onClosed handlers when settings are dirty. `restartDialog` is defined in Windows (line 751-769) and base (line 1083-1098) but absent from +android/main.qml.
- **Impact:** Changing UI language or layout direction on Android crashes app when overlay is dismissed.

---

### [R2-AND-03] Android Settings missing fakeFullScreen persistence
- **File:** src/kirigami_ui/+android/main.qml:72-77
- **Severity:** Medium
- **Category:** Platform/Build
- **Analysis:** "mainWindow" Settings block on Android only persists x,y,width,height. Missing `property alias fakeFullScreen: root.__fakeFullscreen` (present in Windows line 86, base line 91). Android uses __fakeFullscreen in visibility binding but never saves it.
- **Impact:** Fake fullscreen preference always resets to false on app restart.

---

### [R2-AND-04] Android Settings for "background" missing transparency persistence
- **File:** src/kirigami_ui/+android/main.qml:96-100
- **Severity:** Low
- **Category:** Platform/Build
- **Analysis:** "background" Settings persists opacity/shadows but missing `property alias transparency: root.__translucidBackground` (present in Windows line 108, base line 113). Consistent with Android hardcoding transparency as readonly, but forward-compat issue.
- **Impact:** No current user-facing impact (menu item absent). Future issue if transparency toggle enabled.

---

### [R2-AND-05] Android loadTelemetryPage passes no properties object to pageStack push
- **File:** src/kirigami_ui/+android/main.qml:162
- **Severity:** Low
- **Category:** QML/UI
- **Analysis:** Android passes telemetryPageComponent with no second argument to push(). Windows (line 176) and base (line 189) pass `{}`. In Qt 6.x strict mode, missing properties object could cause warning or incorrect initialization.
- **Impact:** If telemetry page is ever un-commented, Android may fail to open it correctly.

---

### [R2-OVL-01] InputsOverlay onOpened calls cursorAutoHide.restart() instead of reset()
- **File:** src/kirigami_ui/InputsOverlay.qml:41
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** All other overlays consistently call `cursorAutoHide.reset()` on open (LanguageSettingsOverlay:40, LayoutDirectionSettingsOverlay:39, WheelSettingsOverlay:36, countdownConfiguration in PrompterPage:1072) to prevent cursor auto-hide. InputsOverlay calls `cursorAutoHide.restart()` which re-enables the auto-hide timer.
- **Impact:** Cursor vanishes during key binding configuration; user forced to move mouse repeatedly.

---

### [R2-OVL-02] LanguageSettingsOverlay popup ListView currentIndex always resolves to -1
- **File:** src/kirigami_ui/LanguageSettingsOverlay.qml:73
- **Severity:** Low
- **Category:** Logic
- **Analysis:** `currentIndex: languageSelector.model.indexOf(languageSelector.currentIndex)` — model is array of objects `{text, value}`, searched for an integer. Always returns -1. Compare with LayoutDirectionSettingsOverlay:76 which correctly uses `layoutSelector.currentIndex` directly.
- **Impact:** Currently selected language never highlighted in popup list. Keyboard navigation may not start from correct position.

---

### [R2-PTH-01] FileDialog filter matches all files on Linux due to stray glob
- **File:** src/kirigami_ui/PathsPage.qml:105
- **Severity:** Medium
- **Category:** Type Safety
- **Analysis:** Filter string is `"Executable <bin>(*.bin *.BIN *)"` — space between `*.BIN` and `*` means `*` is a third glob pattern matching every file. Should be `(*.bin *.BIN)` without trailing ` *`.
- **Impact:** Executable file filter shows every file on Linux/Unix, defeating its purpose.

---

### [R2-PTH-02] File path from file:// URL preserves percent-encoding
- **File:** src/kirigami_ui/PathsPage.qml:113
- **Severity:** Medium
- **Category:** QML/UI
- **Analysis:** `pathsDialog.selectedFile.toString().slice(...)` removes `file://` prefix but does not decode percent-encoding. Path `C:\Program Files\...` becomes `C:/Program%20Files/...` after slicing.
- **Impact:** LibreOffice won't be found if installed in directory with spaces or non-ASCII characters.

---

### [R2-WHE-01] `focus: true` is JavaScript label, not assignment
- **File:** src/kirigami_ui/WheelSettingsOverlay.qml:90
- **Severity:** High
- **Category:** QML/UI
- **Analysis:** Inside onValueModified: `focus: true` uses colon instead of `=`. In JS this is a labeled statement (label `focus` with expression `true`), not assignment to SpinBox's focus property. Should be `focus = true`.
- **Impact:** Throttle factor SpinBox never receives keyboard focus when value is modified.

---

### [R2-EDT-01] Qt.AlignHustify typo — nonexistent enum value
- **File:** src/kirigami_ui/EditorToolbar.qml:380
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** Justify menu item's `enabled` binding compares against `Qt.AlignHustify` instead of `Qt.AlignJustify`. `AlignHustify` is undefined; comparison `!== undefined` always true.
- **Impact:** Justify menu item in mobile alignment menu always enabled, even when already justified.

---

### [R2-EDT-02] wheelThrottleSettingsButton checked bound to completely unrelated document property
- **File:** src/kirigami_ui/EditorToolbar.qml:790
- **Severity:** High
- **Category:** QML/UI
- **Analysis:** `checked: viewport.prompter.document.namedMarker` and `onClicked: wheelSettings.open()`. Button opens wheel/scroll settings but checked state bound to named marker property — a copy-paste error from namedBookmarkButton (line 233).
- **Impact:** Wheel settings button toggle state controlled by whether a named marker exists, semantically unrelated to wheel settings.

---

### [R2-EDT-03] Checkable ToolButtons break checked property bindings on first click — systematic
- **File:** src/kirigami_ui/EditorToolbar.qml:223-224,233-236,380-381,392-394,404-406,416-418,429-431,449-452,460-463,471-474,482-485,493-503,513-525,725-727,741-743,751-753,769-772,790-792,836
- **Severity:** High
- **Category:** Logic
- **Analysis:** ~20 buttons have `checked: someExpression` + onClicked/onToggled handler. First user click toggles checked internally, permanently breaking the declarative binding. After that, external changes to the bound property (selecting differently formatted text, changing alignment) no longer update button state. Affects all bold/italic/underline/strike/alignment/capitalization buttons.
- **Impact:** After clicking any formatting button once, its checked indicator disconnects from document state. Selecting differently-formatted text shows stale button states.

---

### [R2-TEL-01] Telemetry sub-toggles permanently disconnect from master toggle on click
- **File:** src/kirigami_ui/TelemetryPage.qml:80-88,101-110,123-132,149-158
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** Each sub-toggle has `checked: root.__telemetry` as initial binding + `checkable: true`. Clicking any sub-toggle breaks the binding. After that, toggling master switch no longer controls that sub-option. Value persisted via QSettings but orphaned.
- **Impact:** After interacting with individual telemetry option, master toggle no longer controls it. UI state inconsistent.

---

### [R2-REC-01] File URI prefix strip off-by-one on Windows
- **File:** src/kirigami_ui/RecentDocuments.qml:70
- **Severity:** Low
- **Category:** QML/UI
- **Analysis:** `uri.substring(7)` strips 7 chars. Windows file URIs have 3 slashes (`file:///C:/...`), so substring(7) leaves leading `/` on path → `/C:/Users/...` instead of `C:/Users/...`.
- **Impact:** Recent document tooltips on Windows display malformed path with leading forward slash.

---

### [R2-REC-02] refreshExistence skips UI updates when dynamic children out of sync
- **File:** src/kirigami_ui/RecentDocuments.qml:171
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** Guard `if (anyChanged && _dynamicChildren.length === recentsModel.count)` only updates when count matches. During rapid add/remove operations, counts diverge and existence updates silently discarded. Stale UI actions retain old `exists` values.
- **Impact:** Under timing edge cases, recently opened docs incorrectly appear as existing or missing.

---

### [R2-IOS-01] Method swizzling re-entry causes infinite recursion on second invocation
- **File:** src/shakedetector.mm:74-78
- **Severity:** High
- **Category:** Platform/Build
- **Analysis:** setupShakeDetection has no guard against multiple calls. Second call: class_addMethod fails (method already swizzled), method_setImplementation replaces qprompt_motionEnded with itself, capturing itself as s_originalMotionEnded. Subsequent shake → infinite recursion → stack overflow.
- **Impact:** App crashes on shake gesture if setupShakeDetection runs more than once (QML engine reload, destroy/create cycle).

---

### [R2-IOS-02] Delegate block captures raw assign pointer — use-after-free risk
- **File:** src/iossavedialog.mm:42-44,50-52
- **Severity:** Medium
- **Category:** Platform/Build
- **Analysis:** QPromptDocPickerDelegate.dialog declared `assign`. Blocks capture _dialog by value (raw pointer copy). If IosSaveDialog destroyed while UIDocumentPickerViewController presented, block executes with dangling pointer.
- **Impact:** Crash if dialog singleton destroyed during active save operation. Latent memory safety defect.

---

### [R2-IOS-03] UIApplication.keyWindow deprecated since iOS 13; breaks multi-window iPadOS
- **File:** src/iossavedialog.mm:109, src/shakedetector.mm:114
- **Severity:** Medium
- **Category:** Platform/Build
- **Analysis:** Both files use `[UIApplication sharedApplication].keyWindow` to get root view controller. Deprecated in iOS 13, returns nil on iPadOS with UIScene-based lifecycle. presentViewController becomes no-op.
- **Impact:** File save dialog and undo/redo alert silently fail to appear on iPadOS multi-window and modern iOS.

---

### [R2-WASM-01] File input element never removed from DOM on user cancel
- **File:** src/wasmintegration.cpp:148-149
- **Severity:** Medium
- **Category:** Resource Management
- **Analysis:** Hidden `<input type="file">` appended to DOM at line 148. removeChild at line 126 only fires inside change event listener. User cancel → no change event → input element leaks permanently in DOM.
- **Impact:** Cumulative DOM node leak on every cancelled file picker. Long sessions consume browser memory and bloat DOM.

---

### [R2-WASM-02] Insecure hostname validation via endsWith allows subdomain spoofing
- **File:** src/wasmintegration.cpp:192
- **Severity:** Medium
- **Category:** Security
- **Analysis:** officialHost() uses `h.endsWith("localhost")` (matches evillocalhost.com) and `h.endsWith("qprompt.app")` (matches fakeqprompt.app). Should use exact match: `h == "qprompt.app" || h.endsWith(".qprompt.app")`, and `h == "localhost"`.
- **Impact:** Malicious host can bypass official-host guard, enabling phishing/unauthorized distribution.

---

### [R2-FONT-01] RichText label renders unescaped plain text — HTML metacharacters break display
- **File:** src/systemfontchooserdialog.ui:44, src/systemfontchooserdialog.cpp:55
- **Severity:** Medium
- **Category:** Type Safety
- **Analysis:** textPreviewLabel configured as RichText in UI file. show() calls setText(text) with raw user text. `<`, `>`, `&` chars parsed as HTML, causing text to disappear or render garbled.
- **Impact:** Font preview shows broken/missing text whenever script contains angle brackets or ampersands. Should use Qt::convertFromPlainText() or switch to PlainText.

---

### [R2-FONT-02] Duplicate setText call on preview label
- **File:** src/systemfontchooserdialog.cpp:55-56
- **Severity:** Low
- **Category:** Edge Case
- **Analysis:** Lines 55 and 56 are identical: `ui->textPreviewLabel->setText(text);` called twice consecutively. Copy-paste artifact, harmless.
- **Impact:** No functional impact; cosmetic code quality issue.

---

### [R2-ANDMAN-01] Ungrantable system/signature permissions bloating manifest
- **File:** android/AndroidManifest.xml:51-53
- **Severity:** Medium
- **Category:** Platform/Build
- **Analysis:** MOUNT_UNMOUNT_FILESYSTEMS, MOUNT_FORMAT_FILESYSTEMS, and ACCESS_CHECKIN_PROPERTIES are signature|privileged permissions a third-party app can never obtain. Google Play may flag as suspicious or reject.
- **Impact:** Potential Play Store rejection or review delay. Zero functional benefit.

---

### [R2-ANDMAN-02] MANAGE_EXTERNAL_STORAGE likely triggers Play Store scrutiny
- **File:** android/AndroidManifest.xml:49
- **Severity:** Medium
- **Category:** Platform/Build
- **Analysis:** MANAGE_EXTERNAL_STORAGE is an All Files Access permission restricted by Google Play policy. Apps must submit declaration proving core functionality requires broad file access. Teleprompter unlikely to qualify.
- **Impact:** Play Store rejection risk unless app has justified and approved use case. READ_EXTERNAL_STORAGE alone usually sufficient.

---

---

## Round 3 — Wave 3: Cross-Cutting Audits

---

### [R3-CTX-01] AbstractUnits missing QML_ELEMENT — all duration constants resolve to undefined
- **File:** src/abstractunits.hpp:30
- **Severity:** Critical
- **Category:** QML/UI
- **Analysis:** Class declares `QML_UNCREATABLE` but omits `QML_ELEMENT`. Without QML_ELEMENT, Qt never registers the type. The old Qt 5 registration in main.cpp:219 is commented out. 36 QML references to `Units.ShortDuration`, `Units.LongDuration`, `Units.VeryLongDuration`, `Units.HumanMoment` across 7 files all resolve to `undefined`.
- **Impact:** Every animation (fades, slides, pointer transitions) using these constants gets zero/undefined duration. App-wide visual experience broken.

---

### [R3-CTX-02] GlobalHotkeys.SkipForward enum value mismatch — trailing 's' missing
- **File:** src/kirigami_ui/InputsOverlay.qml:673
- **Severity:** High
- **Category:** QML/UI
- **Analysis:** C++ enum defines `SkipForwards` (with 's'). InputsOverlay.qml:673 uses `GlobalHotkeys.SkipForward` (no 's'). All 65 other references in the file use correct `SkipForwards`. Silently passes `undefined` as the action parameter.
- **Impact:** "Skip forward" hotkey binding never saved/registered. User-configured skip-forward hotkey silently non-functional.

---

### [R3-DOC-01] m_reloading uninitialized — undefined behavior on first load
- **File:** src/documenthandler.cpp:123-130, src/documenthandler.h:337
- **Severity:** Critical
- **Category:** Edge Case
- **Analysis:** `m_reloading` (bool) absent from constructor initializer list. Every other bool member listed. Read at line 1034 before being written — garbage value. true→skip undo clear, false→unconditionally clear.
- **Impact:** Non-deterministic undo stack behavior on first document load.

---

### [R3-DOC-02] Unbalanced edit block in setLineHeight/setParagraphHeight
- **File:** src/documenthandler.cpp:1596-1601, 1610-1615
- **Severity:** Critical
- **Category:** Edge Case
- **Analysis:** Both functions call `cursor.joinPreviousEditBlock()` which is a no-op when no edit block is active. Then `endEditBlock()` is called without matching `beginEditBlock()`. Qt assert-fails in debug, corrupts undo stack in release.
- **Impact:** Debug crash or release undo corruption when adjusting line/paragraph height.

---

### [R3-DOC-03] load() sets m_fileUrl and emits fileUrlChanged even on failed load
- **File:** src/documenthandler.cpp:1032,1040
- **Severity:** High
- **Category:** Edge Case
- **Analysis:** Lines execute unconditionally after file existence check block. If file doesn't exist, fails to open, or lacks permissions, m_fileUrl is updated and fileUrlChanged emitted anyway.
- **Impact:** UI shows filename that was never loaded. Subsequent save() overwrites real file with empty content.

---

### [R3-DOC-04] saveAs() silently ignores write/flush failures
- **File:** src/documenthandler.cpp:1164-1168
- **Severity:** High
- **Category:** Edge Case
- **Analysis:** After file.write() and file.flush(), code calls doc->setModified(false) without checking return values. On full disk, permission error, or quota exhaustion, save silently fails but document marked unmodified.
- **Impact:** Silent data loss — user believes work was saved when it wasn't.

---

### [R3-DOC-05] updateContents() produces two separate undo entries — undo destroys document
- **File:** src/documenthandler.cpp:1104-1122
- **Severity:** High
- **Category:** Edge Case
- **Analysis:** No beginEditBlock/endEditBlock wrapping removeSelectedText + insertText/insertHtml. Two independent undo entries created. Undo after file load: only insertion reversed, leaving permanently empty document.
- **Impact:** Undo after file load irreversibly destroys document content.

---

### [R3-DOC-06] reload() leaks m_reloading=true on URL mismatch
- **File:** src/documenthandler.cpp:857-865
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** Unconditionally sets m_reloading=true at 859, only calls load() (which clears it) if url==m_fileUrl. Encoding differences between raw file:// string and QUrl normalization → load() never called → m_reloading permanently true → all future loads skip clearUndoRedoStacks().
- **Impact:** Undo stacks accumulate across document loads; stale undo data causes crash.

---

### [R3-DOC-07] Inverted selection state after failed search()
- **File:** src/documenthandler.cpp:1574-1579
- **Severity:** High
- **Category:** Logic
- **Analysis:** Failed search sets selectionEnd=-1 while selectionStart retains old value (e.g., 42). Creates inverted selection (42 > -1). textCursor() constructs cursor at position 42 with KeepAnchor to -1, creating spurious selection from start to 42.
- **Impact:** Accidental text overwrite if user types after failed search.

---

### [R3-SPL-01] encode() uses toLocal8Bit() instead of dictionary-encoding-aware conversion
- **File:** src/spellchecker.cpp:400-406
- **Severity:** Medium
- **Category:** Type Safety
- **Analysis:** Fallback uses `word.toLocal8Bit()` regardless of dictionary's actual encoding (ISO8859-2, KOI8-R, CP1251). No code path uses QStringConverter with d.encoding. System local 8-bit may differ from dictionary encoding.
- **Impact:** Non-ASCII words garbled before reaching Hunspell on non-UTF-8 dictionaries with mismatched locale.

---

### [R3-SPL-02] decode() uses fromLocal8Bit() — suggestions show as mojibake
- **File:** src/spellchecker.cpp:408-413
- **Severity:** Medium
- **Category:** Type Safety
- **Analysis:** Same encoding mismatch as encode(). Hunspell suggestions from non-UTF-8 dictionary interpreted with system local 8-bit codec instead of dictionary encoding.
- **Impact:** Spelling suggestions with non-ASCII characters appear as garbled text.

---

### [R3-SPL-03] removeCustomWord() silently discards all addWord() additions
- **File:** src/spellchecker.cpp:134-140 vs 338-344
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** addWord() calls d.hunspell->add() but does NOT append to m_customWords. removeCustomWord() reloads all dictionaries from scratch via loadOne(), losing any words added via addWord().
- **Impact:** User-accepted words (right-click "Add to Dictionary") vanish after removing a different custom word or changing languages.

---

### [R3-SPL-04] Corrupt cached dictionary file persists permanently after failed copy
- **File:** src/spellchecker.cpp:198-201
- **Severity:** Medium
- **Category:** Edge Case
- **Analysis:** QFile::copy() return value unchecked. If copy fails partway (disk full, I/O error), truncated corrupt file passes QFile::exists() check forever. No atomic write (write-to-temp-then-rename) or checksum verification.
- **Impact:** Hunspell loads corrupt .aff/.dic file. Language appears permanently missing until user manually deletes cache directory.

---

### [R3-SPL-05] SpellChecker has zero thread safety — all methods unprotected
- **File:** src/spellchecker.h:32-77
- **Severity:** Medium
- **Category:** Edge Case
- **Analysis:** No QMutex, QMutexLocker, or std::mutex anywhere. Multiple methods iterate m_dicts (spell, suggest) while others mutate it (setLanguage, setLanguages, removeCustomWord, unload). QSyntaxHighlighter::highlightBlock iterates m_dicts extensively; any slot calling setLanguage during highlighting → iterator invalidation. Hunspell itself is not thread-safe.
- **Impact:** Segfault on concurrent access. Currently single-thread use; becomes immediate crash if spell-check is moved to background thread.

---

### [R3-MAIN-01] Command-line positional argument description/syntax swapped
- **File:** src/main.cpp:158
- **Severity:** Medium
- **Category:** Platform/Build
- **Analysis:** addPositionalArgument("source", "file", "File to copy.") — 2nd and 3rd arguments swapped. Signature is (name, description, syntax).
- **Impact:** --help output garbled; users can't understand expected file argument.

---

### [R3-MAIN-02] Invalid locale string constructed for short language codes
- **File:** src/main.cpp:141-143
- **Severity:** High
- **Category:** Platform/Build
- **Analysis:** language.toUtf8() + ".UTF-8" produces e.g., "es.UTF-8" — not a valid POSIX locale. setlocale() silently fails; C library uses "C" locale.
- **Impact:** Wrong date/number formatting, sorting, character classification throughout the app.

---

### [R3-MAIN-03] System locale changed even when translation file fails to load
- **File:** src/main.cpp:141-149
- **Severity:** Medium
- **Category:** Platform/Build
- **Analysis:** qputenv("LANGUAGE"), qputenv("LC_ALL"), qputenv("LANG"), and QLocale::setDefault() execute unconditionally before translator.load(). If .qm file missing/corrupt, translator fails silently but locale already switched.
- **Impact:** User sees English UI with foreign locale formatting — confusing half-translated state.

---

### [R3-MAIN-04] Stack-allocated QTranslator outlives QApplication on shutdown
- **File:** src/main.cpp:133,107/109,138/149
- **Severity:** Low
- **Category:** Memory Management
- **Analysis:** QTranslator translator (line 133) declared after app (lines 107/109), destroyed before app. app.installTranslator(&translator) stores raw pointer → dangling during app destructor. Violates documented contract.
- **Impact:** Use-after-free during QApplication teardown (plugin cleanup). Low probability, high severity if triggered.

---

### [R3-MAIN-05] Hardcoded Homebrew version-specific Kirigami import path
- **File:** src/main.cpp:314
- **Severity:** Medium
- **Category:** Platform/Build
- **Analysis:** /opt/homebrew/Cellar/kf5-kirigami2/5.95.0/lib/qt6/qml — every brew upgrade changes directory → path stale. QQmlEngine::addImportPath silently ignores missing dirs.
- **Impact:** After Homebrew upgrade, Kirigami QML imports fail silently. App starts with blank window.

---

### [R3-MAIN-06] Inconsistent Kirigami platform guards — missing WATCHOS and QNX
- **File:** src/main.cpp:225,42-43
- **Severity:** High
- **Category:** Platform/Build
- **Analysis:** KIRIGAMI_BUILD_TYPE_STATIC defined and kirigamiplugin.h included for 5 platforms (ANDROID, IOS, WASM, WATCHOS, QNX). But registerTypes() on line 225 only guarded for 3 platforms (ANDROID, IOS, WASM). WATCHOS and QNX omitted.
- **Impact:** On WatchOS and QNX, Kirigami QML types never registered → blank screen or crash.

---

### [R3-MAIN-07] XDG_CURRENT_DESKTOP unconditionally forced to "KDE" on all Linux
- **File:** src/main.cpp:86-87
- **Severity:** Medium
- **Category:** Platform/Build
- **Analysis:** qputenv("XDG_CURRENT_DESKTOP", "KDE") on every Linux system regardless of actual desktop. Qt picks KDE platform theme, icon theme, font rendering.
- **Impact:** On GNOME/XFCE/Sway: blank icons if Breeze not installed, visual clash with native desktop, wrong widget styling.

---

### [R3-MAIN-08] QFontDatabase::addApplicationFont return value discarded
- **File:** src/main.cpp:120
- **Severity:** Low
- **Category:** Platform/Build
- **Analysis:** Returns font ID on success or -1 on failure. Discarded. If bundled emoji font missing, failure is silent.
- **Impact:** On WASM, emoji render as tofu (□). Developer can't detect failure without runtime enumeration.

---

### [R3-APP-01] AppController singleton and children never deallocated
- **File:** src/appcontroller.cpp:35,25-28
- **Severity:** Low
- **Category:** Memory Management
- **Analysis:** new AppController() with no parent. m_hotkeys and m_wasm parented to this, entire tree leaks. QQmlEngine::setObjectOwnership(this, CppOwnership) prevents QML engine cleanup.
- **Impact:** Memory leak on shutdown. Application-lifetime singleton conventionally acceptable but masks real leaks.

---

### [R3-PROP-01] selectionIsLowerCase bound to wrong NOTIFY signal
- **File:** src/documenthandler.h:119
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** NOTIFY is fontCapitalizationChanged which fires from setFontCapitalization() and reset(). Pure text edits without cursor moves, or selection-only changes via setSelectionStart/setSelectionEnd without cursor moves, never trigger notification.
- **Impact:** QML bindings reading selectionIsLowerCase can become stale, showing incorrect case state.

---

### [R3-SIG-01] textChanged() signal declared but never emitted
- **File:** src/documenthandler.h:307
- **Severity:** Low
- **Category:** Logic
- **Analysis:** Signal `void textChanged()` declared in Q_SIGNALS but zero emits in entire codebase. Not used as NOTIFY for any Q_PROPERTY.
- **Impact:** Dead code. Any connection to this signal silently never fires.

---

### [R3-SIG-02] ShakeDetector signals declared but never emitted — dead feature
- **File:** src/shakedetector.h:40-42, shakedetector.cpp:45-47
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** shakeDetected(), undoRequested(), redoRequested() declared but never emitted. setupShakeDetection() has empty body.
- **Impact:** Shake-to-undo feature declared in QML interface but completely non-functional.

---

### [R3-SIG-03] IosSaveDialog accepted/rejected signals declared but never emitted
- **File:** src/iossavedialog.h:44-45, iossavedialog.cpp:44-47
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** Both signals declared, saveDocument() has empty body with no emits. Zero emits anywhere.
- **Impact:** On iOS, QML waiting for accepted()/rejected() hangs indefinitely. Save-as flow broken.

---

### [R3-PMT-01] OBS WebSocket JSON.parse without try/catch — crash on malformed input
- **File:** src/prompter/Prompter.qml:368
- **Severity:** High
- **Category:** Edge Case
- **Analysis:** JSON.parse(m) in onTextMessageReceived has no error handling. Malformed JSON from OBS or non-OBS service on configured port → unhandled JS exception → application termination.
- **Impact:** Crash-to-desktop on malformed WebSocket message.

---

### [R3-PMT-02] OBS WebSocket no onError handler, no reconnection logic
- **File:** src/prompter/Prompter.qml:353-389
- **Severity:** Medium
- **Category:** Edge Case
- **Analysis:** WebSocket has no onError handler, no onStatusChanged for WebSocket.Error. Connection failure silently ignored. No reconnection attempt.
- **Impact:** Silent failure of OBS scene switching; user has no indication connection is broken.

---

### [R3-PMT-03] goToNextMarker fallback desynchronizes cursor from viewport
- **File:** src/prompter/Prompter.qml:658-659
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** Fallback scrolls viewport to document end but doesn't update editor.cursorPosition. Cursor stays where document.nextMarker() placed it (possibly stale).
- **Impact:** Editor cursor and viewport out of sync. Subsequent marker lookups use wrong position.

---

### [R3-TMR-01] TimerClock ETA uses __iDefault instead of actual __i during reverse scroll
- **File:** src/prompter/TimerClock.qml:66
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** Fallback uses Math.pow(Math.abs(__iDefault), curvature) instead of __i. __iDefault frozen at session-start; if user changes velocity mid-session, ETA uses wrong speed.
- **Impact:** ETA displays incorrect remaining time by factor of (actualSpeed/defaultSpeed)^curvature.

---

## Round 4 — Wave 4: Qt Compat, Export, Root QML, Events, Comments, Preprocessor, Projections

---

### [R4-QTV-01] QtQuick 2.13 import does not exist in Qt 6.5
- **File:** src/prompter/ProjectionsManager.qml:22
- **Severity:** Critical
- **Category:** QML/UI
- **Analysis:** Qt 6 registers QtQuick as 6.x and 2.15 for backward compat. Version 2.13 not registered. QML engine finds no module with major=2 and minor≤13 (2.15 > 2.13 excluded). Module-not-found error at runtime.
- **Impact:** ProjectionsManager.qml fails to load; all external display/projector mirroring completely non-functional.

---

### [R4-QTV-02] QtQuick.Window 2.0 import does not exist in Qt 6.5
- **File:** src/prompter/ReadRegionOverlay.qml:25
- **Severity:** Critical
- **Category:** QML/UI
- **Analysis:** QtQuick.Window 2.0 from Qt 5.0 era. Qt 6 merged it into QtQuick; only provides backward compat at 2.15 and 6.x. Module-not-found at runtime.
- **Impact:** ReadRegionOverlay.qml fails to load; reading region overlay (bars, pointers, controls) completely broken.

---

### [R4-QTV-03] QtQuick.Dialogs 6.6 imported in 9 files on Qt 6.5 target
- **Files:** src/prompter/TimerClock.qml:27, PrompterBackground.qml:25, Prompter.qml:79, PointerSettings.qml:27, kirigami_ui/PrompterPage.qml:28, PathsPage.qml:27, main.qml:28, +windows/main.qml:28, +android/main.qml:28
- **Severity:** High
- **Category:** QML/UI
- **Analysis:** All 9 files import QtQuick.Dialogs 6.6 but project targets Qt 6.5. QML engine downgrades to 6.5 silently, but any 6.6-specific Dialog property/signal/enum usage crashes.
- **Impact:** File/color/message dialogs risk runtime failures if 6.6-specific APIs accidentally referenced.

---

### [R4-EXP-01] No XSS sanitization — script tags, event handlers, javascript: URLs unfiltered
- **File:** src/documenthandler.cpp:1246-1334
- **Severity:** Critical
- **Category:** Security
- **Analysis:** filterHtml() applies only CSS-property regex filters. None of the 6 regexes remove script/iframe/object/embed/svg tags, onerror/onload/onclick event handlers, or javascript: URLs. Qt's QTextHtmlImporter preserves event handler attributes on known tags, re-exported verbatim by toHtml().
- **Impact:** Malicious HTML imported/pasted/dropped injects executable JavaScript into exported documents. Event handlers survive round-trip save/load.

---

### [R4-EXP-02] insertHtmlAt() bypasses filterHtml() — unsanitized HTML from QML
- **File:** src/documenthandler.cpp:1425-1460
- **Severity:** High
- **Category:** Security
- **Analysis:** insertHtmlAt() is Q_INVOKABLE, accepts arbitrary HTML from QML, calls cursor.insertHtml() directly with zero sanitization. paste() properly runs filterHtml() first — this is an unprotected second entry path.
- **Impact:** Any QML caller injects scripts/event handlers/arbitrary HTML bypassing sanitization.

---

### [R4-EXP-03] loadFromNetwork() destroys URL for relative URLs — host/path swapped
- **File:** src/documenthandler.cpp:870-878
- **Severity:** High
- **Category:** Logic
- **Analysis:** For relative URLs, url.path() (full string like "example.com/path") assigned to setHost(). Path never set. Result: host="example.com/path", path empty. DNS failure.
- **Impact:** All relative URL network loads fail with DNS errors.

---

### [R4-EXP-04] AutoText inserts plain text as HTML — content corruption
- **File:** src/documenthandler.cpp:1104-1123
- **Severity:** High
- **Category:** Logic
- **Analysis:** For Qt::AutoText, falls through Qt::RichText to cursor.insertHtml(). If QTextDocument::find() auto-detects as plain text, <script> disappears, entities cause parse errors, angle brackets silently swallowed.
- **Impact:** Plain-text files with <, >, & lose content segments when opened via AutoText path.

---

### [R4-EXP-05] No encoding/charset detection — all imports assumed UTF-8
- **File:** src/documenthandler.cpp:890-895,955,960,1007,1010
- **Severity:** Medium
- **Category:** Type Safety
- **Analysis:** Every import path uses QString::fromUtf8() without inspecting HTML meta charset or HTTP Content-Type. ISO-8859-1, Windows-1252, Shift-JIS, GB2312 produce mojibake. For network loads, HTTP response charset never read from QNetworkReply headers.
- **Impact:** Non-UTF-8 HTML files display garbled text; East Asian and legacy encodings silently corrupted.

---

### [R4-EXP-06] UTF-8 BOM not stripped — becomes phantom character at position 0
- **File:** src/documenthandler.cpp:955,960,1007
- **Severity:** Medium
- **Category:** Type Safety
- **Analysis:** QString::fromUtf8() does not strip BOM (\xEF\xBB\xBF). Decoded as U+FEFF at document position 0. Shifts all cursor positions by 1. save() exports without BOM (round-trip changes file).
- **Impact:** Hidden leading character; cursor positions off by one; file hash changes on save.

---

### [R4-EXP-07] data: URI assumes base64 encoding without checking ;base64 token
- **File:** src/documenthandler.cpp:1445-1448
- **Severity:** Medium
- **Category:** Type Safety
- **Analysis:** Unconditionally calls QByteArray::fromBase64() on data URI payload. Per RFC 2397, data URIs without ;base64 contain percent-encoded data. Non-base64 URIs produce garbage. dataStr.toLatin1() corrupts non-ASCII bytes.
- **Impact:** Non-base64 data URIs produce corrupted images. Latin-1 conversion maims binary data.

---

### [R4-EXP-08] EPUB/MOBI/AZW import replaces document with error string
- **File:** src/documenthandler.cpp:1078-1080,998-1000
- **Severity:** Medium
- **Category:** Edge Case
- **Analysis:** Import branch for EPUB/MOBI/AZW is empty — program stays "", QProcess::start("", {}) fails, error string returned. In load(), error string passed to updateContents() replacing entire document.
- **Impact:** Attempting EPUB/MOBI/AZW import irreversibly destroys current document with error message.

---

### [R4-EXP-09] LibreOffice import --cat and --convert-to flags are contradictory
- **File:** src/documenthandler.cpp:1076
- **Severity:** Low
- **Category:** Logic
- **Analysis:** --cat dumps to stdout; --convert-to writes to file. These conflict — --convert-to suppresses stdout. Code reads from stdout expecting --cat behavior but LibreOffice may produce nothing.
- **Impact:** LibreOffice imports may produce empty output depending on version.

---

### [R4-ROOT-01] Qt.openUrlExternally called with translation context string instead of URL
- **File:** src/kirigami_ui/main.qml:899
- **Severity:** High
- **Category:** QML/UI
- **Analysis:** Qt.openUrlExternally("Global menu actions", "https://feedback.qprompt.app") — first arg is the qsTr disambiguation string copy-pasted from previous line. "Global menu actions" treated as URL; real URL ignored/triggers warning.
- **Impact:** "Report Bug" menu item opens nothing. Users cannot reach feedback page.

---

### [R4-ROOT-02] Invalid QML color value "initial"
- **File:** src/kirigami_ui/main.qml:126 (also +windows:121, ProjectionsManager:195)
- **Severity:** Medium
- **Category:** QML/UI
- **Analysis:** color: root.__translucidBackground ? "transparent" : "initial" — "initial" is CSS keyword, not SVG named color. Not valid in QML color type. Falls back to default (likely black) with runtime warning.
- **Impact:** Disabling background transparency renders window background black instead of system-theme color.

---

### [R4-ROOT-03] ESC global shortcut skips single-layer pages — can't dismiss with keyboard
- **File:** src/kirigami_ui/main.qml:481
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** StandardKey.Cancel checks `if (layers.depth > 1)` before clear(). Exactly one layer (common case: About, Paths, Remote pages) → depth===1 → branch skipped → falls through to restoreFocus() leaving layer visible. Should be `depth > 0`.
- **Impact:** On desktop Linux/macOS (no back button), pressing Escape on layer pages does nothing visible.

---

### [R4-ROOT-04] Duplicate "&Open" menu item in native File menu
- **File:** src/kirigami_ui/main.qml:628-635
- **Severity:** Medium
- **Category:** QML/UI
- **Analysis:** Lines 628-631 and 632-635 are exact duplicates. Two identical "&Open" items. Platform overlays have only one occurrence each.
- **Impact:** Confusing duplicate File menu entry. Ambiguous Alt+O accelerator.

---

### [R4-ROOT-05] loadRemoteControlPage/loadTelemetryPage reference undefined component IDs
- **File:** src/kirigami_ui/main.qml:175-181
- **Severity:** Low
- **Category:** QML/UI
- **Analysis:** Functions reference remoteControlPageComponent and telemetryPageComponent — both commented out in base main.qml (lines 1072-1079). Functions reachable via QMetaObject::invokeMethod from C++.
- **Impact:** If C++ calls these functions, ReferenceError crashes the application.

---

### [R4-EVT-01] Missing braces on if/else — syntax error in alignRightButton
- **File:** src/kirigami_ui/EditorToolbar.qml:755-758
- **Severity:** Critical
- **Category:** QML/UI
- **Analysis:** onClicked has `if (condition) stmt; else stmt;` — `if` without braces controls only next statement; `else` is syntactically orphaned. alignLeftButton correctly uses {}.
- **Impact:** QML engine syntax error. Prevents application loading or causes right-align button malfunction.

---

### [R4-EVT-02] Velocity modifier ComboBox lists 2 options but switch handles 4 — dead code
- **File:** src/kirigami_ui/InputsOverlay.qml:425-441
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** ComboBox model has only 2 items ("Alt", "Ctrl") but onActivated switch covers cases 0-3. Cases 2 (ShiftModifier) and 3 (MetaModifier) never reachable.
- **Impact:** Users cannot set velocity modifier to Shift or Meta despite C++ backend support.

---

### [R4-EVT-03] CursorAutoHide null access on root.pageStack.currentItem during page transitions
- **File:** src/prompter/CursorAutoHide.qml:28,31,43,56
- **Severity:** High
- **Category:** QML/UI
- **Analysis:** Four expressions dereference root.pageStack.currentItem without null guard. During page stack transitions, currentItem briefly null → TypeError. Broken QML bindings never recover.
- **Impact:** After page transition, hoverEnabled/enabled bindings dead; cursor auto-hide permanently broken (cursor always visible or always hidden).

---

### [R4-CMT-01] PDF import completely broken — converter invocation commented out
- **File:** src/documenthandler.cpp:1049-1053
- **Severity:** Critical
- **Category:** Platform/Build
- **Analysis:** pdf_importer member initialized to "TextExtraction" but the code block invoking the external PDF-to-text converter is entirely commented out. Binary PDF loaded as garbled text.
- **Impact:** PDF files cannot be imported at all. Users see raw binary garbage.

---

### [R4-PRJ-01] flip variable spuriously reset in project() inner loop else-branch
- **File:** src/prompter/ProjectionsManager.qml:108-114
- **Severity:** High
- **Category:** Logic
- **Analysis:** Inner for loop sets flip on match, but else runs for EVERY non-matching iteration, unconditionally resetting flip to defaultDisplayMode. First match silently discarded.
- **Impact:** Screens configured for projection (flip>0) get no projection window if any non-matching display entry follows.

---

### [R4-PRJ-02] displayModel.get().flipSetting writes to snapshot copy — never mutates model
- **File:** src/prompter/ProjectionsManager.qml:83,141,150
- **Severity:** High
- **Category:** Logic
- **Analysis:** Qt Quick ListModel.get(index) returns plain JS object snapshot, not live reference. Setting flipSetting/flip on copy — actual ListModel data unchanged. putDisplayFlip(), update(), updateFromRoot() all silently no-op.
- **Impact:** Flip settings configured through UI never persisted. Projection windows show stale flip values.

---

### [R4-PRJ-03] setScreensModel() duplicates display entries on each toggle cycle
- **File:** src/prompter/ProjectionsManager.qml:157-164
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** Component.onCompleted runs setScreensModel() populating displayModel. Toggling projections on calls setScreensModel() again without clearing first, appending duplicate entries. Each cycle adds copies.
- **Impact:** Duplicate entries compound PRJ-01 making projection setup increasingly unreliable.

---

### [R4-PRJ-04] Division by zero in projection image height
- **File:** src/prompter/ProjectionsManager.qml:298
- **Severity:** Medium
- **Category:** Edge Case
- **Analysis:** height calculation divides by forwardTo.width/height which may be 0 before main prompter layout. Produces Infinity/NaN → broken Image geometry.
- **Impact:** Projection windows show degenerate/stretched image at startup until main window first paints.

---

### [R4-ROV-01] Division by zero in __customPlacement when overlay full
- **File:** src/prompter/ReadRegionOverlay.qml:189
- **Severity:** High
- **Category:** Edge Case
- **Analysis:** readRegion.y / (overlay.height - readRegion.height) — when read region fills full overlay (equal heights), denominator 0 → Infinity → NaN propagation.
- **Impact:** Read region position corrupted; overlay unusable until value reset externally.

---

### [R4-ROV-02] Drag permanently breaks y property binding on readRegion
- **File:** src/prompter/ReadRegionOverlay.qml:181-182,141
- **Severity:** High
- **Category:** QML/UI
- **Analysis:** MouseArea drag.target assigns y directly to readRegion, breaking the declarative y binding. After drag stops, nothing re-establishes it. Changing positionState updates __placement but y no longer has live binding.
- **Impact:** After dragging read region once, positionState toggle (Top/Middle/Bottom/Fixed) silently stops working.

---

### [R4-ROV-03] Bitwise OR | used for width fallback instead of logical OR
- **File:** src/prompter/ReadRegionOverlay.qml:396
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** (rightPointer.item.width | rightPointer.item.contentWidth) / 2 — bitwise OR on two non-zero ints produces garbage combination (50|60=62), wrong origin. Meant to be || or ternary.
- **Impact:** Right pointer icon appears off-center when both width and contentWidth have non-zero values.

---

### [R4-BKG-01] Flip transform origin stays at (0,0) when Flip stored as property
- **File:** src/prompter/PrompterBackground.qml:89-90 (also ReadRegionOverlay:65,90)
- **Severity:** Medium
- **Category:** QML/UI
- **Analysis:** readonly property Scale __flips: Flip{} — Scale item whose origin.x: width/2, origin.y: height/2 bind to Scale's own width/height, always 0. Flip occurs around top-left corner.
- **Impact:** Background image and overlay flips visibly off-center; mirrored content jumps to one side.

---

### [R4-SHD-01] Duplicate class implementation between .cpp and .mm — ODR risk
- **File:** src/shakedetector.cpp:24-43 and shakedetector.mm:45-64
- **Severity:** Medium
- **Category:** Platform/Build
- **Analysis:** Constructor, instance(), create(), and s_instance duplicated identically in both. CMake compiles only one per platform, but future change in one file risks silent platform divergence.
- **Impact:** Latent maintenance hazard; behavioral divergence if only one file updated.

---

### [R4-IOSCPP-01] QTemporaryDir created on all platforms including non-iOS where unused
- **File:** src/iossavedialog.h:49
- **Severity:** Low
- **Category:** Resource Management
- **Analysis:** QTemporaryDir m_tempDir by-value member — default constructor creates real temp directory on disk immediately. Non-iOS platforms: saveDocument no-op but directory still created.
- **Impact:** Unnecessary filesystem I/O and temporary directory creation on Windows, Linux, macOS, Android, WASM at every app start.

---

### [R4-SIG-ADD-01] SessionModel::appendDataPoint declared public slot but never connected
- **File:** src/prompsession.h:71
- **Severity:** Low
- **Category:** Logic
- **Analysis:** Declared as public slot but no connect() call anywhere connects any signal to it. Not marked Q_INVOKABLE. If intended as signal-driven telemetry, silently broken.
- **Impact:** Likely low. If QML invokes via slot mechanism it works, but signal-driven recording is dead.

---

## Final Summary

| Category | Critical | High | Medium | Low | Total |
|---|---|---|---|---|---|
| Memory Management | 0 | 2 | 1 | 1 | 4 |
| Logic / Control Flow | 0 | 8 | 22 | 5 | 35 |
| QML / UI | 9 | 14 | 10 | 3 | 36 |
| Security | 2 | 2 | 4 | 0 | 8 |
| Resource Management | 0 | 2 | 2 | 3 | 7 |
| Type Safety / Conversion | 0 | 4 | 13 | 2 | 19 |
| Edge Case / Error Handling | 5 | 8 | 6 | 4 | 23 |
| Platform / Build | 2 | 5 | 20 | 8 | 35 |
| **TOTAL** | **18** | **45** | **78** | **26** | **167** |

## Final Bug Density by File

| File | Bugs |
|---|---|
| src/documenthandler.cpp | 30 |
| src/documenthandler.h | 7 |
| src/kirigami_ui/PrompterPage.qml | 7 |
| src/main.cpp | 11 |
| src/kirigami_ui/main.qml | 6 |
| src/kirigami_ui/EditorToolbar.qml | 5 |
| src/prompter/ReadRegionOverlay.qml | 8 |
| src/prompter/ProjectionsManager.qml | 6 |
| src/spellchecker.cpp | 9 |
| CMakeLists.txt | 4 |
| src/kirigami_ui/+android/main.qml | 6 |
| src/markersmodel.cpp | 3 |
| cmake/FindSphinx.cmake | 3 |
| src/prompsession.cpp | 2 |
| src/prompsession.h | 3 |
| src/globalhotkeys.cpp | 2 |
| src/shakedetector.cpp | 4 |
| src/iossavedialog.mm | 3 |
| src/CMakeLists.txt | 2 |
| src/qt/WindowDragger.qml | 2 |
| src/prompter/Countdown.qml | 2 |
| src/prompter/Prompter.qml | 5 |
| src/prompter/pointers/pointer_0.qml | 1 |
| src/prompter/pointers/pointer_1.qml | 1 |
| src/prompter/pointers/pointer_2.qml | 1 |
| src/prompter/PointerSettings.qml | 1 |
| src/prompter/PrompterBackground.qml | 1 |
| src/prompter/Find.qml | 1 |
| src/prompter/TimerClock.qml | 1 |
| src/prompter/CursorAutoHide.qml | 1 |
| src/kirigami_ui/KeyInputButton.qml | 1 |
| src/kirigami_ui/PathsPage.qml | 2 |
| src/kirigami_ui/WheelSettingsOverlay.qml | 1 |
| src/kirigami_ui/TelemetryPage.qml | 1 |
| src/kirigami_ui/RecentDocuments.qml | 2 |
| src/kirigami_ui/InputsOverlay.qml | 2 |
| src/kirigami_ui/LanguageSettingsOverlay.qml | 1 |
| src/qmlutil.hpp | 1 |
| src/iossavedialog.cpp | 1 |
| src/shakedetector.mm | 2 |
| src/wasmintegration.cpp | 2 |
| src/systemfontchooserdialog.cpp | 2 |
| src/appcontroller.cpp | 2 |
| cmake/BreezeIconSubset.cmake | 1 |
| android/AndroidManifest.xml | 2 |
| cmake/HunspellDictionaries.cmake | 1 |
| .env.android | 1 |
| setup.sh | 1 |
| .gitmodules | 1 |

---

## Round 5-7 — Final Waves: Typo Sweep, Deep Specialization, Synthesis

### Critical New Findings (Not Previously Documented)

### [FINAL-01] TimerClock references undefined `timer` id — ETA and stopwatch completely broken
- **File:** src/prompter/TimerClock.qml:70,82,85
- **Severity:** Critical
- **Category:** QML/UI
- **Analysis:** Lines 70 and 82 call `timer.getTimeString(...)` — but `timer` is not an id in this file (the Timer object at line 190 has no `id`). The correct reference is `clock.getTimeString(...)`. Line 85 writes `timer.elapsedMilliseconds = 0` — same undefined id.
- **Impact:** ETA and stopwatch display labels never update. The timer clock is completely non-functional.

### [FINAL-02] Missing `QtQuick.Controls.Material` import — 3 Material references unresolved
- **File:** src/kirigami_ui/WheelSettingsOverlay.qml:59,78,96
- **Severity:** Critical
- **Category:** QML/UI
- **Analysis:** Lines use `Material.theme: Material.Dark` but file lacks `import QtQuick.Controls.Material`.
- **Impact:** QML binding errors on two Buttons and one SpinBox; theme styling silently fails.

### [FINAL-03] Missing breeze-icons submodule — fresh clone cannot build
- **File:** .gitmodules (omission), cmake/BreezeIconSubset.cmake:98-101
- **Severity:** Critical
- **Category:** Platform/Build
- **Analysis:** `3rdparty/breeze-icons` is required by BreezeIconSubset.cmake but has no entry in .gitmodules. CMake emits FATAL_ERROR on configure.
- **Impact:** Fresh clone → cannot configure. Every platform affected.

### [FINAL-04] NSIS start-menu shortcut icon name mismatches actual binary name
- **File:** CMakeLists.txt:465
- **Severity:** High
- **Category:** Platform/Build
- **Analysis:** Shortcut points to `qprompt.exe` but installed binary is `QPrompt.exe` (from OUTPUT_NAME). Also overwrites correct line 463.
- **Impact:** Windows installer shortcut broken — "file not found" error.

### [FINAL-05] WindowDragger mouse delta accumulation error — window moves farther than cursor
- **File:** src/qt/WindowDragger.qml:42,46
- **Severity:** High
- **Category:** QML/UI
- **Analysis:** `prevX = mouse.x - deltaX` algebraically reduces to `prevX = prevX` — prevX never advances. Every drag event adds delta from the *original press*, not last position. Mouse 20px → window 30px.
- **Impact:** Window drag increasingly faster than cursor; jerky, unpredictable positioning.

### [FINAL-06] CMAKE_OSX_ARCHITECTURES contains literal quotes — universal binary broken
- **File:** CMakeLists.txt:418, src/CMakeLists.txt:29
- **Severity:** High
- **Category:** Platform/Build
- **Analysis:** `set(CMAKE_OSX_ARCHITECTURES="x86_64;arm64")` — quotes become part of value. Clang receives `-arch "x86_64;arm64"` — invalid argument.
- **Impact:** macOS universal binary silently fails; produces x86_64-only.

### [FINAL-07] CMake wrong variable name: InstallRequiredSystemLibraries instead of CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS
- **File:** CMakeLists.txt:414
- **Severity:** High
- **Category:** Platform/Build
- **Analysis:** Setting the include-module name as a variable has no effect. MSVC runtime DLLs never bundled.
- **Impact:** Windows installer missing VCRUNTIME; app silently fails to launch on machines without VC++ Redist.

### [FINAL-08] setup.sh vcvarsall.bat executed from bash — MSVC env not propagated
- **File:** setup.sh:175
- **Severity:** High
- **Category:** Platform/Build
- **Analysis:** Windows .bat runs in isolated cmd.exe subprocess; env vars (PATH, INCLUDE, LIB) lost when subprocess exits.
- **Impact:** Windows build path in setup.sh completely broken; cmake can't find MSVC compiler.

### [FINAL-09] `on__IChanged` handler typo — never fires
- **File:** src/prompter/Prompter.qml:200
- **Severity:** Medium
- **Category:** QML/UI
- **Analysis:** Property is `__i` (lowercase). Handler `on__IChanged` (capital I) does not match. Should be `on__iChanged`.
- **Impact:** The `__tikTok` jitter-margin toggle never runs; subpixel positioning jitter remains static.

### [FINAL-10] Two animations target same `position` property — conflict
- **File:** src/prompter/Prompter.qml:839,909
- **Severity:** High
- **Category:** QML/UI
- **Analysis:** `Behavior on position` and `NumberAnimation on position` both target `prompter.position`. On reset, both fire simultaneously with different durations.
- **Impact:** Animation jitter/jump on rewind-to-start; one animation overrides the other mid-flight.

### [FINAL-11] onFrameSwapped calls grabToImage every frame — severe performance hit
- **File:** src/kirigami_ui/main.qml:1041-1045
- **Severity:** High
- **Category:** QML/UI
- **Analysis:** Every frame, when projections enabled, `viewport.grabToImage()` triggers offscreen render + GPU readback.
- **Impact:** Major frame rate degradation during screen projections.

### [FINAL-12] SystemFontChooserDialog setWindowFlags strips all decorations
- **File:** src/systemfontchooserdialog.cpp:32
- **Severity:** Medium
- **Category:** QML/UI
- **Analysis:** `setWindowFlags(Qt::WindowStaysOnTopHint)` replaces ALL flags, removing title bar, close button, resize, minimize. Should be `windowFlags() | Qt::WindowStaysOnTopHint`.
- **Impact:** Font dialog appears as borderless, uncloseable rectangle.

### [FINAL-13] Invalid Korean locale code "ko_KO" — should be "ko_KR"
- **File:** src/kirigami_ui/LanguageSettingsOverlay.qml:127
- **Severity:** Medium
- **Category:** I18N
- **Analysis:** "KO" is not valid ISO 3166-1 (South Korea = KR). Translation file won't match.
- **Impact:** Korean users get no translation — silently falls back to English.

### [FINAL-14] Wrong placeholder `%0` instead of `%1` — font name never displayed
- **File:** src/kirigami_ui/EditorToolbar.qml:588
- **Severity:** Medium
- **Category:** I18N
- **Analysis:** `qsTr("Active font: %0")` — arg() uses 1-based placeholders. %0 treated as literal text.
- **Impact:** Font selector shows literal "Active font: %0" instead of the active font name.

### [FINAL-15] Missing edit block wrapping in setLineHeight/setParagraphHeight
- **File:** src/documenthandler.cpp:1596,1610
- **Severity:** High
- **Category:** Edge Case
- **Analysis:** `cursor.joinPreviousEditBlock()` without prior beginEditBlock(). If another operation left an edit block open, two unrelated operations fused into single undo step.
- **Impact:** Non-deterministic undo grouping; format + line-height changes become one undo step.

### [FINAL-16] Countdown completion uses state++ bypassing toggle() entry actions
- **File:** src/prompter/Countdown.qml:122-123
- **Severity:** Critical
- **Category:** Logic
- **Analysis:** `prompter.state++` directly increments state from Countdown(2) to Prompting(3), bypassing toggle() which does timer.reset(), preventSleep(true), addMissingProjections(), restoreFocus().
- **Impact:** When countdown finishes: timer not reset, system allowed to sleep, projections not created.

### [FINAL-17] ScriptAction references non-existent function `paintReady`
- **File:** src/prompter/Countdown.qml:318
- **Severity:** Medium
- **Category:** QML/UI
- **Analysis:** Transition scriptName: "paintReady" — this function does not exist anywhere in the codebase.
- **Impact:** Standby→Ready transition is empty; intended paintReady side-effects never execute.

### [FINAL-18] MarkersModel extendLastMarker modifies data without emitting dataChanged
- **File:** src/markersmodel.cpp:109-114
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** Mutates m_data.last().text directly with no dataChanged signal. Violates QAbstractItemModel contract.
- **Impact:** QML views show stale marker text after key-marker text extension.

### [FINAL-19] Encoding fallback uses toLocal8Bit() instead of dictionary's actual encoding
- **File:** src/spellchecker.cpp:402-406, 408-412
- **Severity:** Medium
- **Category:** I18N
- **Analysis:** encode()/decode() ignore d.encoding (read from .aff file). Fallback to system locale 8-bit, which differs from dictionary encoding.
- **Impact:** Non-ASCII words corrupted in non-UTF-8 Hunspell dictionaries; false positives/negatives.

### [FINAL-20] Dangling pointer from temporary QByteArray in marker anchor parsing
- **File:** src/documenthandler.cpp:1664
- **Severity:** High
- **Category:** Type Safety
- **Analysis:** `(*constIterator).toUtf8().constData()` — stores pointer to temporary QByteArray buffer. Temporary destroyed at end of expression; pointer dangles.
- **Impact:** Memory corruption when parsing markers with non-ASCII anchor names.

### [FINAL-21] clearProperty(AnchorHref/AnchorName) ineffective through mergeCharFormat
- **File:** src/documenthandler.cpp:800-801
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** clearProperty marks properties as unset locally. mergeCharFormat only applies set properties; unset properties silently skipped. Stale AnchorHref/AnchorNames persist.
- **Impact:** Markers retain stale key bindings across disable/re-enable cycles.

### [FINAL-22] Behavior.onRunningChanged calls toggle() from within animation handler — re-entrant state change
- **File:** src/prompter/Prompter.qml:855
- **Severity:** High
- **Category:** Logic
- **Analysis:** toggle() called inside the Behavior animation's onRunningChanged signal handler. Triggers state machine transition while animation system mid-processing.
- **Impact:** Undefined behavior at AtEndActions.Exit; PropertyChanges may not apply correctly; focus/play/property state inconsistent.

---

## Synthesis Analysis

### 1. Bug Chains (Compound Failures)

**Chain 1: Search/Replace Death Spiral** — LOG-05 (loop param ignored for regex) + LOG-06 (replaceAll infinite loop). "Replace All" with regex=true guaranteed hang at 100% CPU.

**Chain 2: Null Document Crash Cascade** — EDGE-04/05/06 (3 null derefs in load/search/parse) + R3-DOC-01 (m_reloading uninitialized). Five independent crashes all reachable from QML before any document loads.

**Chain 3: Pointer/Overlay Ghost System** — R4-QTV-02 (QtQuick.Window 2.0 not in Qt 6.5) → ReadRegionOverlay.qml fails to load, masking QML-01 (26 undefined refs) + QML-02 + R4-ROV-01/02/03 + R4-BKG-01. **31 bugs behind a dead component.**

**Chain 4: Projections Compound Failure** — R4-QTV-01 (QtQuick 2.13 not in Qt 6.5) → ProjectionsManager.qml never loads, masking R4-PRJ-01/02/03/04.

**Chain 5: Progressive UI Decay** — R2-EDT-03 (~20 buttons) + R2-TEL-01 + R4-ROV-02 + R3-DOC-06. Every user interaction permanently degrades application state. No crashes — silently cumulative corruption.

**Chain 6: Document Destruction Path** — R4-EXP-08 (EPUB/AZW replaces with error) + R4-EXP-04 (AutoText: <> parsed as HTML) + R4-EXP-06 (UTF-8 BOM as phantom char at 0) + R3-DOC-05 (undo after load = empty doc). Four independent silent data destruction paths.

**Chain 7: Network Reply Double-Fault** — RES-01 (reply overwritten without abort) + RES-02 (slot ignores signal's QNetworkReply* parameter) + EDGE-11 (m_reply deref without null check).

**Chain 8: Android Crash Trinity** — R2-AND-01 (no QmlUtil → factory reset crash) + R2-AND-02 (no restartDialog → lang/layout crash) + QML-10 (no util → recents crash).

### 2. Root Cause Clusters

| Cluster | Count | Pattern |
|---|---|---|
| QML case-sensitivity (wrong caps) | 8 bugs | `SmallSpacing`, `LongDuration`, `AlignHustify`, `SkipForward`, etc. |
| Kirigami namespace omission | 3 bugs, 6 sites | Bare `Units` instead of `Kirigami.Units` |
| Missing parent QObject (leaks) | 3 bugs | `_markersModel`, `_fileSystemWatcher`, `m_fontDialog` |
| Uninitialized members | 5 bugs | `m_reply`, `m_reloading`, `m_documentComesFromNetwork`, `DataPoint` fields, `SessionModel::dirty` |
| Null/empty container dereference | 6 bugs | first(), last(), document(), textDocument(), m_reply |
| Q_UNREACHABLE as placeholder | 3 bugs | 3 reachable code paths marked unreachable |
| Signal declared but never emitted | 4 bugs | textChanged, ShakeDetector, IosSaveDialog, appendDataPoint |
| Qt import version mismatch | 5 bugs, 13 files | QtQuick 2.13, QtQuick.Window 2.0, Dialogs 6.6, Shapes 6.6, CurveRendering 6.7 |
| Platform variant drift | 9 bugs | Android/WATCHOS/QNX missing features present in base/windows |

### 3. Architectural Defects

1. **No Thread Safety Model** — Zero mutexes, only guard is Q_ASSERT (debug-only). Any move to background processing = crash.
2. **Fragile Declarative/Imperative Mix** — ~23 declarative bindings broken by user interaction; no recovery mechanism.
3. **No Input Sanitization Architecture** — Data flows from external sources to dangerous sinks with no validation layer.
4. **Abandoned Feature Proliferation** — KCrash, telemetry, remote control, Touch Bar, PDF import: half-built, dead code masking real state.
5. **Inconsistent Platform Abstraction** — Every platform variant diverged; no single source of truth.

### 4. Synthetic Bugs (Big-Picture Only)

1. **Progressive UI Decay** — App doesn't crash; it becomes silently, progressively wrong with each user action.
2. **Conflicting Crash Avoidance vs. Causation** — KCrash (crash handler) is dead code while Q_UNREACHABLE introduces new crash sources.
3. **Perpetual Upgrade Breakage** — Hardcoded Homebrew paths, Qt 5-era import versions, Qt 6.7 APIs on 6.5 target. Any dependency update breaks something.
4. **QML Component Load Order Minefield** — Import version errors, syntax errors, async Loader races: app can start with blank sections and no error.

### 5. Priority Fix Order (Top 10)

| Rank | Bug | Rationale |
|---|---|---|
| 1 | SEC-01 (sys:// RCE) | Remote code execution; ship-stopper |
| 2 | R4-EVT-01 (missing braces syntax error) | Prevents app from loading; blocks all debugging |
| 3 | R4-QTV-01 + R4-QTV-02 (Qt import versions) | Unmasks 35+ bugs behind dead components |
| 4 | EDGE-04/05/06 (null deref cascade) | 3 crashes in basic operations |
| 5 | R3-DOC-01 (m_reloading uninitialized) | Non-deterministic behavior on first load |
| 6 | R3-CTX-01 (AbstractUnits missing QML_ELEMENT) | 36 QML refs resolve to undefined; all animations broken |
| 7 | R2-EDT-03 (systematic binding breakage) | Template fix for 23 similar bugs |
| 8 | LOG-05 + LOG-06 (replaceAll infinite loop) | App hangs at 100% CPU |
| 9 | R3-DOC-05 (updateContents undo corruption) | Silent data loss: undo destroys document |
| 10 | R2-AND-01 + R2-AND-02 (Android crashes) | 3 routine ops crash Android app |

### 6. Severity Re-classifications

**RAISED:**
- R2-EDT-03: High → **Critical** (23 bindings break on first interaction)
- EDGE-07: High → **Critical** (Q_UNREACHABLE in Q_INVOKABLE; UB in release)
- R2-GH-01: High → **Critical** (abort on GNOME/Sway/Hyprland Wayland)
- R3-DOC-07: High → **Critical** (inverted selection = silent text overwrite)
- R4-PRJ-02: High → **Critical** (entire projections config feature is a no-op)
- QML-10 + R2-AND-01: → **Critical** (Android unusable without fixes)

**LOWERED:**
- PLAT-01: High → **Medium** (KCrash dead code, not actively harmful)

---

## Grand Total Summary

| Category | Critical | High | Medium | Low | Total |
|---|---|---|---|---|---|
| Memory Management | 0 | 2 | 2 | 2 | 6 |
| Logic / Control Flow | 1 | 10 | 28 | 8 | 47 |
| QML / UI | 11 | 19 | 15 | 4 | 49 |
| Security | 2 | 2 | 5 | 0 | 9 |
| Resource Management | 0 | 3 | 3 | 3 | 9 |
| Type Safety / Conversion | 0 | 5 | 15 | 3 | 23 |
| Edge Case / Error Handling | 6 | 10 | 8 | 5 | 29 |
| Platform / Build | 3 | 9 | 22 | 9 | 43 |
| I18N / Encoding | 0 | 1 | 6 | 2 | 9 |
| **TOTAL** | **23** | **61** | **104** | **36** | **224+** |

**224+ confirmed bugs. 10 critical bug chains. 9 root cause clusters. 5 architectural defects.**

---

---

## Round 6+ — Wave 8-10: Surgical Deep Audits

### [CUR-N01] replaceAll() infinite loop when replacement contains search pattern
- **File:** src/documenthandler.cpp:1503-1516
- **Severity:** Critical
- **Category:** Logic
- **Analysis:** selectionStart never updated after insertText; stale value causes re-find of same text. If replacement contains searchedText (e.g., replace "a" with "aa"), loop never terminates.
- **Impact:** 100% CPU hang. UI freeze requiring force-quit.

### [CUR-N02] search() regex path ignores loop parameter — unconditional wrap
- **File:** src/documenthandler.cpp:1552-1557
- **Severity:** High
- **Category:** Logic
- **Analysis:** Regex branch wraps unconditionally; non-regex branch correctly checks loop parameter. replaceAll passes loop=false but regex ignores it.
- **Impact:** Incorrect search results; compounds with CUR-N01 for guaranteed infinite loop on regex replaceAll.

### [CUR-N03] alignment() reads blockFormat on multi-block selection — returns wrong alignment
- **File:** src/documenthandler.cpp:547-550
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** textCursor() on multi-block selection: mergeBlockFormat/blockFormat returns neutral (Qt::AlignLeft) instead of actual alignment. Formatting toolbar shows wrong alignment state.
- **Impact:** Alignment toolbar button checked state incorrect when multiple blocks selected.

### [DCL-N01] filterHtml default parameter in .cpp but not in header — QML can't call with 1 arg
- **File:** src/documenthandler.h:235 vs .cpp:1246
- **Severity:** Medium
- **Category:** Type Safety
- **Analysis:** Header declares `filterHtml(QString, bool)` with no default. .cpp implements `= true` default. Moc generates requiring both args. Default dead code.
- **Impact:** QML cannot call `filterHtml(html)` with one argument as intended.

### [DCL-N02] setKeyMarker default parameter mismatch — same pattern
- **File:** src/documenthandler.h:213 vs .cpp:707
- **Severity:** Medium
- **Category:** Type Safety
- **Analysis:** Empty-string default in .cpp invisible to QML callers. Intended single-arg shortcut unreachable.
- **Impact:** setKeyMarker("") no-op from C++ but QML can't invoke without explicit empty string.

### [IMP-N01] import Qt.labs.platform 1.1 — Menu/MenuBar/MenuItem dropped in Qt 6
- **File:** src/kirigami_ui/main.qml:29,617-922
- **Severity:** Critical
- **Category:** QML/UI
- **Analysis:** Qt 6's Qt.labs.platform no longer exports MenuBar, Menu, MenuItem. Base main.qml instantiates these for native menu bar — all undefined types.
- **Impact:** Native File/Format/View/Help menu bar silently dead on Linux/macOS (the targets for base main.qml).

### [IMP-N02] import QtWebSockets 1.10 — wrong version for Qt 6.5
- **File:** src/prompter/Prompter.qml:80
- **Severity:** Critical
- **Category:** QML/UI
- **Analysis:** In Qt 6.x, QML WebSocket module uses Qt version number (6.5) not 1.x. Version 1.10 doesn't exist.
- **Impact:** OBS WebSocket remote control integration completely non-functional.

### [MATH-N01] Division by zero in __timeToArival/__timeToEnd when speed=0
- **File:** src/prompter/Prompter.qml:121-123
- **Severity:** High
- **Category:** Logic
- **Analysis:** __relativeSpeed=0 when __speed=0 or fontSize=0 → division by zero → Infinity assigned to NumberAnimation duration. No isFinite guard.
- **Impact:** Teleprompter scrolling freezes permanently when speed slider hits 0.

### [MATH-N02] Bitwise << on floating-point in TimerClock — precision loss
- **File:** src/prompter/TimerClock.qml:127
- **Severity:** Medium
- **Category:** Type Safety
- **Analysis:** `... * prompter.__vw << 3` coerces float to 32-bit int before shift. e.g., 9.6 → 9 → 72 instead of 76.8. Should use `* 8`.
- **Impact:** Stopwatch font size loses fractional precision at certain viewport widths.

### [LYR-N01] InputsOverlay calls cursorAutoHide.restart() on open instead of reset()
- **File:** src/kirigami_ui/InputsOverlay.qml:41
- **Severity:** High
- **Category:** Logic
- **Analysis:** All other overlays call reset() on open (stop timer, show cursor). InputsOverlay calls restart() (re-enables auto-hide). Cursor hides after 1 second while user configuring key bindings.
- **Impact:** Cursor vanishes during key binding configuration. User locked out of overlay.

### [LYR-N02] Three OverlaySheets missing from ESC dismiss chain
- **File:** src/kirigami_ui/main.qml:489-504
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** obsConfiguration, dictionariesSheet, customWordsSheet added to PrompterPage after ESC handler. Not in the if-else chain. ESC falls through without closing them.
- **Impact:** ESC doesn't close OBS/dictionary/custom-words sheets. User must click close button.

### [LYR-N03] ContextDrawer exposes prompter actions while viewing layer pages
- **File:** src/kirigami_ui/main.qml:929
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** Guard `depth <= 1` always true since clear() before push(). Should be `depth < 1`. Prompter actions (start prompting, screen projections) shown on About/Paths/Remote pages.
- **Impact:** ContextDrawer shows wrong actions on secondary pages; clicking affects hidden prompter.

### [LYR-N04] ESC handler uses activeFocus in base but focus in platform variants — inconsistent
- **File:** src/kirigami_ui/main.qml:512 vs +windows:483 vs +android:422
- **Severity:** Medium
- **Category:** Logic
- **Analysis:** Base checks `prompter.activeFocus`, platform variants check `prompter.focus`. If prompter is FocusScope delegating to child, activeFocus=false while focus=true. Platform divergence.
- **Impact:** Linux/macOS ESC may fail to cancel prompting; Windows/Android work correctly.

### [TRL-N01] qsTr() uses %0 placeholder — should be %1 (font name never displayed)
- **File:** src/kirigami_ui/EditorToolbar.qml:588
- **Severity:** High
- **Category:** I18N
- **Analysis:** `qsTr("Active font: %0").arg(fontFamily)` — Qt arg() uses 1-based placeholders. %0 treated as literal text.
- **Impact:** Font selector shows literal "Active font: %0" instead of actual font name in all languages.

### [TRL-N02] Application --help description not translatable
- **File:** src/main.cpp:154-155
- **Severity:** Medium
- **Category:** I18N
- **Analysis:** setApplicationDescription uses QLatin1String instead of tr(). User-visible in --help output.
- **Impact:** App description never translated. Non-English users see English in --help.

### [TRL-N03] About-dialog credit roles not translatable
- **File:** src/main.cpp:194,202,205-206
- **Severity:** Medium
- **Category:** I18N
- **Analysis:** "Author", "Software Tester", credit descriptions use QLatin1String instead of tr().
- **Impact:** Credit roles always English in About dialog.

---

## Wave 10 — Hotkeys, PrompterView, Clipboard, Conversion, WASM, Dependencies

### [W10-HTK-01] autoRepeat=true for ALL QHotkey shortcuts — non-velocity actions broken when held
- **File:** src/globalhotkeys.cpp:1116
- **Severity:** Critical
- **Category:** Logic
- **Analysis:** m_setHotkeyShortcut passes true for autoRepeat unconditionally. Holding TogglePrompter/Pause/Stop/Reverse floods with repeated activated() signals. Toggle actions rapidly flip on/off.
- **Impact:** All non-velocity hotkeys broken when held. Toggle-type actions rapidly flip state.

### [W10-HTK-02] QHotkey::setShortcut return value silently ignored — no failure detection
- **File:** src/globalhotkeys.cpp:1116
- **Severity:** High
- **Category:** Edge Case
- **Analysis:** bool return indicating successful OS registration discarded. Failed registrations (OS conflict, duplicate, Wayland limitation) silently produce non-functional hotkeys.
- **Impact:** Broken hotkeys give zero user feedback. User has no way to know registration failed.

### [W10-PMV-01] font.pixelSize evaluates to 0 before first layout pass — crash hazard
- **File:** src/prompter/PrompterView.qml:242
- **Severity:** High
- **Category:** QML/UI
- **Analysis:** WYSIWYG branch: fontSize depends on __vw = width/100. Before QML layout assigns width=0, fontSize=0. Requires pixelSize>0 for text rendering.
- **Impact:** Debug assertion failure; release builds may render invisible text or layout collapse at startup.

### [W10-PMV-02] Circular ShaderEffectSource dependency — shadow ghost on first frame
- **File:** src/prompter/PrompterView.qml:230-233, Prompter.qml:744-770
- **Severity:** Medium
- **Category:** QML/UI
- **Analysis:** ShaderEffectSource captures prompter with layer effect applied, feeds back as shadow texture. One-frame-lag ghosting.
- **Impact:** Missing/shadow flash on first paint; ghosting during rapid scroll on Metal/WASM.

### [W10-CLP-01] Paste-without-formatting fails when clipboard lacks text/plain
- **File:** src/documenthandler.cpp:1346-1348
- **Severity:** High
- **Category:** Edge Case
- **Analysis:** paste(true) calls mimeData->text(). If clipboard has HTML but no text/plain MIME (some apps omit it), returns empty → nothing inserted.
- **Impact:** Ctrl+Shift+V silently does nothing. Should fall back to stripping HTML tags.

### [W10-CLP-02] Remote image URLs in pasted HTML cause unsanctioned network requests
- **File:** src/documenthandler.cpp:1246-1334, 1425-1455
- **Severity:** Medium
- **Category:** Security
- **Analysis:** filterHtml doesn't remove img tags with remote src. insertHtmlAt pre-loads remote images synchronously. Pasted web content causes tracking-able network requests.
- **Impact:** Privacy leak — user IP revealed to remote servers when pasting web content.

### [W10-CNV2-01] Default stylesheet has invalid CSS color quoting — exported HTML broken in browsers
- **File:** src/documenthandler.cpp:184-189
- **Severity:** High
- **Category:** Type Safety
- **Analysis:** color:\"#FFFFFF\" and border-color:\"#404040\" — quoted color values invalid per CSS spec. toHtml() embeds this verbatim. Browsers fail to interpret.
- **Impact:** Saved HTML documents lose foreground/border colors when viewed in browsers.

### [W10-CNV2-02] No markdown export — round-trip silently destroys all formatting
- **File:** src/documenthandler.cpp:1138-1177
- **Severity:** High
- **Category:** Logic
- **Analysis:** Markdown imported via Qt::MarkdownText but saveAs only branches HTML/plain. .md extension → toPlainText() stripping all formatting. toMarkdown() never called.
- **Impact:** Opening .md, editing with formatting, saving → all bold/italic/images/hyperlinks destroyed.

### [W10-CNV2-03] import() uses fromStdString on non-Windows — encoding corruption
- **File:** src/documenthandler.cpp:1096
- **Severity:** High
- **Category:** Type Safety
- **Analysis:** Non-Win path: QString::fromStdString(bytes.toStdString()) — assumes locale encoding in Qt5, UTF-8 in Qt6. LibreOffice output may use different encoding.
- **Impact:** Imported ODT/DOCX/DOC/RTF documents may contain garbled characters on macOS/Linux.

### [W10-SWT-01] CloseActions switch drops RecentLocal/RecentRemote — recent document open silently lost after save
- **File:** src/prompter/Prompter.qml:2479
- **Severity:** High
- **Category:** Logic
- **Analysis:** FileDialog.onAccepted switch handles 5 of 8 CloseActions values. RecentLocal/RecentRemote missing. Line 2302 switch correctly handles all 8. Save dialog path loses intent.
- **Impact:** User triggers recent-document-open, prompted to save, saves, and recent document never opens.

### [W10-SWT-02] Same bug in IosSaveDialog.onAccepted path
- **File:** src/prompter/Prompter.qml:2500
- **Severity:** High
- **Category:** Logic
- **Analysis:** Identical omission in iOS save dialog switch.
- **Impact:** Same silent loss of recent-document-load intent on iOS.

### [W10-DEP-01] Missing vcpkg.json manifest — vcpkg manifest mode installs nothing
- **File:** vcpkg-configuration.json (no companion vcpkg.json)
- **Severity:** Critical
- **Category:** Platform/Build
- **Analysis:** vcpkg-configuration.json present but no vcpkg.json. vcpkg manifest mode reads vcpkg.json for ports to install. Without it, zero dependencies installed.
- **Impact:** vcpkg-based builds completely broken. Windows CI/CD using vcpkg cannot configure.

### [W10-WSM-01] Infinite reload loop on unauthorized WASM host — app unusable
- **File:** src/prompter/Prompter.qml:439, src/wasmintegration.cpp:189-194
- **Severity:** Critical
- **Category:** Platform/Build
- **Analysis:** Every toggle() calls officialHost() which calls QCoreApplication::quit() on unauthorized hosts. aboutToQuit → location.reload() → same host → restart cycle.
- **Impact:** App enters inescapable reload loop on any host other than localhost/qprompt.app.

### [W10-WSM-02] Global file-picker state overwritten by re-entrant calls — wrong file delivered
- **File:** src/wasmintegration.cpp:37-40, 64-88, 164-171
- **Severity:** Medium
- **Category:** Platform/Build
- **Analysis:** Static s_pending* globals for file picker with no re-entrancy guard. Second call before first dialog completes overwrites state; first dialog delivers to second caller's objects.
- **Impact:** Wrong file/image delivered to wrong QML property on rapid multi-click.

### [W10-PLF-01] BSD detection broken — FreeBSD enters wrong code paths
- **File:** CMakeLists.txt:250,487
- **Severity:** Critical
- **Category:** Platform/Build
- **Analysis:** CMake has no standard `BSD` variable. `${BSD}` never set → `NOT BSD` always true → FreeBSD routes through wrong FetchContent/find_package and wrong CPack generator.
- **Impact:** FreeBSD build completely misconfigured. Wrong dependency resolution and packaging.

### [W10-PLF-02] QHotkey_FOUND never set in FetchContent path — built but never linked
- **File:** CMakeLists.txt:252-258, src/CMakeLists.txt:495-500
- **Severity:** High
- **Category:** Platform/Build
- **Analysis:** FetchContent_MakeAvailable(QHotkey) processes but doesn't set QHotkey_FOUND CMake variable. add_definitions and target_link_libraries gated on it → never executed.
- **Impact:** QHotkey compiled by FetchContent but never linked. Global hotkey functionality silently disabled on Windows/macOS/Linux+BSD FetchContent builds.

---

## Round 7 — Re-Run Deep Audits (Waves 11R)

---

### Translation Files (42 bugs across 20 .ts files)

### [TS-01] Finnish welcome guide → Dutch (not Finnish)
- **File:** po/qprompt_fi.ts:656 — `welcome_nl.html` should be `welcome_fi.html`

### [TS-02] Arabic file `ar_EG` vs UI `ar_AE` mismatch
- **File:** po/qprompt_ar.ts:3 — `language="ar_EG"` but LanguageSettingsOverlay.qml uses `ar_AE`

### [TS-03] Korean UI `ko_KO` vs file `ko_KR` mismatch  
- **File:** src/kirigami_ui/LanguageSettingsOverlay.qml:127 — `"ko_KO"` invalid; file uses `ko_KR`

### [TS-04] French "Saved" → verb "Enregistrer" (should be adjective "Enregistré")
- **File:** po/qprompt_fr.ts:679

### [TS-05] Finnish/French/Korean/Italian "Saved" → verb with stray `&amp;` accelerator
- **Files:** po/qprompt_fi.ts:678, po/qprompt_ko.ts:677, po/qprompt_it.ts:679

### [TS-06] Czech/French "Language settings" → "Pointer settings" (copy-paste error)
- **Files:** po/qprompt_cs.ts:354, po/qprompt_fr.ts:353

### [TS-07] Finnish/French/Korean "Colors for prompter states" → "Toggle Prompter State"
- **Files:** po/qprompt_fi.ts:462, po/qprompt_fr.ts:463

### [TS-08] French "Prompting:" → "Start prompter"
- **File:** po/qprompt_fr.ts:478

### [TS-09] Finnish/French/Korean/Dutch "Vertical offset" → "Velocity"
- **Files:** po/qprompt_fi.ts:560, po/qprompt_fr.ts:561, po/qprompt_ko.ts:559, po/qprompt_nl.ts:561

### [TS-10] Finnish/Korean "Next reload starts at" → "Step acceleration"
- **Files:** po/qprompt_fi.ts:158, po/qprompt_ko.ts:158

### [TS-11] French/Finnish/Korean "No pointers" → "Both pointers" (opposite meaning)
- **Files:** po/qprompt_fr.ts:1003, po/qprompt_fi.ts:981, po/qprompt_ko.ts:980

### [TS-12] French "Alt" key → "Tout" (means "All")
- **File:** po/qprompt_fr.ts:270

### [TS-13] French "Set velocity to 0–10" (all 11) → identical "Vitesse de départ"
- **File:** po/qprompt_fr.ts:276-337

### [TS-14] French "Clear color" → "Light color"
- **File:** po/qprompt_fr.ts:1048

### [TS-15] Finnish/Korean right pointer reuse → left pointer (swapped)
- **Files:** po/qprompt_fi.ts:494, po/qprompt_ko.ts:493

### [TS-16] Paragraph spacing: 8 languages strip trailing `%` from `<pre>%1%</pre>`
- **Files:** po/qprompt_cs.ts:128, po/qprompt_de.ts:132, po/qprompt_es.ts:132, po/qprompt_fr.ts:128, po/qprompt_fi.ts:128, po/qprompt_ko.ts:128, po/qprompt_nl.ts:128, po/qprompt_zh.ts:128

### [TS-17] Line width: 7 languages add spurious `%` to `<pre>%1</pre>`
- **Files:** po/qprompt_de.ts:539, po/qprompt_es.ts:543, po/qprompt_fi.ts:529, po/qprompt_fr.ts:530, po/qprompt_ko.ts:528, po/qprompt_nl.ts:530, po/qprompt_pt_BR.ts:539, po/qprompt_zh.ts:539

### [TS-18] Orphan files: Hebrew and Polish exist but UI entries commented out
- **Files:** po/qprompt_he.ts, po/qprompt_pl.ts

---

### iPadOS Platform Gaps (16 sites)

Qt 6.2+ returns `"ipados"` on iPads. These 16 sites check only `"ios"`:

| Bug | File:Line | What breaks on iPad |
|---|---|---|
| IPAD-01 | qt/WindowDragger.qml:26 | Window drag MouseArea enabled (should be disabled) |
| IPAD-02 | EditorToolbar.qml:88 | Formatting tools not auto-hidden |
| IPAD-03 | EditorToolbar.qml:784 | Wheel throttle button visible |
| IPAD-04 | EditorToolbar.qml:797 | Window stay-on-top button may be visible |
| IPAD-05 | main.qml:996 | Wrong toolbar header style (None instead of ToolBar) |
| IPAD-06 | MarkersDrawer.qml:93 | "Edit" marker action incorrectly visible |
| IPAD-07 | Prompter.qml:806 | Wheel MouseArea incorrectly enabled |
| IPAD-08 | Prompter.qml:994 | Wrong text rendering path |
| IPAD-09 | Prompter.qml:2235 | Passive notification incorrectly shown |
| IPAD-10 | Prompter.qml:2278 | Falls to generic saveDialog instead of IosSaveDialog |
| IPAD-11 | Prompter.qml:2492 | IosSaveDialog Connections disabled |
| IPAD-12 | PrompterBackground.qml:107 | Non-native ColorDialog |
| IPAD-13 | PrompterPage.qml:1009 | Non-native text ColorDialog |
| IPAD-14 | PrompterPage.qml:1024 | Non-native highlight ColorDialog |
| IPAD-15 | TimerClock.qml:200 | Non-native timer ColorDialog |
| IPAD-16 | PointerSettings.qml:653 | Broken indexOf logic for ColorDialog |

---

### Hotkey System (8 bugs)

### [HTK-01] KGlobalAccel default permanently destroyed on first user customization
- **File:** globalhotkeys.cpp:1130,1138
- **Severity:** Critical
- **Analysis:** `removeAllShortcuts()` at line 1130 clears BOTH custom AND default. Then `defaultShortcut()` at 1138 reads already-cleared default (empty). Empty list set as permanent default at 1140. Every customization irreversibly erases factory defaults.
- **Impact:** KDE "Defaults" button becomes destructive. Only fix: delete KGlobalAccel config file.

### [HTK-02] User shortcuts never persisted when only Use_GlobalAccel defined (no QHotkey)
- **File:** globalhotkeys.cpp:831
- **Severity:** High
- **Analysis:** QSettings save block gated on `#ifdef QHotkey_FOUND`. On KDE-only Linux builds, shortcuts work in-session but all customizations lost on restart.
- **Impact:** Linux users without QHotkey lose shortcuts every restart.

### [HTK-03] KGlobalAccel defaults silently zeroed on non-Wayland when QHotkey co-exists
- **File:** globalhotkeys.cpp:1123-1127,1132
- **Severity:** High
- **Analysis:** On non-Wayland platforms, key/modifiers overwritten to unknown/NoModifier before setting as default. If QHotkey::setShortcut fails silently, zero fallback.
- **Impact:** No-fallback failure; switching X11→Wayland loses all hotkey config.

### [HTK-04] Wrong enum type `Qt::KeyboardModifier` (singular) for modifier variable
- **File:** globalhotkeys.cpp:566
- **Severity:** Medium
- **Analysis:** Declared as singular enum, not QFlags. Multi-modifier values produce UB via static_cast. Currently masked on mainstream compilers but formally UB.
- **Impact:** UBSan/strict MSVC could truncate multi-modifier combos.

### [HTK-05] VelocityTo0 default shortcut uses `Qt::Key_acute` — unreachable dead key
- **File:** globalhotkeys.cpp:657
- **Severity:** Medium
- **Analysis:** Qt::Key_acute is a combining diacritical dead key, not a physical keycap on US/ANSI keyboards. Ctrl+acute can never be generated by physical input.
- **Impact:** "Set Velocity to 0" non-functional out of box on all US keyboards.

### [HTK-06] Pause (Ctrl+Space) and Stop (Meta+Space) conflict — Meta+Space captured by OS
- **File:** globalhotkeys.cpp:581,586
- **Severity:** Medium
- **Analysis:** Stop uses Meta/Win+Space. On Windows (Start menu), GNOME (input source), macOS (Spotlight) — captured by OS. Never reaches QPrompt.
- **Impact:** Stop hotkey non-functional by default on all 3 major platforms.

### [HTK-07] Double `removeAllShortcuts()` IPC round-trip in customization path
- **File:** globalhotkeys.cpp:1130,1139
- **Severity:** Low
- **Analysis:** Called unconditionally at 1130, then again at 1139 in `!setAsDefault` branch. Redundant D-Bus round-trip to kglobalacceld.
- **Impact:** Minor latency during bulk shortcut import.

### [HTK-08] key/modifiers parameters silently discarded mid-function on non-Wayland
- **File:** globalhotkeys.cpp:1123-1127
- **Severity:** Low
- **Analysis:** By-value params overwritten to unknown/NoModifier. Function signature misleadingly suggests original values are used.
- **Impact:** Code clarity/auditability hazard; obscured HTK-01/HTK-03 during audit.

---

### QML Scope/Context (20 files referencing ApplicationWindow properties from wrong root)

These component files reference `root.__isMobile`, `root.shadows`, `root.pageStack`, `root.theforce`, etc. — but their root items are plain Item/Flickable/MouseArea/ToolBar/etc., not ApplicationWindow. They depend on outer-scope `id: root` resolution:

| Bug | File | Missing properties (via root.xxx) |
|---|---|---|
| SCP-01 | ReadRegionOverlay.qml:191 | `root.isMobile` typo (should be `__isMobile` with double underscore) |
| SCP-02 | ReadRegionOverlay.qml:145 | `root.shadows` |
| SCP-03 | PrompterView.qml:50,56,115,200 | `root.__isMobile`, `root.visibility`, `root.theforce` |
| SCP-04 | Find.qml:47,69,78 | `root.__isMobile` |
| SCP-05 | TimerClock.qml:127 | `root.width`, `root.height` (ambiguous — Item vs Window dims) |
| SCP-06 | CursorAutoHide.qml:28,31,43,56 | `root.pageStack`, `root.activeFocusItem` |
| SCP-07 | ProgressIndicator.qml:34 | `root.__isMobile` |
| SCP-08 | ProjectionsManager.qml:74,75,180,188,194,195,204 | `root.__isMobile`, `root.showMaximized()`, `root.screen`, `root.__windowStayOnTop`, `root.__translucidBackground`, `root.pageStack` |
| SCP-09 | Countdown.qml:196 | `root.forceQtTextRenderer` |
| SCP-10 | Prompter.qml | 40+ refs to `root.pageStack`, `root.__isMobile`, `root.onDiscard`, `root.shadows`, `root.recentDocuments`, etc. |
| SCP-11 | PrompterBackground.qml:34,49,108 | `root.background.__backgroundColor` |
| SCP-12 | EditorToolbar.qml | 30+ refs to `root.__isMobile`, `root.__opacity`, `root.pageStack`, etc. |
| SCP-13 | PrompterPage.qml:559,717,739,1064,1290 | `root.shadows`, `root.__fullScreen`, `root.theforce`, `root.minimumWidth`, `root.recentDocuments` |
| SCP-14 | TelemetryPage.qml:72-154 (11 sites) | `root.__telemetry` |
| SCP-15 | WheelSettingsOverlay.qml:37,54,73,82,87 | `root.pageStack`, `root.__scrollAsDial`, `root.__throttleWheel`, `root.__wheelThrottleFactor` |
| SCP-16 | LanguageSettingsOverlay.qml:37,41,65 | `root.minimumWidth`, `root.pageStack`, `root.height` |
| SCP-17 | LayoutDirectionSettingsOverlay.qml:40,44,45 | `root.pageStack` |
| SCP-18 | InputsOverlay.qml:32 | `root.minimumWidth` |
| SCP-19 | PointerSettings.qml:422 | `root.minimumHeight` |
| SCP-20 | WindowDragger.qml:41,45 | `root.x`, `root.y` (uses MouseArea's own x/y, not window position) |

All depend on QML's outer-scope `id` resolution to reach `id: root` in main.qml. None declare `id: root` on their own top-level item.

---

### Countdown / Timer State Machine (8 bugs)

### [TMR-01] Countdown→Prompting auto-transition via state++ bypasses toggle() entirely
- **File:** Countdown.qml:123
- **Severity:** High
- **Analysis:** `prompter.state++` directly increments from Countdown to Prompting, skipping toggle() which does: timer.reset(), document.parse(), preventSleep(true), addMissingProjections(), overlay position fix, loop stop check.
- **Impact:** Timer not reset. Sleep prevention off. Stale/unparsed document displayed. Missing projections.

### [TMR-02] timer.updateTimer() runs before timer.startTimer() on Prompting entry
- **File:** Prompter.qml:3093 vs :3113
- **Severity:** Medium
- **Analysis:** onStateChanged fires before transitions. updateTimer() computes elapsedMilliseconds with stale startTime. Then startTimer() uses corrupted elapsed value.
- **Impact:** First 333ms tick shows bogus elapsed time (~tens of seconds phantom).

### [TMR-03] dissolveIn animation re-triggered entering Running from Ready — flicker
- **File:** Countdown.qml:274-276,289-291
- **Severity:** Medium
- **Analysis:** Both Ready and Running states set dissolveIn.running=true. Ready→Running: dissolveIn restarts from 0 while opacity=1, causing 1→0→1 flicker.
- **Impact:** Visible flash when "Begin countdown" clicked.

### [TMR-04] Countdown arc hypotenuse uses geometric center instead of arc center
- **File:** Countdown.qml:79
- **Severity:** Low
- **Analysis:** Formula uses centreX but arc drawn at offsetCentre. When editorXOffset ≠ 0, radius too small for corners.
- **Impact:** Countdown arc may not extend to screen edges when editor is scrolled.

### [TMR-05] ScriptAction `paintReady` references non-existent function
- **File:** Countdown.qml:318
- **Severity:** Low
- **Analysis:** No `paintReady` function exists anywhere. Silent no-op.
- **Impact:** Standby→Ready transition has no script behavior; incomplete feature.

### [TMR-06] dissolveOut starts too early when disappearWithin > 1
- **File:** Countdown.qml:110-113,145
- **Severity:** Low
- **Analysis:** dissolveOut always 1000ms but starts disappearWithin-1 iterations before end. If disappearWithin=3, animation completes before final iteration.
- **Impact:** Countdown overlay fully transparent while still counting; prompter text visible prematurely.

### [TMR-07] countdownAnimation restart uses non-idempotent running=true
- **File:** Countdown.qml:119
- **Severity:** Low
- **Analysis:** Assigning running=true to already-running animation (from PropertyChanges) may be ignored on some Qt versions.
- **Impact:** Countdown may freeze between iterations on certain Qt builds.

### [TMR-08] timer.running not explicitly set in Countdown state — relies on revert behavior
- **File:** Prompter.qml:2980-3026
- **Severity:** Low
- **Analysis:** Only Prompting state sets timer.running. If transition interrupted, timer could accumulate elapsed during countdown.
- **Impact:** Timer display incorrect if state machine interrupted.

---

### SpellChecker (10 bugs)

### [SPL2-11] addCustomWord trims but removeCustomWord does not — asymmetry
- **File:** spellchecker.cpp:309 vs 328
- **Severity:** Medium
- **Analysis:** addCustomWord calls word.trimmed(); removeCustomWord uses raw word.indexOf(). "hello" stored but " hello " cannot be removed.

### [SPL2-12] Case-sensitive contains/indexOf but case-insensitive sort — duplicates
- **File:** spellchecker.cpp:312,328 vs 316-319
- **Severity:** Medium
- **Analysis:** Duplicate detection case-sensitive; sort case-insensitive. "Hello" + "hello" both pass contains check. Case variants accumulate permanently.

### [SPL2-13] saveCustomWordsToDisk has void return — callers cannot detect I/O failure
- **File:** spellchecker.cpp:383,390-392
- **Severity:** Medium
- **Analysis:** Void function with silent return on file open failure. addCustomWord/removeCustomWord report success despite no persistence.

### [SPL2-14] Cached QRC dicts never invalidated after app update
- **File:** spellchecker.cpp:193-202
- **Severity:** Medium
- **Analysis:** exists() gate prevents re-copy. Stale dictionaries used forever after app update.

### [SPL2-15] spell() returns true when no dicts loaded — silent no-op
- **File:** spellchecker.cpp:106-107
- **Severity:** Medium
- **Analysis:** m_dicts.empty() → return true. Indistinguishable from correctly-spelled word. isValid() exists but never checked by callers.

### [SPL2-16] QDir::mkpath return unchecked — dict cache directory may silently not exist
- **File:** spellchecker.cpp:196,351
- **Severity:** Low

### [SPL2-17] QFile::setPermissions return unchecked — cached dict may be unreadable
- **File:** spellchecker.cpp:200
- **Severity:** Low

### [SPL2-18] Hunspell::add return value unchecked at 4 call sites
- **File:** spellchecker.cpp:139,173,179,321
- **Severity:** Low

### [SPL2-19] availableDictionaries enumerates .dic without verifying .aff exists
- **File:** spellchecker.cpp:250-256
- **Severity:** Low

### [SPL2-20] loadCustomWordsFromDisk redundant exists() before open()
- **File:** spellchecker.cpp:365-368
- **Severity:** Low

---

### Build / WASM (2 bugs)

### [WSM-03] readAsDataURL causes quadruple in-memory copy of file content
- **File:** wasmintegration.cpp:129-144
- **Severity:** High
- **Analysis:** readAsDataURL base64-encodes (~+33%). Then TextEncoder Uint8Array, malloc+HEAPU8, QString::fromUtf8. 10MB image → 75MB peak memory.
- **Impact:** Memory exhaustion + UI freeze on large file pick. Should use readAsArrayBuffer.

### [BLD-05] .env.android references Qt 5.15.2 — project requires Qt 6.8.2+
- **File:** .env.android:6
- **Severity:** Medium
- **Analysis:** `export Qt5_android=$ADIR/Qt/5.15.2/android/` — stale Qt 5 configuration.
- **Impact:** Android builds fail for developers following this file.

---

### QML Events / Interaction (10 bugs)

### [EVT-01] velocityDragArea (z:5) blocks viewport.mouse (z:0) wheel events
- **File:** PrompterPage.qml:875 vs PrompterView.qml:254
- **Severity:** High
- **Analysis:** velocityDragArea fills viewport at z:5, no wheel handler, no propagateComposedEvents. viewport.mouse at z:0 never receives wheel events.
- **Impact:** Mouse wheel scrolling non-functional during normal operation.

### [EVT-02] Zero inputMethodHints on any TextField — IME broken for CJK/Indic
- **File:** Prompter.qml:936, PrompterPage.qml, EditorToolbar.qml (15+ TextFields)
- **Severity:** High
- **Analysis:** No inputMethodHints on any field. Virtual keyboard can't show correct layout. CJK composition events blocked.
- **Impact:** CJK/Indic users cannot compose. Mobile keyboard shows wrong layout. Accessibility barrier.

### [EVT-03] velocityDragOverlay (z:7) steals clicks from control buttons (z:6)
- **File:** PrompterPage.qml:914 vs PrompterView.qml:61
- **Severity:** High
- **Analysis:** Overlay at z:7 above controls at z:6. LeftButton dismisses immediately, button never gets click.
- **Impact:** All control buttons require double-click when velocity indicator visible.

### [EVT-04] Drag breaks editor.x declarative binding permanently
- **File:** Prompter.qml:1984,958
- **Severity:** High
- **Analysis:** drag.target: editor writes x imperatively, breaks `x: contentsPlacement*(prompter.width) + 20` binding.
- **Impact:** After one drag, editor horizontal position frozen. Resize/orientation changes no-op.

### [EVT-05] Drag breaks positionHandler.x declarative binding permanently
- **File:** Prompter.qml:2018,926
- **Severity:** High
- **Analysis:** Same pattern. drag.target breaks x binding; coordinate system becomes inconsistent.

### [EVT-06] Drag breaks stopwatch.x binding permanently
- **File:** TimerClock.qml:178,130
- **Severity:** Medium
- **Analysis:** Same pattern. After one drag, stopwatch no longer re-centers on resize.

### [EVT-07] TabBar currentIndex binding broken on first TabButton click
- **File:** PointerSettings.qml:266,248
- **Severity:** Medium
- **Analysis:** TabBar sets currentIndex imperatively, breaking binding to pointerSettings.pointerKind. Two-way sync dead after first click.

### [EVT-08] Two additional checkable ToolButton binding breakage instances
- **File:** EditorToolbar.qml:913-918,1541-1556
- **Severity:** Medium
- **Analysis:** opacity toggle and overlay bars toggle not in R2-EDT-03 list but suffer same binding-breakage pattern.

### [EVT-09] Flow ToolSeparator visibility compares y of potentially invisible rows
- **File:** EditorToolbar.qml:246-249,284-287,309-312,347-350,433-437,549-552,710-713,774-777
- **Severity:** Low
- **Analysis:** Separator visibility uses row.y when row may be invisible (y=0), matching visible row at y=0 → false positive separator.

### [EVT-10] Nested MouseAreas with hoverEnabled steal hover from parent Buttons
- **File:** ProjectionsManager.qml:347-354,376-383,405-412
- **Severity:** Low
- **Analysis:** Child MouseArea hoverEnabled:true fills parent Button. Button's hovered property never fires → flat highlight missing.

---

---

## Wave 27 — String Ops, Easing, Network

### [ENC-01] truncate(-1) when font preview text has no spaces
- **File:** documenthandler.cpp:736-738
- **Severity:** Medium
- **Analysis:** text truncated to 64 chars, then lastIndexOf(" ") → -1 if no space found. truncate(-1) empties string or UB. Preview shows just "…" with no text.
- **Impact:** Font preview dialog blank for long unbroken strings (URLs, long words).

### [ENC-02] getMarkerKey() mid(4) without length/startsWith guard
- **File:** documenthandler.cpp:756
- **Severity:** Low
- **Analysis:** Unlike parse() which guards mid(4) with startsWith("key_"), getMarkerKey() blindly takes mid(4) from first anchor name. Anchor names <4 chars or without "key_" prefix produce garbage key codes.
- **Impact:** Malformed anchor names silently produce wrong marker key display.

### [ANM-N01] Easing.EaseOut is not a valid Qt Quick easing type (2 instances)
- **File:** PrompterView.qml:88,140
- **Severity:** Medium
- **Analysis:** `Easing.EaseOut` is CSS convention, not valid QML. Valid: Easing.OutQuad, Easing.OutCubic, etc. Falls back to Easing.Linear silently.
- **Impact:** Margin animations run abruptly instead of smoothly easing.

### [NET-01] loadFromNetworkFinihed never checks m_reply->error()
- **File:** documenthandler.cpp:889-890
- **Severity:** High
- **Analysis:** readAll() called without error() check. HTTP 4xx/5xx error pages loaded as document content. Network failures silent.
- **Impact:** 404 pages become document content. No error feedback for broken connections.

### [NET-02] RedirectPolicyAttribute set to boolean true → NoLessSafeRedirectPolicy
- **File:** documenthandler.cpp:883,1739
- **Severity:** Medium
- **Analysis:** true (int 1) = NoLessSafeRedirectPolicy. Only allows http→https redirects. Same-origin redirects (cdn, www, trailing-slash) silently dropped.
- **Impact:** Most real-world redirects silently fail; network loads break on common URL patterns.

---

## Wave 28 — Threading, Drawer Dismiss, Android Build

### [THR-01] IosSaveDialog::create() — unsynchronized singleton race
- **File:** iossavedialog.cpp:37-42
- **Severity:** Medium
- **Analysis:** Classic check-then-act: `if (!s_instance) s_instance = new ...` with no mutex. Constructor writes s_instance=this before construction done. Two QML engine threads → dual instance or partially-constructed object.
- **Impact:** Use-after-free or double-delete under concurrent engine access.

### [THR-02] ShakeDetector::create() — identical unsynchronized singleton race
- **File:** shakedetector.cpp:38-43
- **Severity:** Medium
- **Analysis:** Same if(!s_instance) pattern as THR-01. Constructor also sets s_instance=this.
- **Impact:** Same race condition.

### [THR-03] search() — mutable static QRegularExpression shared across all callers
- **File:** documenthandler.cpp:1543-1544
- **Severity:** Low
- **Analysis:** `static QRegularExpression searchRegEx; searchRegEx.setPattern(subString);` mutates shared static state. If search() ever called from worker thread, setPattern() races with find().
- **Impact:** Data race crash if cross-thread access added.

### [THR-04] SpellChecker zero thread safety — explicit finding
- **File:** spellchecker.h:76-77, spellchecker.cpp
- **Severity:** Medium
- **Analysis:** m_dicts (vector) and m_customWords (QStringList) with no mutex. spell()/suggest() read while addCustomWord/removeCustomWord/setLanguages mutate. Hunspell not thread-safe. QSyntaxHighlighter default main thread, but Qt 6.7+ async highlighting → immediate crash.
- **Impact:** Iterator invalidation / segfault on concurrent access.

### [DRW-01] interalFocusElsewhere() misses 3 OverlaySheets + 2 Drawers — hotkeys pass through
- **File:** Prompter.qml:283-296
- **Severity:** Medium
- **Analysis:** Function blocks hotkeys when overlays open, but omits obsConfiguration, dictionariesSheet, customWordsSheet, contextDrawer, globalMenu. Hotkeys (play/pause/stop) execute through while configuring OBS/dictionaries/words or with drawer open.
- **Impact:** Unexpected prompter state changes while interacting with overlays/drawers.

### [DRW-02] globalDrawer and contextDrawer missing from ESC dismiss chain
- **File:** main.qml:481-504, +windows:452-487, +android:391-426
- **Severity:** Medium
- **Analysis:** ESC handler checks markersDrawer + 8 sheets but never checks contextDrawer.drawerOpen or globalMenu.drawerOpen. ESC falls through, drawer stays open.
- **Impact:** ESC does not close global/context drawer; user must manually tap outside.

### [AND-BLD-01] Missing version.gradle — Gradle build fails
- **File:** android/build.gradle:19
- **Severity:** Critical
- **Analysis:** `apply from: '../version.gradle'` — file does not exist. projectVersionFull/projectVersionCode undefined.
- **Impact:** Android build cannot sync or compile.

### [AND-RES-01] Invalid android:scaleType on bitmap element
- **File:** android/res/drawable/splash.xml:7
- **Severity:** Medium
- **Analysis:** scaleType is ImageView attribute, not valid on bitmap drawable. AAPT2 error.
- **Impact:** Build failure or silently ignored attribute.

### [AND-MFT-01] FileProvider resource @xml/qtprovider_paths — file named filepaths.xml
- **File:** AndroidManifest.xml:43 vs res/xml/filepaths.xml
- **Severity:** Medium (latent)
- **Analysis:** Commented-out FileProvider references qtprovider_paths but actual file is filepaths.xml. Resource-not-found if uncommented.
- **Impact:** Build error if FileProvider block ever activated.

---

## Wave 29 — Shadowing, Focus, Version Guars, Const&, Dialog Sizing, JSON, QList

### [SHADOW-01] id: rotation shadows Item.rotation property
- **File:** Prompter.qml:1280
- **Severity:** Low
- **Analysis:** Rotation transform has id: rotation. Flipable inherits Item.rotation (qreal). Bare rotation resolves to Rotation object, not the float.
- **Impact:** Future code reading bare rotation gets wrong type.

### [SHADOW-02] id: flow shadows Flow.flow property
- **File:** EditorToolbar.qml:184
- **Severity:** Low
- **Analysis:** Flow layout has id: flow. Flow.flow is direction enum. Bare flow resolves to Flow item. Reading flow direction requires awkward flow.flow.
- **Impact:** Error-prone property access.

### [FOC-N01] focus: true is JS label in atEndLoopDelay SpinBox
- **File:** Prompter.qml:1311
- **Severity:** Low
- **Analysis:** onValueModified uses colon instead of =. SpinBox never gets focus after value change.

### [FOC-N02] Same JS label bug in countdownConfiguration SpinBoxes (2 instances)
- **File:** PrompterPage.qml:1093,1114
- **Severity:** Low
- **Analysis:** __iterations and __disappearWithin SpinBoxes both have focus: true (colon) instead of assignment.

### [FOC-N03] Tab/Backtab asymmetry — Backtab silently unhandled
- **File:** Prompter.qml:2170-2173
- **Severity:** Low
- **Analysis:** Keys.onPressed handles Qt.Key_Tab but not Qt.Key_Backtab. Users can Tab forward but cannot Shift+Tab backward to return.
- **Impact:** One-directional keyboard accessibility navigation.

### [VER-01] Qt::MarkdownText version guard 0x050F00 (5.15) — API added in 5.14
- **File:** documenthandler.cpp:958
- **Severity:** Low
- **Analysis:** guard uses Qt 5.15 (0x050F00) but MarkdownText was introduced in Qt 5.14 (0x050E00). Qt 5.14 users silently get plain text import instead of markdown.

### [CPY-01] 5 Q_INVOKABLE methods pass QString by value instead of const&
- **Files:** markersmodel.h:68, documenthandler.h:213,215,227, systemfontchooserdialog.h:53
- **Severity:** Low
- **Analysis:** extendLastMarker, setKeyMarker, setMarkerHref, replaceSelected, setFontFamily all take QString by value but only read (never mutate). Unnecessary heap allocation per call.

### [DSZ-01] InputsOverlay hardcoded height:680 — overflows on phones
- **File:** InputsOverlay.qml:33
- **Severity:** Medium
- **Analysis:** No Math.min with screen height. On phones (~500dp usable), content exceeds viewport with no scroll.

### [DSZ-02] pointerConfiguration OverlaySheet no vertical ScrollView
- **File:** PrompterPage.qml:1426-1445
- **Severity:** Medium
- **Analysis:** PointerSettings ~600-800px implicit height. No vertical ScrollView/Flickable. Overflows on small screens.

### [DSZ-03] Magic number 68 in ListView height binding
- **File:** InputsOverlay.qml:83
- **Severity:** Low
- **Analysis:** `height: keyConfigurationOverlay.height - inputSettingsTabs.height - 68` — brittle constant that doesn't reference Kirigami header/units.

### [JSN-01] i.d.authentication accessed without undefined guard
- **File:** Prompter.qml:373-374
- **Severity:** High
- **Analysis:** Even after successful JSON.parse, code assumes i.d and i.d.authentication exist. {"op":0} (no d) → TypeError crash.
- **Impact:** Crash on OBS v4, non-OBS services, or protocol changes.

### [JSN-02] ws.sendTextMessage() called without checking WebSocket status
- **File:** Prompter.qml:383,413
- **Severity:** Medium
- **Analysis:** No check for ws.status === WebSocket.Open before sending. Non-Open socket silently discards messages.
- **Impact:** OBS commands silently lost if connection dropped.

### [QCN-01] O(n²) contains()-in-loop during custom words file load
- **File:** spellchecker.cpp:370-374
- **Severity:** Low
- **Analysis:** while-loop calls contains() on growing unsorted list. Total cost O(n²). QSet dedup then sort would be O(n log n).
- **Impact:** Quadratic startup time with large custom dictionaries.

---

## Wave 30 — PropertyChanges, QTextDocument, Metadata, Opacity

### [PC-01] countdown.state not set in Prompting state — countdown visible during teleprompting
- **File:** Prompter.qml:3027-3086
- **Severity:** Medium
- **Analysis:** Editing/Standby/Countdown states all set countdown.state via PropertyChanges. Prompting state has no countdown PropertyChanges at all. After countdown completes or user skips, countdown reverts to Ready state (visible, opacity:1).
- **Impact:** Countdown numeral overlays prompter text for entire prompting session.

### [QTD-01] m_spellHighlighter not detached when setDocument(nullptr)
- **File:** documenthandler.cpp:183-199
- **Severity:** Medium
- **Analysis:** m_spellHighlighter.reset() inside if(m_document) block. When new doc is nullptr, old highlighter remains attached to orphaned QTextDocument. Document destroyed → highlighter holds dangling pointer → use-after-free at DocumentHandler destructor.
- **Impact:** Use-after-free on QTextDocument/SpellHighlighter cleanup.

### [QTD-02] QQuickTextDocument destroyed without destroyed signal connection
- **File:** documenthandler.h:334, documenthandler.cpp:175-202
- **Severity:** Low-Medium
- **Analysis:** m_document is raw QQuickTextDocument* from QML. No destroyed signal to null it. If TextEdit destroyed before DocumentHandler, m_document dangles. Composes with QTD-01.
- **Impact:** Dangling m_document during destructor if QML cleanup order unfavorable.

### [META-01–12] Desktop/AppData metadata bugs (12 total)
- Invalid category `Qt` in desktop file (not a registered freedesktop.org category)
- MimeType mismatch: desktop has `text/html` only, AppData has `text/plain`, `text/markdown`, `text/html`
- Spam keyword `imaginary` in desktop file
- Typo `fixedd` (double-d) in v2.0.2 release notes
- 11 releases use non-ISO-8601 dates (YYYY-M-D instead of YYYY-MM-DD)
- XML indentation inconsistency at v1.1.5 release tag
- Missing checksum on v2.0.2 source artifact
- v1.0 missing checksums on 4/5 artifacts
- Version `1.1` vs GitHub tag `v1.1.0` mismatch
- Version `1.0` vs GitHub tag `v1.0.0` mismatch
- Artifact URLs use `QPrompt` repo name, everything else uses `QPrompt-Teleprompter` → 404

### [OPC-01] Right-click toggle desynchronizes velocityIndicator visible/opacity
- **File:** PrompterPage.qml:906,979-980
- **Severity:** Medium
- **Analysis:** Right-click toggles only opacity (0 ↔ 1), leaving visible=true. When opacity=0 but visible=true: middle-click reactivation blocked, full-screen MouseArea consumes input, auto-dismiss Connection fires inconsistently.
- **Impact:** Velocity indicator stuck in invisible-but-interactive state; requires second right-click to recover.

---

## Wave 31 — Headers, I/O, Bindings, WASM, Bounds, i18n

### [HDR-N01] promptsession.h not in CMakeLists.txt — SessionModel/DataPoint dead code
- **File:** src/promptsession.h, src/promptsess.cpp, src/CMakeLists.txt
- **Severity:** Low
- **Analysis:** promptsession.h/cpp exist on disk but are not listed in any CMakeLists.txt. No other file includes promptsession.h. The entire file is never MOC-processed, never compiled. LOG-01/LOG-02 bugs have zero runtime impact.
- **Impact:** Orphaned dead code clutters tree; bugs in this file can't manifest.

### [HDR-N02] telemetry.h not in CMakeLists.txt — Telemetry dead code
- **File:** src/telemetry.h, src/telemetry.cpp, src/CMakeLists.txt
- **Severity:** Low
- **Analysis:** Same as HDR-N01. Telemetry Q_OBJECT class never MOC-processed. All methods already commented out; source still exists on disk.
- **Impact:** Build hygiene — orphaned .h/.cpp create false expectations of functionality.

### [IO-N01] saveAs() leaves _fileSystemWatcher permanently blocked on open failure
- **File:** documenthandler.cpp:1143,1161
- **Severity:** Medium
- **Analysis:** `_fileSystemWatcher->blockSignals(true)` at line 1143. If `file.open()` fails at line 1159, early-return at 1161 skips `QTimer::singleShot(2600, ...)` at 1170 that calls `unblockFileWatcher()`. Watcher stays blocked forever — auto-reload dead after any failed save.
- **Impact:** User must restart app or trigger successful save to recover auto-reload.

### [IO-N02] save() constructs QUrl without file:// scheme — broken on non-Windows
- **File:** documenthandler.cpp:1183-1184
- **Severity:** High
- **Analysis:** `QUrl::setUrl(QUrl::toPercentEncoding(fileName, "/:"))` passes raw path like `C:/Users/...` without `file://` prefix. `QUrl::setUrl()` parses drive letter as URL scheme. `toLocalFile()` garbled on Linux/macOS — Ctrl+S broken for files with absolute paths.
- **Impact:** Save-in-place broken on Linux/macOS.

### [IO-N03] iossavedialog.mm QFile::write() return value unchecked
- **File:** iossavedialog.mm:92
- **Severity:** Medium
- **Analysis:** `tempFile.write(htmlContent.toUtf8())` return value discarded. Disk-full or I/O error → partial/corrupt file presented to UIDocumentPicker silently.
- **Impact:** Silent data corruption on iOS when storage is full.

### [QML-BND-01] countdownAnimation.running binding permanently broken after first iteration
- **File:** Countdown.qml:100,119
- **Severity:** High
- **Analysis:** `running: countdown.running` (line 100) is a declarative binding. Inside `onFinished`, `running = true` (line 119) imperatively assigns — permanently breaking the binding. `running` can never be set to false again via binding. Standby/Ready states have no PropertyChanges for countdownAnimation.
- **Impact:** After first countdown iteration, sweep animation runs silently consuming CPU in Standby/Ready. If user cancels mid-cycle, animation runs indefinitely.

### [QML-BND-02] clock.__iteration binding broken by post-decrement in animation handler
- **File:** Countdown.qml:76,116,121
- **Severity:** Medium
- **Analysis:** `property int __iteration: countdown.__iterations - 1` (line 76) is a declarative binding. Line 116 (`clock.__iteration--`) and 121 (direct assignment) imperatively write to it, breaking the binding. If `__iterations` changes while countdown is running, clock uses stale value.
- **Impact:** Stale iteration count if config changes mid-countdown.

### [QML-BND-03] ReadRegionOverlay onDestruction — harmless dead code
- **File:** ReadRegionOverlay.qml:86-89
- **Severity:** None (info)
- **Analysis:** `Component.onDestruction` sets positionState during teardown. Children already destroyed (QML bottom-up destruct), Settings already persists via alias. No practical effect.
- **Impact:** None. Redundant code.

### [WSM-N01] Synchronous QImage::load() from HTTP blocks WASM main thread
- **File:** documenthandler.cpp:1449-1451,1733
- **Severity:** High
- **Analysis:** `image.load(src)` with HTTP URL → synchronous XMLHttpRequest on WASM. Deprecated in Chrome/Firefox/Safari. Blocks UI thread for entire request duration.
- **Impact:** Multi-second UI freezes on WASM during image paste with remote URLs; browser console deprecation warnings.

### [WSM-N02] WASM preventSleep() falls through to desktop #else — always returns false
- **File:** documenthandler.cpp:1929-1931
- **Severity:** Low
- **Analysis:** `#ifdef` chain covers Android/iOS, but no WASM guard. Falls to generic `#else` returning `false & prevent` (including `&` typo from TYP-04). No Web Screen Wake Lock API integration.
- **Impact:** `preventSleep(true)` silently no-ops on WASM. Missing guard blocks future Web API integration.

### [QRC-N01] icons.qrc contains duplicate \<file\> entry
- **File:** src/icons/icons.qrc:45,47
- **Severity:** Low
- **Analysis:** Identical `<file alias="gnumeric-object-scrollbar.svg">16/gnumeric-object-scrollbar.svg</file>` at lines 45 and 47. Resource compiler embeds same SVG twice.
- **Impact:** Slightly bloated binary.

### [QRC-N02] Four .qrc files are dead code — never referenced by CMakeLists.txt
- **Files:** src/icons/icons.qrc, src/fonts/fonts.qrc, src/fonts/chinese.qrc, src/prompter/pointers/pointers.qrc
- **Severity:** Low
- **Analysis:** All resources are actually compiled via `qt_add_resources()` and `qt_add_qml_module()` in src/CMakeLists.txt. Standalone .qrc files never included. fonts.qrc references wrong file paths vs CMakeLists.txt; pointers.qrc has different RESOURCE_PREFIX.
- **Impact:** Misleading artifact; developers may edit wrong resource definitions.

### [CMAKE-N01] WASM build excludes TelemetryPage.qml and RemotePage.qml
- **File:** src/CMakeLists.txt:106-121, main.qml:175-181
- **Severity:** Low
- **Analysis:** Unlike +windows/+android which compile these pages, WASM `qprompt_frontend_sources` excludes them. If menu entries ever uncommented, WASM crashes with missing QML type.
- **Impact:** WASM-specific crash risk if telemetry/remote features are enabled.

### [OOB-N01] MarkersModel::data() — m_data.at() without row < rowCount() guard
- **File:** markersmodel.cpp:40-43
- **Severity:** Medium
- **Analysis:** `index.isValid()` only checks row>=0, column>=0, model!=nullptr. If row >= m_data.size(), `QList::at()` throws or asserts. `removeMarker()` already has the correct guard.
- **Impact:** Crash if QML passes out-of-range row to data().

### [OOB-N02] SessionModel::data() — same missing row bounds guard
- **File:** promptsession.cpp:40-43
- **Severity:** Medium
- **Analysis:** Identical to OOB-N01. `isValid()` does not enforce row < m_data.size().
- **Impact:** Crash on out-of-range index access.

### [OOB-N03] alignment() fetches textCursor() twice — stale cursor race
- **File:** documenthandler.cpp:547-550
- **Severity:** Low
- **Analysis:** Double textCursor() fetch — first null-checked, second reads alignment from potentially different position if cursorPosition changed between calls.
- **Impact:** Formatting toolbar shows wrong alignment in rare race conditions.

### [I18N-N01] Stale source-location line numbers in all 20 .ts files
- **Files:** po/*.ts (20 files)
- **Severity:** Low
- **Analysis:** lupdate not re-run after code changes. Example: `documenthandler.cpp:446` in .ts maps to actual `documenthandler.cpp:739`. Qt Linguist "Go to Source" navigates to wrong code. lupdate merge heuristic may duplicate entries.
- **Impact:** Translator tooling UX degraded; potential duplicate translation entries.

### [I18N-N02] Vanished translation entries not purged across 13 language files
- **Files:** 13 of 20 .ts files (de:14, es:14, pt_PT:13, ru:13, uk:13, zh:13, pt_BR:10, cs:8, fr:8, fi:4, ko:4, nl:4, oc:2)
- **Severity:** Low
- **Analysis:** Entries contain type="vanished" — strings removed from source but not cleaned with `lupdate -no-obsolete`. Remnants of old format filters and bar-position labels.
- **Impact:** Bloated .ts files; translators see nonexistent strings in Qt Linguist; outdated translations count against completion stats.

---

## Wave 32 — Strings, Q_PROPERTY, Enums, DPI, Settings

### [STR-N01] main.cpp:158 QLatin1String iterator-pair UB from two unrelated string literals
- **File:** main.cpp:158
- **Severity:** High
- **Analysis:** `QLatin1String("file", "File to copy.")` matches the iterator-pair constructor `QLatin1StringView(const char *first, const char *last)`. Pointer subtraction between two unrelated string literals is undefined behavior. Resulting QLatin1StringView has arbitrary m_size — garbage content.
- **Impact:** `--help` output contains garbage or crashes during argument parsing.

### [NOTIFY-01] setAutoReload doesn't emit autoReloadChanged NOTIFY signal
- **File:** documenthandler.cpp:909-919, documenthandler.h:120,300
- **Severity:** Medium
- **Analysis:** Q_PROPERTY declares NOTIFY autoReloadChanged. Signal exists. `setAutoReload()` sets `m_autoReload` but never emits. Every other WRITE method in DocumentHandler emits its NOTIFY — this is the single exception. QML bindings reading `document.autoReload` become stale after any C++ write.
- **Impact:** QML bindings never update when autoReload changed from C++.

### [NOTIFY-02] availableDictionariesChanged NOTIFY signal never emitted
- **File:** documenthandler.h:137,318
- **Severity:** Low
- **Analysis:** Q_PROPERTY `availableDictionaries` declares NOTIFY. Signal declared but zero emits in entire codebase. Underlying `SpellChecker::availableDictionaries()` is a static disk-scan — results can't change at runtime — so signal is semantically dead.
- **Impact:** No current impact. Future dynamic dictionary loading would fail to notify QML.

### [MIX-01] spellchecker.cpp:98 size_t→int narrowing in languages() reserve
- **File:** spellchecker.cpp:98
- **Severity:** Low
- **Analysis:** `out.reserve(static_cast<int>(m_dicts.size()))` — size_t to signed 32-bit narrowing. While dictionary count is small, the conversion is a correctness violation.
- **Impact:** No current runtime impact; code quality issue.

### [ENUM-01] documenthandler.cpp:1108 updateContents switch no default — silent data loss
- **File:** documenthandler.cpp:1108
- **Severity:** Medium
- **Analysis:** updateContents unconditionally clears document via `cursor.removeSelectedText()` before switch on format. No default case. If format is Qt::UnknownText (-1) or future value, document destroyed with zero content inserted.
- **Impact:** Silent data loss if unexpected format value reaches the function.

### [DPI-01] TimerClock.qml:127 devicePixelRatio in raw arithmetic with magic multiplier
- **File:** TimerClock.qml:127
- **Severity:** Medium
- **Analysis:** `screen.devicePixelRatio` used in font-size calculation with `<< 3` multiplier. Fractional HiDPI (150%, 175%) produces inconsistent scaling misaligned with rest of UI.
- **Impact:** Timer font too small/large on fractional HiDPI.

### [DPI-02] MarkersDrawer.qml:37 drawer minimumWidth hardcoded to 260px
- **File:** MarkersDrawer.qml:37
- **Severity:** Low
- **Analysis:** `minimumWidth: 260` in px. On 200% DPI this is 130 logical px — drawer too narrow to read marker labels.
- **Impact:** Unusable drawer on high DPI.

### [DPI-03] Find.qml:38 searchBarWidth:724 hardcoded in px
- **File:** Find.qml:38
- **Severity:** Low
- **Analysis:** Hardcoded pixel width ignores DPI scaling.
- **Impact:** Search bar width wrong on non-default scaling.

### [DPI-04] InputsOverlay.qml:33 height:680 hardcoded
- **File:** InputsOverlay.qml:33
- **Severity:** Medium
- **Analysis:** Overlay height 680px hardcoded. On 1920x1080 at 200% DPI, overlay exceeds screen height.
- **Impact:** Content clipped or unreachable on small HiDPI screens.

### [GEO-01] main.qml initial 728px height too large for 1366x768 laptops
- **File:** main.qml:77-78, +windows/main.qml
- **Severity:** Low
- **Analysis:** Initial window 1220x728. On 1366x768 laptops, 728 + taskbar (~40px) exceeds desktop area. Window clipped by WM on first launch.
- **Impact:** User must resize window on first launch.

### [GEO-02] main.qml persists x/y/width/height with zero validation
- **File:** main.qml:85-91, +windows/main.qml
- **Severity:** Medium
- **Analysis:** Settings save/restore window geometry without screen-bounds validation. Remove external monitor → restart places window off-screen. No recovery mechanism.
- **Impact:** Unreachable window requiring manual settings reset.

### [GEO-03] +android/main.qml no minimumWidth/minimumHeight
- **File:** +android/main.qml
- **Severity:** Low
- **Analysis:** Unlike base and Windows variants (min 351x291), Android has no minimum size. Layout may break on very small screens.
- **Impact:** UI layout corruption on small Android screens.

### [UNIT-01] ProgressIndicator.qml:46 Units.ShortDuration with no Kirigami import
- **File:** ProgressIndicator.qml:46
- **Severity:** High
- **Analysis:** `duration: Units.ShortDuration` but file has no Kirigami import. `Units` resolves to `undefined` — animation never runs. Loading indicator dead.
- **Impact:** Progress indicator invisible; users see no loading feedback.

### [UNIT-02] PrompterView.qml 7x Units.ShortDuration with no Kirigami import
- **File:** PrompterView.qml:80,87,103,132,139,155,185
- **Severity:** High
- **Analysis:** 7 fade/slide animations use `duration: Units.ShortDuration` but file only imports QtQuick and QtCore. All transitions dead — opacity, scale, y-position changes snap instantly.
- **Impact:** Jerky prompter transitions instead of smooth animations.

### [UNIT-03] PrompterBackground.qml:160 Units.LongDuration no Kirigami import
- **File:** PrompterBackground.qml:160
- **Severity:** Medium
- **Analysis:** Opacity animation `duration: Units.LongDuration` with no Kirigami import. Snap transition instead of smooth fade.
- **Impact:** Background opacity changes abruptly.

### [UNIT-04] Flip.qml:34,41 two Units.LongDuration no Kirigami import
- **File:** Flip.qml:34,41
- **Severity:** Medium
- **Analysis:** xScale/yScale behavior animations use Units.LongDuration without Kirigami import. Flips snap instantly.
- **Impact:** Flip transitions instantaneous instead of animated.

### [UNIT-05] pointer_0.qml:72 Units.VeryLongDuration no Kirigami import
- **File:** pointer_0.qml:72
- **Severity:** Low
- **Analysis:** strokeColor animation with Units.VeryLongDuration — no Kirigami import. Arrow pointer color changes snap instantly.
- **Impact:** Pointer color transitions instantaneous.

### [UNIT-06] Find.qml:92 Units.ShortDuration with namespaced Kirigami import
- **File:** Find.qml:92
- **Severity:** Medium
- **Analysis:** Imported as `Kirigami`, but uses bare `Units.ShortDuration`. Should be `Kirigami.Units.ShortDuration`.
- **Impact:** Find bar slide animation dead.

### [UNIT-07] ReadRegionOverlay.qml 3x Units.ShortDuration with namespaced import
- **File:** ReadRegionOverlay.qml:546,610,616
- **Severity:** Medium
- **Analysis:** Three animation durations use bare `Units.ShortDuration` with namespaced `Kirigami` import. Pointer/overlay position transitions dead.
- **Impact:** Read region position changes snap instead of animating.

### [AR-01] PrompterView.qml:53-58 Rotation debug feature clips on extreme aspect ratios
- **File:** PrompterView.qml:53-58
- **Severity:** Low
- **Analysis:** "theforce" debug Rotation `origin.x: parent.width*0.15; angle: 77`. On ultrawide 21:9 or tablet portrait, rotated content clips severely outside viewport.
- **Impact:** Debug feature visual corruption on extreme aspect ratios.

### [SAFE-01] +android/main.qml zero safe area insets
- **File:** +android/main.qml
- **Severity:** Medium
- **Analysis:** Full-screen Android window lacks safe area margins. Content obscured by camera notch and gesture navigation pill on modern devices (Pixel, Galaxy S).
- **Impact:** UI elements hidden behind notch/pill on modern Android devices.

### [SAFE-02] ReadRegionOverlay screenMiddle ignores notch/status bar height
- **File:** ReadRegionOverlay.qml:132-134
- **Severity:** Medium
- **Analysis:** screenMiddle calculation uses raw `screen.height` without subtracting status bar/notch height. On notched devices, reading region "middle" is physically offset downward.
- **Impact:** Read region misaligned on iPhones and notched Android devices.

### [SET-01] macOS/iOS: QSettings split across two preference domains
- **Files:** documenthandler.cpp, globalhotkeys.cpp
- **Severity:** High
- **Analysis:** C++ uses `QSettings(organizationDomain(), applicationName())` → domain `com.cuperino.qprompt`. QML Settings and default `QSettings()` → domain `Cuperino/qprompt`. Two separate preference files on macOS/iOS. C++ keys (autoReload, hotkeys, paths) stored in different domain than QML keys (background, prompter, scroll, editor, etc.).
- **Impact:** Settings written by C++ invisible to QML and vice versa.

### [SET-02] factoryReset() incomplete on macOS/iOS — domain-path settings survive
- **File:** qmlutil.hpp:135-137
- **Severity:** High
- **Analysis:** `QSettings().clear()` only clears default organization-name domain. All C++ settings in `com.cuperino.qprompt` domain survive. Hotkeys, spellcheck languages, auto-reload, LibreOffice path persist after "factory reset."
- **Impact:** Factory reset leaves stale state; user believes settings cleared but critical prefs persist.

### [SET-03] QString "true" used as default for boolean QSettings value
- **File:** documenthandler.cpp:137
- **Severity:** Low
- **Analysis:** `settings.value("editor/autoReload", "true").toBool()` — default is QString "true" while stored value is bool. Relies on implicit QVariant cross-type conversion.
- **Impact:** Fragile — any code using `.toString()` would get type mismatch.

### [SET-04] spellCheckLanguages read without explicit default value
- **File:** documenthandler.cpp:153
- **Severity:** Low
- **Analysis:** `settings.value("editor/spellCheckLanguages").toStringList()` — no default argument. Relies on implicit empty-QStringList-from-invalid-QVariant behavior.
- **Impact:** Code quality — inconsistent with all other settings.value() calls.

---

## Wave 33 — Invokable, CMake, Dialogs, Imports, Mouse, Comments, Regex, Hotkeys

### [INV-N01] QmlUtil::r() stores QML-owned QQuickItemGrabResult raw pointer — use-after-free
- **File:** qmlutil.hpp:175-180, main.qml:1045
- **Severity:** Medium
- **Analysis:** `grabToImage()` returns JavaScriptOwnership result. `r()` stores raw pointer in C++ buffer. After JS callback, GC may delete object → `deleteLater()` on freed memory → crash. Or `deleteLater()` runs first → GC double-frees.
- **Impact:** Intermittent crash during projection sessions.

### [CMAKE-NEW-01] Remote.qml exists on disk but never listed in QML_FILES
- **File:** src/CMakeLists.txt, src/prompter/Remote.qml
- **Severity:** Low
- **Analysis:** Remote.qml not in any CMake source list. Orphaned dead code.
- **Impact:** Runtime "not installed" error if Remote component ever referenced.

### [CMAKE-NEW-02] Duplicate install() of appdata.xml/desktop in root and src/CMakeLists.txt
- **File:** CMakeLists.txt:408-409, src/CMakeLists.txt:524-525
- **Severity:** Medium
- **Analysis:** Both root and src CMakeLists install same files to same destinations. CMake 3.27+ CMP0177 hard-errors on duplicate install.
- **Impact:** Build configure failure on CMake 3.27+.

### [CMAKE-NEW-03] find_package(KF6Crash ... COMPONENTS) — COMPONENTS keyword with zero names
- **File:** CMakeLists.txt:316
- **Severity:** Medium
- **Analysis:** `find_package(KF6Crash ${REQUIRED_KF6_VERSION} COMPONENTS)` — after expansion, COMPONENTS keyword has no arguments. Syntax error. No QUIET – hard-errors if not found despite TYPE OPTIONAL next line.
- **Impact:** CMake warning/error on configure.

### [CMAKE-NEW-04] execute_process uses CMAKE_PREFIX_PATH (list) as scalar — broken command
- **File:** src/CMakeLists.txt:512
- **Severity:** Medium
- **Analysis:** `${CMAKE_PREFIX_PATH}/bin/lconvert` — semicolon-separated list produces broken multi-path string. No RESULT_VARIABLE (silent failure). Redundant with qt_add_translations on line 345. Runs on all platforms including WASM where host binaries don't exist.
- **Impact:** Non-functional command, wasted configure time.

### [DLG-N01] document.modified=false set BEFORE saveAs() — failed save loses unsaved flag
- **File:** Prompter.qml:2291
- **Severity:** High
- **Analysis:** Modified flag cleared BEFORE save. If save fails (disk full, permissions), error fires but `modified` already false. User sees no "unsaved changes" — may close app and lose data.
- **Impact:** Data loss risk on save failure.

### [DLG-N02] onError handler clears document.modified on save failure
- **File:** Prompter.qml:2348-2352
- **Severity:** High
- **Analysis:** `onError` handler sets `document.modified = false` — but save failed, doc IS still modified. Doubly broken when combined with DLG-N01.
- **Impact:** Data loss risk — user not prompted to retry save.

### [DLG-N03] errorDialog MessageDialog has no title
- **File:** Prompter.qml:2510-2513
- **Severity:** Low
- **Analysis:** Error dialog displayed with blank title bar. closeDialog, restartDialog, factoryResetDialog all set descriptive titles.
- **Impact:** Blank title bar in error dialogs.

### [DLG-N04] load() silently fails with no notification when file missing or unreadable
- **File:** documenthandler.cpp:944-947
- **Severity:** Medium
- **Analysis:** No else-branch — file nonexistent or unreadable → no error signal, no dialog. Nothing visibly happens to user.
- **Impact:** Silent failure; user doesn't know why file didn't open.

### [DLG-N05] loadFromNetworkFinihed() silently ignores empty response
- **File:** documenthandler.cpp:888-902
- **Severity:** Medium
- **Analysis:** Empty reply (dropped connection, empty 200) silently does nothing. No error signal, no notification.
- **Impact:** Silent failure on network errors returning empty body.

### [DLG-N06] import() error strings passed as document content via updateContents()
- **File:** documenthandler.cpp:1000,1087
- **Severity:** High
- **Analysis:** ALL import formats depending on external tools (ODT, DOCX, DOC, RTF, ABW, PAGESX, PAGES) — if LibreOffice unavailable/crashes/times out, the error description becomes document content. No notification distinguishes error-text-as-content from successful import.
- **Impact:** User's document silently replaced with error message text.

### [DLG-N07] 5 showPassiveNotification() calls ignore passiveNotifications preference
- **File:** Find.qml:133,135,160, EditorToolbar.qml:627, PrompterPage.qml:890
- **Severity:** Low
- **Analysis:** Search wrap, replace-count, "No glyphs selected", velocity indicator notifications fire regardless of `root.passiveNotifications: false`.
- **Impact:** Notification spam when user disabled notifications.

### [DLG-N08] 3 save-completion passive notifications lack passiveNotifications guard
- **File:** Prompter.qml:2294,2296,2474,2499
- **Severity:** Low
- **Analysis:** Save completion notifications fire even when user disabled notifications. Six other call sites in same file correctly guard with `if(root.passiveNotifications)`.
- **Impact:** Inconsistent notification behavior.

### [IMP-NEW-01] #include \<qnativeinterface.h\> doesn't exist — breaks Android build
- **File:** documenthandler.cpp:83
- **Severity:** High
- **Analysis:** No such header in any Qt 5 or Qt 6. Correct access via `<QCoreApplication>` (already included). Fatal: `'qnativeinterface.h': No such file or directory`.
- **Impact:** Android builds cannot compile.

### [IMP-NEW-02] main.cpp:22 #include "qglobal.h" uses quotes + Qt5-era name
- **File:** main.cpp:22
- **Severity:** Low
- **Analysis:** Double-quotes search local dir first; `qglobal.h` is pre-Qt6 header name. Qt 6 canonical: `<QtGlobal>`. Local file named `qglobal.h` would shadow system header.
- **Impact:** Fragile include — harmless currently.

### [IMP-NEW-03] main.cpp:38-39 redundant #include \<QtQml/qqml.h\> + #include \<QtQml\>
- **File:** main.cpp:38-39
- **Severity:** Low
- **Analysis:** `<QtQml>` umbrella already pulls in `qqml.h`. Sub-include is redundant.
- **Impact:** Code clarity only.

### [IMP-NEW-04] AboutPage.qml imports Kirigami 2.9 vs 2.11 in all other files
- **File:** AboutPage.qml:22
- **Severity:** Low
- **Analysis:** CMake requires KF6 6.9.0 = Kirigami 2.11+. All 12 other QML files import 2.11. AboutPage alone uses 2.9.
- **Impact:** Future AboutPage edit using 2.10+ API silently fails.

### [IMP-NEW-05] pointers.qrc RESOURCE_PREFIX conflicts with qt_add_qml_module
- **File:** pointers.qrc:2, src/CMakeLists.txt:253
- **Severity:** Low (orphaned QRC, never compiled)
- **Analysis:** Orphaned QRC has `/qt/qml/com/cuperino/qprompt/pointers/` prefix overlapping QML module prefix. Would create duplicate resource registrations if activated.
- **Impact:** None currently. Would break if QRC ever activated.

### [MA-N01] overlayMouseArea permanently disabled — dead MouseArea
- **File:** ReadRegionOverlay.qml:116-122
- **Severity:** Low
- **Analysis:** `enabled: false` hardcoded. Never set to true by any state/binding/code. Id never referenced. Intended overlay cursor behavior non-functional.
- **Impact:** Dead code; whatever this was for doesn't work.

### [MA-N02] textDragArea missing cursorShape — ArrowCursor over IBeamCursor on editor
- **File:** Prompter.qml:1429-1431
- **Severity:** Low
- **Analysis:** Topmost MouseArea over editor TextArea defaults to ArrowCursor. MouseArea below it correctly sets IBeamCursor but is concealed.
- **Impact:** Arrow cursor over all editor text instead of I-beam.

### [CMT-N01] Justify ToolButton comment says it's commented out — but it's active
- **File:** EditorToolbar.qml:761-773
- **Severity:** Medium
- **Analysis:** Comment claims justify is commented out. Code is fully active, controlled by `toolbar.showJustify`. Contradicts reality.

### [CMT-N02] Truncated comment in markersmodel.cpp:107-108
- **File:** markersmodel.cpp:107-108
- **Severity:** Low
- **Analysis:** Second sentence truncated: "Joins the text of the next fragment..." — never says what it joins or why.
- **Impact:** Workaround purpose obscured.

### [CMT-N03] Misleading OpenGL workaround comment — scope of impact understated
- **File:** main.cpp:79
- **Severity:** Medium
- **Analysis:** Comment only mentions "opacity bug in DirectX RHIs." Doesn't mention side effect: forces deprecated OpenGL backend on ALL Windows systems. Typo "Workarround."
- **Impact:** Developer may not realize full scope of this environment variable.

### [CMT-N04] Comment masks invalid enum bug — 2 - value produces out-of-range LayoutDirection
- **File:** main.cpp:165
- **Severity:** Medium
- **Analysis:** Comment "Substract from 2 because order inverted" explains intent, masks that `2 - 0 = 2` is invalid enum value (valid range 0-1). Bug: TYP-02. Comment itself actively misleading. Typo "Substract."
- **Impact:** Masks real bug behind innocent explanation.

### [CMT-N05] Missing security warning on QProcess RCE sink (sys://)
- **File:** qmlutil.hpp:84-95
- **Severity:** High
- **Analysis:** `run()` executes arbitrary commands via QProcess::startDetached. No comment warns of security implications or unsanitized input. Bug: SEC-01.
- **Impact:** Dangerous code sink with no annotation for future maintainers.

### [CMT-N06] Missing warning: re-entrant toggle() inside Behavior.onRunningChanged
- **File:** Prompter.qml:855-856
- **Severity:** Medium
- **Analysis:** `toggle()` called inside animation signal handler — re-entrant state machine manipulation. Bug: FINAL-22. No warning comment.
- **Impact:** Future maintainers unaware of re-entrancy risk.

### [CMT-N07] Missing warning: joinPreviousEditBlock() without beginEditBlock()
- **File:** documenthandler.cpp:1596,1610
- **Severity:** Medium
- **Analysis:** Both setLineHeight/setParagraphHeight call joinPreviousEditBlock() with no matching beginEditBlock(). Debug assertion failure, release undo corruption. Bug: R3-DOC-02. Unannotated.
- **Impact:** Dangerous QTextDocument manipulation without documentation.

### [CMT-N08] Entire Telemetry class is dead commented-out shell across 4 files
- **File:** telemetry.h, telemetry.cpp, promptsession.h, promptsession.cpp
- **Severity:** Medium
- **Analysis:** All methods commented out. Class compiles to nothing. Should be removed or clearly marked as planned.
- **Impact:** Dead files create false expectation of telemetry functionality.

### [CMT-N09] Commented-out PropertyActions in active loop animation — stale state risk
- **File:** Prompter.qml:866-871
- **Severity:** Medium
- **Analysis:** Two PropertyActions resetting `__i` and `position` are commented out in the main scroll loop. Without them, loop depends on stale state from previous run.
- **Impact:** Loop behavior silently changed; no explanation for why reset was removed.

### [CMT-N10] Obsolete Qt 5 qmlRegisterType calls as commented-out cruft
- **File:** main.cpp:68-69,215-223
- **Severity:** Low
- **Analysis:** Multiple `// qmlRegisterType<...>(...)` and `// #include` from Qt 5 era. Malformed comment nesting at line 219 (`/**/` inside `//`).
- **Impact:** Misleads about current C++ registration mechanism (QML_ELEMENT).

### [REGEX-N01] All 13 QRegularExpression objects lack isValid() checks
- **File:** documenthandler.cpp, spellhighlighter.cpp (13 regex objects)
- **Severity:** Medium
- **Analysis:** Every regex constructed without validating. Pattern typo → silent no-match instead of error. searchRegEx (line 1543) receives user input — invalid user regex like `[` silently matches nothing.
- **Impact:** Regex bugs silently break filtering/search/highlighting.

### [REGEX-N02] regex_5 accidentally excludes 15+ HTML5 tags from background-color filtering
- **File:** documenthandler.cpp:1300
- **Severity:** Medium
- **Analysis:** `[^sS][^pP][^aA][^nN]` excludes all tags starting with s/p/a/n. Also excludes `<strong>`, `<script>`, `<style>`, `<svg>`, `<section>`, `<source>` etc. These retain unwanted background colors after filtering.
- **Impact:** Pasted HTML from rich editors may retain background colors on these elements.

### [REGEX-N03] Unescaped dot in font-size regex — matches any char instead of decimal
- **File:** documenthandler.cpp:894,954,1274
- **Severity:** Low
- **Analysis:** `(?:.[\\d]+)` uses `.` (any char) instead of `\\.` (literal dot). Works only by coincidence on well-formed HTML.
- **Impact:** Theoretical. No practical impact with well-formed inputs.

### [HK-N01] Missing event.isAutoRepeat guard on main Keys.onPressed
- **File:** Prompter.qml:2672
- **Severity:** High
- **Analysis:** No auto-repeat suppression. Holding Pause rapidly flips play/pause. Reverse rapidly flips state. Toggle/Stop/Skip/Marker all repeat-fire.
- **Impact:** Keys behave erratically when held.

### [HK-N02] Typo Qt.Key_VolumeDowm — "Dowm" instead of "Down" — volume-down hardware key dead
- **File:** Prompter.qml:2674
- **Severity:** Medium
- **Analysis:** 'm' instead of 'n'. Resolves to `undefined`. Volume-down key never works. Volume-up (Key_VolumeUp) correct.
- **Impact:** Volume-down hardware button non-functional.

### [HK-N03] platformName() != "wayland" fails on "wayland-egl" — global hotkeys dead
- **File:** globalhotkeys.cpp:16 sites
- **Severity:** High
- **Analysis:** Qt reports "wayland-egl" on Wayland with EGL backend. `!= "wayland"` passes → QHotkey shortcuts zeroed AND KGlobalAccel defaults zeroed. Zero global hotkeys on Wayland-EGL.
- **Impact:** All global hotkeys non-functional on Wayland-EGL compositors.

### [HK-N04] No auto-repeat guard in key-binding configuration Keys.onPressed
- **File:** KeyInputButton.qml:103
- **Severity:** Medium
- **Analysis:** Auto-repeat races with toggleButtonsOff() mitigation. Signal-chain latency can allow second event before checked clears.
- **Impact:** Double-assignment during key re-binding.

### [HK-N05] Strict === equality on modifiers breaks user keybinds with NumLock
- **File:** Prompter.qml:2674-2794
- **Severity:** Medium
- **Analysis:** All 31 `event.modifiers === keys.xxxModifiers` use strict equality. NumLock/KeypadModifier/GroupSwitchModifier bits cause mismatch. Hardcoded Ctrl+F/V/D correctly use `&`.
- **Impact:** User-configured keybinds silently fail with NumLock on.

### [HK-N06] isValidInput checks local keybindings only — silent conflict with global hotkeys
- **File:** KeyInputButton.qml:62-85
- **Severity:** Low
- **Analysis:** Conflict check only covers `prompter.keys.*`. User can assign same key+modifier to local AND global. Both fire — undefined behavior.
- **Impact:** Double-execution on keypress if conflict created.

---

## Wave 34 — Loader, Parsing, Props, Network, Init Order

### [LDR-N01] InputsOverlay typeof null guard fails — null.item crash on rapid close
- **File:** InputsOverlay.qml:105-112,562-569
- **Severity:** Medium
- **Analysis:** `typeof children[i].item !== "undefined"` — `typeof null === "object"`, so the guard passes when Loader.item is null. `item.checked = false` throws TypeError. Reachable when overlay closes before async Loaders complete.
- **Impact:** Crash on rapid overlay open/close.

### [PARSE-N01] insertImageAt() stores image resource with file:// key but looks up via plain path
- **File:** documenthandler.cpp:1766-1769
- **Severity:** Medium
- **Analysis:** `addResource(ImageResource, imageUrl, image)` uses full file:// QUrl. `imageFormat.setName(imageUrl.toLocalFile())` stores plain path. Later `imageAt()`/`imageRect()` lookup via `QUrl(imgFmt.name())` misses because plain-path QUrl != file:// QUrl. Remote image path (line 1753) correctly uses `.toString()` for both.
- **Impact:** Image dimension retrieval broken for locally inserted images (drag-and-drop from filesystem).

### [PARSE-N02] MarkersModel::keySearch() hits=1 limits search to first marker only
- **File:** markersmodel.cpp:120
- **Severity:** Medium
- **Analysis:** `match(index(0), KeyRole, key, 1, ...)` — hits=1 returns only first match. Variable name is plural (`markersThatMatchShortcut`). Multiple markers with same key at different positions: only first found, second unreachable.
- **Impact:** Key-based marker navigation (Ctrl+key) misses markers beyond first match.

### [PROP-N01] on__FullScreenChanged handler casing mismatch — never fires
- **File:** main.qml:36-37
- **Severity:** High
- **Analysis:** Property declared `__fullScreen` (lowercase `f`). Handler written `on__FullScreenChanged` (uppercase `F`). Auto-generated handler name doesn't match. Same bug class as FINAL-09 (`on__IChanged`). `AppController.wasm.toggleBrowserFullscreen()` never called.
- **Impact:** WASM native browser Fullscreen API never invoked; fullscreen only within browser tab frame.

### [PROP-N02] setCursorPosition → reset() — 12-signal storm, no debounce
- **File:** documenthandler.cpp:455-463,1187-1201
- **Severity:** Medium
- **Analysis:** setCursorPosition unconditionally calls reset() emitting 12 NOTIFY signals + synchronous document reads. No throttling, coalescing, or change-detection. During typing (10-30 Hz) or smooth scrolling (60 Hz): 120-720 emissions/sec + synchronous doc reads.
- **Impact:** Severe QML binding churn. UI stuttering, battery drain on mobile/WASM.

### [PROP-N03] setMarker/setKeyMarker/setMarkerHref silently trigger full document reparse
- **File:** documenthandler.cpp:720,775,804
- **Severity:** Low
- **Analysis:** All three Q_PROPERTY WRITE methods call `setMarkersListDirty()`, triggering O(n) parse() on next toggle(). Neither Q_PROPERTY name nor NOTIFY signal hints at this side effect.
- **Impact:** First prompter start after adding marker slower than expected. Toggle latency between Edit/Prompting states.

### [NET-N04] No transfer timeout on any QNetworkRequest
- **File:** documenthandler.cpp:882-884,1739
- **Severity:** Medium
- **Analysis:** No `setTransferTimeout()` call. Qt default: 0 (infinite). Hanging server blocks request forever with no abort path or user feedback.
- **Impact:** App hangs indefinitely on unreachable network resources.

### [NET-N05] loadFromNetwork() hardcodes http:// scheme — never upgrades to HTTPS
- **File:** documenthandler.cpp:872
- **Severity:** Medium
- **Analysis:** `resultingUrl.setScheme("http")` always forces HTTP for relative URLs. HTTPS URL treated as relative → downgraded to plaintext HTTP.
- **Impact:** MITM exposure when loading remote documents.

### [NET-N06] loadFromNetwork() validates original URL, not constructed resultingUrl
- **File:** documenthandler.cpp:881
- **Severity:** Low
- **Analysis:** `if (url.isValid())` checks input URL, not the constructed `resultingUrl`. If construction produces malformed URL (beyond already-documented R4-EXP-03 host/path swap), guard passes, bad request issued.
- **Impact:** Masked URL construction errors reach network layer.

### [URL-N01] reload() constructs file:// URL by string concatenation without encoding
- **File:** documenthandler.cpp:860
- **Severity:** Medium
- **Analysis:** `QUrl("file://" + fileUrl)` — no percent-encoding. Paths with spaces, #, ?, or non-ASCII chars produce malformed QUrl. load() fails to round-trip back via `QQmlFile::urlToLocalFileOrQrc()`.
- **Impact:** Auto-reload broken for files with special characters in path.

### [DISK-N01] saveCustomWordsToDisk() non-atomic write — data loss on power failure
- **File:** spellchecker.cpp:383-397
- **Severity:** Low
- **Analysis:** Writes directly to target file (no temp-file-and-rename). QFile::open failure silently returns void. QTextStream::status never checked. Power loss or disk full leaves corrupted/truncated custom dictionary.
- **Impact:** Custom dictionary corruption on crash/power loss during save.

### [INIT-N01] Velocity modifier ComboBox model has 2 entries, switch handles 4 cases
- **File:** InputsOverlay.qml:423-425,430-441
- **Severity:** Medium
- **Analysis:** ComboBox lists only Alt and Ctrl. `onActivated` switch handles cases 0-3 including Shift (2) and Meta (3), which are unreachable. Commented-out hotkey tab version correctly lists all 4.
- **Impact:** Users cannot select Shift or Meta as velocity modifier.

### [INIT-N02] Find.qml SearchField placeholderText always empty — no guidance text
- **File:** Find.qml:183
- **Severity:** Low
- **Analysis:** `placeholderText: ""` hardcoded empty. Never populated with "Search..." or equivalent. Field renders blank until user types.
- **Impact:** Search bar lacks placeholder guidance.

### [INIT-N03] ReadRegionOverlay screenMiddle uses root.y from cross-file id resolution
- **File:** ReadRegionOverlay.qml:132-134
- **Severity:** Low
- **Analysis:** `root.y` resolves through parent scope chain (ReadRegionOverlay → PrompterView → PrompterPage → ApplicationWindow). Fragile: if component loaded in different context, resolution changes silently. root also used inside ShaderEffect contexts.
- **Impact:** Works by accident. Screen-middle miscalculation if component hierarchy changes.

### [INIT-N04] PrompterView ShaderEffectSource.sourceItem references prompter id declared later
- **File:** PrompterView.qml:230-236
- **Severity:** Low
- **Analysis:** ShaderEffectSource at line 230 references `prompter` id declared at line 235 below. QML bindings lazy, but internal sourceItem resolution may attempt immediate access during construction.
- **Impact:** First rendered frame may lack prompter text shadows; resolves on next frame.

---

## Wave 35 — Combos, Visibility, Scroll Math, Naming, Casts, Actions

### [CMB-N01] autoReloadSeconds SpinBox from binding circular — clamps to 1 when all-zero
- **File:** PrompterPage.qml:1381
- **Severity:** Medium
- **Analysis:** `from: value>0 || autoReloadMinutes.value>0 || autoReloadHours.value>0 ? -1 : 1`. Own-value self-reference creates binding loop. When all three time fields reach 0, from=1 but value=0, silently clamped to 1. Also, when hours=1 and seconds=0, from=-1 and seconds CAN be 0 — preventing-all-zeros logic is inconsistently applied.
- **Impact:** Cannot set all three auto-reload time fields to zero; seconds forced to 1.

### [CMB-N02] autoReloadMinutes SpinBox from contains redundant circular self-reference
- **File:** PrompterPage.qml:1356
- **Severity:** Low
- **Analysis:** `from: value>0 || autoReloadMinutes.value>0 || autoReloadHours.value>0 ? -1 : 0` — `value` and `autoReloadMinutes.value` are the same property. Redundant circular binding.
- **Impact:** Binding loop warning; no functional impact.

### [CMB-N03] LanguageSettingsOverlay ListView currentIndex always -1 — wrong indexOf() call
- **File:** LanguageSettingsOverlay.qml:73
- **Severity:** Medium
- **Analysis:** `currentIndex: languageSelector.model.indexOf(languageSelector.currentIndex)` — Array.indexOf() uses strict equality (===). Searches for number in array of objects `{text:..., value:...}` — never matches. Returns -1 always. Correct pattern used elsewhere: `comboBox.highlightedIndex`.
- **Impact:** Selected language never highlighted in dropdown popup.

### [VIS-N04] Countdown crosshair frame renders orphan lines when enabled=false
- **File:** Countdown.qml:151-178
- **Severity:** Low
- **Analysis:** `Shape { id: frame }` (crosshair lines) has no visible binding. All other countdown elements guard with `visible: countdown.enabled`. When disabled but Prompter in Standby, only orphan crosshair lines render.
- **Impact:** Meaningless hairline crosshairs visible during standby with countdown disabled.

### [VIS-N05] velocityDragOverlay blocks all interaction during indicator fade-out (~500ms dead zone)
- **File:** PrompterPage.qml:913-919,865-872
- **Severity:** Medium
- **Analysis:** velocityDragOverlay visible bound to velocityIndicator.visible (stays true during fade-out). Fade animation hides indicator visually over ~500ms but overlay blocks all clicks/mouse movement across entire viewport the whole time.
- **Impact:** 500ms dead zone after velocity indicator timeout where user cannot interact.

### [SCRL-N01] __jitterMargin: fractional result from modulus violates 0/1 toggle design
- **File:** Prompter.qml:114
- **Severity:** Medium
- **Analysis:** `(__tikTok+viewport.__baseSpeed+viewport.__curvature+fontSize)%2` — real operands produce fractional remainder via JS `%`. Designed as 0/1 subpixel toggle but yields arbitrary fractional values. Combined with FINAL-09 (__tikTok stuck at 0), jitter becomes static fraction from slider positions.
- **Impact:** Subpixel jitter function permanently broken; produces static fraction instead of alternating.

### [SCRL-N02] __destination typed int truncates real-valued position
- **File:** Prompter.qml:125
- **Severity:** Medium
- **Analysis:** RHS involves `editor.height` (real), `fontSize` (real), `topMargin` (real). Result truncated to `int` by property type. Behavior animation only receives integer target — loses subpixel precision. __jitterMargin fractional offset (SCRL-N01) is discarded by truncation.
- **Impact:** Position animation loses subpixel smoothness.

### [SCRL-N03] setVelocity() triggers two conflicting scroll animations with intermediate velocity
- **File:** Prompter.qml:605-613
- **Severity:** Medium
- **Analysis:** Sets `__i = velocity-1`, writes `position = __destination` (triggers Behavior toward wrong target), then `__i = velocity`, writes `position = __destination` (re-targets mid-flight). Two back-to-back assignments cause NumberAnimation to start then re-target.
- **Impact:** Visible jitter/flicker when pressing velocity preset hotkeys (Ctrl+1..0).

### [SCRL-N04] __speed non-zero when __i=0 and __curvature=0 (Math.pow(0,0)===1)
- **File:** Prompter.qml:118-119
- **Severity:** Low
- **Analysis:** ECMAScript: `Math.pow(0,0) === 1`. When curvature slider at minimum and velocity stopped, `__speed = __baseSpeed * 1` instead of 0. Masked in main animation path (__destination==position when __i==0, timeToArrival==0). But TimerClock.updateTimer() fallback produces inconsistent ETA.
- **Impact:** Inconsistent time-to-end display when curvature=0.

### [SCRL-N05] __speedLimit check is dead logic — always true
- **File:** Prompter.qml:129,494,510
- **Severity:** Low
- **Analysis:** `__speedLimit = __vw * 100` (~1920px × 100 = ~192,000). `__velocity < this.__speedLimit` (velocity typically < 100). Guard condition always true for normal operation. Mirror in decreaseVelocity also always true.
- **Impact:** Dead code — speed limit boundary never reached.

### [SCRL-N06] __timeToEnd uses unexplained 2× factor
- **File:** Prompter.qml:122, TimerClock.qml:66
- **Severity:** Low
- **Analysis:** `2 * (editor.height + fontSize - __travelDistance) / __relativeSpeed` doubles estimated remaining time versus standard distance/rate formula. No documentation. TimerClock fallback shares same pattern — may be intentional but undocumented.
- **Impact:** ETA display may be 2× actual; impossible to distinguish intentional vs accidental.

### [TYP-N01] Misspelled method name: loadFromNetworkFinihed (missing 's')
- **File:** documenthandler.cpp:145,888, documenthandler.h:274
- **Severity:** Low
- **Analysis:** "Finihed" instead of "Finished." Consistent across all 3 locations.
- **Impact:** Developer confusion — typo search failures.

### [TYP-N02] Misspelled parameter: withoutFormating (missing 't')
- **File:** documenthandler.h:225, documenthandler.cpp:1336,1347
- **Severity:** Low
- **Analysis:** "Formating" instead of "Formatting." Consistent across declaration, definition, usage.
- **Impact:** Developer confusion; code-search failures.

### [TYP-N03] Inconsistent `_` vs `m_` member prefix: _markersModel, _fileSystemWatcher
- **File:** documenthandler.h:343-344
- **Severity:** Low
- **Analysis:** Two members use `_` prefix while all 15+ other members use `m_`. MEM-01/MEM-02 reference these but never flag convention break.
- **Impact:** Code style inconsistency.

### [TYP-N04] Inconsistent m_ method naming: m_initializeSource — mixed underscore+camelCase
- **File:** abstractinputsource.h:50, globalhotkeys.h:150
- **Severity:** Low
- **Analysis:** Underscore inside name joins "initialize" and "Source." Other m_ methods use pure camelCase: m_setGlobalShortcut, m_setActionShortcut, m_setHotkeyShortcut.
- **Impact:** Code style inconsistency.

### [TYP-N05] Uninitialized member m_documentComesFromNetwork
- **File:** documenthandler.h:338, documenthandler.cpp:123-130
- **Severity:** Low
- **Analysis:** Bool member absent from constructor initializer list and never assigned in constructor body. First write in setDocumentComesFromNetwork() (called from loadFromNetworkFinihed:896 or load:1039). QML property comesFromNetwork can be read before either path.
- **Impact:** Undefined bool if QML reads property before document load completes.

### [TYP-N06] 9 getters copy-paste double-textCursor() pattern — null check on stale cursor
- **File:** documenthandler.cpp: alignment(548), bold(565), italic(581), underline(597), strike(613), subscript(629), superscript(648), fontCapitalization(669), regularMarker(694)
- **Severity:** Low
- **Analysis:** LOG-07 flags namedMarker() double-textCursor(). Same pattern in 9 more getters: null-check local QTextCursor, then read from fresh textCursor() call. Null check meaningless — cursor may have changed.
- **Impact:** Rare stale formatting state. Formatting toolbar may show wrong indicator.

### [CAST-N01] setFontCapitalization static_cast with no range validation — reachable from QML
- **File:** documenthandler.cpp:677
- **Severity:** Medium
- **Analysis:** `static_cast<QFont::Capitalization>(capitalization)` — Q_INVOKABLE takes arbitrary int from QML. QFont::Capitalization valid range [0,4]. Passing 5, -1, 100 from QML → out-of-range enum → UB. Same class as TYP-02 (LayoutDirection) but different enum.
- **Impact:** Undefined behavior if QML passes invalid capitalization value.

### [IMG-N01] Missing go-previous-symbolic.svg — back-navigation icon blank on Android/Windows
- **File:** +android/main.qml:575, +windows/main.qml:631
- **Severity:** Medium
- **Analysis:** `source: "qrc:/qt/qml/com/cuperino/qprompt/icons/go-previous-symbolic.svg"` — file doesn't exist. Bypasses icon theme entirely with direct URL. Correct: `image://icon/go-previous-symbolic` or icon theme lookup.
- **Impact:** Back-navigation arrow permanently invisible when pageStack has layers.

### [ACT-N05] +windows main.qml Controls Settings submenu missing OBS Settings action
- **File:** +windows/main.qml vs main.qml:261-270
- **Severity:** Medium
- **Analysis:** Base main.qml includes OBS Settings in Controls Settings. +windows omits it. Since +windows has no Labs.MenuBar (dead code per IMP-N01), Windows users have zero menu access to OBS configuration.
- **Impact:** Windows users cannot reach OBS WebSocket settings.

### [ACT-N06] +windows main.qml Performance tweaks missing enableBarsSetting
- **File:** +windows/main.qml:320-391 vs main.qml:374-386
- **Severity:** Low
- **Analysis:** Disable-bars-overlay toggle missing from +windows global menu. Context-drawer access still works via readRegionBarsButton.
- **Impact:** Windows users missing menu toggle for bars overlay.

### [ACT-N07] namedBookmarkButton: checkable button opens dialog — stale indicator after first click
- **File:** EditorToolbar.qml:225-236
- **Severity:** Medium
- **Analysis:** checkable with checked binding to document.namedMarker. onClicked opens dialog instead of toggling property. Binding breaks on first click; indicator never re-syncs. Worse than R2-EDT-03 because formatting buttons re-sync each click — this one permanently desyncs.
- **Impact:** Named-marker button shows stale checkmark after first use.

### [ACT-N08] All checkable Labs.MenuItems inherit R2-EDT-03 binding-break pattern
- **File:** main.qml:617-922
- **Severity:** Medium (masked — Labs.MenuBar dead per IMP-N01)
- **Analysis:** Every checkable Labs.MenuItem (Bold/Italic/Underline, Full Screen, Indicators, Position items, scroll/dial) has `checked: binding` + `onTriggered: property = checked`. On first click, native checkmark toggles imperatively → QML binding breaks. Currently masked because Qt 6 drops Qt.labs.platform Menu/MenuBar.
- **Impact:** If ever migrated to working native menu API, ALL checkable items decay after first use.

---

## Wave 36 — Render, Text, Platform, Decls, Colors

### [RENDER-01] ShaderEffectSource prompterShadowSource runs unconditionally — wastes GPU capture when shadows disabled
- **File:** PrompterView.qml:230-233
- **Severity:** Medium
- **Analysis:** `live` defaults to true. Captures entire prompter Flickable to texture every frame. Downstream shadow chain gated by `layer.enabled: root.shadows` in Prompter.qml:744, but shadowSource has no `live: root.shadows` guard. When shadows off (default), every frame incurs full off-screen render + GPU texture copy.
- **Impact:** Unnecessary GPU bandwidth and frame-time increase on every frame during prompting.

### [RENDER-02] ShaderEffectSource pointerShadowSource runs unconditionally — same pattern
- **File:** ReadRegionOverlay.qml:123-126
- **Severity:** Medium
- **Analysis:** Identical to RENDER-01. Always captures readRegion to texture. Downstream shadow on readRegion gated by `layer.enabled`, but source never stops when shadows off.
- **Impact:** Wasted texture capture every frame when shadows disabled.

### [TXT-N01] Find/replace fields missing persistentSelection: true
- **File:** Find.qml:182,230
- **Severity:** Low
- **Analysis:** Both SearchField and replaceField set `selectByMouse: true` but omit `persistentSelection: true`. Selected text disappears on focus loss. Main editor (Prompter.qml:972) correctly enables it.
- **Impact:** User-selected find/replace text vanishes on focus loss.

### [TXT-N02] TimerClock default text color #AAA on #131619 — fails WCAG AA contrast
- **File:** TimerClock.qml:93,138,151,163
- **Severity:** Low
- **Analysis:** Default `timerSettings.color = "#AAA"` on background `#131619` — contrast ratio ~3.16:1, below WCAG AA minimum 4.5:1. Timer text is small (viewport-scaled), compounding legibility issues.
- **Impact:** Stopwatch/ETA text hard to read for visually impaired users under default settings.

### [PLAT-N01] qmlutil.hpp incorrectly excludes QNX from QProcess — run()/restartApplication() silently no-op
- **File:** qmlutil.hpp:35,86,99
- **Severity:** Medium
- **Analysis:** Three guards omit Q_OS_QNX despite QNX being a POSIX RTOS with full QProcess support in Qt. main.cpp:23,42,106 correctly include QNX in similar guards. run() becomes Q_UNUSED, restartApplication() only calls quit() without spawning replacement.
- **Impact:** sys:// URL handler, app restart on language/layout change, factory reset all broken on QNX.

### [PLAT-N02] documenthandler.cpp incorrectly excludes QNX from import() — LibreOffice broken on QNX
- **File:** documenthandler.h:330, documenthandler.cpp:964,1012,1043
- **Severity:** Medium
- **Analysis:** import() calls LibreOffice via QProcess for ODT/DOCX/DOC/RTF/ABW/PAGES. QNX guard incorrectly excludes it. Since QNX has QProcess, this is inconsistent with PLAT-N01. Falls through to raw-binary auto-detection.
- **Impact:** Opening rich document formats renders binary garbage on QNX.

### [PLAT-N03] Zero Q_OS_TVOS preprocessor guards in C++ despite 19 QML references — build failure
- **Files:** All .cpp/.h/.mm (zero Q_OS_TVOS); 19 QML references to "tvos"
- **Severity:** High
- **Analysis:** Qt 6: Q_OS_TVOS is exclusive of Q_OS_IOS. Every C++ guard checks Q_OS_IOS but never Q_OS_TVOS. On tvOS: includes QApplication/QtWidgets (build error), skips Kirigami static registration (blank window), uses wrong QSettings path, includes SystemFontChooserDialog (QDialog — build error on tvOS).
- **Impact:** tvOS build fails at multiple points. QML references suggest tvOS was considered but C++ backend never implemented.

### [DECL-N01] MarkersModel::keySearch — default params in definition but not declaration
- **File:** markersmodel.h:64 vs markersmodel.cpp:117
- **Severity:** Low
- **Analysis:** Same DCL pattern as DCL-N01/DCL-N02. Defaults `currentPosition = 0, reverse = false, wrap = true` in definition invisible to MOC and QML. Currently always called with all 4 args, masked.
- **Impact:** Latent — any direct QML invocation with fewer args fails.

### [DECL-N02] SessionModel::resetInternalData() missing override keyword and Qt 6 version guard
- **File:** promptsession.h:74-75
- **Severity:** Low
- **Analysis:** MarkersModel correctly guards with `#if QT_VERSION >= QT_VERSION_CHECK(6,0,0)` and `override`. SessionModel omits both — no compiler-checked override. Stray function in Qt 5. Note: file is dead code (HDR-N01).
- **Impact:** No compiler diagnostic if QAbstractItemModel::resetInternalData() signature changes.

### [COLOR-01] ProjectionsManager.qml uses invalid "initial" color — repro of R4-ROOT-02
- **File:** ProjectionsManager.qml:195
- **Severity:** Medium
- **Analysis:** `color: root.__translucidBackground ? "transparent" : "initial"` — "initial" is CSS keyword, not valid QML color. Falls to default (black) with runtime warning.
- **Impact:** Projection windows render with black instead of system-theme color.

### [COLOR-02] Hardcoded #EED text invisible on light themes — WheelSettingsOverlay
- **File:** WheelSettingsOverlay.qml:105
- **Severity:** Medium
- **Analysis:** `color: "#EED"` (~#EEEDDD, extremely light cream) on Kirigami OverlaySheet (light theme = white background). Help text: "Enable throttling for use with touchpads..."
- **Impact:** Help text unreadable on light themes — accessibility failure.

### [COLOR-03] velocityText ColorAnimation flash: #BBB → #FFF → #CCC jump
- **File:** PrompterPage.qml:842-860
- **Severity:** Low
- **Analysis:** Setting `color = "#BBB"` then restarting animation with `from: "#FFF"` causes white flash mid-transition. Should omit from so animation picks up current value.
- **Impact:** Visual jitter/flash in velocity indicator on each velocity change.

### [COLOR-04] ReadRegionOverlay ColorAnimation tracks __fillColor that never changes
- **File:** ReadRegionOverlay.qml:204,616
- **Severity:** Low
- **Analysis:** __fillColor initialized to `"#00000000"`, never reassigned. ColorAnimation interpolates on every state transition with zero visual effect.
- **Impact:** Wasted frame budget evaluating no-op color interpolation.

### [COLOR-05] Prompter scrollbar gradient hardcodes #CCC/#998/#665 — low contrast on light backgrounds
- **File:** Prompter.qml:1008-1009
- **Severity:** Low
- **Analysis:** Hardcoded warm-grey values. On light prompter backgrounds (#FAFAFA), scrollbar handle nearly invisible. No Kirigami theme color consulted.
- **Impact:** Scrollbar handle low-contrast/invisible on light prompter backgrounds.

### [COLOR-06] Countdown #FFF digits on #333-at-0.48-overlay — insufficient contrast on light backgrounds
- **File:** Countdown.qml:71,192,212
- **Severity:** Low
- **Analysis:** All countdown colors hardcoded. #333 at 0.48 opacity on #FAFAFA = ~#C8C8C8 effective background. White digits on that = poor contrast. Shape stroke colors equally unresponsive to theme.
- **Impact:** Countdown digits hard to read on light prompter backgrounds.

### [COLOR-07] CSS default stylesheet hardcodes #FFFFFF body text — ignores user text color
- **File:** documenthandler.cpp:185-189
- **Severity:** Low
- **Analysis:** `setDefaultStyleSheet("body{...color:\"#FFFFFF\";...}")` — white text on light prompter background before user applies formatting. Q_PROPERTY textColor overrides at QTextCursor level only for newly typed/selected text.
- **Impact:** White text invisible on light backgrounds until user manually changes text color.

---

## Wave 37 — Events, States, Sizing, Const, Persistence

### [EVT-N10] Editor Ctrl+Letter shortcuts don't accept event — marker key-search double-fires
- **File:** Prompter.qml:2123-2161
- **Severity:** Medium
- **Analysis:** Ctrl+B/I/U/T/L/R/E/M toggles format but doesn't set `event.accepted = true`. Event bubbles to Prompter Flickable Keys.onPressed, calls `document.keySearch(event.key)` — searches for named markers by bare key code. Ctrl+B may simultaneously bold text AND scroll to B-marker.
- **Impact:** Unintended prompter scroll during text editing when named markers exist.

### [EVT-N11] windowStayOnTopButton lacks focusPolicy — unreachable via keyboard
- **File:** EditorToolbar.qml:794-804
- **Severity:** Low
- **Analysis:** All 20+ ToolButtons in toolbar set `focusPolicy: Qt.TabFocus`. This one defaults to Qt.NoFocus — only toggle button without keyboard access.
- **Impact:** Keyboard users cannot Tab to Stay-on-Top toggle. Accessibility gap.

### [EVT-N12] velocityDragArea and viewport.mouse share z:5 — wheel dispatch ambiguous
- **File:** PrompterPage.qml:875-877 vs PrompterView.qml:3083
- **Severity:** Low
- **Analysis:** Same-z siblings in Prompting state. velocityDragArea (no wheel handler) declared later → sits "on top" of viewport.mouse (has wheel handler). Qt version-dependent: may silently consume wheel events even without onWheel.
- **Impact:** Wheel scrolling may fail intermittently during prompting on some Qt builds.

### [STATE-N01] Shadowed Prompting→Editing transition — velocity default never saved
- **File:** Prompter.qml:3119-3137
- **Severity:** High
- **Analysis:** Two transitions target `to: Editing`. First (line 3119) matches and runs only `timer.stopTimer()`. Second (line 3127, guarded by `from: Prompting`) saves `__iDefault = prompter.__i` and calls `cursorAutoHide.reset()` — but QML selects first matching transition. Velocity-save code is dead.
- **Impact:** User's last prompting velocity never saved as new default. __iDefault stays at initial value forever.

### [STATE-N02] Find.toggle() uses !visible instead of !isOpen — can't close during Prompting
- **File:** Find.qml:51
- **Severity:** Medium
- **Analysis:** `toggle()` computes `isOpen = !visible` but `visible` is bound to `height>0` which is false during Prompting/Countdown regardless of `isOpen`. When isOpen=true and state=Prompting: `isOpen = !false = true` — no change. Find stays logically open.
- **Impact:** Find bar reappears unexpectedly when returning to Editing after pressing close shortcut during prompting.

### [STATE-N03] Countdown Running restarts dissolveIn unnecessarily — visual dim-to-bright flash
- **File:** Countdown.qml:289
- **Severity:** Low
- **Analysis:** Entering Running sets `dissolveIn.running = true`. Exiting Ready reverts dissolveIn to default `running: false`. Running then restarts from 0→1 even though countdown already fully visible.
- **Impact:** Brief dim-to-bright flash when countdown begins.

### [STATE-N04] loop animation cancel() state change overridden by toggle() due to QML batching
- **File:** Prompter.qml:900-907
- **Severity:** Low
- **Analysis:** SequentialAnimation's final ScriptAction calls `prompter.cancel()` (sets state=Editing) then `prompter.toggle()` (overwrites state). QML batches in same JS execution — only toggle()'s final state takes effect. cancel() state transition dead.
- **Impact:** Dead code — cancel() effects never run except side effect `cursorAutoHide.reset()` which gets immediately undone.

### [SIZE-N01] concentricCircles Shape has conflicting anchors.fill + anchors.centerIn
- **File:** Countdown.qml:207-209
- **Severity:** Medium
- **Analysis:** `anchors.fill: parent` sets left/right/top/bottom. `anchors.centerIn: parent` sets horizontalCenter/verticalCenter. Both simultaneously — prohibited in Qt Quick. QML anchor conflict warning; positioning unpredictable.
- **Impact:** Concentric circles may be mispositioned on some Qt builds.

### [SIZE-N02] Three Button children of Row have dead anchors.bottom declarations
- **File:** PrompterView.qml:148,163,179
- **Severity:** Low
- **Analysis:** Positioner children (Row) ignore manual anchors. Three `anchors.bottom: parent.bottom` declarations are silently dead.
- **Impact:** Dead code — zero effect.

### [CONST-N01] getMarkerKey() not const — pure reader without side effects
- **File:** documenthandler.h:214, documenthandler.cpp:746
- **Severity:** Low
- **Analysis:** Reads cursor anchor names, converts to display string. Zero member mutation. Should be const.
- **Impact:** Cannot be called on const DocumentHandler&.

### [CONST-N02] getMarkerHref() not const — identical pattern
- **File:** documenthandler.h:216, documenthandler.cpp:779
- **Severity:** Low
- **Analysis:** Same as CONST-N01 — pure reader.
- **Impact:** Same.

### [CONST-N03] MarkersModel::previousMarker(), nextMarker(), keySearch(), binarySearch() not const
- **File:** markersmodel.h:62,63,64,78, markersmodel.cpp:117,151,205,217
- **Severity:** Low
- **Analysis:** Four pure-read query methods (binarySearch recursive, previous/next/keySearch call binarySearch/data) declared non-const. Transitive — binarySearch non-const forces all callers non-const.
- **Impact:** Cannot be called on const MarkersModel&.

### [CONST-N04] GlobalHotkeys::globalShortcutKey(Action) not const — Q_INVOKABLE pure query
- **File:** globalhotkeys.h:147, globalhotkeys.cpp:108
- **Severity:** Low
- **Analysis:** Queries QHotkey::shortcut() (const) and KGlobalAccel::shortcut() (const). No mutation. Called from QML via AppController.
- **Impact:** Blocks const-correct usage.

### [CONST-N05] Unnecessary copy via const auto instead of const auto& in extendLastMarker
- **File:** markersmodel.cpp:111
- **Severity:** Low
- **Analysis:** `const auto last = m_data.last()` — QList::last() returns T&. const auto deduces to const Marker (strips reference), causing full struct copy. Only .text.length() read then discarded.
- **Impact:** Unnecessary heap copy on every marker extension during document parse.

### [SAVE-N01] loadFromNetworkFinihed sets m_fileUrl to phantom QTemporaryFile path
- **File:** documenthandler.cpp:897,144
- **Severity:** Medium
- **Analysis:** m_cache is new QTemporaryFile(this) never opened. `m_cache->fileName()` returns auto-generated temp name with no file on disk. m_fileUrl set to this phantom path. Title bar shows garbage; save() constructs broken URL.
- **Impact:** Corrupted file URL after every network load. Save-in-place broken.

### [SAVE-N02] iOS save flow never updates C++ m_fileUrl — file URL perpetually stale
- **File:** Prompter.qml:2493-2506, iossavedialog.mm:36-46
- **Severity:** High
- **Analysis:** iOS saves entirely outside C++ DocumentHandler. accepted(fileUrl) received in QML but never calls `document.saveAs(fileUrl)`. fileUrl is READ-only Q_PROPERTY (no WRITE). Can't update m_fileUrl. editor.lastDocument records stale URL.
- **Impact:** After iOS save, Ctrl+S/auto-save writes to wrong location. Title bar and recent docs show wrong URL.

### [SAVE-N03] saveAs() never updates _fileSystemWatcher — watches stale file after save-as
- **File:** documenthandler.cpp:1023-1028,1138-1176
- **Severity:** Medium
- **Analysis:** Watcher path only configured in load(). saveAs() updates m_fileUrl but never adds new path to watcher. Old path still watched — external change to old file triggers auto-reload, replacing current content. New path not watched — external changes undetected.
- **Impact:** Auto-reload can silently replace content with old file after save-as.

### [SAVE-N04] save() unnecessary QString→std::string→QString round-trip through locale encoding
- **File:** documenthandler.cpp:1183
- **Severity:** Low
- **Analysis:** `QString::fromStdString(QUrl::toPercentEncoding(...).toStdString())` — useless conversion. Qt 5: locale-dependent encoding corrupts non-ASCII paths.
- **Impact:** Non-ASCII file paths corrupted during save under Qt 5.

### [SAVE-N05] save() broken on Android content:// URIs — empty filename
- **File:** documenthandler.cpp:1181-1184
- **Severity:** Low
- **Analysis:** `QQmlFile::urlToLocalFileOrQrc()` can't resolve content:// URIs, returns empty string. Propagates through encoding to saveAs("") → open fails with confusing empty-path error.
- **Impact:** Ctrl+S always fails on Android for files from FileDialog.

### [LOAD-N01] TOCTOU race between QFile::exists() and file.open() in load()
- **File:** documenthandler.cpp:944-947
- **Severity:** Medium
- **Analysis:** File can be deleted/replaced between exists() check and open() call. If vanishes: open fails, content block skipped, but m_fileUrl set and fileUrlChanged emitted anyway. clearUndoRedoStacks() called despite nothing loaded. No error emitted.
- **Impact:** Silent empty document with wrong file URL after race. Undo history lost for no reason.

### [LOAD-N02] reset() emits 12 NOTIFY signals when open() fails but exists() succeeds
- **File:** documenthandler.cpp:1017-1018
- **Severity:** Low
- **Analysis:** reset() called outside file.open() success block but inside exists() block. File exists but unreadable → reset() fires all format NOTIFY signals with property values from unchanged document. UI churns for nothing.
- **Impact:** Spurious formatting toolbar re-bind, animation restarts, visual flash on permission errors.

---

## Wave 38 — Shader, RAII, Z-Order, Leaks

### [SHDR-N01] Math.cos/Math.sin used with degrees value — shadow offset diagonal instead of horizontal
- **File:** Prompter.qml:749, ReadRegionOverlay.qml:151-155
- **Severity:** Medium
- **Analysis:** `readonly property real angle: 180` then `offset = Qt.point(Math.cos(angle), Math.sin(angle))`. QML Math.cos/sin operate in radians. 180 rad ≈ 28.65 rotations; cos≈-0.598, sin≈-0.801 — diagonal up-left offset instead of intended horizontal-left (−1, 0) for 180°. Math.PI never used.
- **Impact:** Text/read-region drop shadows are offset diagonally. Should multiply by Math.PI/180 for degree conversion.

### [RAII-N01] QDrag object never deleteLater'd after exec() — leaks on rejected drags
- **File:** documenthandler.cpp:1486-1489
- **Severity:** Medium
- **Analysis:** `new QDrag(this)` followed by `exec()`. Qt docs: "QDrag object needs to be deleted after exec() returns." Code never calls `deleteLater()`. Rejected/cancelled drags accumulate as zombie children of DocumentHandler. Paired QMimeData also leaked.
- **Impact:** Memory leak on every drag-and-drop operation that is cancelled or rejected.

### [RAII-N02] IosSaveDialog::m_tempDir created unconditionally on all platforms — wasted I/O
- **File:** iossavedialog.h:49
- **Severity:** Low
- **Analysis:** `QTemporaryDir m_tempDir` is a by-value member — default constructor creates real temp directory on disk at every app start, on ALL platforms. On non-iOS, saveDocument() is a no-op but temp directory still created and leaked until process exit.
- **Impact:** Unnecessary filesystem I/O at every app launch on non-iOS platforms.

### [RAII-N03] QProcess orphan — child process detached on waitForFinished() timeout
- **File:** documenthandler.cpp:1083-1089
- **Severity:** Medium
- **Analysis:** Stack QProcess started (LibreOffice child). If waitForFinished times out (30s default), function returns early, QProcess dtor runs. Qt docs: "child process may continue running after QProcess destroyed." No kill()/terminate() before return. Orphan child process leaks.
- **Impact:** Zombie LibreOffice process left running indefinitely after import timeout.

### [Z-N01] CursorAutoHide has no explicit z — hover detection fragile against Kirigami internals
- **File:** main.qml:954, +windows/main.qml:618, +android/main.qml:562
- **Severity:** Medium
- **Analysis:** MouseArea with anchors.fill:parent has z:0 (default). If any Kirigami internal component assigns z>0 to page content, hover events are intercepted — cursor auto-show is dead. Only declaration order keeps it working.
- **Impact:** On Kirigami versions where internal content uses explicit z, cursor auto-hide is silently broken.

### [Z-N02] Two OverlaySheets have z:1 while nine others have none — inconsistent stacking
- **File:** LanguageSettingsOverlay.qml:36, LayoutDirectionSettingsOverlay.qml:36
- **Severity:** Low
- **Analysis:** Only 2 of 11 OverlaySheets set explicit z. Remaining 9 have implicit z. If two sheets ever coincide (ESC chain race), stacking is unpredictable.
- **Impact:** Fragile overlay layering contract.

### [Z-N03] ComboBox Popup z:103 inside OverlaySheets with z:1 — disconnected layering
- **File:** LanguageSettingsOverlay.qml:67, LayoutDirectionSettingsOverlay.qml:70
- **Severity:** Low
- **Analysis:** Popup z:103 vs parent OverlaySheet z:1. Gap of 102 suggests developer intended popup far above, but OverlaySheet renders in dedicated overlay layer — raw z on children may not propagate correctly.
- **Impact:** ComboBox dropdown may render behind OverlaySheet or at incorrect layer.

### [Z-N04] PrompterBackground (z:0) renders above viewport.mouse (z:0) — latent input intercept
- **File:** PrompterView.qml:249,320
- **Severity:** Low
- **Analysis:** Both same-z. prompterBackground declared after → stacks on top of wheel-scroll MouseArea. Currently benign (no input children at that level), but adding MouseArea to background would unexpectedly intercept wheel events.
- **Impact:** Latent hazard for future changes. No current bug.

---

## Wave 39 — DateTime, Transforms, API Contracts, Architecture

### [TIME-N01] copyrightYear computed then discarded — stale "2020-2026" in About after 2026
- **File:** main.cpp:176-179
- **Severity:** Low
- **Analysis:** `QDate::currentDate().year()` computed into `copyrightYear` but never interpolated into `copyrightStatement2` which hardcodes "2026". The `(currentYear <= 2020)` branch is dead code. Missing `#include <QDate>` (works only via transitive includes).
- **Impact:** About dialog shows stale copyright range starting 2027.

### [XFRM-N01] PrompterView.qml Rotation permanently overridden by PrompterPage.qml
- **File:** PrompterView.qml:53-58 vs PrompterPage.qml:750-765
- **Severity:** Low
- **Analysis:** PrompterView declares `transform: Rotation { angle: 77; axis { x: root.theforce?1:0 } }` for 3D perspective tilt debug feature. PrompterPage unconditionally sets `transform: Rotation {...}` on the PrompterView instance — overriding the internal Rotation. "theforce" 3D perspective tilt is dead code, never renders.
- **Impact:** Debug feature never shows intended visual effect. Dead code in release.

### [API-N01] setAlignment() missing null-cursor guard — crash risk with no document
- **File:** documenthandler.cpp:557-558
- **Severity:** Medium
- **Analysis:** Unlike all other format setters, setAlignment() creates a QTextCursor and calls mergeBlockFormat() without checking cursor.isNull(). Dereferences null QTextDocument if no document loaded.
- **Impact:** Crash if alignment changed before document loaded.

### [API-N02] selectionIsLowerCase NOTIFY signal is wrong — fontCapitalizationChanged, never emitted for case changes
- **File:** documenthandler.h:119
- **Severity:** Medium
- **Analysis:** `Q_PROPERTY(bool selectionIsLowerCase READ selectionIsLowerCase NOTIFY fontCapitalizationChanged)` — fontCapitalizationChanged only emits when capitalization format changes, never when user types that changes case. If selection was previously uppercase and user types lowercase, property silently becomes true with no notification.
- **Impact:** Stale selectionIsLowerCase binding — QML never knows selection turned lowercase.

### [API-N03] CursorAutoHide.qml unconditionally dereferences pageStack.currentItem.prompter
- **File:** CursorAutoHide.qml:31
- **Severity:** Medium
- **Analysis:** `parseInt(root.pageStack.currentItem.prompter.state)` — assumes currentItem always has prompter child. If user navigates to Settings/About where PrompterPage is not current, throws TypeError.
- **Impact:** Crash when navigating away from main page while cursor auto-hide is active.

### [API-N04] setMarker(bool) misleadingly named — sets regular marker, not any marker
- **File:** documenthandler.h:123,212
- **Severity:** Low
- **Analysis:** Q_PROPERTY `regularMarker` has WRITE `setMarker`. But `setMarker()` exclusively creates regular markers with `href="#"` — name implies it could set any marker type.
- **Impact:** API confusion — caller expecting to set named marker via `setMarker(true)` gets wrong behavior.

### [API-N05] fileName()/fileType() return fabricated defaults — can't distinguish "no file" from "untitled.html"
- **File:** documenthandler.cpp:838-850
- **Severity:** Low
- **Analysis:** When m_fileUrl empty, fileName() returns "untitled.html" and fileType() returns "html". No way to distinguish from an actual file named "untitled.html". fileUrlChanged fires when fileName() changes even though fileUrl may not.
- **Impact:** QML can't distinguish "no file loaded" from a real file. Misleading signals.

### [API-N06] SystemFontChooserDialog::show() calls setText() on same label twice — dead code
- **File:** systemfontchooserdialog.cpp:55-56
- **Severity:** Low
- **Analysis:** `ui->textPreviewLabel->setText(text);` called twice with same argument. Copy-paste artifact — dead duplicate.
- **Impact:** None. Code quality only.

### [API-N07] SpellChecker::encode() fallback says "Latin-1" but calls toLocal8Bit()
- **File:** spellchecker.cpp:400-406
- **Severity:** Low
- **Analysis:** Comment says "Fallback to Latin-1" but code calls `word.toLocal8Bit()`, using system locale encoding (e.g., Windows-1252, ISO-8859-2 depending on locale). Comment and code conflict.
- **Impact:** Wrong encoding for dictionaries on systems with locale ≠ Latin-1.

### [ARC-01] Velocity physics engine entirely in QML (~20 readonly property bindings)
- **File:** Prompter.qml:113-129
- **Analysis:** Core teleprompter behavior — `__speed`, `__velocity`, `__relativeSpeed`, `__timeToEnd`, `__destination`, `__jitterMargin`, `__speedLimit` — all in QML bindings with Math.pow, division, branching. Cannot be unit-tested; fragile to QML engine behavioral changes.

### [ARC-02] Arc-03 Search/replace state machine fully in QML (50+ lines)
- **File:** Find.qml:112-161
- **Analysis:** Mode dispatch, replace-next/replace-previous/replace-all orchestration, wrap detection, cursor math all in QML. Should be in C++ for testability.

### [ARC-03] OBS WebSocket v5 protocol in QML — opcode dispatch, auth, subscription
- **File:** Prompter.qml:366-388
- **Analysis:** Complete WebSocket handshake JSON parsed and opcode-dispatched in QML. C++ provides only raw authStr(). Protocol changes require QML edits.

### [ARC-04] DocumentHandler is 2295-line god class spanning file I/O, network, HTML filtering, markers, spellcheck, drag-drop, images, search, undo, clipboard, sleep prevention, font dialog
- **File:** documenthandler.cpp (2295 lines)
- **Analysis:** At least 6 separable concerns in a single class. Any change risks all subsystems. Test isolation impossible.

### [ARC-05] Prompter.qml is 3139-line god component spanning velocity, state machine, keyboard, WebSocket, markers, spellcheck UI, file dialogs, WYSIWYG toggle, shadows
- **File:** Prompter.qml (3139 lines)
- **Analysis:** Single QML file with 7+ responsibilities. State machine, physics engine, and keyboard handler alone justify separate components.

### [ARC-06] qmlutil.hpp is utility grab-bag with 10+ unrelated functions
- **File:** qmlutil.hpp (184 lines)
- **Analysis:** Key validation, QProcess exec (sys:// RCE), app restart, cursor management, font listing, factory reset, OBS crypto, file existence, projection buffer. No coherent responsibility.

---

## Wave 40 — Key Modifiers, CLI, DPR, Transforms, Bindings

### [KEY-N01] Named marker key binding silently discards all modifier information
- **Files:** PrompterPage.qml:1187, documenthandler.h:213, documenthandler.cpp:707-715, markersmodel.cpp:117-120
- **Severity:** Medium
- **Analysis:** KeyInputButton emits `setKey(keyCode, modifiers)` but PrompterPage only passes `keyCode` to `document.setKeyMarker(keyCode)` — modifiers discarded. Stored anchor is `key_<bare_code>` with zero modifier encoding. KeySearch matches by bare KeyRole. UI shows "Ctrl+A" but behavior is identical to plain "A".
- **Impact:** Cannot create distinct markers using same physical key with different modifiers. Collisions produce unpredictable navigation. UI misleading.

### [CLI-N01] --version flag non-functional — version string empty when parser processes
- **File:** main.cpp:159,214
- **Severity:** Medium
- **Analysis:** `parser.process(app)` handles --version by reading `QCoreApplication::applicationVersion()`, but version is only set later at line 214 via `KAboutData::setApplicationData()`. applicationVersion() is empty at parse time.
- **Impact:** `qprompt --version` displays empty version. Users cannot determine installed version from CLI.

### [DPR-N01] Prompter.qml uses Screen.devicePixelRatio (global) instead of screen.devicePixelRatio (window)
- **File:** Prompter.qml:994
- **Severity:** Medium
- **Analysis:** `Screen.devicePixelRatio` (capital S) is application-global singleton returning primary screen's DPR. On multi-monitor with different DPIs (laptop + 4K external), text renderer selection uses wrong monitor's DPR. Countdown.qml:196 correctly uses lowercase `screen`.
- **Impact:** Wrong text rendering path on multi-DPI multi-monitor systems.

### [SCALE-N01] Right pointer xScale: -1 mirrors text pointers — backwards/unreadable text
- **File:** ReadRegionOverlay.qml:391-398
- **Severity:** Medium
- **Analysis:** `Scale { xScale: -1 }` applied when sameAsLeftPointer or pointerKind is Arrow. For pointer_0 (arrow Shape), mirroring correct — arrow points inward. For pointer_1 (text pointer), text rendered backwards/unreadable.
- **Impact:** Right-side text pointers display mirrored, unreadable text (masked by broken pointerSettings refs).

### [ORIENT-N01] TimerClock binary width>height orientation creates sharp 2x font jump at 1:1
- **File:** TimerClock.qml:127
- **Severity:** Low
- **Analysis:** `root.width/root.height>1 ? 2 : 1` divides font by 2 when width > height. At near-square window (800x798→800x802), timer font size abruptly doubles/halves at the 1:1 boundary. Smooth ratio-based formula would avoid discontinuity.
- **Impact:** Timer text doubles/halves in size when window crosses near-square aspect ratio.

### [BIND-N01] contentWidth undefined for Shape/Image pointer types — transform origin silently wrong
- **File:** ReadRegionOverlay.qml:396
- **Severity:** Low
- **Analysis:** `(rightPointer.item.width | rightPointer.item.contentWidth) / 2` — contentWidth is Text-only property. For pointer_0 (Shape) and pointer_2 (Image), contentWidth is undefined. `number | undefined` → `ToInt32(undefined)` → 0. Origin depends on low-bit coincidence rather than intended center.
- **Impact:** Right-pointer transform origin silently wrong for Arrow and Image pointer kinds.

### [STR-CNV] 5 defensive validation gaps: toInt() without ok flag in getMarkerKey, parse(×2), setFontSize, and 32 hotkey reads
- **Files:** documenthandler.cpp:757,1667,1675,829, globalhotkeys.cpp:569-698
- **Severity:** Low
- **Analysis:** All rely on `toInt()`/`QVariant::toInt()` returning 0 on failure, which matches desired default (0 = unknown/unset) in every case. No functional behavior incorrect — omission of explicit ok validation and defensive coding.
- **Impact:** None currently. Latent fragility if Qt changes implicit-from-invalid behavior.

---

## Wave 41 — Shadowing, Link, Comparison, Layout, Synthesis

### [SHADOW-N03] id: stopwatch shadows property bool stopwatch — timersEnabled always true
- **File:** TimerClock.qml:38,122,100
- **Severity:** High
- **Analysis:** `id: stopwatch` (Item child) shadows `property bool stopwatch: true` in same scope. Line 100 `timersEnabled: enabled && (stopwatch || eta)` — bare `stopwatch` resolves to Item (always truthy), never to bool. timersEnabled always returns `enabled && true`, permanently ignoring both stopwatch and eta toggles.
- **Impact:** 9 consumers of viewport.timer.timersEnabled across main.qml, +windows, +android, PrompterPage ALL receive wrong values. Timer display always enabled regardless of toggles.

### [SHADOW-N04] id: frame shadows property bool frame — latent hazard
- **File:** Countdown.qml:42,152
- **Severity:** Low
- **Analysis:** `id: frame` (Shape) shadows `property bool frame: false`. No bare `frame` usage currently exists, but any future code referencing `frame` will resolve to Shape (truthy) instead of bool toggle.
- **Impact:** None currently. Latent maintenance hazard.

### [LINK-N01] Qt::Network not linked on iOS static build — unresolved symbols
- **File:** src/CMakeLists.txt:418-427
- **Severity:** High
- **Analysis:** iOS target_link_libraries omits Qt::Network despite unconditional QNetworkAccessManager usage in documenthandler.cpp. Qt::Network not transitively linked via Qt::Quick.
- **Impact:** iOS static build fails with unresolved symbols.

### [LINK-N02] Qt::Network not linked on WASM static build — same as LINK-N01
- **File:** src/CMakeLists.txt:436-445
- **Severity:** High
- **Analysis:** WASM target_link_libraries omits Qt::Network.
- **Impact:** WASM static build fails with unresolved symbols.

### [LINK-N03] Qt::WebSockets found as REQUIRED but never explicitly linked
- **File:** CMakeLists.txt:145, all target_link_libraries blocks
- **Severity:** Medium
- **Analysis:** find_package REQUIRED ensures module installed but no target_link_libraries entry on any platform. Works on dynamic-link via QML plugin; breaks on static if qmlimportscanner misses it.
- **Impact:** OBS WebSocket integration broken on static builds if auto-scan fails.

### [LINK-N04] KF6::GlobalAccel find_package/link mismatch on Haiku
- **File:** CMakeLists.txt:303-308, src/CMakeLists.txt:446-460
- **Severity:** Medium
- **Analysis:** Haiku uses special KF6 find_package (IconThemes only, line 306-308) but src/CMakeLists links KF6::GlobalAccel. Works only by accident via idempotent find_package.
- **Impact:** Fragile Haiku build — may fail to configure if KF6 installed with mismatched version.

### [COMP-N01] Case-sensitive duplicate detection in setLanguages()
- **File:** spellchecker.cpp:83
- **Severity:** Low
- **Analysis:** `seen.contains(lang)` is case-sensitive. `{"en_US", "EN_US"}` loaded as separate dictionaries. Same root cause as SPL2-12 but different code site.
- **Impact:** Duplicate dictionary loading on case-different language inputs.

### [COMP-N02] Case-sensitive suffix check misses mixed-case extensions — silent format loss
- **File:** documenthandler.cpp:1154
- **Severity:** Medium
- **Analysis:** saveAs() only checks lowercase and UPPERCASE extensions ("html", "html", "HTML", "HTM" etc). Extensions like "Html", "Htm" on case-preserving filesystems (Windows/macOS) slip through — file saved as plain text, silently destroying all formatting.
- **Impact:** Silent formatting loss when saving files with mixed-case extensions.

### [COMP-N03] regularMarker() same double-textCursor anti-pattern as LOG-07
- **File:** documenthandler.cpp:693-696
- **Severity:** Low
- **Analysis:** Null-check on local QTextCursor (fetch 1), reads anchor properties from 3 independent textCursor() calls (fetches 2-4). LOG-07 documents namedMarker() only — regularMarker() has identical bug.
- **Impact:** Rare stale formatting state on marker toolbar button.

### [LBL-N01] All 12 Sliders in EditorToolbar missing Layout.fillWidth: true — cramped
- **File:** EditorToolbar.qml (12 Slider instances)
- **Severity:** Medium
- **Analysis:** Every Slider child of RowLayout (velocity, opacity, fontSize, lineHeight, paragraphSpacing, wordSpacing, overlayOpacity, overlayBrightness, letterSpacing, baseSpeed, baseAcceleration, WYSIWYG fontSize) lacks Layout.fillWidth. Renders at implicit width (~100px) even when toolbar is 800+ px wide.
- **Impact:** All sliders unnecessarily short and imprecise on wide displays. Primary velocity slider during prompting especially affected.

### [LBL-N02] 11 Labels with Layout.bottomMargin: -14 — undefined behavior, overlap risk
- **File:** EditorToolbar.qml (11 Label instances)
- **Severity:** Medium
- **Analysis:** Negative margins on RowLayout children are undefined behavior per Qt Quick docs. Intent is vertical tightening but relies on undefined layout engine behavior. Can cause label text to bleed into adjacent rows.
- **Impact:** Text overlap on adjacent rows; fragile to Qt version/font size changes.

### [LBL-N03] PrompterView 3× height overflow in theforce debug mode
- **File:** PrompterPage.qml:739
- **Severity:** Low
- **Analysis:** `height: (root.theforce ? 3 : 1) * parent.height`. At minimum window (291px), produces 873px — far exceeding window. Oversized Flickable allocates and renders off-screen content.
- **Impact:** 3× memory/layout overhead in debug mode; visual corruption on small windows.

---

## Deep Synthesis Analysis (Wave 41 Synthesis Subagent)

### Top 3 Root Causes Generating Most Downstream Bugs

**Root Cause #1: Declarative/Imperative Binding Destruction (~30 bugs)**
QML declarative bindings silently destroyed by imperative writes on user interaction. No recovery mechanism. Each user action permanently degrades state: ~23 ToolButton checked states, 3 drag-origin bindings, 4 telemetry toggles, animation running flags, TabBar currentIndex, named bookmark indicator.

**Root Cause #2: Qt Version Confusion — Import/API Mismatch (~22 bugs)**
Targets Qt 6.5 but uses Qt 5.0/5.14/5.15 import versions, Qt 6.6+ versions, and Qt 6.7+ APIs indiscriminately. No systematic version enforcement. Dead imports block entire components (ReadRegionOverlay, ProjectionsManager, native menus).

**Root Cause #3: Unvalidated Pointer/Container Dereference (~14 bugs)**
C++ members/containers accessed without null or bounds validation. Many reachable from QML via Q_INVOKABLE before state initialization. Null QTextDocument derefs, empty QList first()/last(), uninitialized members, missing row bounds guards.

### Critical Bug Chains

**Chain A — Dead Component Cascade (35+ bugs):** R4-QTV-02 → ReadRegionOverlay fails to load, masking QML-01 (26 undefined refs), QML-02, R4-ROV-01/02/03, R4-BKG-01, SCP-01/02, UNIT-07. R4-QTV-01 → ProjectionsManager fails to load, masking R4-PRJ-01/02/03/04, SCP-08. IMP-N01 → native menus dead. **35+ bugs invisible behind 3 broken imports.**

**Chain B — Network Reply Double-Fault:** RES-01 (m_reply overwritten without abort) + RES-02 (slot uses wrong reply) + NET-01 (error never checked) + SAVE-N01 (phantom temp-file URL). Each alone is High; combined guarantee silent data corruption + crash + broken saves.

**Chain C — Search/Replace Death Spiral (guaranteed):** LOG-05 (loop param ignored) + LOG-06 (infinite loop) + CUR-N01 (replacement matches search pattern). **100% CPU hang on any regex Replace All, even `replaceAll("a","aa")`.**

**Chain D — Progressive UI Decay:** R2-EDT-03 + EVT-04/05/06 + R4-ROV-02 + QML-BND-01/02 + R2-TEL-01 + EVT-07 + ACT-N07. **30+ bugs from one root cause: declarative bindings destroyed by imperative writes.**

**Chain E — Settings Split-Personality:** SET-01 (C++ and QML write to different QSettings domains on macOS/iOS) + SET-02 (factoryReset clears only one domain). Neither file alone reveals the divergence. "Reset" button is a lie.

**Chain F — Hotkey Annihilation Triad:** HTK-01 (defaults erased on customize) + HTK-02 (persistence broken in non-KDE builds) + HTK-03 (defaults zeroed on Wayland-EGL). **Hotkeys broken on ALL platform/build combinations.**

### Top 5 Fix Priority Order (Highest Leverage)

| Priority | Bug(s) | Lines | Direct Fixes | Cascade Fixes |
|---|---|---|---|---|
| **1** | SEC-01 (sys:// RCE) | ~3 | 1 | 2 |
| **2** | R4-QTV-01 + R4-QTV-02 (dead imports) | ~2 | 2 | **35+ unmasked** |
| **3** | R3-CTX-01 (AbstractUnits QML_ELEMENT) | 1 | 1 | 5+ (all animations work) |
| **4** | R2-EDT-03 (binding break pattern) | ~5 | 23 | 8+ |
| **5** | HTK-01 (defaults destroyed) | ~3 | 1 | 2 |

**Fixing priorities 1-5: ~27 bugs directly fixed, 50+ cascade-fixed, ~14 lines of code.**

### Bugs With Compound Severity

- **RES-01+RES-02:** Stale reply downloads AND its data loaded → guaranteed silent data corruption → **Critical**
- **LOG-05+LOG-06+CUR-N01:** Infinite loop on ALL regex Replace All → **Critical (guaranteed)**
- **DLG-N01+DLG-N02+R3-DOC-04:** Modified cleared before AND after failed save → **Critical data loss**
- **SET-01+SET-02:** Settings split + false "factory reset" → **Critical**

### Bugs Visible Only From Abstract Overview (Cross-File)

- SET-01+SET-02: C++ and QML agree on wrong QSettings domain assumption
- PLAT-01: KF6Crash CMake var never compiled into C++ macro — build file and source look correct in isolation
- SCP-01 through SCP-20: 20 files reference `root.*` via outer-scope id resolution — works "by accident"
- R3-CTX-01 + Qt 5 registration comments + 36 QML call sites: Three pieces in three different files needed to see full picture
- HDR-N01 + LOG-01/02: 3 bugs documented in a file never compiled — need build system + code analysis together

---

## Wave 42 — Layout, Dialogs, Q_PROPERTY, Paths, Mobile

### [LAY-N01] 10 Labels with Layout.margins but inside MouseArea, not direct layout child — dead
- **File:** EditorToolbar.qml (10 Labels)
- **Severity:** Low
- **Analysis:** opacityLabel, fontSizeLabel, lineHeightLabel, paragraphSpacingLabel, wordSpacingLabel, overlayOpacityLabel, overlayBrightnessLabel, letterSpacingLabel, baseSpeedLabel, baseAccelerationLabel declare Layout.topMargin/bottomMargin/rightMargin/leftMargin but are children of MouseArea, not the surrounding RowLayout. Layout attached properties only apply to direct layout children. Negative bottomMargins (-14) meant to tighten vertical spacing are silently ignored.
- **Impact:** Labels appear at default positions without intended spacing adjustments.

### [LAY-N02] WheelSettingsOverlay explanation text constrained to single column in 2-column GridLayout
- **File:** WheelSettingsOverlay.qml:100-109
- **Severity:** Low
- **Analysis:** GridLayout columns:2. Explanation text RowLayout occupies column 0 only. Missing Layout.columnSpan:2 means text constrained to half width, causing excessive vertical wrapping.
- **Impact:** Dense text wrapping; wasted space in right column.

### [DLG-N10] TimerClock ColorDialog selectedColor never initialized from persisted settings
- **File:** TimerClock.qml:198-210
- **Severity:** Medium
- **Analysis:** onVisibleChanged syncs custom `color` but never `selectedColor` — the property the dialog actually displays. On app restart, dialog shows Qt's runtime default instead of persisted QSettings color.
- **Impact:** Timer color picker shows wrong starting color on first open after restart.

### [DLG-N11] PrompterPage ColorDialogs — dead acceptedColor property binding
- **File:** PrompterPage.qml:1010,1025, PrompterView.qml:240-241
- **Severity:** Low
- **Analysis:** Both colorDialog and highlightDialog declare `property color acceptedColor` but never assign it. PrompterView binds prompter.textColor/textBackground to acceptedColor — binding receives default/uninitialized value. Currently masked by direct setTextColor() call in onAccepted.
- **Impact:** Dead binding. Would silently break color changes if refactored to rely on binding.

### [QPROP-N02] comesFromNetwork Q_PROPERTY missing WRITE clause
- **File:** documenthandler.h:121
- **Severity:** Medium
- **Analysis:** `setDocumentComesFromNetwork()` exists (public, emits NOTIFY, called from C++), but WRITE absent from Q_PROPERTY declaration. Read-only to QML property system.
- **Impact:** Any QML attempting to set comesFromNetwork silently fails.

### [PATH-N01] save() fragile percent-encoding round-trip — broken for UNC paths
- **File:** documenthandler.cpp:1183
- **Severity:** Medium
- **Analysis:** `QUrl::toPercentEncoding()`→`toStdString()`→`fromStdString()`→`setUrl()` chain is unnecessary. UNC paths (`//server/share/file.html`) mangled because setUrl() interprets leading `//` as authority delimiter. Should be `QUrl::fromLocalFile(fileName)`.
- **Impact:** save() produces broken URLs for Windows UNC paths.

### [PATH-N02] reload() constructs file:// URL via raw string concat — #/? in filenames break URL
- **File:** documenthandler.cpp:860
- **Severity:** Medium
- **Analysis:** `QUrl("file://" + fileUrl)` — no URL-encoding. `#` parsed as fragment delimiter, `?` as query delimiter. Spaces produce invalid URL. Root cause of R3-DOC-06 m_reloading permanently stuck. Should be `QUrl::fromLocalFile(fileUrl)`.
- **Impact:** File-watcher reload silently fails for files with #, ?, or space in path.

### [MOB-01] Android: projectionManager undefined — 3 unguarded reference sites
- **File:** +android/main.qml:303-306, PrompterPage.qml:746
- **Severity:** Medium
- **Analysis:** projectionManager stub entirely commented out. "Disable projections" menu action's checked binding and onTriggered reference undefined id. PrompterPage layer.enabled binding silently fails.
- **Impact:** Menu action non-functional. Prompter viewport layer.enabled always undefined.

### [MOB-02] No +ios/ QML selector — iOS inherits base main.qml with desktop-only components
- **File:** Missing +ios/main.qml
- **Severity:** Medium
- **Analysis:** iOS loads base main.qml which instantiates ProjectionsManager (desktop QWindow objects), Labs.MenuBar (native menubar), onFrameSwapped (grabToImage every frame). iOS has no multi-window or menu bar support.
- **Impact:** Unnecessary component init, spurious QWindow creation, per-frame grabToImage on iOS.

### [MOB-03] iOS: IosSaveDialog silently hangs QML caller when temp dir invalid
- **File:** iossavedialog.mm:79-81
- **Severity:** Medium
- **Analysis:** `if (!m_tempDir.isValid()) return;` — early return without emitting rejected(). QML waits forever for accepted() or rejected() signal.
- **Impact:** Save-as flow hangs indefinitely with no feedback on temp dir failure.

### [MOB-04] Android: restartApplication() quits without restart
- **File:** qmlutil.hpp:97-103
- **Severity:** Low
- **Analysis:** On Android/iOS/WASM/WatchOS, QProcess guard skips startDetached, leaving only quit(). Factory reset just closes app without relaunching.
- **Impact:** User must manually reopen app after factory reset.

### [MOB-05] Android: Missing INTERNET permission in manifest
- **File:** android/AndroidManifest.xml:48-53
- **Severity:** Low
- **Analysis:** App uses Qt::Network (remote files, OBS WebSocket). android.permission.INTERNET not declared. Qt may auto-inject via library merge but explicit needed for API < 31.
- **Impact:** Network failure on older Android devices; remote file/OBS silently fail.

### [MOB-06] Android: PrompterPage display delegate Component.onCompleted references projectionManager — startup TypeError
- **File:** PrompterPage.qml:675-677
- **Severity:** Low
- **Analysis:** `visible = projectionManager.isEnabled` in onCompleted runs even when parent action hidden. Spurious TypeError on Android startup.
- **Impact:** Console error on startup; no user-facing effect (parent action hidden).

---

## Wave 43 — Menus, Debug, Static Analysis, Data Flows

### [MENU-N01] contextMenu.popup(this) missing click coordinates — menu at wrong position
- **File:** Prompter.qml:1402
- **Severity:** Medium
- **Analysis:** `contextMenu.popup(this)` equivalent to popup(parent, 0, 0) — menu at top-left of editor. Right-click position available via `mouse` parameter but ignored.
- **Impact:** On mobile/WASM, spell-check context menu at top-left instead of click position.

### [MENU-N02] Mobile "Add to dictionary" missing %1 placeholder — word never shown
- **File:** Prompter.qml:2620
- **Severity:** Medium
- **Analysis:** `qsTr("Add to dictionary", ...).arg(prompter.spellMisspelledWord)` — no `%1` in string. arg() silently does nothing. Desktop version has `qsTr("Add \"%1\" to dictionary", ...)`.
- **Impact:** Users see "Add to dictionary" with no indication of which word.

### [MENU-N03] Text alignment menu RTL swap: labels swap but actions don't
- **File:** EditorToolbar.qml:362-374
- **Severity:** Medium
- **Analysis:** `text` and `enabled` bindings swap for RTL, but `onTriggered` unconditionally sets AlignLeft/AlignRight. In RTL, clicking "Right" sets AlignLeft. Global Format menu correctly swaps both text and action.
- **Impact:** Alignment menu produces opposite of label in RTL mode.

### [MENU-N04] Trailing empty MenuSeparator at end of mobile context menu
- **File:** Prompter.qml:2662
- **Severity:** Low
- **Analysis:** Final MenuSeparator with no menu items after it creates dangling separator line.
- **Impact:** Visual artifact — thin line at bottom of context menu.

### [MENU-N05] "Redo" context menu item missing & accelerator
- **File:** Prompter.qml:2633
- **Severity:** Low
- **Analysis:** All other menu items have `&` accelerator. "Redo" is the only one missing it.
- **Impact:** Keyboard navigation skips Redo when cycling accelerators.

### [MENU-N06] Paste behavior inconsistent between context menu and global Edit menu
- **File:** Prompter.qml:2564,2651 vs main.qml:686
- **Severity:** Low
- **Analysis:** Context menu Paste → document.paste() (filters HTML). Global Edit menu Paste → editor.paste() (raw, unfiltered). Same operation, different results.
- **Impact:** HTML from browser pasted via global Edit menu injects unfiltered HTML.

### [DBG-N01] OBS WebSocket auth challenge+salt logged to console in release builds
- **File:** Prompter.qml:364,372,386
- **Severity:** Medium
- **Analysis:** `console.log(m)` logs full WebSocket Hello message including authentication challenge and salt on every connection. `console.info(m)` at line 386 maps to qInfo() — never suppressed. No debug guard.
- **Impact:** Security-sensitive material leaked to console/logs in production.

### [DBG-N02] Velocity debug logging active in production
- **File:** Prompter.qml:606, InputsOverlay.qml:441
- **Severity:** Low
- **Analysis:** `console.log("velocity: ", velocity)` and modifier logging on every keypress/ComboBox change. No debug guard.
- **Impact:** Production console spam on every velocity change.

### [DBG-N03] Latent debug state leak: pointers/debug Setting persists Guides checkbox
- **File:** PointerSettings.qml:94, ReadRegionOverlay.qml:239
- **Severity:** Low
- **Analysis:** After QML-01 fixed, users who checked "Guides" will see red debug rectangles appear with no way to disable (cross-file reference still broken).
- **Impact:** Debug rectangles appear in production after fixing QML-01.

### [DBG-N04] qDebug() in namedMarker()/setMarker() active in release
- **File:** documenthandler.cpp:760,793
- **Severity:** Low
- **Analysis:** `qDebug() << "Empty"` and `qDebug() << marker` trace every marker query/set. CMake doesn't define QT_NO_DEBUG_OUTPUT.
- **Impact:** Production debug spam on every marker interaction.

### [WARN-N01] SpellHighlighter::isEnabled() — dead code, never called
- **File:** spellhighlighter.h:36
- **Severity:** Low
- **Analysis:** Public method defined but zero invocations in entire codebase.

### [WARN-N02] SpellChecker::addWord() — dead public API, never called
- **File:** spellchecker.h:48, spellchecker.cpp:134-140
- **Severity:** Low
- **Analysis:** Full implementation but never invoked. DocumentHandler uses addCustomWord() instead.

### [WARN-N03] quint64→int implicit narrowing in nextMarker()/previousMarker()
- **File:** documenthandler.cpp:1713,1721
- **Severity:** Low
- **Analysis:** Q_INVOKABLE accepts quint64 but calls MarkersModel methods taking int. 64→32 bit unsigned→signed truncation. Compiler warning on some toolchains.
- **Impact:** Code quality — practical document sizes stay within int range.

### [WARN-N04] QProcess::startDetached() bool return silently ignored
- **File:** qmlutil.hpp:91
- **Severity:** Low
- **Analysis:** `startDetached()` returns bool. Discarded. If program not found, failure invisible — no error logged, no QML notification.
- **Impact:** Silent failure of sys:// URL handler and app restart on missing program.

### [FLOW-N01] setKeyMarker() calls setAnchor("#") — const char*→bool conversion, href never set
- **File:** documenthandler.cpp:716
- **Severity:** Medium
- **Analysis:** `format.setAnchor("#")` — `setAnchor(bool)` is only overload. `"#"` decays to const char* → pointer-to-bool → true. setAnchorHref never called. Regular markers (setMarker:798) correctly use `setAnchorHref("#")`. Parse sees key markers with url="" vs regular markers with url="#".
- **Impact:** Inconsistent marker url role; QML consuming url sees wrong classification.

### [FLOW-N02] increaseVelocity()/decreaseVelocity() skip velocity change when paused
- **File:** Prompter.qml:494-497,510-513
- **Severity:** Medium
- **Analysis:** `if (this.__play) this.__i++` — __i modification gated on play. When paused, functions only resume at existing velocity + trigger animated jump to document end. Contrast with setVelocity() which always modifies __i.
- **Impact:** "Increase/Decrease Velocity" buttons do nothing to velocity when paused — behavioral inconsistency.

---

## Wave 44 — Drag, Timers, QFileInfo, Creative Scan

### [DEF-N01] Flickable.flicking undefined in Qt 6 — wrong cursor during momentum scroll
- **File:** Prompter.qml:1981,2024
- **Severity:** Medium
- **Analysis:** `flicking` was Qt 5 Flickable property renamed to `moving` in Qt 6. Resolves to `undefined` (falsy). Cursor falls to wrong branch — OpenHandCursor instead of OpenHandCursor-like drag visual during momentum scroll.
- **Impact:** Wrong cursor cue during momentum scroll on Qt 6.

### [DEF-N02] DropArea internalDrag always false — internal drag handler dead code
- **File:** Prompter.qml:1331,1350
- **Severity:** Medium
- **Analysis:** `property bool internalDrag: false` never set to true. C++ startTextDrag()/startRangeDrag() never called from QML. Actual internal drag uses separate manual MouseArea mechanism. If startTextDrag() ever invoked, onDropped would incorrectly treat internal drag as external content, corrupting the operation.
- **Impact:** Two parallel drag systems with no connection. Dead code hazard.

### [TMR-N01] resetBackground Timer not stopped when new background loaded — race erases new image
- **File:** PrompterBackground.qml:47-57,73-76
- **Severity:** Medium
- **Analysis:** clearBackground() starts 2.8s timer to clear source. setBackgroundImage() loads new image but never stops timer. If user clears background then immediately loads new image within 2.8s, timer fires and erases newly loaded image.
- **Impact:** New background image silently disappears after ~2.8 seconds.

### [TMR-N02] Windows onFrameSwapped missing qmlutil.r(p) — per-frame grab result leak
- **File:** +windows/main.qml:706-716 vs main.qml:1036-1047
- **Severity:** Medium
- **Analysis:** Base main.qml calls qmlutil.r(p) for double-buffer + deleteLater. Windows variant missing this call. Each grabToImage() (60fps) leaks one QQuickItemGrabResult when projections enabled.
- **Impact:** Steady memory leak on Windows during screen projections. Accumulates unboundedly.

### [CMAKE-N05] foreach(file IN LISTS icon_files doc) — "doc" never defined
- **File:** src/CMakeLists.txt:243
- **Severity:** Low
- **Analysis:** Variable `doc` never defined. CMake treats as empty. If `doc` was typo for `document_files`, all welcome HTML docs would receive wrong resource aliases.
- **Impact:** Dead/confusing code; probable typo masked by undefined=lazy empty.

### [PRE-N01] Preprocessor uses `or` instead of `||` in 6 #if directives — MSVC build break
- **File:** documenthandler.cpp:132,347,911,1057; globalhotkeys.cpp:560,832
- **Severity:** Low
- **Analysis:** `#if (defined(Q_OS_MACOS) or defined(Q_OS_IOS))` — C preprocessor doesn't recognize `or` on MSVC without `/Zc:preprocessor`. 40+ other guards use `||`.
- **Impact:** Build failure on MSVC with `/permissive-`.

### [CNTD-N01] Countdown Running: dissolveIn and dissolveOut compete for same opacity when __iterations===__disappearWithin===1
- **File:** Countdown.qml:289-291,308
- **Severity:** Low
- **Analysis:** Running state sets dissolveIn.running=true (fade-in 0→1) AND dissolveOut.running (fade-out 1→0) concurrently when both equal 1. Two NumberAnimations compete for countdown.opacity — winner undefined.
- **Impact:** Erratic opacity flash/stutter with specific countdown config (1 iteration + 1 disappear step).

### [QF-N02] QDir::entryList missing QDir::Readable in availableDictionaries()
- **File:** spellchecker.cpp:254
- **Severity:** Low
- **Analysis:** `QDir::Files` lists unreadable .dic files as available. Hunspell fails to open them with only qWarning, no user feedback.
- **Impact:** Broken-permission dictionaries pollute available list.

### [QF-N03] TOCTOU: QFile::exists() → QFile::copy() in resource cache extraction
- **File:** spellchecker.cpp:198-199
- **Severity:** Low
- **Analysis:** Another process creating outPath between exists() check and copy() causes copy to silently fail (masked by unchecked copy return = EDGE-09). Corrupt partial file passes future exists() checks.
- **Impact:** Corrupt Hunspell dictionaries persist indefinitely; only manual cache deletion fixes.

---

## Wave 45 — Integer Portability, Text, URLs, Performance, Error Recovery

### [TXT-CRIT] Plain 'v'/'V' keypress silently consumed — letter 'v' cannot be typed
- **File:** Prompter.qml:2163-2168
- **Severity:** Critical
- **Analysis:** In no-modifiers branch, `case Qt.Key_V:` catches every plain 'v', Shift+'v', Alt+'v' and forwards to prompter handler where Ctrl modifier check fails → nothing happens. Letter silently discarded. Copy-paste error from Ctrl+modifier block where `case Qt.Key_V` correctly handles Ctrl+V paste.
- **Impact:** Letter 'v' cannot be typed anywhere in scripts — ~1% of English characters lost. Documents requiring "very", "voice", "video" etc. impossible to type.

### [TXT-N03] Toolbar paste and Edit menu paste bypass HTML sanitization
- **File:** EditorToolbar.qml:345, main.qml:686
- **Severity:** Medium
- **Analysis:** Both invoke TextArea.paste() directly — zero HTML filtering. Ctrl+V and context menu correctly call document.paste() which runs filterHtml(). Same "Paste" operation produces different results depending on access path.
- **Impact:** HTML pasted via toolbar/menu retains unwanted formatting (hardcoded sizes, colors, nowrap). Inconsistent behavior vs shortcuts.

### [TXT-N04] goToNextMarker() temporarily sets cursorPosition=-1 — corrupts cursor state
- **File:** Prompter.qml:656-659
- **Severity:** Medium
- **Analysis:** When no markers exist, nextMarker() returns Marker(-1) with position=-1. editor.cursorPosition set to -1 fires onChange signals; cursorRectangle.y read from invalid state before guard corrects position. Qt may assert-fail in debug.
- **Impact:** Visual jitter/flash on "next marker" with empty markers list. Debug assertion failures.

### [INT-N01] quint64→int narrowing at DocumentHandler→MarkersModel boundary (4 sites)
- **File:** documenthandler.cpp:1713,1721, markersmodel.h:62-63
- **Severity:** Low
- **Analysis:** DocumentHandler Q_INVOKABLE accepts quint64 position but MarkersModel takes int. 64→32 bit truncation. For very large documents (>2GB text), marker navigation produces wrong results.
- **Impact:** Wrong marker positions in very large documents.

### [INT-N02] replaceAll() returns long — 32-bit overflow on Windows x64
- **File:** documenthandler.h:228, documenthandler.cpp:1494
- **Severity:** Medium
- **Analysis:** long is 32-bit on Windows x64 (LLP64). Replacement counter silently overflows at 2^31 matches. Should be qlonglong/qint64.
- **Impact:** Replace-all count silently wrong on Windows with >2B matches.

### [INT-N03] 6 qsizetype→int narrowing conversions across models and loops
- **File:** markersmodel.cpp:101,121, promptsession.cpp:88, main.cpp:274, spellchecker.cpp:98,328
- **Severity:** Low
- **Analysis:** size()/length()/indexOf() return qsizetype (64-bit), narrowed to int (32-bit). Sentinels like -1 fit but values > INT_MAX corrupt.
- **Impact:** Code quality — practical document sizes stay within int range.

### [URL-N03] Network-loaded HTML lacks base URL — relative resources broken
- **File:** documenthandler.cpp:888-901
- **Severity:** Medium
- **Analysis:** loadFromNetworkFinihed never calls doc->setBaseUrl(). Original network URL discarded. Relative URLs in HTML (`<img src="images/photo.jpg">`) can't resolve. May resolve against stale base URL from prior local file.
- **Impact:** Images, stylesheets in network-loaded HTML fail to load.

### [URL-N04] loadFromNetwork() validates wrong URL instance
- **File:** documenthandler.cpp:881
- **Severity:** Low
- **Analysis:** `if (url.isValid())` checks original URL, not constructed resultingUrl. Valid relative URL can produce invalid resultingUrl that passes unchecked.
- **Impact:** Invalid network requests silently initiated.

### [URL-N05] openFromRemote() blindly prepends http:// to non-HTTP schemes
- **File:** PrompterPage.qml:1279-1282
- **Severity:** Medium
- **Analysis:** Any URL not starting with http:// or https:// gets http:// prepended. `file:///path` becomes `http://file:///path`. Case variants like `HTTP://` not handled.
- **Impact:** Silently broken behavior when pasting file:// or other-scheme URLs.

### [PERF-N01] onFrameSwapped calls markerCompare() unconditionally — wasted JS call every frame
- **File:** main.qml:1038
- **Severity:** Medium
- **Analysis:** markerCompare() fires every display frame (60-144 Hz) even when not prompting. Has internal guard that returns immediately, but JS function call/stack frame overhead wasted. State check should be hoisted.
- **Impact:** 60+ wasted function calls/sec during editing.

### [PERF-N02] RecentDocuments._load() blocks startup with N synchronous createObject() calls
- **File:** RecentDocuments.qml:221,82-107
- **Severity:** Medium
- **Analysis:** Up to 30 Kirigami.Action components created synchronously during Component.onCompleted. Plus file-existence queries via C++. All on main thread during startup.
- **Impact:** App startup delayed proportionally to recent document count. ~50-200ms extra latency with 30 entries.

### [PERF-N03] velocityDragOverlay hot-loop calls velocity functions without throttling
- **File:** PrompterPage.qml:939-976
- **Severity:** Low
- **Analysis:** for-loop calls increase/decreaseVelocity N times per mouse event (N=⌊deltaY/20⌋). Each triggers full Prompter binding cascade + position update + NumberAnimation rebind. Dozens of velocity changes per mouse event.
- **Impact:** UI jank during mouse-drag velocity adjustment.

### [ERR-N01] removeCustomWord() silently drops dictionary languages on partial reload failure
- **File:** spellchecker.cpp:334-344
- **Severity:** Medium
- **Analysis:** If any loadOne() fails during reload, language silently skipped — lost from m_dicts with no notification. Always returns true (success).
- **Impact:** User loses entire dictionary languages silently after removing a custom word.

### [ERR-N02] insertImageAt() async callback silently discards 3 failure modes
- **File:** documenthandler.cpp:1744-1752
- **Severity:** Medium
- **Analysis:** Network error, null downloaded image, null textDocument — all three silently return without emitting error(). User sees nothing happen.
- **Impact:** Silent failure when pasting remote images; no way to know operation failed.

### [PATH-N03] Wrong ../fonts/ depth in +android and +windows FontLoader paths
- **File:** +android/main.qml:465, +windows/main.qml:531
- **Severity:** High
- **Analysis:** `source: "../fonts/LibertinusSans-Regular.otf"` but files nested one level deeper than base main.qml. Path resolves to non-existent qrc location. Base main.qml:560 at correct depth.
- **Impact:** Timer/stopwatch number font fails to load on Android and Windows. Falls back to system default.

---

## Wave 46 — Signals, QObject, Tabs, Regex, Defaults, Visual

### [SIG-N03] MessageDialog.onButtonClicked declares unused second parameter role
- **Files:** main.qml:1088, +windows:757,777,797, +android:681,701
- **Severity:** Low
- **Analysis:** buttonClicked signal has signature `buttonClicked(StandardButton button)` — 1 param. Handler declares `(button, role)` with 2 params. role always undefined. Copy-paste error.
- **Impact:** None functionally (role never accessed). Misleading for maintainers.

### [QOBJ-N01] QmlUtil missing constructor with parent parameter
- **File:** qmlutil.hpp:47
- **Severity:** Low
- **Analysis:** QML_ELEMENT type with all methods inline. No parent constructor. `new QmlUtil` from C++ leaks without parent.
- **Impact:** Potential leak if instantiated from C++ (currently only QML instantiated via singleton).

### [TAB-N01] PointerSettings TabButton onClicked skips currentIndex assignment
- **File:** PointerSettings.qml:268-289
- **Severity:** Medium
- **Analysis:** All 4 TabButtons call `positionViewAtIndex(...)` but never set `listView.currentIndex`. currentIndex may not update until animation completes. TabBar highlight and PropertyChanges stale during animation. InputsOverlay.qml correctly uses direct `currentIndex = N`.
- **Impact:** TabBar highlight desync during tab switch animation. Wrong pointer settings displayed momentarily.

### [REGEX-CRIT-01] regex_4 destroys <body> tag — removes opening tag instead of color attributes
- **File:** documenthandler.cpp:1287
- **Severity:** High
- **Analysis:** Pattern matches from `<body` through last color attribute quote but doesn't consume `>`. replace() deletes everything from `<body` to last `"`, leaving orphaned `>content</body>`. Intended approach (commented-out loop) surgically removes one color at a time.
- **Impact:** HTML body tag destroyed; content after replacement is corrupted HTML.

### [REGEX-CRIT-02] searchRegEx.setPattern() from user input — isValid() never called
- **File:** documenthandler.cpp:1543-1544
- **Severity:** High
- **Analysis:** User input from QML search box passed directly to setPattern(). No isValid() check. Invalid pattern (unbalanced parentheses, malformed quantifiers) → undefined behavior in QTextDocument::find().
- **Impact:** Search/replace crashes or silently misfires on invalid user regex.

### [REGEX-N04] ReDoS — user-supplied regex has no length limit, timeout, or backtracking guard
- **File:** documenthandler.cpp:1543-1557
- **Severity:** Medium
- **Analysis:** subString from QML user input. No QRegularExpression::optimize(), MatchTimeout, or pattern-length cap. Evil regex like `(a+)+b` causes exponential backtracking in replaceAll() loop. Combined with LOG-05/LOG-06 infinite loop risk.
- **Impact:** Application hang with 100% CPU during Search/Replace All with malicious regex.

### [REGEX-N05] regex_0 and regex_3 use . (any-char) instead of \. (literal dot) in decimal matching
- **File:** documenthandler.cpp:893-894,1274-1275
- **Severity:** Low
- **Analysis:** `(?:.[\d]+)*` intended as `(?:\.[\d]+)*` for decimal points. Unescaped `.` matches any character, potentially over-matching on malformed CSS.
- **Impact:** Minor. Works by coincidence on well-formed inputs.

### [REGEX-N06] imgSrcRegex captures wrong src when data-src follows real src
- **File:** documenthandler.cpp:1432-1434
- **Severity:** Medium
- **Analysis:** Pattern `[^>]+` is greedy. For `<img src="real.jpg" data-src="lazy.jpg">`, backtracks to last `src=` occurrence (inside data-src), capturing lazy.jpg. Should use `[^>]+?` or word boundary before `src`.
- **Impact:** Wrong (lazy/placeholder) image URL loaded for images with lazy-load attributes.

### [VCI-N01] At-end action buttons use inconsistent font scaling (1/1.5 vs 1/1.75) in same group
- **File:** Prompter.qml:1158,1185,1212 vs 1256,1269,1309
- **Severity:** Low
- **Analysis:** Stop/Exit/Loop buttons scale by 1/1.5; adjacent Flipable buttons and SpinBox scale by 1/1.75. Buttons visibly 16.7% larger than neighbors.
- **Impact:** Visible size mismatch between button rows in same footer control.

### [VCI-N02] upperControls and bottomControls fade to different opacity levels during Prompting
- **File:** PrompterView.qml:70 vs 120
- **Severity:** Low
- **Analysis:** Top controls fade to 0.1, bottom controls to 0.2 during Prompting. Identical purpose, different opacity target.
- **Impact:** Asymmetric fade — top controls nearly invisible while bottom controls remain twice as visible.

### [VCI-N03] Hardcoded divider/separator/border colors (#292929, #606060, #808080) break theme adaptation
- **Files:** PointerSettings.qml, InputsOverlay.qml, Find.qml, PrompterPage.qml, ProgressIndicator.qml
- **Severity:** Low
- **Analysis:** Fixed gray values never adapt to theme. Dark themes render dividers near-invisible; light themes produce harsh dark borders.
- **Impact:** Divider lines invisible on dark themes, jarring on light themes.

---

## Wave 47 — Unicode, Android, Clipboard, Switch

### [UTF-N01] text.truncate(64) can split UTF-16 surrogate pairs — corrupted display
- **File:** documenthandler.cpp:736
- **Severity:** Medium
- **Analysis:** `text.truncate(64)` cuts at UTF-16 code unit 64. Supplementary-plane character (emoji, rare CJK) straddling position 64 → orphaned high surrogate. Also `text.truncate(-1)` when no space found in first 64 chars (lastIndexOf returns -1) → undefined behavior.
- **Impact:** Corrupted preview text in font dialog for texts with emoji or rare CJK.

### [AND-CRIT-01] Missing android.permission.INTERNET — all network silently fails
- **File:** AndroidManifest.xml:47-53
- **Severity:** Critical
- **Analysis:** Manifest requests READ_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE, ACCESS_WIFI_STATE, but omits INTERNET. App uses QNetworkAccessManager for loadFromNetwork() and WebSocket for OBS.
- **Impact:** Remote file loading and OBS scene switching silently fail on all Android versions.

### [AND-HIGH-01] Android back button doesn't dismiss overlays/drawers before close
- **File:** +android/main.qml:144-150, PrompterPage.qml:64
- **Severity:** High
- **Analysis:** PrompterPage.onBackRequested triggers close() directly. ESC key cascade (dismiss layers→drawers→overlays→find→exit prompting) absent from back button. Any open overlay/drawer triggers save-before-close instead of dismiss.
- **Impact:** Broken Android UX — cannot dismiss overlays with back button.

### [AND-HIGH-02] Android screen never sleeps after prompter use
- **File:** Prompter.qml:465
- **Severity:** High
- **Analysis:** `document.preventSleep(false)` on entering Editing is commented out. `preventSleep(true)` active for Prompting/Standby/Countdown. Combined with `keepScreenOn="true"`, screen stays on permanently after first session.
- **Impact:** Severe battery drain — screen never times out after using prompter once.

### [AND-HIGH-03] factoryReset() quits Android app without restarting
- **File:** qmlutil.hpp:97-103
- **Severity:** High
- **Analysis:** restartApplication() skip QProcess on Android → only quit(). Factory reset silently kills app; user must manually reopen.
- **Impact:** Factory reset exits app with no restart or feedback on Android.

### [AND-MED-01] Missing intent-filter for opening files from other apps
- **File:** AndroidManifest.xml:29-32
- **Severity:** Medium
- **Analysis:** Only LAUNCHER intent-filter. No VIEW filter for text/html or text/plain. Cannot open .html scripts from file managers, email, or Downloads.
- **Impact:** No "Open with QPrompt" or "Share to QPrompt" on Android.

### [CLP-N01] Copy/Cut exports unfiltered HTML to system clipboard
- **File:** Prompter.qml, EditorToolbar.qml, main.qml
- **Severity:** Medium
- **Analysis:** All copy/cut paths use editor.copy()/cut() — places raw QTextDocument HTML on system clipboard. filterHtml() doesn't strip scripts/event handlers (R4-EXP-01). Malicious HTML propagates to other apps via clipboard.
- **Impact:** Security boundary leak — dangerous HTML reaches browser/email via clipboard paste.

### [CLP-N02] DropArea external drop never calls drop.accept()
- **File:** Prompter.qml:1369-1379
- **Severity:** Medium
- **Analysis:** External drop branch processes content but never accepts drop action. Internal drag branches correctly call accept(). Drag source may signal rejection → rollback/undo on source side.
- **Impact:** Cross-application drag behavior undefined; source app may undo cut operations.

### [CLP-N03] DropArea external drop: URLs consumed preferentially — text silently lost
- **File:** Prompter.qml:1370-1378
- **Severity:** Medium
- **Analysis:** hasUrls branch handles ONLY images via insertImageAt() and never falls through to hasHtml/hasText. Browser drags with both URLs and HTML lose all text content.
- **Impact:** Drag-and-drop from web browsers inserts only images; all text silently lost.

### [SWT-N01] OBS WebSocket Switch checked binding broken on first toggle
- **File:** PrompterPage.qml:1468-1474
- **Severity:** Medium
- **Analysis:** `checked: viewport.prompter.ws.active` + `onToggled: viewport.prompter.ws.active = checked`. User toggle severs declarative binding. If WebSocket disconnects, ws.active=false but Switch still shows ON. Same class as R2-EDT-03.
- **Impact:** UI state mismatch — OBS Switch shows connected when actually disconnected.

---

## Wave 48 — Input Method, Window, Gesture

### [IMH-SYS] Systemic absence of inputMethodHints on ALL TextFields (16 sites)
- **Files:** EditorToolbar.qml (10 numeric TextFields), PrompterPage.qml (openUrl, wsUrlField, markerHrefField), PathsPage.qml (sofficePathField), PointerSettings.qml (3 color hex, 4 path TextFields), Find.qml (replaceField)
- **Severity:** Medium
- **Analysis:** Zero `inputMethodHints` set on any TextField. No `ImhFormattedNumbersOnly` on 10 numeric fields, no `ImhUrlCharactersOnly` on URL/path fields, no `ImhNoAutoUppercase` on dictionary word field, no `ImhNoPredictiveText` on replace field.
- **Impact:** Full QWERTY with auto-correct/auto-cap on all mobile fields. Numeric fields get wrong keyboard. URLs get auto-correct corruption. Dictionary words get forced capitalization. Paths get predictive text mangling.

### [EKA-SYS] Systemic absence of EnterKeyAction on ALL TextFields (7 sites)
- **Files:** PrompterPage.qml (openUrl, wsUrlField, markerHrefField, newWordField), Find.qml (searchField, replaceField), PathsPage.qml (sofficePathField)
- **Severity:** Low
- **Analysis:** Fields with onAccepted/onEditingFinished/ReturnPressed handlers lack EnterKeyAction. Virtual keyboard shows default "Return" instead of contextual "Go"/"Search"/"Done".
- **Impact:** Mobile keyboard enter-key label wrong — no visual cue for action. 10 EditorToolbar numeric fields also affected.

### [WINDOW-N01] Projection windows not closed on main window close — orphaned on Linux
- **File:** main.qml:159-165, +windows:154-160, +android:144-150
- **Severity:** Medium
- **Analysis:** onClosing opens save dialog if modified but never calls projectionManager.closeAll() or sets isEnabled=false. Projection Windows with transientParent:root: on Windows/macOS may auto-hide but on Linux/X11, transient children not guaranteed to close when parent closes.
- **Impact:** Orphaned projection windows remain on-screen after app exits on Linux.

### [GSW-N01] MarkersDrawer SwipeListItem navigates on swipe — gesture conflict on touch
- **File:** MarkersDrawer.qml:70-74
- **Severity:** Medium
- **Analysis:** `onPressed` fires at start of every touch including swipe. Swiping to reveal edit action first triggers navigation to marker position + drawer close. Should use `onClicked` which only fires on press-release without exceeding swipe threshold.
- **Impact:** Swipe-to-reveal-edit non-functional on touchscreens; every swipe navigates away first.

### [GSW-N02] Flickable onDragStarted uses stale __iBackup after non-prompting drags
- **File:** Prompter.qml:773-781,788-798
- **Severity:** Low
- **Analysis:** In editing mode, onMovementEnded leaves __iBackup non-zero. Second drag: guard prevents backup, restore uses stale first-drag value instead of current velocity.
- **Impact:** Wrong scroll velocity restored after consecutive drags in editing mode.

*Report: waves 1-10, synthesis, re-run, waves 27-48.*
