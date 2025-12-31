"""
BigQuery Agent
Responsible for retrieving attribution and delegation data from BigQuery.
"""

from google.cloud import bigquery
from google.api_core.exceptions import NotFound
import os
import yaml
from src.utils.logger import get_logger

# Load config
CONFIG_PATH = os.path.join(os.path.dirname(__file__), '../../config/app_config.yaml')
with open(CONFIG_PATH, 'r') as f:
    config = yaml.safe_load(f)

PROJECT_ID = config['gcp']['project_id']
DATASET = config['bigquery']['dataset']

# Initialize BigQuery client
client = bigquery.Client(project=PROJECT_ID)


def get_member_attribution(member_id: int, trace_id: str) -> dict:
    """
    Fetches joined member attribution + delegation info from BigQuery.
    """
    logger = get_logger("BQ_AGENT", trace_id)

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
        rows = list(result)
        if not rows:
            logger.info(f"No data returned for member_id={member_id}")
            return None
        row_dict = dict(rows[0])
        logger.info(f"Fetched attribution data for member_id={member_id}")
        return row_dict
    except NotFound:
        logger.error(f"Table not found in dataset {DATASET}")
        return None
    except Exception as e:
        logger.error(f"Error querying BigQuery: {e}")
        return None

def run_dynamic_query(sql: str, trace_id: str) -> list:
    logger = get_logger("BQ_AGENT", trace_id)

    query_job = client.query(sql)
    rows = query_job.result()

    results = [dict(row) for row in rows]

    logger.info(f"Returned {len(results)} rows")
    return results
