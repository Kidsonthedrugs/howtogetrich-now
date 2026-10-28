"""Real narrow-viewport verification: load index.html inside an iframe of an exact size."""
import pathlib, re, subprocess, json, html as H

ROOT = pathlib.Path(r"C:/Users/EasyMoneySniper/howtogetrich")
CH = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
TMP = ROOT / "shots" / "_probe"
TMP.mkdir(parents=True, exist_ok=True)

WRAPPER = """<!doctype html><html><head><meta charset="utf-8"><style>
html,body{margin:0;padding:0;background:#333}
iframe{border:0;display:block;width:%(w)dpx;height:%(h)dpx}
</style></head><body>
<iframe id="f" src="%(src)s"></iframe>
<script>
const RESULT = {};
document.getElementById('f').addEventListener('load', () => {
  setTimeout(() => {
    const f = document.getElementById('f');
    const d = f.contentDocument, w = f.contentWindow;
    const de = d.documentElement;
    RESULT.vw = de.clientWidth;
    RESULT.overflowX = de.scrollWidth - de.clientWidth;
    RESULT.scrollH = d.body.scrollHeight;
    RESULT.hasHScroll = de.scrollWidth > de.clientWidth + 1;
    const h1 = d.querySelector('h1');
    RESULT.h1 = {fs: getComputedStyle(h1).fontSize, w: Math.round(h1.getBoundingClientRect().width)};
    RESULT.wide = [...d.querySelectorAll('body *')].filter(e=>{
      const cs = w.getComputedStyle(e);
      if(cs.position==='fixed'||cs.display==='none') return false;
      return e.getBoundingClientRect().width > de.clientWidth+2;
    }).slice(0,6).map(e=>e.tagName+'.'+String(e.className).slice(0,16)+':'+Math.round(e.getBoundingClientRect().width));
    RESULT.clipped = [...d.querySelectorAll('h1,h2,h3,h4,p,li,span,button')].filter(e=>
      e.scrollWidth > e.clientWidth+2 && e.getBoundingClientRect().width>0
    ).slice(0,6).map(e=>e.tagName+':'+e.textContent.trim().slice(0,24));
    RESULT.smallTap = [...d.querySelectorAll('a,button,.card,.sp li')].filter(e=>{
      const r=e.getBoundingClientRect(); return r.height>0 && (r.height<44||r.width<44);
    }).slice(0,10).map(e=>e.tagName+' '+Math.round(e.getBoundingClientRect().width)+'x'+Math.round(e.getBoundingClientRect().height));
    RESULT.jumpScroll = (()=>{const j=d.querySelector('.jump'); return j? {sw:j.scrollWidth, cw:j.clientWidth, overflow:j.scrollWidth>j.clientWidth+1}:null;})();
    RESULT.counts = {cards:d.querySelectorAll('.card').length, tabs:d.querySelectorAll('.tabs button').length,
      sprint:d.querySelectorAll('.sp li').length, steps:d.querySelectorAll('ol.pb li').length};
    // mobile stacking sanity: pgrid should be 1 column under 860
    const pg = d.querySelector('.pgrid');
    RESULT.pgridCols = pg ? w.getComputedStyle(pg).gridTemplateColumns : null;
    RESULT.leaks = ['undefined','NaN','${','[object Object]'].filter(k=>d.body.innerText.includes(k));
    const pre = document.createElement('pre'); pre.id='R'; pre.textContent = JSON.stringify(RESULT);
    document.body.appendChild(pre);
  }, 700);
});
</script></body></html>"""

def measure(w, h=900):
    src = (ROOT / "index.html").as_uri()
    page = TMP / f"wrap_{w}.html"
    page.write_text(WRAPPER % {"w": w, "h": h, "src": src}, encoding="utf-8")
    p = subprocess.run([CH, "--headless=new", "--disable-gpu", "--allow-file-access-from-files",
                        "--virtual-time-budget=6000", "--window-size=1600,1400",
                        "--dump-dom", page.as_uri()],
                       capture_output=True, text=True, encoding="utf-8", errors="ignore")
    m = re.search(r'<pre id="R">(.*?)</pre>', p.stdout, re.S)
    if not m:
        return {"ERROR": "no result", "stderr": p.stderr[-200:]}
    return json.loads(H.unescape(m.group(1)))

ok = True
for w in (390, 375, 360, 320, 414, 768, 834):
    r = measure(w)
    if "ERROR" in r:
        print(w, "FAILED", r); ok = False; continue
    flag = "OK " if (r["overflowX"] == 0 and not r["wide"] and not r["clipped"] and not r["leaks"]) else "!! "
    if flag != "OK ": ok = False
    print(f"{flag}{w:>4}px vw={r['vw']:>3} overX={r['overflowX']} scrollH={r['scrollH']:>5} "
          f"h1={r['h1']['fs']:>6} wide={len(r['wide'])} clip={len(r['clipped'])} leak={r['leaks']} "
          f"jumpSW={r['jumpScroll']} pgCols={(r['pgridCols'] or '')[:26]}")
    if r["wide"]: print("      WIDE:", r["wide"])
    if r["clipped"]: print("      CLIP:", r["clipped"])
    if r["smallTap"]: print("      TAP<44:", r["smallTap"][:6])
print("\nALL PASS" if ok else "\nISSUES FOUND")
