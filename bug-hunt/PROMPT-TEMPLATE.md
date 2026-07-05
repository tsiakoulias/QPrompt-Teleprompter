# Per-agent assessment prompt (paste VERBATIM to each model)

One model = one column. Give every model the **same** prompt + `bugs.csv` + repo access.
After it returns its CSV, ingest it with:

```
python multi-agent/build_review.py add <agent-name> <returned-file.csv>
```

(e.g. `add glm-5.2-xhigh`, `add kimi-k2.7-code`, `add opus-r2` for a re-verification round). That stamps the
agent name, appends rows to `assessments.csv`, and rebuilds `REVIEW.md`. Adding a column
never rewrites existing data — it only appends rows.

---

You are auditing a 723-item bug report against the QPrompt teleprompter codebase
(Qt 6 / QML / C++). For EVERY finding, independently decide whether the reported bug is
real — by reading the actual source yourself, not by trusting the report.

## HARD CONSTRAINT — INDEPENDENCE (read first)
Do NOT open, read, grep, or reference ANY of these, even though they exist in the repo:
  multi-agent/assessments.csv, multi-agent/assess-*.csv, multi-agent/REVIEW.md,
  multi-agent/MULTI-AGENT-*.md, BUG-HUNT-VERDICT.md, or any file containing pre-existing
  verdicts, confidence numbers, or rationales.
If you encounter one, ignore it entirely. Derive every verdict, confidence number, and
rationale yourself, from the SOURCE CODE only. Use your own confidence scale and your own
wording. A result that closely matches a pre-existing assessment will be treated as a failed run.

## INPUTS (read from the checked-out repository)
- multi-agent/bugs.csv     — the authoritative list of findings. Columns: id, category,
                             severity, title, location. Use these ids EXACTLY; assess all 723.
- BUG-HUNT-ALL-IN-ONE.md   — the original report text (claim + analysis) for each id.
- src/, CMakeLists.txt, src/CMakeLists.txt, android/, cmake/, *.ts — the code to verify against.

## FOR EACH id IN bugs.csv
1. Open the cited `location` (file:line) in the actual source and inspect it yourself.
2. Read the matching `### [id]` entry in BUG-HUNT-ALL-IN-ONE.md only to learn the claim.
3. Decide whether the bug is real AS DESCRIBED, from your own reading of the code.
   The report is frequently wrong or overstated — verify, don't parrot.

## VERIFY, DON'T PARROT — check these yourself before accepting any claim
- The Qt build TARGET (CMakeLists.txt QT_MIN_VERSION), NOT the `import X 6.5` line — a versioned
  import is a minimum API level, not the target. Don't accept "version mismatch" without this.
- Whether an "undefined" QML id resolves via the QML context hierarchy (unqualified ids like
  prompter/viewport/pointerSettings can come from an ancestor file) — trace the instantiation chain.
- Both the .cpp AND the .mm for platform-split classes before claiming "never implemented".
- Reachability/impact of Q_UNREACHABLE, Q_ASSERT, raw new in app-lifetime singletons, RAII
  flush-on-destroy, and default function args — these are often correct or benign.
- Distinguish a genuine defect from a real-but-trivial observation (z-order, focus policy,
  hardcoded sizes, missing smooth:true, cosmetic naming) — grade impact honestly.
- For .ts translation findings, mark SEMANTIC (wrong-word) claims UNSURE unless you can verify
  the language; only grade STRUCTURAL ones (wrong locale code, broken %/&amp; placeholders).

## OUTPUT — STRICT, one line per id
Output ONLY CSV, no prose, no fences, with this header line first:
    id,verdict,confidence,rationale
- verdict ∈ LEGIT | FALSE | PARTIAL | UNSURE
    LEGIT   = real bug as described.
    FALSE   = claim or its analysis is wrong / not a real defect.
    PARTIAL = real observation but impact overstated / only partly right / right symptom, wrong cause.
    UNSURE  = cannot determine from code inspection (needs runtime / language / missing context).
- confidence = integer 0–100 (your own scale).
- rationale = the LAST field: free text, MUST cite a file:line. It may contain commas and
  parentheses — do NOT wrap it in quotes and do NOT use commas anywhere in the first three
  fields. (Everything after the 4th comma on the line is the rationale.) Keep it on ONE line.

## COMPLETENESS MANDATE (do not skip anything)
- Exactly ONE row for EVERY id in bugs.csv — all 723, each id exactly once.
- Do NOT summarize, group, or write "remaining are similar". Every id gets its own verified row.
- If too long for one message, continue in further messages until every id is covered. Do not stop early.
- End with a final separate line:  DONE: <N> rows  (N must equal the id count). Self-check that
  every id appears once and fix omissions/duplicates before declaring DONE.
