#!/usr/bin/env python3
import argparse
import json
import os
import re
import subprocess
import sys


def parse_text(text: str):
    out = {
        "prompt": text.strip(),
        "negative": "",
        "n": 1,
        "width": int(os.getenv("SD_DEFAULT_WIDTH", "768")),
        "height": int(os.getenv("SD_DEFAULT_HEIGHT", "1024")),
        "steps": int(os.getenv("SD_DEFAULT_STEPS", "28")),
        "cfg": float(os.getenv("SD_DEFAULT_CFG", "7")),
    }

    m_n = re.search(r"(?:生成|来|要)?\s*(\d{1,2})\s*张", text)
    if m_n:
        out["n"] = max(1, min(int(m_n.group(1)), 20))

    m_wh = re.search(r"(\d{3,4})\s*[xX\*]\s*(\d{3,4})", text)
    if m_wh:
        out["width"] = int(m_wh.group(1))
        out["height"] = int(m_wh.group(2))

    m_steps = re.search(r"(?:steps\s*[=:]?\s*|步数\s*)(\d{1,3})", text, re.IGNORECASE)
    if m_steps:
        out["steps"] = int(m_steps.group(1))

    m_cfg = re.search(r"(?:cfg\s*[=:]?\s*|CFG\s*[=:]?\s*)(\d+(?:\.\d+)?)", text)
    if m_cfg:
        out["cfg"] = float(m_cfg.group(1))

    m_neg = re.search(r"(?:负面词|反向词|negative)\s*[：:]\s*(.+)$", text, re.IGNORECASE)
    if m_neg:
        out["negative"] = m_neg.group(1).strip()

    # remove control fragments from prompt
    prompt = re.sub(r"(?:生成|来|要)?\s*\d{1,2}\s*张", "", out["prompt"])
    prompt = re.sub(r"\d{3,4}\s*[xX\*]\s*\d{3,4}", "", prompt)
    prompt = re.sub(r"(?:steps\s*[=:]?\s*|步数\s*)\d{1,3}", "", prompt, flags=re.IGNORECASE)
    prompt = re.sub(r"(?:cfg\s*[=:]?\s*|CFG\s*[=:]?\s*)\d+(?:\.\d+)?", "", prompt)
    prompt = re.sub(r"(?:负面词|反向词|negative)\s*[：:].*$", "", prompt, flags=re.IGNORECASE)
    prompt = prompt.replace("：", " ").replace(":", " ").strip(" ,，")
    out["prompt"] = prompt if prompt else text.strip()

    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", required=True, help="raw user command")
    args = parser.parse_args()

    p = parse_text(args.text)
    cmd = [
        sys.executable,
        os.path.join(os.path.dirname(__file__), "generate.py"),
        "--prompt", p["prompt"],
        "--negative", p["negative"],
        "--n", str(p["n"]),
        "--width", str(p["width"]),
        "--height", str(p["height"]),
        "--steps", str(p["steps"]),
        "--cfg", str(p["cfg"]),
    ]

    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        print(json.dumps({"error": proc.stderr or proc.stdout or "generate failed"}, ensure_ascii=False))
        return proc.returncode

    try:
        data = json.loads(proc.stdout)
    except Exception:
        print(json.dumps({"error": "invalid generate output", "raw": proc.stdout}, ensure_ascii=False))
        return 1

    data["parsed"] = p
    print(json.dumps(data, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
