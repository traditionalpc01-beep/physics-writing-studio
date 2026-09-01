#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""distill_physics_corpus.py - deterministic distillation of a physics/QLED corpus into v3-style TSV increments.

Companion to run 1 of the physics_optoelectronics register (see knowledge/domain_metrics_physics.tsv
and the Domain Register Notes in prompts/system_writer.txt).

Usage:
    python distill_physics_corpus.py --corpus <dir> --out <dir> [--min-count 3]

Corpus expectations:
    - one plain-text (.txt or .md) Nature-family PUBLISHED paper per file (not arXiv preprints:
      the point is post-editorial style);
    - UTF-8; section headers on their own line (Abstract, Introduction, Results, Discussion,
      Methods, and common variants such as 'Results and discussion').

Outputs (append-ready increments, evidence value: distilled_physics):
    opener_distribution_increment.tsv      section / opener_3gram / count
    gap_transitions_increment.tsv          section / pivot_word / template
    hedge_verbs_increment.tsv              verb / tier / count
    cross_section_linkers_increment.tsv    from_section / to_section / pattern
    results_discussion_openers_increment.tsv  section / opener_template / count

Merge policy: keep only rows with count >= --min-count, then hand-merge into the live TSVs in
knowledge/ after spot-checking quotes against the source files (the original pipeline used
LCS-based quote validation, ratio >= 0.5; re-verify anything you promote).
"""
from __future__ import annotations
import argparse
import re
import sys
from collections import Counter
from pathlib import Path

SECTION_PAT = re.compile(
    r"^(#{1,3}\s*)?(abstract|introduction|results?( and discussion)?|discussion|methods?|materials and methods|"
    r"experimental( section| procedures)?|conclusions?)\s*:?\s*$",
    re.IGNORECASE,
)
SECTION_ALIASES = {
    "results and discussion": "results",
    "materials and methods": "methods",
    "experimental": "methods",
    "experimental section": "methods",
    "experimental procedures": "methods",
    "conclusion": "discussion",
    "conclusions": "discussion",
}
PIVOTS = ("however", "but", "yet", "while", "although", "whereas", "despite", "nevertheless")
HEDGE_TIERS = {
    "causal": ("show", "shows", "showed", "demonstrate", "demonstrates", "demonstrated",
               "establish", "established", "identify", "identified", "report", "reported",
               "achieve", "achieved", "realize", "realized", "confirm", "confirmed"),
    "associative": ("suggest", "suggests", "suggested", "indicate", "indicates", "indicated",
                    "support", "supports", "supported", "consistent", "agree", "agrees",
                    "accord", "accords"),
    "speculative": ("may", "could", "might", "appears", "appear", "seems", "seem", "possibly"),
}
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z])")


def split_sections(text: str) -> dict[str, list[str]]:
    """Return {section: [sentence, ...]} using the last header seen above each paragraph."""
    sections: dict[str, list[str]] = {}
    current = "front"
    for line in text.splitlines():
        m = SECTION_PAT.match(line.strip())
        if m:
            name = m.group(2).lower()
            current = SECTION_ALIASES.get(name, name)
            sections.setdefault(current, [])
            continue
        if line.strip():
            for sent in SENT_SPLIT.split(line.strip()):
                sent = sent.strip()
                if len(sent.split()) >= 4:
                    sections.setdefault(current, []).append(sent)
    return sections


def words(sent: str) -> list[str]:
    return [w.strip(",;:()").lower() for w in sent.split() if w.strip(",;:()")]


def templatize(sent: str) -> str:
    """Mask volatile tokens so near-duplicate gap sentences collapse to one template."""
    t = re.sub(r"\d+\.?\d*", "#", sent)
    t = re.sub(r"#\s*%", "#%", t)
    return t


def distill(sections: dict[str, list[str]]):
    openers, gaps, hedges, linkers, rd_openers = Counter(), [], Counter(), [], Counter()
    prev_section = None
    for sec, sents in sections.items():
        for i, sent in enumerate(sents):
            ws = words(sent)
            if len(ws) >= 3:
                openers[(sec, " ".join(ws[:3]))] += 1
            if sec in ("results", "discussion") and len(ws) >= 5:
                rd_openers[(sec, " ".join(ws[:5]))] += 1
            low = sent.lower()
            for pivot in PIVOTS:
                if re.search(rf"\b{pivot}\b", low):
                    gaps.append((sec, pivot, templatize(sent)))
                    break
            for tier, verbs in HEDGE_TIERS.items():
                if any(re.search(rf"\b{v}\b", low) for v in verbs):
                    hit = next(v for v in verbs if re.search(rf"\b{v}\b", low))
                    hedges[(hit, tier)] += 1
            if i == 0 and prev_section is not None:
                linkers.append((prev_section, sec, templatize(sent)))
        if sents:
            prev_section = sec
    return openers, gaps, hedges, linkers, rd_openers


def write_tsv(path: Path, header: list[str], rows: list[list]):
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write("\t".join(header) + "\n")
        for row in rows:
            cells = [str(c).replace("\t", " ") for c in row]
            f.write("\t".join(cells) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--corpus", required=True, type=Path, help="directory of .txt/.md paper texts")
    ap.add_argument("--out", required=True, type=Path, help="output directory for increment TSVs")
    ap.add_argument("--min-count", type=int, default=3, help="keep counted rows with count >= this")
    args = ap.parse_args()

    files = sorted(p for p in args.corpus.iterdir() if p.suffix.lower() in (".txt", ".md"))
    if not files:
        print(f"no .txt/.md files under {args.corpus}", file=sys.stderr)
        return 1

    agg_openers: Counter = Counter()
    agg_hedges: Counter = Counter()
    agg_rd: Counter = Counter()
    agg_gaps: list[tuple] = []
    agg_linkers: list[tuple] = []
    for fp in files:
        secs = split_sections(fp.read_text(encoding="utf-8", errors="ignore"))
        op, gaps, hd, lk, rd = distill(secs)
        agg_openers.update(op)
        agg_hedges.update(hd)
        agg_rd.update(rd)
        agg_gaps.extend(gaps)
        agg_linkers.extend(lk)

    args.out.mkdir(parents=True, exist_ok=True)
    seen, gap_rows = set(), []
    for sec, pivot, tmpl in agg_gaps:
        key = (sec, pivot, tmpl)
        if key not in seen:
            seen.add(key)
            gap_rows.append([sec, pivot, tmpl])
    linker_rows = [list(l) for l in agg_linkers]

    write_tsv(args.out / "opener_distribution_increment.tsv", ["section", "opener_3gram", "count"],
              [[s, o, c] for (s, o), c in agg_openers.items() if c >= args.min_count])
    write_tsv(args.out / "gap_transitions_increment.tsv", ["section", "pivot_word", "template"], gap_rows)
    write_tsv(args.out / "hedge_verbs_increment.tsv", ["verb", "tier", "count"],
              [[v, t, c] for (v, t), c in agg_hedges.items() if c >= args.min_count])
    write_tsv(args.out / "cross_section_linkers_increment.tsv", ["from_section", "to_section", "pattern"], linker_rows)
    write_tsv(args.out / "results_discussion_openers_increment.tsv", ["section", "opener_template", "count"],
              [[s, o, c] for (s, o), c in agg_rd.items() if c >= args.min_count])

    n = len(files)
    print(f"distilled {n} paper(s): {len(gap_rows)} gap templates, "
          f"{sum(1 for c in agg_openers.values() if c >= args.min_count)} openers, "
          f"{len(linker_rows)} linkers -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
