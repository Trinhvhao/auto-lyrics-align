// ============================================================
// DEMO SETTINGS - DUYÊN TRỜI
// ============================================================
// Copy toàn bộ file này và paste vào Console (F12) của trang auto_karaoke.html
// Sau đó chọn file nhạc có tên "demo_duyen_troi.mp3" (hoặc tạo file giả)

const demoSettings = {
  songId: "demo_duyen_troi_mp3_0",
  bgPickTarget: "both",
  bgPath: { menu: "", display: "" },
  bgBase64: { menu: null, display: null },
  bgMime: { menu: null, display: null },
  currentColor: "#f5f5f8",
  cSize: 20,
  
  // Text data: [word, color, wave, flash, star, burst, groupId, note, glow]
  textData: [
    // Intro - Group 0 (Màu hồng, WAVE + GLOW)
    ["Duyên", "#ff87eb", true, false, false, false, 0, "", true],
    ["của", "#ff87eb", true, false, false, false, 0, "", true],
    ["trời", "#ff87eb", true, false, false, false, 0, "", true],
    ["anh", "#ff87eb", true, false, false, false, 0, "", true],
    ["để", "#ff87eb", true, false, false, false, 0, "", true],
    ["mặc", "#ff87eb", true, false, false, false, 0, "", true],
    ["dần", "#ff87eb", true, false, false, false, 0, "", true],
    ["trôi", "#ff87eb", true, false, false, false, 0, "", true],
    
    // Verse 1 - Group 1 (Màu xanh dương)
    ["Bật", "#4ba5ff", false, false, false, false, 1, "", false],
    ["không", "#4ba5ff", false, false, false, false, 1, "", false],
    ["biết", "#4ba5ff", false, false, false, false, 1, "", false],
    ["mấy", "#4ba5ff", false, false, false, false, 1, "", false],
    ["đèn", "#ffff6e", false, true, false, false, 1, "", false],
    ["xanh", "#ffff6e", false, true, false, false, 1, "", false],
    ["rồi", "#4ba5ff", false, false, false, false, 1, "", false],
    
    // Verse 2 (Màu xanh lá)
    ["Chỉ", "#55eb55", false, false, false, false, -1, "", false],
    ["chờ", "#55eb55", false, false, false, false, -1, "", false],
    ["anh", "#ffff6e", false, false, true, false, -1, "", false],
    ["dám", "#ffff6e", false, false, true, false, -1, "", false],
    ["nói", "#ffff6e", false, false, true, false, -1, "", false],
    
    // Chorus 1 - Group 2 (Màu đỏ, FLASH + STAR)
    ["Bỏ", "#ff5555", false, true, true, false, 2, "Điệp khúc chính", false],
    ["lỡ", "#ff5555", false, true, true, false, 2, "", false],
    ["rồi", "#ff5555", false, true, true, false, 2, "", false],
    ["sẽ", "#ff5555", false, true, true, false, 2, "", false],
    ["tiếc", "#ffff6e", false, true, true, false, 2, "", true],
    ["cho", "#ff5555", false, true, true, false, 2, "", false],
    ["mà", "#ff5555", false, true, true, false, 2, "", false],
    ["xem", "#ff5555", false, true, true, false, 2, "", false],
    
    // Verse 3 (Màu tím)
    ["Người", "#a55fff", false, false, false, false, -1, "", false],
    ["như", "#a55fff", false, false, false, false, -1, "", false],
    ["anh", "#ffff6e", false, false, false, false, -1, "", false],
    ["xứng", "#a55fff", false, false, false, false, -1, "", false],
    ["đáng", "#a55fff", false, false, false, false, -1, "", false],
    ["có", "#a55fff", false, false, false, false, -1, "", false],
    ["em", "#ff87eb", false, false, true, false, -1, "", true],
    
    // Verse 4 (Màu xanh lá)
    ["Đừng", "#55eb55", false, false, false, false, -1, "", false],
    ["suy", "#55eb55", false, false, false, false, -1, "", false],
    ["nghĩ", "#55eb55", false, false, false, false, -1, "", false],
    ["thêm", "#55eb55", false, false, false, false, -1, "", false],
    
    // Bridge - Group 3 (Màu hồng, WAVE + GLOW)
    ["Nhìn", "#ff87eb", true, false, false, false, 3, "", true],
    ["anh", "#ff87eb", true, false, false, false, 3, "", true],
    ["thấy", "#ff87eb", true, false, false, false, 3, "", true],
    ["cô", "#ff87eb", true, false, false, false, 3, "", true],
    ["đơn", "#ff87eb", true, false, false, false, 3, "", true],
    
    // Verse 5 (Màu xanh dương)
    ["Nên", "#4ba5ff", false, false, false, false, -1, "", false],
    ["là", "#4ba5ff", false, false, false, false, -1, "", false],
    ["em", "#ff87eb", false, false, false, false, -1, "", false],
    ["cho", "#4ba5ff", false, false, false, false, -1, "", false],
    ["phép", "#4ba5ff", false, false, false, false, -1, "", false],
    ["anh", "#ffff6e", false, false, true, false, -1, "", false],
    ["thương", "#ffff6e", false, false, true, false, -1, "", true],
    
    // Verse 6 (Màu xanh lá)
    ["Mong", "#55eb55", false, false, false, false, -1, "", false],
    ["anh", "#55eb55", false, false, false, false, -1, "", false],
    ["hiểu", "#55eb55", false, false, false, false, -1, "", false],
    ["em", "#ff87eb", false, false, false, false, -1, "", false],
    ["hơn", "#55eb55", false, false, false, false, -1, "", false],
    
    // Verse 7 (Màu tím)
    ["Bởi", "#a55fff", false, false, false, false, -1, "", false],
    ["vì", "#a55fff", false, false, false, false, -1, "", false],
    ["em", "#ff87eb", false, false, false, false, -1, "", false],
    ["lúc", "#a55fff", false, false, false, false, -1, "", false],
    ["yêu", "#ffff6e", false, true, true, false, -1, "", true],
    ["rất", "#a55fff", false, false, false, false, -1, "", false],
    ["là", "#a55fff", false, false, false, false, -1, "", false],
    ["bất", "#ffff6e", false, true, false, false, -1, "", false],
    ["thường", "#ffff6e", false, true, false, false, -1, "", false],
    
    // Verse 8 (Màu xanh dương)
    ["Dù", "#4ba5ff", false, false, false, false, -1, "", false],
    ["chưa", "#4ba5ff", false, false, false, false, -1, "", false],
    ["rõ", "#4ba5ff", false, false, false, false, -1, "", false],
    ["nông", "#4ba5ff", false, false, false, false, -1, "", false],
    ["sâu", "#4ba5ff", false, false, false, false, -1, "", false],
    
    // Verse 9 (Màu xanh lá)
    ["Nhưng", "#55eb55", false, false, false, false, -1, "", false],
    ["mà", "#55eb55", false, false, false, false, -1, "", false],
    ["anh", "#ffff6e", false, false, false, false, -1, "", false],
    ["cứ", "#55eb55", false, false, false, false, -1, "", false],
    ["mãi", "#55eb55", false, false, false, false, -1, "", false],
    ["trong", "#55eb55", false, false, false, false, -1, "", false],
    ["đầu", "#ffff6e", false, false, true, false, -1, "", true],
    
    // Ending (Màu đỏ, FLASH + STAR + GLOW)
    ["Bởi", "#ff5555", false, true, true, false, -1, "", false],
    ["người", "#ff5555", false, true, true, false, -1, "", false],
    ["xưa", "#ff5555", false, true, true, false, -1, "", false],
    ["mới", "#ff5555", false, true, true, false, -1, "", false],
    ["hay", "#ff5555", false, true, true, false, -1, "", false],
    ["có", "#ff5555", false, true, true, false, -1, "", false],
    ["câu", "#ff5555", false, true, true, false, -1, "", false],
    ["Có", "#ffff6e", false, true, true, false, -1, "", true],
    ["công", "#ffff6e", false, true, true, false, -1, "", true],
    ["mài", "#ffff6e", false, true, true, false, -1, "", true],
    ["sắc", "#ffff6e", false, true, true, false, -1, "", true],
    ["có", "#ffff6e", false, true, true, false, -1, "", true],
    ["ngày", "#ffff6e", false, true, true, false, -1, "", true],
    ["nên", "#ffff6e", false, true, true, false, -1, "", true],
    ["duyên", "#ff87eb", true, true, true, false, -1, "", true]
  ],
  
  questionData: {
    active: false,
    yesText: "",
    yesLabel: "Yes",
    noLabel: "No"
  },
  
  autoTimings: [],
  autoAudioUrl: null,
  savedAt: new Date().toISOString()
};

// Apply settings to localStorage
try {
  const key = 'karaoke_song_' + demoSettings.songId;
  localStorage.setItem(key, JSON.stringify(demoSettings));
  
  console.log('✅ Demo settings applied successfully!');
  console.log('📊 Stats:');
  console.log('  - Song ID:', demoSettings.songId);
  console.log('  - Total words:', demoSettings.textData.length);
  console.log('  - Groups: 4 (Intro, Verse, Chorus, Bridge)');
  console.log('  - Effects: WAVE, FLASH, STAR, GLOW');
  console.log('');
  console.log('🎯 Next steps:');
  console.log('  1. Tạo file nhạc tên "demo_duyen_troi.mp3" (hoặc bất kỳ file nào)');
  console.log('  2. Chọn file đó trong Auto Panel');
  console.log('  3. Settings sẽ tự động load!');
  console.log('  4. Bấm "Bỏ qua →" để vào menu');
  console.log('  5. Bấm START để xem demo!');
  
} catch(e) {
  console.error('❌ Error applying settings:', e);
}
