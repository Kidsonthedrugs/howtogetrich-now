# howtogetrich.now

A single-page playbook for 2026: **Creator**, **Clipper**, **Vibe Coder**.
One HTML file, no framework, no build step at runtime.

- Live design stance: **Neon Brutalist** (176px→146px headlines, hard borders, offset shadows, rotated marquee bands)
- 37 KB HTML, 12.3 KB gzipped, zero external requests
- Verified 0 horizontal overflow and 0 clipped text from 320px to 1440px

## Structure

```
index.html            the page (GENERATED — do not edit by hand)
og.png                1200x630 social card (GENERATED)
deploy/               upload this folder to Cloudflare Pages
build/
  data.py             all copy, numbers and paths live here  ← edit this
  site.py             DATA -> index.html + build/og.html
  package.py          -> deploy/ (404, robots, sitemap, _headers)
  verify.py           desktop layout assertions (headless Chrome)
  verify_mobile.py    320-834px assertions via iframe viewports
  make_variants.py    the three original design sketches
  shots.py            screenshot harness
sketches/             the three stances explored (002 was chosen)
BLUEPRINT.md          content architecture, voice rules, decisions log
DEPLOY.md             5-step Cloudflare Pages guide
```

## Build

```bash
python build/site.py        # DATA -> index.html
python build/package.py     # -> deploy/
python build/verify.py      # desktop checks
python build/verify_mobile.py
```

Content lives only in `build/data.py`. `index.html` is generated output.

## Adding a skill path

1. Add a card to `DATA["three"]["cards"]` (same order as the path).
2. Add the path to `DATA["paths"]` — `id`, `n`, `name`, `tagline`, `metrics`,
   `why`, `playbook` (5), `stack` (5), `money` (5), `proof`.
3. Flip its row in `DATA["pipeline"]["items"]` from `QUEUED` to `LIVE`.
4. Rebuild, redeploy. Tabs, nav and responsive rules all derive from array length.

## Deploy

See `DEPLOY.md`. Cloudflare Pages, upload `deploy/`, point `howtogetrich.now` at it.

Nothing here is financial advice.
