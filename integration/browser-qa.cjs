/* Optional browser QA. Reuse an installed Playwright module; no browser install or cloud calls.
   Run after integration.scenario --serve --session-file /tmp/portfolio-session.json.
   PORTFOLIO_PLAYWRIGHT_MODULE can point at the host's existing Playwright installation. */
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const { chromium } = require(process.env.PORTFOLIO_PLAYWRIGHT_MODULE || 'playwright');

(async () => {
  const session = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const output = path.resolve(process.argv[3] || '/tmp/portfolio-browser-evidence');
  fs.mkdirSync(output, { recursive: true });
  const browser = await chromium.launch({ headless: true, channel: process.env.PORTFOLIO_BROWSER_CHANNEL || 'chrome' });
  const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
  page.setDefaultTimeout(12000);
  const errors = [], expectedDenials = [], checks = [], screenshots = [];
  page.on('pageerror', error => errors.push(error.message));
  page.on('console', message => {
    if (message.type() !== 'error') return;
    if (message.text().includes('status of 403')) expectedDenials.push(message.text());
    else errors.push(message.text());
  });
  const check = (label, condition) => { assert(condition, label); checks.push({ check: label, passed: true }); };
  async function capture(name) {
    const file = path.join(output, name + '.png');
    await page.screenshot({ path: file, fullPage: true });
    screenshots.push(file);
  }
  async function responsive(name) {
    await page.setViewportSize({ width: 390, height: 844 });
    check(name + ' has no mobile page overflow', !(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth)));
    await capture(name + '-mobile');
    await page.setViewportSize({ width: 1440, height: 1000 });
  }
  try {
    await page.goto('http://127.0.0.1:8086');
    await page.getByText('6.03 months', { exact: true }).waitFor();
    check('playbook page identity', await page.title() === 'AI Transformation Studio');
    await capture('playbook-desktop');
    await page.getByRole('spinbutton', { name: 'Adoption rate', exact: true }).fill('0');
    await page.getByRole('button', { name: 'Recalculate scenario' }).click();
    await page.getByText('No positive payback', { exact: true }).waitFor();
    check('zero adoption has no positive payback', await page.locator('#hours').textContent() === '0 h');
    await page.getByRole('button', { name: 'Base case', exact: true }).click();
    await page.getByText('6.03 months', { exact: true }).waitFor();
    const download = page.waitForEvent('download');
    await page.getByRole('button', { name: 'Download evidence JSON' }).click();
    check('scenario evidence download', (await download).suggestedFilename() === 'hypothetical-capacity-scenario.json');
    await responsive('playbook');

    await page.goto(session.urls.accounting + '/console');
    check('accounting page identity', (await page.title()).includes('Factuurwerkbank'));
    async function accountingRole(role) {
      await page.locator('#key').fill(session.keys.accounting[role]);
      await page.getByRole('button', { name: 'Verbinden en laden' }).click();
      await page.getByText('Werkvoorraad geladen. Acties worden door jouw serverrol gecontroleerd.', { exact: true }).waitFor();
    }
    await accountingRole('operator');
    const invoice = { supplier_id: 'synthetic-office', invoice_number: 'SYN-BROWSER-' + Date.now(), invoice_date: '2026-01-01',
      currency: 'EUR', net: '200.00', vat: '42.00', total: '242.00', description: 'Synthetic browser verification supplies' };
    await page.locator('#source-file').setInputFiles({ name: 'synthetic-invoice.json', mimeType: 'application/json',
      buffer: Buffer.from(JSON.stringify(invoice)) });
    await page.getByText('Bron geladen. Controleer het voorstel en dien het afzonderlijk in.', { exact: true }).waitFor();
    check('JSON source import preserves explicit fields without AI claim', JSON.parse(await page.locator('#invoice').inputValue()).total === '242.00');
    await page.getByText('Synthetische factuur indienen', { exact: true }).click();
    await page.getByRole('button', { name: 'Indienen voor controle' }).click();
    await page.getByText('Synthetische factuur opgeslagen. Wissel naar de reviewerrol voor een beslissing.', { exact: true }).waitFor();
    await page.locator('#reason').fill('Independent source verification in browser QA');
    await page.getByRole('button', { name: 'Goedkeuren', exact: true }).click();
    await page.getByText('Deze rol mag deze actie niet uitvoeren. Wissel naar de bevoegde rol.', { exact: true }).waitFor();
    check('accounting browser cannot approve as operator', true);
    await accountingRole('reviewer');
    await page.getByRole('button', { name: 'Open ' + invoice.invoice_number, exact: true }).click();
    await page.locator('#reason').fill('Independent source verification in browser QA');
    await page.getByRole('button', { name: 'Goedkeuren', exact: true }).click();
    await page.getByText('Factuur goedgekeurd en in exportwachtrij geplaatst.', { exact: true }).waitFor();
    check('accounting reviewer approval updates real state', await page.locator('#detail-status').textContent() === 'Goedgekeurd');
    await page.getByRole('button', { name: 'Audittrail laden', exact: true }).click();
    await page.locator('#detail pre').filter({ hasText: 'invoice.approved' }).waitFor();
    await capture('accounting-desktop');
    await responsive('accounting');
    await accountingRole('exporter');
    await page.getByRole('button', { name: 'Goedgekeurde facturen overdragen' }).click();
    await page.getByText('1 facturen overgedragen aan lokale mock-ERP.', { exact: true }).waitFor();
    check('accounting UI delivers approved invoice to local mock', true);
    await page.getByRole('button', { name: 'Verbinding wissen' }).click();
    check('accounting clears source and invoice data on disconnect', (await page.locator('#source-preview').textContent()) === '');

    await page.goto(session.urls.workflow + '/console');
    check('workflow page identity', await page.title() === 'Workflow Control');
    async function workflowRole(role) {
      await page.locator('#key').fill(session.keys.workflow[role]);
      const loaded = page.waitForResponse(response => response.url() === session.urls.workflow + '/runs' && response.request().method() === 'GET');
      await page.getByRole('button', { name: 'Connect', exact: true }).click();
      await loaded;
      await page.waitForFunction(() => document.getElementById('message').textContent.includes('workflows loaded.'));
      await page.locator('#runs button').first().waitFor();
    }
    await workflowRole('builder');
    await page.getByText('Prepare a new workflow', { exact: true }).click();
    await page.getByRole('button', { name: 'Create workflow', exact: true }).click();
    await page.getByText('Workflow created. Advance steps to prepare the proposal.', { exact: true }).waitFor();
    await page.getByRole('button', { name: 'Advance ready steps', exact: true }).click();
    await page.locator('.status.waiting_approval').waitFor();
    await page.getByText('Tool calls and saved evidence', { exact: true }).click();
    check('workflow exposes actual accounting and RAG receipts', (await page.locator('#detail pre').textContent()).includes('rag_api'));
    await page.locator('#reason').fill('Independent proposal check');
    await page.getByRole('button', { name: 'Approve proposal', exact: true }).click();
    await page.getByText('Your role cannot perform this action.', { exact: true }).waitFor();
    check('workflow self approval blocked in browser', true);
    await capture('workflow-desktop');
    await responsive('workflow');
    await workflowRole('reviewer');
    // The newest run is the just-created approval request.
    await page.locator('#runs button').first().click();
    await page.locator('#reason').fill('Independent browser reviewer accepts synthetic proposal');
    await page.getByRole('button', { name: 'Approve proposal', exact: true }).click();
    await page.locator('.status.approved').waitFor();
    check('workflow reviewer advances approval state', true);
    await workflowRole('builder');
    await page.locator('#runs button').first().click();
    await page.getByRole('button', { name: 'Advance ready steps', exact: true }).click();
    await page.locator('.status.completed').waitFor();
    check('workflow browser completes approved mock case', true);

    await page.goto(session.urls.rag + '/console');
    check('RAG page identity', await page.title() === 'Knowledge Review');
    await page.locator('#key').fill(session.keys.rag.finance);
    await page.getByRole('button', { name: 'Connect', exact: true }).click();
    await page.getByRole('button', { name: 'Search sources' }).click();
    await page.locator('#sources .source').first().waitFor();
    check('RAG shows actual authorized source', (await page.locator('#sources').textContent()).includes('invoice-policy'));
    await capture('rag-desktop');
    await page.locator('#question').fill('7312');
    await page.getByRole('button', { name: 'Search sources' }).click();
    await page.getByText('No authorized matching source. Ask a document owner for help.', { exact: true }).waitFor();
    check('RAG HR canary withheld from finance UI', (await page.locator('#sources').textContent()) === '');
    await responsive('rag');

    await page.goto(session.urls.governance + '/console');
    check('evaluation page identity', await page.title() === 'Evaluation Review');
    await page.locator('#key').fill(session.keys.governance.governor);
    await page.getByRole('button', { name: 'Load runs', exact: true }).click();
    await page.waitForFunction(() => /\d+ executed runs loaded\./.test(document.getElementById('message').textContent));
    await page.getByRole('button', { name: 'Run positive fixture' }).click();
    await page.getByRole('heading', { name: 'Release gate passed' }).waitFor();
    check('evaluation positive fixture executed through UI', await page.locator('#detail tbody tr').count() === 16);
    await page.getByRole('button', { name: 'Run negative fixture' }).click();
    await page.getByRole('heading', { name: 'Release gate blocked' }).waitFor();
    check('evaluation negative control blocks gate in UI', (await page.locator('#detail tbody').textContent()).includes('FAIL'));
    await capture('governance-desktop');
    await responsive('governance');
    check('no browser runtime or console errors', errors.length === 0);
    fs.writeFileSync(path.join(output, 'browser-qa.json'), JSON.stringify({ browser: 'Playwright Chromium',
      viewports: ['1440x1000', '390x844'], browser_plugin: 'not available; existing Playwright used', checks, errors, expectedDenials, screenshots }, null, 2));
    console.log(JSON.stringify({ passed: checks.length, errors, evidence: output }));
  } catch (error) {
    await page.screenshot({path: path.join(output, 'failure.png'), fullPage: true});
    fs.writeFileSync(path.join(output, 'failure.json'), JSON.stringify({error:error.message, checks, errors, url:page.url()},null,2));
    throw error;
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error.message); process.exitCode = 1; });
