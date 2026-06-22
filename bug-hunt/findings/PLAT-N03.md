# [PLAT-N03] Zero Q_OS_TVOS preprocessor guards in C++ despite 19 QML references — build failure

- **Status:** NEEDS-INFO
- **Severity:** High
- **Category:** 
- **Location:** `All .cpp/.h/.mm (zero Q_OS_TVOS); 19 QML references to "tvos"`
- **Consensus:** 2/6 agents LEGIT · CONFLICT

## Original report claim

- **Files:** All .cpp/.h/.mm (zero Q_OS_TVOS); 19 QML references to "tvos"
- **Severity:** High
- **Analysis:** Qt 6: Q_OS_TVOS is exclusive of Q_OS_IOS. Every C++ guard checks Q_OS_IOS but never Q_OS_TVOS. On tvOS: includes QApplication/QtWidgets (build error), skips Kirigami static registration (blank window), uses wrong QSettings path, includes SystemFontChooserDialog (QDialog — build error on tvOS).
- **Impact:** tvOS build fails at multiple points. QML references suggest tvOS was considered but C++ backend never implemented.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❔ UNSURE | 45 | Q_OS_TVOS C++ guard gap vs QML refs; tvOS not a shipping target (multi-file) |
| gpt | ❔ UNSURE | 39 | tvOS support is unclear; QML strings alone do not prove C++ build failure (src/kirigami_ui/main.qml:45) |
| deepseek | ❌ FALSE | 80 | tvOS is not a shipping target in CMake; no C++ guards needed for unsupported platform |
| glm | ✅ LEGIT | 80 | Zero Q_OS_TVOS preprocessor guards in C++ despite QML references to tvos; build may fail for tvOS |
| kimi | ✅ LEGIT | 90 | No Q_OS_TVOS appears in any C++ source; main.cpp:23 and documenthandler.h QtWidgets-style guards use only Q_OS_IOS, so a tvOS build would pull in QApplication/QtWidgets and fail. |
| opus-ultra | ❔ UNSURE | 45 | max: unverifiable statically (runtime/semantic) — Q_OS_TVOS C++ guard gap vs QML refs; tvOS not a shipping target (multi-file) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

