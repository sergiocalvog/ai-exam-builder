import os
import json

try:
    from pdf_service import extract_text_from_pdf
    from ai_service import generate_quiz
except ImportError:
    import sys
    sys.path.insert(0, os.path.dirname(__file__))
    from pdf_service import extract_text_from_pdf
    from ai_service import generate_quiz


def handler(request, context):
    if request.method == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type',
            }
        }

    if request.method != 'POST':
        return {
            'statusCode': 405,
            'body': json.dumps({'error': 'Method not allowed'}),
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json',
            }
        }

    try:
        content_type = request.headers.get('content-type', '')
        if 'multipart/form-data' not in content_type:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Only multipart/form-data allowed'}),
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json',
                }
            }

        body = request.get_body()
        boundary = None
        for part in content_type.split(';'):
            if 'boundary' in part:
                boundary = part.split('=')[1].strip()
                break

        if not boundary:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'No boundary found'}),
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json',
                }
            }

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
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'No file provided'}),
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json',
                }
            }

        text = extract_text_from_pdf(file_content)
        if not text:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Could not extract text from PDF'}),
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json',
                }
            }

        quiz = generate_quiz(text, num_questions)
        if not quiz:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': 'Failed to generate quiz with AI'}),
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json',
                }
            }

        return {
            'statusCode': 200,
            'body': json.dumps(quiz),
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json',
            }
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json',
            }
        }
