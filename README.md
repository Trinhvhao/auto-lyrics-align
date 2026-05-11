# 🎤 Auto Lyrics Align - Vietnamese Karaoke

Ứng dụng web chuyên nghiệp để căn chỉnh lời bài hát với nhạc nền, tạo hiệu ứng chữ nhảy múa đồng bộ (karaoke) bằng Wav2Vec2 AI Model.

## 📁 Cấu trúc Dự án

```
auto-lyrics-align/
├── backend/
│   └── fastapi_app.py              # API Backend (FastAPI)
├── frontend/
│   └── static/
│       └── index.html              # Web UI (HTML/CSS/JS)
├── models/
│   ├── alignment-code/             # Source code mô hình (Wav2Vec2CTC)
│   └── lyric-alignment/            # AI Model weights
├── docs/                           # Documentation
├── examples/                       # Demo files & examples
├── scripts/                        # Utility scripts
├── uploads/                        # Runtime folder (lưu file tải lên)
├── run.sh                          # Entry point (khởi động app)
└── README.md
```

## 🚀 Cách Chạy

### 1. **Khởi động Server FastAPI**

```bash
cd auto-lyrics-align
./run.sh
```

Hoặc chạy trực tiếp:

```bash
cd /hdd3/nhannv/Hello/TrinhHao/lyric-karaoke-app/models/alignment-code
conda run -n lyric_env python ../../backend/fastapi_app.py
```

Server sẽ chạy tại: **http://127.0.0.1:7864**

### 2. **Truy cập Web UI**

Mở trình duyệt và nhập:

```
http://127.0.0.1:7864
```

Nếu chạy trên server từ xa, thay thế `127.0.0.1` bằng địa chỉ IP của server.

### 3. **Cách Sử dụng**

1. Chọn file nhạc (`.mp3`, `.wav`, `.flac`, v.v.)
2. Nhập lời bài hát (mỗi dòng = 1 đoạn)
3. Bấm **"Bắt đầu Căn chỉnh Lời"**
4. Đợi khoảng 10-30 giây để AI xử lý
5. Bấm **Play ▶️** để xem chữ chạy đồng bộ với nhạc

## 🛠️ Yêu cầu Hệ thống

- **Python 3.10+**
- **Conda** (với environment `lyric_env` đã được cài đặt)
- **GPU** (nên có để xử lý nhanh, CPU cũng được nhưng chậm hơn)

### Packages Cần Thiết:

```bash
conda run -n lyric_env pip install fastapi uvicorn python-multipart torch torchaudio transformers
```

## 📝 Thông tin API

### POST /api/align

**Request:**
- `audio_file`: File audio (multipart form)
- `lyric_text`: Lời bài hát (dạng text)

**Response:**
```json
{
  "audio_url": "/media/audio_<uuid>.mp3",
  "alignment": [
    {
      "s": 0,
      "e": 500,
      "l": [
        { "s": 0, "e": 250, "d": "Xin" },
        { "s": 250, "e": 500, "d": "chào" }
      ]
    }
  ]
}
```

## 🎯 Các File Quan Trọng

| File | Mục đích |
|------|---------|
| `backend/fastapi_app.py` | API Server, xử lý alignment |
| `frontend/static/index.html` | Giao diện web, hiệu ứng karaoke |
| `models/alignment-code/predict.py` | Gọi AI Model để căn chỉnh |
| `models/alignment-code/read_map.json` | Mapping dữ liệu model |

## 🐛 Troubleshooting

### Lỗi: "Address already in use"
```bash
fuser -k 7864/tcp  # Kill process đang dùng port 7864
```

### Lỗi: "read_map.json not found"
Đảm bảo đang chạy từ thư mục `models/alignment-code`:
```bash
cd /hdd3/nhannv/Hello/TrinhHao/lyric-karaoke-app/models/alignment-code
conda run -n lyric_env python ../../backend/fastapi_app.py
```

### Chậm xử lý
- Kiểm tra GPU: `nvidia-smi` (nếu có)
- Tăng kích thước RAM nếu xử lý bị out-of-memory

## 📞 Hỗ Trợ

Nếu gặp vấn đề, hãy kiểm tra:
1. Port 7864 có sẵn không?
2. Conda environment `lyric_env` có được kích hoạt không?
3. Model weights có tải về không? (folder `models/lyric-alignment`)

---

**Tạo bởi:** AI Assistant  
**Ngôn ngữ:** Python (FastAPI), HTML/CSS/JavaScript  
**Model:** Wav2Vec2 (facebook/wav2vec2-base-960h)  
