# The Six Figure Insider — newsletter archive

A small static site (built with [Astro](https://astro.build)) that archives every issue of The Six Figure Insider.

Live at **https://thesixfigureslp.com/insider/**.

- `/insider/` — archive: featured latest issue, search, every issue grouped by year
- `/insider/issues/<file-name>/` — one page per issue

## How an issue gets published

1. Dictate a voice memo and paste the transcript into Claude.
2. The newsletter skill (`newsletter-skill/SKILL.md`) writes the issue and offers subject lines.
3. The publishing-partner skill (`publishing-partner-skill/`) edits it, adds highlights, callouts and graphics, and shows you the result.
4. Once you approve, it saves the issue as a Markdown file in `content/issues/` on the `main` branch.
5. GitHub Actions (`.github/workflows/deploy.yml`) rebuilds the site and uploads it to Hostinger. It's live a few minutes later.

Callout and graphic templates: `publishing-partner-skill/references/components.md`.

The deploy also makes an **email GIF** for each new or changed issue: the issue scrolling inside a phone, at `https://thesixfigureslp.com/insider/email/<issue>.gif`. The scripts and phone frame are in `email-gif/`. Running the workflow by hand from the Actions tab remakes every GIF.

## Issue file format

The file name becomes the URL: `content/issues/2026-10-28-i-gotta-get-this-off-my-chest.md` → `/insider/issues/2026-10-28-i-gotta-get-this-off-my-chest/`.

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

The site is uploaded over SSH to `domains/thesixfigureslp.com/public_html/insider` on Hostinger, so it shows at **https://thesixfigureslp.com/insider/**. Only that folder is touched; the rest of the website stays as it is.

1. **Turn on SSH:** in hPanel, open **Advanced > SSH Access** and enable it. Note the IP address, port (usually `65002`) and username (like `u123456789`).
2. **Make a deploy key** on your computer (Terminal on a Mac):
   `ssh-keygen -t ed25519 -C "insider-deploy" -f ~/insider_deploy -N ""`
   This makes two files: `~/insider_deploy` (private) and `~/insider_deploy.pub` (public).
3. **Give Hostinger the public key:** on the same SSH Access page, add an SSH key and paste the contents of `insider_deploy.pub`.
4. **Give GitHub the private key and login:** in this repository open **Settings > Secrets and variables > Actions** and add three repository secrets:
   - `SSH_HOST`: the IP address from step 1
   - `SSH_USERNAME`: the username from step 1
   - `SSH_PRIVATE_KEY`: the full contents of `insider_deploy` (including the BEGIN and END lines)
5. Run **Deploy to Hostinger** from the Actions tab (or push to `main`).

Optional repository **variables** (same page, Variables tab): `SSH_PORT` if it isn't `65002`, and `SSH_TARGET_DIR` if the domain's folder is somewhere else. The workflow refuses a folder that isn't inside `public_html`, so it can never overwrite the main website.

Until the secrets are set, the workflow still builds the site but skips the upload and shows a warning.

## Running it locally

Needs Node 22.12+.

```sh
npm install
npm run dev      # http://localhost:4321/insider/
npm run build    # static site in dist/
```

## Notes

- **Font license:** Bringbold Nineties (`public/fonts/`) needs a commercial web license before launch.
- Theme choice is saved in `localStorage` (`sfi-theme`). With no saved choice the site follows the visitor's system setting.
- Design handoff (brief + design-canvas files) lives in `design/` for reference.
