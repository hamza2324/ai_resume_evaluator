AI Resume Evaluator

AI Resume Evaluator is a web-based tool that analyzes resumes (PDF or DOCX) and provides actionable feedback on skills, structure, and improvement areas using AI. This project was developed as Task #2 of the GenAI Internship with Internie.pk.

Features

Upload resumes in PDF or DOCX format.

Extract text from resumes using Python libraries (pdfplumber & python-docx).

Analyze resumes with AI using Groq API for content understanding.

Generate structured feedback on strengths, weaknesses, and improvement suggestions.

Simple web interface built with Flask (or Streamlit version for deployment).

Tech Stack
Technology	Purpose
Python	Core programming language
Flask	Web server and file upload interface
Streamlit (optional)	Alternative interactive web interface
Groq API	AI-powered LLM for analyzing resume content
LangChain	Prompt management and structured AI responses
pdfplumber	Extract text from PDF resumes
python-docx	Extract text from DOCX resumes
How It Works

User uploads a resume.

Text is extracted from the PDF or DOCX file.

Text is sent to Groq API through LangChain for AI evaluation.

AI returns structured feedback highlighting strengths, weaknesses, and suggestions.

Feedback is displayed on the web interface.

Contributing

Contributions are welcome! Feel free to:

Add new features (e.g., scoring, keyword matching, template recommendations).

Improve AI feedback formatting.

Integrate multi-language support.

Acknowledgements

Internie.pk – For providing the GenAI Internship opportunity.

Groq AI & LangChain – For enabling AI-powered resume analysis.

License

This project is licensed under the MIT License.
