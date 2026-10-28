# Deploy — howtogetrich.now

Single static page. No build step at runtime. Everything in `deploy/` is what ships.

## What ships

```
deploy/
├── index.html     37 KB   the page (inline CSS + JS, zero dependencies)
├── og.png         162 KB  1200×630 social card
├── 404.html        1 KB
├── robots.txt
├── sitemap.xml
└── _headers              security + cache headers (Cloudflare Pages)
```

Total: ~200 KB, one HTML request, no JS framework, no fonts fetched at runtime
(system font stack only — the `preconnect` hints are inert leftovers and can be dropped).

## Cloudflare Pages — 5 steps

1. **Dash → Workers & Pages → Create → Pages → Upload assets.**
2. Project name: `howtogetrich` (or anything; the custom domain is what matters).
3. Drag the whole `deploy/` folder into the upload box. Deploy.
4. **Custom domains → Set up a domain →** enter `howtogetrich.now`.
5. Cloudflare prints a CNAME target (`<project>.pages.dev`). Add the CNAME at your
   registrar. If the domain's nameservers are already on Cloudflare, this is one click.

`.now` is a normal TLD for DNS purposes — no special handling needed.

## After deploy — verify these four things

| Check | How | Pass looks like |
|---|---|---|
| Page loads | open the domain | hero renders, no console errors |
| OG card | https://cards-dev.twitter.com/validator | 1200×630 image, title, description |
| Mobile | DevTools → 390px | one column, section nav scrolls sideways |
| Checklist persists | tick day 1, reload | still ticked |

## Regenerating the page

```bash
cd C:/Users/EasyMoneySniper/howtogetrich
python build/site.py       # DATA → index.html (+ build/og.html)
python build/package.py    # → deploy/
python build/verify.py     # desktop assertions
python build/verify_mobile.py   # 320–834px assertions
```

Content lives in `build/data.py`. Never edit `index.html` directly — it is generated.

## Adding a new skill path

1. Add a card to `DATA["three"]["cards"]` (same order as the path below).
2. Add the path object to `DATA["paths"]` with `id`, `n`, `name`, `tagline`,
   `metrics`, `why`, `playbook` (5 items), `stack` (5), `money` (5), `proof`.
3. Move its row in `DATA["pipeline"]["items"]` from `QUEUED` to `LIVE`.
4. Re-run `site.py` + `package.py`, redeploy.

Nothing else changes — tabs, nav, mobile rules all derive from array length.

## Before going public

- [ ] Replace `og.png` if the copy changes (it hardcodes the three skill names).
- [ ] Decide whether to keep the airdrop ledger public (it names 10 projects and dollar amounts).
- [ ] Confirm `@0xdierich` handles in the CTA and footer go to the right account.
- [ ] Add a `datePublished` to the JSON-LD if you want richer search results.
