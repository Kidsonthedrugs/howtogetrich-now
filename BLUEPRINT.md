# howtogetrich.now — Content & UI Blueprint

Decision log from the structuring session. Everything below is what the three
sketches implement; changing a decision means editing `DATA` in
`build/make_variants.py`, not the HTML.

## Locked decisions

| Topic | Decision |
|---|---|
| Language | English only |
| CTA | Personal brand only (`@0xdierich`). No email capture, no product sale |
| Content | Full rewrite + web tightening of the original article, plus 2026 patches |
| Stack | Single-file HTML → Cloudflare Pages |
| Growth model | "Living edition": new paths are added as patches, never as rewrites |

## Content architecture — 8 stations

| # | Section | Job | Key element |
|---|---|---|---|
| 00 | HERO | Threat + promise in 3 lines | oversized type, live ticker |
| 01 | THE SHIFT | Why now: credentials → distribution | 2021 → 2027 timeline |
| 02 | THE THREE | Creator / Clipper / Vibe Coder | 3 clickable cards |
| 03 | THE PATHS | One deep dive per skill | tab switcher, 5-part anatomy |
| 04 | PATCH LOG | Room for future skills | status cards (IN PROGRESS / QUEUED) |
| 05 | THE COMBO | The flywheel | numbered chain + payoff line |
| 06 | RECEIPTS | Numbers, not narratives | 4 stat cells + airdrop ledger |
| 07 | 7-DAY SPRINT | Turn reading into doing | localStorage checklist |
| 08 | FINAL WARNING | Close the manifesto | full-bleed, "choose wisely" |

## The repeating path anatomy (section 03)

Every path uses the same five blocks, so the reader learns the shape once:

1. **Why now** — the market argument, 3–4 sentences, ends on a named example
2. **The playbook** — exactly 5 numbered moves
3. **Starter stack** — 5 tools, chips
4. **How the money works** — 5 revenue lines with realistic ranges
5. **Receipt** — one real quote with a named handle

## Adding a new path (the growth path)

1. Append an object to `DATA.paths` and a card to `DATA.three.cards`.
2. Change its entry in `DATA.pipeline.items` from QUEUED to LIVE.
3. Re-run `python build/make_variants.py`.

No layout work. No new CSS. The tabs, rail, TOC and mobile rules all derive
from the array length.

## UI stance — PICKED: Neon Brutalist

Three were built (`sketches/`), the user chose **002 Neon Brutalist**.
The shipping page (`index.html`) is that stance, refined:

- Headline capped at 146px (was 176px) so a phone still shows the next section.
- Section height cut ~10% by tightening section padding 74→56 and card padding.
- Hard 3px borders, offset box-shadows, rotated marquee bands kept as identity.
- Serif accents from the rejected editorial variant were NOT imported — the
  brutalist stance stays sans + mono.

The other two sketches stay in the repo as reference, not as alternatives to ship.

## Rules of the writing voice

- Sentence length under ~18 words. Second person. Present tense.
- One number per screen: $7,161 / $1,000 / 95% / 2027.
- Every claim ends in a name: Kaito, MrBeast, Cerebro, Gomtu, @Incenzee.
- No hedging verbs: "you will be obsolete", not "may face obsolescence".
- Admit the loss (95% in 2021) before quoting the win. It converts.

## Technical invariants

- Single file, no framework, no build step, <30 KB.
- All animation via IntersectionObserver + CSS transitions.
- `prefers-reduced-motion` is honored (reveals and marquee freeze).
- OG image 1200×630 required before publishing — link previews die without it.

## A11y + SEO shipped

- Skip link, single h1, 8 h2s, `role=tablist/tab/tabpanel`, `role=checkbox` with `aria-checked`.
- All tap targets ≥44px (section nav, tabs, checklist rows, footer links).
- `@supports` fallback for `-webkit-text-stroke` so the hero outline never goes invisible.
- OG + Twitter card (1200×630 png generated from `build/og.html`), canonical, JSON-LD Article.

## Files

```
howtogetrich/
├── build/make_variants.py     # DATA + 3 templates → sketches/
├── build/probe_layout.py      # desktop layout assertions (headless Chrome)
├── build/probe_mobile.py      # 390px / 768px assertions
├── build/shots.py             # screenshot harness
├── build/data.py              # ← all copy & numbers live here
├── build/site.py              # DATA → index.html + build/og.html
├── build/package.py           # → deploy/ (404, robots, sitemap, _headers)
├── build/verify_mobile.py     # 320–834px assertions via iframe viewports
├── index.html                 # GENERATED — do not edit
├── og.png                     # 1200×630 social card
├── deploy/                    # ← upload this folder
├── sketches/                  # 3 stances (002 chosen; keep as reference)
├── shots/                     # rendered PNGs
└── compare.html               # side-by-side iframes
```

## Verified (headless Chrome, shipping file)

| Width | Overflow-X | Clipped | Leaks |
|---|---|---|---|
| 1440 | 0 | 0 | 0 |
| 1280 | 0 | 0 | 0 |
| 1024 | 0 | 0 | 0 |
| 900 | 0 | 0 | 0 |
| 834 | 0 | 0 | 0 |
| 768 | 0 | 0 | 0 |
| 600 | 0 | 0 | 0 |
| 430 | 0 | 0 | 0 |
| 414 / 390 / 375 / 360 / 320 | 0 | 0 | 0 |

Also verified: tab switch → 5 playbook steps; sprint toggle → counter + `aria-checked`;
all 9 sections populated (no empty boxes); served over HTTP 200 for every asset;
37 KB HTML (12.3 KB gzipped), zero external requests except the canonical URL.
