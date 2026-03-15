import sys
import os
import asyncio
import json

# Add backend to path
sys.path.append(os.path.join(os.getcwd(), "backend"))

from ai_service import generate_quiz
import ai_service

async def test_ia():
    print("DEBUG: Connecting to Gemini API...")
    texto_prueba = "La fotosintesis es un proceso biologico."
    
    try:
        # Test model directly
        prompt = "Provide a JSON with a single question about photosynthesis."
        response = ai_service.model.generate_content(prompt)
        print("DEBUG: RAW Response received")
        print(response.text)
        
        quiz = await generate_quiz(texto_prueba)
        if quiz and "questions" in quiz:
            print("SUCCESS: Quiz generated")
            print(json.dumps(quiz, indent=2))
        else:
            print("FAILURE: Invalid JSON structure or empty")
    except Exception as e:
        print(f"ERROR: {str(e)}")

if __name__ == "__main__":
    asyncio.run(test_ia())
