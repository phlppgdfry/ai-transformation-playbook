# Independent presentation audit — 5 November 2026

Scope: all six current READMEs, main/tag/CI state, canonical showcase, release handover, architecture/source entry points, screenshots and existing demonstration/learning instructions. [Current repository evidence](evidence/baseline.json) confirms public visibility and successful CI on the fetched main SHAs. Scores describe presentation suitability, not professional competence or objective engineering maturity. No runtime expansion is proposed.

## Rubric

0 = absent or contradicted; 1 = assertion without usable support; 2 = partial, difficult to find or materially unclear; 3 = usable with reviewer effort; 4 = clear and supported with a small limitation; 5 = exceptionally direct, complete for the stated audience and independently navigable. A 5 never means production certification or personal mastery. Baseline scores below precede the career-launch edits; no artificial post-edit perfect score is assigned. Do not average away a limitation.

B = business value; T = technical credibility; D = demonstrability; A = architecture; Doc = documentation; E = evidence; P = presentation; R = recruiter accessibility; H = hiring-manager relevance; O = honesty.

| Repository | B | T | D | A | Doc | E | P | R | H | O |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Accounting | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 |
| Workflow | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 |
| Knowledge | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 |
| Evals | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 |
| Microsoft automation | 3 | 4 | 3 | 4 | 4 | 3 | 3 | 3 | 4 | 4 |
| Playbook | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 3 | 4 | 3 |

## Repository findings and evidence

- **Accounting:** clear invoice business trigger, realistic exception/reviewer/export workspace and reproducible CLI. `src/accounting_copilot/models.py`, `store.py`, `tests/test_workflow.py`, README and `docs/security.md` support the technical story. Exact amounts/outbox language needs plain explanation for recruiters. Synthetic mock ERP and unverified live Azure limits are already explicit. Keep the implementation and independent quick start.
- **Workflow:** strongest bounded-tool engineering evidence, supported by `src/workflow_platform/engine.py`, `models.py`, `tests/test_workflows.py`, `tests/test_cancellation.py` and README. Technical terms precede a clear personal-career story. Explain persisted steps and separate authority without marketing it as autonomous multi-agent reasoning. Keep the fixed engine and real-versus-fixture distinction.
- **Knowledge:** access before retrieval, visible sources and explicit local/cloud modes. Inspect `rag/core.py`, `rag/azure.py`, `tests/test_retrieval.py` and `docs/architecture.md`. Local lexical extracts are valuable for the demonstration but are not semantic LLM RAG; preserve that distinction. Avoid adding SharePoint or cloud work to improve a presentation score.
- **Evals:** positive and unsafe controls, reproducible reports and metric definitions. `evalgov/engine.py`, `evalgov/portfolio.py`, `tests/test_engine.py` and `docs/evaluation-design.md` support inspection. A recruiter needs to hear why a deliberately blocked run is evidence rather than a broken product. No semantic safety guarantee should replace the current heuristic limitations.
- **Microsoft:** actual exported connector and local role boundaries are supported by `solution/README.md`, `tests/test_solution_artifact.py` and `automation/api.py`. Artifact acceptance is less immediately demonstrable than a full tenant conversation, so D/E remain lower. Keep the reserved host and runtime limitation; do not invent a tenant video or dashboard.
- **Playbook:** genuine central case, calculator and extensive release evidence. `consulting/business_case.py`, `docs/01-discovery-process.md`, `portfolio/SHOWCASE.md` and the November handover provide depth. Initial overview did not introduce Philippe or target entry roles. Lower README text said repositories were private while the top said public; `integration/README.md` repeated private wording. Historical October reports are useful archives but confusing when treated as current entry pages.

All component README/source links are reachable from the [central responsibility matrix](../SHOWCASE.md#proposed-solution); the exact fetched revisions are in the baseline snapshot. [Historical verification index](../release-2026-11-01/FINAL-HANDOVER.md) supports the evidence scores, with its date and scope preserved.

## Prioritized backlog and resolution

| Priority | Finding | Action in this branch |
|---|---|---|
| P0 | No confirmed new secret or fabricated customer-result finding in the inspected current entry material | New content still requires staged secret/claim review; do not treat historical scans as permanent proof |
| P1 | Central opening explains components before author, relevant problems and realistic role direction | Add identity, ~100-word overview, contribution boundaries and reader routes |
| P1 | Contradictory private status in central README and integration quick start | Correct the two current instructions; preserve dated evidence |
| P1 | Senior-sounding role shorthand could be inferred from technical breadth | Position toward analysis/implementation/product entry roles; separate artifact behavior from assessed personal skill |
| P2 | Prior handovers contain good material but application/recording assets are scattered | Add a compact career index; link deeper existing walkthroughs instead of copying them wholesale |
| P2 | Website inclusion and recordable three-minute path are missing for this six-component case | Add one bilingual catalogue entry to the identified site on a local branch; prepare a recording package, not a fictional video |
| P2 | Personal mastery has not been evidenced | Supply independent exercises, a 14-day schedule and acceptance criteria; do not complete them for the author |
| P3 | Social-preview art, extra badges, animation or new dashboards | Not required; reuse authentic screens and simple responsibility diagrams |

## Preserve / do not change

All APIs, contracts, locks, CI definitions, existing evidence, source datasets, public main branches and milestone tags. Retain existing architecture/security learning depth. Other five component repositories are inspected, not edited. The actual personal website is related scope, but unrelated projects in its catalogue must remain byte-equivalent as data objects. The older unconfirmed Next.js candidate is not the active site and is not edited.

No live customer workshop, job eligibility, deployed site commit or independent skill level can be inferred from the files. Those remain UNKNOWN or require human evidence. See [final verification](FINAL-REPORT.md).
