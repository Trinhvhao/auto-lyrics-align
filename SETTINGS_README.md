# 💾 Hệ thống Lưu Settings Tự Động

## Tính năng mới

Hệ thống karaoke giờ đây **tự động lưu settings** cho từng bài nhạc vào **localStorage** của trình duyệt. Mỗi khi bạn chọn lại cùng một file nhạc, tất cả settings sẽ được khôi phục tự động!

## ✨ Những gì được lưu

Cho mỗi bài nhạc, hệ thống lưu:

- ✅ **Lyrics đã alignment** (textData)
- ✅ **Timing tự động** (autoTimings) 
- ✅ **Màu sắc chữ** (currentColor)
- ✅ **Hiệu ứng** (WAVE, FLASH, STAR, BURST, GLOW)
- ✅ **Nhóm từ** (groups)
- ✅ **Ghi chú** (notes)
- ✅ **Background** (menu & display)
- ✅ **Question data**
- ✅ **Audio URL**

## 🎯 Cách hoạt động

### 1. Lần đầu tiên với bài nhạc mới

```
1. Chọn file nhạc → Hệ thống tạo ID duy nhất
2. Nhập lyrics → Chạy Auto Align
3. Settings tự động lưu vào localStorage
```

### 2. Lần sau với cùng bài nhạc

```
1. Chọn lại file nhạc (cùng tên + kích thước)
2. ✓ Settings tự động load!
3. Lyrics, timing, màu sắc, hiệu ứng đều được khôi phục
4. Có thể bỏ qua bước alignment
```

## 🔑 Song ID

Mỗi bài nhạc được nhận diện bằng:
- **Tên file** + **Kích thước file**
- Ví dụ: `bai_hat_mp3_5242880` (tên file + size)

⚠️ **Lưu ý**: Nếu file nhạc bị sửa đổi (size thay đổi), sẽ được coi là bài mới.

## 🎮 Các nút điều khiển

### Trong Auto Panel:

1. **🗑 Xóa settings** 
   - Xóa settings của bài nhạc hiện tại
   - Cần confirm trước khi xóa

2. **📋 Danh sách**
   - Xem tất cả bài nhạc đã lưu
   - Hiển thị: số từ, số mốc timing, thời gian lưu

## 💡 Tự động lưu

Settings được tự động lưu khi:

- ✅ Hoàn thành alignment
- ✅ Thay đổi màu sắc chữ
- ✅ Bật/tắt hiệu ứng (WAVE, FLASH, etc.)
- ✅ Tạo/xóa nhóm từ
- ✅ Thêm/sửa/xóa từ
- ✅ Thay đổi background

## 🔧 Console Commands

Mở Developer Console (F12) để dùng các lệnh:

```javascript
// Xem tất cả bài đã lưu
listSavedSongs()

// Xóa settings bài hiện tại
clearCurrentSongSettings()

// Xóa TẤT CẢ settings (dọn dẹp)
clearAllSongSettings()

// Xem Song ID hiện tại
console.log(currentSongId)
```

## 📊 Dung lượng localStorage

- **Giới hạn**: ~5-10MB tùy trình duyệt
- **Mỗi bài**: ~50-500KB tùy độ dài
- **Ước tính**: Có thể lưu 10-100 bài

⚠️ Nếu đầy, sẽ hiện toast: "⚠️ Bộ nhớ đầy - không thể lưu"

## 🚀 Workflow khuyến nghị

### Lần đầu:
```
1. Chọn file nhạc
2. Nhập lyrics
3. Chạy Auto Align
4. Chỉnh màu, hiệu ứng
5. → Tự động lưu!
```

### Lần sau:
```
1. Chọn lại file nhạc
2. ✓ Mọi thứ đã load sẵn!
3. Bấm "Bỏ qua →" để vào menu
4. START để xem ngay
```

## 🐛 Troubleshooting

### Settings không load?
- Kiểm tra tên file và size có giống không
- Xem console log: `🎵 Song ID: ...`
- Thử xóa và tạo lại

### Bộ nhớ đầy?
- Dùng `clearAllSongSettings()` để dọn dẹp
- Hoặc xóa từng bài không cần thiết

### Settings bị mất?
- localStorage bị xóa khi:
  - Clear browser data
  - Incognito mode
  - Khác domain/port

## 📝 Technical Details

### Storage Key Format
```
karaoke_song_<filename>_<size>
```

### Data Structure
```javascript
{
  songId: "bai_hat_mp3_5242880",
  textData: [...],
  autoTimings: [...],
  currentColor: "#f5f5f8",
  bgPath: { menu: "...", display: "..." },
  savedAt: "2024-01-01T00:00:00.000Z"
}
```

## 🎉 Lợi ích

- ⚡ **Tiết kiệm thời gian**: Không cần alignment lại
- 💾 **Bảo toàn công sức**: Màu sắc, hiệu ứng được giữ nguyên
- 🔄 **Làm việc liên tục**: Thoát ra vào lại không mất gì
- 🎨 **Thử nghiệm thoải mái**: Luôn có thể quay lại settings cũ

---

**Tác giả**: Kiro AI Assistant  
**Phiên bản**: 1.0  
**Ngày**: 2024
