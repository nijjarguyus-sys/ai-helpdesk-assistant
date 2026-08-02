from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def ask_ai(question: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an experienced IT Help Desk Engineer. "
                        "Provide: 1. Possible cause, "
                        "2. Step-by-step troubleshooting, "
                        "3. When to contact IT support."
                    ),
                },
                {"role": "user", "content": question},
            ],
        )

        return response.choices[0].message.content

    except Exception as error:
        print(f"Groq error: {error}")
        return "⚠️ AI service is temporarily unavailable."