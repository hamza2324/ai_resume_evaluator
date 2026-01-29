from flask import Flask, request, render_template, jsonify
import os
import json
from resume_processor import extract_text
from evaluator import evaluate_resume

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    """Render home page"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle resume upload and evaluation"""
    
    # Check if file is present
    if 'resume' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['resume']
    
    # Check if file is selected
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    # Check file extension
    if not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type. Please upload PDF or DOCX"}), 400
    
    # Check file size (10MB limit)
    file.seek(0, os.SEEK_END)
    file_size = file.tell()
    file.seek(0)
    
    if file_size > 10 * 1024 * 1024:
        return jsonify({"error": "File size exceeds 10MB limit"}), 400

    try:
        # Save file
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # Extract text from resume
        text = extract_text(filepath)
        
        if not text.strip():
            return jsonify({"error": "Could not extract text from resume. Please ensure the file is readable."}), 400

        # Evaluate resume using Groq API
        feedback = evaluate_resume(text)

        # Render results
        return render_template('index.html', feedback=feedback, filename=file.filename, show_feedback=True)
    
    except Exception as e:
        return jsonify({"error": f"Error processing file: {str(e)}"}), 500

@app.route('/api/upload', methods=['POST'])
def api_upload():
    """API endpoint for resume evaluation (returns JSON)"""
    
    if 'resume' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['resume']
    
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    if not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type. Please upload PDF or DOCX"}), 400

    try:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        text = extract_text(filepath)
        
        if not text.strip():
            return jsonify({"error": "Could not extract text from resume"}), 400

        feedback = evaluate_resume(text)
        
        return jsonify({
            "success": True,
            "filename": file.filename,
            "feedback": feedback
        }), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 AI Resume Evaluator - Starting Server")
    print("=" * 60)
    print("\n✅ Server is running at: http://127.0.0.1:5000/")
    print("✅ Open your browser and go to: http://127.0.0.1:5000/")
    print("\n📝 Supported file formats: PDF, DOCX")
    print("📁 Uploaded files will be saved in: ./uploads/")
    print("\n" + "=" * 60)
    app.run(debug=True, port=5000)
