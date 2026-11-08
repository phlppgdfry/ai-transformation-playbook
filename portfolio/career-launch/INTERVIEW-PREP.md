# Interview preparation

Use this as an evidence map, not a script of fictional first-person experience. Twenty-four questions span eight groups. Source filenames are relative to the named component; workflow files are under src/workflow_platform and accounting files under src/accounting_copilot. For deeper exercises use [the ownership plan](OWNERSHIP-PLAN.md).

## Business analysis

### 1. What problem would you validate before proposing AI?
- **Why asked:** Checks problem discovery before tool selection.
- **Evidence:** Playbook docs/01-discovery-process.md.
- **Credible points:** Observe review steps, exceptions, current handling/rework and accountable process owners; scenario assumptions are not client research.
- **Follow-up:** What evidence would make you reject AI here?
- **Weak/misleading:** We deployed AI to save time, without a baseline or observed user need.

### 2. Turn independent approval into an acceptance criterion.
- **Why asked:** Tests precision and negative cases.
- **Evidence:** Accounting tests/test_workflow.py and store.py::decide.
- **Credible points:** Specify creator versus reviewer identity, role, version and expected denial/approval states; include same-subject alternate credentials.
- **Follow-up:** What happens when the invoice changes after review?
- **Weak/misleading:** A user clicks approve; no server or concurrency condition.

### 3. How would you assess benefits?
- **Why asked:** Checks whether business claims follow measurements.
- **Evidence:** Playbook consulting/business_case.py; docs/05-pilot-adoption.md.
- **Credible points:** Compare similar tasks, adoption, rework, time, errors and actual cost in a controlled pilot; distinguish capacity from cash.
- **Follow-up:** Who owns realization of the benefit?
- **Weak/misleading:** Quote the calculator output as a client saving.

## AI fundamentals

### 4. Which parts actually use a model?
- **Why asked:** Tests model versus deterministic literacy.
- **Evidence:** Workflow planners.py/ollama.py; Knowledge rag/core.py; retained local-inference evidence.
- **Credible points:** Fixture plan is model-free; optional Qwen makes a bounded tool plan; local knowledge uses lexical extracts; live Azure quality unverified.
- **Follow-up:** Why can the demo still be useful without an LLM?
- **Weak/misleading:** Every component is AI because it is named Copilot or RAG.

### 5. What does confidence mean for invoice extraction?
- **Why asked:** Tests calibration and uncertainty.
- **Evidence:** Accounting providers.py; extraction.py; tests/test_extraction_review.py.
- **Credible points:** Provider confidence supports a review proposal, not approval or an unmeasured accuracy probability; calibrate on permitted labeled data.
- **Follow-up:** What would you do with a missing high-value field?
- **Weak/misleading:** 95% confidence guarantees 95% correctness.

### 6. Can a valid citation accompany a false answer?
- **Why asked:** Tests provenance versus grounding.
- **Evidence:** Knowledge rag/azure.py; evalgov/engine.py.
- **Credible points:** Allowed source IDs show membership, not semantic entailment; representative labeled answer checks remain needed.
- **Follow-up:** How would you test an unsupported conclusion?
- **Weak/misleading:** A citation makes hallucination impossible.

## System architecture

### 7. Why six repositories?
- **Why asked:** Checks boundary reasoning rather than code volume.
- **Evidence:** Central SHOWCASE.md; integration/scenario.py.
- **Credible points:** Separate business state, orchestration, knowledge, evaluation, Microsoft adapter and consulting artifacts; optional HTTP runner, no shared database.
- **Follow-up:** What operational cost does that separation introduce?
- **Weak/misleading:** Microservices are automatically enterprise-grade.

### 8. Why retain a fixed workflow engine?
- **Why asked:** Checks whether complexity has a requirement.
- **Evidence:** Workflow engine.py; store.py; models.py.
- **Credible points:** Bounded process with checkpoints, retries, leases and approvals already fits the scenario; adaptive agents/frameworks need a real requirement.
- **Follow-up:** When would the fixed process become restrictive?
- **Weak/misleading:** More agents or frameworks would look more advanced.

### 9. What does the local outbox prove?
- **Why asked:** Tests transaction-domain limits.
- **Evidence:** Accounting store.py::decide/export_mock.
- **Credible points:** Approval/outbox and local mock effects share controlled SQLite transactions; a remote ERP requires idempotency and reconciliation.
- **Follow-up:** How do you recover an uncertain external outcome?
- **Weak/misleading:** The local demo proves exactly-once delivery to any ERP.

## Integration

### 10. How do you prevent an LLM choosing an arbitrary endpoint?
- **Why asked:** Tests trust in tool arguments.
- **Evidence:** Workflow integrations.py; tests/test_portfolio_tools.py.
- **Credible points:** Server owns origins, credentials and invoice binding; schemas/allowlist/scope checks constrain proposed calls.
- **Follow-up:** What if an approved dependency returns malicious text?
- **Weak/misleading:** Ask the model to use trusted URLs.

### 11. What did the Microsoft solution verify?
- **Why asked:** Tests honest platform scope.
- **Evidence:** Automation solution/README.md; tests/test_solution_artifact.py.
- **Credible points:** Historical import/export/reimport plus current checksum/schema checks; reserved host, no verified active connection/agent/flow.
- **Follow-up:** What must a tenant administrator still configure?
- **Weak/misleading:** Import success proves a working end-to-end Copilot.

### 12. How do you handle a repeated request?
- **Why asked:** Tests identity and recovery semantics.
- **Evidence:** Accounting store.py; Automation api.py; workflow tests.
- **Credible points:** Same key/same payload replays safely; conflicting payload is rejected; business duplicates and external uncertain results are separate concerns.
- **Follow-up:** What if the caller times out after the server commits?
- **Weak/misleading:** Just retry with a new key until it succeeds.

## Security and governance

### 13. Can a prompt authorize an action?
- **Why asked:** Checks authority outside model text.
- **Evidence:** Workflow models.py/store.py; Automation connector and api.py.
- **Credible points:** No; identity, role, tenant, state and independent decision checks enforce authority. Tests do not prove universal injection resistance.
- **Follow-up:** Can one subject approve through another role key?
- **Weak/misleading:** The system prompt tells the model not to approve.

### 14. Why filter access before retrieval?
- **Why asked:** Tests leakage pathways.
- **Evidence:** Knowledge rag/core.py::retrieve; tests/test_retrieval.py.
- **Credible points:** Unauthorized documents must not enter results or local corpus statistics/context; tenant/groups are server configuration.
- **Follow-up:** What happens after a document ACL update?
- **Weak/misleading:** Hide forbidden citations after generating the answer.

### 15. What does a green evaluation gate establish?
- **Why asked:** Tests evidence scope.
- **Evidence:** Evals engine.py; tests/test_engine.py; dataset fingerprint.
- **Credible points:** The executed checks passed on the recorded cases and compatible baseline; heuristic quality and security coverage remain limited.
- **Follow-up:** Could an incorrect answer satisfy required keywords?
- **Weak/misleading:** It certifies safety, compliance and model quality.

## Product thinking

### 16. How would you prioritize this use case?
- **Why asked:** Checks value/feasibility/risk judgment.
- **Evidence:** Playbook business_case.py::prioritize; data/use-cases.csv.
- **Credible points:** Frame user need, readiness, impact and adoption; risk is a separate gate, not something a weighted score averages away.
- **Follow-up:** Which unknown would you investigate first?
- **Weak/misleading:** Choose the highest technical novelty or AI trend.

### 17. What would you remove from a first pilot?
- **Why asked:** Tests scope discipline.
- **Evidence:** Release limitations; consulting delivery contract.
- **Credible points:** Keep a bounded, synthetic/approved workflow with explicit acceptance; avoid extra providers, agents or integrations without need.
- **Follow-up:** What is the smallest result a process owner can assess?
- **Weak/misleading:** Build every integration before showing a user anything.

### 18. How would you improve adoption?
- **Why asked:** Checks user support beyond implementation.
- **Evidence:** Playbook docs/05-pilot-adoption.md.
- **Credible points:** Agree responsibilities, train on real tasks, provide exception/support paths and measure independent task performance plus actual usage.
- **Follow-up:** What would low adoption do to the business case?
- **Weak/misleading:** Training attendance proves adoption.

## Project ownership

### 19. How much did you personally build, and how did you use AI?
- **Why asked:** Tests integrity and learning ownership.
- **Evidence:** Contribution section; OWNERSHIP-PLAN.md; actual personal evidence log when available.
- **Credible points:** State substantial AI assistance, author-directed intent, tool-executed evidence and exactly which unaided tasks you can demonstrate; disclose unassessed areas.
- **Follow-up:** Show a change you can explain without generated help.
- **Weak/misleading:** I manually wrote and architected every line, or dismissing all responsibility because AI helped.

### 20. Trace one request right now.
- **Why asked:** Distinguishes repository familiarity from memorization.
- **Evidence:** Accounting api.py → models.py/store.py → tests/test_workflow.py.
- **Credible points:** Locate real route, principal, validation, persistence, replay and response; narrate an error path with code references.
- **Follow-up:** Where would you set a breakpoint or add a diagnostic?
- **Weak/misleading:** Repeat the architecture diagram without opening the actual route.

### 21. What can you confidently change independently today?
- **Why asked:** Tests truthful readiness.
- **Evidence:** Your completed ownership evidence, not repository test counts.
- **Credible points:** Name a genuinely completed bounded exercise, show its diff/test and remaining help needs. If none yet, say so and demonstrate current understanding.
- **Follow-up:** Why is the new test meaningful?
- **Weak/misleading:** Passing 172 assisted tests means I independently master every component.

## Technical trade-offs

### 22. Why use SQLite and API keys?
- **Why asked:** Tests contextual engineering decisions.
- **Evidence:** Per-repository architecture/security docs.
- **Credible points:** Simple reproducible single-host reference; production identity, HA, rotation and distributed operations are separate pilot requirements.
- **Follow-up:** Which failure would make SQLite unsuitable here?
- **Weak/misleading:** SQLite/API keys are either universally enterprise-ready or universally wrong.

### 23. What is the cost of strict model-plan validation?
- **Why asked:** Tests safety versus usefulness.
- **Evidence:** Workflow models.py::Plan.check_scope; planners.py.
- **Credible points:** Invalid/extra/out-of-scope plans fail closed; useful but differently ordered plans may be rejected; evaluate that trade-off on representative cases.
- **Follow-up:** How would you measure rejection and recovery burden?
- **Weak/misleading:** Rejecting everything unsafe has no usability cost.

### 24. Why keep documentation corrections after an immutable tag?
- **Why asked:** Tests release provenance.
- **Evidence:** November final handover; milestone tags and main history.
- **Credible points:** Tags preserve audited implementation; documented rendering/status follow-ups on main do not rewrite history; distinguish source and evidence revisions.
- **Follow-up:** How would you reproduce the exact tagged package?
- **Weak/misleading:** Move the published tag silently so it looks perfect.

## Answering the AI-assistance question truthfully

Use four statements, each tied to something you can show: (1) the independent portfolio goal and fictional scope; (2) substantial AI generation/iteration in code, architecture and documentation; (3) the actual test/release evidence and your ability to inspect it; (4) the specific debugging/change tasks you have personally completed, with help disclosed. Do not invent a workshop, production incident or independent coding session. If the personal exercises are not complete, say “not yet assessed” rather than treating the repository as a qualification.

A professional answer accepts responsibility for understanding what is presented while being precise about assistance. An interviewer may ask you to trace a function, explain a failing test or change a small rule; prepare through practice, not memorized senior-level phrasing.
