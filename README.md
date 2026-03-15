# AI Exam Builder

Generador de exámenes inteligente basado en PDFs utilizando Google Gemini AI.

## Estructura del Proyecto

- `backend/`: API construida con FastAPI.
- `frontend/`: Aplicación React + Vite.

## Requisitos Previos

1. Python 3.8+
2. Node.js 18+
3. Gemini API Key (Obtenla en [Google AI Studio](https://aistudio.google.com/))

## Instalación y Ejecución

### 1. Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # Añade tu API Key al archivo .env
python main.py
```

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

## Características

- ✨ Generación automática de preguntas basada en el contenido del PDF.
- 🎨 Diseño moderno con Glassmorphism.
- ⏱️ Feedback inmediato y puntuación final.
- 📚 Explicaciones detalladas para cada respuesta.
