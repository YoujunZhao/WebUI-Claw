#!/usr/bin/env python3
import argparse
import json
import re
from collections import defaultdict
from datetime import datetime, timezone


def topic_bucket(text: str):
    t = (text or "").lower()
    if any(k in t for k in ["security", "attack", "defense", "safety", "guardrail", "prompt injection"]):
        return "Security & Safety"
    if any(k in t for k in ["agent", "system", "architecture", "resource", "routing", "os"]):
        return "Agent Systems & Architecture"
    if any(k in t for k in ["memory", "benchmark", "evaluation", "reinforcement", "rl", "learning"]):
        return "Learning, Memory & Evaluation"
    return "Applications & Domain Use Cases"


def pub_bucket(p):
    v = (p.get("venue") or "").strip()
    if v:
        low = v.lower()
        if any(k in low for k in ["conference", "proceedings", "symposium", "workshop"]):
            return "Published Papers (Conference)"
        return "Published Papers (Journal/Other Venue)"
    return "Preprints / Unpublished"


def badge(label, link, color):
    if link:
        return f"[![{label}](https://img.shields.io/badge/{label}-{color}.svg)]({link})"
    return f"[![{label}](https://img.shields.io/badge/{label}-Not%20Found-lightgrey)](#)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--topic", required=True)
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    data = json.load(open(args.input, "r", encoding="utf-8"))
    papers = data.get("papers", [])

    grouped = defaultdict(lambda: defaultdict(list))
    for p in papers:
        primary_text = f"{p.get('title', '')} {p.get('abstract', '')}"
        tcat = topic_bucket(primary_text)
        pcat = pub_bucket(p)
        grouped[tcat][pcat].append(p)

    lines = []
    lines.append("# Awesome " + args.topic.title() + " Papers")
    lines.append("")
    lines.append(f"A curated list of papers for **{args.topic}** across arXiv, Crossref, and Semantic Scholar.")
    lines.append("")
    lines.append(f"> Last update: **{datetime.now(timezone.utc).strftime('%Y-%m-%d')}**")
    lines.append("")
    lines.append("## Table of Contents")
    cats = list(grouped.keys())
    for c in cats:
        anchor = re.sub(r"[^a-z0-9]+", "-", c.lower()).strip("-")
        lines.append(f"- [{c}](#{anchor})")
    lines.append("")

    for c in cats:
        lines.append("---")
        lines.append("")
        lines.append(f"## {c}")
        lines.append("")
        for pcat in ["Published Papers (Conference)", "Published Papers (Journal/Other Venue)", "Preprints / Unpublished"]:
            items = grouped[c].get(pcat, [])
            if not items:
                continue
            lines.append(f"### {pcat}")
            lines.append("")
            for p in items:
                title = p.get("title", "Untitled").strip()
                primary = p.get("url") or p.get("arxiv") or "#"
                date = p.get("date") or "Unknown"
                venue = (p.get("venue") or "").strip()
                if venue:
                    pub_label = f"[Published at: {venue}]"
                else:
                    pub_label = "[Publication: Preprint / Unknown]"

                arxiv = p.get("arxiv") or ""
                github = ""
                website = ""

                lines.append(f"+ [{title}]({primary})")
                lines.append(f"  {pub_label}")
                lines.append("  " + badge("arXiv", arxiv, "b31b1b"))
                lines.append("  " + badge("GitHub", github, "9cf"))
                lines.append("  " + badge("Website", website, "9cf") + f" **({date})**")
                lines.append("")

    open(args.output, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"Wrote README -> {args.output}")


if __name__ == "__main__":
    main()
