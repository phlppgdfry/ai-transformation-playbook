# Feature evidence matrix — 29 October 2026

Status vocabulary: **VERIFIED** means the stated local behavior was executed; **IMPLEMENTED BUT NOT VERIFIED** means code/artifacts exist without live acceptance; **MOCKED** means a deliberately substituted external effect; **DOCUMENTED ONLY** is a design/runbook; **PLANNED** is future work. Local tests do not prove production safety, real customer use or legal compliance.

Verification commands and results are in [verification-2026-10-29.json](verification-2026-10-29.json). Original 28 October evidence is retained as historical evidence. The pinned dependency audit reports no known advisories at scan time, not absence of all vulnerabilities. Request logs omit bodies, query strings and credentials.

| Feature | Status | Evidence / limitation |
|---|---|---|
| Capacity model and risk-gated prioritization | VERIFIED | tests/test_business_case.py; tests/test_workspace.py |
| Interactive assumptions, sensitivity, download and roadmap | VERIFIED | portfolio/browser-qa.json; screenshots/desktop.png |
| Five-API integration tied to the business case | VERIFIED | portfolio/integration-result.json; 27 actual HTTP checks |
| Workshop/risk/adoption/UAT methodology | DOCUMENTED ONLY | fictional consulting templates, no real workshop claim |
| Actual client benefits, user adoption, candidate competence | PLANNED | not observed or assessed |
| Executive brief and presentation content | DOCUMENTED ONLY | portfolio/EXECUTIVE-BRIEF.md; no validated PPTX export available |
