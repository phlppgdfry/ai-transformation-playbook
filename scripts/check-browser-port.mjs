// Checks the browser port (site/console/model.js) against fixtures produced by the Python model.
// Run: node scripts/check-browser-port.mjs
import { readFileSync } from 'node:fs';
import { businessCase, prioritize, ScenarioError } from '../site/console/model.js';

const { cases } = JSON.parse(readFileSync(new URL('../tests/parity/business-case-cases.json', import.meta.url), 'utf8'));
let failed = 0;
for (const c of cases) {
  let ok;
  try {
    const r = businessCase(c.input);
    ok = !c.expected.error && Object.entries(c.expected).every(([k, v]) => r[k] === v);
    if (!ok) console.log('  expected', c.expected, '\n  got', r);
  } catch (e) {
    ok = e instanceof ScenarioError && e.message === c.expected.error;
  }
  if (!ok) { failed++; console.log(`FAIL ${c.name}`); }
}
const csv = readFileSync(new URL('../data/use-cases.csv', import.meta.url), 'utf8').trim().split('\n');
const head = csv[0].split(',');
const ranking = prioritize(csv.slice(1).map(l => Object.fromEntries(l.split(',').map((v, i) => [head[i], v]))));
const evidence = JSON.parse(readFileSync(new URL('../evidence/business-case.json', import.meta.url), 'utf8'));
const rankOk = JSON.stringify(ranking) === JSON.stringify(evidence.prioritization);
if (!rankOk) { failed++; console.log('FAIL prioritization differs from evidence/business-case.json'); }
if (failed) { console.error(`${failed} difference(s) between the browser port and the Python model`); process.exit(1); }
console.log(`browser port matches all ${cases.length} business-case fixtures and the prioritization`);
