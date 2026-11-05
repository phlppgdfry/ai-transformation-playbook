# Personal ownership plan — 14 days

All exercises start **NOT ASSESSED**. The author must execute and explain them. This task does not complete personal exercises or infer mastery from automated results. Repository paths below are relative to the named repository; workflow paths use its own src/workflow_platform directory.

Use a separate local practice branch, synthetic fixtures and temporary databases. Preserve release tags/main and dated evidence. Never push a deliberate defect. Record help used; attempt unaided first, then compare with source/docs. If stuck, request a small explanation and repeat the explanation independently later. No live cloud services are needed.

## 1. Explain the architecture unaided
**Objective:** Understand responsibility and authority, not memorize a diagram.
**Repository / exact files:** Playbook — `portfolio/SHOWCASE.md; integration/scenario.py`.
**Prerequisites:** HTTP request/response, component versus business process.
**Task:** Draw the business flow from memory. Mark each database/state owner, reviewer, model boundary and mock sink. Then compare your drawing with the runner call sites and correct it in another colour. Explain where a failure stops the process.
**Expected evidence:** A dated before/after drawing and a two-minute audio explanation.
**Acceptance:** All six responsibilities are named; workflow approval is separate from invoice approval; no cloud connection is invented.
**Common mistakes:** Copying the published diagram; calling all steps agents; claiming a shared transaction across services.
**Difficulty:** 1 — introductory.

## 2. Trace an HTTP request
**Objective:** Follow one real route through validation, identity, persistence and response.
**Repository / exact files:** Accounting — `src/accounting_copilot/api.py; src/accounting_copilot/models.py; src/accounting_copilot/store.py; tests/test_workflow.py`.
**Prerequisites:** Python functions/dicts, JSON, HTTP statuses.
**Task:** Choose POST /invoices. Read the actual model and route. Trace Idempotency-Key, principal/tenant, Store.submit, validation/duplicate paths and returned identifier. Run the existing relevant test locally, then explain a 409 versus a validation rejection.
**Expected evidence:** An annotated call trace with source function names and actual test output.
**Acceptance:** Trace includes the server-owned principal and tenant, amount model, persisted request identity and one failure response.
**Common mistakes:** Trusting a request role; confusing duplicate invoice identity with request replay; treating floats as exact currency.
**Difficulty:** 2 — supported practice.

## 3. Explain a database model
**Objective:** Connect persisted invariants to business behavior.
**Repository / exact files:** Accounting — `src/accounting_copilot/store.py; tests/test_workflow.py`.
**Prerequisites:** SQL table/key/unique constraint, transaction basics.
**Task:** Inspect the schema initialization. List the invoice, outbox and audit relationships using actual column names. Locate duplicate constraints and the transaction that saves approval/outbox state. Inspect only a temporary synthetic database.
**Expected evidence:** One-page schema sketch with two invariants and code references.
**Acceptance:** Can explain what commits together, what can be replayed, and why a real ERP is another transaction domain.
**Common mistakes:** Claiming immutable audit storage or external exactly-once effects because the local mock is atomic.
**Difficulty:** 2 — supported practice.

## 4. Explain an approval boundary
**Objective:** Distinguish role, identity and state.
**Repository / exact files:** Microsoft Automation — `automation/api.py; tests/test_boundary.py; connectors/dossier-agent.swagger.json`.
**Prerequisites:** Authentication versus authorization, state transitions.
**Task:** Find proposal, decision and execution operations. Run existing denial tests. Explain why the connector excludes privileged operations and why changing a conversation sentence cannot approve a task. Compare caller subject with creator identity.
**Expected evidence:** Role/operation matrix and one denied-request trace.
**Acceptance:** Names server-enforced reviewer/executor checks, tenant handling and immutable decision behavior; no agent key grants reviewer rights.
**Common mistakes:** Using another key with the same subject to claim independent approval; presenting an imported connector as live runtime.
**Difficulty:** 2 — supported practice.

## 5. Identify and assess a security risk
**Objective:** Separate a threat, an implemented control and an unverified limit.
**Repository / exact files:** Workflow — `src/workflow_platform/models.py; src/workflow_platform/integrations.py; tests/test_portfolio_tools.py`.
**Prerequisites:** Untrusted input, schemas, least privilege.
**Task:** Choose malicious tool-output text or a wrong-customer plan. Locate schema/scope checks and server-owned destination bindings. Write threat → possible effect → actual control → residual risk. Run an existing relevant denial test and explain its scope.
**Expected evidence:** A short threat note plus test output, not a universal safety claim.
**Acceptance:** Shows one concrete server check and admits what its test does not prove about prompt injection or production identity.
**Common mistakes:** Treating the LLM refusal or policy advice as authorization; claiming a test proves complete security.
**Difficulty:** 2 — supported practice.

## 6. Explain a failed evaluation
**Objective:** Interpret a gate and metric validity.
**Repository / exact files:** Evals — `evalgov/engine.py; evalgov/datasets/responses-unsafe.json; tests/test_engine.py`.
**Prerequisites:** JSON, test expectations, positive/negative controls.
**Task:** Run good and unsafe fixtures to new reports under reports/ownership. Inspect the first failed check and trace its definition to score/evaluate. Explain expected exit 1 for unsafe. Find one answer that could contain expected words but still be false.
**Expected evidence:** One failure explanation with case ID, metric definition and limitation.
**Acceptance:** Distinguishes deliberate negative control from execution failure; does not infer general LLM quality from authored fixture success.
**Common mistakes:** Quoting the aggregate score without the hard gate; editing expected answers just to get green.
**Difficulty:** 2 — supported practice.

## 7. Modify one small behavior
**Objective:** Translate a hypothetical requirement into a bounded code change.
**Repository / exact files:** Playbook — `consulting/business_case.py::prioritize; tests/test_business_case.py`.
**Prerequisites:** Python conditionals, numeric comparisons, Git diff.
**Task:** In a separate practice branch, define a fictional policy requiring specialist review from risk 3 instead of 4. State acceptance cases for risks 2.9, 3 and 3.5 before editing. Change only the gate threshold. Do not change weighting or historical scenario evidence.
**Expected evidence:** A requirement note and a small diff with expected output.
**Acceptance:** Boundary behavior matches the stated hypothetical policy; no change is merged/pushed or presented as a real client rule.
**Common mistakes:** Changing many rules at once; increasing weighted priority to hide risk; overwriting dated evidence.
**Difficulty:** 2 — supported practice.

## 8. Add one meaningful test
**Objective:** Prove a business boundary that would fail before the practice change.
**Repository / exact files:** Playbook — `tests/test_business_case.py; consulting/business_case.py`.
**Prerequisites:** unittest assertions, test setup, boundary values.
**Task:** For exercise 7, add a case with excellent impact/feasibility and risk 3.5. Assert specialist_review even with a high priority score, plus a below-threshold control. Demonstrate the new requirement test fails against the old threshold and passes against the practice change.
**Expected evidence:** Red/green outputs and the test diff, with an explanation of why it protects the new policy.
**Acceptance:** Test checks observable gate behavior and the risk/priority separation; old policy fails for a documented reason.
**Common mistakes:** Only asserting the numeric constant; duplicating a current risk-5 test; claiming the hypothetical change belongs in production.
**Difficulty:** 2 — supported practice.

## 9. Debug an introduced defect
**Objective:** Diagnose a permission regression without weakening the requirement.
**Repository / exact files:** Knowledge — `rag/core.py::Store.retrieve; tests/test_retrieval.py; tests/test_security_regressions.py`.
**Prerequisites:** Python sets/JSON, tenant and group permissions, isolated tests.
**Task:** Use a disposable practice checkout and tests with temporary databases only. Deliberately bypass the group-membership condition in retrieve. Run the finance/HR denial regression and observe failure. Trace the leak path, restore the original condition manually and rerun. Never start a public server or commit the defective variant.
**Expected evidence:** Failing then passing test output, root-cause note and final diff showing no retained insecure edit.
**Acceptance:** Explains why filtering precedes ranking and how restoration prevents unauthorized sources; original requirements unchanged.
**Common mistakes:** Editing the denial expectation; widening permissions to make retrieval pass; using real data or pushing the defect.
**Difficulty:** 3 — requires care.

## 10. Explain the business consequences
**Objective:** Make a technical trade-off legible to a process owner.
**Repository / exact files:** Playbook and Workflow — `docs/02-delivery-contract.md; docs/05-pilot-adoption.md; consulting/business_case.py; agentic-workflow-platform: src/workflow_platform/engine.py`.
**Prerequisites:** Acceptance criteria, latency/cost, user workflow.
**Task:** Compare a strict three-tool proposal with a hypothetical adaptive loop. Identify benefits, rejection/recovery costs, human workload and measurement needs. Write a short decision note that could justify retaining the existing fixed engine, with an explicit condition for revisiting it.
**Expected evidence:** A one-page decision note with assumptions, two trade-offs and pilot measures.
**Acceptance:** Separates hypothetical outcomes from observations; includes adoption/rework and an accountable decision owner.
**Common mistakes:** Calling a framework upgrade a business result; treating capacity value as cash savings or inventing stakeholder agreement.
**Difficulty:** 2 — supported practice.

## Fourteen-day schedule — 60–90 minutes daily

| Day | Work | Time budget | Evidence / exit condition |
|---|---|---|---|
| 1 | Exercise 1: draw the process and six responsibilities | 20 read + 30 draw + 15 explain | Unaided first drawing saved |
| 2 | Exercise 1 review; identify fixture/model/mock boundaries | 20 compare + 30 explain + 15 notes | Corrected drawing and recorded explanation |
| 3 | Exercise 2 HTTP trace | 20 prerequisites + 35 trace + 20 test | Route-to-store failure path explained |
| 4 | Exercise 3 schema and transaction | 20 SQL basics + 40 inspect + 15 draw | Actual constraints and local/external boundary |
| 5 | Exercise 4 approval and identities | 20 inspect + 30 test + 20 explain | Denied operation and separate authority |
| 6 | Exercise 5 concrete threat/control/residual risk | 25 inspect + 30 test + 20 note | One evidence-backed threat analysis |
| 7 | Exercise 6 unsafe evaluation | 20 run + 30 inspect + 20 explain | Case-level failure with metric limitation |
| 8 | Exercise 7 hypothetical policy change | 20 requirement + 35 edit + 15 review | Small practice-only diff |
| 9 | Exercise 8 meaningful regression | 20 design + 35 red/green + 20 explain | Requirement test red before / green after |
| 10 | Exercise 9 controlled permission defect | 20 setup + 30 diagnose + 25 restore | Fail/pass trace, no insecure edit retained |
| 11 | Exercise 10 business trade-off | 20 inspect + 35 write + 15 rehearse | Decision note with measures and assumptions |
| 12 | Rehearse the three-minute demo | 20 setup + 25 rehearse + 20 review | Explain modes and limitations in own words |
| 13 | Answer interview questions and request a peer review | 30 Q&A + 25 revise + 15 notes | Record gaps honestly; peer may remain pending |
| 14 | Choose a role track, tailor CV and plan applications | 25 role screen + 25 materials + 20 plan | A truthful application draft, not an invented employment claim |

## Evidence log and self-assessment

For each exercise record date, source revision, commands, actual output, help used, explanation and reviewer feedback. Mark **attempted**, **needs help**, or **independently explained**; completion requires the acceptance criteria, not elapsed study time. If a task takes longer, move the next day rather than falsely ticking it complete. No external assessor, certification or client outcome is implied.
