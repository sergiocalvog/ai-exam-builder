import os
import json
import io
import fitz  # PyMuPDF
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# PDF service logic (Inlined)
def extract_text(stream):
    try:
        doc = fitz.open(stream=stream, filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        print(f"PDF Error: {e}")
        return None

# AI Service logic (Inlined with modern google-genai)
PROMPT_TEMPLATE = """
Eres un experto en educación. A partir del siguiente texto extraído de un PDF, genera un examen de opción múltiple en formato JSON.

**IMPORTANTE: ALEATORIEDAD Y DIVERSIDAD**
- Genera preguntas variadas sobre diferentes partes del texto.
- Asegúrate de que las preguntas sean aleatorias y no se repitan si se solicita el examen varias veces sobre el mismo texto.
- Cambia el enfoque de las preguntas (algunas de memoria, otras de comprensión, otras de aplicación).

El JSON debe tener la siguiente estructura:
{{
  "title": "Evaluación de Examíname",
  "questions": [
    {{
      "id": 1,
      "question": "Texto de la pregunta",
      "options": ["A", "B", "C", "D"],
      "correctAnswer": 0,
      "explanation": "Breve explicación de por qué es la respuesta correcta"
    }}
  ]
}}

Genera preguntas variadas. Asegúrate de que el formato JSON sea válido y no incluya markdown extra (solo el JSON).

TEXTO:
{text}
"""

@app.get("/api/generate")
@app.get("/")
async def health():
    return {
        "status": "ok", 
        "message": "AI Exam Builder API is running",
        "env_key_present": bool(os.getenv("GEMINI_API_KEY"))
    }

@app.post("/api/generate")
@app.post("/")
async def generate(file: UploadFile = File(...), num_questions: int = 10):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY not configured in Vercel")

    try:
        # 1. Read PDF
        contents = await file.read()
        text = extract_text(contents)
        if not text:
            raise HTTPException(status_code=400, detail="Could not extract text from PDF")
            
        # 2. Setup AI Client
        client = genai.Client(api_key=api_key)
        prompt = PROMPT_TEMPLATE.format(text=text[:15000]) + f"\nIMPORTANTE: Genera exactamente {num_questions} preguntas."
        
        # 3. Generate content
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        
        content = response.text
        # Robust JSON extraction
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
        
        # Strip any leading/trailing non-JSON characters
        start = content.find('{')
        end = content.rfind('}') + 1
        if start != -1 and end != 0:
            content = content[start:end]
            
        return json.loads(content)
        
    except Exception as e:
        print(f"Critical Server Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
