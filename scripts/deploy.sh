#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

if [ ! -f .env ]; then
  cp .env.example .env
  echo "[deploy] .env not found, created from .env.example"
fi

echo "[deploy] starting Stable Diffusion WebUI..."
docker compose up -d

echo "[deploy] waiting for API..."
for i in {1..60}; do
  if curl -fsS http://127.0.0.1:7860/sdapi/v1/samplers >/dev/null 2>&1; then
    echo "[deploy] WebUI API is ready: http://127.0.0.1:7860"
    exit 0
  fi
  sleep 3
done

echo "[deploy] timeout: WebUI API not ready. Check logs: docker compose logs -f webui"
exit 1
