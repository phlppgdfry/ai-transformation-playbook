# Executive brief: controlled invoice review pilot

**Fictional client:** a Belgian accounting practice. **Decision requested:** approve discovery and a measured shadow pilot; no production or paid cloud deployment is authorized by this document.

## Business problem and proposed process

Invoice review combines document transcription, policy lookup and coordination between employees. The proposed solution prepares evidence and highlights exceptions while an independently authenticated employee retains accounting approval. A separate exporter transfers only approved records to a local mock ERP in the portfolio.

The working demonstration combines accounting validation, access-filtered knowledge retrieval, durable workflow proposals, policy advice, separate approvals and executed evaluation gates. Copilot Studio integration is represented by a constrained connector package and a local task API; Microsoft connector artifact acceptance is verified; an active connection and conversational/flow runtime are unverified.

## Business case with traceable assumptions

Source: `data/scenarios.json`, scenario `base`; formula: `consulting/business_case.py`; reproducible output: `evidence/business-case.json`.

| Assumption | Base scenario |
|---|---:|
| Monthly volume | 1,000 invoices |
| Active handling time | 8 to 3 minutes |
| Adoption / process coverage | 70% / 75% |
| Rework | 8% × 4 minutes |
| Capacity hour value | €45 |
| Monthly operating cost / initial implementation | €350 / €9,000 |

This yields **40.95 hypothetical hours/month**, €1,842.75 gross capacity value/month, €1,492.75 net capacity value/month, €8,913 first-year net capacity value and 6.03 months indicative payback. These are model outputs, not actual savings or cloud quotations. Zero adoption produces zero released hours and negative monthly value. The interactive workspace exposes these sensitivities. No staffing reduction, additional revenue or client result is inferred.

## Delivery and acceptance

Discover → analyze → prioritize → design → implement → validate → adopt → measure. Illustrative timing: two weeks of observation/baseline, two weeks of feasibility/design, four weeks of implementation/shadow evaluation, four weeks of limited adoption measurement. This is a planning assumption, not a project commitment.

The process owner accepts requirements and outcome definitions. IT/security owns enterprise identity and service boundaries; data owners confirm access/retention; privacy/legal assess the real use case; L&D organizes observed task practice. Go/no-go requires representative extraction/retrieval data, independent approval, denied unauthorized actions, recovery exercises, user competence and a support owner. Stop the pilot on a confirmed data-access leak or unauthorized effect.

## Measurement and adoption

Measure active handling time, rework minutes, accepted correct fields, access incidents, cost per task and independently completed user tasks. Compare comparable tasks before/after; report sample size, uncertainty and failures. Train users to compare source and suggestion, recognize abstention and report defects. A training attendance list is not evidence of independent competence.

## Unresolved decisions

Authorize a specific Microsoft test tenant/resource only after budget, licensing, identity, DLP and data approvals. Entra authentication, managed identity deployment, actual OCR/LLM quality, Dataverse/Graph effects and production operations are not yet proven. The current local tests cannot establish legal compliance or guarantee AI safety.

## Executive presentation outline

1. Invoice review problem and pilot decision.
2. Working source-to-review-to-export demonstration, with offline/cloud labels.
3. Six complementary responsibilities and separate approval authority.
4. Base assumptions, downside sensitivity and capacity versus cash.
5. Phased roadmap and accountable owners.
6. Acceptance gates, stop rules, adoption and measurement.
7. Remaining Microsoft validation and next authorized decision.

An editable PPTX was **not generated**: the installed presentation skill requires the `load_workspace_dependencies` artifact runtime, which is not exposed in this session. The outline and brief are provided as source content, not presented as a finished/validated deck.
