# [SEC-04] SSRF / URL Injection — User-Controlled URL Passed to Network Loader

- **Status:** OPEN
- **Severity:** High
- **Category:** 
- **Location:** `src/documenthandler.cpp:867-886, src/kirigami_ui/PrompterPage.qml:1277-1291`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

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

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 55 | user-initiated load; SSRF framing weak but host/path bug real (documenthandler.cpp:873) |
| gpt | ⚠️ PARTIAL | 58 | observed SSRF / URL Injection - User-Controlled URL Passed to Network Loader (src/documenthandler.cpp:867) |
| deepseek | ✅ LEGIT | 85 | Relative URL path becomes host at doc.cpp:873; user-supplied URL like 'localhost:4455' -> HTTP GET to internal service — genuine SSRF vector |
| glm | ✅ LEGIT | 85 | documenthandler.cpp:867-886 loadFromNetwork takes user-controlled URL and passes it to QNetworkAccessManager without validation |
| kimi | ✅ LEGIT | 90 | documenthandler.cpp:867-886 treats relative URL host as url.path() allowing requests to internal IPs; no whitelist. |
| opus-ultra | ⚠️ PARTIAL | 50 | max: real but non-behavioral (style/arch/non-issue) — user-initiated load; SSRF framing weak but host/path bug real (documenthandler.cpp:873) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

