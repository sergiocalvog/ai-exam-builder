from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# Adjust path to import local services
sys.path.insert(0, os.path.dirname(__file__))
from pdf_service import extract_text_from_pdf
from ai_service import generate_quiz

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request, call_next):
    print(f"DEBUG: Request to {request.url.path} [{request.method}]")
    response = await call_next(request)
    return response

@app.get("/api/generate")
@app.get("/")
async def health_check():
    return {"status": "ok", "message": "API is running with modern GenAI", "env_key_present": bool(os.getenv("GEMINI_API_KEY"))}

@app.api_route("/{path:path}", methods=["GET", "POST", "OPTIONS"])
async def catch_all(path: str = "", file: UploadFile = File(None), num_questions: int = 10):
    # This catch-all handles both the root and subpaths
    if (path in ["api/generate", "generate"] or not path) and file:
        return await generate(file, num_questions)
    
    return {"status": "ok", "message": f"API is alive at path: {path}"}

@app.post("/api/generate")
@app.post("/")
async def generate(file: UploadFile = File(...), num_questions: int = 10):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    try:
        contents = await file.read()
        text = extract_text_from_pdf(contents)
        
        if not text:
            raise HTTPException(status_code=400, detail="Could not extract text from PDF")
            
        quiz = generate_quiz(text, num_questions)
        
        if not quiz:
            raise HTTPException(status_code=500, detail="AI generation failed. Check GEMINI_API_KEY.")
            
        return quiz
    except Exception as e:
        print(f"Server Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
