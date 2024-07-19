#!/usr/bin/env bash
echo "Running tests #1"
servercheck -s "TEST:4000" --server "Other:3000" -f data.json
