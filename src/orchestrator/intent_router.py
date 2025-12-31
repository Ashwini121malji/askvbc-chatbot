from src.agents.bq_agent import get_member_attribution
from src.agents.explanation_agent import explain_attribution
from src.utils.logger import get_logger


def handle_question(question: str, trace_id: str) -> dict:
    logger = get_logger("INTENT_ROUTER", trace_id)
    q = question.lower()

    if "member" in q and "attribute" in q:
        logger.info("Detected ATTRIBUTION intent")

        member_id = None
        for word in q.split():
            if word.isdigit():
                member_id = int(word)
                break

        if not member_id:
            return {
                "answer": "Please provide a valid member ID.",
                "rules_checked": []
            }

        data = get_member_attribution(member_id, trace_id)
        return explain_attribution(data, trace_id)

    logger.info("Unknown intent")
    return {
        "answer": "I currently support member attribution questions.",
        "rules_checked": []
    }
