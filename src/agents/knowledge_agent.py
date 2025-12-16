"""
Knowledge Agent
Provides business rule explanations based on documented logic.
"""

DELEGATION_RULES = {
    "DEL-014": {
        "rule_name": "Out-of-State Provider Delegation",
        "business_description": (
            "VBC contracts are state-specific. When a member's assigned provider "
            "operates outside the member's enrolled state, the member cannot be "
            "directly attributed under the VBC program."
        )
    },
    "DEL-021": {
        "rule_name": "No Active VBC Contract",
        "business_description": (
            "Applied when there is no active VBC contract available for the member's "
            "state during the attribution period."
        )
    }
}


def get_delegation_rule(rule_id: str):
    """
    Returns business explanation for a delegation rule.
    """
    if not rule_id:
        return None

    return DELEGATION_RULES.get(rule_id)