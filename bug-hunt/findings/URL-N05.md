# [URL-N05] openFromRemote() blindly prepends http:// to non-HTTP schemes

- **Status:** OPEN
- **Severity:** Medium
- **Category:** 
- **Location:** `PrompterPage.qml:1279-1282`
- **Consensus:** 5/6 agents LEGIT · split

## Original report claim

- **File:** PrompterPage.qml:1279-1282
- **Severity:** Medium
- **Analysis:** Any URL not starting with http:// or https:// gets http:// prepended. `file:///path` becomes `http://file:///path`. Case variants like `HTTP://` not handled.
- **Impact:** Silently broken behavior when pasting file:// or other-scheme URLs.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 55 | openFromRemote blindly prepends http:// to non-HTTP schemes (PrompterPage.qml:1279) |
| gpt | ⚠️ PARTIAL | 58 | observed openFromRemote() blindly prepends http:// to non-HTTP schemes (src/kirigami_ui/PrompterPage.qml:1279) |
| deepseek | ✅ LEGIT | 90 | PrompterPage.qml:1279-1282: any URL not starting http:// or https:// gets http:// prepended; file:// becomes http://file:// case variants like HTTP:// missed |
| glm | ✅ LEGIT | 80 | PrompterPage.qml:1279-1282 openFromRemote() blindly prepends http:// to non-HTTP schemes |
| kimi | ✅ LEGIT | 85 | PrompterPage.qml:1279-1282 prepends 'http://' to any URL not starting with http/https, breaking file:// and other schemes. |
| opus-ultra | ✅ LEGIT | 55 | openFromRemote blindly prepends http:// to non-HTTP schemes (PrompterPage.qml:1279) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

