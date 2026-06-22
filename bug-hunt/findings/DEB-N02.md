# [DEB-N02] qml6-module-qtcore is not a real Debian package — .deb uninstallable

- **Status:** NEEDS-INFO
- **Severity:** High
- **Category:** 
- **Location:** `CMakeLists.txt:446`
- **Consensus:** 3/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** CMakeLists.txt:446
- **Severity:** High
- **Analysis:** QtCore has no QML module. Correct name is qml6-module-qtqml. apt cannot resolve.
- **Impact:** DEB package uninstallable — dependency resolution fails.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❔ UNSURE | 45 | qml6-module-qtcore package-existence claim; Debian-specific (CMakeLists.txt:446) |
| gpt | ✅ LEGIT | 84 | qml6-module-qtcore is not a real Debian package - .deb uninstallable (CMakeLists.txt:446) |
| deepseek | ✅ LEGIT | 95 | CMakeLists.txt:446: qml6-module-qtcore not a real Debian package; QtCore has no QML module; apt resolution fails |
| glm | ✅ LEGIT | 80 | CMakeLists.txt:446 qml6-module-qtcore is not a real Debian package; .deb uninstallable |
| kimi | ❌ FALSE | 90 | qml6-module-qtcore exists in Ubuntu/Debian Qt6 (qt6-declarative); the package name is real |
| opus-ultra | ❔ UNSURE | 45 | max: unverifiable statically (runtime/semantic) — qml6-module-qtcore package-existence claim; Debian-specific (CMakeLists.txt:446) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

