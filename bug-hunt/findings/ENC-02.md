# [ENC-02] getMarkerKey() mid(4) without length/startsWith guard

- **Status:** OPEN
- **Severity:** Low
- **Category:** 
- **Location:** `documenthandler.cpp:756`
- **Consensus:** 6/6 agents LEGIT · AGREE

## Original report claim

- **File:** documenthandler.cpp:756
- **Severity:** Low
- **Analysis:** Unlike parse() which guards mid(4) with startsWith("key_"), getMarkerKey() blindly takes mid(4) from first anchor name. Anchor names <4 chars or without "key_" prefix produce garbage key codes.
- **Impact:** Malformed anchor names silently produce wrong marker key display.

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ✅ LEGIT | 55 | names.first().mid(4) assumes key_ prefix; only !isEmpty guarded (documenthandler.cpp:756) |
| gpt | ✅ LEGIT | 78 | getMarkerKey() mid(4) without length/startsWith guard (src/documenthandler.cpp:756) |
| deepseek | ✅ LEGIT | 85 | mid(4) without startsWith('key_') guard; anchor names <4 chars or no prefix->garbage key (documenthandler.cpp:756) |
| glm | ✅ LEGIT | 80 | documenthandler.cpp:756 mid(4) without length/startsWith guard on anchor name; assumes 'key_' prefix |
| kimi | ✅ LEGIT | 90 | documenthandler.cpp:756 calls names.first().mid(4) without checking length or startsWith(\key_\") |
| opus-ultra | ✅ LEGIT | 55 | names.first().mid(4) assumes key_ prefix; only !isEmpty guarded (documenthandler.cpp:756) |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

