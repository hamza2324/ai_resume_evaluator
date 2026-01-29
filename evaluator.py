import json
import os
from groq import Groq
from langchain.prompts import PromptTemplate

# Initialize Groq client
os.environ['GROQ_API_KEY'] = "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"
client = Groq()

def evaluate_resume(text):
    """
    Send resume text to Groq LLM for analysis
    """
    prompt_template = """You are an expert AI resume evaluator. Analyze the following resume and provide detailed feedback in JSON format.

Return ONLY a valid JSON object with these exact keys: strengths (list of strengths), weaknesses (list of areas to improve), improvement_suggestions (specific actionable suggestions), overall_score (0-10), summary (Brief professional summary).

Resume Content:
{text}

Ensure the response is valid JSON only, with no additional text."""
    
    prompt = PromptTemplate(
        input_variables=["text"],
        template=prompt_template
    )
    formatted_prompt = prompt.format(text=text)

    try:
        # Call Groq API with the correct model
        message = client.chat.completions.create(
            model="openai/gpt-oss-safeguard-20b",
            max_tokens=2048,
            messages=[
                {"role": "user", "content": formatted_prompt}
            ]
        )
        
        response_text = message.choices[0].message.content
        
        # Extract JSON from response
        try:
            # Try to parse the entire response as JSON
            feedback = json.loads(response_text)
        except json.JSONDecodeError:
            # If that fails, try to extract JSON from the response
            import re
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            if json_match:
                feedback = json.loads(json_match.group())
            else:
                feedback = {
                    "strengths": ["Unable to parse response"],
                    "weaknesses": [],
                    "improvement_suggestions": [],
                    "overall_score": 0,
                    "summary": response_text
                }
        
        return feedback
    except Exception as e:
        return {
            "strengths": [],
            "weaknesses": [str(e)],
            "improvement_suggestions": ["Please check your API key and try again"],
            "overall_score": 0,
            "summary": f"Error: {str(e)}"
        }
