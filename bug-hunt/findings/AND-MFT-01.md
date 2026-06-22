# [AND-MFT-01] FileProvider resource @xml/qtprovider_paths — file named filepaths.xml

- **Status:** OPEN
- **Severity:** Medium (latent)
- **Category:** 
- **Location:** `AndroidManifest.xml:43 vs res/xml/filepaths.xml`
- **Consensus:** 3/6 agents LEGIT · split

## Original report claim

- **File:** AndroidManifest.xml:43 vs res/xml/filepaths.xml
- **Severity:** Medium (latent)
- **Analysis:** Commented-out FileProvider references qtprovider_paths but actual file is filepaths.xml. Resource-not-found if uncommented.
- **Impact:** Build error if FileProvider block ever activated.

---

## Agent assessments

| Agent | Verdict | Conf | Rationale |
|---|---|---|---|
| opus | ⚠️ PARTIAL | 45 | FileProvider @xml/qtprovider_paths vs filepaths.xml; needs res check (AndroidManifest.xml:43) |
| gpt | ⚠️ PARTIAL | 58 | observed FileProvider resource @xml/qtproviderpaths - file named filepaths.xml (android/AndroidManifest.xml:43) |
| deepseek | ✅ LEGIT | 85 | commented FileProvider refs @xml/qtprovider_paths but actual file is filepaths.xml; resource-not-found if activated (AndroidManifest.xml:43) |
| glm | ⚠️ PARTIAL | 65 | AndroidManifest.xml:43 FileProvider references @xml/qtprovider_paths but file is named filepaths.xml. However FileProvider is commented out. |
| kimi | ✅ LEGIT | 75 | AndroidManifest.xml:43 (commented) references @xml/qtprovider_paths while res/xml/filepaths.xml is the actual file; latent mismatch. |
| opus-ultra | ✅ LEGIT | 68 | max: real defect; severity is a separate axis (was PARTIAL) — FileProvider @xml/qtprovider_paths vs filepaths.xml; needs res check (AndroidManifest.xml: |

## Patch  _(fill when fixing)_

- **Root cause:**
- **Fix:**
- **Files changed:**
- **Verification:**
- **Commit / PR:**

