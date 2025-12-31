from src.agents.bq_agent import get_member_attribution

def main():
    test_member_ids = [101, 103, 105, 106, 104]
    
    for member_id in test_member_ids:
        print(f"\n--- Fetching data for member_id = {member_id} ---")
        result = get_member_attribution(member_id, trace_id=str(member_id))
        if not result:
            print("No data found.")
        else:
            for k, v in result.items():
                print(f"{k}: {v}")
            print("----------------------------------------")

if __name__ == "__main__":
    main()
