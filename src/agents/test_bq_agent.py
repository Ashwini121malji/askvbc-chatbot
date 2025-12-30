from src.agents.bq_agent import get_member_attribution

# Test member_id with different scenarios
test_member_ids = [101, 103, 105, 106, 104]

for member_id in test_member_ids:
    print(f"\n--- Fetching data for member_id = {member_id} ---")
    result = get_member_attribution(member_id)
    if result:
        for row in result:
            print(row)
    else:
        print("No data returned from BigQuery")
