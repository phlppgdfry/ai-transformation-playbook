# Explain, modify and debug the actual portfolio

Personal competency starts **not assessed**. Passing generated tests does not establish that the candidate can explain or operate the code. For each exercise, record your own explanation, change, observed failure, correction and evidence without assistant-generated claims of experience.

## Interview questions

| Question | Evidence to discuss |
|---|---|
| Why is invoice review not an autonomous payment agent? | Accounting `models.py`, `store.py`, role-protected decision/export routes; error impact and segregation of duties |
| What happens if an ERP times out after accepting a write? | Local outbox transaction versus separate remote transaction; stable remote idempotency key, uncertain-outcome reconciliation |
| Can a model choose a different customer, URL or credential? | Workflow `Plan.check_scope`, `integrations.py` server bindings and endpoint restrictions |
| What can cancellation actually guarantee? | `Store.cancel`, worker lease token invalidation, shared delivery transaction; cannot undo external effects or instantly kill network calls |
| Why keep this engine instead of installing LangGraph or Agent Framework? | Fixed three steps, tested persistence/fencing, migration cost; branching/hosting requirements that would change the decision |
| What does a 100% fixture score prove? | Only the authored checks/fixtures; semantic correctness, representative quality and calibrated safety require different evidence |
| How can access leak through retrieval statistics? | RAG ACL trimming before BM25 corpus/IDF calculation; server identity and Azure response scope validation |
| Why can a document update leave stale chunks? | Changing chunk count; explicit parent deletion and non-atomic cloud replacement; maintenance gating and index-version rollout |
| When does a valid citation still support a wrong answer? | Source ID validity versus entailment/semantic groundedness; need human/model grading and disagreement analysis |
| Why are workflow approval and invoice approval separate? | Ownership and authorization boundaries; actual integration assertion that export remains empty after workflow approval |
| What can the Copilot connector do? | Generated Swagger operation allowlist, separate agent/reviewer/executor credentials; unverified tenant deployment |
| When would Power Automate be a better implementation? | Stable existing connectors, tenant ownership/licensing/DLP, low-code ALM; custom validation and uncertainty requiring code |
| How would you convince a skeptical process owner? | Observe the baseline, test worst-case assumptions, show source review, agree stop rules, train/observe users |
| Is released capacity an actual saving? | Model adoption/coverage/rework assumptions, negative zero-adoption result, ability to redeploy time, measurement plan |

## Skills gaps and practical exercises

Paths are relative to the named repository. Certification topics are a study mapping, not a claim of complete examination coverage. Official guides checked on 29 October 2026: [AI-103](https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-103/) covers Azure AI planning, generative/agentic solutions and information extraction; [PL-900](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-900) covers business value, Dataverse, platform governance, flows and Copilot Studio. Recheck guides before enrollment.

| Gap | Repository / relevant source | Exercise and learning objective | Microsoft topic |
|---|---|---|---|
| Real extraction quality | Accounting `providers.py`, `extraction.py`, `tests/test_providers.py` | With an approved test resource, label 20 synthetic invoices, record per-field accuracy/abstention and compare confidence bins; understand why confidence is not calibrated accuracy | AI-103 information extraction |
| Provider/tool failure diagnosis | Workflow `planners.py`, `engine.py`, `tests/test_workflows.py` | Inject a 429 and malformed tool arguments, inspect persisted retry times and safe error codes, explain permanent versus transient failures | AI-103 generative/agentic implementation |
| Concurrent execution | Workflow `store.py`, `tests/test_cancellation.py` | Pause a worker after claim, cancel, resume and prove fenced writes cannot commit; explain the race if delivery wins first | AI-103 planning/managing solutions; engineering extension |
| Safe system integration | Workflow `integrations.py`, `tests/test_portfolio_tools.py` | Add a second tenant binding without broadening credentials; prove wrong tenant, redirect and excessive response are denied | AI-103 secure AI integration |
| Enterprise identity | All API `api.py` and `security.py` | Replace local keys in a separate exercise with verified Entra token issuer/audience/scopes; test wrong issuer/audience and token expiry before using real data | AI-103 solution security; PL-900 governance |
| Retrieval engineering | RAG `core.py`, `evaluate.py`, `fixtures/retrieval-cases.json` | Add paraphrases that lexical search misses, label relevance, calculate precision/recall/MRR/nDCG and explain null relevance cases | AI-103 knowledge connections/generative solutions |
| Cloud document lifecycle | RAG `index.py`, `azure.py`, `tests/test_index_lifecycle.py` | In a dedicated authorized index, shorten/restrict/delete a document; observe visibility and failure recovery; design index-version rollback | AI-103 managing Azure AI solutions |
| Evaluation design | Evals `engine.py`, `portfolio.py`, `datasets/portfolio-rag-v1.jsonl` | Add a factually wrong answer that passes substring checks, then propose and validate a labeled semantic evaluator; distinguish precision from safety | AI-103 evaluating AI solutions |
| Copilot/Power Platform tenant work | Automation `scripts/package_connector.py`, `connectors/`, `docs/tenant-setup.md` | In an approved tenant, import connector, configure agent-only connection, exercise denied approval and separate review/execution; save real run IDs | PL-900 Copilot Studio, flows, Dataverse and governance |
| ALM and DLP | Automation `docs/connector-deployment.md`, `power-automate/approval-flow.md` | Export a real solution with connection references/environment variables, import into a second environment and test DLP restrictions | PL-900 platform administration/governance |
| Observability and operations | All `security.py`, workflow `store.py`, playbook `integration/scenario.py` | Trace a failed request by generated request ID without logging keys/documents; set latency/concurrency budgets and rehearse recovery | AI-103 solution monitoring/management |
| Business discovery | Playbook `docs/01-discovery-process.md`, `docs/02-delivery-contract.md` | Run a fictional workshop with another person, challenge one assumption and turn it into measurable acceptance criteria | PL-900 business value |
| Business-case reasoning | Playbook `consulting/business_case.py`, `server.py`, `data/scenarios.json` | Change adoption, coverage and rework until payback disappears; explain capacity value versus cash and prepare a measured pilot | PL-900 business value |
| Adoption and benefits realization | Playbook `docs/05-pilot-adoption.md`, `portfolio/EXECUTIVE-BRIEF.md` | Observe someone independently handling an incorrect suggestion, an access denial and an abstention; change training based on errors | PL-900 business process adoption; consulting extension |

Future architect development requires real deployment responsibility, tradeoff reviews, identity/network operations, cost ownership and stakeholder decisions. A certification or this portfolio alone does not establish enterprise architect experience.
