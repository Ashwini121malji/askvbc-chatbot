from src.services.attribution_service import handle_why_query

def test_delegated_member():
    response = handle_why_query(101)
    assert "delegated" in response.lower()