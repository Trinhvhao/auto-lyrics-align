# 🎵 Lyrics Video Generator

Pipeline hoàn chỉnh: **Audio + Lyrics text → Forced Alignment → ASS/SRT/Video**

## 📦 Cài đặt

```bash
# Cài đặt dependencies chính
pip install whisperx torch torchaudio moviepy pillow numpy

# Optional: Tách vocal cho kết quả chính xác hơn
pip install demucs
```

## 🚀 Cách sử dụng

### 1. Chuẩn bị file lyrics

Tạo file `lyrics.txt` với format mỗi dòng là một câu:

```
Nói bỏ lỡ rồi sẽ tiếc cho mà xem
Đừng để một ngày em bước ra khỏi đây
Vì anh đã từng yêu em nhiều như thế
```

### 2. Chạy alignment cơ bản

```bash
python lyrics_align.py --audio song.mp3 --lyrics lyrics.txt --lang vi
```

### 3. Các tùy chọn nâng cao

```bash
# Tách vocal trước khi align (chính xác hơn)
python lyrics_align.py --audio song.mp3 --lyrics lyrics.txt --lang vi --separate-vocals

# Render video luôn
python lyrics_align.py --audio song.mp3 --lyrics lyrics.txt --lang vi --render-video

# Chỉ định thư mục output
python lyrics_align.py --audio song.mp3 --lyrics lyrics.txt --output-dir my_output
```

## 📤 Output formats

Script sẽ tạo ra các file:

- **`.srt`** - Subtitle chuẩn (dùng cho video editor)
- **`.lrc`** - Karaoke format (dùng cho music player)
- **`.ass`** - Advanced SubStation Alpha với word-level karaoke effect
- **`.json`** - Data format cho web player (như app hiện tại)
- **`.mp4`** - Video lyrics (nếu dùng `--render-video`)

## 🎯 Tích hợp với Web App

File JSON output có format tương thích với web app hiện tại:

```json
{
  "words": [
    {"word": "Nói", "start": 0.12, "end": 0.45},
    {"word": "bỏ", "start": 0.46, "end": 0.68}
  ],
  "lines": [
    {
      "text": "Nói bỏ lỡ rồi sẽ tiếc cho mà xem",
      "start": 0.12,
      "end": 2.45,
      "words": [...]
    }
  ]
}
```

## 🔧 Troubleshooting

### CUDA out of memory
```bash
# Dùng CPU thay vì GPU
export CUDA_VISIBLE_DEVICES=""
python lyrics_align.py ...
```

### Font không tìm thấy (khi render video)
- Windows: Script tự động dùng `arial.ttf`
- Linux: Cài font: `sudo apt install fonts-dejavu-core`
- Mac: Font mặc định đã có sẵn

## 💡 Tips

1. **Chất lượng audio tốt** = alignment chính xác hơn
2. **Tách vocal** (`--separate-vocals`) giúp cải thiện độ chính xác đáng kể
3. **Lyrics chính xác** - Đảm bảo lyrics khớp 100% với bài hát
4. **Ngôn ngữ đúng** - Dùng `--lang en` cho tiếng Anh, `--lang vi` cho tiếng Việt

## 🎬 Workflow đề xuất

```bash
# Bước 1: Test alignment nhanh
python lyrics_align.py --audio song.mp3 --lyrics lyrics.txt --lang vi

# Bước 2: Kiểm tra file JSON/SRT xem có chính xác không

# Bước 3: Nếu OK, render video với vocal separation
python lyrics_align.py --audio song.mp3 --lyrics lyrics.txt --lang vi \
  --separate-vocals --render-video
```

## 📝 Notes

- WhisperX model `large-v3` cần ~10GB VRAM
- Demucs vocal separation cần ~2-3 phút cho 1 bài 4 phút
- Video rendering tốc độ phụ thuộc vào độ dài bài hát

---

**Tác giả:** Lyrics Alignment Pipeline  
**License:** MIT
