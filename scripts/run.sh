#!/bin/bash

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ALIGNMENT_CODE_DIR="$SCRIPT_DIR/models/alignment-code"

# Change to alignment-code directory so it can find read_map.json
cd "$ALIGNMENT_CODE_DIR"

# Run the FastAPI app
conda run -n lyric_env python "$SCRIPT_DIR/backend/fastapi_app.py"
