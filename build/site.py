import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from data import DATA

ROOT = pathlib.Path(__file__).resolve().parent.parent
D_JSON = json.dumps(DATA, ensure_ascii=False)

HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>How to Get Rich in 2026 — 3 Skills That Print Money</title>

<meta name="description" content="Three skills that quietly dominate the next decade: Creator, Clipper, Vibe Coder. A living playbook — learn, monetize, combine.">
<meta name="author" content="@0xdierich">
<link rel="canonical" href="https://howtogetrich.now/">
<meta name="theme-color" content="#0A0A0A">

<meta property="og:type" content="website">
<meta property="og:site_name" content="howtogetrich.now">
<meta property="og:url" content="https://howtogetrich.now/">
<meta property="og:title" content="How to Get Rich in 2026 — 3 Skills That Print Money">
<meta property="og:description" content="Creator. Clipper. Vibe Coder. Master one and you stay relevant. Combine all three and you become dangerous.">
<meta property="og:image" content="https://howtogetrich.now/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="How to get rich in 2026 — three skills that print money">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@0xdierich">
<meta name="twitter:creator" content="@0xdierich">
<meta name="twitter:title" content="How to Get Rich in 2026 — 3 Skills That Print Money">
<meta name="twitter:description" content="Creator. Clipper. Vibe Coder. Master one and you stay relevant. Combine all three and you become dangerous.">
<meta name="twitter:image" content="https://howtogetrich.now/og.png">

<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%230A0A0A'/%3E%3Ctext x='16' y='23' font-family='Segoe UI,Arial' font-size='19' font-weight='900' fill='%23F2FF3B' text-anchor='middle'%3E%24%3C/text%3E%3C/svg%3E">

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How to Get Rich in 2026: 3 Skills That Make You Rich",
  "description": "Creator, Clipper, Vibe Coder — a living playbook for the next era of the economy.",
  "author": {"@type": "Person", "name": "@0xdierich", "url": "https://x.com/0xdierich"},
  "publisher": {"@type": "Organization", "name": "howtogetrich.now"},
  "mainEntityOfPage": "https://howtogetrich.now/",
  "dateModified": "2026-10-28"
}
</script>

<style>
:root{
  --bg:#0A0A0A;--fg:#FFF;--mut:#A2A2A2;--hot:#FF3B00;--cy:#00E5FF;--yel:#F2FF3B;--rule:#262626;
  --sans:"Segoe UI",Inter,-apple-system,BlinkMacSystemFont,system-ui,sans-serif;
  --mono:ui-monospace,"Cascadia Mono",Consolas,"SF Mono",monospace;
  --maxw:1180px;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;scroll-padding-top:96px;-webkit-text-size-adjust:100%}
body{background:var(--bg);color:var(--fg);font-family:var(--sans);line-height:1.5;overflow-x:hidden;
  -webkit-font-smoothing:antialiased;
  background-image:radial-gradient(900px 520px at 8% -6%,rgba(255,59,0,.20),transparent 70%),
                   radial-gradient(800px 460px at 102% 12%,rgba(0,229,255,.14),transparent 70%),
                   radial-gradient(700px 700px at 50% 118%,rgba(242,255,59,.06),transparent 70%);
  background-attachment:fixed}
a{color:inherit;text-decoration:none}
:focus-visible{outline:3px solid var(--yel);outline-offset:3px}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 22px}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
/* ── top bar ── */
.top{position:sticky;top:0;z-index:60;background:#0A0A0A;border-bottom:3px solid #fff}
.top .in{display:flex;align-items:center;justify-content:space-between;gap:14px;height:50px;
  font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase}
.top .in b{background:var(--yel);color:#000;padding:4px 8px;font-weight:700}
.top .in .mid{color:#8A8A8A;font-size:10px;letter-spacing:.18em}
.jump{display:flex;gap:0;overflow-x:auto;scrollbar-width:none;border-top:1px solid var(--rule);background:#080808}
.jump::-webkit-scrollbar{display:none}
.jump a{flex:0 0 auto;font-family:var(--mono);font-size:9.5px;letter-spacing:.14em;text-transform:uppercase;
  color:#7A7A7A;padding:14px 13px;border-right:1px solid #1A1A1A;transition:.15s;white-space:nowrap;
  display:flex;align-items:center;min-height:44px}
.jump a:hover,.jump a:focus-visible{color:var(--yel);background:#111}
.jump a.on{color:#000;background:var(--yel);font-weight:700}
.prog{height:3px;background:#1A1A1A}
.prog b{display:block;height:100%;background:var(--hot);width:0;will-change:width}
/* ── hero ── */
.hero{padding:58px 0 0}
.eyebrow{display:inline-block;font-family:var(--mono);font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;
  border:2px solid #fff;padding:6px 11px;margin-bottom:22px;background:#000}
h1{font-size:clamp(50px,10.4vw,146px);line-height:.82;letter-spacing:-.055em;font-weight:900;text-transform:uppercase}
h1 .o{color:#fff;font-weight:900}
@supports ((-webkit-text-stroke:2px #fff) or (text-stroke:2px #fff)){
  h1 .o{color:transparent;-webkit-text-stroke:2px #fff}
}
h1 .hot{color:var(--hot)}
.sub{margin-top:20px;font-size:clamp(18px,2.9vw,30px);font-weight:800;letter-spacing:-.02em;text-transform:uppercase;line-height:1.15}
.sub u{text-decoration:none;background:var(--yel);color:#000;padding:0 8px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.lead{margin-top:20px;max-width:58ch;font-size:16.5px;line-height:1.6;color:#C6C6C6}
.hero-cta{margin-top:26px;display:flex;gap:12px;flex-wrap:wrap;align-items:center}
.btn{display:inline-flex;align-items:center;gap:9px;font-family:var(--mono);font-size:11.5px;font-weight:700;
  letter-spacing:.14em;text-transform:uppercase;background:var(--yel);color:#000;border:3px solid #000;
  padding:12px 17px;box-shadow:6px 6px 0 #fff;transition:.13s}
.btn:hover{transform:translate(-3px,-3px);box-shadow:9px 9px 0 var(--hot)}
.btn.ghost{background:#000;color:#fff;border-color:#fff;box-shadow:6px 6px 0 #333}
.btn.ghost:hover{box-shadow:9px 9px 0 var(--cy)}
.stats{display:flex;flex-wrap:wrap;margin-top:32px;border:3px solid #fff;background:#000}
.stats div{flex:1 1 150px;padding:14px 16px;border-right:3px solid #fff}
.stats div:last-child{border-right:0}
.stats b{display:block;font-family:var(--mono);font-size:clamp(24px,2.9vw,32px);color:var(--cy);letter-spacing:-.02em}
.stats span{font-family:var(--mono);font-size:9.5px;text-transform:uppercase;letter-spacing:.11em;color:#9A9A9A;display:block;margin-top:3px}
/* ── marquee ── */
.mq{margin-top:38px;background:var(--hot);color:#000;border-top:3px solid #000;border-bottom:3px solid #000;
  overflow:hidden;transform:rotate(-1.1deg);position:relative;z-index:2}
.mq div{display:flex;gap:26px;white-space:nowrap;padding:8px 0;font-family:var(--mono);font-size:12.5px;
  font-weight:700;letter-spacing:.14em;text-transform:uppercase;animation:mv 38s linear infinite}
.mq.alt{background:var(--cy);transform:rotate(.9deg)}
.mq.dark{background:#000;color:var(--yel);border-color:#fff}
@keyframes mv{to{transform:translateX(-50%)}}
/* ── sections ── */
.blk{padding:56px 0 48px;border-bottom:1px solid #1E1E1E}
.kick{display:flex;align-items:center;gap:11px;font-family:var(--mono);font-size:10.5px;letter-spacing:.2em;
  text-transform:uppercase;color:var(--yel);margin-bottom:15px}
.kick i{display:inline-block;width:30px;height:3px;background:var(--yel)}
h2{font-size:clamp(28px,4.5vw,52px);line-height:.98;letter-spacing:-.04em;font-weight:900;text-transform:uppercase;max-width:24ch}
h2 em{font-style:normal;color:var(--yel)}
.note{margin-top:14px;font-family:var(--mono);font-size:12.5px;color:#9A9A9A;max-width:66ch;line-height:1.7}
/* timeline */
.tl{margin-top:30px}
.tl .row{display:grid;grid-template-columns:112px 1fr;gap:20px;padding:16px 0;border-top:2px solid #242424}
.tl .row:first-child{border-top:3px solid #fff}
.tl .y{font-family:var(--mono);font-size:clamp(19px,2.5vw,26px);font-weight:700;color:var(--hot)}
.tl .k{font-family:var(--mono);font-size:11px;letter-spacing:.16em;color:var(--yel);margin-bottom:5px}
.tl p{font-size:15px;line-height:1.55;color:#C6C6C6;max-width:58ch}
/* cards */
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(248px,1fr));gap:16px;margin-top:30px}
.card{background:#0D0D0D;border:3px solid #fff;padding:20px;cursor:pointer;transition:.14s;
  box-shadow:8px 8px 0 var(--hot);position:relative;text-align:left;color:#fff;font-family:inherit;width:100%}
.card:nth-child(2){box-shadow:8px 8px 0 var(--cy)}
.card:nth-child(3){box-shadow:8px 8px 0 var(--yel)}
.card:hover{transform:translate(-4px,-4px);box-shadow:13px 13px 0 var(--hot)}
.card .role{font-family:var(--mono);font-size:9.5px;letter-spacing:.2em;background:#fff;color:#000;display:inline-block;padding:3px 7px;font-weight:700}
.card h3{margin:13px 0 7px;font-size:21px;line-height:1.08;letter-spacing:-.03em;text-transform:uppercase;font-weight:900}
.card p{font-size:13.5px;color:#B8B8B8;min-height:52px;line-height:1.5}
.card .meta{margin-top:13px;border-top:2px solid #262626;padding-top:9px;font-family:var(--mono);font-size:9.5px;
  letter-spacing:.09em;text-transform:uppercase;color:#8A8A8A;display:grid;gap:4px}
.card .arrow{position:absolute;top:12px;right:12px;font-size:19px;color:#3A3A3A;transition:.15s}
.card:hover .arrow{color:var(--yel);transform:translateX(3px)}
/* tabs */
.tabs{display:flex;flex-wrap:wrap;gap:9px;margin:28px 0 24px}
.tabs button{font-family:var(--mono);font-size:11px;letter-spacing:.13em;text-transform:uppercase;font-weight:700;
  background:#000;color:#fff;border:3px solid #fff;padding:13px 14px;min-height:44px;cursor:pointer;transition:.13s;box-shadow:4px 4px 0 #333}
.tabs button:hover{transform:translate(-2px,-2px);box-shadow:6px 6px 0 #555}
.tabs button.on{background:var(--yel);color:#000;box-shadow:4px 4px 0 var(--hot)}
.phead{margin-bottom:4px}
.ptitle{font-size:clamp(24px,3.6vw,38px);font-weight:900;letter-spacing:-.04em;text-transform:uppercase;line-height:.98}
.ptag{font-family:var(--mono);font-size:12px;color:var(--cy);letter-spacing:.05em;margin-top:4px}
.pgrid{display:grid;grid-template-columns:1.05fr .95fr;gap:32px;margin-top:20px}
.pbody{font-size:15px;line-height:1.62;color:#C6C6C6;margin-bottom:22px;max-width:60ch}
.plabel{font-family:var(--mono);font-size:9.5px;letter-spacing:.2em;text-transform:uppercase;color:#7A7A7A;
  margin-bottom:11px;border-left:3px solid var(--hot);padding-left:8px}
ol.pb{list-style:none;counter-reset:i;margin-bottom:22px}
ol.pb li{counter-increment:i;position:relative;padding-left:34px;margin-bottom:11px;font-size:14.5px;line-height:1.55;color:#D0D0D0}
ol.pb li::before{content:counter(i,decimal-leading-zero);position:absolute;left:0;top:0;font-family:var(--mono);
  font-size:10.5px;background:var(--hot);color:#000;width:24px;height:19px;line-height:19px;text-align:center;font-weight:700}
.chips{display:flex;flex-wrap:wrap;gap:7px;margin-bottom:22px}
.chips span{font-family:var(--mono);font-size:10.5px;border:2px solid #fff;padding:5px 9px;background:#111}
.money{border:3px solid #fff;background:#000;margin-bottom:22px}
.money .mr{display:flex;justify-content:space-between;gap:12px;padding:10px 13px;border-bottom:2px solid #1E1E1E;font-size:13px}
.money .mr:last-child{border-bottom:0}
.money .mr:nth-child(odd){background:#0E0E0E}
.money .mr span:last-child{font-family:var(--mono);font-size:11px;color:var(--yel);white-space:nowrap;font-weight:700}
.proof{border:3px solid var(--yel);background:#000;padding:18px;box-shadow:7px 7px 0 rgba(242,255,59,.2)}
.proof p{font-size:14.5px;line-height:1.55;color:#EFEFEF}
.proof cite{display:block;margin-top:10px;font-family:var(--mono);font-size:10px;color:var(--cy);font-style:normal;letter-spacing:.05em}
.pm{display:flex;gap:24px;margin-top:18px;flex-wrap:wrap}
.pm div b{display:block;font-family:var(--mono);font-size:21px;color:var(--cy)}
.pm div span{font-family:var(--mono);font-size:9px;letter-spacing:.1em;text-transform:uppercase;color:#7A7A7A}
/* pipeline */
.pipe{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-top:28px}
.pcard{border:3px dashed #464646;padding:17px;background:#0C0C0C}
.pcard .top{display:flex;justify-content:space-between;font-family:var(--mono);font-size:9px;letter-spacing:.13em;color:#7A7A7A}
.pcard .top b{color:var(--hot)}
.pcard h4{margin:11px 0 5px;font-size:14px;font-family:var(--mono);letter-spacing:.06em;color:var(--yel)}
.pcard p{font-size:12.5px;color:#A6A6A6;line-height:1.5}
/* combo */
.steps{list-style:none;counter-reset:c;margin-top:28px;display:grid;gap:10px}
.steps li{counter-increment:c;display:grid;grid-template-columns:50px 1fr;gap:16px;align-items:center;
  font-size:clamp(14.5px,2vw,19px);font-weight:700;letter-spacing:-.02em;line-height:1.35;padding:13px 15px;
  background:#0E0E0E;border-left:5px solid var(--hot)}
.steps li:nth-child(2){border-left-color:var(--cy)}
.steps li:nth-child(3){border-left-color:var(--yel)}
.steps li:nth-child(4){border-left-color:#fff}
.steps li:nth-child(5){border-left-color:var(--hot)}
.steps li::before{content:counter(c,decimal-leading-zero);font-family:var(--mono);font-size:14px;color:#6A6A6A}
.bigline{margin-top:24px;font-size:clamp(18px,2.9vw,30px);font-weight:900;letter-spacing:-.03em;text-transform:uppercase;line-height:1.14}
.bigline b{color:var(--yel)}
.result{margin-top:18px;display:inline-block;background:var(--hot);color:#000;font-family:var(--mono);font-size:12px;
  font-weight:700;letter-spacing:.05em;text-transform:uppercase;padding:10px 14px;transform:rotate(-.7deg);line-height:1.4}
/* numbers */
.nums{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));margin-top:28px;border:3px solid #fff;background:#000}
.nums div{padding:20px 14px;border-right:3px solid #fff}
.nums div:last-child{border-right:0}
.nums b{display:block;font-family:var(--mono);font-size:clamp(22px,3.1vw,34px);color:var(--yel);letter-spacing:-.03em}
.nums span{font-family:var(--mono);font-size:9px;letter-spacing:.09em;text-transform:uppercase;color:#8A8A8A;display:block;margin-top:2px}
.ledger{margin-top:20px;border:3px solid #1E1E1E;background:#0B0B0B;padding:14px}
.ledger .lh{font-family:var(--mono);font-size:9.5px;letter-spacing:.18em;text-transform:uppercase;color:var(--yel);margin-bottom:9px}
.ledger p{font-family:var(--mono);font-size:11.5px;color:#A2A2A2;line-height:2;letter-spacing:.01em}
.ledger p b{color:#fff;font-weight:600}
/* sprint */
.sp{list-style:none;margin-top:26px;border-top:3px solid #fff}
.sp li{display:flex;gap:14px;align-items:flex-start;padding:14px 6px;border-bottom:1px solid #242424;cursor:pointer;
  font-size:14.5px;line-height:1.55;transition:.12s;text-align:left;width:100%;background:none;border-left:0;border-right:0;border-top:0;color:#fff;font-family:inherit}
.sp li:hover{background:#101010}
.sp li:focus-visible{outline:3px solid var(--yel);outline-offset:-3px}
.sp .box{width:24px;height:24px;border:3px solid #fff;flex:0 0 auto;position:relative;transition:.12s;margin-top:1px}
.sp li.done .box{background:var(--yel);border-color:var(--yel)}
.sp li.done .box::after{content:"";position:absolute;left:6px;top:2px;width:6px;height:11px;
  border-right:3px solid #000;border-bottom:3px solid #000;transform:rotate(40deg)}
.sp li.done .txt{color:#5A5A5A;text-decoration:line-through}
.sp .d{font-family:var(--mono);font-size:10.5px;color:#6A6A6A;margin-right:7px}
.spbar{margin-top:18px;font-family:var(--mono);font-size:11px;letter-spacing:.14em;color:#8A8A8A}
.spbar i{display:block;height:8px;background:#1E1E1E;border:2px solid #333;margin-top:8px;position:relative}
.spbar i b{position:absolute;inset:0 auto 0 0;background:var(--yel);width:0;transition:.25s}
/* warning */
.warn{background:var(--yel);color:#000;padding:64px 0 58px;border-top:3px solid #000;border-bottom:3px solid #000}
.warn .kick{color:#000}.warn .kick i{background:#000}
.warn h2{color:#000;font-size:clamp(36px,7.6vw,92px);line-height:.86;max-width:16ch}
.warn p{margin-top:18px;max-width:58ch;font-size:15.5px;font-weight:600;color:#141414;line-height:1.6}
.warn .rule{margin-top:26px;font-family:var(--mono);font-weight:700;font-size:13px;letter-spacing:.14em;
  text-transform:uppercase;background:#000;color:var(--yel);display:inline-block;padding:10px 14px}
footer{padding:26px 0 54px;font-family:var(--mono);font-size:10.5px;letter-spacing:.09em;text-transform:uppercase;
  color:#7A7A7A;display:flex;justify-content:space-between;gap:14px;flex-wrap:wrap;align-items:center}
footer a{color:var(--yel);display:inline-flex;align-items:center;min-height:44px}
footer a:hover{text-decoration:underline}
.fnav{display:flex;gap:16px;flex-wrap:wrap;align-items:center}
/* reveal */
.rv{opacity:0;transform:translateY(16px);transition:opacity .5s ease,transform .5s ease}
.rv.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  .rv{opacity:1;transform:none;transition:none}
  .mq div{animation:none}
  *{transition-duration:.01ms!important;animation-duration:.01ms!important}
}
@media(max-width:860px){
  .pgrid{grid-template-columns:1fr;gap:24px}
  .tl .row{grid-template-columns:64px 1fr;gap:13px}
  .tl p{font-size:14px}
  .stats div{flex:1 1 100%;border-right:0;border-bottom:3px solid #fff}
  .stats div:last-child{border-bottom:0}
  h1{font-size:clamp(42px,12.6vw,74px)}
  .hero{padding-top:40px}
  .blk{padding:42px 0 36px}
  .nums{grid-template-columns:1fr 1fr}
  .nums div:nth-child(2){border-right:0}
  .nums div:nth-child(3),.nums div:nth-child(4){border-top:3px solid #fff}
  .nums div:nth-child(3){border-right:3px solid #fff}
  .btn{width:100%;justify-content:center}
  footer{flex-direction:column;align-items:flex-start;gap:10px}
}
@media(max-width:430px){
  .wrap{padding:0 16px}
  .top .in .mid{display:none}
  .steps li{grid-template-columns:38px 1fr;gap:11px;padding:11px 12px}
  .money .mr{font-size:12px;padding:9px 10px}
  .money .mr span:last-child{font-size:10px}
}
</style>
</head>
<body>

<a class="sr" href="#shift">Skip to content</a>

<header class="top">
  <div class="wrap in">
    <span>HOWTOGETRICH<b>.NOW</b></span>
    <span class="mid">3 SKILLS · 1 FLYWHEEL</span>
    <span>2026</span>
  </div>
  <nav class="jump wrap" id="jump" aria-label="Sections"></nav>
  <div class="prog"><b id="prog"></b></div>
</header>

<main class="wrap" id="app"></main>

<section class="warn" id="warn">
  <div class="wrap" id="warnbody"></div>
</section>

<div class="wrap"><footer id="foot"></footer></div>

<script>
const D = __DATA__;
const esc = s => String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
const $ = s => document.querySelector(s);

const NAV = [
  ["shift","01 SHIFT"],["three","02 THREE"],["paths","03 PATHS"],
  ["pipeline","04 PATCHES"],["combo","05 COMBO"],["proof","06 RECEIPTS"],["sprint","07 SPRINT"]
];
$("#jump").innerHTML = NAV.map(([id,l])=>`<a href="#${id}" data-id="${id}">${l}</a>`).join("");

let active = D.paths[0].id;

function pathHTML(p){
  return `<div class="rv in">
    <div class="phead"><div class="ptitle">${esc(p.name)}</div><div class="ptag">${esc(p.tagline)}</div></div>
    <div class="pgrid">
      <div>
        <p class="pbody">${esc(p.why)}</p>
        <div class="plabel">The playbook</div>
        <ol class="pb">${p.playbook.map(x=>`<li>${esc(x)}</li>`).join("")}</ol>
        <div class="pm">${p.metrics.map(m=>`<div><b>${esc(m[0])}</b><span>${esc(m[1])}</span></div>`).join("")}</div>
      </div>
      <div>
        <div class="plabel">Starter stack</div>
        <div class="chips">${p.stack.map(s=>`<span>${esc(s)}</span>`).join("")}</div>
        <div class="plabel">How the money works</div>
        <div class="money">${p.money.map(m=>`<div class="mr"><span>${esc(m[0])}</span><span>${esc(m[1])}</span></div>`).join("")}</div>
        <div class="plabel">Receipt</div>
        <div class="proof"><p>&ldquo;${esc(p.proof[0])}&rdquo;</p><cite>&mdash; ${esc(p.proof[1])}</cite></div>
      </div>
    </div>
  </div>`;
}

$("#app").innerHTML = `
<section class="hero" id="top">
  <div class="eyebrow">${esc(D.hero.eyebrow)}</div>
  <h1>${esc(D.hero.l1)}<br><span class="hot">${esc(D.hero.l2a)}</span> <span class="o">${esc(D.hero.l2b)}</span></h1>
  <p class="sub"><u>${esc(D.hero.sub)}</u></p>
  <p class="lead">${esc(D.hero.lead)}</p>
  <div class="hero-cta">
    <a class="btn" href="#paths">Pick your skill &darr;</a>
    <a class="btn ghost" href="${esc(D.x_url)}" target="_blank" rel="noopener me">Follow @0xdierich &nearr;</a>
  </div>
  <div class="stats">${D.hero.stats.map(s=>`<div><b>${esc(s[0])}</b><span>${esc(s[1])}</span></div>`).join("")}</div>
</section>

<div class="mq"><div>${Array(8).fill("MASTER ONE &rarr; STAY RELEVANT").join(" <span>&middot;</span> ")}</div></div>

<section class="blk" id="shift">
  <div class="kick"><i></i>${esc(D.shift.num)} / ${esc(D.shift.kicker)}</div>
  <h2>${esc(D.shift.title)}</h2>
  <p class="note">${esc(D.shift.body)}</p>
  <div class="tl">${D.shift.timeline.map(r=>`<div class="row rv"><div class="y">${esc(r[0])}</div><div><div class="k">${esc(r[1])}</div><p>${esc(r[2])}</p></div></div>`).join("")}</div>
</section>

<section class="blk" id="three">
  <div class="kick"><i></i>${esc(D.three.num)} / ${esc(D.three.kicker)}</div>
  <h2>${esc(D.three.title)}</h2>
  <p class="note">${esc(D.three.note)}</p>
  <div class="cards">
    ${D.three.cards.map((c,i)=>`<button class="card rv" data-go="${D.paths[i].id}" aria-label="Read the ${esc(c[0])} path">
      <span class="arrow" aria-hidden="true">&nearr;</span>
      <span class="role">${esc(c[0])}</span><h3>${esc(c[1])}</h3><p>${esc(c[2])}</p>
      <span class="meta"><span>${esc(c[3])}</span><span>${esc(c[4])}</span><span>first $ &rarr; ${esc(c[5])}</span></span></button>`).join("")}
  </div>
</section>

<div class="mq alt"><div>${Array(8).fill("CLIP IT &middot; SHIP IT &middot; POST IT").join(" <span>&middot;</span> ")}</div></div>

<section class="blk" id="paths">
  <div class="kick"><i></i>03 / THE PATHS</div>
  <h2>Three roads. <em>One destination.</em></h2>
  <p class="note">Pick your entry point. Then read the rest anyway.</p>
  <div class="tabs" id="tabs" role="tablist" aria-label="Skill paths">
    ${D.paths.map(p=>`<button role="tab" data-id="${p.id}" aria-selected="${p.id===active}" class="${p.id===active?"on":""}">${p.n} ${esc(p.name.replace("THE ",""))}</button>`).join("")}
  </div>
  <div id="pathbody" role="tabpanel">${pathHTML(D.paths[0])}</div>
</section>

<section class="blk" id="pipeline">
  <div class="kick"><i></i>${esc(D.pipeline.num)} / ${esc(D.pipeline.kicker)}</div>
  <h2>${esc(D.pipeline.title)}</h2>
  <p class="note">${esc(D.pipeline.note)}</p>
  <div class="pipe">${D.pipeline.items.map(i=>`<div class="pcard rv"><div class="top"><span>${esc(i[0])}</span><b>${esc(i[2])}</b></div><h4>${esc(i[1])}</h4><p>${esc(i[3])}</p></div>`).join("")}</div>
</section>

<div class="mq dark"><div>${Array(8).fill("MASTER ONE AND YOU STAY RELEVANT").join(" <span>&middot;</span> ")}</div></div>

<section class="blk" id="combo">
  <div class="kick"><i></i>${esc(D.combo.num)} / ${esc(D.combo.kicker)}</div>
  <h2>${esc(D.combo.title)}</h2>
  <ol class="steps">${D.combo.steps.map(s=>`<li>${esc(s)}</li>`).join("")}</ol>
  <p class="bigline">${esc(D.combo.line).replace("idea &rarr; product &rarr; distribution","<b>IDEA &rarr; PRODUCT &rarr; DISTRIBUTION</b>").replace("idea → product → distribution","<b>IDEA → PRODUCT → DISTRIBUTION</b>")}</p>
  <div class="result">${esc(D.combo.result)}</div>
</section>

<section class="blk" id="proof">
  <div class="kick"><i></i>${esc(D.proof.num)} / ${esc(D.proof.kicker)}</div>
  <h2>${esc(D.proof.title)}</h2>
  <div class="nums">${D.proof.numbers.map(n=>`<div><b>${esc(n[0])}</b><span>${esc(n[1])}</span></div>`).join("")}</div>
  <div class="ledger"><div class="lh">${esc(D.proof.note_label)}</div><p>${esc(D.proof.note)}</p></div>
</section>

<section class="blk" id="sprint">
  <div class="kick"><i></i>${esc(D.sprint.num)} / ${esc(D.sprint.kicker)}</div>
  <h2>${esc(D.sprint.title)}</h2>
  <p class="note">Tick them off. It remembers.</p>
  <ul class="sp" id="sp">${D.sprint.items.map((s,i)=>`<li data-i="${i}" role="checkbox" aria-checked="false" tabindex="0"><span class="box" aria-hidden="true"></span><span class="txt"><span class="d">D${i+1}</span>${esc(s)}</span></li>`).join("")}</ul>
  <div class="spbar"><span id="sptxt">0 / 7 COMPLETE</span><i><b id="spfill"></b></i></div>
</section>
`;

$("#warnbody").innerHTML = `
  <div class="kick"><i></i>${esc(D.warning.num)} / ${esc(D.warning.kicker)}</div>
  <h2>${esc(D.warning.title)}</h2>
  <p>${esc(D.warning.body)}</p>
  <p style="margin-top:12px">${esc(D.warning.close)}</p>
  <div class="rule">${esc(D.warning.rule)}</div>`;

$("#foot").innerHTML = `
  <span>${esc(D.footer.brand)} &mdash; ${esc(D.footer.note)}</span>
  <span class="fnav">
    <a href="${esc(D.x_url)}" target="_blank" rel="noopener me">X / Twitter &nearr;</a>
    <a href="#top">Back to top &uarr;</a>
  </span>
  <span>${esc(D.footer.domain)}</span>`;

// ── tabs
const tabs = $("#tabs");
function setPath(id){
  active = id;
  tabs.querySelectorAll("button").forEach(x=>{
    const on = x.dataset.id===active;
    x.classList.toggle("on",on);
    x.setAttribute("aria-selected", on);
  });
  $("#pathbody").innerHTML = pathHTML(D.paths.find(p=>p.id===active));
}
tabs.addEventListener("click", e=>{
  const b = e.target.closest("button"); if(!b) return;
  setPath(b.dataset.id);
});
tabs.addEventListener("keydown", e=>{
  const btns = [...tabs.querySelectorAll("button")];
  const i = btns.indexOf(document.activeElement);
  if(i < 0) return;
  if(e.key==="ArrowRight"||e.key==="ArrowLeft"){
    e.preventDefault();
    const n = (i + (e.key==="ArrowRight"?1:-1) + btns.length) % btns.length;
    btns[n].focus(); setPath(btns[n].dataset.id);
  }
});
// ── cards
document.querySelectorAll(".card").forEach(c=>c.addEventListener("click",()=>{
  const id = c.dataset.go;
  document.getElementById("paths").scrollIntoView({behavior:"smooth"});
  setTimeout(()=>setPath(id), 400);
}));
// ── sprint
const KEY = "htgr_sprint_v1";
let done = [];
try{ done = JSON.parse(localStorage.getItem(KEY) || "[]"); }catch(e){ done = []; }
const items = [...document.querySelectorAll("#sp li")];
function renderSprint(){
  let n = 0;
  items.forEach(li=>{
    const on = done.includes(+li.dataset.i);
    li.classList.toggle("done", on);
    li.setAttribute("aria-checked", on);
    if(on) n++;
  });
  $("#sptxt").textContent = `${n} / ${items.length} COMPLETE`;
  $("#spfill").style.width = (n/items.length*100) + "%";
}
function toggleSprint(li){
  const i = +li.dataset.i;
  done = done.includes(i) ? done.filter(x=>x!==i) : [...done, i];
  try{ localStorage.setItem(KEY, JSON.stringify(done)); }catch(e){}
  renderSprint();
}
items.forEach(li=>{
  li.addEventListener("click", ()=>toggleSprint(li));
  li.addEventListener("keydown", e=>{
    if(e.key===" "||e.key==="Enter"){ e.preventDefault(); toggleSprint(li); }
  });
});
renderSprint();
// ── progress
const prog = $("#prog");
addEventListener("scroll", ()=>{
  const h = document.documentElement;
  const max = h.scrollHeight - h.clientHeight;
  prog.style.width = (max>0 ? h.scrollTop/max*100 : 0) + "%";
}, {passive:true});
// ── reveal
const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
if(!reduce && "IntersectionObserver" in window){
  const io = new IntersectionObserver(es=>es.forEach(e=>{
    if(e.isIntersecting){ e.target.classList.add("in"); io.unobserve(e.target); }
  }), {threshold:.1, rootMargin:"0px 0px -40px 0px"});
  document.querySelectorAll(".rv:not(.in)").forEach(e=>io.observe(e));
} else {
  document.querySelectorAll(".rv").forEach(e=>e.classList.add("in"));
}
// ── active nav
const links = [...document.querySelectorAll("#jump a")];
if("IntersectionObserver" in window){
  const nio = new IntersectionObserver(es=>es.forEach(e=>{
    if(e.isIntersecting){
      links.forEach(a=>a.classList.toggle("on", a.dataset.id===e.target.id));
    }
  }), {rootMargin:"-45% 0px -50% 0px"});
  NAV.forEach(([id])=>{ const s=document.getElementById(id); if(s) nio.observe(s); });
}
</script>
</body>
</html>
"""

html = HTML.replace("__DATA__", D_JSON)
(ROOT / "index.html").write_text(html, encoding="utf-8")
print("wrote index.html", round(len(html)/1024,1), "KB")

# ── OG image source
OG = """<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}
body{width:1200px;height:630px;background:#0A0A0A;color:#fff;overflow:hidden;position:relative;
  font-family:"Segoe UI",Inter,Arial,sans-serif;
  background-image:radial-gradient(700px 400px at 6% -8%,rgba(255,59,0,.30),transparent 70%),
                   radial-gradient(650px 380px at 104% 10%,rgba(0,229,255,.20),transparent 70%),
                   radial-gradient(600px 500px at 50% 118%,rgba(242,255,59,.10),transparent 70%)}
.pad{padding:56px 62px;height:100%;display:flex;flex-direction:column;justify-content:space-between}
.top{display:flex;justify-content:space-between;align-items:center;font-family:ui-monospace,Consolas,monospace;
  font-size:17px;letter-spacing:.2em;text-transform:uppercase;color:#9A9A9A}
.top b{background:#F2FF3B;color:#000;padding:6px 12px;letter-spacing:.16em}
h1{font-size:118px;line-height:.82;letter-spacing:-.055em;font-weight:900;text-transform:uppercase}
h1 .hot{color:#FF3B00}h1 .o{color:transparent;-webkit-text-stroke:2.5px #fff}
.sub{font-size:31px;font-weight:800;letter-spacing:-.02em;text-transform:uppercase;margin-top:16px}
.sub u{text-decoration:none;background:#F2FF3B;color:#000;padding:0 10px}
.row{display:flex;align-items:center;gap:16px;margin-top:26px}
.chip{font-family:ui-monospace,Consolas,monospace;font-size:19px;font-weight:700;letter-spacing:.1em;
  border:3px solid #fff;padding:9px 15px;text-transform:uppercase}
.chip.a{background:#FF3B00;border-color:#FF3B00;color:#000}
.chip.b{background:#00E5FF;border-color:#00E5FF;color:#000}
.chip.c{background:#F2FF3B;border-color:#F2FF3B;color:#000}
.foot{display:flex;justify-content:space-between;align-items:flex-end;font-family:ui-monospace,Consolas,monospace;
  font-size:20px;letter-spacing:.08em;color:#A2A2A2;border-top:3px solid #fff;padding-top:18px}
.foot b{color:#fff}
</style></head><body><div class="pad">
<div class="top"><span><b>HOWTOGETRICH.NOW</b></span><span>THE 2026 PLAYBOOK</span></div>
<div>
  <h1>HOW TO GET<br><span class="hot">RICH</span> <span class="o">IN 2026</span></h1>
  <div class="sub"><u>Three skills that print money.</u></div>
  <div class="row"><span class="chip a">01 CREATOR</span><span class="chip b">02 CLIPPER</span><span class="chip c">03 VIBE CODER</span></div>
</div>
<div class="foot"><span><b>@0xdierich</b> &mdash; master one, or stack all three</span><span>$7,161 PROVED</span></div>
</div></body></html>"""
(ROOT / "build" / "og.html").write_text(OG, encoding="utf-8")
print("wrote build/og.html")
