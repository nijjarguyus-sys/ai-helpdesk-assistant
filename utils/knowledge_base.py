import json
from pathlib import Path

FAQ_FILE = Path(__file__).parent.parent / "data" / "faq.json"


def get_answer(question):
    # Handle empty input safely
    if not question:
        return None

    try:
        with open(FAQ_FILE, "r", encoding="utf-8") as file:
            faq = json.load(file)

        question = question.lower()

        for keyword, answer in faq.items():
            if keyword.lower() in question:
                return answer

        return None

    except FileNotFoundError:
        return "❌ FAQ database not found."

    except json.JSONDecodeError:
        return "❌ FAQ database contains invalid JSON."