from src.agents.bq_agent import get_member_attribution


def test_member(member_id):
    print(f"\n--- Fetching data for member_id = {member_id} ---")

    rows = get_member_attribution(member_id)

    if not rows:
        print("No data returned from BigQuery")
        return

    # Normalize to list (handles 1 or many rows)
    if isinstance(rows, dict):
        rows = [rows]

    for row in rows:
        for key, value in row.items():
            print(f"{key}: {value}")
        print("-" * 40)


if __name__ == "__main__":
    for mid in [101, 103, 105, 106, 104]:
        test_member(mid)
