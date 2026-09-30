import os
from dotenv import load_dotenv
from google import genai

from tools import calculator, current_date

# Load .env
load_dotenv()

# Get API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is missing. "
        "Add it to your local .env file or Render Environment Variables."
    )

MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.1-flash-lite"
)

# Gemini client
client = genai.Client(
    api_key=GEMINI_API_KEY
)


def run_agent(question):
    """
    Main AI Study Agent function.
    """

    question = (question or "").strip()

    if not question:
        return "Please enter a question."

    prompt = f"""
You are an AI Study Agent.

Help students with:
- Python
- Artificial Intelligence
- Machine Learning
- Programming
- Projects
- Exams
- Interview preparation
- Technical concepts
- Career-related technical guidance

Give clear, simple and useful answers.

User Question:
{question}
"""

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )

        if response and response.text:
            return response.text

        return "Sorry, I could not generate a response."

    except Exception as e:
        print("Gemini Error:", e)
        return "Sorry, an error occurred while processing your question."