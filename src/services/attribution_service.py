"""
Attribution Service
Handles business workflows related to attribution and delegation.
"""

from agents.bq_agent import get_member_attribution
from agents.knowledge_agent import get_delegation_rule
from agents.explanation_agent import build_why_explanation


def handle_why_query(member_id: int) -> str:
    """
    Handles 'why' questions for a member.
    """

    attribution_data = get_member_attribution(member_id)

    if not attribution_data:
        return f"No attribution data found for member {member_id}."

    if attribution_data["attribution_type"] != "DELEGATED":
        return (
            f"Member {member_id} was directly attributed to provider "
            f"{attribution_data['provider_id']} and was not delegated."
        )

    rule_info = get_delegation_rule(attribution_data["rule_applied"])

    return build_why_explanation(member_id, attribution_data, rule_info)