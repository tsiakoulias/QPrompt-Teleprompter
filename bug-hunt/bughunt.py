#!/usr/bin/env python3
"""QPrompt bug-hunt — per-bug tickets, priority backlog, and the agent work loop.

DATA (source of truth, compact, grows by ROWS):
  bugs.csv         canonical index: id,category,severity,title,location
  assessments.csv  long/tidy: id,agent,verdict,confidence,rationale
                   - first 4 fields comma-free; rationale = everything after the 4th comma
                     (no quoting). One reserved agent `STATUS` is unused here (ticket files own status).
  ../BUG-HUNT-ALL-IN-ONE.md  the original report (claim/analysis/impact per id).

GENERATED:
  findings/<ID>.md  one ticket per finding — the WORK UNIT. Embeds the original claim, EVERY
                    agent's verdict+confidence+rationale, the consensus, a Status field, and an
                    empty Patch section. Scaffolded ONCE; thereafter owned/edited by humans+agents
                    (the Patch section + Status line). `scaffold` never overwrites an existing ticket.
  BACKLOG.md        priority-ordered queue of OPEN tickets (regenerated from ticket Status lines).
  REVIEW.md         full 6-agent matrix + divergences (bird's-eye, regenerated from assessments.csv).

PRIORITY (for the backlog / `next`):
  gate  : ticket Status == OPEN  AND  the max-rigor reviewer `opus-4.8-ultra` == LEGIT
  rank  : severity (Critical>High>Medium>Low)  then  corroboration (# of agents calling it LEGIT)

USAGE:
  python bughunt.py scaffold              # create missing tickets + BACKLOG.md + REVIEW.md
  python bughunt.py backlog               # refresh BACKLOG.md from ticket Status lines
  python bughunt.py next                  # print the #1 OPEN actionable ticket (path + body)
  python bughunt.py status <ID> <VALUE> [note]   # set a ticket's Status (OPEN/FIXED/REJECTED/...)
  python bughunt.py add <agent> <csv>     # ingest a new model column into assessments.csv, rebuild
  python bughunt.py review                # rebuild REVIEW.md only
"""
import csv
import re
import sys
from collections import Counter, OrderedDict
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUGS = HERE / "bugs.csv"
ASSESS = HERE / "assessments.csv"
REPORT = HERE.parent / "BUG-HUNT-ALL-IN-ONE.md"
FIND = HERE / "findings"
BACKLOG = HERE / "BACKLOG.md"
REVIEW = HERE / "REVIEW.md"
HDR = "id,agent,verdict,confidence,rationale"
EMOJI = {"LEGIT": "✅", "FALSE": "❌", "PARTIAL": "⚠️", "UNSURE": "❔"}
VERDICTS = set(EMOJI)
SEVW = {"critical": 4, "high": 3, "medium": 2, "low": 1}
GATE = "opus-4.8-ultra"  # the max-rigor reviewer used to triage what enters the work queue
STATUS_RE = re.compile(r"^- \*\*Status:\*\*\s*(\S+)", re.M)


# ---------- data ----------
def read_bugs():
    b = OrderedDict()
    with BUGS.open(encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            b[r["id"].strip()] = {"severity": (r.get("severity") or "").strip(),
                                  "category": (r.get("category") or "").strip(),
                                  "title": (r.get("title") or "").strip(),
                                  "location": (r.get("location") or "").strip()}
    return b


def read_assessments():
    per, agents = {}, []
    if ASSESS.exists():
        for ln in ASSESS.read_text(encoding="utf-8").splitlines():
            if not ln.strip() or ln.startswith("id,agent,"):
                continue
            p = ln.split(",", 4)
            while len(p) < 5:
                p.append("")
            i, a, v, c, r = p[0].strip(), p[1].strip(), p[2].strip(), p[3].strip(), p[4]
            if a == "STATUS":
                continue
            if a not in agents:
                agents.append(a)
            per.setdefault(i, {})[a] = (v, c, r)
    return per, agents


def write_assessments(rows):
    ASSESS.write_text("\n".join([HDR] + [f"{i},{a},{v},{c},{r}" for i, a, v, c, r in rows]) + "\n",
                      encoding="utf-8")


def read_report_blocks():
    blocks = {}
    if not REPORT.exists():
        return blocks
    cur, buf = None, []
    for ln in REPORT.read_text(encoding="utf-8", errors="replace").splitlines():
        m = re.match(r"^###\s+\[([A-Z0-9][A-Z0-9-]*)\]\s*(.*)$", ln)
        if m or ln.startswith("## "):
            if cur:
                blocks[cur] = "\n".join(buf).strip()
            cur, buf = (m.group(1) if m else None), []
            continue
        if cur:
            buf.append(ln)
    if cur:
        blocks[cur] = "\n".join(buf).strip()
    return blocks


def sevw(s):
    return SEVW.get((s or "").split()[0].lower() if s else "", 0)


def consensus(verds):
    vs = [v for v in verds if v in VERDICTS]
    if len(vs) < 2:
        return ""
    s = set(vs)
    if len(s) == 1:
        return "AGREE"
    if "LEGIT" in s and "FALSE" in s:
        return "CONFLICT"
    return "split"


def default_status(per_id):
    g = per_id.get(GATE, ("", "", ""))[0]
    return {"LEGIT": "OPEN", "PARTIAL": "OPEN", "FALSE": "REJECTED", "UNSURE": "NEEDS-INFO"}.get(g, "OPEN")


# ---------- tickets ----------
def ticket_body(bid, b, per, agents, blocks, status):
    legit = sum(per.get(bid, {}).get(a, ("",))[0] == "LEGIT" for a in agents)
    con = consensus([per.get(bid, {}).get(a, ("",))[0] for a in agents])
    out = [f"# [{bid}] {b['title']}", "",
           f"- **Status:** {status}",
           f"- **Severity:** {b['severity']}",
           f"- **Category:** {b['category']}",
           f"- **Location:** `{b['location']}`",
           f"- **Consensus:** {legit}/{len(agents)} agents LEGIT · {con or 'n/a'}", "",
           "## Original report claim", "",
           blocks.get(bid, "_(no matching block in BUG-HUNT-ALL-IN-ONE.md)_"), "",
           "## Agent assessments", "",
           "| Agent | Verdict | Conf | Rationale |", "|---|---|---|---|"]
    for a in agents:
        t = per.get(bid, {}).get(a)
        if t and t[0]:
            out.append(f"| {a} | {EMOJI.get(t[0], t[0])} {t[0]} | {t[1]} | {t[2].replace('|', chr(92)+'|')} |")
        else:
            out.append(f"| {a} | · | | not assessed |")
    out += ["",
            "## Patch  _(fill when fixing)_", "",
            "- **Root cause:**", "- **Fix:**", "- **Files changed:**",
            "- **Verification:**", "- **Commit / PR:**", ""]
    return "\n".join(out) + "\n"


def scaffold():
    FIND.mkdir(exist_ok=True)
    b = read_bugs()
    per, agents = read_assessments()
    blocks = read_report_blocks()
    created = 0
    for bid, meta in b.items():
        p = FIND / f"{bid}.md"
        if p.exists():
            continue
        p.write_text(ticket_body(bid, meta, per, agents, blocks,
                                 default_status(per.get(bid, {}))), encoding="utf-8")
        created += 1
    print(f"scaffold: {created} new tickets ({len(b)} total) · agents: {', '.join(agents)}")
    build_review()
    backlog()


def ticket_status(p):
    m = STATUS_RE.search(p.read_text(encoding="utf-8"))
    return (m.group(1) if m else "OPEN").upper()


def backlog():
    b = read_bugs()
    per, agents = read_assessments()
    rows = []
    counts = Counter()
    for bid, meta in b.items():
        p = FIND / f"{bid}.md"
        if not p.exists():
            continue
        st = ticket_status(p)
        counts[st] += 1
        g = per.get(bid, {}).get(GATE, ("", "", ""))[0]
        legit = sum(per.get(bid, {}).get(a, ("",))[0] == "LEGIT" for a in agents)
        rows.append({"id": bid, "sev": meta["severity"], "title": meta["title"],
                     "status": st, "gate": g, "legit": legit, "sw": sevw(meta["severity"])})
    actionable = [r for r in rows if r["status"] == "OPEN" and r["gate"] == "LEGIT"]
    actionable.sort(key=lambda r: (-r["sw"], -r["legit"], r["id"]))
    out = ["# Bug-Hunt Backlog", "",
           f"Work queue: OPEN tickets the max-rigor reviewer (`{GATE}`) confirms as LEGIT, "
           "ranked by severity then corroboration (number of the 6 agents that also called it LEGIT). "
           "Each row links to its full ticket in `findings/`.", "",
           f"Status tally: " + " · ".join(f"{k} {counts[k]}" for k in sorted(counts)) + ".", "",
           f"**{len(actionable)} actionable OPEN findings.**", "",
           "| # | Sev | Corrob. | ID | Title |", "|---|---|---|---|---|"]
    for n, r in enumerate(actionable, 1):
        out.append(f"| {n} | {r['sev']} | {r['legit']}/{len(agents)} | "
                   f"[{r['id']}](findings/{r['id']}.md) | {r['title'].replace('|', chr(92)+'|')} |")
    # also list the non-actionable buckets so nothing is hidden
    for label, pred in [("Minor / non-behavioral (opus-4.8-ultra = PARTIAL)", lambda r: r["gate"] == "PARTIAL"),
                        ("Rejected (opus-4.8-ultra = FALSE)", lambda r: r["gate"] == "FALSE"),
                        ("Needs info (opus-4.8-ultra = UNSURE)", lambda r: r["gate"] == "UNSURE"),
                        ("Done", lambda r: r["status"] in ("FIXED", "WONTFIX"))]:
        ids = [r["id"] for r in rows if pred(r) and r["status"] not in ("FIXED", "WONTFIX")] \
            if "Done" not in label else [r["id"] for r in rows if r["status"] in ("FIXED", "WONTFIX")]
        if ids:
            out += ["", f"<details><summary>{label} — {len(ids)}</summary>", "",
                    ", ".join(f"[{i}](findings/{i}.md)" for i in ids), "", "</details>"]
    BACKLOG.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"backlog: {len(actionable)} actionable OPEN · tally {dict(counts)}")


def audit():
    """Second-chance queue: REJECTED / NEEDS-INFO tickets, ranked by how CONTESTED the rejection
    is (how many of the other agents called it LEGIT) then severity. Re-examine each against the
    code; promote a wrongly-rejected one with `status <ID> OPEN`, or confirm it (`WONTFIX`)."""
    b = read_bugs()
    per, agents = read_assessments()
    rows = []
    for bid, meta in b.items():
        p = FIND / f"{bid}.md"
        if not p.exists():
            continue
        st = ticket_status(p)
        if st not in ("REJECTED", "NEEDS-INFO"):
            continue
        legit = sum(per.get(bid, {}).get(a, ("",))[0] == "LEGIT" for a in agents)
        rows.append((st, legit, sevw(meta["severity"]), bid, meta))
    rows.sort(key=lambda r: (-r[1], -r[2], r[3]))
    print(f"# Audit queue — {len(rows)} rejected / needs-info findings (every bug gets a second look)")
    print("# ranked by CONTESTEDNESS: how many of the 6 agents disagreed with the rejection.")
    print("# promote a wrongly-rejected one:  python bughunt.py status <ID> OPEN")
    print("# confirm a rejection:             python bughunt.py status <ID> WONTFIX\n")
    print(f"{'STATUS':<11} {'LEGIT/6':<8} {'SEV':<9} ID")
    for st, legit, sw, bid, meta in rows:
        flag = "  <-- contested" if (st == "REJECTED" and legit >= 1) else ""
        print(f"{st:<11} {str(legit)+'/'+str(len(agents)):<8} {meta['severity'][:8]:<9} {bid}{flag}")


def next_bug():
    b = read_bugs()
    per, agents = read_assessments()
    cand = []
    for bid, meta in b.items():
        p = FIND / f"{bid}.md"
        if not p.exists() or ticket_status(p) != "OPEN":
            continue
        if per.get(bid, {}).get(GATE, ("", "", ""))[0] != "LEGIT":
            continue
        legit = sum(per.get(bid, {}).get(a, ("",))[0] == "LEGIT" for a in agents)
        cand.append((-sevw(meta["severity"]), -legit, bid))
    if not cand:
        print("No OPEN actionable findings. 🎉")
        return
    cand.sort()
    top = cand[0][2]
    p = FIND / f"{top}.md"
    print(f"=== NEXT: {p.relative_to(HERE.parent)} ===\n")
    print(p.read_text(encoding="utf-8"))


def set_status(bid, value, note):
    p = FIND / f"{bid}.md"
    if not p.exists():
        print(f"no ticket findings/{bid}.md")
        return
    txt = p.read_text(encoding="utf-8")
    repl = f"- **Status:** {value.upper()}" + (f"  ({note})" if note else "")
    txt2 = re.sub(r"^- \*\*Status:\*\*.*$", repl, txt, count=1, flags=re.M)
    p.write_text(txt2, encoding="utf-8")
    print(f"{bid} -> {value.upper()}")
    backlog()


def add_agent(name, path):
    b = read_bugs()
    rows = [(i, a, v, c, r) for ln in (ASSESS.read_text(encoding="utf-8").splitlines() if ASSESS.exists() else [])
            if not ln.startswith("id,agent,") and ln.strip()
            for (i, a, v, c, r) in [(lambda p: (p+[''] * (5-len(p)))[:5])(ln.split(",", 4))]]
    have = {(i, a) for i, a, *_ in rows}
    new, added, skip = [], 0, 0
    for r in csv.DictReader(open(path, encoding="utf-8")):
        i = (r.get("id") or "").strip()
        if i not in b or (i, name) in have:
            skip += 1
            continue
        new.append((i, name, (r.get("verdict") or "").strip().upper(),
                    (r.get("confidence") or "").strip(),
                    (r.get("rationale") or "").strip().replace("\n", " ")))
        added += 1
    write_assessments(rows + new)
    print(f"ingested '{name}': +{added} (skipped {skip}). Re-run `scaffold` is NOT auto (tickets are not "
          f"regenerated, to preserve patch notes); run `review` for the matrix.")
    build_review()


def build_review():
    b = read_bugs()
    per, agents = read_assessments()
    dist = {a: Counter() for a in agents}
    con = Counter()
    for bid in b:
        for a in agents:
            v = per.get(bid, {}).get(a, ("",))[0]
            if v:
                dist[a][v] += 1
        con[consensus([per.get(bid, {}).get(a, ("",))[0] for a in agents]) or "n/a"] += 1
    def cell(t):
        return f"{EMOJI.get(t[0], t[0])}{t[1]}" if t and t[0] else "·"
    out = ["# Multi-Agent Bug Review — QPrompt", "",
           f"_{len(b)} findings · agents: {', '.join(agents)}_", "",
           "Bird's-eye matrix + divergences. Per-bug detail (incl. each agent's full rationale, the "
           "original claim, and the patch workspace) lives in `findings/<ID>.md`; the work queue is "
           "`BACKLOG.md`.", "", "## Summary", "",
           "| Agent | " + " | ".join(sorted(VERDICTS)) + " |", "|---|" + "---|" * len(VERDICTS)]
    for a in agents:
        out.append(f"| {a} | " + " | ".join(str(dist[a][v]) for v in sorted(VERDICTS)) + " |")
    out += ["", f"**Consensus** ({len(agents)} agents): "
            + " · ".join(f"{k} {con[k]}" for k in ("AGREE", "split", "CONFLICT") if con.get(k)), "",
            "## Matrix", "",
            "| ID | Sev | " + " | ".join(agents) + " | Consensus | Title |",
            "|---|---|" + "---|" * len(agents) + "---|---|"]
    for bid, meta in b.items():
        verds = [per.get(bid, {}).get(a, ("",))[0] for a in agents]
        c = consensus(verds)
        out.append(f"| {bid} | {meta['severity']} | " + " | ".join(cell(per.get(bid, {}).get(a)) for a in agents)
                   + f" | {'**CONFLICT**' if c=='CONFLICT' else c} | {meta['title'].replace('|', chr(92)+'|')} |")
    REVIEW.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"review: {len(b)} rows · {', '.join(agents)} · AGREE {con.get('AGREE',0)} "
          f"split {con.get('split',0)} CONFLICT {con.get('CONFLICT',0)}")


if __name__ == "__main__":
    a = sys.argv[1:] or ["next"]
    cmd = a[0]
    if cmd == "scaffold":
        scaffold()
    elif cmd == "backlog":
        backlog()
    elif cmd == "next":
        next_bug()
    elif cmd == "audit":
        audit()
    elif cmd == "review":
        build_review()
    elif cmd == "status" and len(a) >= 3:
        set_status(a[1], a[2], " ".join(a[3:]))
    elif cmd == "add" and len(a) == 3:
        add_agent(a[1], a[2])
    else:
        print(__doc__)
        sys.exit(1)
