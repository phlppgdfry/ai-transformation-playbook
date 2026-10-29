# Interface verification — final implementation

Five implemented interfaces were exercised with installed Chrome through Playwright, at 1440×1000 and 390×844. The Browser plugin was not available. No browser dependency was installed; an unconfigured shared-tool shim was bypassed with the already installed Node executable. Exact repeatable test: `integration/browser-qa.cjs`. Results: [browser-qa.json](browser-qa.json).

| Check | Result | Evidence |
|---|---|---|
| Page identity | PASS | Titles verified for accounting, workflow, consulting, knowledge and evaluation |
| Meaningful rendered content | PASS | Actual invoices, workflow receipts, assumptions, retrieved sources and executed evaluation rows |
| Framework overlay | PASS | Native server-rendered HTML/JS pages; inspected screenshots show no runtime overlay |
| Console health | PASS | No unexpected console or page errors; deliberate 403 authorization denials recorded separately |
| Desktop/mobile layout | PASS | No page overflow at either tested width; screenshots inspected |
| Real interaction flow | PASS | 26 checks against actual local APIs; no browser response mocks |
| Screenshots | PASS | Actual rendered pages, stored per repository in `evidence/screenshots/` |

Flows exercised:

- Accounting: connect operator → import explicit synthetic JSON source → submit → deny operator approval → switch to reviewer → open current invoice → approve → load audit → switch exporter → execute mock export → clear sensitive page state.
- Workflow: create → advance real invoice/policy tools → inspect receipts → deny self-approval → switch independent reviewer → approve → switch operator → complete local case. The source and selected details clear on identity changes.
- Consulting: base assumptions → zero adoption → no positive payback → restore base → download evidence → responsive layout. Sensitivity figures use actual calculator API results.
- Knowledge: finance search → inspect actual policy/source chunk → search hidden HR canary → abstain with no source disclosure.
- Evaluation: load saved runs → execute positive control → pass → execute negative control → block, with 16 actual case rows.

Failures during QA were corrected rather than counted as passing: repeated synthetic IDs, stale detail/reason fields during role switching, and an incorrect test assumption that the evaluation store would always be empty. Final browser checks use distinct synthetic invoice IDs, synchronized role changes and persisted-state-compatible assertions.

The separate genuine local-model integration uses actual Qwen inference; interface screenshots intentionally show their actual fixture/control execution labels. No screenshot is represented as Azure/Copilot runtime evidence. Remaining verification: other browsers, screen-reader navigation, automated accessibility auditing, high-volume data and load/concurrency budgets.

Screenshot gallery is available through the six repository READMEs and evidence folders. The final report links these artifacts rather than presenting designed mockups as implemented UI.
