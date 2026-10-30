# Recruiter and interview handover

Use these as prompts for your own explanation. The software's demonstrated behavior is supported by evidence; your independent proficiency has **not been assessed**. Do not imply client work, achieved savings, production operation or Microsoft runtime delivery.

## Thirty seconds

“This portfolio follows a fictional accounting practice improving invoice review. Six small repositories connect process discovery and a transparent business case to invoice automation, controlled AI tool proposals, permission-filtered knowledge, evaluation and a Microsoft connector artifact. The integrated demonstration runs locally, including an optional genuine local model. Human authority stays in the application. Cloud quality and full Copilot Studio runtime are explicit remaining validation steps.”

## Two minutes

“The business question is where AI can reduce handling effort without obscuring accountability. The consulting playbook documents process, requirements, risks, adoption and scenario assumptions. Its calculator estimates capacity under different adoption and rework assumptions; these are not achieved cash savings.

“The accounting application validates amounts and duplicates, requires an independent reviewer, and records local mock ERP export through an outbox. The workflow platform proposes a bounded sequence of tools, reads actual invoice and policy APIs, persists execution and waits for approval. The model cannot grant itself authority. The knowledge assistant filters access before retrieval. Evaluations inspect the resulting contracts and security cases, retaining both positive and deliberately unsafe controls.

“The Microsoft repository provides a real exported connector solution plus a locally working approval API. Import acceptance does not prove a live agent or flow is running. All business effects remain synthetic local mocks. The code and evidence are available for technical inspection, and the learning exercises test whether I can independently explain and debug each boundary.”

## Match the role

| Role | Lead with | Demonstrate yourself before claiming proficiency |
|---|---|---|
| AI & Automation Consultant | Process fit, human review, exceptions, evaluation and adoption | Explain why a model is useful for a proposal but cannot authorize an action |
| Digital Transformation Analyst | Current/future process, assumptions, risk, pilot and benefits | Run a discovery workshop and defend a measurement plan without hypothetical ROI becoming a result |
| Functional Analyst | Requirements, role matrix, acceptance and failure scenarios | Translate an invoice correction or rejection need into testable acceptance criteria |
| Business Applications Analyst | API contract, state transitions, integration and support | Diagnose a denied role, stale decision or conflicting idempotency request |
| Junior AI Solutions Engineer | Schemas, provider failures, tool scopes, retrieval and tests | Change a small rule, add a meaningful regression test and trace an end-to-end request |

## Five-minute demonstration

Use fresh temporary state and the [existing integration guide](../../integration/README.md). Have the five sibling API environments installed. Run the calculator and scenario in separate terminals. Browser checks are optional automation of the same interactions, using installed Chrome.

| Time | Show | Explain |
|---|---|---|
| 0:00–0:45 | Calculator assumptions; set adoption to zero | Fictional process, hypothetical capacity, no positive payback without benefit |
| 0:45–2:00 | Accounting JSON source import, submit, denied operator approval, independent reviewer | Explicit fields are not OCR; schema and server role checks are executable controls |
| 2:00–3:00 | Workflow tool receipts and approval wait | Actual invoice/policy HTTP reads; fixture mode label or separately recorded genuine Qwen run; no export credentials for model |
| 3:00–4:00 | Finance policy search then denied HR canary; good/unsafe evaluation controls | Authorization before retrieval; heuristic tests with useful but limited evidence |
| 4:00–4:30 | Separate invoice approval, local export and audit | Workflow approval does not approve an invoice; repeated export does not duplicate the local effect |
| 4:30–5:00 | Microsoft solution and release report | Artifact verification differs from runtime; cloud and personal ownership limitations |

Do not share the temporary session file: it holds synthetic role keys. Stop your own servers normally so the runner removes its databases and session. No cloud provisioning or model download is required by the default scenario.

## Fifteen-minute technical walkthrough

| Time | Inspect | Decision or failure to explain |
|---|---|---|
| 0–2 min | `consulting/business_case.py`, `data/scenarios.json` | Adoption/coverage/rework/cost assumptions; risk gate separate from ranking |
| 2–5 min | Accounting `models.py`, `store.py`, `api.py` | Decimal amounts, duplicate identity, stale versions, independent approval, local transaction/outbox |
| 5–8 min | Workflow `models.py`, `engine.py`, `store.py`, `integrations.py` | Bounded tool plan, unchanged scope, lease fencing, cancellation and saved receipts |
| 8–10 min | RAG `core.py`, `azure.py`, `evaluate.py` | Access before ranking; local lexical search versus optional cloud hybrid; citations are not entailment |
| 10–12 min | Evals `engine.py`, `portfolio.py` | Hard gates, compatible baseline, unsafe negative control, observation without effects |
| 12–13 min | Automation connector, `automation/api.py`, exported ZIP | Agent proposal/status only; independent reviewer/executor; artifact versus runtime |
| 13–15 min | Release checks and CI evidence | Installed wheel outside source, dependency/secret checks, hosted results versus local results |

The [architecture diagram](../SHOWCASE.md) describes actual local boundaries. Separate state owners avoid an unnecessary shared platform. Existing small modules were retained instead of migrating frameworks. A real ERP sink needs its own reconciliation contract; a shared local transaction cannot prove external exactly-once delivery.

## Practice questions and defensible answers

1. **What is actually AI here?** Optional Ollama/Qwen makes native tool calls for a bounded plan. Default planning is deterministic. Local retrieval uses lexical extracts. Live Azure generation and extraction quality are unverified.
2. **Can prompt injection approve an invoice?** Text has no approval authority; server roles, independent identity and state checks enforce the decision. This does not prove universal prompt-injection protection.
3. **Why keep human approval outside the agent?** A proposed action and an authorization decision have different owners. Agent-accessible credentials cannot call privileged reviewer/executor operations.
4. **What does an idempotency key protect?** Request replays with identical content; changed content conflicts. Business duplicate identity and external reconciliation are separate concerns.
5. **Can good citations still accompany a false answer?** Yes. Allowed source membership does not establish semantic support. Representative labeled evaluation is still needed.
6. **What does a passing evaluation prove?** The specific executed checks passed on the recorded cases. Fixture success is not evidence of model quality or absolute safety.
7. **Why no multi-agent framework?** This fixed process already has durable checkpoints and controlled tools. Added coordination must solve a demonstrated requirement.
8. **What did the Microsoft export prove?** Historical tenant artifact acceptance and current local integrity/schema checks; no full agent/flow runtime operation.
9. **How would you demonstrate business impact?** Agree comparable tasks, baseline handling time, rework, adoption, cost and error measures, then test a controlled pilot. Capacity estimates are not realized savings.
10. **What must change before real customer data?** Enterprise identity, approved hosting/operations, real-sink recovery, retention and representative quality/security validation, with explicit cloud authorization.

## Personal ownership gate

Before interviews, complete one exercise per repository from [LEARNING.md](../release-2026-10-30/LEARNING.md). Without assistance, explain the failing test, find its source path, make a focused change, rerun the affected checks and explain the tradeoff. Then run the integrated demo and diagnose one denied request without widening permissions.

Essential concepts: business requirements and acceptance; Decimal financial validation; server-owned identity/tenant scope; idempotency versus duplicate detection; transactions/outbox; leases and fencing; tool schemas and bounded inference; retrieval authorization; citation versus groundedness; negative controls and metric validity; connector versus runtime; adoption and measured benefits.

Existing files and test results demonstrate implementation. Passing these ownership exercises yourself would provide evidence of your understanding; no such personal assessment is claimed here.
