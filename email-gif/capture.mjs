// Capture issue pages at phone size for the email GIF.
// usage: node email-gif/capture.mjs <base-url> <out-dir> <slug> [<slug> …]
// Writes <out-dir>/<slug>.png (full page at 2x) and <out-dir>/<slug>.json
// (positions of the graphics and callouts, in CSS px).
import { mkdir, writeFile } from 'node:fs/promises';
import { chromium } from 'playwright';

const [baseUrl, outDir, ...slugs] = process.argv.slice(2);
if (!baseUrl || !outDir || slugs.length === 0) {
  console.error('usage: node email-gif/capture.mjs <base-url> <out-dir> <slug> [<slug> …]');
  process.exit(1);
}

await mkdir(outDir, { recursive: true });
const browser = await chromium.launch(process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {});

for (const slug of slugs) {
  const page = await browser.newPage({
    viewport: { width: 390, height: 844 },
    deviceScaleFactor: 2,
    // Skips the page-turn and typewriter animations and shows highlights fully drawn.
    reducedMotion: 'reduce',
    colorScheme: 'light',
  });
  await page.goto(`${baseUrl.replace(/\/$/, '')}/issues/${slug}/`, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: `${outDir}/${slug}.png`, fullPage: true });
  const layout = await page.evaluate(() => {
    const box = (el) => {
      const r = el.getBoundingClientRect();
      return { y: Math.round(r.top + scrollY), h: Math.round(r.height) };
    };
    return {
      height: document.documentElement.scrollHeight,
      graphics: [...document.querySelectorAll('.prose .fig')].map(box),
      callouts: [...document.querySelectorAll('.prose .callout')].map(box),
      headings: [...document.querySelectorAll('.prose h2')].map(box),
    };
  });
  await writeFile(`${outDir}/${slug}.json`, JSON.stringify(layout));
  await page.close();
  console.log(`captured ${slug}`);
}

await browser.close();
