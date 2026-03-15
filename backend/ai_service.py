import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-flash-latest")

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

async def generate_quiz(text: str, num_questions: int = 10):
    """
    Generates a quiz using Gemini API.
    """
    try:
        prompt = PROMPT_TEMPLATE.format(text=text[:15000]) + f"\nIMPORTANTE: Genera exactamente {num_questions} preguntas."
        response = model.generate_content(prompt)
        
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
        print(f"Error generating quiz: {e}")
        return None
