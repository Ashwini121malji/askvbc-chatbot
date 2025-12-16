SELECT
  m.member_id,
  m.state AS member_state,
  a.provider_id,
  p.provider_state,
  a.vbc_contract_id,
  a.attribution_type
FROM askvbc_attribution.member_master m
JOIN askvbc_attribution.member_attribution a
  ON m.member_id = a.member_id
JOIN askvbc_attribution.provider_master p
  ON a.provider_id = p.provider_id
WHERE m.member_id = @member_id;