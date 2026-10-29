"""Loopback-only scenario workspace using the same tested calculation as the CLI."""
import argparse
import csv
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from .business_case import business_case, prioritize

ROOT = Path(__file__).resolve().parents[1]


def calculate(values):
    allowed = {'monthly_volume', 'minutes_before', 'minutes_after', 'hourly_cost', 'adoption',
               'automation_coverage', 'monthly_run_cost', 'implementation_cost', 'rework_rate', 'rework_minutes'}
    if not isinstance(values, dict) or set(values) != allowed:
        raise ValueError('Supply the ten documented scenario assumptions')
    if any(type(value) not in (int, float) or value > 1_000_000_000 for value in values.values()):
        raise ValueError('Assumptions must be bounded numeric values')
    return business_case(**values)


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def send(self, status, body, mime='application/json'):
        encoded = body.encode() if isinstance(body, str) else json.dumps(body, allow_nan=False).encode()
        self.send_response(status)
        for key, value in {'Content-Type': mime, 'Content-Length': str(len(encoded)), 'Cache-Control': 'no-store',
                           'X-Content-Type-Options': 'nosniff', 'X-Frame-Options': 'DENY'}.items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(encoded)

    def do_GET(self):
        if self.path in ('/', '/console'):
            return self.send(200, (ROOT / 'consulting/console.html').read_text(), 'text/html; charset=utf-8')
        if self.path == '/api/scenarios':
            with (ROOT / 'data/use-cases.csv').open() as file:
                ranking = prioritize(list(csv.DictReader(file)))
            return self.send(200, {'scenarios': json.loads((ROOT / 'data/scenarios.json').read_text()), 'prioritization': ranking})
        if self.path == '/health':
            return self.send(200, {'status': 'ok', 'mode': 'hypothetical-capacity-model'})
        self.send(404, {'detail': 'Not found'})

    def do_POST(self):
        if self.path != '/api/calculate':
            return self.send(404, {'detail': 'Not found'})
        # Browser requests must be same-origin; this local calculator has no user data or write operations.
        if self.headers.get('Origin') and self.headers.get('Origin') != 'http://' + self.headers.get('Host', ''):
            return self.send(403, {'detail': 'Cross-origin requests are not accepted'})
        try:
            length = int(self.headers.get('Content-Length', '0'))
            if not 0 < length <= 8192:
                return self.send(413, {'detail': 'Scenario request must be 1..8192 bytes'})
            if self.headers.get_content_type() != 'application/json':
                return self.send(415, {'detail': 'Use application/json'})
            self.send(200, calculate(json.loads(self.rfile.read(length))))
        except (ValueError, TypeError, OverflowError):
            self.send(422, {'detail': 'Check all numeric assumptions and rates; rates must be 0..1'})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8086)
    args = parser.parse_args()
    server = ThreadingHTTPServer(('127.0.0.1', args.port), Handler)
    server.timeout = 10
    print(f'Scenario workspace: http://127.0.0.1:{args.port}', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
