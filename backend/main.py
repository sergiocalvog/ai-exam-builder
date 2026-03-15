from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pdf_service import extract_text_from_pdf
from ai_service import generate_quiz
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "AI Exam Builder API is running"}

@app.post("/api/generate")
async def generate_from_pdf(file: UploadFile = File(...), num_questions: int = 10):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    try:
        contents = await file.read()
        text = extract_text_from_pdf(contents)
        
        if not text:
            raise HTTPException(status_code=400, detail="Could not extract text from PDF")
            
        quiz = await generate_quiz(text, num_questions)
        
        if not quiz:
            raise HTTPException(status_code=500, detail="Failed to generate quiz with AI")
            
        return quiz
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    # Use PORT environment variable for cloud hosting like Render/Railway
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
