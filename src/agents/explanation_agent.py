from src.utils.confidence import calculate_confidence, classify_confidence


def build_why_not(data: dict) -> list[str]:
    reasons = []

    if data.get("attribution_type") == "DIRECT":
        reasons.append(
            "Member was not attributed via INDIRECT because a DIRECT provider match existed."
        )

    if data.get("member_state") == data.get("provider_state"):
        reasons.append(
            "Geographic fallback was skipped as member and provider states matched."
        )

    if not data.get("manual_override"):
        reasons.append(
            "No manual override rule was triggered."
        )

    return reasons


from src.utils.confidence import calculate_confidence, classify_confidence


def explain_attribution(data: dict, trace_id: str) -> dict:
    confidence, confidence_explanation, rule_confidence = calculate_confidence(data)
    confidence_level = classify_confidence(confidence)

    answer = (
        f"Member {data['member_id']} was attributed using the "
        f"{data['attribution_type']} attribution model. "
        f"The delegation rule {data['rule_applied']} was applied due to "
        f"condition: {data['delegation_code']}."
    )

    return {
        "answer": answer,
        "rules_checked": [data.get("rule_applied")],
        "confidence": confidence,
        "confidence_level": confidence_level,
        "confidence_explanation": confidence_explanation,
        "rule_confidence": rule_confidence,
        "trace": data.get("trace", [])
    }

