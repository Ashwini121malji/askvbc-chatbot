"""
AskVBC - Application Entry Point
"""

from orchestrator.intent_router import route_query


def askvbc(user_query: str) -> str:
    """
    Main function exposed to UI or API.
    """
    return route_query(user_query)


if __name__ == "__main__":
    # Local testing (optional)
    sample_question = "Why was member 101 delegated to OAKST_VT?"
    print(askvbc(sample_question))