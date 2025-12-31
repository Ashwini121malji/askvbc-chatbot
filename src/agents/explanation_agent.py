from src.utils.logger import get_logger


def explain_attribution(data: dict, trace_id: str) -> dict:
    logger = get_logger("EXPLANATION_AGENT", trace_id)

    if not data:
        return {
            "answer": "No attribution found for this member.",
            "rules_checked": [],
            "trace": []
        }

    trace = []

    trace.append({
        "step": "INPUT",
        "details": {
            "member_id": data["member_id"],
            "member_state": data["member_state"]
        }
    })

    trace.append({
        "step": "ATTRIBUTION_MODEL",
        "details": {
            "type": data["attribution_type"],
            "provider_id": data["provider_id"],
            "provider_state": data["provider_state"],
            "vbc_contract_id": data["vbc_contract_id"]
        }
    })

    trace.append({
        "step": "DELEGATION_RULE",
        "details": {
            "rule_applied": data["rule_applied"],
            "delegation_code": data["delegation_code"]
        }
    })

    explanation = (
        f"Member {data['member_id']} was attributed using the "
        f"{data['attribution_type']} attribution model. "
        f"The delegation rule {data['rule_applied']} was applied "
        f"due to condition: {data['delegation_code']}."
    )

    logger.info(f"Attribution explained using rule {data['rule_applied']}")

    return {
        "answer": explanation,
        "rules_checked": [data["rule_applied"]],
        "trace": trace
    }
