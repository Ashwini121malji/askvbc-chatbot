from src.agents.bq_agent import get_member_attribution

member_id = 101
result = get_member_attribution(member_id)

if result:
    print("BigQuery returned:")
    for k, v in result.items():
        print(f"{k}: {v}")
else:
    print(f"No data found for member {member_id}")
