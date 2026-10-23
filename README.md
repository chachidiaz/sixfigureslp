# The Six Figure Insider — newsletter archive

A small static site (built with [Astro](https://astro.build)) that archives every issue of The Six Figure Insider.

- `/` — archive: featured latest issue, search, every issue grouped by year
- `/issues/<file-name>/` — one page per issue

## How an issue gets published

1. Dictate a voice memo and paste the transcript into Claude.
2. The newsletter skill (`newsletter-skill/SKILL.md`) writes the issue and offers subject lines.
3. Once you approve it, the skill saves it as a Markdown file in `content/issues/` on the `main` branch.
4. GitHub Actions (`.github/workflows/deploy.yml`) rebuilds the site and uploads it to Hostinger. It's live a few minutes later.

## Issue file format

The file name becomes the URL: `content/issues/2026-10-28-i-gotta-get-this-off-my-chest.md` → `/issues/2026-10-28-i-gotta-get-this-off-my-chest/`.

```md
---
title: "I gotta get this off my chest"
summary: "One sentence shown under the title and in the archive."
date: 2026-10-28
---

Body text…

## A header he'd say out loud

> One line as a pull quote (optional).

A <mark>highlighted phrase</mark> (optional).

*Talk soon,*
*Emily (and Chachi)*
```

Optional extra fields: `number: "07"` and `readTime: 5` override the automatic issue number (counted by date, oldest = 01) and read time (from the word count). `author` sets the byline (default "The Insider team").

## Hostinger setup (one time)

1. In Hostinger hPanel, add the domain or subdomain the site should live on.
2. Under **Files > FTP Accounts**, note the FTP host, username and password, and the folder the site is served from (usually `public_html`).
3. In GitHub, open this repository's **Settings > Secrets and variables > Actions** and add three repository secrets: `FTP_SERVER`, `FTP_USERNAME`, `FTP_PASSWORD`.
4. If the site's folder is not `public_html/` (for example a subdomain folder), add a repository **variable** `FTP_SERVER_DIR` with that folder, ending in `/`.
5. Run the **Deploy to Hostinger** workflow from the Actions tab (or push to `main`).

Until the secrets are set, the workflow still builds the site but skips the upload and shows a warning.

## Running it locally

Needs Node 22.12+.

```sh
npm install
npm run dev      # http://localhost:4321
npm run build    # static site in dist/
```

## Notes

- **Font license:** Bringbold Nineties (`public/fonts/`) needs a commercial web license before launch.
- Theme choice is saved in `localStorage` (`sfi-theme`). With no saved choice the site follows the visitor's system setting.
- Design handoff (brief + design-canvas files) lives in `design/` for reference.
