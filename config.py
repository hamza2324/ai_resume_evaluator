# Configuration file for AI Resume Evaluator
# You can modify these settings as needed

# Flask Configuration
DEBUG = True
PORT = 5000
HOST = '127.0.0.1'

# File Upload Settings
UPLOAD_FOLDER = 'uploads'
MAX_FILE_SIZE_MB = 10
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

# Groq API Configuration
# Model: mixtral-8x7b-32768 (as per user's original setup)
# If this model is decommissioned, Groq API will return error
# Check: https://console.groq.com/docs/models
GROQ_MODEL = "openai/gpt-oss-safeguard-20b"
GROQ_MAX_TOKENS = 2048

# Resume Analysis Settings
MIN_RESUME_LENGTH = 100  # Minimum characters required
ANALYSIS_TIMEOUT = 30  # Timeout in seconds

# UI Settings
THEME = "modern"  # Can be customized
