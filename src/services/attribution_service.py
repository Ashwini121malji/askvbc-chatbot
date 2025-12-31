"""
Attribution Service
Coordinates between BQ Agent and Explanation Agent.
"""

from src.agents.bq_agent import get_member_attribution
from src.agents.explanation_agent import explain_attribution


def get_attribution_explanation(member_id: int) -> str:
    data = get_member_attribution(member_id)

    if not data:
        return f"No attribution data found for member {member_id}."

    # BQ agent returns dict or list — normalize
    if isinstance(data, dict):
        data = [data]

    return explain_attribution(data)


def get_attribution_details(member_id: int):
    return get_member_attribution(member_id)
