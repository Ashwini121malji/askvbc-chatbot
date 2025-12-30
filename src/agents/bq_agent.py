"""
BigQuery Agent
Responsible for retrieving attribution and delegation data from BigQuery.
"""

from google.cloud import bigquery
from google.api_core.exceptions import NotFound
from configparser import ConfigParser
import yaml

# Load configuration from YAML
import os
import yaml

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '../../config/app_config.yaml')
with open(CONFIG_PATH, 'r') as f:
    config = yaml.safe_load(f)

PROJECT_ID = config['gcp']['project_id']
DATASET = config['bigquery']['dataset']

# Initialize client
client = bigquery.Client(project=PROJECT_ID)


def get_member_attribution(member_id: int) -> dict:
    """
    Fetches joined member attribution + delegation info from BigQuery.
    Returns a dictionary like:
    {
        "member_id": 101,
        "member_state": "TX",
        "provider_id": "P1002",
        "provider_state": "VT",
        "vbc_contract_id": "VBC_VT_001",
        "attribution_type": "DELEGATED",
        "delegation_code": "OAKST_VT",
        "rule_applied": "DEL-014"
    }
    """

    query = f"""
    SELECT
      m.member_id,
      m.state AS member_state,
      a.provider_id,
      p.provider_state,
      a.vbc_contract_id,
      a.attribution_type,
      d.delegation_code,
      d.rule_applied
    FROM `{PROJECT_ID}.{DATASET}.member_master` m
    LEFT JOIN `{PROJECT_ID}.{DATASET}.member_attribution` a
      ON m.member_id = a.member_id
    LEFT JOIN `{PROJECT_ID}.{DATASET}.provider_master` p
      ON a.provider_id = p.provider_id
    LEFT JOIN `{PROJECT_ID}.{DATASET}.delegation_events` d
      ON m.member_id = d.member_id
    WHERE m.member_id = @member_id
    """

    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("member_id", "INT64", member_id)
        ]
    )

    try:
        query_job = client.query(query, job_config=job_config)
        result = query_job.result()
        row = list(result)
        if not row:
            return None
        # Convert row to dictionary
        row_dict = dict(row[0])
        return row_dict

    except NotFound:
        print(f"Table not found in dataset {DATASET}")
        return None
    except Exception as e:
        print(f"Error querying BigQuery: {e}")
        return None

if __name__ == "__main__":
    print("This module is not meant to be run directly.")