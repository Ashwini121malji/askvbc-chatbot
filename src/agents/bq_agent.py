from src.utils.logger import get_logger


def get_member_attribution(member_id: int, trace_id: str) -> dict:
    logger = get_logger("BQ_AGENT", trace_id)

    # 🔹 Mocked attribution data (replace with BigQuery logic later)
    attribution_type = "DIRECT"
    provider_id = "P1001"
    provider_state = "TX"
    contract_id = "C_TX_01"
    rule_applied = "DEL-014"
    delegation_code = "OUT_STATE"
    member_state = "TX"

    trace = []

    # Step 1: Input
    trace.append({
        "step": "INPUT",
        "details": {
            "member_id": member_id,
            "member_state": member_state
        }
    })

    # Step 2: Attribution model
    trace.append({
        "step": "ATTRIBUTION_MODEL",
        "details": {
            "type": attribution_type,
            "provider_id": provider_id,
            "provider_state": provider_state,
            "vbc_contract_id": contract_id
        }
    })

    # Step 3: Delegation rule
    trace.append({
        "step": "DELEGATION_RULE",
        "details": {
            "rule_applied": rule_applied,
            "delegation_code": delegation_code
        }
    })

    logger.info(f"Fetched attribution data for member_id={member_id}")

    # ✅ MUST return data
    return {
        "member_id": member_id,
        "member_state": member_state,
        "provider_state": provider_state,
        "attribution_type": attribution_type,
        "provider_id": provider_id,
        "vbc_contract_id": contract_id,
        "rule_applied": rule_applied,
        "delegation_code": delegation_code,
        "trace": trace
    }
