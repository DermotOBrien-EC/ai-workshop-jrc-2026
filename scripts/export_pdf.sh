#!/usr/bin/env bash
# Export the rendered slides to output/workshop-2026-09-11.pdf with headless Chrome.
#
#   bash scripts/build.sh          # first, so index.html exists
#   bash scripts/export_pdf.sh
#
# reveal.js prints one slide per page when the URL ends in ?print-pdf, and it
# needs to be served over HTTP, so this script starts a local server for the
# duration of the export. Set CHROME to your browser binary if it is not the
# macOS default below. Expected result: 43 pages.
set -euo pipefail
cd "$(dirname "$0")/.."

CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
PORT="${PORT:-8765}"
OUT="output/workshop-2026-09-11.pdf"

[ -f index.html ] || { echo "index.html not found: run scripts/build.sh first" >&2; exit 1; }
[ -x "$CHROME" ] || { echo "Chrome not found at $CHROME (set CHROME=...)" >&2; exit 1; }

mkdir -p output
python3 -m http.server "$PORT" --bind 127.0.0.1 >/dev/null 2>&1 &
SERVER=$!
trap 'kill $SERVER 2>/dev/null || true' EXIT
sleep 1

"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
  --run-all-compositor-stages-before-draw --virtual-time-budget=30000 \
  --print-to-pdf="$OUT" "http://127.0.0.1:$PORT/index.html?print-pdf" 2>/dev/null

ls -l "$OUT"
