# howtogetrich.now — build 3 MVP variants
# Single source of content (DATA) + three distinct design stances.
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent / "sketches"

DATA = {
  "brand": "@0xdierich",
  "domain": "howtogetrich.now",
  "ticker": [
    "$7,161 airdrops in 2025",
    "3 skills",
    "1 flywheel",
    "0 credentials needed",
    "2027 is the deadline",
    "$1,000 paid unsolicited",
  ],
  "hero": {
    "eyebrow": "THE 2026 PLAYBOOK — LIVING EDITION",
    "l1": "HOW TO GET",
    "l2": "RICH IN 2026",
    "sub": "Three skills that print money.",
    "lead": "The rules of the game are changing. What made you valuable yesterday won't make you relevant tomorrow. 2026 rewards one type of person: someone who can create, package and ship ideas faster than the market can absorb them.",
    "stats": [
      ["3", "skills that actually matter"],
      ["$7,161", "proved in 12 months"],
      ["2027", "the deadline"]
    ]
  },
  "shift": {
    "num": "01",
    "kicker": "THE SHIFT",
    "title": "Attention, speed and distribution now beat credentials, degrees and capital.",
    "body": "This isn't another Web3 trend piece. It's a survival guide for the next era of the economy. The three skills below will quietly dominate the next decade — and this page is the roadmap for learning, monetizing and compounding them.",
    "timeline": [
      ["2021", "LOST 95%", "My capital disappeared in the crash. A degree wouldn't have saved me. Speed would have."],
      ["2025", "ACCELERATE", "InfoFi, airdrops, short-form video and AI tooling collapsed the cost of going from zero to paid."],
      ["2026", "ACQUIRE", "Influence, attention and shipping speed stop being advantages and become the price of entry."],
      ["2027", "OBSOLETE", "If you can't create content, capture attention or build products, you're professionally obsolete in most fields."]
    ]
  },
  "three": {
    "num": "02",
    "kicker": "THE THREE",
    "title": "Pick one. Then stack them.",
    "note": "Master one and you stay relevant. Combine all three and you become dangerous.",
    "cards": [
      ["CREATOR", "Influence is the new currency.", "You turn a voice and a niche into trust, and trust into income.", "owns → influence", "hard to start · easy to compound", "1–3 months"],
      ["CLIPPER", "Whoever controls attention controls the market.", "You cut the noise into 45 seconds nobody can scroll past.", "owns → attention", "easiest entry point", "days"],
      ["VIBE CODER", "Ship at the speed of culture.", "You build the tool the timeline keeps complaining about.", "owns → efficiency", "medium · highest ceiling", "1 weekend"]
    ]
  },
  "paths": [
    {
      "id": "creator",
      "n": "01",
      "name": "THE CREATOR",
      "tagline": "Influence is the new currency.",
      "metrics": [["6 months", "stranger → paid"], ["$7,000+", "via InfoFi"]],
      "why": "The creator economy stopped being a niche. Ronaldo runs YouTube like a business channel. MrBeast built a nine-figure empire out of thumbnails and retention curves. @KaitoAI became a unicorn selling analysis of Crypto Twitter — it invented a category, InfoFi, and disrupted the agencies that used to own that data. Power is shifting from opaque institutions to transparent, value-adding individuals.",
      "playbook": [
        "Pick a niche where curiosity meets pain: education, onchain analysis, teardowns, building in public.",
        "Hold one filter: if it doesn't save time, make money or reduce confusion, it won't scale.",
        "Use AI as a private tutor, research assistant and writing amplifier. It's the only unfair advantage that's still cheap.",
        "Layer high-signal inputs — builders who ship, not theorists who comment.",
        "Post the work, not the opinion. Proof compounds faster than takes."
      ],
      "stack": ["Frontier AI model as tutor", "X + long-form", "Notion / Obsidian", "Kaito mindshare", "YouTube"],
      "money": [
        ["Paid collaborations", "$300–$3k / post"],
        ["Sponsored content", "$500–$5k"],
        ["Advisory seats", "retainer"],
        ["InfoFi campaigns", "$200–$5k"],
        ["Ambassador programs", "equity + tokens"]
      ],
      "proof": ["I was a complete newcomer in Q1 2025. Less than six months of staying visible and shipping value in public unlocked $7,000+ through InfoFi.", "@0xdierich"]
    },
    {
      "id": "clipper",
      "n": "02",
      "name": "THE CLIPPER",
      "tagline": "Whoever controls attention controls the market.",
      "metrics": [["45s", "the only window"], ["$1,000", "paid, unsolicited"]],
      "why": "In an economy of infinite content, attention is the scarcest resource. The battle is no longer won by long-form writing — it's won in under sixty seconds. TikTok, Reels and X all re-engineered their algorithms to reward whoever can hold a stranger's eyes. A clipper is not a video editor. A clipper is a storyteller with a stopwatch.",
      "playbook": [
        "Learn CapCut. Then forget it — psychology is the edge, not the tool.",
        "Master three levers: clickbait earns the click, ragebait earns the reaction, retention earns the watch.",
        "Target the gap Web3 has: protocol explainers, cinematic launches, AMAs turned into moments, memes that encode alpha.",
        "Ship unsolicited. Nobody hires a portfolio they've never seen.",
        "Post daily for thirty days. Volume is the tuition."
      ],
      "stack": ["CapCut / Premiere", "Opus Clip", "ElevenLabs", "AI b-roll", "X + Shorts + Reels"],
      "money": [
        ["Web3 bounties", "$1k–$5k / campaign"],
        ["Freelance retainers", "$1k–$3k / mo"],
        ["Full-time media roles", "salary"],
        ["Launch packages", "$2k–$10k"],
        ["Rev-share on virals", "uncapped"]
      ],
      "proof": ["A community member sent unsolicited, high-quality clips to Cerebro. They replied with $1,000 in USDC — without being asked. Skill plus initiative beats resumes.", "@Incenzee → @cerebro_hq"]
    },
    {
      "id": "coder",
      "n": "03",
      "name": "THE VIBE CODER",
      "tagline": "Ship at the speed of culture.",
      "metrics": [["1 weekend", "idea → live"], ["∞", "leverage per tool"]],
      "why": "AI. DeFi. Prediction markets. Stablecoins. All powerful narratives — but the real unlock is the ability to ship tools at the speed of culture. Vibe coding isn't about perfect architecture, it's about timing: see a trend, feel a need, ship something useful, iterate in public. @gomtu_xyz shipped a Kaito tracker because people asked for rankings outside the top 100. Simple idea. Real demand. Massive leverage.",
      "playbook": [
        "See a trend, feel a need, ship something useful, iterate in public — in that order.",
        "Start with no-code, browser extensions, Dune dashboards, single-purpose SaaS utilities.",
        "One job per tool. If it needs a tutorial, it's too big.",
        "Let agents write the code. You own the taste and the timing.",
        "Ship on a weekend. Distribution decides the rest."
      ],
      "stack": ["Cursor / Claude Code", "Next.js + Vercel", "Dune", "Supabase", "Chrome extensions"],
      "money": [
        ["Airdrops & points", "$500–$10k"],
        ["Partnerships", "retainer"],
        ["Promotion deals", "$1k–$5k"],
        ["Tool bundles", "recurring"],
        ["Data access", "licensing"]
      ],
      "proof": ["Rankings outside of TOP 100? You asked, I ship. Utility creates gravity — the app isn't the business, the ecosystem around it is.", "@gomtu_xyz"]
    }
  ],
  "pipeline": {
    "num": "03",
    "kicker": "PATCH LOG",
    "title": "This playbook grows. New paths land here as they're proven.",
    "note": "Nothing is added until someone has actually been paid for it.",
    "items": [
      ["PATCH 01", "AGENT OPERATOR", "IN PROGRESS", "Run fleets of agents that execute work, not chat about it."],
      ["PATCH 02", "ONCHAIN ANALYST", "QUEUED", "Turn raw chain data into a paid, recurring newsletter."],
      ["PATCH 03", "INFOFI PLAYER", "QUEUED", "Treat mindshare as an asset class and trade it."]
    ]
  },
  "combo": {
    "num": "04",
    "kicker": "THE COMBO",
    "title": "Alone they're skills. Together they're an engine.",
    "steps": [
      "As a Creator, you spot a gap in the market.",
      "As a Vibe Coder, you ship the fix in a weekend.",
      "As a Clipper, you cut the demo into twelve clips that sell themselves.",
      "Attention becomes trust. Trust becomes money.",
      "Then you repeat — and the flywheel compounds."
    ],
    "line": "You now control the entire value chain: idea → product → distribution.",
    "result": "Master one and you stay relevant. Combine all three and you become dangerous."
  },
  "proof": {
    "num": "05",
    "kicker": "RECEIPTS",
    "title": "Numbers, not narratives.",
    "numbers": [["$7,161", "2025 airdrop total"], ["$1,000", "paid, unsolicited"], ["6 mo", "stranger → paid"], ["95%", "lost in 2021"]],
    "note": "2025 airdrops: Newton $1,795 · Avantis $2,450 · TAC $1,068 · Tanssi $586 · Turtle $330 · Huma $261 · Multipli $219 · An0ma $202 · Anichess $178 · Infinit $72."
  },
  "sprint": {
    "num": "06",
    "kicker": "7-DAY SPRINT",
    "title": "The resources are available. Your move takes a week.",
    "items": [
      "Pick one niche and write the single sentence describing who you help.",
      "Post one piece built on that sentence. No warm-up posts.",
      "Clip the best forty seconds of your own post and publish it.",
      "Ask the timeline what tool it wants. Count the repeats.",
      "Build the smallest version tonight. Ship it ugly.",
      "Cut a thirty-second demo and send it to the ten people who asked.",
      "Write what worked. Run it again next week."
    ]
  },
  "warning": {
    "num": "07",
    "kicker": "FINAL WARNING",
    "title": "Don't get left behind.",
    "body": "2025 was the year to accelerate. 2026 is the year you must acquire these skills to keep up. By 2027, if you don't understand the dynamics of creating content, capturing attention and rapidly building products, you will be professionally obsolete in many fields.",
    "close": "The demand is exploding. The cost of starting has never been lower.",
    "rule": "Choice is yours. Just choose wisely."
  },
  "footer": {
    "brand": "@0xdierich",
    "note": "Built in public. Nothing here is financial advice.",
    "domain": "howtogetrich.now"
  }
}

DATA_JSON = json.dumps(DATA, ensure_ascii=False)
OUT.mkdir(parents=True, exist_ok=True)

# ─────────────────────────────────────────────────────────────
# VARIANT A — TERMINAL NOIR (dense, mono numbers, rail nav)
# ─────────────────────────────────────────────────────────────
A = r"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>How to Get Rich in 2026 — 3 Skills That Print Money</title>
<meta name="description" content="The 2026 playbook: Creator, Clipper, Vibe Coder. Learn them, monetize them, combine them.">
<style>
:root{
  --bg:#08090A; --bg2:#0C0F0D; --fg:#EDEEE9; --mut:#8B918C; --line:#1E2320;
  --acc:#B8FF3C; --acc2:#FF5C39;
  --mono:ui-monospace,"Cascadia Mono",Consolas,"Courier New",monospace;
  --sans:"Segoe UI",Inter,-apple-system,system-ui,sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;scroll-padding-top:80px}
body{background:var(--bg);color:var(--fg);font-family:var(--sans);line-height:1.45;-webkit-font-smoothing:antialiased;overflow-x:hidden}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:9;
  background:repeating-linear-gradient(0deg,rgba(255,255,255,.018) 0 1px,transparent 1px 3px);opacity:.6}
a{color:inherit;text-decoration:none}
/* top bar */
.bar{position:fixed;top:0;left:0;right:0;height:46px;z-index:50;display:flex;align-items:center;
  gap:18px;padding:0 18px;background:rgba(8,9,10,.88);backdrop-filter:blur(8px);
  border-bottom:1px solid var(--line);font-family:var(--mono);font-size:11px;letter-spacing:.1em}
.bar .b{color:var(--acc);font-weight:600}
.bar .tick{flex:1;overflow:hidden;mask-image:linear-gradient(90deg,transparent,#000 6%,#000 94%,transparent)}
.bar .tick div{display:flex;gap:36px;white-space:nowrap;animation:sl 46s linear infinite;color:var(--mut);text-transform:uppercase}
.bar .tick b{color:var(--fg);font-weight:500}
@keyframes sl{to{transform:translateX(-50%)}}
.bar .r{color:var(--mut)}
.prog{position:fixed;top:45px;left:0;height:2px;background:var(--acc);z-index:51;width:0}
/* shell */
.shell{display:grid;grid-template-columns:132px minmax(0,1fr);gap:44px;max-width:1240px;margin:0 auto;padding:104px 26px 0}
.rail{position:sticky;top:104px;align-self:start;font-family:var(--mono);font-size:10.5px;letter-spacing:.12em;text-transform:uppercase}
.rail a{display:flex;gap:10px;padding:7px 33px 7px 0;color:var(--mut);border-bottom:1px solid transparent;transition:.2s}
.rail a span{color:#3A423C}
.rail a:hover{color:var(--fg)}
.rail a.on{color:var(--acc);border-bottom-color:#2A322B}
.rail a.on span{color:var(--acc)}
/* hero */
.hero{padding-bottom:64px;border-bottom:1px solid var(--line)}
.eyebrow{font-family:var(--mono);font-size:10.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--acc);margin-bottom:26px}
.hero h1{font-size:clamp(46px,7.4vw,108px);font-weight:800;letter-spacing:-.045em;line-height:.9;text-transform:uppercase}
.hero h1 em{font-style:normal;color:var(--acc)}
.hero .sub{margin-top:18px;font-size:clamp(17px,2vw,23px);color:var(--fg);font-weight:300;letter-spacing:-.01em}
.hero .lead{margin-top:20px;max-width:60ch;font-size:15.5px;color:var(--mut)}
.hstats{display:grid;grid-template-columns:repeat(3,1fr);margin-top:40px;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.hstats div{padding:18px 18px 18px 0}
.hstats div+div{border-left:1px solid var(--line);padding-left:18px}
.hstats b{display:block;font-family:var(--mono);font-size:clamp(22px,3vw,34px);font-weight:600;color:var(--acc);letter-spacing:-.02em}
.hstats span{font-family:var(--mono);font-size:10px;text-transform:uppercase;letter-spacing:.11em;color:var(--mut)}
/* sections */
.sec{padding:62px 0;border-bottom:1px solid var(--line)}
.shead{margin-bottom:32px}
.snum{font-family:var(--mono);font-size:10.5px;letter-spacing:.2em;color:var(--acc);text-transform:uppercase}
.shead h2{margin-top:12px;font-size:clamp(25px,3.5vw,42px);font-weight:700;letter-spacing:-.03em;line-height:1.08;max-width:30ch}
.snote{margin-top:14px;font-family:var(--mono);font-size:12px;color:var(--mut);letter-spacing:.02em}
/* timeline */
.tl{display:grid;gap:0}
.tl .row{display:grid;grid-template-columns:90px 148px minmax(0,1fr);gap:18px;padding:16px 0;border-top:1px dashed #20261F;font-size:14px}
.tl .row:first-child{border-top:0}
.tl .y{font-family:var(--mono);color:var(--acc);letter-spacing:.08em}
.tl .k{font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;color:var(--fg)}
.tl .row p{color:var(--mut)}
/* cards */
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(215px,1fr));gap:14px}
.card{background:var(--bg2);border:1px solid var(--line);padding:22px 20px;cursor:pointer;transition:.22s;position:relative}
.card:hover{border-color:#39412F;background:#101411;transform:translateY(-3px)}
.card .role{font-family:var(--mono);font-size:9.5px;letter-spacing:.2em;color:var(--acc);text-transform:uppercase}
.card h3{margin:12px 0 8px;font-size:20px;letter-spacing:-.02em;font-weight:600}
.card p{font-size:13.5px;color:var(--mut);min-height:56px}
.card .meta{margin-top:16px;padding-top:12px;border-top:1px solid var(--line);font-family:var(--mono);font-size:10px;color:#6C726D;letter-spacing:.06em;text-transform:uppercase;display:grid;gap:5px}
.card .go{position:absolute;top:18px;right:16px;color:#39412F;font-family:var(--mono)}
.card:hover .go{color:var(--acc)}
/* tabs */
.tabs{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:30px}
.tabs button{font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--mut);
  background:transparent;border:1px solid var(--line);padding:10px 15px;cursor:pointer;transition:.18s}
.tabs button:hover{color:var(--fg);border-color:#39412F}
.tabs button.on{background:var(--acc);color:#08090A;border-color:var(--acc);font-weight:600}
.pgrid{display:grid;grid-template-columns:1.05fr .95fr;gap:44px}
.ptitle{font-size:clamp(24px,3vw,34px);letter-spacing:-.025em;font-weight:600;margin-bottom:6px}
.ptag{font-family:var(--mono);font-size:12px;color:var(--acc);margin-bottom:22px}
.pbody{font-size:14.5px;color:#B7BDB7;margin-bottom:26px}
.plabel{font-family:var(--mono);font-size:9.5px;letter-spacing:.2em;text-transform:uppercase;color:#6C726D;margin-bottom:12px}
ol.pb{list-style:none;counter-reset:i}
ol.pb li{counter-increment:i;position:relative;padding-left:34px;margin-bottom:13px;font-size:13.8px;color:#C9CFC9}
ol.pb li::before{content:counter(i,decimal-leading-zero);position:absolute;left:0;top:1px;font-family:var(--mono);font-size:10.5px;color:var(--acc)}
.chips{display:flex;flex-wrap:wrap;gap:7px;margin-bottom:26px}
.chips span{font-family:var(--mono);font-size:10.5px;color:#A9AFA9;border:1px solid var(--line);padding:6px 10px;background:#0B0E0C}
.money{width:100%;border-top:1px solid var(--line);margin-bottom:26px}
.money .mr{display:flex;justify-content:space-between;gap:14px;padding:11px 0;border-bottom:1px solid #171C18;font-size:13px}
.money .mr span:first-child{color:#B7BDB7}
.money .mr span:last-child{font-family:var(--mono);font-size:11.5px;color:var(--acc);white-space:nowrap}
.proof{border-left:2px solid var(--acc);padding:4px 0 4px 18px}
.proof p{font-size:14.5px;color:#D6DBD6;font-style:italic;line-height:1.55}
.proof cite{display:block;margin-top:10px;font-family:var(--mono);font-size:10.5px;color:var(--mut);font-style:normal}
.pm{display:flex;gap:34px;margin-top:22px;padding-top:16px;border-top:1px solid var(--line)}
.pm div b{display:block;font-family:var(--mono);font-size:20px;color:var(--acc)}
.pm div span{font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:#5F6660}
/* pipeline */
.pipe{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px}
.pcard{border:1px dashed #2A3128;padding:18px;background:#0A0D0B}
.pcard .top{display:flex;justify-content:space-between;font-family:var(--mono);font-size:9px;letter-spacing:.14em;color:#5F6660}
.pcard .top b{color:var(--acc2)}
.pcard h4{margin:10px 0 6px;font-size:14px;letter-spacing:.04em;font-family:var(--mono)}
.pcard p{font-size:12.5px;color:#7E857F}
/* combo */
.steps{list-style:none;counter-reset:c;margin-bottom:26px}
.steps li{counter-increment:c;display:grid;grid-template-columns:52px 1fr;gap:16px;padding:14px 0;border-top:1px solid #171C18;font-size:15px;color:#C9CFC9}
.steps li::before{content:counter(c,decimal-leading-zero);font-family:var(--mono);color:var(--acc);font-size:13px}
.bigline{font-size:clamp(18px,2.3vw,26px);letter-spacing:-.02em;color:var(--fg);font-weight:300}
.bigline b{color:var(--acc);font-weight:600}
.result{margin-top:22px;padding:18px;background:#0C100D;border-left:2px solid var(--acc);font-family:var(--mono);font-size:12px;letter-spacing:.04em;color:#C9CFC9}
/* numbers */
.nums{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.nums div{padding:22px 16px 22px 0}
.nums div+div{border-left:1px solid var(--line);padding-left:16px}
.nums b{display:block;font-family:var(--mono);font-size:clamp(22px,3.4vw,36px);color:var(--acc);letter-spacing:-.03em}
.nums span{font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:#5F6660}
.small{margin-top:18px;font-family:var(--mono);font-size:11px;color:#6C726D;line-height:1.8}
/* sprint */
.sp{list-style:none}
.sp li{display:flex;gap:14px;align-items:flex-start;padding:13px 0;border-bottom:1px solid #171C18;font-size:14px;color:#C9CFC9;cursor:pointer}
.sp li .box{width:15px;height:15px;border:1px solid #3A423C;flex:0 0 auto;margin-top:2px;transition:.2s;position:relative}
.sp li.done .box{background:var(--acc);border-color:var(--acc)}
.sp li.done .box::after{content:"✕";position:absolute;inset:0;color:#08090A;font-size:11px;line-height:13px;text-align:center;font-weight:700}
.sp li.done .txt{color:#5F6660;text-decoration:line-through}
.spbar{margin-top:16px;font-family:var(--mono);font-size:10.5px;letter-spacing:.12em;color:var(--mut)}
.spbar i{display:block;height:3px;background:#1A1F1B;margin-top:8px;position:relative}
.spbar i b{position:absolute;inset:0 auto 0 0;background:var(--acc);width:0;transition:.3s}
/* warning */
.warn{padding:76px 0 60px;border-bottom:1px solid var(--line)}
.warn h2{font-size:clamp(38px,7vw,86px);font-weight:800;letter-spacing:-.05em;line-height:.92;text-transform:uppercase}
.warn h2 em{font-style:normal;color:var(--acc2)}
.warn p{margin-top:22px;max-width:56ch;font-size:15px;color:#B7BDB7}
.warn .rule{margin-top:34px;font-family:var(--mono);font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--acc)}
footer{padding:34px 0 60px;display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;color:#5F6660;text-transform:uppercase}
figcaption, .rv{opacity:1}
.rv{opacity:0;transform:translateY(14px);transition:opacity .6s ease,transform .6s ease}
.rv.in{opacity:1;transform:none}
@media(max-width:900px){
  .shell{grid-template-columns:1fr;gap:0;padding:86px 18px 0}
  .rail{display:none}
  .pgrid{grid-template-columns:1fr;gap:30px}
  .tl .row{grid-template-columns:64px 1fr;gap:10px}
  .tl .row p{grid-column:1/-1;font-size:13px}
  .hero h1{font-size:clamp(40px,11vw,64px)}
  .hstats{grid-template-columns:1fr}
  .hstats div+div{border-left:0;border-top:1px solid var(--line);padding-left:0}
}
</style></head>
<body>
<div class="bar">
  <div class="b">HOWTOGETRICH.NOW</div>
  <div class="tick"><div id="tick"></div></div>
  <div class="r">2026</div>
</div>
<div class="prog" id="prog"></div>

<div class="shell">
  <nav class="rail" id="rail"></nav>
  <main id="app"></main>
</div>

<script>
const D = __DATA__;
const $ = (s,r=document)=>r.querySelector(s);
const esc = s => String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;");
const tick = D.ticker.concat(D.ticker).map(t=>`<span>${esc(t)}</span><b>·</b>`).join("");
$("#tick").innerHTML = tick;

const NAV = [
  ["top","00","Start"],["shift","01","The shift"],["three","02","The three"],
  ["paths","03","Paths"],["pipeline","04","Patch log"],["combo","05","The combo"],
  ["proof","06","Receipts"],["sprint","07","7-day sprint"],["warn","08","Warning"]
];
$("#rail").innerHTML = NAV.map(([id,n,l])=>`<a href="#${id}" data-id="${id}"><span>${n}</span>${l}</a>`).join("");

let active = D.paths[0].id;

function pathHTML(p){
  return `
  <div class="pgrid rv">
    <div>
      <div class="ptitle">${esc(p.name)}</div>
      <div class="ptag">${esc(p.tagline)}</div>
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
      <div class="proof"><p>“${esc(p.proof[0])}”</p><cite>— ${esc(p.proof[1])}</cite></div>
    </div>
  </div>`;
}

$("#app").innerHTML = `
<section class="hero" id="top">
  <div class="eyebrow">${esc(D.hero.eyebrow)}</div>
  <h1>${esc(D.hero.l1)}<br><em>${esc(D.hero.l2)}</em></h1>
  <div class="sub">${esc(D.hero.sub)}</div>
  <p class="lead">${esc(D.hero.lead)}</p>
  <div class="hstats">${D.hero.stats.map(s=>`<div><b>${esc(s[0])}</b><span>${esc(s[1])}</span></div>`).join("")}</div>
</section>

<section class="sec" id="shift">
  <div class="shead"><div class="snum">${esc(D.shift.num)} / ${esc(D.shift.kicker)}</div>
  <h2>${esc(D.shift.title)}</h2><p class="snote">${esc(D.shift.body)}</p></div>
  <div class="tl">${D.shift.timeline.map(r=>`<div class="row"><div class="y">${esc(r[0])}</div><div class="k">${esc(r[1])}</div><p>${esc(r[2])}</p></div>`).join("")}</div>
</section>

<section class="sec" id="three">
  <div class="shead"><div class="snum">${esc(D.three.num)} / ${esc(D.three.kicker)}</div><h2>${esc(D.three.title)}</h2><p class="snote">${esc(D.three.note)}</p></div>
  <div class="cards">
    ${D.three.cards.map((c,i)=>`<div class="card" data-go="${D.paths[i].id}"><div class="go">↗</div>
      <div class="role">${esc(c[0])}</div><h3>${esc(c[1])}</h3><p>${esc(c[2])}</p>
      <div class="meta"><span>${esc(c[3])}</span><span>${esc(c[4])}</span><span>first $ → ${esc(c[5])}</span></div></div>`).join("")}
  </div>
</section>

<section class="sec" id="paths">
  <div class="shead"><div class="snum">03 / THE PATHS</div><h2>Three roads. One destination.</h2><p class="snote">Read the one that matches your starting point. Then read the other two.</p></div>
  <div class="tabs" id="tabs">${D.paths.map(p=>`<button data-id="${p.id}" class="${p.id===active?"on":""}">${p.n} — ${esc(p.name.replace("THE ",""))}</button>`).join("")}</div>
  <div id="pathbody">${pathHTML(D.paths[0])}</div>
</section>

<section class="sec" id="pipeline">
  <div class="shead"><div class="snum">${esc(D.pipeline.num)} / ${esc(D.pipeline.kicker)}</div><h2>${esc(D.pipeline.title)}</h2><p class="snote">${esc(D.pipeline.note)}</p></div>
  <div class="pipe">${D.pipeline.items.map(i=>`<div class="pcard"><div class="top"><span>${esc(i[0])}</span><b>${esc(i[2])}</b></div><h4>${esc(i[1])}</h4><p>${esc(i[3])}</p></div>`).join("")}</div>
</section>

<section class="sec" id="combo">
  <div class="shead"><div class="snum">${esc(D.combo.num)} / ${esc(D.combo.kicker)}</div><h2>${esc(D.combo.title)}</h2></div>
  <ol class="steps">${D.combo.steps.map(s=>`<li>${esc(s)}</li>`).join("")}</ol>
  <div class="bigline">${esc(D.combo.line).replace("idea → product → distribution","<b>idea → product → distribution</b>")}</div>
  <div class="result">${esc(D.combo.result)}</div>
</section>

<section class="sec" id="proof">
  <div class="shead"><div class="snum">${esc(D.proof.num)} / ${esc(D.proof.kicker)}</div><h2>${esc(D.proof.title)}</h2></div>
  <div class="nums">${D.proof.numbers.map(n=>`<div><b>${esc(n[0])}</b><span>${esc(n[1])}</span></div>`).join("")}</div>
  <p class="small">${esc(D.proof.note)}</p>
</section>

<section class="sec" id="sprint">
  <div class="shead"><div class="snum">${esc(D.sprint.num)} / ${esc(D.sprint.kicker)}</div><h2>${esc(D.sprint.title)}</h2><p class="snote">Tick them off. It remembers.</p></div>
  <ul class="sp" id="sp">${D.sprint.items.map((s,i)=>`<li data-i="${i}"><span class="box"></span><span class="txt"><b style="color:#5F6660;font-family:var(--mono);font-size:10px;margin-right:8px">D${i+1}</b>${esc(s)}</span></li>`).join("")}</ul>
  <div class="spbar"><span id="sptxt">0 / 7 COMPLETE</span><i><b id="spfill"></b></i></div>
</section>

<section class="warn" id="warn">
  <div class="snum">${esc(D.warning.num)} / ${esc(D.warning.kicker)}</div>
  <h2 style="margin-top:18px">${esc(D.warning.title).replace("left behind","left <em>behind</em>")}</h2>
  <p>${esc(D.warning.body)}</p>
  <p style="margin-top:14px">${esc(D.warning.close)}</p>
  <div class="rule">${esc(D.warning.rule)}</div>
</section>
<footer><span>${esc(D.footer.brand)} — ${esc(D.footer.note)}</span><span>${esc(D.footer.domain)}</span></footer>
`;

// tabs
$("#tabs").addEventListener("click", e=>{
  const b = e.target.closest("button"); if(!b) return;
  active = b.dataset.id;
  document.querySelectorAll("#tabs button").forEach(x=>x.classList.toggle("on", x.dataset.id===active));
  $("#pathbody").innerHTML = pathHTML(D.paths.find(p=>p.id===active));
  const nl = $("#pathbody .rv"); if(nl) requestAnimationFrame(()=>nl.classList.add("in"));
});
// cards → path
document.querySelectorAll(".card").forEach(c=>c.addEventListener("click",()=>{
  const id=c.dataset.go;
  document.querySelector('#paths').scrollIntoView({behavior:"smooth"});
  setTimeout(()=>{
    active=id;
    document.querySelectorAll("#tabs button").forEach(x=>x.classList.toggle("on",x.dataset.id===active));
    $("#pathbody").innerHTML=pathHTML(D.paths.find(p=>p.id===active));
    const nl=$("#pathbody .rv"); if(nl) requestAnimationFrame(()=>nl.classList.add("in"));
  },420);
}));
// sprint
const KEY="htgr_sprint_v1";
let done = [];
try{ done = JSON.parse(localStorage.getItem(KEY)||"[]"); }catch(e){ done=[]; }
const spItems=[...document.querySelectorAll("#sp li")];
function spRender(){
  let n=0;
  spItems.forEach(li=>{
    const on = done.includes(+li.dataset.i);
    li.classList.toggle("done",on); if(on) n++;
  });
  $("#sptxt").textContent = `${n} / 7 COMPLETE`;
  $("#spfill").style.width = (n/7*100)+"%";
}
spItems.forEach(li=>li.addEventListener("click",()=>{
  const i=+li.dataset.i;
  done = done.includes(i) ? done.filter(x=>x!==i) : [...done,i];
  try{ localStorage.setItem(KEY,JSON.stringify(done)); }catch(e){}
  spRender();
}));
spRender();
// progress + rail
const prog=$("#prog");
addEventListener("scroll",()=>{
  const h=document.documentElement;
  prog.style.width = (h.scrollTop/(h.scrollHeight-h.clientHeight)*100)+"%";
},{passive:true});
const io=new IntersectionObserver(es=>{
  es.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add("in"); } });
},{threshold:.12});
document.querySelectorAll(".rv").forEach(e=>io.observe(e));
$(".rv")?.classList.add("in");
const navio=new IntersectionObserver(es=>{
  es.forEach(e=>{ if(e.isIntersecting){
    const id=e.target.id;
    document.querySelectorAll(".rail a").forEach(a=>a.classList.toggle("on",a.dataset.id===id));
  }});
},{rootMargin:"-45% 0px -50% 0px"});
NAV.forEach(([id])=>{ const s=document.getElementById(id); if(s) navio.observe(s); });
</script>
</body></html>
"""

# ─────────────────────────────────────────────────────────────
# VARIANT B — NEON BRUTALIST
# ─────────────────────────────────────────────────────────────
B = r"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>How to Get Rich in 2026 — 3 Skills That Print Money</title>
<meta name="description" content="Three skills. One flywheel. Zero credentials.">
<style>
:root{
  --bg:#0A0A0A;--fg:#FFF;--mut:#A0A0A0;--hot:#FF3B00;--cy:#00E5FF;--yel:#F2FF3B;
  --sans:"Segoe UI",Inter,-apple-system,system-ui,sans-serif;
  --mono:ui-monospace,"Cascadia Mono",Consolas,monospace;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;scroll-padding-top:70px}
body{background:var(--bg);color:var(--fg);font-family:var(--sans);line-height:1.4;overflow-x:hidden;
  background-image:radial-gradient(900px 520px at 8% -6%,rgba(255,59,0,.20),transparent 70%),
                   radial-gradient(800px 460px at 102% 12%,rgba(0,229,255,.14),transparent 70%),
                   radial-gradient(700px 700px at 50% 120%,rgba(242,255,59,.07),transparent 70%);
  background-attachment:fixed}
a{color:inherit;text-decoration:none}
.wrap{max-width:1160px;margin:0 auto;padding:0 22px}
/* top */
.top{position:sticky;top:0;z-index:40;background:#0A0A0A;border-bottom:3px solid #fff}
.top .in{display:flex;align-items:center;justify-content:space-between;height:52px;font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase}
.top .in b{background:var(--yel);color:#000;padding:4px 8px}
.prog{height:4px;background:#1E1E1E}
.prog b{display:block;height:100%;background:var(--hot);width:0}
/* hero */
.hero{padding:64px 0 0;position:relative}
.eyebrow{display:inline-block;font-family:var(--mono);font-size:11px;letter-spacing:.2em;text-transform:uppercase;
  border:2px solid #fff;padding:7px 12px;margin-bottom:26px;background:#000}
h1{font-size:clamp(52px,12.4vw,184px);line-height:.8;letter-spacing:-.055em;font-weight:900;text-transform:uppercase}
h1 .o{color:transparent;-webkit-text-stroke:2px #fff}
h1 .hot{color:var(--hot)}
.sub{margin-top:22px;font-size:clamp(19px,3.2vw,34px);font-weight:800;letter-spacing:-.02em;text-transform:uppercase}
.sub u{text-decoration:none;background:var(--yel);color:#000;padding:0 8px}
.lead{margin-top:20px;max-width:56ch;font-size:16px;color:#C6C6C6}
.stats{display:flex;flex-wrap:wrap;gap:0;margin-top:38px;border:3px solid #fff;background:#000}
.stats div{flex:1 1 160px;padding:16px 18px;border-right:3px solid #fff}
.stats div:last-child{border-right:0}
.stats b{display:block;font-family:var(--mono);font-size:30px;color:var(--cy);letter-spacing:-.02em}
.stats span{font-family:var(--mono);font-size:9.5px;text-transform:uppercase;letter-spacing:.12em;color:#9A9A9A}
/* marquee */
.mq{margin-top:44px;background:var(--hot);color:#000;border-top:3px solid #000;border-bottom:3px solid #000;
  overflow:hidden;transform:rotate(-1.4deg);margin-bottom:-6px;position:relative;z-index:2}
.mq div{display:flex;gap:28px;white-space:nowrap;padding:9px 0;font-family:var(--mono);font-size:13px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;animation:mv 34s linear infinite}
.mq.alt{background:var(--cy);transform:rotate(1.1deg)}
.mq.dark{background:#000;color:var(--yel);border-color:#fff}
@keyframes mv{to{transform:translateX(-50%)}}
/* sections */
section.blk{padding:74px 0 62px;border-bottom:1px solid #232323}
.kick{display:flex;align-items:center;gap:12px;font-family:var(--mono);font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--yel);margin-bottom:18px}
.kick i{display:inline-block;width:34px;height:3px;background:var(--yel)}
h2{font-size:clamp(30px,5.4vw,62px);line-height:.94;letter-spacing:-.045em;font-weight:900;text-transform:uppercase;max-width:22ch}
.note{margin-top:16px;font-family:var(--mono);font-size:12.5px;color:#9A9A9A;max-width:64ch;line-height:1.7}
/* timeline */
.tl{margin-top:34px;display:grid;gap:0}
.tl .row{display:grid;grid-template-columns:120px 1fr;gap:20px;padding:18px 0;border-top:2px solid #262626}
.tl .row:first-child{border-top:3px solid #fff}
.tl .y{font-family:var(--mono);font-size:clamp(20px,3vw,30px);font-weight:700;color:var(--hot)}
.tl .k{font-family:var(--mono);font-size:11px;letter-spacing:.16em;color:var(--yel);margin-bottom:6px}
.tl .row p{font-size:14.5px;color:#C6C6C6;max-width:56ch}
/* cards */
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:18px;margin-top:34px}
.card{background:#0D0D0D;border:3px solid #fff;padding:22px;cursor:pointer;transition:.14s;box-shadow:9px 9px 0 var(--hot);position:relative}
.card:nth-child(2){box-shadow:9px 9px 0 var(--cy)}
.card:nth-child(3){box-shadow:9px 9px 0 var(--yel)}
.card:hover{transform:translate(-4px,-4px);box-shadow:14px 14px 0 var(--hot)}
.card .role{font-family:var(--mono);font-size:10px;letter-spacing:.2em;background:#fff;color:#000;display:inline-block;padding:3px 7px}
.card h3{margin:14px 0 8px;font-size:23px;line-height:1.05;letter-spacing:-.03em;text-transform:uppercase;font-weight:900}
.card p{font-size:13.5px;color:#B8B8B8;min-height:58px}
.card .meta{margin-top:14px;border-top:2px solid #2A2A2A;padding-top:10px;font-family:var(--mono);font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:#8A8A8A;display:grid;gap:4px}
.card .arrow{position:absolute;top:14px;right:14px;font-size:20px;color:#3A3A3A;transition:.15s}
.card:hover .arrow{color:var(--yel);transform:translateX(3px)}
/* tabs */
.tabs{display:flex;flex-wrap:wrap;gap:10px;margin:32px 0 28px}
.tabs button{font-family:var(--mono);font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;font-weight:700;
  background:#000;color:#fff;border:3px solid #fff;padding:12px 16px;cursor:pointer;transition:.13s;box-shadow:5px 5px 0 #333}
.tabs button:hover{transform:translate(-2px,-2px);box-shadow:7px 7px 0 #555}
.tabs button.on{background:var(--yel);color:#000;box-shadow:5px 5px 0 var(--hot)}
.phead{display:flex;flex-wrap:wrap;align-items:baseline;gap:14px;margin-bottom:6px}
.ptitle{font-size:clamp(26px,4.2vw,44px);font-weight:900;letter-spacing:-.04em;text-transform:uppercase;line-height:.95}
.ptag{font-family:var(--mono);font-size:12px;color:var(--cy);letter-spacing:.06em}
.pgrid{display:grid;grid-template-columns:1.05fr .95fr;gap:34px;margin-top:22px}
.pbody{font-size:14.5px;color:#C6C6C6;margin-bottom:24px;max-width:58ch}
.plabel{font-family:var(--mono);font-size:10px;letter-spacing:.2em;text-transform:uppercase;color:#7A7A7A;margin-bottom:12px;border-left:3px solid var(--hot);padding-left:8px}
ol.pb{list-style:none;counter-reset:i;margin-bottom:26px}
ol.pb li{counter-increment:i;position:relative;padding-left:38px;margin-bottom:12px;font-size:14px;color:#D0D0D0}
ol.pb li::before{content:counter(i,decimal-leading-zero);position:absolute;left:0;top:0;font-family:var(--mono);font-size:11px;
  background:var(--hot);color:#000;width:26px;height:20px;line-height:20px;text-align:center;font-weight:700}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:24px}
.chips span{font-family:var(--mono);font-size:11px;border:2px solid #fff;padding:6px 10px;background:#111}
.money{border:3px solid #fff;background:#000;margin-bottom:24px}
.money .mr{display:flex;justify-content:space-between;gap:12px;padding:11px 14px;border-bottom:2px solid #232323;font-size:13px}
.money .mr:last-child{border-bottom:0}
.money .mr:nth-child(odd){background:#0E0E0E}
.money .mr span:last-child{font-family:var(--mono);font-size:11.5px;color:var(--yel);white-space:nowrap;font-weight:700}
.proof{border:3px solid var(--yel);background:#000;padding:20px;box-shadow:8px 8px 0 rgba(242,255,59,.22)}
.proof p{font-size:15px;line-height:1.55;color:#EFEFEF}
.proof cite{display:block;margin-top:12px;font-family:var(--mono);font-size:10.5px;color:var(--cy);font-style:normal;letter-spacing:.06em}
.pm{display:flex;gap:26px;margin-top:20px;flex-wrap:wrap}
.pm div b{display:block;font-family:var(--mono);font-size:22px;color:var(--cy)}
.pm div span{font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:#7A7A7A}
/* pipeline */
.pipe{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px;margin-top:32px}
.pcard{border:3px dashed #4A4A4A;padding:18px;background:#0C0C0C}
.pcard .top{display:flex;justify-content:space-between;font-family:var(--mono);font-size:9.5px;letter-spacing:.14em;color:#7A7A7A}
.pcard .top b{color:var(--hot)}
.pcard h4{margin:12px 0 6px;font-size:15px;font-family:var(--mono);letter-spacing:.06em;color:var(--yel)}
.pcard p{font-size:12.5px;color:#A6A6A6}
/* combo */
.steps{list-style:none;counter-reset:c;margin-top:32px;display:grid;gap:12px}
.steps li{counter-increment:c;display:grid;grid-template-columns:54px 1fr;gap:18px;align-items:center;font-size:clamp(15px,2.2vw,21px);
  font-weight:700;letter-spacing:-.02em;padding:14px 16px;background:#0E0E0E;border-left:5px solid var(--hot)}
.steps li:nth-child(2){border-left-color:var(--cy)}
.steps li:nth-child(3){border-left-color:var(--yel)}
.steps li:nth-child(4){border-left-color:#fff}
.steps li::before{content:counter(c,decimal-leading-zero);font-family:var(--mono);font-size:15px;color:#6A6A6A}
.bigline{margin-top:26px;font-size:clamp(20px,3.4vw,34px);font-weight:900;letter-spacing:-.03em;text-transform:uppercase;line-height:1.1}
.bigline b{color:var(--yel)}
.result{margin-top:20px;display:inline-block;background:var(--hot);color:#000;font-family:var(--mono);font-size:12.5px;
  font-weight:700;letter-spacing:.06em;text-transform:uppercase;padding:11px 15px;transform:rotate(-.8deg)}
/* numbers */
.nums{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:0;margin-top:32px;border:3px solid #fff;background:#000}
.nums div{padding:22px 16px;border-right:3px solid #fff}
.nums div:last-child{border-right:0}
.nums b{display:block;font-family:var(--mono);font-size:clamp(24px,3.6vw,38px);color:var(--yel);letter-spacing:-.03em}
.nums span{font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:#8A8A8A}
.small{margin-top:18px;font-family:var(--mono);font-size:11.5px;color:#8A8A8A;line-height:1.8;max-width:80ch}
/* sprint */
.sp{list-style:none;margin-top:30px;border-top:3px solid #fff}
.sp li{display:flex;gap:16px;align-items:flex-start;padding:16px 6px;border-bottom:1px solid #262626;cursor:pointer;font-size:15px;transition:.12s}
.sp li:hover{background:#101010}
.sp .box{width:26px;height:26px;border:3px solid #fff;flex:0 0 auto;position:relative;transition:.12s}
.sp li.done .box{background:var(--yel);border-color:var(--yel)}
.sp li.done .box::after{content:"✕";position:absolute;inset:0;color:#000;font-weight:900;text-align:center;line-height:20px;font-size:16px}
.sp li.done .txt{color:#5A5A5A;text-decoration:line-through}
.sp .d{font-family:var(--mono);font-size:11px;color:#6A6A6A;margin-right:8px}
.spbar{margin-top:20px;font-family:var(--mono);font-size:11px;letter-spacing:.14em;color:#8A8A8A}
.spbar i{display:block;height:8px;background:#1E1E1E;border:2px solid #333;margin-top:8px;position:relative}
.spbar i b{position:absolute;inset:0 auto 0 0;background:var(--yel);width:0;transition:.25s}
/* warn */
.warn{background:var(--yel);color:#000;padding:76px 0 66px;border-top:3px solid #000;border-bottom:3px solid #000;margin-top:0}
.warn .kick{color:#000}.warn .kick i{background:#000}
.warn h2{color:#000;font-size:clamp(42px,9vw,110px);line-height:.84}
.warn p{margin-top:20px;max-width:58ch;font-size:15.5px;font-weight:600;color:#141414}
.warn .rule{margin-top:30px;font-family:var(--mono);font-weight:700;font-size:14px;letter-spacing:.14em;text-transform:uppercase;background:#000;color:var(--yel);display:inline-block;padding:11px 15px}
footer{padding:30px 0 60px;font-family:var(--mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:#7A7A7A;display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
.rv{opacity:0;transform:translateY(18px);transition:opacity .55s,transform .55s}
.rv.in{opacity:1;transform:none}
@media(max-width:820px){
  .pgrid{grid-template-columns:1fr}
  .tl .row{grid-template-columns:70px 1fr}
  .stats div{flex:1 1 100%;border-right:0;border-bottom:3px solid #fff}
  .stats div:last-child{border-bottom:0}
  h1{font-size:clamp(46px,13.5vw,80px)}
}
</style></head>
<body>
<div class="top"><div class="wrap in"><span>HOWTOGETRICH<b>.NOW</b></span><span style="color:#8A8A8A">3 SKILLS · 1 FLYWHEEL</span><span>2026</span></div>
<div class="prog"><b id="prog"></b></div></div>

<main class="wrap" id="app"></main>

<script>
const D = __DATA__;
const esc = s => String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;");
const app = document.getElementById("app");
const marquee = (text, cls="") => `<div class="mq ${cls}"><div>${(text+" · ").repeat(2).split("·").concat(text).join(" · ")}</div></div>`;
const band = (t,cls) => `<div class="mq ${cls}"><div>${Array(6).fill(t).join(" <span>·</span> ")}</div></div>`;

let active = D.paths[0].id;

function pathHTML(p){
  return `<div class="rv">
    <div class="phead"><div class="ptitle">${esc(p.name)}</div></div>
    <div class="ptag">${esc(p.tagline)}</div>
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
        <div class="proof"><p>“${esc(p.proof[0])}”</p><cite>— ${esc(p.proof[1])}</cite></div>
      </div>
    </div></div>`;
}

app.innerHTML = `
<section class="hero" id="top">
  <div class="eyebrow">${esc(D.hero.eyebrow)}</div>
  <h1>${esc(D.hero.l1)}<br><span class="hot">${esc(D.hero.l2.split(" ")[0])}</span> <span class="o">${esc(D.hero.l2.split(" ").slice(1).join(" "))}</span></h1>
  <div class="sub"><u>${esc(D.hero.sub)}</u></div>
  <p class="lead">${esc(D.hero.lead)}</p>
  <div class="stats">${D.hero.stats.map(s=>`<div><b>${esc(s[0])}</b><span>${esc(s[1])}</span></div>`).join("")}</div>
</section>
${band("MASTER ONE → STAY RELEVANT", "")}

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
    ${D.three.cards.map((c,i)=>`<div class="card rv" data-go="${D.paths[i].id}"><div class="arrow">↗</div>
      <div class="role">${esc(c[0])}</div><h3>${esc(c[1])}</h3><p>${esc(c[2])}</p>
      <div class="meta"><span>${esc(c[3])}</span><span>${esc(c[4])}</span><span>first $ → ${esc(c[5])}</span></div></div>`).join("")}
  </div>
</section>

${band("CLIP IT · SHIP IT · POST IT", "alt")}

<section class="blk" id="paths">
  <div class="kick"><i></i>03 / THE PATHS</div>
  <h2>Three roads. One destination.</h2>
  <p class="note">Pick your entry point. Then read the rest anyway.</p>
  <div class="tabs" id="tabs">${D.paths.map(p=>`<button data-id="${p.id}" class="${p.id===active?"on":""}">${p.n} ${esc(p.name.replace("THE ",""))}</button>`).join("")}</div>
  <div id="pathbody">${pathHTML(D.paths[0])}</div>
</section>

<section class="blk" id="pipeline">
  <div class="kick"><i></i>${esc(D.pipeline.num)} / ${esc(D.pipeline.kicker)}</div>
  <h2>${esc(D.pipeline.title)}</h2>
  <p class="note">${esc(D.pipeline.note)}</p>
  <div class="pipe">${D.pipeline.items.map(i=>`<div class="pcard rv"><div class="top"><span>${esc(i[0])}</span><b>${esc(i[2])}</b></div><h4>${esc(i[1])}</h4><p>${esc(i[3])}</p></div>`).join("")}</div>
</section>
${band("MASTER ONE AND YOU STAY RELEVANT", "dark")}
<section class="blk" id="combo">
  <div class="kick"><i></i>${esc(D.combo.num)} / ${esc(D.combo.kicker)}</div>
  <h2>${esc(D.combo.title)}</h2>
  <ol class="steps">${D.combo.steps.map(s=>`<li>${esc(s)}</li>`).join("")}</ol>
  <div class="bigline">${esc(D.combo.line).replace("idea → product → distribution","<b>IDEA → PRODUCT → DISTRIBUTION</b>")}</div>
  <div class="result">${esc(D.combo.result)}</div>
</section>

<section class="blk" id="proof">
  <div class="kick"><i></i>${esc(D.proof.num)} / ${esc(D.proof.kicker)}</div>
  <h2>${esc(D.proof.title)}</h2>
  <div class="nums">${D.proof.numbers.map(n=>`<div><b>${esc(n[0])}</b><span>${esc(n[1])}</span></div>`).join("")}</div>
  <p class="small">${esc(D.proof.note)}</p>
</section>

<section class="blk" id="sprint">
  <div class="kick"><i></i>${esc(D.sprint.num)} / ${esc(D.sprint.kicker)}</div>
  <h2>${esc(D.sprint.title)}</h2>
  <ul class="sp" id="sp">${D.sprint.items.map((s,i)=>`<li data-i="${i}"><span class="box"></span><span class="txt"><span class="d">D${i+1}</span>${esc(s)}</span></li>`).join("")}</ul>
  <div class="spbar"><span id="sptxt">0 / 7 COMPLETE</span><i><b id="spfill"></b></i></div>
</section>
</main>

<section class="warn" id="warn">
  <div class="wrap">
    <div class="kick"><i></i>${esc(D.warning.num)} / ${esc(D.warning.kicker)}</div>
    <h2>${esc(D.warning.title)}</h2>
    <p>${esc(D.warning.body)}</p>
    <p style="margin-top:12px">${esc(D.warning.close)}</p>
    <div class="rule">${esc(D.warning.rule)}</div>
  </div>
</section>
<div class="wrap"><footer><span>${esc(D.footer.brand)} — ${esc(D.footer.note)}</span><span>${esc(D.footer.domain)}</span></footer></div>
`;
</script>

<script>
$tabs = document.getElementById("tabs");
$tabs.addEventListener("click", e=>{
  const b=e.target.closest("button"); if(!b) return;
  active=b.dataset.id;
  $tabs.querySelectorAll("button").forEach(x=>x.classList.toggle("on",x.dataset.id===active));
  const body=document.getElementById("pathbody");
  body.innerHTML=pathHTML(D.paths.find(p=>p.id===active));
  body.querySelector(".rv")?.classList.add("in");
});
document.querySelectorAll(".card").forEach(c=>c.addEventListener("click",()=>{
  const id=c.dataset.go;
  document.getElementById("paths").scrollIntoView({behavior:"smooth"});
  setTimeout(()=>{
    active=id;
    $tabs.querySelectorAll("button").forEach(x=>x.classList.toggle("on",x.dataset.id===active));
    const body=document.getElementById("pathbody");
    body.innerHTML=pathHTML(D.paths.find(p=>p.id===active));
    body.querySelector(".rv")?.classList.add("in");
  },450);
}));
const KEY="htgr_sprint_b";
let done=[]; try{done=JSON.parse(localStorage.getItem(KEY)||"[]")}catch(e){done=[]}
const items=[...document.querySelectorAll("#sp li")];
function render(){
  let n=0;
  items.forEach(li=>{const on=done.includes(+li.dataset.i);li.classList.toggle("done",on);if(on)n++});
  document.getElementById("sptxt").textContent=`${n} / 7 COMPLETE`;
  document.getElementById("spfill").style.width=(n/7*100)+"%";
}
items.forEach(li=>li.addEventListener("click",()=>{
  const i=+li.dataset.i;
  done = done.includes(i)?done.filter(x=>x!==i):[...done,i];
  try{localStorage.setItem(KEY,JSON.stringify(done))}catch(e){}
  render();
}));
render();
const prog=document.getElementById("prog");
addEventListener("scroll",()=>{const h=document.documentElement;
  prog.style.width=(h.scrollTop/(h.scrollHeight-h.clientHeight)*100)+"%"},{passive:true});
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)e.target.classList.add("in")}),{threshold:.1});
document.querySelectorAll(".rv").forEach(e=>io.observe(e));
</script>
</body></html>
"""

# ─────────────────────────────────────────────────────────────
# VARIANT C — QUIET EDITORIAL
# ─────────────────────────────────────────────────────────────
C = r"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>How to Get Rich in 2026 — A Playbook in Three Skills</title>
<meta name="description" content="Influence, attention, efficiency. A living playbook for the next era of the economy.">
<style>
:root{
  --paper:#FBFAF7;--ink:#14130F;--mut:#6B6862;--rule:#E3DFD5;--soft:#F3F0E9;--acc:#2C4A3B;
  --serif:"Iowan Old Style","Palatino Linotype",Cambria,Georgia,serif;
  --sans:"Segoe UI",Inter,-apple-system,system-ui,sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;scroll-padding-top:40px}
body{background:var(--paper);color:var(--ink);font-family:var(--serif);line-height:1.62;
  -webkit-font-smoothing:antialiased;
  background-image:radial-gradient(1200px 600px at 50% -10%,#FFF 0%,transparent 60%)}
a{color:inherit;text-decoration:none}
.masthead{border-bottom:1px solid var(--rule);padding:20px 26px;display:flex;justify-content:space-between;align-items:baseline;gap:16px;
  font-family:var(--sans);font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--mut)}
.masthead b{color:var(--ink);letter-spacing:.26em}
.page{max-width:1030px;margin:0 auto;padding:0 26px}
.grid{display:grid;grid-template-columns:minmax(0,700px) 168px;gap:66px;align-items:start;padding-top:60px}
/* hero */
.hero{padding-bottom:44px;border-bottom:1px solid var(--rule)}
.eyebrow{font-family:var(--sans);font-size:10.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--acc);margin-bottom:24px}
h1{font-size:clamp(38px,5.6vw,68px);line-height:1.04;letter-spacing:-.022em;font-weight:600}
h1 span{display:block}
h1 em{font-style:italic;color:var(--acc)}
.sub{margin-top:20px;font-size:21px;line-height:1.4;color:#33302A;font-style:italic}
.byline{margin-top:22px;font-family:var(--sans);font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--mut);
  display:flex;gap:14px;flex-wrap:wrap;padding-top:14px;border-top:1px solid var(--rule)}
.lead{margin-top:26px;font-size:19px;line-height:1.72;color:#2A2721}
.lead::first-letter{font-size:64px;float:left;line-height:.86;padding:4px 10px 0 0;color:var(--acc);font-weight:600}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:0;margin-top:34px;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)}
.stats div{padding:16px 14px 16px 0}
.stats div+div{border-left:1px solid var(--rule);padding-left:16px}
.stats b{display:block;font-family:var(--sans);font-size:25px;font-weight:600;letter-spacing:-.02em;color:var(--acc);font-variant-numeric:tabular-nums}
.stats span{font-family:var(--sans);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--mut);line-height:1.5;display:block;margin-top:3px}
/* toc */
.toc{position:sticky;top:34px;font-family:var(--sans);font-size:11px;letter-spacing:.06em}
.toc .h{font-size:9.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--mut);padding-bottom:10px;border-bottom:1px solid var(--rule);margin-bottom:10px}
.toc a{display:block;padding:5px 0;color:#55524C;transition:.15s;border-left:2px solid transparent;padding-left:9px;margin-left:-11px}
.toc a:hover{color:var(--ink)}
.toc a.on{color:var(--acc);border-left-color:var(--acc);font-weight:600}
/* sections */
.sec{padding:46px 0;border-bottom:1px solid var(--rule)}
.sec:last-of-type{border-bottom:0}
.kick{font-family:var(--sans);font-size:10px;letter-spacing:.2em;text-transform:uppercase;color:var(--acc);margin-bottom:14px}
h2{font-size:clamp(24px,3vw,32px);line-height:1.24;letter-spacing:-.015em;font-weight:600;max-width:34ch;margin-bottom:16px}
.sec p{font-size:18.5px;line-height:1.75;color:#2A2721;margin-bottom:14px;max-width:66ch}
.sec p.dim{color:var(--mut);font-size:16.5px}
/* timeline */
.tl{margin-top:24px}
.tl .row{display:grid;grid-template-columns:78px 1fr;gap:22px;padding:14px 0;border-top:1px solid var(--rule)}
.tl .row:last-child{border-bottom:1px solid var(--rule)}
.tl .y{font-family:var(--sans);font-size:13px;font-weight:600;color:var(--acc);letter-spacing:.06em;padding-top:2px}
.tl .k{font-family:var(--sans);font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--mut);margin-bottom:4px}
.tl p{font-size:16.5px;line-height:1.65;margin:0;color:#33302A}
/* cards */
.cards{display:grid;gap:0;margin-top:20px;border-top:1px solid var(--rule)}
.card{display:grid;grid-template-columns:96px 1fr auto;gap:20px;align-items:baseline;padding:18px 0;border-bottom:1px solid var(--rule);
  cursor:pointer;transition:.18s}
.card:hover{background:var(--soft);padding-left:10px;padding-right:10px}
.card .role{font-family:var(--sans);font-size:9.5px;letter-spacing:.18em;text-transform:uppercase;color:var(--acc)}
.card h3{font-size:19px;font-weight:600;letter-spacing:-.01em;margin-bottom:2px}
.card p{font-size:15.5px;color:var(--mut);margin:0;line-height:1.5}
.card .go{font-family:var(--sans);font-size:11px;color:var(--mut);letter-spacing:.08em;white-space:nowrap}
.card:hover .go{color:var(--acc)}
/* tabs */
.tabs{display:flex;gap:22px;margin:22px 0 26px;border-bottom:1px solid var(--rule);flex-wrap:wrap}
.tabs button{background:none;border:0;border-bottom:2px solid transparent;padding:0 0 9px;margin-bottom:-1px;cursor:pointer;
  font-family:var(--sans);font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--mut);transition:.15s}
.tabs button:hover{color:var(--ink)}
.tabs button.on{color:var(--ink);border-bottom-color:var(--acc);font-weight:600}
.ptitle{font-size:26px;font-weight:600;letter-spacing:-.015em}
.ptag{font-size:18px;font-style:italic;color:var(--acc);margin:4px 0 18px}
.plabel{font-family:var(--sans);font-size:9.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--mut);margin:26px 0 10px;
  padding-bottom:7px;border-bottom:1px solid var(--rule)}
ol.pb{list-style:none;counter-reset:i}
ol.pb li{counter-increment:i;position:relative;padding-left:30px;margin-bottom:11px;font-size:17px;line-height:1.65;color:#2A2721}
ol.pb li::before{content:counter(i) ".";position:absolute;left:0;font-family:var(--sans);font-size:12px;font-weight:600;color:var(--acc);top:4px}
.chips{display:flex;flex-wrap:wrap;gap:7px}
.chips span{font-family:var(--sans);font-size:11.5px;letter-spacing:.04em;border:1px solid var(--rule);background:#fff;padding:5px 10px;color:#4A4741}
.money{margin-top:0}
.money .mr{display:flex;justify-content:space-between;align-items:baseline;gap:12px;padding:9px 0;border-bottom:1px dotted #D6D1C6;font-size:16.5px}
.money .mr span:last-child{font-family:var(--sans);font-size:12.5px;color:var(--acc);font-variant-numeric:tabular-nums;letter-spacing:.02em}
blockquote{margin-top:26px;padding:4px 0 4px 22px;border-left:2px solid var(--acc)}
blockquote p{font-size:19px;line-height:1.68;font-style:italic;color:#2A2721;margin:0}
blockquote cite{display:block;margin-top:10px;font-family:var(--sans);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--mut);font-style:normal}
.pm{display:flex;gap:36px;margin-top:26px;padding-top:16px;border-top:1px solid var(--rule)}
.pm b{display:block;font-family:var(--sans);font-size:20px;font-weight:600;color:var(--acc);letter-spacing:-.01em}
.pm span{font-family:var(--sans);font-size:9.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--mut)}
/* pipeline */
.pipe{margin-top:16px}
.pcard{display:grid;grid-template-columns:78px 1fr;gap:18px;padding:14px 0;border-top:1px solid var(--rule);align-items:baseline}
.pcard:last-child{border-bottom:1px solid var(--rule)}
.pcard .n{font-family:var(--sans);font-size:9.5px;letter-spacing:.14em;color:var(--mut)}
.pcard h4{font-size:16.5px;font-weight:600;display:inline}
.pcard .st{font-family:var(--sans);font-size:9px;letter-spacing:.14em;text-transform:uppercase;color:var(--acc);
  border:1px solid var(--rule);padding:2px 6px;margin-left:8px;vertical-align:2px}
.pcard p{font-size:15.5px;color:var(--mut);margin:3px 0 0;line-height:1.55}
/* combo */
.steps{list-style:none;counter-reset:c;margin-top:18px}
.steps li{counter-increment:c;position:relative;padding-left:38px;margin-bottom:12px;font-size:18px;line-height:1.6;color:#2A2721}
.steps li::before{content:counter(c,decimal-leading-zero);position:absolute;left:0;top:3px;font-family:var(--sans);font-size:11px;color:var(--acc);letter-spacing:.06em}
.pull{margin-top:26px;font-size:clamp(20px,2.6vw,26px);line-height:1.42;letter-spacing:-.01em;font-weight:600;max-width:30ch}
.pull b{color:var(--acc);font-style:italic}
/* numbers */
.nums{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);margin-top:20px}
.nums div{padding:18px 12px 18px 0}
.nums div+div{border-left:1px solid var(--rule);padding-left:14px}
.nums b{display:block;font-family:var(--sans);font-size:clamp(20px,2.6vw,27px);font-weight:600;color:var(--ink);letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.nums span{font-family:var(--sans);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--mut);display:block;margin-top:2px}
.small{margin-top:16px;font-size:14px;color:var(--mut);line-height:1.7;font-family:var(--sans)}
/* sprint */
.sp{list-style:none;margin-top:18px;border-top:1px solid var(--rule)}
.sp li{display:flex;gap:14px;align-items:flex-start;padding:13px 0;border-bottom:1px solid var(--rule);cursor:pointer;font-size:17px;line-height:1.55;transition:.15s}
.sp li:hover{color:#000}
.sp .box{width:14px;height:14px;border:1px solid #A9A49A;flex:0 0 auto;margin-top:6px;position:relative;transition:.15s}
.sp li.done .box{background:var(--acc);border-color:var(--acc)}
.sp li.done .box::after{content:"";position:absolute;left:3px;top:0;width:5px;height:9px;border-right:1.5px solid #fff;border-bottom:1.5px solid #fff;transform:rotate(40deg)}
.sp li.done .txt{color:#A9A49A;text-decoration:line-through}
.sp .d{font-family:var(--sans);font-size:10px;letter-spacing:.12em;color:var(--mut);margin-right:8px}
.spbar{margin-top:16px;font-family:var(--sans);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--mut)}
.spbar i{display:block;height:2px;background:var(--rule);margin-top:8px;position:relative}
.spbar i b{position:absolute;inset:0 auto 0 0;background:var(--acc);width:0;transition:.3s}
/* warn */
.warn{padding:60px 0;border-top:1px solid var(--rule);text-align:left}
.warn h2{font-size:clamp(30px,4.4vw,46px);line-height:1.14;max-width:24ch;margin-bottom:18px}
.warn p{font-size:18px;line-height:1.72;color:#2A2721;max-width:60ch}
.warn .rule{margin-top:28px;font-family:var(--sans);font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--acc);
  padding-top:16px;border-top:1px solid var(--rule);display:inline-block}
footer{padding:30px 0 60px;display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;
  font-family:var(--sans);font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--mut)}
.rv{opacity:0;transform:translateY(8px);transition:opacity .7s,transform .7s}
.rv.in{opacity:1;transform:none}
@media(max-width:880px){
  .grid{grid-template-columns:1fr;gap:0;padding-top:34px}
  .toc{display:none}
  .stats{grid-template-columns:1fr}
  .stats div+div{border-left:0;border-top:1px solid var(--rule);padding-left:0}
  .card{grid-template-columns:1fr;gap:6px}
  .card .go{display:none}
  .nums{grid-template-columns:1fr 1fr}
  .nums div:nth-child(3){border-left:0;border-top:1px solid var(--rule);padding-left:0}
  .nums div:nth-child(4){border-top:1px solid var(--rule)}
  .lead::first-letter{font-size:52px}
  .tl .row{grid-template-columns:64px 1fr;gap:14px}
  .pcard{grid-template-columns:1fr;gap:4px}
}
</style></head>
<body>
<div class="masthead"><span><b>HOWTOGETRICH.NOW</b></span><span>A playbook in three skills</span><span>Vol. 01 · 2026</span></div>
<div class="page"><div class="grid">
  <main id="app"></main>
  <aside class="toc" id="toc"></aside>
</div></div>

<script>
const D = __DATA__;
const esc = s => String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;");
const NAV=[["top","Opening"],["shift","The shift"],["three","The three"],["paths","The paths"],
  ["pipeline","Patch log"],["combo","The combo"],["proof","Receipts"],["sprint","7-day sprint"],["warn","Warning"]];
document.getElementById("toc").innerHTML = `<div class="h">Contents</div>` +
  NAV.map(([id,l])=>`<a href="#${id}" data-id="${id}">${esc(l)}</a>`).join("");

let active=D.paths[0].id;
function pathHTML(p){
  return `<div class="rv">
    <div class="ptitle">${esc(p.name)}</div>
    <div class="ptag">${esc(p.tagline)}</div>
    <p>${esc(p.why)}</p>
    <div class="pm">${p.metrics.map(m=>`<div><b>${esc(m[0])}</b><span>${esc(m[1])}</span></div>`).join("")}</div>
    <div class="plabel">The playbook</div>
    <ol class="pb">${p.playbook.map(x=>`<li>${esc(x)}</li>`).join("")}</ol>
    <div class="plabel">Starter stack</div>
    <div class="chips">${p.stack.map(s=>`<span>${esc(s)}</span>`).join("")}</div>
    <div class="plabel">How the money works</div>
    <div class="money">${p.money.map(m=>`<div class="mr"><span>${esc(m[0])}</span><span>${esc(m[1])}</span></div>`).join("")}</div>
    <blockquote><p>“${esc(p.proof[0])}”</p><cite>${esc(p.proof[1])}</cite></blockquote>
  </div>`;
}

document.getElementById("app").innerHTML=`
<section class="hero" id="top">
  <div class="eyebrow">${esc(D.hero.eyebrow)}</div>
  <h1><span>How to get <em>rich</em></span><span>in 2026.</span></h1>
  <div class="sub">${esc(D.hero.sub)}</div>
  <div class="byline"><span>By ${esc(D.footer.brand)}</span><span>${esc(D.footer.domain)}</span><span>Living edition</span></div>
  <p class="lead">${esc(D.hero.lead)}</p>
  <div class="stats">${D.hero.stats.map(s=>`<div><b>${esc(s[0])}</b><span>${esc(s[1])}</span></div>`).join("")}</div>
</section>

<section class="sec" id="shift">
  <div class="kick">${esc(D.shift.num)} — ${esc(D.shift.kicker)}</div>
  <h2>${esc(D.shift.title)}</h2>
  <p>${esc(D.shift.body)}</p>
  <div class="tl">${D.shift.timeline.map(r=>`<div class="row rv"><div class="y">${esc(r[0])}</div><div><div class="k">${esc(r[1])}</div><p>${esc(r[2])}</p></div></div>`).join("")}</div>
</section>

<section class="sec" id="three">
  <div class="kick">${esc(D.three.num)} — ${esc(D.three.kicker)}</div>
  <h2>${esc(D.three.title)}</h2>
  <p class="dim">${esc(D.three.note)}</p>
  <div class="cards">${D.three.cards.map((c,i)=>`<div class="card rv" data-go="${D.paths[i].id}">
    <div class="role">${esc(c[0])}</div>
    <div><h3>${esc(c[1])}</h3><p>${esc(c[2])}</p></div>
    <div class="go">${esc(c[5])} →</div></div>`).join("")}</div>
</section>

<section class="sec" id="paths">
  <div class="kick">03 — The paths</div>
  <h2>Three roads. One destination.</h2>
  <div class="tabs" id="tabs">${D.paths.map(p=>`<button data-id="${p.id}" class="${p.id===active?"on":""}">${p.n} — ${esc(p.name.replace("THE ",""))}</button>`).join("")}</div>
  <div id="pathbody">${pathHTML(D.paths[0])}</div>
</section>

<section class="sec" id="pipeline">
  <div class="kick">${esc(D.pipeline.num)} — ${esc(D.pipeline.kicker)}</div>
  <h2>${esc(D.pipeline.title)}</h2>
  <p class="dim">${esc(D.pipeline.note)}</p>
  <div class="pipe">${D.pipeline.items.map(i=>`<div class="pcard rv"><div class="n">${esc(i[0])}</div><div><h4>${esc(i[1])}</h4><span class="st">${esc(i[2])}</span><p>${esc(i[3])}</p></div></div>`).join("")}</div>
</section>

<section class="sec" id="combo">
  <div class="kick">${esc(D.combo.num)} — ${esc(D.combo.kicker)}</div>
  <h2>${esc(D.combo.title)}</h2>
  <ol class="steps">${D.combo.steps.map(s=>`<li>${esc(s)}</li>`).join("")}</ol>
  <div class="pull">${esc(D.combo.line).replace("idea → product → distribution","<b>idea → product → distribution</b>")}</div>
  <p class="dim" style="margin-top:16px">${esc(D.combo.result)}</p>
</section>

<section class="sec" id="proof">
  <div class="kick">${esc(D.proof.num)} — ${esc(D.proof.kicker)}</div>
  <h2>${esc(D.proof.title)}</h2>
  <div class="nums">${D.proof.numbers.map(n=>`<div><b>${esc(n[0])}</b><span>${esc(n[1])}</span></div>`).join("")}</div>
  <p class="small">${esc(D.proof.note)}</p>
</section>

<section class="sec" id="sprint">
  <div class="kick">${esc(D.sprint.num)} — ${esc(D.sprint.kicker)}</div>
  <h2>${esc(D.sprint.title)}</h2>
  <ul class="sp" id="sp">${D.sprint.items.map((s,i)=>`<li data-i="${i}"><span class="box"></span><span class="txt"><span class="d">D${i+1}</span>${esc(s)}</span></li>`).join("")}</ul>
  <div class="spbar"><span id="sptxt">0 of 7 complete</span><i><b id="spfill"></b></i></div>
</section>

<section class="warn" id="warn">
  <div class="kick">${esc(D.warning.num)} — ${esc(D.warning.kicker)}</div>
  <h2>${esc(D.warning.title)}</h2>
  <p>${esc(D.warning.body)}</p>
  <p style="margin-top:12px">${esc(D.warning.close)}</p>
  <div class="rule">${esc(D.warning.rule)}</div>
</section>
<footer><span>${esc(D.footer.brand)} — ${esc(D.footer.note)}</span><span>${esc(D.footer.domain)}</span></footer>
`;

const tabs=document.getElementById("tabs");
tabs.addEventListener("click",e=>{
  const b=e.target.closest("button"); if(!b) return;
  active=b.dataset.id;
  tabs.querySelectorAll("button").forEach(x=>x.classList.toggle("on",x.dataset.id===active));
  const body=document.getElementById("pathbody");
  body.innerHTML=pathHTML(D.paths.find(p=>p.id===active));
  body.querySelector(".rv")?.classList.add("in");
});
document.querySelectorAll(".card").forEach(c=>c.addEventListener("click",()=>{
  const id=c.dataset.go;
  document.getElementById("paths").scrollIntoView({behavior:"smooth"});
  setTimeout(()=>{
    active=id;
    tabs.querySelectorAll("button").forEach(x=>x.classList.toggle("on",x.dataset.id===active));
    const body=document.getElementById("pathbody");
    body.innerHTML=pathHTML(D.paths.find(p=>p.id===active));
    body.querySelector(".rv")?.classList.add("in");
  },420);
}));
const KEY="htgr_sprint_c";
let done=[]; try{done=JSON.parse(localStorage.getItem(KEY)||"[]")}catch(e){done=[]}
const items=[...document.querySelectorAll("#sp li")];
function render(){
  let n=0;
  items.forEach(li=>{const on=done.includes(+li.dataset.i);li.classList.toggle("done",on);if(on)n++});
  document.getElementById("sptxt").textContent=`${n} of 7 complete`;
  document.getElementById("spfill").style.width=(n/7*100)+"%";
}
items.forEach(li=>li.addEventListener("click",()=>{
  const i=+li.dataset.i;
  done=done.includes(i)?done.filter(x=>x!==i):[...done,i];
  try{localStorage.setItem(KEY,JSON.stringify(done))}catch(e){}
  render();
}));
render();
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)e.target.classList.add("in")}),{threshold:.1});
document.querySelectorAll(".rv").forEach(e=>io.observe(e));
const nio=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){
  document.querySelectorAll(".toc a").forEach(a=>a.classList.toggle("on",a.dataset.id===e.target.id));
}}),{rootMargin:"-40% 0px -55% 0px"});
NAV.forEach(([id])=>{const s=document.getElementById(id);if(s)nio.observe(s)});
</script>
</body></html>
"""

variants = {
  "001-terminal-noir": A,
  "002-neon-brutalist": B,
  "003-quiet-editorial": C,
}
for name, tpl in variants.items():
    d = OUT / name
    d.mkdir(parents=True, exist_ok=True)
    html = tpl.replace("__DATA__", DATA_JSON)
    (d / "index.html").write_text(html, encoding="utf-8")
    print(f"wrote {d/'index.html'}  ({len(html)/1024:.1f} KB)")
