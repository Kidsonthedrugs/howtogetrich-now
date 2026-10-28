import pathlib, json

ROOT = pathlib.Path(r"C:/Users/EasyMoneySniper/howtogetrich")

README_A = """## Variant A — Terminal Noir

### Design stance
A trading terminal that happens to be a manifesto. Credibility first: if a
Bloomberg screen and a bootstrapper's Notion collided, this is the result.

### Key choices
- **Layout:** fixed left rail with numbered section index, single content column, hard 1px rules.
- **Typography:** 800-weight Segoe UI at 105px for the hero, monospace everywhere numbers live.
- **Color:** near-black `#08090A`, acid green `#B8FF3C` for money/numbers, hot orange for warnings.
- **Texture:** 1px scanline overlay across the whole viewport; 2px acid scroll progress bar.
- **Interaction:** sticky rail highlights the current section; cards jump into the path tabs; sprint checklist persists in localStorage.

### Trade-offs
- **Strong at:** authority, data density, screenshots that look good on X.
- **Weak at:** the scanlines + acid green read "crypto tool" and can feel cold to a non-crypto reader.

### Best for
- An audience that already lives on Crypto Twitter and respects receipts over vibes.
"""

README_B = """## Variant B — Neon Brutalist

### Design stance
Everything is a headline and everything is shouting. Built for scroll-stopping,
not for reading comfort.

### Key choices
- **Layout:** centered 1160px column, giant type, hard 3px white borders, offset box-shadows.
- **Typography:** 900-weight at up to 176px, tight tracking, uppercase throughout.
- **Color:** black + white with one hot orange, one cyan, one yellow. Rotated marquee bands separate sections.
- **Texture:** three large radial glows fixed behind the page.
- **Interaction:** stacked shadow cards that lift on hover; tab buttons that physically depress.

### Trade-offs
- **Strong at:** stopping power, viral screenshots, personality — nobody scrolls past this.
- **Weak at:** reading fatigue. 176px headlines mean fewer sections per screen, and the neon palette narrows the audience to a younger, crypto-native crowd.

### Best for
- A launch post that has to win the timeline in the first two seconds.
"""

README_C = """## Variant C — Quiet Editorial

### Design stance
A magazine feature, not a landing page. The argument is that this content is
worth reading, so the design gets out of the way and lets the writing carry it.

### Key choices
- **Layout:** 700px measure with a 168px sticky table of contents, 66px gutters.
- **Typography:** serif stack (Iowan/Palatino/Georgia) at 18.5px body, drop cap on the lead.
- **Color:** warm paper `#FBFAF7`, near-black ink, forest green `#2C4A3B` accent.
- **Texture:** hairlines only. No shadows, no glows, no depth.
- **Interaction:** contents rail tracks the current section; paths are rows, not cards.

### Trade-offs
- **Strong at:** trust, readability, long dwell time, printing cleanly.
- **Weak at:** low urgency. It does not feel like a "playbook", it feels like an essay — weaker for a 60-second mobile visit.

### Best for
- A reader who arrives from a newsletter, and for anyone who will judge the page by how it reads rather than how it flashes.
"""

for name, txt in [("001-terminal-noir", README_A), ("002-neon-brutalist", README_B), ("003-quiet-editorial", README_C)]:
    (ROOT / "sketches" / name / "README.md").write_text(txt, encoding="utf-8")
    print("wrote", name, "README")

# comparison page with live iframes
COMPARE = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><title>howtogetrich.now — 3 variants</title>
<style>
  *{box-sizing:border-box;margin:0;padding:0}
  body{background:#0B0B0C;color:#EAEAE6;font-family:"Segoe UI",system-ui,sans-serif;padding:22px}
  h1{font-size:15px;letter-spacing:.18em;text-transform:uppercase;color:#9A9A94;font-weight:600;margin-bottom:16px}
  h1 b{color:#fff}
  .grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
  .col{background:#111114;border:1px solid #26262B;border-radius:10px;overflow:hidden;display:flex;flex-direction:column;min-height:0}
  .hd{display:flex;align-items:center;justify-content:space-between;padding:10px 12px;border-bottom:1px solid #26262B;font-size:11.5px;letter-spacing:.1em;text-transform:uppercase}
  .hd .n{font-weight:600}
  .hd a{color:#8FA88F;font-size:10.5px;text-decoration:none;border:1px solid #2F3A2F;padding:3px 7px;border-radius:4px}
  .hd a:hover{background:#1B241B;color:#C6E0C6}
  iframe{width:100%;height:78vh;border:0;background:#000}
  .tag{font-size:10px;color:#6E6E76;padding:0 12px 10px;letter-spacing:.04em}
  .A .n{color:#B8FF3C}.B .n{color:#FF3B00}.C .n{color:#C9B98F}
  @media(max-width:1000px){.grid{grid-template-columns:1fr}iframe{height:70vh}}
</style></head><body>
<h1><b>howtogetrich.now</b> — three design stances, same content</h1>
<div class="grid">
  <div class="col A"><div class="hd"><span class="n">A · Terminal Noir</span><a href="sketches/001-terminal-noir/index.html" target="_blank">open ↗</a></div>
    <div class="tag">trading terminal · mono numbers · acid green</div>
    <iframe src="sketches/001-terminal-noir/index.html"></iframe></div>
  <div class="col B"><div class="hd"><span class="n">B · Neon Brutalist</span><a href="sketches/002-neon-brutalist/index.html" target="_blank">open ↗</a></div>
    <div class="tag">176px headlines · hard borders · rotated bands</div>
    <iframe src="sketches/002-neon-brutalist/index.html"></iframe></div>
  <div class="col C"><div class="hd"><span class="n">C · Quiet Editorial</span><a href="sketches/003-quiet-editorial/index.html" target="_blank">open ↗</a></div>
    <div class="tag">700px measure · serif · drop cap</div>
    <iframe src="sketches/003-quiet-editorial/index.html"></iframe></div>
</div>
</body></html>
"""
(ROOT / "compare.html").write_text(COMPARE, encoding="utf-8")
print("wrote compare.html")
