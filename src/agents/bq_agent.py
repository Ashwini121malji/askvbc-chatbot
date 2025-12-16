"""
BigQuery Agent
Responsible only for retrieving attribution data.
"""

def get_member_attribution(member_id: int):
    """
    Mocked BigQuery response.
    Replace with real BigQuery SQL execution later.
    """

    # This structure mirrors joined BigQuery tables
    MOCK_DATA = {
        101: {
            "member_id": 101,
            "member_state": "TX",
            "provider_id": "P1002",
            "provider_state": "VT",
            "vbc_contract_id": "VBC_VT_001",
            "attribution_type": "DELEGATED",
            "delegation_code": "OAKST_VT",
            "rule_applied": "DEL-014"
        },
        102: {
            "member_id": 102,
            "member_state": "TX",
            "provider_id": "P1001",
            "provider_state": "TX",
            "vbc_contract_id": "VBC_TX_001",
            "attribution_type": "DIRECT",
            "delegation_code": None,
            "rule_applied": None
        }
    }

    return MOCK_DATA.get(member_id)