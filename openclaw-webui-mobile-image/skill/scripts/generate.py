#!/usr/bin/env python3
import argparse
import json
import os
import sys
from urllib import request


def post_json(url: str, payload: dict, timeout: int):
    data = json.dumps(payload).encode("utf-8")
    req = request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--negative", default="")
    parser.add_argument("--n", type=int, default=1)
    parser.add_argument("--width", type=int, default=int(os.getenv("SD_DEFAULT_WIDTH", "768")))
    parser.add_argument("--height", type=int, default=int(os.getenv("SD_DEFAULT_HEIGHT", "1024")))
    parser.add_argument("--steps", type=int, default=int(os.getenv("SD_DEFAULT_STEPS", "28")))
    parser.add_argument("--cfg", type=float, default=float(os.getenv("SD_DEFAULT_CFG", "7")))
    args = parser.parse_args()

    base = os.getenv("SD_WEBUI_URL", "http://127.0.0.1:7860").rstrip("/")
    timeout = int(os.getenv("SD_WEBUI_TIMEOUT", "180"))

    payload = {
        "prompt": args.prompt,
        "negative_prompt": args.negative,
        "steps": args.steps,
        "cfg_scale": args.cfg,
        "width": args.width,
        "height": args.height,
        "batch_size": 1,
        "n_iter": max(1, min(args.n, 20)),
        "seed": -1,
    }

    try:
        res = post_json(f"{base}/sdapi/v1/txt2img", payload, timeout)
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        return 1

    out = {
        "images": res.get("images", []),
        "meta": {
            "prompt": args.prompt,
            "n": payload["n_iter"],
            "width": args.width,
            "height": args.height,
            "steps": args.steps,
            "cfg": args.cfg,
        },
    }
    print(json.dumps(out, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
