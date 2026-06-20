# Bug Hunt — Waves 11-26 Additional Findings

**Date:** 2026-06-20  
**Methodology:** Continuous parallel subagent rotation (8 agents/wave, 16 waves) after initial 10-wave sweep

---

## Top Critical/High Impact Findings Not in Main BUG-HUNT.md

### Translation File Corruption (68 bugs across 20 .ts files)

- **Finnish** welcome guide redirects to Dutch (`welcome_nl.html` instead of `welcome_fi.html`)
- **Dutch** welcome guide redirects to German (`welcome_de.html` instead of `welcome_nl.html`)
- Multiple languages translate "Language settings" as "Pointer settings" (Cyrillic, French, Portuguese — copy-paste error)
- Multiple languages translate "No pointers" as "Both pointers" (Finnish, French, Korean, Dutch)
- Multiple languages translate "Vertical offset" as "Velocity" (Finnish, French, Korean, Dutch, Portuguese)
- "Saved" translated as verb "Save" instead of adjective in 5 languages
- `Paragraph spacing <pre>%1%</pre>` — 8 languages strip the trailing `%` sign from placeholder
- `Line width <pre>%1</pre>` — 7 languages add spurious `%` sign after placeholder
- Hebrew and Polish .ts files exist but are commented out in UI
- Korean locale code `ko_KO` invalid (should be `ko_KR`)
- English locale `en` in .ts but `en_US` in UI (mismatch)

### iPadOS Platform Gaps (17 sites)

Qt 6.2+ returns `"ipados"` on iPads (distinct from `"ios"` on iPhones). 17 locations check only `=== "ios"`:
- `EditorToolbar.qml:88,291,784,797` — toolbar visibility/config wrong on iPad
- `Prompter.qml:806,994,2235,2278,2492` — MouseArea, text rendering, save dialog broken on iPad
- `PrompterPage.qml:1009,1024` — ColorDialog options wrong
- `TimerClock.qml:200`, `PrompterBackground.qml:107` — ColorDialog options wrong
- `PointerSettings.qml:653` — ColorDialog options wrong
- `main.qml:996`, `+android/main.qml:513` — toolbar style/visibility wrong

### Hotkey System Bugs

- **autoRepeat=true** for ALL QHotkey shortcuts — toggle/one-shot actions broken when held (TogglePrompter, Pause, Stop, Reverse flood with repeated activations)
- **QHotkey::setShortcut()** return value silently ignored — OS registration failures give zero user feedback
- **KGlobalAccel default corruption**: `m_setActionShortcut` calls `removeAllShortcuts()` BEFORE reading `defaultShortcut()`, permanently erasing factory defaults on every user customization
- Global Rewind/FastForward never stops — QHotkey emits only on press, no release path; action toggles to checked but never back

### WASM Platform

- **Infinite reload loop** on unauthorized host: every `toggle()` calls `officialHost()` which calls `QCoreApplication::quit()` → `aboutToQuit` → `location.reload()` → same host → repeat
- DOM input element never removed when user cancels file picker (cumulative DOM leak)
- Insecure hostname validation: `endsWith("localhost")` matches `evillocalhost.com`; `endsWith("qprompt.app")` matches `fakeqprompt.app`

### Build System

- **Missing breeze-icons submodule** — `.gitmodules` has no entry for `3rdparty/breeze-icons`; CMake FATAL_ERROR on fresh clone
- **Missing vcpkg.json** — `vcpkg-configuration.json` exists but no port manifest; vcpkg installs nothing
- **BSD detection broken** — CMake has no standard `BSD` variable; `${BSD}` never set → FreeBSD enters wrong FetchContent/CPack paths
- **QHotkey_FOUND never set** in FetchContent path — QHotkey compiled from source but `add_definitions(-DQHotkey_FOUND)` skipped → global hotkeys silently disabled
- **CMAKE_OSX_ARCHITECTURES** contains literal quotes (`"x86_64;arm64"` becomes value including quotes, not a list)
- **NSIS shortcut** points to `qprompt.exe` but binary is `QPrompt.exe`
- **InstallRequiredSystemLibraries** (module name) used instead of `CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS` — MSVC DLLs never bundled
- **vcvarsall.bat** in setup.sh runs in isolated cmd.exe subprocess — MSVC env vars not propagated to bash

### Timer/Countdown System

- **TimerClock ETA/stopwatch broken**: `timer.getTimeString()` references undefined `timer` id (should be `clock.getTimeString()`)
- **Countdown→Prompting via state++ bypasses toggle()**: timer not reset, sleep prevention not enabled, projections not created
- **document.parse() never called** when autoStart bypasses Standby — markers from edited text not reflected in prompter
- `timer.updateTimer()` corrupts `elapsedMilliseconds` before `timer.startTimer()` on countdown completion
- Countdown `__hypotenuse` formula uses `1.4333*Math.sqrt(...)` — ~43% too large for viewport corners

### QML Scope/Ownership

- `Find.qml` uses `root.__isMobile` but root Item has no `__isMobile` property (resolves to undefined)
- `ReadRegionOverlay.qml` uses `root.shadows` / `root.isMobile` — both undefined on plain Item root
- `PrompterView.qml` uses `root.theforce`, `root.__isMobile`, `root.visibility` — all undefined on viewport Item
- **Drag breaks property bindings**: `editor.x`, `positionHandler.x`, `stopwatch.x`, `stopwatch.y` all permanently lose declarative bindings after drag — same class as R4-ROV-02 but on different targets

### Z-Index / Event Propagation

- `velocityDragArea` (z:5) blocks `viewport.mouse` (z:5) wheel scrolling — both `anchors.fill: viewport`, velocityDragArea on top has no wheel handler, wheel events never reach viewport.mouse (sibling, not parent)
- Flow `ToolSeparator` visibility bound to `rowA.y === rowB.y` — when a row is invisible (y=0), matches first visible row (also y=0), separator incorrectly shown

### Input Method/IME

- Flickable MouseArea blocks IME composed events (`propagateComposedEvents: false`)
- Editor TextArea missing `inputMethodHints: Qt.ImhMultiLine`
- 10 numeric TextFields lack `inputMethodHints: Qt.ImhFormattedNumbersOnly` (virtual keyboard shows full-text instead of numeric pad)

### SpellChecker Deep Findings

- `removeCustomWord()` doesn't trim input but `addCustomWord()` does — asymmetry causes silent removal failure
- Case-sensitive `contains`/`indexOf` but case-insensitive sort — case variants accumulate permanently
- `saveCustomWordsToDisk()` silently fails on file open (void return, no qWarning)
- Cached QRC dictionary never refreshed after app update — stale dictionaries used forever
- `spell()` returns true when no dictionaries loaded — silent no-op failure mode

### QML Animator/Effects

- `ParallelAnimation` mixes `ScaleAnimator` (Animator) with `ColorAnimation` (PropertyAnimation) — Qt forbids mixing; ColorAnimation may silently not run
- `OpacityAnimator.onFinished` doesn't sync property: rendered opacity snaps to old value before visible=false (one-frame flicker)
- Shadow shader uses `Math.cos(180)` / `Math.sin(180)` — expects degrees but JS uses radians (shadow cast at ~233° instead of 180°)

### State Machine & Flow

- `closeDialog.onDiscard` switch missing `RecentLocal`/`RecentRemote` in saveAs path — recent document open silently dropped after save
- Countdown dissolveIn animation restarts `from:0` in Running state → opacity jumps 1→0→1 (visible flicker)
- `overlay.state` set to `ReadRegionOverlay.States.*` but overlay has no `states:` block — dead PropertyChanges
- `flipable.height` bound to `back.implicitWidth` instead of `back.implicitHeight`

---

## Continuous Rotation Stats (Waves 11-26)

| Wave | Clean/8 | Key Finds |
|------|---------|-----------|
| 11 | 0 | Bindings, Loaders, NOTIFY signals, Q_ENUM |
| 12 | 1 | Timer binding loop, const-correctness, state/transition |
| 13 | 3 | Parent-child, countdown timer corruption, spellcheck encoding |
| 14 | 0 | Translation files (68 bugs!), dead code, CMake variables |
| 15 | 3 | Font corruption, Repeater model, shade degrees/radians bug |
| 16 | 4 | Z-index wheel block, explicit/override, focus labels |
| 17 | 6 | QML scope (root undefined), signal handler case, startup flash |
| 18 | 4 | Drag binding breakage (4 sites), Flipable size, include order |
| 19 | 6 | Image smooth/mipmap, QDir mkpath unchecked, QSettings default |
| 20 | 5 | TabBar desync, version macro wrong, debug log levels |
| 21 | 6 | Checkable binding breakage, __hypotenuse multiplier |
| 22 | 6 | Animator mixing, QUrl construction, Action shortcut missing |
| 23 | 5 | iPadOS gaps (17 sites!), size_t narrowing, Flow separator |
| 24 | 5 | hoverEnabled steals, QML ownership, ListView clip missing |
| 25 | 1 | IME hints, signal relay, QStringLiteral efficiency |
| 26 | 1 | Nth-pass still finding: imageRect null, import() UI freeze, etc. |

**Best wave: 6/8 clean (waves 17, 19, 21, 22). Never achieved 8/8 clean, let alone 5 consecutive.**

---

This codebase is exceptionally deep — even 6th-pass re-audits on the most heavily scrutinized files continue to find new bugs. The systemic issues (fragile QML declarative/imperative mix, inconsistent platform abstraction, no thread safety, missing input sanitization) mean that fixing individual bugs without addressing root causes will leave the codebase vulnerable to regression.
