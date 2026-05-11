#!/bin/bash

# Main entry point for the Karaoke Lyric Alignment application

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "🎤 Starting Auto Lyrics Align Karaoke App..."
echo "📁 Project directory: $SCRIPT_DIR"

# Navigate to alignment-code directory so it can find read_map.json
cd "$SCRIPT_DIR/models/alignment-code"

# Run the FastAPI app
echo "🚀 Starting FastAPI server..."
conda run -n lyric_env python "$SCRIPT_DIR/backend/fastapi_app.py"
