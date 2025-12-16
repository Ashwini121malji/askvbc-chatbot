"""
Explanation Agent
Builds business-friendly explanations for attribution decisions.
"""

def build_why_explanation(member_id: int, data: dict, rule_info: dict) -> str:
    """
    Creates a clear explanation for why a member was delegated.
    """

    if not data:
        return f"No attribution data found for member {member_id}."

    if not rule_info:
        return (
            f"Member {member_id} was delegated based on system rules, "
            "but detailed rule documentation is not available."
        )

    return (
        f"Member {member_id} is enrolled in {data['member_state']} and was "
        f"initially assigned to a provider located in {data['provider_state']}. "
        f"{rule_info['business_description']} "
        f"As a result, the member was delegated under the rule "
        f"'{rule_info['rule_name']}' and assigned to {data['delegation_code']}."
    )