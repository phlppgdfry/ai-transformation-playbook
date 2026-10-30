# Learn to explain, modify and diagnose the actual implementation

Personal competence is **NOT ASSESSED**. Complete the exercises yourself, record what you changed and explain a failure without code generation. Repository tests demonstrate program behavior, not personal expertise.

The topic mappings below use the official [AI-103 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103) for Azure AI planning, secure generative/agentic systems and extraction, and the [PL-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-900) for Power Platform business value, governance, Dataverse and automation. These are selected study topics, not complete exam coverage or certification claims. Guides were checked on 30 October 2026.

## Accounting Copilot

Five essentials:

| Concept | Important source | Decision to understand |
|---|---|---|
| Exact financial validation | `src/accounting_copilot/models.py` | Decimal values and balanced totals, rather than binary floats |
| Identity and tenancy | `api.py` | Server credentials determine permissions; request fields do not |
| Independent approval | `store.py::decide` | Submitter cannot approve; version protects a stale decision |
| Transactional outbox | `store.py::export_mock` | Local effect and acknowledgement share a transaction |
| Extraction as a proposal | `providers.py`, `extraction.py` | Confidence is uncalibrated and never grants approval |

Debug three failures:

1. Submit the same idempotency key with different content. Diagnose the 409 and explain why changing the key is not a correction workflow. Objective: distinguish request identity from business duplicate identity.
2. Review using an obsolete `expected_version` or the submitter identity. Trace the conflict to its actual rule and retry only after an independent review. Objective: understand concurrency and separation of duties.
3. Inject a provider timeout with MockTransport, then a successful low-confidence response. Prove neither approves or silently substitutes fixture data. Objective: distinguish transport, extraction and business authority.

Interview: **Why not claim remote exactly-once export?** The local mock shares the database; a real ERP is a separate transaction domain. Use stable remote idempotency keys, reconciliation and uncertain-outcome handling. **Does 95% confidence mean 95% field accuracy?** No; calibrate against labeled examples before interpreting it that way.

Common failures: unknown supplier, unbalanced amounts, blocked invoice, stale version, provider refusal/timeout. Learn next: real extraction calibration, Entra identity and remote ERP recovery. Microsoft topics: AI-103 information extraction and secure AI solution management.

## Agentic Workflow Platform

| Concept | Important source | Decision to understand |
|---|---|---|
| Native tool calls versus fixtures | `planners.py`, `ollama.py` | A real model call is opt-in; invalid output has no fixture fallback |
| Tool schema and scope | `models.py::Plan.check_scope` | Three allowed steps and unchanged customer identity |
| Read-only system integration | `integrations.py` | Server owns URL, credential and invoice binding |
| Checkpoint and fencing | `store.py`, `engine.py` | A worker must still own its lease when committing |
| Human authority and cancellation | `store.py::decide`, `cancel` | Approval and cancellation are transactional state changes |

Debug three failures:

1. Change a synthetic planner to return another customer or a forbidden tool; inspect failure state without a CRM case. Objective: locate structural checks outside the model.
2. Block a worker after claim, cancel it, then let it return. Prove its checkpoint is fenced; explain the different outcome if delivery committed first. Objective: reason about races rather than timing sleeps.
3. Make the policy API return 503, then 403. Explain retry/backoff versus permanent failure and prove no local fixture replaces the missing evidence. Objective: safe dependency recovery.

Interview: **Is this adaptive multi-agent reasoning?** No: one bounded planning call followed by deterministic checkpoints. **Why no orchestration framework?** The fixed process already has tested leases, receipts and approval; choose a framework when branching/hosting requirements justify migration.

Common failures: mode mismatch after restart, active lease, schema violation, absent policy source, refused model call. Learn next: representative model evaluation, deployment concurrency, adaptive loops only with a real requirement. Microsoft topics: AI-103 tools, guarded agent workflows, monitoring and quotas.

## Knowledge Assistant

| Concept | Important source | Decision to understand |
|---|---|---|
| Access before ranking | `rag/core.py::retrieve` | Inaccessible documents do not influence the lexical corpus statistics |
| Chunk identity/lifecycle | `core.py::upsert`, `delete` | Replace old chunks and preserve tenant scope |
| Local versus Azure mode | `azure.py` | Extractive lexical search differs from embeddings/hybrid generation |
| Source validity versus truth | `azure.py::answer` | Allowed citation IDs do not prove every assertion is entailed |
| Retrieval evaluation | `evaluate.py`, `data/` | Document-level metrics deduplicate chunks and define empty relevance cases |

Debug three failures:

1. Search the HR canary as finance, HR and another tenant. Inspect source IDs without widening a role. Objective: prove authorization independently of relevance.
2. Shorten a document and change its groups. Verify old local chunks/access disappear; contrast with non-atomic Azure replacement. Objective: distinguish local transactions from search-index visibility.
3. Install the wheel in a new environment and run the demo from an empty directory. Then add a paraphrase that lexical search misses. Objective: separate packaging failures from retrieval limitations.

Interview: **Why can a citation pass while the answer is wrong?** ID validation checks provenance membership, not semantic support. **Why not report recall on an empty relevant set as 100%?** Recall is undefined there; the benchmark records null and tests abstention/permissions separately.

Common failures: missing group membership, empty corpus, unsupported query vocabulary, stale cloud index, provider failure. Learn next: representative relevance labels, Azure hybrid quality, index-version deployment and semantic answer evaluation. Microsoft topics: AI-103 retrieval/indexing, grounding and search monitoring.

## Evals & Governance

| Concept | Important source | Decision to understand |
|---|---|---|
| Strict producer contract | `evalgov/models.py` | Reject malformed outputs and usage values |
| Metric limitations | `engine.py::score` | Substrings/citations are deterministic heuristics, not semantic judgment |
| Hard safety gates | `engine.py::evaluate` | Critical failures block even if aggregate score is acceptable |
| Compatible baselines | `engine.py` | Compare the same dataset fingerprint and ordered cases |
| Observation versus authority | `portfolio.py`, `policy.py` | Evaluation observes; policy advice never authorizes execution |

Debug three failures:

1. Construct a factually wrong answer containing the expected words. Explain why it passes and design an independently labeled semantic evaluation. Objective: understand metric validity.
2. Change a dataset case but reuse an old baseline. Diagnose the compatibility failure rather than dropping its hash. Objective: reproducible regression claims.
3. Test a target redirect, oversized response or missing permission. Confirm errors block the run and no response body enters reports. Objective: preserve target reliability/privacy boundaries.

Interview: **What does a green fixture run prove?** That the authored checks accept those fixtures, not that an LLM is reliable. **Why not execute tools during evaluation?** Observation avoids evaluation causing business effects; separate authorized scenario tests exercise execution.

Common failures: malformed output, incompatible baseline, forbidden canary, unexpected call, over-budget report. Learn next: semantic graders, reviewer disagreement, representative datasets and measured inference cost. Microsoft topics: AI-103 AI evaluation, safety monitoring and observability.

## Microsoft Automation

| Concept | Important source | Decision to understand |
|---|---|---|
| Narrow agent capability | `connectors/dossier-agent.swagger.json` | Agent only proposes and reads status |
| Separate identities | `automation/api.py` | Reviewer and executor roles remain unavailable to the connector |
| Immutable decision and retry | `api.py::decide`, `execute` | Replays do not create another local task |
| Actual artifact integrity | `solution/releases/`, `tests/test_solution_artifact.py` | Compare the exported ZIP with recorded hash and schema |
| Artifact versus runtime acceptance | `solution/README.md` | The reserved example host is not a working deployment |

Debug three failures:

1. Attempt approval with the agent key and self-review through another role. Trace the denied server check. Objective: authority cannot come from conversation text.
2. Mutate a local copy of the solution ZIP or authentication schema. Show the artifact regression test failing; do not modify the historical exported original. Objective: inspect packaging without a tenant write.
3. Design the trace for a future connector timeout after execution. Explain idempotency and why a tenant import cannot prove this behavior. Objective: understand the unverified runtime boundary.

Interview: **What was verified in Microsoft?** Historical isolated solution/connector import, export and reimport; current local checksum/schema checks. **What is still missing?** Approved hosted API, connection, actual agent/flow operation, identity, DLP and recorded tenant run outcomes.

Common failures: missing licence/connection, bad origin, wrong role, immutable decision, conflicting idempotency payload. Learn next: real environment ALM, connection references, DLP, Entra and tenant monitoring. Microsoft topics: PL-900 connectors, Dataverse, environments, flows and Copilot Studio.

## Transformation Playbook

| Concept | Important source | Decision to understand |
|---|---|---|
| Traceable assumptions | `data/scenarios.json`, `consulting/business_case.py` | Outputs are hypothetical capacity, not realized savings |
| Risk separate from score | `business_case.py::prioritize` | An attractive opportunity cannot average away a risk gate |
| Process and acceptance | `docs/01-discovery-process.md`, `02-delivery-contract.md` | Discover the task and define evidence before choosing tools |
| Optional system integration | `integration/scenario.py` | Independent APIs, no shared database, separate authority |
| Adoption and measurement | `docs/05-pilot-adoption.md` | Observed independent task competence matters more than attendance |

Debug three failures:

1. Reduce adoption to zero and increase rework. Explain negative capacity value and null payback without hiding the scenario. Objective: defend the business case.
2. Break one sibling API origin/credential in a temporary scenario. Find the failing boundary and clean up only the runner's own processes. Objective: diagnose integration without bypassing security.
3. Run verification into a new evidence directory and compare its results with the historical report. Explain changed counts and preserve old artifacts. Objective: evidence provenance and release discipline.

Interview: **How do you prove business impact?** Measure comparable tasks, rework, adoption, costs and errors before/after a controlled pilot. **Does this case prove consulting experience?** No; conduct and document your own workshop, acceptance review and user exercise before claiming personal proficiency.

Common failures: invalid rates, missing sibling installation, unavailable local model, incorrect role, biased assumptions. Learn next: real discovery facilitation, user acceptance, benefits realization and operational handover. Microsoft topics: PL-900 business value and governance; AI-103 monitoring/solution planning where relevant.
