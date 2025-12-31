from src.utils.logger import get_logger


def generate_sql(question: str, trace_id: str) -> dict:
    logger = get_logger("SQL_AGENT", trace_id)

    q = question.lower()

    if "del-014" in q:
        sql = """
        SELECT
          member_id,
          member_state,
          provider_id,
          attribution_type,
          delegation_code,
          rule_applied
        FROM member_attribution_view
        WHERE rule_applied = 'DEL-014'
        """
        intent = "RULE_IMPACT"

    elif "missing pcp" in q:
        sql = """
        SELECT
          member_id,
          member_state
        FROM member_attribution_view
        WHERE delegation_code = 'PCP_MISSING'
        """
        intent = "DATA_QUALITY"

    elif "delegated" in q and "state" in q:
        sql = """
        SELECT
          member_state,
          COUNT(*) AS delegated_count
        FROM member_attribution_view
        WHERE attribution_type = 'DELEGATED'
        GROUP BY member_state
        """
        intent = "AGGREGATION"

    else:
        return {
            "sql": None,
            "intent": "UNSUPPORTED"
        }

    logger.info(f"SQL generated for intent {intent}")

    return {
        "intent": intent,
        "sql": sql.strip()
    }
