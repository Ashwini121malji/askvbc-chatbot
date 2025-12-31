"""
AskVBC Chatbot - Entry Point
"""

from src.orchestrator.intent_router import detect_intent
from src.services.attribution_service import (
    get_attribution_explanation,
    get_attribution_details
)


def run_chatbot(user_input: str):
    intent_payload = detect_intent(user_input)

    intent = intent_payload["intent"]
    member_id = intent_payload["member_id"]

    if not member_id:
        return "Please specify a member ID."

    if intent == "ATTRIBUTION_EXPLANATION":
        return get_attribution_explanation(member_id)

    elif intent == "ATTRIBUTION_DETAILS":
        return get_attribution_details(member_id)

    elif intent == "VBC_ELIGIBILITY":
        details = get_attribution_details(member_id)
        if not details:
            return "Member is not part of a VBC contract."
        return "Member is part of a VBC contract."

    else:
        return "Sorry, I couldn't understand your question."


if __name__ == "__main__":
    while True:
        question = input("\nAskVBC > ")
        if question.lower() in ["exit", "quit"]:
            break
        print(run_chatbot(question))
