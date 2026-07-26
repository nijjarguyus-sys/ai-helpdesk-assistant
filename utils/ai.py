from google import genai
from config import GEMINI_API_KEY


client = genai.Client(
    api_key=GEMINI_API_KEY
)


def ask_ai(question: str) -> str:

    try:

        prompt = f"""
You are an experienced IT Help Desk Engineer.

A user has reported this problem:

{question}

Provide:

1. Possible cause
2. Step-by-step troubleshooting
3. When to contact IT support

Keep the answer professional and easy to understand.
"""

        response = client.models.generate_content(
           model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text


    except Exception as error:

        return f"AI Error: {error}"