#!/bin/bash
# Double-click to start the AWS AIP-C01 practice quiz. It then opens in your browser.
# First run only: macOS may block it — right-click this file -> Open -> Open.
cd "$(dirname "$0")" || exit 1
PY=""
for c in /usr/bin/python3 /opt/homebrew/bin/python3 /usr/local/bin/python3; do
  [ -x "$c" ] && PY="$c" && break
done
[ -z "$PY" ] && PY="$(command -v python3 2>/dev/null)"
if [ -z "$PY" ]; then
  osascript -e 'display dialog "Python 3 was not found. Install it from python.org (or run: xcode-select --install in Terminal), then try again." buttons {"OK"} with title "AWS Quiz"'
  exit 1
fi
exec "$PY" app.py
