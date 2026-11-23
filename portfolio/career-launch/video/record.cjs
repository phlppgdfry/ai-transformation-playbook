// Records real public browser interactions. No application HTML/state is replaced.
const path = require('node:path');
const fs = require('node:fs');
const root = path.resolve(__dirname, '../../..');
const { chromium } = require(require.resolve('playwright', { paths: [path.join(root, 'integration')] }));
const out = process.argv[2];
if (!out) throw new Error('Usage: node portfolio/career-launch/video/record.cjs OUTPUT_DIRECTORY');
fs.mkdirSync(out, { recursive: true });
const base = 'https://phlppgdfry.github.io/';
async function frame(p) {
  const panel = p.locator('#demo .demo').first();
  if (await panel.count()) await panel.evaluate(el => window.scrollTo(0, window.scrollY + el.getBoundingClientRect().top - 70));
  else await p.evaluate(() => window.scrollTo(0, 0));
}
const selected = new Set((process.argv[3] || '').split(',').filter(Boolean));
const scenes = [
  ['01-overview', 'ai-transformation-playbook', null, 10, async () => {}],
  ['02-business', 'ai-transformation-playbook/console', null, 20, async p => {
    await p.locator('#hours').filter({ hasText: /\d/ }).waitFor();
    await p.waitForTimeout(5000);
    await p.locator('#adoption').fill('0');
    await p.getByRole('button', { name: 'Recalculate scenario' }).click(); await frame(p);
    await p.waitForTimeout(1000);
    if (!/^0(?:[.,]0+)?/.test(await p.locator('#hours').innerText())) throw Error('Zero adoption did not remove capacity');
  }],
  ['03-accounting', 'enterprise-ai-accounting-copilot', '#demo', 20, async p => {
    await p.getByRole('button', { name: 'Valid invoice', exact: true }).click(); await frame(p);
    await p.waitForTimeout(4000);
    await p.getByRole('button', { name: 'Off by one cent', exact: true }).click(); await frame(p);
    await p.locator('#ac-status').filter({ hasText: '422' }).waitFor();
    await p.waitForTimeout(5000);
    await p.getByRole('button', { name: 'Unknown supplier, €12,000', exact: true }).click(); await frame(p);
    await p.locator('#ac-status').filter({ hasText: 'blocked' }).waitFor();
  }],
  ['04-workflow', 'agentic-workflow-platform', '#demo', 20, async p => {
    await p.locator('#aw-tl li').filter({ hasText: 'plan validated' }).click(); await frame(p);
    await p.waitForTimeout(5000);
    await p.locator('#aw-tl li').filter({ hasText: 'approval requested' }).click(); await frame(p);
    await p.locator('#aw-detail').filter({ hasText: 'no CRM case exists yet' }).waitFor();
    await p.waitForTimeout(5000);
    await p.locator('#aw-tl li').filter({ hasText: 'case created' }).click(); await frame(p);
    await p.locator('#aw-detail').filter({ hasText: 'mock CRM' }).waitFor();
  }],
  ['05-knowledge', 'azure-ai-rag-knowledge-assistant', '#demo', 20, async p => {
    await p.locator('#kb-q').fill('opleidingsbudget 7312');
    await p.locator('#kb-who').selectOption('finance');
    await p.locator('#kb-hits').filter({ hasText: 'No permitted document' }).waitFor();
    await p.waitForTimeout(6000);
    await p.locator('#kb-who').selectOption('hr');
    await p.locator('#kb-hits .kb-hit').first().waitFor();
  }],
  ['06-evaluation', 'enterprise-ai-evals-governance', '#demo', 20, async p => {
    await p.locator('#eg-runs button[data-r="good"]').click(); await frame(p);
    await p.locator('#eg-verdict').filter({ hasText: 'PASSED' }).waitFor();
    await p.waitForTimeout(6000);
    await p.locator('#eg-runs button[data-r="unsafe"]').click(); await frame(p);
    await p.locator('#eg-verdict').filter({ hasText: 'FAILED' }).waitFor();
  }],
  ['07-microsoft', 'microsoft-copilot-studio-automation', '#demo', 20, async p => {
    await p.locator('#cs-steps button[data-i="1"]').click(); await frame(p);
    await p.locator('#cs-stage').filter({ hasText: 'Human approval required' }).waitFor();
    await p.waitForTimeout(6000);
    await p.locator('#cs-steps button[data-i="2"]').click(); await frame(p);
    await p.waitForTimeout(4000);
    await p.locator('#cs-steps button[data-i="3"]').click(); await frame(p);
    await p.locator('#cs-stage').filter({ hasText: 'local mock task' }).waitFor();
  }],
  ['08-limits', 'ai-transformation-playbook', '#how', 10, async () => {}],
];
(async () => {
  const browser = await chromium.launch({ channel: 'chrome', headless: true });
  const evidencePath = path.join(out, 'capture.json');
  const evidence = fs.existsSync(evidencePath) ? JSON.parse(fs.readFileSync(evidencePath)) : { recordedAt: new Date().toISOString(), type: 'Actual public showcase interactions; recorded evidence replays remain replays', scenes: [] };
  try {
    for (const [id, repo, anchor, duration, action] of scenes.filter(s => !selected.size || selected.has(s[0]))) {
      const context = await browser.newContext({ viewport: { width: 1280, height: 600 }, recordVideo: { dir: out, size: { width: 1280, height: 600 } }, reducedMotion: 'reduce' });
      const p = await context.newPage();
      const clock = Date.now(); const errors = [];
      p.on('pageerror', e => errors.push(e.message));
      p.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
      const url = base + repo + '/';
      const response = await p.goto(url, { waitUntil: 'networkidle' });
      if (response.status() !== 200) throw Error('HTTP ' + response.status());
      if (anchor) { await p.locator(anchor).scrollIntoViewIfNeeded(); await p.evaluate(() => window.scrollBy(0, -70)); }
      if (anchor || repo.endsWith("/console")) await frame(p);
      await p.waitForTimeout(1000);
      const start = (Date.now() - clock) / 1000;
      const began = Date.now();
      await action(p);
      await p.waitForTimeout(Math.max(0, duration * 1000 - (Date.now() - began)));
      await p.screenshot({ path: path.join(out, id + '.png') });
      const video = p.video(); await context.close();
      await video.saveAs(path.join(out, id + '.webm'));
      evidence.scenes = evidence.scenes.filter(s => s.id !== id);
      evidence.scenes.push({ id, url, start, duration, capturedAt: new Date().toISOString(), assertions: 'passed', errors });
      evidence.scenes.sort((a, b) => a.id.localeCompare(b.id));
      fs.writeFileSync(path.join(out, 'capture.json'), JSON.stringify(evidence, null, 2) + '\n');
      console.log(id, 'recorded', errors.length, 'errors');
      if (errors.length) throw Error(id + ': browser errors');
    }
  } finally { await browser.close(); }
})().catch(e => { console.error(e); process.exitCode = 1; });
