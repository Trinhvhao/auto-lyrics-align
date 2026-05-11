#!/bin/bash

# 🎤 Auto Lyrics Align - Main Entry Point
# This script sets up and runs the FastAPI server

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
MODELS_DIR="$SCRIPT_DIR/models/alignment-code"
BACKEND_DIR="$SCRIPT_DIR/backend"

echo "================================"
echo "🎤 Auto Lyrics Align Karaoke App"
echo "================================"
echo ""

# Check if Conda environment exists
if ! command -v conda &> /dev/null; then
    echo "⚠️  Conda not found. Please install conda or activate venv:"
    echo "   conda activate lyric_env"
    echo "   OR"
    echo "   source lyric_env/bin/activate"
    exit 1
fi

# Try to activate conda environment if available
if conda env list | grep -q "^lyric_env"; then
    echo "📦 Activating conda environment: lyric_env"
    source /opt/miniconda3/etc/profile.d/conda.sh 2>/dev/null || source ~/miniconda3/etc/profile.d/conda.sh 2>/dev/null || true
    conda activate lyric_env
else
    echo "⚠️  Environment 'lyric_env' not found"
    echo "   Create it with:"
    echo "   conda env create -f environment.yml"
    exit 1
fi

# Verify key dependencies
echo "✅ Checking dependencies..."
python -c "import fastapi, transformers, torch; print('   ✓ All core packages found')" || {
    echo "❌ Missing dependencies. Run: pip install -r requirements.txt"
    exit 1
}

# Navigate to models directory for predict.py
echo ""
echo "📂 Setting working directory: $MODELS_DIR"
cd "$MODELS_DIR"

# Run FastAPI app
echo ""
echo "🚀 Starting FastAPI server..."
echo "   Server: http://localhost:8000"
echo "   API Docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop"
echo "================================"
echo ""

python "$BACKEND_DIR/fastapi_app.py"
