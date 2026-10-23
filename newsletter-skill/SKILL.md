---
name: "newsletter-creation-skill"
description: "Generates Six Figure Insider Newsletter from voice memo dictation and publishes approved issues to the Insider website"
---

# Six Figure Insider Newsletter

## What this does
Chachi sends a transcribed voice memo (a stream-of-consciousness rant). Turn it into a newsletter for the Six Figure Insider list. It should read like Chachi talking, not like AI wrote it.

## Format
- Subject line: short, honest, mid-conversation (e.g. "I gotta get this off my chest"). Offer 5 options if he hasn't chosen one. Never name specific creators or challenges in the subject.
- Length: about 600 to 800 words, a 3 to 5 minute read. Detailed but concise.
- Skimmable: use bold headers that sound like something he'd say out loud, not marketing-listicle headers.
- Sign-off: "Talk soon, Emily (and Chachi)"
- Default to value-driven content with no sales CTA unless he asks for one.
- If a point is unclear or a fact is missing, ask before guessing.

## Voice rules
1. Lead with goodwill before any critique.
2. Use "I want to be really clear in that..." to mark the most important point.
3. Circle back to the main point instead of saying it once.
4. Write long, additive sentences with "and" and "so" openers and soft trailing qualifiers ("if that makes sense," "and yeah").
5. Use plain, funny, everyday metaphors (e.g. "underwear in a wad," "lottery ticket," "copy of a copy," "step one vs. step thirty"). Use his own metaphors from the transcript before inventing new ones.
6. Make big numbers feel big with "staggering" and "quite literally."
7. Teach the real process and call out the highlight reel.
8. Use AI to go faster, but keep the human perspective his.
9. Speak as "we," with relatable "myself included" moments.
10. End with reassurance: they're not behind, and we're here for them.

## Avoid
- Tidy three-part structures and perfectly balanced sentences
- Smooth consultant-style transitions
- Listicle-sounding headers
- Anything that sounds polished or AI-written
- Inventing stories, numbers, or claims he didn't say

## Process
1. Read the whole transcript and pull out his main point, the supporting beats, and his own phrases and metaphors.
2. Keep his actual wording wherever possible. Clean up filler and false starts, but keep the rhythm and the repeats.
3. Draft the newsletter in the format above.
4. Offer subject line options and ask if anything should change.
5. When he approves the draft and picks a subject line, publish it to the Insider website (see below). Never publish before he says it's approved.

## Audience
Speech-language pathologists who are building income beyond 1:1 therapy: pre-launch dreamers, stuck practice owners, online builders, and overwhelmed learners. They're skeptical of hype and "get rich quick" language, so stay honest, realistic, and encouraging.
## Publishing to the Insider website
Every approved issue is archived on the Insider website. Publishing means saving one Markdown file to GitHub; the site rebuilds and goes live on its own a few minutes later.

- Repository: `chachidiaz/sixfigureslp`
- Branch: `main`
- File path: `content/issues/YYYY-MM-DD-short-slug.md` (today's date, then 3 to 6 lowercase words from the subject line joined by hyphens, e.g. `content/issues/2026-10-28-i-gotta-get-this-off-my-chest.md`)
- Commit message: `Publish issue: <subject line>`

File format:

```md
---
title: "<the subject line he picked>"
summary: "<one sentence, under 140 characters, in his voice, saying what the issue is about>"
date: YYYY-MM-DD
---

<the newsletter body>
```

Rules for the file:
- Only `title`, `summary` and `date` go at the top. The website works out the issue number and read time by itself.
- Put the title and summary in double quotes. If they contain a double quote, write it as \" or use curly quotes.
- Leave out the subject line from the body (the website shows it as the headline).
- Write each bold header as a `## ` heading on its own line, not as **bold** text.
- Optional: put the single most important line on its own as a pull quote, starting the line with `> `. Use this at most once.
- Optional: wrap one short key phrase in `<mark>` and `</mark>` to highlight it. Use this at most once.
- End with the sign-off on two lines, in italics:
  `*Talk soon,*` then a line with `*Emily (and Chachi)*`

To save the file, use a GitHub tool that can create a file in the repository (for example a GitHub connector's "create or update file" action). If there is no tool that can write to GitHub, give Chachi the finished file and its file path so he can add it on github.com (Add file > Create new file). After saving, tell him the issue will be live on the website in a few minutes.

To fix a published issue, update the same file. Don't create a new one.
