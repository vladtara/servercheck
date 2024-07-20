#!/usr/bin/env bash
echo "Running tests #1"
servercheck -s "google.com" --server "amazon.com" -f data.json
