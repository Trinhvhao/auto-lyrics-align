# 🎵 Standalone Lyrics Player

Một player lyrics nhẹ, đẹp và dễ sử dụng - không cần server backend!

## ✨ Tính năng

- **Offline-first** - Chạy hoàn toàn trên browser, không cần internet
- **2 input modes**:
  - ✍️ Manual: Nhập lyrics format LRC `[mm:ss.xx] text`
  - 📦 JSON: Paste output từ `lyrics_align.py`
- **Word-level highlighting** - Chữ sáng lên theo từng từ
- **Smooth animations** - Chuyển dòng mượt mà
- **Mobile-friendly** - Responsive design
- **Minimal UI** - Focus vào lyrics

## 🚀 Cách sử dụng

### Option 1: Qua Web Server (đang chạy)

Truy cập: **http://localhost:7864/player**

### Option 2: Mở trực tiếp file HTML

```bash
# Mở bằng browser
open frontend/static/player.html

# Hoặc double-click vào file player.html
```

## 📝 Input Format

### Manual Mode (LRC)

```
[00:05.20] Nói bỏ lỡ rồi sẽ tiếc cho mà xem
[00:09.80] Đừng để một ngày em bước ra khỏi đây
[00:14.30] Vì anh biết khi đã mất đi rồi
[00:19.10] Chỉ còn lại những tiếc nuối thôi
```

Format: `[phút:giây.centisecond] lời bài hát`

### JSON Mode

Paste output từ `lyrics_align.py`:

```json
{
  "lines": [
    {
      "text": "Nói bỏ lỡ rồi sẽ tiếc cho mà xem",
      "start": 5.2,
      "end": 8.9,
      "words": [
        {"word": "Nói", "start": 5.2, "end": 5.6},
        {"word": "bỏ", "start": 5.6, "end": 6.0}
      ]
    }
  ]
}
```

## 🎯 Use Cases

1. **Preview lyrics** trước khi render video
2. **Test alignment** từ `lyrics_align.py`
3. **Karaoke practice** - Học thuộc lời bài hát
4. **Share lyrics** - Gửi file HTML cho bạn bè

## 🎨 UI Features

- **Dark theme** - Dễ nhìn, không chói mắt
- **Gradient highlights** - Vàng cam đẹp mắt
- **3-line view** - Hiện prev/current/next line
- **Progress bar** - Click để seek
- **Time display** - Elapsed / Duration
- **Controls** - Play/Pause, Skip ±5s

## 💡 Tips

1. **LRC format** - Dùng tool online để convert lyrics sang LRC
2. **JSON output** - Chạy `lyrics_align.py` để có word-level timing chính xác
3. **Mobile** - Player hoạt động tốt trên điện thoại
4. **Offline** - Save file HTML và dùng mọi lúc mọi nơi

## 🔗 Integration

Player này tương thích với:
- Output từ `lyrics_align.py` (JSON mode)
- File LRC chuẩn (Manual mode)
- Web app chính tại `/` (cùng format JSON)

## 📱 Screenshots

```
┌─────────────────────────┐
│   🎵 Lyrics Player      │
│                         │
│  Đừng để một ngày em    │  ← prev (mờ)
│                         │
│  Vì anh biết khi đã     │  ← active (sáng + highlight)
│  mất đi rồi             │
│                         │
│  Chỉ còn lại những      │  ← next (mờ)
│                         │
│  ━━━━━━━━━━━━━━━━━━━   │  ← progress
│  1:23        3:45       │
│                         │
│    ⟪    ▶    ⟫         │  ← controls
└─────────────────────────┘
```

## 🛠️ Customization

Muốn tùy chỉnh? Edit file `player.html`:

- **Colors**: Tìm `#FF9500`, `#FFD43B` trong CSS
- **Font size**: Thay `.lyric-line.active { font-size: 2.6rem }`
- **Animation speed**: Sửa `transition: all 0.3s ease`
- **Background**: Thay `radial-gradient` trong `body::before`

---

**Tác giả:** Lyrics Player  
**License:** MIT  
**Version:** 1.0
