# bug-hunt — multi-agent bug backlog for QPrompt

This directory is a triaged backlog of **723 candidate bugs** in the QPrompt source, each
independently reviewed by **6 AI agents** (opus, opus-ultra, gpt, deepseek, glm, kimi) and turned
into a self-contained, patch-ready ticket.

> **Fixing bugs?** Read [`FIX-AGENT.md`](FIX-AGENT.md) — the operating brief (standards, the
> verify-first rule, the fix protocol). It's the one file to hand a coding agent.

## If you are an agent asked to "find the most important bug and patch it"

1. Run:
   ```
   python bug-hunt/bughunt.py next
   ```
   It prints the single highest-priority **OPEN** finding that the strictest reviewer
   (`opus-ultra`) confirms is a real bug — as a complete work order: the original claim, the exact
   `file:line`, and all six agents' verdicts + rationales. You do **not** need to re-derive anything.
   (Prefer a glanceable list? Open [`BACKLOG.md`](BACKLOG.md) — same ranking, with links.)

2. Open that finding's ticket: `bug-hunt/findings/<ID>.md`. Read the original claim and the agent
   assessments. **Verify it against the live code yourself before changing anything** — agents
   disagree, and even the queue can be wrong.

3. Patch the code. Then record what you did in the ticket's `## Patch` section
   (root cause, fix, files changed, verification, commit), and mark it done:
   ```
   python bug-hunt/bughunt.py status <ID> FIXED "what you changed / commit sha"
   ```
   That drops it out of the queue. Then go back to step 1 for the next one.

## Priority model (how "most important" is decided)
- **Gate:** only findings where the max-rigor reviewer `opus-ultra` = **LEGIT** and Status = **OPEN**
  enter the queue. This excludes the report's false positives (the credulous models accept many;
  `opus-ultra` rejected **70** as not-real and flagged **63** as unverifiable).
- **Rank:** severity (Critical → Low), then **corroboration** = how many of the 6 agents also called
  it LEGIT. So #1 is the highest-severity, most-agreed, rigor-confirmed, still-open bug.

## Nothing is buried — every finding gets a second chance
The gate keeps the *fix queue* high-precision, but `opus-ultra` is a single reviewer and can be wrong
to reject. So rejected/uncertain findings are not dropped — they go to a **second-look queue**:
```
python bug-hunt/bughunt.py audit
```
It lists the **REJECTED** and **NEEDS-INFO** tickets ranked by how *contested* the rejection is (how
many of the 6 agents disagreed). Re-check each against the code, then either:
- promote a wrongly-rejected real bug back into the fix queue: `bughunt.py status <ID> OPEN`, or
- confirm the rejection: `bughunt.py status <ID> WONTFIX`.

(All 723 tickets also exist on disk regardless of status — you can open and patch any `findings/<ID>.md`
directly at any time.)

## What's here
| Path | What it is |
|---|---|
| `findings/<ID>.md` | one **ticket per bug** — original claim + every agent's verdict/confidence/rationale + consensus + Status + a Patch section. The work unit. |
| `BACKLOG.md` | priority-ordered queue of actionable OPEN tickets (regenerated from ticket Status). |
| `REVIEW.md` | bird's-eye 6-agent matrix + divergences. |
| `assessments.csv` | source-of-truth data, long format `id,agent,verdict,confidence,rationale` (rationale = everything after the 4th comma; grows by rows). |
| `bugs.csv` | canonical index of the 723 findings. |
| `bughunt.py` | the tool (`next`, `status`, `backlog`, `scaffold`, `review`, `add`). |
| `PROMPT-TEMPLATE.md` | the blinded prompt to add another reviewer column later. |

## Statuses
`OPEN` (to do) · `FIXED` · `WONTFIX` · `REJECTED` (opus-ultra says not a real bug) ·
`NEEDS-INFO` (opus-ultra unsure / needs runtime or language verification).

## Maintenance
- Re-rank the queue after marking fixes: `python bug-hunt/bughunt.py backlog`
- Add a 7th reviewer (or a re-verification round): feed `PROMPT-TEMPLATE.md` + `bugs.csv` to the
  model, then `python bug-hunt/bughunt.py add <name> <its-output.csv>`. Existing tickets are **not**
  regenerated (so patch notes are preserved); `REVIEW.md` refreshes.

## Caveat
These are AI-generated assessments. The queue is a strong prior, not ground truth. Always confirm a
finding against the current code before patching, and prefer the corroborated, high-severity ones.
