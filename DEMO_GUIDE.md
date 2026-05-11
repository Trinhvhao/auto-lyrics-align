# 🎵 Hướng dẫn Demo - Duyên Trời

## 📦 Files demo đã tạo

1. **demo_song_settings.html** - Trang web demo với UI đẹp
2. **apply_demo_settings.js** - Script để chạy trong console
3. **DEMO_GUIDE.md** - File này

## 🚀 Cách 1: Dùng trang HTML (Khuyến nghị)

### Bước 1: Mở file demo
```bash
# Mở file trong trình duyệt
open demo_song_settings.html
# Hoặc
firefox demo_song_settings.html
# Hoặc
chrome demo_song_settings.html
```

### Bước 2: Apply settings
- Bấm nút **"🚀 Apply Settings to localStorage"**
- Thấy thông báo: ✅ Settings đã được lưu vào localStorage!

### Bước 3: Mở trang karaoke
```bash
# Chạy server (nếu chưa chạy)
cd backend
python fastapi_app.py

# Mở trình duyệt
http://localhost:7864/
```

### Bước 4: Load demo
1. Tạo file nhạc giả tên **"demo_duyen_troi.mp3"** (hoặc bất kỳ file mp3 nào)
2. Trong Auto Panel, chọn file đó
3. ✨ Settings tự động load!
4. Bấm **"Bỏ qua →"** để vào menu
5. Bấm **START** để xem demo

---

## 🎮 Cách 2: Dùng Console

### Bước 1: Mở trang karaoke
```
http://localhost:7864/
```

### Bước 2: Mở Console
- Bấm **F12** hoặc **Ctrl+Shift+I**
- Chọn tab **Console**

### Bước 3: Copy & Paste script
```javascript
// Copy toàn bộ nội dung file apply_demo_settings.js
// Paste vào console và Enter
```

### Bước 4: Reload và test
1. Reload trang (F5)
2. Chọn file nhạc tên "demo_duyen_troi.mp3"
3. Settings tự động load!

---

## 🎨 Chi tiết Settings Demo

### Màu sắc
- 🔴 **Đỏ (#ff5555)**: Điệp khúc chính, câu kết
- 🟢 **Xanh lá (#55eb55)**: Câu phụ, verse
- 🔵 **Xanh dương (#4ba5ff)**: Verse chính
- 🟡 **Vàng (#ffff6e)**: Từ highlight quan trọng
- 🟣 **Hồng (#ff87eb)**: Intro, bridge, từ lãng mạn
- 🟣 **Tím (#a55fff)**: Verse đặc biệt

### Hiệu ứng

#### 🌊 WAVE (Sóng)
- Intro: "Duyên của trời anh để mặc dần trôi"
- Bridge: "Nhìn anh thấy cô đơn"
- Ending: "duyên"

#### ⚡ FLASH (Nhấp nháy)
- "đèn xanh"
- Chorus: "Bỏ lỡ rồi sẽ tiếc cho mà xem"
- "yêu", "bất thường"
- Ending: Toàn bộ câu cuối

#### ⭐ STAR (Pháo hoa)
- "anh dám nói"
- Chorus: "Bỏ lỡ rồi sẽ tiếc"
- "em", "anh thương"
- "yêu"
- "đầu"
- Ending: Toàn bộ câu cuối

#### ✨ GLOW (Phát sáng)
- Intro: Toàn bộ
- Bridge: Toàn bộ
- "em", "thương", "yêu", "đầu"
- Ending: "Có công mài sắc có ngày nên duyên"

### Nhóm từ (Groups)

#### Group 0 - Intro
"Duyên của trời anh để mặc dần trôi"
- Hiệu ứng: WAVE + GLOW
- Màu: Hồng

#### Group 1 - Verse 1
"Bật không biết mấy đèn xanh rồi"
- Màu: Xanh dương
- Highlight: "đèn xanh" (vàng + FLASH)

#### Group 2 - Chorus
"Bỏ lỡ rồi sẽ tiếc cho mà xem"
- Hiệu ứng: FLASH + STAR
- Màu: Đỏ
- Note: "Điệp khúc chính"

#### Group 3 - Bridge
"Nhìn anh thấy cô đơn"
- Hiệu ứng: WAVE + GLOW
- Màu: Hồng

---

## 📊 Thống kê

- **Tổng số từ**: 95 từ
- **Số nhóm**: 4 groups
- **Màu sắc**: 6 màu khác nhau
- **Hiệu ứng**:
  - WAVE: 13 từ
  - FLASH: 23 từ
  - STAR: 21 từ
  - GLOW: 22 từ
- **Notes**: 1 note (Chorus)

---

## 🎯 Mục đích Demo

Demo này minh họa:

1. ✅ **Lưu settings phức tạp** với nhiều màu sắc và hiệu ứng
2. ✅ **Nhóm từ** (groups) để tạo hiệu ứng đồng bộ
3. ✅ **Kết hợp nhiều hiệu ứng** trên cùng một từ
4. ✅ **Highlight từ quan trọng** bằng màu vàng
5. ✅ **Tạo cảm xúc** qua màu sắc (hồng = lãng mạn, đỏ = mạnh mẽ)
6. ✅ **Auto-load** khi chọn lại file

---

## 🐛 Troubleshooting

### Settings không load?
```javascript
// Kiểm tra trong console
localStorage.getItem('karaoke_song_demo_duyen_troi_mp3_0')
```

### Xóa và thử lại?
```javascript
// Xóa settings
localStorage.removeItem('karaoke_song_demo_duyen_troi_mp3_0')

// Hoặc xóa tất cả
clearAllSongSettings()
```

### File nhạc không khớp?
- Đảm bảo tên file là: **demo_duyen_troi.mp3**
- Hoặc sửa `songId` trong script

---

## 💡 Tips

1. **Thử nghiệm**: Sau khi load demo, vào EDIT mode để xem cấu trúc
2. **Học hỏi**: Xem cách kết hợp màu sắc và hiệu ứng
3. **Tùy chỉnh**: Copy và sửa settings cho bài hát của bạn
4. **Export**: Dùng VTBT để export toàn bộ settings

---

## 🎉 Kết quả mong đợi

Khi chạy demo, bạn sẽ thấy:

- 🌊 Intro với chữ sóng màu hồng phát sáng
- 🔵 Verse màu xanh dương mượt mà
- 🔴 Chorus màu đỏ với pháo hoa và flash
- 🟡 Từ highlight màu vàng nổi bật
- ✨ Ending hoành tráng với tất cả hiệu ứng

**Chúc bạn thành công!** 🎵
