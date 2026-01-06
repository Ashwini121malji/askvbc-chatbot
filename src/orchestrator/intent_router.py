from src.agents.bq_agent import get_member_attribution
from src.agents.explanation_agent import explain_attribution
from src.utils.logger import get_logger
import uuid


def handle_question(question: str) -> dict:
    trace_id = str(uuid.uuid4())
    logger = get_logger("INTENT_ROUTER", trace_id)

    q = question.lower()
    logger.info(f"Received question: {q}")

    # ✅ ATTRIBUTION INTENT (ROBUST)
    if "member" in q and any(word in q for word in ["attribute", "attribution", "attributed"]):
        logger.info("Detected ATTRIBUTION intent")

        member_id = None
        for token in q.split():
            if token.isdigit():
                member_id = int(token)
                break

        if not member_id:
            return {
                "answer": "Please provide a valid member ID.",
                "rules_checked": []
            }

        data = get_member_attribution(member_id, trace_id)
        return explain_attribution(data, trace_id)

    # ❌ FALLBACK
    logger.info("Unknown intent triggered")
    return {
        "answer": "I can help with member attribution questions.",
        "rules_checked": []
    }
