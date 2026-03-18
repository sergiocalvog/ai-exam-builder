import os
import sys
from http.server import BaseHTTPRequestHandler
import json

sys.path.insert(0, os.path.dirname(__file__))

from pdf_service import extract_text_from_pdf
from ai_service import generate_quiz

class handler(BaseHTTPRequestHandler):
    def cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Content-Type', 'application/json')

    def do_OPTIONS(self):
        self.send_response(200)
        self.cors_headers()
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.cors_headers()
        self.end_headers()
        self.wfile.write(json.dumps({"message": "Examiname API is running"}).encode())
        return

    def do_POST(self):
        if self.path != '/api/generate':
            self.send_response(404)
            self.cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Not found"}).encode())
            return

        try:
            content_type = self.headers.get('Content-Type', '')
            if 'multipart/form-data' not in content_type:
                self.send_response(400)
                self.cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Only multipart/form-data allowed"}).encode())
                return

            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)

            boundary = None
            for part in content_type.split(';'):
                if 'boundary' in part:
                    boundary = part.split('=')[1].strip()
                    break

            if not boundary:
                self.send_response(400)
                self.cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({"error": "No boundary found"}).encode())
                return

            boundary = boundary.encode()
            
            parts = body.split(b'--' + boundary)
            file_content = None
            num_questions = 10

            for part in parts:
                if b'Content-Disposition' in part and b'filename=' in part:
                    header_end = part.find(b'\r\n\r\n')
                    if header_end != -1:
                        file_content = part[header_end + 4:]
                        if file_content.endswith(b'\r\n'):
                            file_content = file_content[:-2]
                elif b'num_questions' in part:
                    value_start = part.find(b'\r\n\r\n') + 4
                    if value_start > 4:
                        try:
                            num_questions = int(part[value_start:].strip())
                        except:
                            num_questions = 10

            if not file_content:
                self.send_response(400)
                self.cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({"error": "No file provided"}).encode())
                return

            text = extract_text_from_pdf(file_content)
            if not text:
                self.send_response(400)
                self.cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Could not extract text from PDF"}).encode())
                return

            quiz = generate_quiz(text, num_questions)
            if not quiz:
                self.send_response(500)
                self.cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Failed to generate quiz with AI"}).encode())
                return

            self.send_response(200)
            self.cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps(quiz).encode())

        except Exception as e:
            print(f"Error: {e}")
            self.send_response(500)
            self.cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())
