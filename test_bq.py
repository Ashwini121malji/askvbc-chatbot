from src.agents.bq_agent import get_member_attribution

def main():
    member_id = 101
    print(f"Testing BigQuery fetch for member_id = {member_id}")

    result = get_member_attribution(member_id)

    if result:
        print("BigQuery returned:")
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print("No data returned from BigQuery")

if __name__ == "__main__":
    main()
