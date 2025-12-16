SELECT
  d.member_id,
  d.delegation_code,
  d.rule_applied,
  d.delegation_reason,
  d.effective_date
FROM askvbc_attribution.delegation_events d
WHERE d.member_id = @member_id;