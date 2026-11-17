// Browser port of consulting/business_case.py (business_case, prioritize) and the input checks of
// consulting/server.py (calculate). tests/parity/business-case-cases.json is checked against the Python
// model (tests/test_browser_parity.py) and against this file (scripts/check-browser-port.mjs) in CI.
const FIELDS = ['monthly_volume', 'minutes_before', 'minutes_after', 'hourly_cost', 'adoption', 'automation_coverage', 'monthly_run_cost', 'implementation_cost', 'rework_rate', 'rework_minutes'];
const round2 = x => Number(x.toFixed(2)) + 0; // + 0 turns -0 into 0, as Python's json would print 0.0

export class ScenarioError extends Error {}

export function calculate(values) {
  if (!values || typeof values !== 'object' || Array.isArray(values)) throw new ScenarioError('Supply the ten documented scenario assumptions');
  const keys = Object.keys(values).sort().join(','), want = [...FIELDS].sort().join(',');
  if (keys !== want) throw new ScenarioError('Supply the ten documented scenario assumptions');
  if (Object.values(values).some(v => typeof v !== 'number' || v > 1_000_000_000)) throw new ScenarioError('Assumptions must be bounded numeric values');
  return businessCase(values);
}

export function businessCase(v) {
  if (Object.values(v).some(x => typeof x !== 'number' || !Number.isFinite(x) || x < 0)) throw new ScenarioError('All assumptions must be finite non-negative numbers');
  if (['adoption', 'automation_coverage', 'rework_rate'].some(k => v[k] > 1)) throw new ScenarioError('Rates must be between zero and one');
  const saved = v.monthly_volume * v.adoption * v.automation_coverage * (v.minutes_before - v.minutes_after - v.rework_rate * v.rework_minutes);
  const freed = saved / 60, capacity = freed * v.hourly_cost, net = capacity - v.monthly_run_cost;
  return {
    assumptions: { ...v },
    label: 'Hypothetical capacity scenario; not realized cash savings',
    freed_hours_monthly: round2(freed),
    capacity_value_monthly_eur: round2(capacity),
    net_capacity_value_monthly_eur: round2(net),
    payback_months: net > 0 ? round2(v.implementation_cost / net) : null,
    first_year_net_capacity_value_eur: round2(net * 12 - v.implementation_cost),
  };
}

export function prioritize(cases) {
  return cases.map(c => {
    const s = Object.fromEntries(['impact', 'feasibility', 'data_readiness', 'adoption_readiness', 'risk'].map(k => [k, Number(c[k])]));
    if (Object.values(s).some(x => !Number.isFinite(x) || x < 1 || x > 5)) throw new ScenarioError('Use-case scores must be finite values in 1..5');
    const score = 0.35 * s.impact + 0.25 * s.feasibility + 0.2 * s.data_readiness + 0.2 * s.adoption_readiness;
    return { id: c.id, name: c.name, score: round2(score), gate: s.risk >= 4 ? 'specialist_review' : 'discovery', risk: s.risk };
  }).sort((a, b) => b.score - a.score || (a.id < b.id ? -1 : a.id > b.id ? 1 : 0));
}
