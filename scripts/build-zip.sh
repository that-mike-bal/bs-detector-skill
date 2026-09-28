#!/usr/bin/env bash
# Builds dist/bs-detector.zip for uploading to claude.ai (Customize > Skills > Upload a skill).
# The zip holds the bs-detector folder at its root, which is what the upload expects.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p dist
rm -f dist/bs-detector.zip
(cd skills && zip -rq ../dist/bs-detector.zip bs-detector -x '*.DS_Store')
echo "Built dist/bs-detector.zip"
