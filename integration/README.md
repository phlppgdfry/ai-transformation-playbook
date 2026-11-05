# Reproduce the integrated accounting case

Clone the six public repositories as sibling directories and install each API repository using its own README and dependency lock. Keep their `.venv` environments separate. The playbook itself uses only Python's standard library.

```bash
cd ai-transformation-playbook
python3 -m integration.scenario --root ..
```

The command starts five real Uvicorn APIs on random **loopback** ports, seeds temporary databases, generates ephemeral role keys, runs 27 assertions, evaluates the actual RAG/workflow APIs, writes `reports/integration-fixture.json`, and shuts down its own processes. It never reads your `.env` files or provisions cloud resources. Environment variables may exist on the host, but provider mode is explicitly pinned to local/disabled/fixture for this run. Use Python 3.11+ and independently installed service virtualenvs.

The scenario uses explicit synthetic invoice fields, not OCR. The bounded planner is a deterministic fixture, knowledge answers are local extracts, and CRM/ERP/tasks are local mocks. Scripted reviewer identities test approval boundaries; they do not represent a real human UAT session. Four-eye checks are enforced independently by each application. Approval in one service grants no rights in another.

## Inspect the live applications

```bash
python3 -m consulting.server
python3 -m integration.scenario --root .. --serve --session-file /tmp/portfolio-session.json
```

The runner prints temporary API URLs; append `/console` for accounting, workflow, RAG and governance, or `/docs` for automation. The calculator is at `http://127.0.0.1:8086`. The optional session file has mode 0600 and contains **temporary credentials** for local QA; never commit/share it. Read it only locally. Interrupt the runner to stop its services and remove its session file/databases. Existing applications are never stopped or overwritten.

## Optional browser verification

Browser QA uses the pinned Playwright dependency and installed Chrome. Run `npm ci --ignore-scripts` in `integration/` first; this downloads no browser. It does not install a browser automatically. Set `PORTFOLIO_PLAYWRIGHT_MODULE` to an existing module path if Playwright is not resolvable normally. `PORTFOLIO_BROWSER_CHANNEL` can select another installed channel.

```bash
node integration/browser-qa.cjs /tmp/portfolio-session.json /tmp/portfolio-browser-evidence
```

This tests actual UI interactions at 1440×1000 and 390×844, saves screenshots, and records checks/expected authorization denials without credentials. Start a fresh synthetic scenario for a clean screenshot dataset. No remote browser plugin was available in the verification session, so the existing Playwright/Chrome installation was used. Cross-browser and assistive-technology verification remain open.

## Contracts and failure modes

- Accounting: `POST /invoices`, `GET /invoices/{id}`, `POST /invoices/{id}/decision`, `POST /exports/run`, `GET /invoices/{id}/audit`. Existing OpenAPI is authoritative. Submission uses `Idempotency-Key`; decisions require `expected_version`.
- Workflow: `POST /runs`, `POST /runs/{id}/drain`, `POST /runs/{id}/decision`, `POST /runs/{id}/cancel`, `GET /runs/{id}`. Plans preserve their planner mode. Tool destinations/credentials/bindings are server configuration.
- RAG: `POST /documents` (admin), `POST /ask` (server identity). Requests never select tenant/groups; finance cannot retrieve HR sources.
- Governance: `POST /policy/decide` returns advice, always `authorization_to_execute=false`; portfolio CLI adapters observe actual service contracts without invoking effects.
- Automation: propose, status, independent decision, executor. The agent connector exposes only proposal/status.

There is no shared database, distributed transaction or claim of remote exactly-once effects. Each service owns its state. A failed assertion makes the runner fail and clean up; fix/retry starts fresh. Do not adapt this temporary test harness into an unattended production orchestrator. Provider outages/retries, stale workers, cancellation, tenant denial and idempotency also have repository-level regression tests.

## Opt-in genuine local inference

The default remains model-free. To use an already installed local Qwen model, run `python3 -m integration.scenario --root .. --planner ollama --model qwen3:8b --output portfolio/integration-local-model-result.json`. This makes a real local model request; it still creates no paid cloud resources or external business effects. The local model report is separate from the default deterministic evidence.

## Preserve historical evidence

`integration.verify` now writes a unique timestamped directory under `reports/` by default. Use `--output YOUR_NEW_EVIDENCE_DIRECTORY` to select another destination. It never writes the October 29 evidence paths implicitly. The scenario defaults to `reports/integration-fixture.json` or `reports/integration-ollama.json`; use explicit new evidence paths for retained release records. Browser checks can use another calculator origin through `PORTFOLIO_PLAYBOOK_ORIGIN`.
