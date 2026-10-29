"""Real local HTTP integration. Synthetic data, fixture planner, mock sinks; no cloud.

Run from this repository: python3 -m integration.scenario --root ..
Each service uses its own installed .venv. No shared runtime database or dependencies.
"""
import argparse
import contextlib
import json
import os
from pathlib import Path
import secrets
import socket
import subprocess
import tempfile
import time
import urllib.error
import urllib.request

from consulting.business_case import business_case

REPOS = {'accounting': 'enterprise-ai-accounting-copilot', 'workflow': 'agentic-workflow-platform',
         'rag': 'azure-ai-rag-knowledge-assistant', 'governance': 'enterprise-ai-evals-governance',
         'automation': 'microsoft-copilot-studio-automation'}


def check(condition, message):
    if not condition:
        raise RuntimeError(message)


class Scenario:
    def __init__(self, root, folder, planner='fixture', model=None):
        self.root, self.folder = Path(root).resolve(), Path(folder)
        self.planner, self.model = planner, model
        self.processes, self.logs, self.urls, self.keys, self.envs = [], [], {}, {}, {}
        self.checks = []

    def verify(self, condition, label):
        check(condition, label)
        self.checks.append({'check': label, 'passed': True})

    def start(self, service, target, env):
        repo = self.root / REPOS[service]
        python = repo / '.venv/bin/python'
        check(python.exists(), f'Missing {python}; install this repository independently first')
        with socket.socket() as sock:
            sock.bind(('127.0.0.1', 0))
            port = sock.getsockname()[1]
        self.urls[service] = f'http://127.0.0.1:{port}'
        # Inherit host tool paths, but explicitly pin demo provider modes and database locations.
        actual_env = {**os.environ, **env}
        self.envs[service] = actual_env
        log = (self.folder / (service + '.log')).open('w')
        self.logs.append(log)
        process = subprocess.Popen([str(python), '-m', 'uvicorn', target,
            *(['--factory'] if service in {'workflow', 'governance'} else []), '--host', '127.0.0.1',
            '--port', str(port), '--no-access-log'], cwd=repo, env=actual_env, stdout=log, stderr=log)
        self.processes.append(process)
        deadline = time.monotonic() + 20
        while time.monotonic() < deadline:
            check(process.poll() is None, f'{service} exited; inspect {log.name}')
            try:
                if self.call(service, '/health')[0] == 200:
                    return
            except OSError:
                pass
            time.sleep(.1)
        raise RuntimeError(f'{service} health deadline exceeded')

    def call(self, service, path, role=None, body=None, method=None, headers=None):
        headers = headers or {}
        if role:
            headers = {**headers, 'X-API-Key': self.keys[service][role]}
        data = json.dumps(body).encode() if body is not None else None
        request = urllib.request.Request(self.urls[service] + path, data=data,
            headers={**headers, 'Content-Type': 'application/json'}, method=method or ('POST' if data else 'GET'))
        try:
            with urllib.request.urlopen(request, timeout=120 if self.planner == 'ollama' and path.endswith('/drain') else 15) as response:
                return response.status, json.load(response)
        except urllib.error.HTTPError as response:
            return response.code, json.load(response)

    def credentials(self, service, roles):
        self.keys[service] = {role: secrets.token_urlsafe(32) for role in roles}
        return self.keys[service]

    def run(self):
        keys = self.credentials('accounting', ['operator', 'reviewer', 'exporter', 'auditor', 'other'])
        mapping = {key: {'actor': role, 'tenant': 'other' if role == 'other' else 'demo',
                         'role': 'reviewer' if role == 'other' else role} for role, key in keys.items()}
        db = str(self.folder / 'accounting.db')
        seed = subprocess.run([str(self.root / REPOS['accounting'] / '.venv/bin/python'), '-c',
            'import os; from accounting_copilot.store import Store; Store(os.environ["ACCOUNTING_DB"]).seed()'],
            env={**os.environ, 'ACCOUNTING_DB': db}, capture_output=True, text=True)
        check(seed.returncode == 0, 'Accounting synthetic seed failed')
        self.start('accounting', 'accounting_copilot.api:app', {'ACCOUNTING_DB': db,
            'ACCOUNTING_API_KEYS': json.dumps(mapping), 'ACCOUNTING_AI_MODE': 'disabled'})
        invoice = {'supplier_id': 'synthetic-office', 'invoice_number': 'SYN-INTEGRATION-001',
            'invoice_date': '2026-01-01', 'currency': 'EUR', 'net': '100.00', 'vat': '21.00',
            'total': '121.00', 'description': 'Synthetic office supplies; source fields entered explicitly, no OCR claim'}
        status, created = self.call('accounting', '/invoices', 'operator', invoice,
                                    headers={'Idempotency-Key': 'portfolio-invoice-v1'})
        self.verify(status == 201 and created['status'] == 'pending_review', 'invoice validated and queued')
        invoice_id = created['id']
        self.verify(self.call('accounting', '/invoices', 'operator', invoice,
            headers={'Idempotency-Key': 'portfolio-invoice-v1'})[1]['id'] == invoice_id, 'submission retry reuses invoice')
        self.verify(self.call('accounting', '/invoices/' + invoice_id, 'other')[0] == 404, 'cross-tenant invoice denied')

        keys = self.credentials('rag', ['admin', 'finance', 'hr', 'other'])
        mapping = {key: {'subject': role, 'tenant': 'other' if role == 'other' else 'demo',
            'groups': ['hr'] if role == 'hr' else ['finance'], 'admin': role == 'admin'} for role, key in keys.items()}
        self.start('rag', 'rag.api:app', {'RAG_DB': str(self.folder / 'rag.db'),
                   'RAG_PRINCIPALS': json.dumps(mapping), 'RAG_PROVIDER': 'local'})
        for doc in json.loads((self.root / REPOS['rag'] / 'fixtures/documents.json').read_text()):
            self.verify(self.call('rag', '/documents', 'admin', doc)[0] == 201, 'ingested ' + doc['id'])
        self.verify(self.call('rag', '/ask', 'finance', {'question': '7312'})[1]['abstained'], 'finance cannot retrieve HR canary')
        self.verify(self.call('rag', '/ask', 'other', {'question': 'factuur'})[1]['abstained'], 'cross-tenant knowledge denied')

        keys = self.credentials('workflow', ['builder', 'reviewer', 'other'])
        mapping = {key: {'subject': role, 'tenant': 'other' if role == 'other' else 'demo',
            'roles': ['approver'] if role == 'reviewer' else ['builder', 'operator', 'approver']}
            for role, key in keys.items()}
        binding = {'demo': {'C-001': {'invoice_id': invoice_id, 'accounting_key': self.keys['accounting']['auditor'],
                                    'rag_key': self.keys['rag']['finance']}}}
        self.start('workflow', 'workflow_platform.api:create_app', {
            'WORKFLOW_DB': str(self.folder / 'workflow.db'), 'WORKFLOW_PRINCIPALS_JSON': json.dumps(mapping),
            'PLANNER_MODE': self.planner, 'OLLAMA_MODEL': self.model or '',
            'OLLAMA_ORIGIN': 'http://127.0.0.1:11434', 'WORKFLOW_TOOLS_MODE': 'portfolio',
            'ACCOUNTING_API_ORIGIN': self.urls['accounting'], 'RAG_API_ORIGIN': self.urls['rag'],
            'WORKFLOW_CUSTOMER_BINDINGS': json.dumps(binding)})
        _, response = self.call('workflow', '/runs', 'builder', {'customer_id': 'C-001',
            'message': 'Prepare independent review of the synthetic invoice.'}, headers={'Idempotency-Key': 'portfolio-workflow-v1'})
        run_id = response['run']['id']
        _, state = self.call('workflow', f'/runs/{run_id}/drain', 'builder', method='POST')
        self.verify(state['status'] == 'waiting_approval' and state['crm_case_id'] is None, 'workflow waits before effect')
        self.verify(state['tool_results'][0]['result']['source'] == 'accounting_api', 'workflow read invoice over HTTP')
        self.verify(state['tool_results'][1]['result']['source'] == 'rag_api', 'workflow retrieved authorized policy over HTTP')
        decision = {'approve': True, 'reason': 'Independent reviewer checked synthetic evidence'}
        self.verify(self.call('workflow', f'/runs/{run_id}/decision', 'builder', decision)[0] == 403, 'workflow self approval denied')
        self.verify(self.call('workflow', f'/runs/{run_id}', 'other')[0] == 404, 'cross-tenant workflow denied')

        keys = self.credentials('governance', ['governor'])
        self.start('governance', 'evalgov.api:create_app', {'EVALGOV_DB': str(self.folder / 'governance.db'),
            'EVALGOV_PRINCIPALS': json.dumps({keys['governor']: {'name': 'synthetic-governor', 'role': 'governor'}})})
        _, advice = self.call('governance', '/policy/decide', 'governor', {'use_case': 'Synthetic invoice review',
            'personal_data': False, 'externally_visible_action': True, 'financial_posting': True,
            'approved_data_source': True, 'retention_days': 30, 'owner': 'Demo process owner'})
        self.verify(advice['human_approval_required'] and not advice['authorization_to_execute'], 'governance advice grants no execution authority')

        keys = self.credentials('automation', ['agent', 'reviewer', 'executor'])
        self.start('automation', 'automation.api:app', {'AUTOMATION_DB': str(self.folder / 'automation.db'),
            'AUTOMATION_PRINCIPALS': json.dumps({key: {'subject': role, 'tenant': 'demo', 'role': role}
                                               for role, key in keys.items()})})
        _, task = self.call('automation', '/requests', 'agent', {'idempotency_key': 'portfolio-approval-v1',
            'dossier': 'SYN-INTEGRATION-001', 'action': 'schedule_review',
            'description': 'Schedule human review for synthetic invoice ' + invoice_id})
        task_id = task['id']
        self.verify(self.call('automation', f'/requests/{task_id}/execute', 'executor', method='POST')[0] == 409,
                    'automation cannot execute before human approval')
        self.verify(self.call('automation', f'/requests/{task_id}/decision', 'agent',
            {'approved': True, 'reason': 'Agent attempts escalation'})[0] == 403, 'agent connector identity cannot approve')
        self.call('automation', f'/requests/{task_id}/decision', 'reviewer',
                  {'approved': True, 'reason': 'Human accepted synthetic scheduling task'})
        self.verify(self.call('automation', f'/requests/{task_id}/execute', 'executor', method='POST')[1]['state'] == 'completed',
                    'approved local scheduling task executed')

        self.verify(self.call('workflow', f'/runs/{run_id}/decision', 'reviewer', decision)[0] == 200, 'workflow independently approved')
        self.verify(self.call('workflow', f'/runs/{run_id}/drain', 'builder', method='POST')[1]['status'] == 'completed', 'workflow completed local mock case')
        self.verify(self.call('accounting', '/exports/run', 'exporter', method='POST')[1]['exported'] == [],
                    'workflow and automation approval do not grant invoice approval')
        self.verify(self.call('accounting', f'/invoices/{invoice_id}/decision', 'operator',
            {**decision, 'expected_version': 1})[0] == 403, 'operator cannot approve invoice')
        self.verify(self.call('accounting', f'/invoices/{invoice_id}/decision', 'reviewer',
            {**decision, 'expected_version': 1})[1]['status'] == 'approved', 'accounting reviewer explicitly approved invoice')
        self.verify(self.call('accounting', '/exports/run', 'exporter', method='POST')[1]['exported'] == [invoice_id], 'approved invoice exported to mock ERP')
        self.verify(self.call('accounting', '/exports/run', 'exporter', method='POST')[1]['exported'] == [], 'repeated export produces no duplicate')
        audit = self.call('accounting', f'/invoices/{invoice_id}/audit', 'auditor')[1]
        self.verify([a['action'] for a in audit] == ['invoice.submitted', 'invoice.approved', 'export.mock_sent'], 'audit records complete invoice lifecycle')

        evaluations = []
        for service, dataset in [('rag', self.root / REPOS['governance'] / 'evalgov/datasets/portfolio-rag-v1.jsonl'),
                                 ('workflow', self.folder / 'workflow-cases.jsonl')]:
            if service == 'workflow':
                calls = [{'name': s['tool'], 'arguments': s['arguments']} for s in state['plan']['steps']]
                dataset.write_text(json.dumps({'id': 'completed-run', 'category': 'tools', 'prompt': run_id,
                    'expected': {'answer_terms': ['completed'], 'allowed_calls': calls, 'required_calls': calls}}) + '\n' +
                    json.dumps({'id': 'missing-run', 'category': 'access', 'prompt': 'unknown-run', 'expected': {'refused': True}}) + '\n')
            output = self.folder / ('eval-' + service)
            command = [str(self.root / REPOS['governance'] / '.venv/bin/python'), '-m', 'evalgov.cli',
                       '--portfolio', service, '--dataset', str(dataset), '--out', str(output),
                       '--db', str(self.folder / 'evaluations.db')]
            result = subprocess.run(command, cwd=self.root / REPOS['governance'], capture_output=True, text=True,
                env={**os.environ, 'EVALGOV_PORTFOLIO_ORIGIN': self.urls[service],
                     'EVALGOV_TARGET_TOKEN': self.keys[service]['finance' if service == 'rag' else 'builder']}, timeout=30)
            self.verify(result.returncode == 0, service + ' evaluation passes against actual API')
            evaluations.append(json.loads((output / 'report.json').read_text()))
        scenarios = json.loads((Path(__file__).resolve().parents[1] / 'data/scenarios.json').read_text())
        return {'schema_version': 1, 'execution': 'actual loopback HTTP; synthetic data; ' + self.planner + ' planner; local mock sinks',
            'cloud_verified': False, 'human_approval': 'separate synthetic reviewer credentials used by scripted test, not a real person',
            'checks': self.checks, 'invoice_id': invoice_id, 'workflow_id': run_id, 'automation_id': task_id,
            'workflow_proposal': state, 'workflow_events': self.call('workflow', f'/runs/{run_id}/events', 'builder')[1],
            'policy_advice': advice, 'audit': audit, 'evaluations': evaluations,
            'business_case': business_case(**scenarios['base'])}

    def close(self):
        for process in reversed(self.processes):
            process.terminate()
        for process in self.processes:
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
        for log in self.logs:
            log.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--output', type=Path, default=Path('portfolio/integration-result.json'))
    parser.add_argument('--serve', action='store_true', help='Keep the seeded demo APIs running until interrupted')
    parser.add_argument('--planner', choices=['fixture', 'ollama'], default='fixture', help='Local inference is explicit and optional')
    parser.add_argument('--model', help='Already installed local model name, required with --planner ollama')
    parser.add_argument('--session-file', type=Path, help='Optional private temporary browser-QA session; contains ephemeral credentials')
    args = parser.parse_args()
    if args.planner == 'ollama' and not args.model:
        parser.error('--model is required for opt-in genuine local inference')
    with tempfile.TemporaryDirectory(prefix='ai-portfolio-') as folder:
        scenario = Scenario(args.root, folder, args.planner, args.model)
        session_created = False
        try:
            result = scenario.run()
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(result, indent=2) + '\n')
            print(json.dumps({'passed': len(result['checks']), 'report': str(args.output), 'urls': scenario.urls}), flush=True)
            if args.session_file:
                check(any(args.session_file.resolve().is_relative_to(root.resolve()) for root in
                          (Path(tempfile.gettempdir()), Path('/tmp'))), 'Session file must be outside repositories in temporary storage')
                descriptor = os.open(args.session_file, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
                session_created = True
                with os.fdopen(descriptor, 'w') as file:
                    json.dump({'urls': scenario.urls, 'keys': scenario.keys}, file)
            if args.serve:
                while True:
                    time.sleep(1)
        except KeyboardInterrupt:
            pass
        finally:
            scenario.close()
            if session_created:
                with contextlib.suppress(FileNotFoundError):
                    args.session_file.unlink()


if __name__ == '__main__':
    main()
