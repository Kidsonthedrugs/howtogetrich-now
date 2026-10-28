import pathlib, re, subprocess, os, json, copy

ROOT = pathlib.Path(r"C:/Users/EasyMoneySniper/howtogetrich")
CH = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
TMP = ROOT / "shots" / "_probe"
TMP.mkdir(parents=True, exist_ok=True)

PROBE = r"""
<script>
window.addEventListener('load', () => {
  const R = {};
  const de = document.documentElement;
  R.overflowX = de.scrollWidth - de.clientWidth;
  R.scrollH = document.body.scrollHeight;
  R.hasHScroll = de.scrollWidth > de.clientWidth + 1;

  // sections with height 0 or huge
  R.sections = [...document.querySelectorAll('section')].map(s => {
    const r = s.getBoundingClientRect();
    return {id: s.id || '(none)', h: Math.round(r.height), w: Math.round(r.width)};
  }).filter(s => s.id !== '(none)');

  // any element wider than viewport
  const vw = de.clientWidth;
  R.wide = [...document.querySelectorAll('body *')].filter(e => {
    const r = e.getBoundingClientRect();
    if (r.width === 0) return false;
    return r.right > vw + 4 && getComputedStyle(e).position !== 'fixed';
  }).slice(0, 8).map(e => e.tagName + '.' + (e.className||'').toString().slice(0,24) + ' w=' + Math.round(e.getBoundingClientRect().width));

  // text overflow / clipping checks
  R.clipped = [...document.querySelectorAll('h1,h2,h3,li,p,span,button,div.ptitle,div.ptag')].filter(e => {
    const cs = getComputedStyle(e);
    if (cs.overflow === 'hidden' || cs.textOverflow === 'ellipsis') return e.scrollWidth > e.clientWidth + 2;
    return false;
  }).slice(0,6).map(e => e.tagName + ' "' + e.textContent.trim().slice(0,26) + '"');

  // key element fonts
  const q = s => document.querySelector(s);
  const f = s => { const e=q(s); if(!e) return 'MISSING'; const cs=getComputedStyle(e); return cs.fontSize+'/'+cs.fontWeight+' '+cs.fontFamily.split(',')[0]; };
  R.fonts = {h1: f('h1'), h2: f('h2'), kick: f('.kick, .snum, .eyebrow'), body: f('body')};

  // colors sanity (not default black-on-white unless intended)
  const bcs = getComputedStyle(document.body);
  R.colors = {bg: bcs.backgroundColor, fg: bcs.color};

  // counts of interactive bits
  R.counts = {
    cards: document.querySelectorAll('.card').length,
    tabs: document.querySelectorAll('.tabs button').length,
    tabsOn: document.querySelectorAll('.tabs button.on').length,
    sprint: document.querySelectorAll('.sp li').length,
    playbook: document.querySelectorAll('ol.pb li').length,
    money: document.querySelectorAll('.money .mr').length,
    chips: document.querySelectorAll('.chips span').length,
    nums: document.querySelectorAll('.nums div').length,
    steps: document.querySelectorAll('.steps li').length,
    pipe: document.querySelectorAll('.pcard').length
  };

  // ---- interaction test: switch to clipper tab ----
  const btn = [...document.querySelectorAll('.tabs button')].find(b => b.dataset.id === 'clipper');
  if (btn) {
    btn.click();
    const body = document.getElementById('pathbody');
    R.tabSwitch = {title: (body.querySelector('.ptitle')||{}).textContent, playbook: body.querySelectorAll('ol.pb li').length,
                   hasEmpty: body.textContent.trim().length < 100};
  } else R.tabSwitch = 'NO TABS';

  // ---- interaction test: sprint toggle ----
  const li = document.querySelector('.sp li');
  if (li) { li.click(); R.sprintToggle = {done: li.classList.contains('done'), counter: (document.getElementById('sptxt')||{}).textContent}; }

  // ---- card click wiring ----
  const c = document.querySelector('.card');
  R.cardWired = !!c && !!c.dataset.go;

  // ---- blank area detection: biggest vertical gap between sibling blocks
  R.emptyish = R.sections.filter(s => s.h < 40).map(s => s.id);

  // ---- no-results / placeholder strings
  const t = document.body.innerText;
  R.leaks = ['undefined','NaN','${','[object','lorem','TODO'].filter(k => t.includes(k));

  const pre = document.createElement('pre');
  pre.id = 'PROBE_RESULT';
  pre.textContent = '###' + JSON.stringify(R) + '###';
  document.body.appendChild(pre);
});
</script>
"""

results = {}
for d in sorted((ROOT / "sketches").iterdir()):
    if not d.is_dir():
        continue
    src = (d / "index.html").read_text(encoding="utf-8")
    probed = src.replace("</body>", PROBE + "</body>")
    out = TMP / f"{d.name}.probe.html"
    out.write_text(probed, encoding="utf-8")
    p = subprocess.run([CH, "--headless=new", "--disable-gpu", "--allow-file-access-from-files",
                        "--virtual-time-budget=4000", "--window-size=1440,1000",
                        "--dump-dom", out.as_uri()],
                       capture_output=True, text=True, encoding="utf-8", errors="ignore")
    m = re.search(r'<pre id="PROBE_RESULT">(.*?)</pre>', p.stdout, re.S)
    if not m:
        results[d.name] = {"ERROR": "probe did not run", "stderr": p.stderr[-300:]}
        continue
    import html as _h
    raw = _h.unescape(m.group(1)).strip()
    raw = raw.replace('###','').strip()
    try:
        results[d.name] = json.loads(raw)
    except Exception as e:
        results[d.name] = {"ERROR": f"json: {e}", "raw": raw[:400]}

print(json.dumps(results, indent=1, ensure_ascii=False))
(ROOT / "shots" / "probe-report.json").write_text(json.dumps(results, indent=1, ensure_ascii=False), encoding="utf-8")
