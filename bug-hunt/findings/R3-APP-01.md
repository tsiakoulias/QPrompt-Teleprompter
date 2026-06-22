# [R3-APP-01] AppController singleton and children never deallocated

- **Status:** REJECTED
- **Severity:** Low
- **Category:** Memory Management
- **Location:** `src/appcontroller.cpp:35,25-28`
- **Consensus:** 1/6 agents LEGIT · CONFLICT

## Original report claim

- **File:** src/appcontroller.cpp:35,25-28
- **Severity:** Low
- **Category:** Memory Management
- **Analysis:** new AppController() with no parent. m_hotkeys and m_wasm parented to this, entire tree leaks. QQmlEngine::setObjectOwnership(this, CppOwnership) prevents QML engine cleanup.
- **Impact:** Memory leak on shutdown. Application-lifetime singleton conventionally acceptable but masks real leaks.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ❌ FALSE | 75 | app-lifetime singleton; report admits acceptable (appcontroller.cpp:35) |
| gpt | ❌ FALSE | 76 | the singleton is process-lifetime, so this is not an app bug (src/appcontroller.cpp:35) |
| deepseek | ❌ FALSE | 85 | appcontroller.cpp:35 static auto singleton=new AppController() — intentional application-lifetime singleton; OS reclaims on process exit not a leak |
| glm | ⚠️ PARTIAL | 60 | appcontroller.cpp:35 singleton new AppController() never deleted; benign for app-lifetime singleton |
| kimi | ✅ LEGIT | 80 | appcontroller.cpp:35 allocates static AppController singleton and returns it; the object is never deleted, leaking its heap-allocated children too. |
| opus-ultra | ❌ FALSE | 75 | app-lifetime singleton; report admits acceptable (appcontroller.cpp:35) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

