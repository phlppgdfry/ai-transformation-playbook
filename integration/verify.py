"""Repeat the final repository-level checks and preserve exact local evidence."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

from .scenario import REPOS


def main():
    root = Path(__file__).resolve().parents[2]
    all_results = []
    with tempfile.TemporaryDirectory() as folder:
        for service, name in {**REPOS, 'playbook': 'ai-transformation-playbook'}.items():
            repo = root / name
            python = str(repo / '.venv/bin/python') if service != 'playbook' else sys.executable
            commands = [[python, '--version'], [python, '-m', 'unittest', 'discover', '-s', 'tests', '-v']] if service == 'playbook' else [
                [python, '--version'], [python, '-m', 'pytest', '-q', '--junitxml=evidence/tests-2026-10-29.xml'],
                [python, '-m', 'pip', 'check'], [python, 'scripts/export_openapi.py', '--check']]
            if service == 'accounting':
                commands += [[str(repo / '.venv/bin/ruff'), 'check', 'src', 'tests'], [python, '-m', 'accounting_copilot.demo']]
            elif service == 'workflow':
                commands += [[python, '-m', 'workflow_platform.cli']]
            elif service == 'rag':
                commands += [[python, '-m', 'rag.demo'], [python, '-m', 'rag.evaluate']]
            elif service == 'automation':
                commands += [[python, 'scripts/export_connector.py', '--check'], [python, '-m', 'automation.demo'],
                             [python, 'scripts/package_connector.py', '--origin', 'https://synthetic.example.com', '--out', folder + '/connector']]
            elif service == 'governance':
                commands += [[python, '-m', 'evalgov.cli', '--fixture', 'good', '--out', folder + '/good', '--db', folder + '/eval.db'],
                             [python, '-m', 'evalgov.cli', '--fixture', 'unsafe', '--baseline', folder + '/good/report.json',
                              '--out', folder + '/unsafe', '--db', folder + '/eval.db']]
            else:
                commands += [[python, '-m', 'consulting.business_case', '--output', folder + '/business-case.json']]
            results = []
            for command in commands:
                result = subprocess.run(command, cwd=repo, capture_output=True, text=True, timeout=90)
                expected = 1 if service == 'governance' and 'unsafe' in command else 0
                results.append({'command': command, 'exit_code': result.returncode, 'expected_exit': expected,
                                'passed': result.returncode == expected, 'stdout': result.stdout, 'stderr': result.stderr})
            if service == 'playbook':
                actual = json.loads(Path(folder + '/business-case.json').read_text())
                saved = json.loads((repo / 'evidence/business-case.json').read_text())
                results.append({'command': ['compare', 'business-case.json'], 'passed': actual == saved})
            data = {'executed_at': datetime.now(timezone.utc).isoformat(), 'repository': name, 'checks': results}
            (repo / 'evidence/verification-2026-10-29.json').write_text(json.dumps(data, indent=2) + '\n')
            all_results.append(data)
            print(name + ': ' + ('PASS' if all(r['passed'] for r in results) else 'FAIL'), flush=True)
        destination = root / 'ai-transformation-playbook/portfolio/verification.json'
        destination.write_text(json.dumps(all_results, indent=2) + '\n')
    return 0 if all(r['passed'] for repo in all_results for r in repo['checks']) else 1


if __name__ == '__main__':
    raise SystemExit(main())
