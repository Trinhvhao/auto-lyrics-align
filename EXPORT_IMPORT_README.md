# 💾 Export & Import Settings - Hướng dẫn

## Tính năng mới

Giờ đây bạn có thể **export settings ra file JSON** và **import lại** một cách dễ dàng!

## ✨ Tính năng

### 1. **Preview từ Edit Mode**
- Trong chế độ EDIT, bấm nút **▶ Preview**
- Xem trực tiếp kết quả với tất cả hiệu ứng
- Bấm **Back** để quay lại edit tiếp

### 2. **Export Settings to JSON**
- Trong chế độ EDIT, bấm nút **💾 Export JSON**
- File JSON sẽ được tải về máy
- Tên file: `karaoke_<songId>_<date>.json`

### 3. **Import Settings from JSON**
- **Cách 1:** Kéo thả file `.json` vào app
- **Cách 2:** Trong MENU, bấm **IMPORT JSON**
- **Cách 3:** Dùng tool `apply_json_settings.html`

## 🎯 Workflow

### Export Settings:

```
1. Vào chế độ EDIT
2. Chỉnh màu, hiệu ứng, groups, etc.
3. Bấm "💾 Export JSON" (desktop) hoặc "💾 Export" (mobile)
4. File JSON được tải về
```

### Import Settings:

**Cách 1 - Drag & Drop:**
```
1. Kéo file .json vào cửa sổ app
2. Settings tự động apply
3. Vào EDIT mode để xem
```

**Cách 2 - Menu Button:**
```
1. Vào MENU
2. Bấm "IMPORT JSON"
3. Chọn file .json
4. Settings tự động apply
```

**Cách 3 - Apply Tool:**
```
1. Mở file apply_json_settings.html
2. Chọn file JSON hoặc dán nội dung
3. Bấm "Apply JSON"
4. Mở app và chọn file nhạc tương ứng
```

## 📊 Nội dung JSON

File JSON chứa toàn bộ settings:

```json
{
  "songId": "music1.mp3_953149",
  "version": "7.6",
  "exportedAt": "2024-01-01T00:00:00.000Z",
  
  "textData": [
    ["Duyên", "#ff87eb", true, false, false, false, 0, "", true],
    ["của", "#ff87eb", false, false, false, false, 0, "", true]
  ],
  
  "autoTimings": [0.5, 1.2, 2.0],
  "autoAudioUrl": "/uploads/audio_xxx.mp3",
  
  "questionData": {
    "active": false,
    "yesText": "",
    "yesLabel": "Yes",
    "noLabel": "No"
  },
  
  "bgPath": {
    "menu": "",
    "display": ""
  },
  
  "bgBase64": {
    "menu": null,
    "display": null
  },
  
  "currentColor": "#f5f5f8",
  "cSize": 20
}
```

## 🔧 TextData Format

Mỗi từ là một array với 9 phần tử:

```javascript
[
  "word",      // 0: Từ
  "#ff87eb",   // 1: Màu sắc
  true,        // 2: WAVE effect
  false,       // 3: FLASH effect
  false,       // 4: STAR effect
  false,       // 5: BURST effect
  0,           // 6: Group ID (-1 = no group)
  "",          // 7: Note text
  true         // 8: GLOW effect
]
```

## 💡 Use Cases

### 1. Backup Settings
```
- Export settings trước khi thử nghiệm
- Nếu hỏng, import lại settings cũ
```

### 2. Share với Team
```
- Export settings
- Gửi file JSON cho đồng nghiệp
- Họ import và có ngay cùng settings
```

### 3. Template Library
```
- Tạo nhiều template khác nhau
- Export thành JSON files
- Import khi cần dùng
```

### 4. Version Control
```
- Lưu các version settings khác nhau
- Dễ dàng quay lại version cũ
- Track changes qua Git
```

## 🎨 Ví dụ: Tạo Template

### Bước 1: Tạo template trong EDIT
```
1. Vào EDIT mode
2. Thêm từ: "Intro", "Verse", "Chorus"
3. Set màu: pink, blue, yellow
4. Add effects: WAVE, FLASH, GLOW
5. Tạo groups
```

### Bước 2: Export
```
1. Bấm "💾 Export JSON"
2. File: karaoke_template_intro_2024-01-01.json
```

### Bước 3: Reuse
```
1. Bắt đầu bài mới
2. Import template JSON
3. Chỉnh sửa từ theo lyrics mới
4. Giữ nguyên màu sắc và hiệu ứng
```

## 🔄 So sánh với localStorage

| Feature | localStorage | JSON Export |
|---------|-------------|-------------|
| Auto-save | ✅ Tự động | ❌ Thủ công |
| Persist | ✅ Luôn có | ✅ File riêng |
| Share | ❌ Không thể | ✅ Dễ dàng |
| Backup | ❌ Khó | ✅ Dễ dàng |
| Version | ❌ Không | ✅ Có |
| Cross-device | ❌ Không | ✅ Có |

## 🚀 Tips & Tricks

### 1. Naming Convention
```
karaoke_<song_name>_<version>_<date>.json

Ví dụ:
- karaoke_duyen_troi_v1_2024-01-01.json
- karaoke_duyen_troi_v2_final_2024-01-05.json
```

### 2. Organize by Folder
```
/karaoke_settings/
  /templates/
    - intro_template.json
    - chorus_template.json
  /songs/
    - song1.json
    - song2.json
  /backup/
    - song1_backup_2024-01-01.json
```

### 3. Git Version Control
```bash
# Initialize repo
git init karaoke_settings
cd karaoke_settings

# Add settings
git add karaoke_duyen_troi.json
git commit -m "Add Duyên Trời settings v1"

# Make changes
git add karaoke_duyen_troi.json
git commit -m "Update: add more GLOW effects"

# Revert if needed
git checkout HEAD~1 karaoke_duyen_troi.json
```

### 4. Batch Processing
```javascript
// Script để apply nhiều settings cùng lúc
const settings = [
  'song1.json',
  'song2.json',
  'song3.json'
];

settings.forEach(file => {
  fetch(file)
    .then(r => r.json())
    .then(data => {
      const key = 'karaoke_song_' + data.songId;
      localStorage.setItem(key, JSON.stringify(data));
      console.log('✓ Applied:', file);
    });
});
```

## 📱 Mobile Support

Trên mobile:
- **Preview:** Bấm nút "▶ Preview" (giữa Clear All và Export)
- **Export:** Bấm nút "💾 Export" (bên phải)
- **Import:** Dùng menu "IMPORT JSON" hoặc share file qua AirDrop/Bluetooth

## 🐛 Troubleshooting

### Settings không apply?
```
1. Kiểm tra songId trong JSON
2. Đảm bảo file nhạc có cùng tên + size
3. Xem console log để debug
```

### File JSON quá lớn?
```
- Xóa bgBase64 nếu không cần background
- Chỉ giữ textData và autoTimings
- Nén file bằng gzip
```

### Import bị lỗi?
```
1. Validate JSON: jsonlint.com
2. Kiểm tra format textData
3. Xem error message trong console
```

## 🎓 Advanced: Edit JSON Manually

Bạn có thể edit JSON trực tiếp:

```json
{
  "textData": [
    // Thêm từ mới
    ["Hello", "#ff5555", true, true, false, false, -1, "", false],
    
    // Copy từ cũ và sửa màu
    ["World", "#55eb55", false, false, true, false, 0, "", true]
  ]
}
```

Sau đó import lại vào app!

## 📚 Resources

- `apply_json_settings.html` - Tool để apply JSON
- `SETTINGS_README.md` - Hướng dẫn localStorage
- `DEMO_GUIDE.md` - Demo settings mẫu

---

**Tác giả:** Kiro AI Assistant  
**Version:** 7.6  
**Ngày:** 2024
