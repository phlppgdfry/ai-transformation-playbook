// Verifies the real hosted/local player; emits only public URLs and test outcomes.
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '../../..');
const { chromium } = require(require.resolve('playwright', { paths: [path.join(root, 'integration')] }));
const base = process.argv[2], output = process.argv[3];
if (!base || !output) throw Error('Usage: node verify.cjs BASE_URL OUTPUT_JSON');
(async () => {
  const browser = await chromium.launch({ channel: 'chrome', headless: true });
  const checks = [], errors = [];
  try {
    const page = await browser.newPage();
    page.on('pageerror', e => errors.push(e.message));
    page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
    for (const width of [375, 768, 1024, 1440]) {
      await page.setViewportSize({ width, height: 900 });
      const response = await page.goto(base.replace(/\/$/, '') + '/?qa_viewport=' + width + '#tour', { waitUntil: 'networkidle' });
      if (!response || response.status() !== 200) throw Error('Page unavailable');
      const video = page.locator('#tour video');
      await video.scrollIntoViewIfNeeded();
      await video.evaluate(v => { v.muted = true; v.load(); });
      await page.waitForFunction(() => document.querySelector('#tour video').readyState >= 2);
      const info = await video.evaluate(v => ({ duration: v.duration, width: v.videoWidth, height: v.videoHeight, controls: v.controls, poster: v.poster }));
      if (Math.abs(info.duration - 140) > 0.1 || info.width !== 1280 || info.height !== 720 || !info.controls) throw Error('Unexpected video metadata');
      await video.evaluate(v => v.play());
      await page.waitForTimeout(1300);
      if (!await video.evaluate(v => v.currentTime > 0 && !v.paused)) throw Error('Video did not play');
      await video.evaluate(v => v.pause());
      const overflow = await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1);
      if (overflow) throw Error('Horizontal overflow at ' + width);
      const transcript = page.locator('#tour a[href="media/TRANSCRIPT-NL.md"]');
      await transcript.waitFor();
      const content = await page.request.get(await transcript.getAttribute('href').then(h => new URL(h, page.url()).href));
      if (content.status() !== 200 || !(await content.text()).includes('Geen nieuwe modelaanroep')) throw Error('Transcript missing');
      checks.push({ width, playerMetadata: 'pass', actualPlayback: 'pass', transcript: 'pass', noPageOverflow: 'pass', info });
    }
    const evidence = { checkedAt: new Date().toISOString(), base, checks, errors };
    fs.writeFileSync(output, JSON.stringify(evidence, null, 2) + '\n');
    console.log(JSON.stringify(evidence));
    if (errors.length) throw Error('Console/page errors occurred');
  } finally { await browser.close(); }
})().catch(e => { console.error(e); process.exitCode = 1; });
