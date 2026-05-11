#!/bin/bash

# Demo script for Lyrics Alignment
# Usage: ./demo_lyrics_align.sh

echo "🎵 Lyrics Alignment Demo"
echo "========================"
echo ""

# Check if conda env exists
if ! conda env list | grep -q "lyric_env"; then
    echo "❌ Conda environment 'lyric_env' not found!"
    echo "Please create it first:"
    echo "  conda create -n lyric_env python=3.10"
    echo "  conda activate lyric_env"
    echo "  pip install -r requirements_lyrics_align.txt"
    exit 1
fi

# Check if sample files exist
if [ ! -f "sample_audio.mp3" ]; then
    echo "⚠️  No sample_audio.mp3 found"
    echo "Please provide:"
    echo "  - sample_audio.mp3 (your audio file)"
    echo "  - sample_lyrics.txt (lyrics, one line per sentence)"
    exit 1
fi

if [ ! -f "sample_lyrics.txt" ]; then
    echo "⚠️  No sample_lyrics.txt found"
    echo "Creating example lyrics file..."
    cat > sample_lyrics.txt << 'EOF'
Nói bỏ lỡ rồi sẽ tiếc cho mà xem
Đừng để một ngày em bước ra khỏi đây
Vì anh đã từng yêu em nhiều như thế
EOF
    echo "✅ Created sample_lyrics.txt - Please edit it to match your song!"
    exit 0
fi

echo "📁 Found input files:"
echo "  - sample_audio.mp3"
echo "  - sample_lyrics.txt"
echo ""

# Run alignment
echo "🚀 Running alignment..."
conda run -n lyric_env python lyrics_align.py \
    --audio sample_audio.mp3 \
    --lyrics sample_lyrics.txt \
    --lang vi \
    --output-dir demo_output

echo ""
echo "✅ Done! Check demo_output/ folder for results"
echo ""
echo "📦 Output files:"
ls -lh demo_output/

echo ""
echo "💡 Next steps:"
echo "  1. Check demo_output/*.json for web player"
echo "  2. Use demo_output/*.srt for video subtitles"
echo "  3. Try --render-video to create lyrics video"
