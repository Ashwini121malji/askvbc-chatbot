SELECT
  member_id,
  attribution_type,
  vbc_contract_id
FROM askvbc_attribution.member_attribution
WHERE member_id IN UNNEST(@member_ids);