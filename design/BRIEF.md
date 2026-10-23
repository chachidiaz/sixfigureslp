# Six Figure Insider — Newsletter Archive: Build Brief

A small, text-first website that archives every issue of **The Six Figure Insider**, a newsletter that teaches SLPs (speech-language pathologists) quick, practical marketing. Written by an SLP and a digital marketer who built an SLP education business together. Readers are already subscribers, so there is **no sign-up form**.

## What's in this folder

| Path | What it is |
|---|---|
| `design/Main.dc.html` | Archive page, desktop (1280 wide, fluid) |
| `design/Issue.dc.html` | Single issue page, desktop |
| `design/Mobile-Archive.dc.html` | Archive page, phone (390 wide) |
| `design/Mobile-Issue.dc.html` | Single issue page, phone |
| `fonts/BringboldNineties-Regular.woff2` | Display font (licensed — see Fonts) |

The `.dc.html` files come from a design canvas. Treat them as the **visual and behavioral reference**, not production code: they use a small template runtime (`<x-dc>`, `{{holes}}`, `<sc-if>`, `<sc-for>`, a `class Component extends DCLogic` script). Rebuild the same result in plain HTML/CSS/JS or the framework of choice. All styles are inline, so exact sizes and spacing can be read straight from the markup.

## Pages

1. **Archive** (`/`) — header bar, intro, featured latest issue, list of all issues grouped by year, footer.
2. **Issue** (`/issues/[slug]`) — header bar, story header, article body, "Keep reading", footer.

Desktop and mobile are one responsive site; the mobile files show the intended phone layout.

## Content model

Store each issue as its own file (e.g. Markdown with front matter) so adding an issue = adding a file:

```yaml
number: "08"            # shown as "Issue 08" / big orange numeral
title: "Why your practice website isn't booking calls"
summary: "Three fixes you can make this week, starting with the button nobody can find."
date: 2026-10-14        # desktop: "October 14, 2026" · mobile: "Oct 14, 2026"
readTime: 4             # "4 min read"
author: "The Insider team"
```

Body supports: paragraphs, `##` section headings, ordered/unordered lists, a **pull quote**, and **highlighted phrases**. The 8 issues in the designs are **dummy content** — replace with real issues.

## Design tokens

Colors (CSS variables, swapped by theme on the page root via `data-theme="light|dark"`):

| Token | Light | Dark | Use |
|---|---|---|---|
| `--paper` | `#faf6ef` | `#1c1216` | Page background |
| `--ink` | `#24101a` | `#f6efe6` | Main text, rules, icons |
| `--muted` | `#6b4f58` | `#c9b4bc` | Secondary text (summaries, meta) |
| `--line` | `#e6d7cb` | `#3d2c33` | Hairline dividers, outlines |
| `--soft` | `#f2ebe1` | `#261a1f` | Tinted cards (pull quote, "Keep reading") |
| `--accent-text` | `#c93a00` | `#ff8a4f` | Small orange text (labels like "Issue 08") |
| orange (fixed) | `#ff4d03` | `#ff4d03` | Big numerals, wordmark, primary button, caret |
| lime highlight | `#d0ce5d` | `#d0ce5d` | Highlighter (text on it stays `#24101a`) |

Outside the page (only visible during the page-turn animation): `#e9e1d8`.

## Fonts

| Role | Font | Notes |
|---|---|---|
| Display: archive headline, issue numerals, year headings, "The Insider" wordmark | **Bringbold Nineties** Regular (`fonts/`) | Never bold, never italic. **Needs a commercial web license before launch.** |
| Serif: issue titles, article h1/h2, italic summaries, pull quote, sign-off | **Libre Baskerville** (Google Fonts, 400/700/400 italic) | Anything italic uses this font. |
| Body: paragraphs, summaries, labels, buttons, meta | **Bricolage Grotesque** (Google Fonts) | Default weight **300 (Light)**; labels 400–500. |
| Small caps labels ("Issue 08", "Latest issue", dates on mobile archive) | **IBM Plex Mono** 500, uppercase | |

Body copy is **16px** everywhere (line-height ~1.6–1.75). Desktop issue h1 is clamp(2rem, 4.5vw, 2.875rem); section h2 24px (22px mobile). Archive headline clamp(2.5rem, 5.5vw, 4.5rem); 46px on mobile.

## Layout

**Header bar (all pages)** — light, full-width, single hairline (`--line`) underneath. Three-column grid:
- Left: archive page → issue count ("8 issues and counting"; on mobile a **search icon**); issue page → "‹ Archive" back link.
- Center: "The Insider" wordmark, Bringbold, orange.
- Right: **light/dark switch** (see Interactions).

**Archive**
- Intro: orange label "Every issue, archived" → Bringbold headline "Every **issue**, in one place." ("issue" in orange) → italic serif intro line.
- Desktop: search field sits right of the intro (underlined input, live results count). Mobile: search lives behind the header search icon and slides open under the bar.
- Featured latest issue: big orange numeral + date, serif title, summary, orange pill "Read the Issue" button with an arrow disc, read time. Hidden while searching.
- Issue list grouped by year (Bringbold year heading + count). Each row: orange numeral, serif title (links to issue), summary; date + read time.
- Footer: © 2026 Six Figure Insider.
- Note: the archive pages still carry a couple of heavier black rules (under year headings, above the footer) from an earlier newspaper style. The issue pages show the newer, calmer direction (hairlines + soft cards) — **align the archive to the issue-page style** when building.

**Issue**
- Reading column ~640–688px, left-aligned.
- Story header: mono orange "Issue 08" → serif headline → italic serif summary → byline line "The Insider team · date · read time".
- Body: 16px Bricolage Light; serif section headings; numbered to-do list; pull quote in a soft rounded card (`--soft`, radius 20/16px) with a big orange Bringbold quotation mark; italic sign-off.
- "Keep reading": soft card for the previous issue (numeral, label, title, chevron) + outlined "See all issues" button.
- Footer: centered small muted copyright.

## Interactions

1. **Light/dark switch** — pill switch (60×32) with sun and moon icons and a sliding knob; `role="switch"`, `aria-checked`, label "Dark mode". Choice is saved in `localStorage` (`sfi-theme`) and shared across pages. Colors transition over 0.3s.
2. **Typewriter headline** — "Every issue, in one place." types in letter by letter (~85ms per character, 0.4s delay) with a blinking orange caret; the headline reserves its final height so nothing jumps. Screen readers get the full text via `aria-label`. Skipped with reduced motion.
3. **Page turn** — on page load the page swings in from the left edge like a newspaper page (rotateY −88° → 0, ~0.9s, with a fading shade). Skipped with reduced motion. (Only the incoming page animates in the designs; a real site can also animate the outgoing page, e.g. with the View Transitions API.)
4. **Highlighter** — highlighted phrases sweep a lime marker left→right as they scroll into view (CSS scroll-driven animation with a timed fallback). Text on the highlight stays dark in both themes.
5. **Search** — filters issues by number, title and summary as you type; shows "X of Y issues match", an empty state with "Clear Search", and hides the featured issue while searching.

## Accessibility

- Visible focus ring: 3px solid `--ink`, 3px offset, on every control.
- Real `<a>`, `<button>`, `<label>`/`<input>` elements; icon-only buttons have `aria-label`s.
- Touch targets ≥ 44px on mobile.
- Respect `prefers-reduced-motion` for all four animations.

## Suggested prompt for Claude Code

> Read BRIEF.md and the files in design/. Build this newsletter archive as a [plain HTML/CSS/JS | Astro | Next.js] site: an archive page and one page per issue generated from Markdown files in `content/issues/`. Match the designs (tokens, fonts, layout, interactions) and make it responsive from 390px to desktop. Convert the 8 dummy issues into Markdown files so I can replace them with real ones.
