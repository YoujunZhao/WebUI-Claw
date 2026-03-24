#!/usr/bin/env bash
set -euo pipefail

URL="${SD_WEBUI_URL:-http://127.0.0.1:7860}"

echo "[healthcheck] checking ${URL}/sdapi/v1/samplers"
curl -fsS "${URL}/sdapi/v1/samplers" | head -c 300 && echo

echo "[healthcheck] ok"
