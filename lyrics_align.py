"""
🎵 LYRICS VIDEO GENERATOR

Pipeline: Audio + Lyrics text → Forced Alignment → ASS/SRT/Video

Cài đặt (chạy 1 lần):
pip install whisperx torch torchaudio moviepy pillow numpy
pip install demucs  # optional: tách vocal cho chính xác hơn

Cách dùng:
python lyrics_align.py --audio song.mp3 --lyrics lyrics.txt --lang vi

Format file lyrics.txt (mỗi dòng 1 câu):
Nói bỏ lỡ rồi sẽ tiếc cho mà xem
Đừng để một ngày em bước ra khỏi đây
...
"""

import argparse
import os
import json
import subprocess
import sys


# ─────────────────────────────────────────────
# BƯỚC 1: Tách vocal (tuỳ chọn, tăng độ chính xác)
# ─────────────────────────────────────────────

def separate_vocals(audio_path: str, output_dir: str = "separated") -> str:
    """Dùng Demucs tách giọng hát ra khỏi nhạc nền"""
    print("🎸 Đang tách vocal với Demucs...")
    os.makedirs(output_dir, exist_ok=True)
    
    subprocess.run([
        sys.executable, "-m", "demucs",
        "--two-stems=vocals",
        "-o", output_dir,
        audio_path
    ], check=True)
    
    # Tìm file vocal output
    base = os.path.splitext(os.path.basename(audio_path))[0]
    vocal_path = os.path.join(output_dir, "htdemucs", base, "vocals.wav")
    
    if os.path.exists(vocal_path):
        print(f"✅ Vocal đã tách: {vocal_path}")
        return vocal_path
    else:
        print("⚠️ Không tìm thấy vocal, dùng audio gốc")
        return audio_path


# ─────────────────────────────────────────────
# BƯỚC 2: Forced Alignment với WhisperX
# ─────────────────────────────────────────────

def align_lyrics(audio_path: str, lyrics_path: str, language: str = "vi") -> tuple:
    """
    Căn timestamp từng từ dùng WhisperX forced alignment
    Trả về list: [{"word": "Nói", "start": 0.12, "end": 0.45}, ...]
    """
    import whisperx
    import torch
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"⚡ Dùng device: {device}")
    
    # Đọc lyrics
    with open(lyrics_path, "r", encoding="utf-8") as f:
        lyrics_lines = [line.strip() for line in f if line.strip()]
    
    full_text = " ".join(lyrics_lines)
    
    # Load alignment model
    print(f"📥 Load alignment model cho ngôn ngữ: {language}")
    model_a, metadata = whisperx.load_align_model(
        language_code=language,
        device=device
    )
    
    # Tạo transcript giả từ lyrics (forced alignment — dùng lyrics có sẵn)
    # WhisperX cần segments với approximate timing để forced align
    # Dùng Whisper để transcribe trước lấy segment boundaries
    print("🎙️ Transcribe để lấy segment boundaries...")
    model = whisperx.load_model("large-v3", device, compute_type="float32")
    audio = whisperx.load_audio(audio_path)
    result = model.transcribe(audio, batch_size=16, language=language)
    
    # Forced align với lyrics chính xác của bạn
    print("🔗 Đang forced alignment...")
    result_aligned = whisperx.align(
        result["segments"],
        model_a,
        metadata,
        audio,
        device,
        return_char_alignments=False
    )
    
    # Trích xuất word-level timestamps
    words = []
    for segment in result_aligned["segments"]:
        for word_info in segment.get("words", []):
            if "start" in word_info and "end" in word_info:
                words.append({
                    "word": word_info["word"].strip(),
                    "start": round(word_info["start"], 3),
                    "end": round(word_info["end"], 3),
                })
    
    print(f"✅ Aligned {len(words)} từ")
    return words, lyrics_lines


# ─────────────────────────────────────────────
# BƯỚC 3: Export các format
# ─────────────────────────────────────────────

def group_words_to_lines(words: list, lyrics_lines: list) -> list:
    """Gom words lại thành từng dòng lyrics"""
    lines = []
    word_idx = 0
    
    for line_text in lyrics_lines:
        line_words_count = len(line_text.split())
        line_words = words[word_idx : word_idx + line_words_count]
        
        if not line_words:
            continue
        
        lines.append({
            "text": line_text,
            "start": line_words[0]["start"],
            "end": line_words[-1]["end"],
            "words": line_words,
        })
        word_idx += line_words_count
    
    return lines


def export_srt(lines: list, output_path: str):
    """Export file .srt chuẩn"""
    def format_time(seconds):
        h = int(seconds // 3600)
        m = int((seconds % 3600) // 60)
        s = int(seconds % 60)
        ms = int((seconds % 1) * 1000)
        return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"
    
    with open(output_path, "w", encoding="utf-8") as f:
        for i, line in enumerate(lines, 1):
            f.write(f"{i}\n")
            f.write(f"{format_time(line['start'])} --> {format_time(line['end'])}\n")
            f.write(f"{line['text']}\n\n")
    
    print(f"📄 Đã export SRT: {output_path}")


def export_lrc(lines: list, output_path: str):
    """Export file .lrc (karaoke format)"""
    def format_time(seconds):
        m = int(seconds // 60)
        s = seconds % 60
        return f"{m:02d}:{s:05.2f}"
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("[ti:Song Title]\n[ar:Artist]\n[by:Generated by LyricsAlign]\n\n")
        for line in lines:
            f.write(f"[{format_time(line['start'])}]{line['text']}\n")
    
    print(f"🎤 Đã export LRC: {output_path}")


def export_ass(lines: list, output_path: str, style: str = "tiktok"):
    """
    Export file .ass với word-level karaoke highlight
    Style 'tiktok': chữ trắng, highlight vàng/cam, nền tối
    """
    def format_time(seconds):
        h = int(seconds // 3600)
        m = int((seconds % 3600) // 60)
        s = int(seconds % 60)
        cs = int((seconds % 1) * 100)
        return f"{h}:{m:02d}:{s:02d}.{cs:02d}"
    
    header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,SVN-Gilroy Bold,85,&H00FFFFFF,&H000000FF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,4,3,2,80,80,200,1
Style: Highlight,SVN-Gilroy Bold,85,&H0000A8FF,&H000000FF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,4,3,2,80,80,200,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    
    events = []
    for line in lines:
        # Build karaoke text với {\k} tags (centiseconds)
        karaoke_text = ""
        for word in line["words"]:
            duration_cs = int((word["end"] - word["start"]) * 100)
            karaoke_text += f"{{\\kf{duration_cs}}}{word['word']} "
        
        karaoke_text = karaoke_text.strip()
        events.append(
            f"Dialogue: 0,{format_time(line['start'])},{format_time(line['end'])},Default,,0,0,0,,{{\\k0}}{karaoke_text}"
        )
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(header)
        f.write("\n".join(events))
    
    print(f"🎬 Đã export ASS (karaoke): {output_path}")


def export_json(words: list, lines: list, output_path: str):
    """Export JSON để dùng với web player"""
    data = {
        "words": words,
        "lines": lines
    }
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"📦 Đã export JSON: {output_path}")


# ─────────────────────────────────────────────
# BƯỚC 4: Render video (tuỳ chọn)
# ─────────────────────────────────────────────

def render_video(audio_path: str, lines: list, output_path: str = "lyrics_video.mp4"):
    """
    Render video lyrics với MoviePy
    Cần: pip install moviepy pillow
    """
    from moviepy.editor import AudioFileClip, ImageClip, CompositeVideoClip
    from PIL import Image, ImageDraw, ImageFont
    import numpy as np
    
    print("🎬 Đang render video...")
    
    W, H = 1080, 1920
    FPS = 30
    
    audio = AudioFileClip(audio_path)
    duration = audio.duration
    
    clips = []
    
    # Background tối
    bg = np.zeros((H, W, 3), dtype=np.uint8)
    bg[:] = [15, 15, 20]  # dark blue-black
    
    for line in lines:
        img = Image.fromarray(bg.copy())
        draw = ImageDraw.Draw(img)
        
        try:
            font = ImageFont.truetype("arial.ttf", 90)
        except:
            font = ImageFont.load_default()
        
        # Vẽ text căn giữa
        text = line["text"]
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        x = (W - tw) // 2
        y = (H - th) // 2
        
        # Shadow
        draw.text((x + 4, y + 4), text, font=font, fill=(0, 0, 0, 180))
        # Text trắng
        draw.text((x, y), text, font=font, fill=(255, 255, 255))
        
        frame = np.array(img)
        clip = (
            ImageClip(frame)
            .set_start(line["start"])
            .set_duration(line["end"] - line["start"])
        )
        clips.append(clip)
    
    video = CompositeVideoClip(clips, size=(W, H))
    video = video.set_audio(audio)
    video.write_videofile(output_path, fps=FPS, codec="libx264", audio_codec="aac")
    
    print(f"✅ Video đã render: {output_path}")


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="🎵 Lyrics Video Generator")
    parser.add_argument("--audio", required=True, help="Đường dẫn file audio (mp3/wav/flac)")
    parser.add_argument("--lyrics", required=True, help="Đường dẫn file lyrics (.txt, mỗi dòng 1 câu)")
    parser.add_argument("--lang", default="vi", help="Ngôn ngữ (vi/en/...) mặc định: vi")
    parser.add_argument("--separate-vocals", action="store_true", help="Tách vocal trước khi align (chính xác hơn)")
    parser.add_argument("--render-video", action="store_true", help="Render ra file MP4")
    parser.add_argument("--output-dir", default="output", help="Thư mục output")
    
    args = parser.parse_args()
    
    os.makedirs(args.output_dir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(args.audio))[0]
    
    # Tách vocal nếu muốn
    audio_to_align = args.audio
    if args.separate_vocals:
        audio_to_align = separate_vocals(
            args.audio, 
            os.path.join(args.output_dir, "separated")
        )
    
    # Aligned timestamps
    words, lyrics_lines = align_lyrics(audio_to_align, args.lyrics, args.lang)
    lines = group_words_to_lines(words, lyrics_lines)
    
    # Export tất cả formats
    export_srt(lines, os.path.join(args.output_dir, f"{base_name}.srt"))
    export_lrc(lines, os.path.join(args.output_dir, f"{base_name}.lrc"))
    export_ass(lines, os.path.join(args.output_dir, f"{base_name}.ass"))
    export_json(words, lines, os.path.join(args.output_dir, f"{base_name}.json"))
    
    # Render video nếu muốn
    if args.render_video:
        render_video(
            args.audio, 
            lines, 
            os.path.join(args.output_dir, f"{base_name}_lyrics.mp4")
        )
    
    print("\n🎉 Xong! Các file output:")
    for f in os.listdir(args.output_dir):
        print(f"   📁 {args.output_dir}/{f}")


if __name__ == "__main__":
    main()
