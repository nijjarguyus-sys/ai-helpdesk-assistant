import json
from pathlib import Path


FAQ_FILE = Path(__file__).parent.parent / "data" / "faq.json"


def normalize_text(text):
    """Normalize text for reliable matching."""

    if not text:
        return ""

    return " ".join(text.lower().strip().split())


def search_knowledge_base(question):
    """
    Search the knowledge base and return the best matching article.

    Returns:
        dict containing article information and match score,
        or None when no meaningful match is found.
    """

    if not question:
        return None

    try:
        with open(FAQ_FILE, "r", encoding="utf-8") as file:
            faq = json.load(file)

    except FileNotFoundError:
        return {
            "error": "❌ FAQ database not found."
        }

    except json.JSONDecodeError:
        return {
            "error": "❌ FAQ database contains invalid JSON."
        }

    question = normalize_text(question)

    best_match = None
    best_score = 0

    for item in faq:

        score = 0

        issue = normalize_text(item.get("issue", ""))

        keywords = [
            normalize_text(keyword)
            for keyword in item.get("keywords", [])
        ]

        symptoms = [
            normalize_text(symptom)
            for symptom in item.get("symptoms", [])
        ]

        # Exact issue phrase
        if issue and issue in question:
            score += 10

        # Symptom matches
        for symptom in symptoms:
            if symptom and symptom in question:
                score += 5

        # Keyword matches
        for keyword in keywords:
            if keyword and keyword in question:
                score += 2

        # Keep the strongest match
        if score > best_score:
            best_score = score
            best_match = item

    # Require a meaningful match
    if best_match and best_score >= 2:

        return {
            "id": best_match.get("id"),
            "category": best_match.get("category"),
            "issue": best_match.get("issue"),
            "answer": best_match.get("answer"),
            "escalation": best_match.get("escalation"),
            "score": best_score,
            "source": "Knowledge Base"
        }

    return None


def get_answer(question):
    """
    Backward-compatible function.

    Returns only the answer text so existing app code
    can continue working.
    """

    result = search_knowledge_base(question)

    if not result:
        return None

    if "error" in result:
        return result["error"]

    return result.get("answer")