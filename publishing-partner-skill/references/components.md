# Insider site components

Copy these templates into the issue's Markdown. The site styles them; never add colours, fonts, sizes or images yourself.

Rules for raw HTML in Markdown:
- Graphics (`<figure class="fig">`) must have **no blank lines inside them** and no indentation, or the Markdown parser breaks them apart.
- Callouts are the opposite: a blank line after `<aside …>` and before `</aside>`, so the Markdown inside is formatted.
- Inside HTML, write curly quotes and apostrophes (’ “ ”) yourself, `&lt;` for <, and `&amp;` for &.
- Leave a blank line before and after every graphic or callout.

## Highlight

```md
Some sentence with <mark>the part that matters most</mark> in it.
```

## Pull quote

```md
> One short sentence that is the heart of the issue.
```

## Callout

For a key paragraph or short list. The label is 2 to 6 words naming the idea.

```md
<aside class="callout" data-label="Every live launch needs three things">

1. A really good, no-brainer, take-my-money offer
2. A dialed-in email sequence and social content
3. Traffic and an audience

</aside>
```

## Graphic frame

Every graphic sits in this frame. `fig__kicker` is a 2–5 word label; `fig__title` says the takeaway. `fig__note` is optional (sources, how a number was worked out).

```html
<figure class="fig">
<figcaption class="fig__cap"><span class="fig__kicker">The masterclass</span><span class="fig__title">From sign-up to sale, live</span></figcaption>
<!-- one or more bodies from below -->
<span class="fig__note">Bars drawn to scale.</span>
</figure>
```

## Bars (comparisons and funnels)

One `.bar` per row. `--v` is the bar length: value ÷ largest value in this chart × 100, as a percent. Example: 2,000 / 300 / 28 → 100% / 15% / 1.4%. Add `bar--muted` to a row to show it as the older or lesser item (grey instead of orange). `<small>` inside the label adds a second line, e.g. a date or how a number was worked out.

```html
<div class="bars">
<div class="bar"><span class="bar__label">Registered</span><span class="bar__track"><span class="bar__fill" style="--v: 100%"></span></span><span class="bar__value">2,000+</span></div>
<div class="bar"><span class="bar__label">Showed up live</span><span class="bar__track"><span class="bar__fill" style="--v: 15%"></span></span><span class="bar__value">&lt;300</span></div>
<div class="bar bar--muted"><span class="bar__label">Revenue per day<small>Oct 2025 · $23k ÷ 12</small></span><span class="bar__track"><span class="bar__fill" style="--v: 59%"></span></span><span class="bar__value">~$1,900</span></div>
</div>
```

## Stats (headline numbers)

Two to four numbers. Keep each value short (`$147`, `8 days`, `+13%`) and put the context in the label.

```html
<div class="stats">
<div class="stat"><span class="stat__value">$147</span><span class="stat__label">price, down from $187</span></div>
<div class="stat"><span class="stat__value">8 days</span><span class="stat__label">on sale, down from 12</span></div>
</div>
```

## Signals (if-this-then-that, diagnosis)

Each `.signal` row has condition chips and what it means. `chip--high` is filled (dark), `chip--low` is outlined. `signals__group` is an optional small heading between groups of rows.

```html
<div class="signals">
<div class="signals__group">Email</div>
<div class="signal"><div class="signal__chips"><span class="chip chip--high">Opens high</span><span class="chip chip--low">Clicks low</span></div><div class="signal__meaning">The emails didn’t resonate. The messaging was off.</div></div>
<div class="signal"><div class="signal__chips"><span class="chip chip--low">Opens low</span><span class="chip chip--high">Clicks high</span></div><div class="signal__meaning">Your subject lines need work.</div></div>
</div>
```

## Timeline (schedules and sequences)

One `<li>` per step: the big number, a short day/time label, what happens, and a tag. Tags: `tag--none` (neutral label, e.g. Launch, Value, Rest), `tag--soft` (lime, e.g. Soft urgency), `tag--hard` (orange, e.g. Hard urgency). Add `class="is-rest"` to an `<li>` for a day off.

```html
<ol class="timeline">
<li><span class="timeline__day"><b>1</b>Tue</span><span class="timeline__what">Cart open announcement</span><span class="tag tag--none">Launch</span></li>
<li class="is-rest"><span class="timeline__day"><b>5</b>Sat</span><span class="timeline__what">No email</span><span class="tag tag--none">Rest</span></li>
<li><span class="timeline__day"><b>6</b>Sun</span><span class="timeline__what">Closes Tuesday</span><span class="tag tag--soft">Soft urgency</span></li>
<li><span class="timeline__day"><b>8</b>Tue PM</span><span class="timeline__what">Final reminder</span><span class="tag tag--hard">Hard urgency</span></li>
</ol>
```

## Worked example

`content/issues/2026-10-28-steal-our-launch-strategy.md` in the repository uses every component above.
