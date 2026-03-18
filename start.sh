#!/bin/bash
set -e
echo "Starting Decentralized Voting System on Blockchain..."
uvicorn app:app --host 0.0.0.0 --port 9075 --workers 1
