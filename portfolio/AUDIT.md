# Portfolio baseline audit — 29 October 2026

Scope: six existing private repositories, all clean on `main`, with matching `phlppgdfry` remotes. No remote writes. Exact starting commits, commands, output and dependency consistency checks: [baseline.json](baseline.json). Tests were rerun, not inferred from yesterday's evidence. No maturity score is assigned: local correctness, cloud verification and operational readiness are separate dimensions.

## Baseline findings

| Repository | Strengths verified in source/tests | Missing capability / debt | Enterprise and interview readiness |
|---|---|---|---|
| Accounting | 29 passing tests; Decimal validation, supplier checks, duplicate detection, four-eyes review, tenant filtering, atomic outbox, retryable local ERP, HTML console; optional Document Intelligence + structured Azure classification adapters | Console submits JSON; no source upload/preview workflow; no calibrated confidence or quality dataset; API-key identity; no global request size or rate limits; provider polling can occupy a worker for minutes | Strong small workflow demonstration. Azure HTTP contracts are mocked, not cloud-tested. Local database atomicity does not prove remote exactly-once delivery. |
| Workflow | 25 passing tests; validated Azure function-call plans, three allowlisted tools, durable cursor/receipts, expiring worker leases/fencing, retry backoff, independent approval | Tool implementations all local fixtures; no cancellation or debugging UI; fixed ordered planning rather than adaptive agent loop; no model usage telemetry | Defensible bounded workflow, not a multi-agent platform or proven production agent. SQLite serializes operations; no distributed scheduler. |
| Evals | 23 passing tests; versioned 16-case dataset, positive/negative fixtures, strict schemas, critical safety gates, baseline compatibility, HTML report, roles, optional HTTP target | No actual portfolio targets; substring checks do not establish groundedness; no retrieval ranking metrics; single organization; synchronous process-local admission lock | Useful release-check framework. Fixture pass rates measure authored controls, not model intelligence. Costs use illustrative tariffs and fixture token counts. |
| RAG | 12 passing tests; ACL before lexical ranking, chunk hashes, local atomic replace/delete, Azure embeddings + prefiltered hybrid search, response ACL validation and citation allowlist | Cloud uploader only merge-or-uploads, leaving stale chunks after shorter updates/removals; no retrieval benchmark; no search UI; static token option lacks refresh; local store loads corpus in memory | Strong access-boundary demonstration, limited corpus scale. No live Azure retrieval or semantic quality evidence. Cloud document lifecycle needs repair before pilot use. |
| Microsoft automation | 6 passing tests; proposal/review/execute boundary, cross-tenant protection, immutable decisions, concurrent idempotency tests, agent-only Swagger connector | Flow is a recipe, not imported solution; no verified tenant, Graph, Dataverse or actual Copilot agent; weak configured keys accepted; no response models on full OpenAPI | Runnable local reference and generated connector. Tenant acceptance remains mandatory. Generating a fake solution ZIP would reduce credibility. |
| Playbook | 6 passing tests; transparent capacity model, risk separate from priority score, workshop/requirements/adoption/risk templates, learning tracker | CLI only; no interactive scenario exploration; no executable portfolio integration; no executive presentation; assumptions need sensitivity exploration | Good fictional consulting case. No observed client outcomes, user adoption, or assessed candidate competency. |

Common strengths: independent dependency locks, restrictive local container bindings, MIT licenses, CI with read-only GitHub permissions, honest limitations, synthetic data. Common gaps: no Entra identity, hosted operational evidence, retention automation, load testing, dependency CVE scan evidence, or shared integration contracts. Five pytest suites emit one upstream TestClient deprecation warning each. `pip check` checks package consistency, not vulnerabilities.

Security review findings: accounting/RAG/automation compare string API keys with `hmac.compare_digest`; non-ASCII header values can raise `TypeError` instead of returning 401. Validation error bodies outside accounting may echo submitted values. Server identity boundaries are already substantive and should be preserved. Database administrators can alter audit rows; these are not immutable compliance records.

## Evidence-based backlog

Priority describes impact, not an assertion that every item is a current exploitable vulnerability. P0 defects precede P1 work; P2/P3 are optional.

| ID | Priority | Change / acceptance evidence | Type |
|---|---|---|---|
| SEC-01 | P0 | Malformed credential consistently returns 401; regression tests across API boundaries | Availability defect |
| INT-01 | P0 | Actual local API scenario crosses accounting, workflow, RAG, governance and automation; export impossible without separate accounting approval; repeat export creates no duplicate | Missing verification |
| RAG-01 | P1 | Explicit Azure document replacement removes all old parent chunks, bounds batches, rejects partial failures; contract tests, no cloud claim | Lifecycle correctness |
| AGT-01 | P1 | Server-configured read-only accounting/RAG tools; deny unmapped tenants/customers, no agent URLs or write credentials, dependency failure tested | Integration capability |
| AGT-02 | P1 | Persisted cancellation fences workers and prevents outbox delivery, including approved runs | Reliability |
| EVAL-01 | P1 | Reusable portfolio RAG/workflow evaluation targets and versioned datasets; real API observations, unauthorized cases, reproducible ranking metrics | Evaluation gap |
| UX-01 | P1 | Accounting upload/preview/review, workflow timeline/approvals, interactive business scenarios; responsive browser tests and authentic screenshots | Usability |
| MS-01 | P1 | Validate importable connector and parameterized packaging assets; document tenant acceptance and licensing boundary exactly | Microsoft readiness |
| SEC-02 | P1 | Bounded request bodies, safe errors, least-privilege adapter credentials, dependency audit evidence | Hardening |
| AI-01 | P1 | Live extraction, tool calling and hybrid retrieval quality against approved Azure resources | Credential/resource dependent; not authorized to provision |
| OPS-01 | P2 | Trace correlation, latency/model-usage history, container re-verification and Entra deployment exercise | Operational enhancement |
| DOC-01 | P2 | Concise READMEs, per-feature evidence matrices, architecture, screenshots, executive materials, interview exercises | Presentation |
| OPT-01 | P3 | Framework migration, MCP, additional model providers, reranker, multi-agent coordination | Only if a concrete requirement emerges |

## Architecture decision

Keep five independently runnable local APIs and one standard-library consulting tool. Integration is an opt-in runner, not shared runtime storage or mandatory microservices. Accounting owns invoice approval/export; workflow owns its separate proposal lifecycle; RAG owns document access; governance provides evaluation/advice and never grants write authority; Microsoft automation exposes proposals through a restricted connector; playbook owns the reproducible case and business assumptions. Cross-repository tools use existing HTTP contracts with server-configured identities.

Microsoft Agent Framework and LangGraph were resolved and read using Context7 on 29 October 2026. Both offer checkpointed execution and human interaction; neither substitutes for application authorization or external sink idempotency. Retain the current engine for its three fixed steps and tested leases. Reconsider LangGraph for dynamic branching/resume, Agent Framework for an actual Microsoft-hosted agent requirement. Do not add MCP: direct fixed REST integrations do not currently need client-discovered tool catalogs.

Sources: [Agent Framework checkpoint/HITL sample](https://github.com/microsoft/agent-framework/blob/main/python/samples/03-workflows/checkpoint/checkpoint_with_human_in_the_loop.py), [LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts), [Azure Search deletion](https://learn.microsoft.com/en-us/azure/search/search-how-to-delete-documents). Documentation review is not execution of these frameworks.
