import os
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is missing."
    )

client = genai.Client(
    api_key=GEMINI_API_KEY
)

# Primary + fallback models
MODELS = [
    "gemini-3.1-flash-lite",
    "gemini-3.5-flash-lite",
    "gemini-2.5-flash-lite"
]


def generate_answer(question):

    prompt = f"""
You are StudyAgent AI.

You help students with:

- Python
- Artificial Intelligence
- Machine Learning
- Programming
- Projects
- Exams
- Interview preparation
- Technical concepts
- Career and internship preparation

Give simple, clear and useful answers.

User Question:
{question}
"""

    for model in MODELS:

        for attempt in range(2):

            try:

                print(
                    f"Trying model: {model} "
                    f"(attempt {attempt + 1})"
                )

                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )

                if response and response.text:
                    print(f"Success: {model}")
                    return response.text

            except Exception as e:

                error_text = str(e)

                print(
                    f"Gemini Error [{model}]: "
                    f"{error_text}"
                )

                # Retry only temporary server errors
                if "503" in error_text or "UNAVAILABLE" in error_text:

                    if attempt == 0:
                        print("Temporary overload. Retrying...")
                        time.sleep(3)
                        continue

                    print(
                        f"{model} unavailable. "
                        "Trying next model..."
                    )
                    break

                # Authentication / other errors
                raise

    return (
        "Gemini AI is temporarily busy. "
        "Please try again in a few seconds."
    )


def run_agent(question):

    question = (question or "").strip()

    if not question:
        return "Please enter a question."

    try:
        return generate_answer(question)

    except Exception as e:

        print("Agent Error:", e)

        return (
            "Sorry, an error occurred while "
            "processing your question."
        )