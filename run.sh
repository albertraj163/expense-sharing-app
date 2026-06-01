#!/bin/bash
cd "$(dirname "$0")"

PORT=5001
URL="http://localhost:${PORT}"

# Already running?
if curl -sf "${URL}/" >/dev/null 2>&1; then
    echo ""
    echo "  ExpenseSplit is already running"
    echo "  Open: ${URL}"
    echo ""
    exit 0
fi

# Port blocked by another app?
if ss -tln 2>/dev/null | grep -q ":${PORT} " || netstat -tln 2>/dev/null | grep -q ":${PORT} "; then
    echo ""
    echo "  Error: Port ${PORT} is used by another program."
    echo "  Close it first, then run ./run.sh again."
    echo ""
    exit 1
fi

pip3 install -r requirements.txt -q
echo ""
echo "  Starting ExpenseSplit..."
echo ""
PORT=${PORT} python3 app.py
