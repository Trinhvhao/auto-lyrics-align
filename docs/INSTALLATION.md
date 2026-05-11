# Setup & Installation Guide - Auto Lyrics Align

## 📋 Yêu Cầu Hệ Thống

- **OS**: Linux, macOS, hoặc Windows
- **Python**: 3.9+
- **RAM**: 8GB tối thiểu (16GB khuyên dùng)
- **GPU**: NVIDIA CUDA 11.8+ (tùy chọn - tăng tốc độ)
- **Disk**: 5GB+ (cho models & dependencies)

---

## 🚀 Cách Cài Đặt

### **Option 1: Dùng Conda (Recommended)**

#### 1. Tạo environment từ file YAML
```bash
cd auto-lyrics-align

# Tạo environment với YAML
conda env create -f environment.yml

# Activate environment
conda activate lyric_env
```

#### 2. Cài pip dependencies nếu có thay đổi
```bash
pip install -r requirements.txt
```

---

### **Option 2: Dùng venv + pip**

#### 1. Tạo virtual environment
```bash
cd auto-lyrics-align
python3 -m venv lyric_env
```

#### 2. Activate environment
```bash
# Linux/macOS
source lyric_env/bin/activate

# Windows
lyric_env\Scripts\activate
```

#### 3. Cài dependencies
```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

---

### **Option 3: Cài Riêng Lẻ (Manual)**

```bash
# 1. PyTorch (chọn phiên bản phù hợp từ https://pytorch.org)
pip install torch torchaudio torchvision

# 2. Core dependencies
pip install fastapi uvicorn pydantic python-multipart

# 3. ML & NLP
pip install transformers numpy tqdm

# 4. Vietnamese NLP
pip install vinorm regtag decorator

# 5. Optional: Video & Audio processing
pip install moviepy Pillow imageio demucs
```

---

## 📦 Các Phiên Bản Requirements

### `requirements.txt` (Bắt buộc)
- Core dependencies cho backend
- Audio & model processing
- Minimalist setup

### `requirements-dev.txt` (Development)
- Testing: pytest, pytest-asyncio
- Code quality: black, flake8, pylint
- Documentation: mkdocs
- Dùng cho developers

### `requirements-ml.txt` (Advanced ML)
- Vocal separation (demucs)
- Transcription (whisperx)
- Video generation (moviepy)
- Dùng cho examples & advanced features

---

## ✅ Kiểm Tra Cài Đặt

### Verify Python & Packages
```bash
# Kiểm tra Python version
python --version

# Kiểm tra PyTorch
python -c "import torch; print(f'PyTorch {torch.__version__}')"

# Kiểm tra CUDA availability (nếu có GPU)
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"

# Kiểm tra các packages chính
python -c "import fastapi, transformers, torchaudio; print('✅ All packages installed')"
```

### Verify File Cấu Trúc
```bash
ls -la
# Kỳ vọng:
# - backend/
# - frontend/
# - models/
# - docs/
# - examples/
# - scripts/
# - requirements.txt
# - environment.yml
# - run.sh
```

---

## 🚀 Chạy Application

### Khởi Động Server
```bash
# Activate environment
conda activate lyric_env

# Chạy server
./run.sh

# Hoặc chi tiết:
cd models/alignment-code
python ../../backend/fastapi_app.py
```

### Access Web UI
```
http://localhost:8000
API docs: http://localhost:8000/docs
```

---

## 🔧 Troubleshooting

### ❌ "ImportError: No module named 'fastapi'"
```bash
# Đảm bảo environment được activate
conda activate lyric_env

# Cài lại
pip install -r requirements.txt
```

### ❌ CUDA/GPU Issues
```bash
# Nếu không có GPU, cài CPU version
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu

# Hoặc modify run.sh để disable GPU
export CUDA_VISIBLE_DEVICES=-1
```

### ❌ Memory Issues với Model Loading
```bash
# Downgrade transformers version
pip install 'transformers<4.35'

# Hoặc disable offloading trong backend
# Xem: backend/fastapi_app.py line ~50
```

### ❌ Port 8000 Already in Use
```bash
# Chạy trên port khác
cd models/alignment-code
python ../../backend/fastapi_app.py --port 8001
```

---

## 📚 Tài Liệu Thêm

Xem các tài liệu chi tiết trong `docs/`:
- [PLAYER_README.md](../docs/PLAYER_README.md) - Hướng dùng web UI
- [LYRICS_ALIGN_README.md](../docs/LYRICS_ALIGN_README.md) - Thuật toán căn chỉnh
- [SETTINGS_README.md](../docs/SETTINGS_README.md) - Cấu hình chi tiết
- [DEMO_GUIDE.md](../docs/DEMO_GUIDE.md) - Demo examples

---

## 💡 Tips

✅ **Lần đầu**: Dùng Conda + `environment.yml` (đơn giản nhất)

✅ **Prod Deployment**: Dùng Docker (xem `Dockerfile` nếu có)

✅ **Development**: Sau khi cài, chạy `pip install -r requirements-dev.txt` thêm

✅ **GPU Optimization**: Update CUDA version để tận dụng tối đa

---

**Happy coding! 🎵**
