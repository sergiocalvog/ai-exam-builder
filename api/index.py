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
    return {"status": "ok", "message": "AI Exam Builder API is running"}

@app.post("/api/generate")
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
            raise HTTPException(status_code=500, detail="Failed to generate quiz with AI")
            
        return quiz
    except Exception as e:
        print(f"Server Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
