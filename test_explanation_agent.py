from src.agents.explanation_agent import explain_attribution

# Sample data to test explanation agent
sample_data = [
    {
        "member_id": 101,
        "member_state": "TX",
        "provider_id": "P1002",
        "provider_state": "VT",
        "vbc_contract_id": "C_VT_01",
        "attribution_type": "DELEGATED",
        "delegation_code": "OUT_STATE",
        "rule_applied": "DEL-014"
    },
    {
        "member_id": 106,
        "member_state": "TX",
        "provider_id": None,
        "provider_state": None,
        "vbc_contract_id": "C_TX_02",
        "attribution_type": "DELEGATED",
        "delegation_code": "PCP_MISSING",
        "rule_applied": "DEL-021"
    }
]

def main():
    for data in sample_data:
        print(f"\n--- Generating explanation for member_id = {data['member_id']} ---")
        explanation = explain_attribution(data, trace_id=str(data['member_id']))
        print("Answer:\n", explanation["answer"])
        print("Rules checked:", explanation["rules_checked"])

if __name__ == "__main__":
    main()
