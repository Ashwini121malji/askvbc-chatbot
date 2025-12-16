"""
Intent Router for AskVBC
Determines the type of user query and routes it accordingly.
"""

import re
from services.attribution_service import handle_why_query


def _detect_intent(user_query: str) -> str:
    query = user_query.lower()

    if query.startswith("why"):
        return "WHY"
    if query.startswith("what"):
        return "WHAT"
    if "compare" in query:
        return "COMPARE"

    return "UNKNOWN"


def _extract_member_id(user_query: str):
    match = re.search(r"\b\d+\b", user_query)
    return int(match.group()) if match else None


def route_query(user_query: str) -> str:
    intent = _detect_intent(user_query)
    member_id = _extract_member_id(user_query)

    if intent == "WHY" and member_id:
        return handle_why_query(member_id)

    return (
        "I can currently help explain why a member was attributed or delegated. "
        "Please ask a 'why' question with a member ID."
    )