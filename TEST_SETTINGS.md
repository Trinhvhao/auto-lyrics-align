# 🧪 Test Settings System

## ✅ Đã sửa

### 1. **Bảo vệ chống ghi đè**
- Khi chọn file đã có settings → Hiện cảnh báo
- Nút đổi màu: `⚠️ Alignment (Ghi đè)` (cam)
- Popup confirm trước khi ghi đè

### 2. **Giữ settings khi bỏ qua**
- Bấm "Bỏ qua →" → Giữ nguyên textData đã load
- Toast: `✓ Đã giữ settings (X từ)`

### 3. **Restore backgrounds**
- Load lại menu background từ base64
- Load lại display background từ base64
- Load lại audio URL

## 🧪 Test Cases

### Test 1: Load settings lần đầu
```
1. Chọn file: "✓ ：)#capcut #music #sieunhannhay.mp3"
2. Kết quả mong đợi:
   ✓ Đã load settings (92 từ, 92 mốc)
   💾 Settings đã lưu - Có thể bỏ qua alignment
   ⚠️ Chạy alignment sẽ GHI ĐÈ settings này!
   Nút: "⚠️ Alignment (Ghi đè)" (màu cam)
```

### Test 2: Bỏ qua và giữ settings
```
1. Chọn file có settings
2. Bấm "Bỏ qua →"
3. Kết quả mong đợi:
   - Toast: "✓ Đã giữ settings (92 từ)"
   - Vào MENU state
   - textData vẫn còn 92 từ
   - autoTimings vẫn còn 92 mốc
```

### Test 3: Vào EDIT mode
```
1. Chọn file có settings
2. Bỏ qua → MENU
3. Bấm EDIT
4. Kết quả mong đợi:
   - Thấy 92 từ trong edit box
   - Màu sắc đúng
   - Hiệu ứng đúng
```

### Test 4: START và xem
```
1. Chọn file có settings
2. Bỏ qua → MENU
3. Bấm START
4. Kết quả mong đợi:
   - Hiển thị 92 từ
   - Màu sắc đúng
   - Hiệu ứng hoạt động
   - Background hiển thị (nếu có)
```

### Test 5: Cảnh báo ghi đè
```
1. Chọn file có settings (92 từ)
2. Bấm "⚠️ Alignment (Ghi đè)"
3. Kết quả mong đợi:
   - Popup hiện:
     "⚠️ Đã có settings cho bài này!
      Số từ hiện tại: 92
      Số mốc timing: 92
      Lưu lúc: [timestamp]
      
      Chạy alignment sẽ GHI ĐÈ settings cũ.
      Bạn có chắc muốn tiếp tục?"
   - Bấm Cancel → Không làm gì
   - Bấm OK → Chạy alignment
```

### Test 6: Ghi đè thành công
```
1. Chọn file có settings
2. Sửa lyrics
3. Bấm "⚠️ Alignment (Ghi đè)"
4. Confirm OK
5. Kết quả mong đợi:
   - Chạy alignment mới
   - Settings cũ bị ghi đè
   - Lưu settings mới
```

## 🐛 Debug Commands

### Kiểm tra settings trong localStorage
```javascript
// Xem tất cả keys
Object.keys(localStorage).filter(k => k.startsWith('karaoke_song_'))

// Xem settings của bài cụ thể
const songId = currentSongId; // Hoặc copy từ console log
const key = 'karaoke_song_' + songId;
const settings = JSON.parse(localStorage.getItem(key));
console.log(settings);

// Kiểm tra textData
console.log('Words:', settings.textData.length);
console.log('Timings:', settings.autoTimings.length);
console.log('Audio URL:', settings.autoAudioUrl);
```

### Kiểm tra state hiện tại
```javascript
console.log('Current state:', state);
console.log('Text data:', textData.length);
console.log('Auto timings:', autoTimings.length);
console.log('Current song ID:', currentSongId);
console.log('Audio:', autoAudio);
```

### Force reload settings
```javascript
// Reload settings manually
if (currentSongId) {
  loadSettings(currentSongId);
  console.log('Reloaded:', textData.length, 'words');
}
```

## 📊 Expected Behavior

### Khi chọn file CÓ settings:
```
1. Load settings từ localStorage
2. Restore textData (92 từ)
3. Restore autoTimings (92 mốc)
4. Restore backgrounds (nếu có)
5. Restore audio URL
6. Pre-fill lyrics textarea
7. Hiện cảnh báo ghi đè
8. Đổi màu nút sang cam
```

### Khi bấm "Bỏ qua":
```
1. Giữ nguyên textData
2. Giữ nguyên autoTimings
3. Giữ nguyên backgrounds
4. Giữ nguyên audio
5. Chuyển sang MENU state
6. Hiện toast confirm
```

### Khi bấm START:
```
1. Chuyển sang DISPLAY state
2. Render textData lên canvas
3. Hiển thị backgrounds
4. Nếu có autoTimings + audio → Auto play
5. Nếu không → Manual advance
```

## ✅ Checklist

- [x] Load settings khi chọn file
- [x] Hiện cảnh báo ghi đè
- [x] Popup confirm trước khi ghi đè
- [x] Giữ settings khi bỏ qua
- [x] Restore backgrounds
- [x] Restore audio
- [x] Pre-fill lyrics
- [x] Đổi màu nút cảnh báo
- [x] Toast notifications
- [x] Console logs

## 🎯 Kết quả mong đợi

Sau khi sửa, workflow sẽ là:

```
1. Chọn file "sieunhannhay.mp3"
   → Load 92 từ + 92 mốc
   → Hiện cảnh báo

2. Bấm "Bỏ qua →"
   → Toast: "✓ Đã giữ settings (92 từ)"
   → Vào MENU

3. Bấm START
   → Hiển thị 92 từ với màu sắc + hiệu ứng
   → Background hiển thị
   → Auto play nếu có audio

4. Hoặc bấm EDIT
   → Thấy 92 từ trong edit mode
   → Có thể chỉnh sửa
   → Auto-save khi thay đổi
```

**Tất cả settings đều được giữ nguyên!** ✨
