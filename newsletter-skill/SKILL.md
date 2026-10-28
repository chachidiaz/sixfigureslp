---
name: "newsletter-creation-skill"
description: "Generates Six Figure Insider Newsletter from voice memo dictation, then hands the approved draft to the insider-publishing-partner skill for editing, graphics and publishing"
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
5. When he approves the draft and picks a subject line, hand it to the Insider Publishing Partner (see below).

## Audience
Speech-language pathologists who are building income beyond 1:1 therapy: pre-launch dreamers, stuck practice owners, online builders, and overwhelmed learners. They're skeptical of hype and "get rich quick" language, so stay honest, realistic, and encouraging.

## Handing off to the Insider website
This skill writes the newsletter; it never publishes anything itself. Once Chachi approves the draft and picks a subject line, use the **insider-publishing-partner** skill. It edits the issue, adds highlights, callouts and graphics, shows Chachi the result, and publishes it to https://thesixfigureslp.com/insider/ only after he approves.

Pass it:
- The subject line he picked (it becomes the title)
- The publish date
- The full newsletter text, including the sign-off

If the insider-publishing-partner skill isn't available, give Chachi the finished newsletter and tell him to run it through that skill before it goes on the website.
