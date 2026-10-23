# The Six Figure Insider — newsletter archive

A small static site (built with [Astro](https://astro.build)) that archives every issue of The Six Figure Insider.

- `/` — archive: featured latest issue, search, every issue grouped by year
- `/issues/<file-name>/` — one page per issue

## Adding an issue

Add a Markdown file to `content/issues/`. The file name becomes the URL, e.g. `09-my-new-issue.md` → `/issues/09-my-new-issue/`.

```md
---
number: "09"
title: "Your headline"
summary: "One-sentence summary shown under the title and in the archive."
date: 2026-10-21
readTime: 4
author: "The Insider team"   # optional, this is the default
---

Body text…

## Section heading

1. Numbered to-do items
- or bullet points

> A blockquote becomes the pull-quote card.

A <mark>highlighted phrase</mark> gets the lime highlighter sweep.

*— The Insider team*  (italic sign-off)
```

The issues in `content/issues/` are placeholders from the design handoff; only issue 08 has a full body. Replace them with the real issues.

## Running it

Needs Node 22.12+.

```sh
npm install
npm run dev      # http://localhost:4321
npm run build    # static site in dist/
```

Deploys as a plain static site (Vercel, Netlify, Cloudflare Pages: build `npm run build`, output `dist`).

## Notes

- **Font license:** Bringbold Nineties (`public/fonts/`) needs a commercial web license before launch.
- Theme choice is saved in `localStorage` (`sfi-theme`). With no saved choice the site follows the visitor's system setting.
- Design handoff (brief + design-canvas files) lives in `design/` for reference.
