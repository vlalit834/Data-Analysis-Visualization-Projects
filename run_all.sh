#!/usr/bin/env bash
set -euo pipefail

# Run each project's main script (using the repo venv python)
PY="/workspaces/Data-Analysis-Visualization-Projects/.venv/bin/python"

echo "Running Ques 1..."
$PY ques/ques1/main.py

echo "\nRunning Ques 2..."
$PY ques/ques2/main.py

echo "\nRunning Ques 3..."
$PY ques/ques3/main.py

echo "\nRunning Ques 4..."
$PY ques/ques4/main.py

echo "\nAll done. Generated plots are in the respective ques/*/plots directories."