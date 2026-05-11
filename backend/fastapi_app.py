import sys
import os
import uuid
from typing import Any, Dict, List

import torch
import torchaudio
import torchaudio.transforms as T
from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
ALIGNMENT_CODE_PATH = os.path.join(PROJECT_ROOT, "models", "alignment-code")
FRONTEND_PATH = os.path.join(PROJECT_ROOT, "frontend")
UPLOAD_DIR = os.path.join(PROJECT_ROOT, "uploads")

# Import alignment module
os.chdir(ALIGNMENT_CODE_PATH)
sys.path.insert(0, ALIGNMENT_CODE_PATH)
import predict

app = FastAPI(title="Vietnamese Lyric Alignment API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup
os.makedirs(UPLOAD_DIR, exist_ok=True)
app.mount("/static", StaticFiles(directory=os.path.join(FRONTEND_PATH, "static")), name="static")
app.mount("/media", StaticFiles(directory=UPLOAD_DIR), name="media")

is_model_loaded = False

def load_and_preprocess_audio(audio_path: str) -> torch.Tensor:
    print(f"Loading audio: {audio_path}")
    wav, sr = torchaudio.load(audio_path)
    
    if len(wav.shape) > 1 and wav.shape[0] > 1:
        wav = wav.mean(dim=0, keepdim=True)
        
    if sr != 16000:
        resampler = T.Resample(sr, 16000)
        wav = resampler(wav)
        
    return wav

def lyrics_text_to_segments(lyrics_text: str) -> List[Dict[str, Any]]:
    lines = lyrics_text.strip().split('\n')
    lyric_segments: List[Dict[str, Any]] = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        words = line.split()
        segment = {
            "s": 0, "e": 0,
            "l": [{"s": 0, "e": 0, "d": w} for w in words]
        }
        lyric_segments.append(segment)
        
    return lyric_segments

@app.on_event("startup")
def load_model_on_startup():
    global is_model_loaded
    if not is_model_loaded:
        print("Loading AI Model (Wav2Vec2)...")
        model_path = os.path.join(PROJECT_ROOT, "models", "lyric-alignment")
        predict.model_path = model_path
        predict.load_model()
        is_model_loaded = True
        print("AI Model loaded!")

@app.get("/")
def serve_frontend():
    return FileResponse(os.path.join(FRONTEND_PATH, "static", "auto_karaoke.html"))

@app.get("/player")
def serve_player():
    return FileResponse(os.path.join(FRONTEND_PATH, "static", "player.html"))

@app.get("/auto")
def serve_auto_karaoke():
    return FileResponse(os.path.join(FRONTEND_PATH, "static", "auto_karaoke.html"))

@app.post("/api/align")
async def align_service(request: Request):
    """Handle alignment with multipart form data"""
    try:
        form_data = await request.form()
        lyrics_text = form_data.get("lyric_text")
        audio_file = form_data.get("audio_file")
        
        print(f"[DEBUG] Form keys: {list(form_data.keys())}")
        print(f"[DEBUG] lyrics text exists: {lyrics_text is not None}")
        print(f"[DEBUG] audio_file exists: {audio_file is not None}")
        
        if not lyrics_text or not str(lyrics_text).strip():
            raise HTTPException(
                status_code=400,
                detail="Please provide lyrics text in form field 'lyric_text'."
            )
        
        if not audio_file:
            raise HTTPException(status_code=400, detail="Please upload audio file.")
        
        lyrics_text = str(lyrics_text).strip()
        
        # Save file
        filename = audio_file.filename if hasattr(audio_file, 'filename') else 'audio.mp3'
        file_ext = os.path.splitext(filename)[1] or ".mp3"
        safe_filename = f"audio_{uuid.uuid4().hex}{file_ext}"
        saved_path = os.path.join(UPLOAD_DIR, safe_filename)
        
        content = await audio_file.read()
        with open(saved_path, "wb") as f:
            f.write(content)
        print(f"[DEBUG] File saved: {saved_path}, size: {len(content)} bytes")
        
        # Process audio
        wav = load_and_preprocess_audio(saved_path)
        
        # Format lyrics
        lyric_segments = lyrics_text_to_segments(lyrics_text)
        print(f"[DEBUG] lyric segments: {len(lyric_segments)}")
        
        # Align
        print("Processing alignment...")
        alignment_result = predict.handle_sample(wav, lyric_segments)
        
        return JSONResponse(content={
            "audio_url": f"/media/{safe_filename}",
            "alignment": alignment_result
        })
        
    except HTTPException:
        raise
    except Exception as e:
        import traceback
        error_msg = f"Error: {str(e)}\n{traceback.format_exc()}"
        print(error_msg)
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("fastapi_app:app", host="0.0.0.0", port=7864, reload=False)
