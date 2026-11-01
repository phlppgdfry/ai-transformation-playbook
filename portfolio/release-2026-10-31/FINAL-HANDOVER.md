> Historical publication-preparation snapshot. The authoritative completed publication report is [Completed public handover](../release-2026-11-01/FINAL-HANDOVER.md).

# Portfolio v1.0 — final publication and handover

## 1. Executive summary

**CONDITIONAL GO pending explicitly authorized publication operations.** The established private release remains intact. This pass performs disclosure review and publication preparation, not another development cycle. Runtime code, fixtures and historical evidence were preserved. Main promotion, visibility changes and milestone tags/releases have not yet been authorized in this phase.

Current reconciliation confirms six clean, synchronized release branches, unchanged `main` ancestry and successful exact-SHA hosted runs. Existing local evidence is reused because no runtime behavior changed: 172 repository tests, five clean installations, 27 deterministic integration checks, 27 genuine local-Qwen checks and 26 Chrome checks. These are executed historical results, not newly rerun claims.

## 2. Repository scorecard

| Repository | Purpose | Security assessment | Publication decision |
|---|---|---|---|
| Agentic Workflow Platform | Durable bounded tool proposals, approval and mock CRM effects | GO in reviewed scope | CONDITIONAL GO: canonical main and publication approval pending |
| Knowledge Assistant | Authorized retrieval, sources and optional Azure adapters | GO in reviewed scope | CONDITIONAL GO: same gates; live Azure quality unverified |
| Microsoft Automation | Restricted connector artifact and independent approval API | GO in reviewed scope | CONDITIONAL GO: artifact/reference wording retained |
| Evals & Governance | Versioned checks, negative controls and observable gates | GO in reviewed scope | CONDITIONAL GO: heuristic limits retained |
| Accounting Copilot | Invoice validation, independent review and mock ERP outbox | GO in reviewed scope | CONDITIONAL GO: local-reference scope retained |
| Transformation Playbook | Business case, adoption, integrated demonstration and learning | GO in reviewed scope | CONDITIONAL GO: primary entry after promotion |

Detailed scope and repository-level findings: [publication assessment](publication/publication-assessment.json).

## 3. Verification matrix

| Verification | Result / evidence |
|---|---|
| Current Git, owner, visibility, ancestry, protections, PRs, tags/releases | VERIFIED read-only: [reconciliation](publication/reconciliation.json). No remote divergence, independent main change, protection/ruleset or open PR blocks fast-forward. No prior tags/releases exist. |
| Current exact-SHA CI | VERIFIED from GitHub run records in reconciliation. See the SHA/run table below; prior [detailed hosted checks](hosted-final.json) remain preserved. |
| Repository suites | Existing 172 passed: [exact commands/results](repository-checks/verification.json). Workflow 47, RAG 25, automation 21, evals 32, accounting 38, playbook 9. |
| Independent installation | Existing five passed: per-API `evidence/release-2026-10-31/installation.json`, wheel/hash and declared dependency licence inventory. |
| Integrated demonstrations | Existing [27 deterministic](deterministic.json), [27 genuine local Qwen](local-inference.json), [26 Chrome](browser/browser-qa.json). No fixture substitution for model failures. |
| Reachable history | Current redacted Gitleaks scans: zero findings; [history content inventory](publication/history-content-inventory.json) adds metadata, email/host and accidental-file review beyond secret patterns. |
| Retained Actions artifacts | All 16 downloaded and inspected without executing contents: [artifact review](publication/workflow-artifact-review.json). Two scanner findings are verified manifest SHA-256 checksums, not credentials: [triage](publication/artifact-finding-triage.json). |
| Completed-run logs | All 18 retained completed-run archives downloaded/scanned: [log review](publication/workflow-log-review.json). Two matching checksum findings independently resolved: [triage](publication/log-finding-triage.json). |
| Screenshots | 30 tracked images screened with installed local OCR, plus selected visual inspection: [review](publication/screenshot-review.json). No detected visible email, home path or credential candidate; OCR is not exhaustive proof. |
| Documentation and assets | Existing local Markdown targets resolve: [review](publication/documentation-review.json). Main links prepared for the pending promotion; anonymous HTTP/rendering tests await actual public visibility. |
| Local docs preparation | No runtime/package version change. Focused stack summaries, six release-note files and central navigation prepared; final local diff/link/secret checks precede any requested push. |
| Cloud / paid inference / deployment | NOT EXECUTED. Azure inference/OCR/search quality and full Copilot Studio runtime remain unverified. |
| Anonymous public visitor | NOT VERIFIED yet: repositories are still private; owner-authenticated access is not anonymous proof. |

The latest verified baseline commits are:

| Repository | Release SHA | Successful hosted run |
|---|---|---|
| Workflow | `54e263f4ec834592ec294a9c7a21a85a9c87d8aa` | [verified run](https://github.com/phlppgdfry/agentic-workflow-platform/actions/runs/41144511697) |
| RAG | `23be5180b667786632fd1d7ddf598d5d491cc5bc` | [verified run](https://github.com/phlppgdfry/azure-ai-rag-knowledge-assistant/actions/runs/41144511648) |
| Automation | `f703d7b4a8a2eca222c3798f905838b5ab6b742b` | [verified run](https://github.com/phlppgdfry/microsoft-copilot-studio-automation/actions/runs/41144511400) |
| Evals | `8f4b5425bd0a80c71b690e764663b3a612108599` | [verified run](https://github.com/phlppgdfry/enterprise-ai-evals-governance/actions/runs/41144511499) |
| Accounting | `15aa403f5478dff3ef888deaeb3e88c996e9bb08` | [verified run](https://github.com/phlppgdfry/enterprise-ai-accounting-copilot/actions/runs/41144511426) |
| Playbook | `2beb0cbbfdbffa124c6705e90ce83f35cfe2e72b` | [verified run](https://github.com/phlppgdfry/ai-transformation-playbook/actions/runs/41144751249) |

Prepared publication documentation commits follow this verified baseline. Their own CI and any promoted main checks must pass before public release; no result for an unexecuted future commit is inferred.

## 4. GitHub status and exact promotion plan

Owner: `phlppgdfry`. All six remain private. Default branch: `main`. Current release branch: `portfolio/enterprise-quality-2026-10-29`. Main is respectively seven, six, six, six, six and seven commits behind the verified baseline; zero ahead. API evidence reports `protected=false`, protection endpoint `404 Branch not protected`, empty rulesets and no open PRs. No existing tag will be overwritten.

Recommended promotion is a normal fast-forward, preserving the tested commit history. A merge commit, squash, rebase or PR adds no required protection here. If main changes, stop and review the difference rather than forcing or blindly merging.

Consolidated plan for all six exact `https://github.com/phlppgdfry/<repository>.git` destinations:

1. After approval, push the prepared documentation/release-note commits to the existing release branches using normal pushes. Wait for exact-SHA hosted checks.
2. Fetch again, confirm each main SHA still matches reconciliation and remains an ancestor. Promote only the audited release SHA with a normal `git push origin <approved-sha>:refs/heads/main`; never force. Default branch remains `main`.
3. Verify remote main equals the approved SHA, monitor its on-push checks and preserve the release branches. No PR, branch deletion or protection change is proposed.
4. Make no visibility change during promotion. Visibility is a separate approved operation after green main checks.

Final evidence/status documentation updates on these same branches must be included in the approval scope. No runtime feature, cloud resource or external repository is included.

## 5. Security assessment

**GO for the reviewed source/history/artifact scope.** No confirmed credential, real customer record, sensitive customer financial data or unexpected local database/configuration was found. Existing application controls remain backed by the preserved regression tests. This is a disclosure assessment, not proof of universal security or legal compliance.

Disclosure classifications:

- **Potential personal metadata concern, resolved by explicit consent:** all Git histories contain the owner's personal author email; evidence contains Mac home paths and temporary tool paths. The user explicitly selected “Allow existing author email and home-path metadata.” No history rewrite or additional publication of the address is needed. This consent does not authorize visibility changes.
- **Benign development/public metadata:** Python versions, local machine hostname, public GitHub owner/IDs, runner paths, reserved example hosts, synthetic email canaries and isolated connector identifiers. No active environment URL or credential is supplied by the Microsoft solution.
- **Previously resolved scanner findings:** `generic-api-key` matched `apiProperties.json` manifest digest values in two artifacts and their logs. Each value exactly equals the archived file's SHA-256. Raw finding counts are retained; no broad detector suppression was introduced.
- **Confirmed critical disclosure defects:** none found in the reviewed scope. Any new sensitive finding blocks that repository's visibility change until resolved; published history must never be rewritten automatically.

Six source licences remain MIT. Wheels retain explicit MIT metadata/LICENSE; dependency licences are inventoried, not relicensed. Screenshots depict authored applications and synthetic data. No model weights, stock artwork, customer dataset or Microsoft platform binary is vendored. An actual connector solution is redistributed as the project's own configuration artifact, with no connection values. Model/service terms remain the operator's responsibility. Licence metadata review is not a legal opinion.

Actions retain immutable action refs, read-only contents permissions and no persisted checkout credential. The private optional cross-repository workflow uses an explicitly configured read token only on manual dispatch; it is not a PR-secret path and was not newly configured or executed. No CI/cloud costs beyond separately approved Actions usage are proposed.

## 6. Showcase assessment

DONE: each README has a business problem, concrete behavior, installation/demo, security, limits and cross-repository navigation. The final preparation adds a short visible stack line and scoped release-note link. Descriptions and topics are already professional and accurate; no unnecessary remote metadata change is proposed. Existing diagrams separate local effects, actual HTTP integrations, optional Azure adapters and unverified Microsoft runtime.

DONE: [SHOWCASE.md](../SHOWCASE.md) is the entry point, with business case → architecture → demo → components → evidence → limitations. Fictional organizations, synthetic records, model versus fixture modes and hypothetical benefits are labelled. Existing genuine screenshots are reused; no mock UI or decorative preview was created. Additional badges/social art are optional, not release gates.

The [handover](HANDOVER.md) already supplies the five target-role perspectives, 30-second introduction, two-minute explanation, five-minute demo, fifteen-minute walkthrough and interview questions. Existing clean-install evidence remains sufficient because only documentation changes were prepared.

## 7. Business value

The case connects process discovery and acceptance criteria to executable invoice validation, scoped policy retrieval, controlled tool proposals, independent human decisions, local mock export, audit and evaluation. The playbook adds prioritization, adoption and a measured-pilot approach. The services retain independent ownership; governance/model text never grants authorization. This demonstrates inspectable consulting and engineering decisions, not delivered client impact. Released capacity is not automatically cash savings.

## 8. Known limitations and v1.0 scope

Azure inference/OCR/hybrid quality and full Copilot Studio/Power Automate runtime are not verified. Historical Microsoft import/export/reimport proves artifact acceptance, not agent execution. API keys, SQLite and local mock sinks are reference choices, not enterprise identity/HA or external exactly-once delivery. Citation IDs and deterministic heuristic gates do not establish semantic truth or universal injection resistance.

The proposed consistent tag is **`portfolio-v1.0.0`**, title **“Portfolio v1.0.0 — synthetic reference release.”** It identifies the stable portfolio milestone, not a production or package/API 1.0 promise. The five Python distributions/API versions deliberately remain `0.1.0`; the playbook has no published package. No package publication or version-only runtime change is needed.

Each repository has prepared [release notes](../../docs/releases/portfolio-v1.0.0.md), with capabilities, independent setup, verification and limits. After separate approval: verify the tag does not exist; annotate it at the approved green-main SHA; push that explicit tag; publish a GitHub release using `--verify-tag` and the prepared `--notes-file`. Do not auto-create tags from an implicit default target. No assets, discussions, package registry or deployment are required. Post-release handover updates may follow as documentation-only commits without moving the frozen implementation tag.

## 9. Remaining tasks

| Class | Task |
|---|---|
| BLOCKER: authorization | Approve six release-branch documentation pushes and fast-forward main promotions, including Actions checks and final status-only follow-ups. |
| BLOCKER: canonical validation | Execute approved promotions and inspect exact main-SHA checks; stop on divergence or failures. |
| BLOCKER: publication authorization | Separately approve all six visibility changes, after the documented disclosure review and main gate. |
| BLOCKER: v1.0 release authorization | Approve six annotated `portfolio-v1.0.0` tags and six published demo-scoped GitHub releases. |
| BLOCKER: public acceptance | Verify anonymous repository/main/README/image/diagram/navigation/licence/CI/release access after actual publication; do not use owner permissions as proof. |
| OPTIONAL | Extra social art/badges, broader browsers/accessibility, pip distribution hashes and a deck export. No new features required. |
| FUTURE LEARNING | Personally complete the existing debugging, business discovery, adoption and operational exercises. Cloud/real sink work requires separate environment/cost approval. |

## 10. Personal learning roadmap

Use [LEARNING.md](../release-2026-10-30/LEARNING.md), with source files, five concepts and three exercises per repository. Before claiming competence, independently demonstrate: exact amounts/duplicates and stale approval; workflow scope/retries/lease fencing; RAG permissions and metric limits; evaluation negative controls/baseline fingerprints; narrow connector versus active runtime; and assumptions/adoption versus observed benefits.

Run the integrated scenario yourself and diagnose a denied action without weakening permissions. Explain one failure and fix a small regression without generated assistance. Microsoft study topics are already mapped in that guide. Program behavior is supported by evidence; personal understanding, client delivery experience and workshop competence remain **NOT ASSESSED**.

## 11. Final release decision

**CONDITIONAL GO.** Engineering and public-disclosure preparation are complete within the reference scope; canonical promotion, public acceptance and milestone publication await exact authorizations and execution. No production/cloud claim is added.

## 12. Completion statement

v1.0 cannot yet be declared publicly complete. The safe local preparation is finished. Complete only the approved promotion, visibility, release and verification operations, retain their evidence, ensure clean synchronized worktrees and stop. No seventh repository, history rewrite, infrastructure deployment or new enhancement cycle is authorized or needed.
