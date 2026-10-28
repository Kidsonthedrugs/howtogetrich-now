import pathlib, re, subprocess, json

ROOT = pathlib.Path(r"C:/Users/EasyMoneySniper/howtogetrich")
CH = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
TMP = ROOT / "shots" / "_probe"

PROBE = r"""
<script>
window.addEventListener('load', () => {
  const R = {}, de = document.documentElement, vw = de.clientWidth;
  R.vw = vw;
  R.overflowX = de.scrollWidth - de.clientWidth;
  R.h1 = (()=>{const e=document.querySelector('h1');const r=e.getBoundingClientRect();return {fs:getComputedStyle(e).fontSize,w:Math.round(r.width),h:Math.round(r.height)};})();
  // elements overflowing right edge (excluding fixed)
  R.wide = [...document.querySelectorAll('body *')].filter(e=>{
    const cs=getComputedStyle(e); if(cs.position==='fixed'||cs.display==='none') return false;
    const r=e.getBoundingClientRect(); return r.width>vw+2 && r.height>0;
  }).slice(0,6).map(e=>e.tagName+'.'+String(e.className).slice(0,20)+' w='+Math.round(e.getBoundingClientRect().width));
  // text clipped horizontally
  R.clipped = [...document.querySelectorAll('h1,h2,h3,h4,p,li,button,.nums b,.hstats b')].filter(e=>{
    const r=e.getBoundingClientRect();
    return e.scrollWidth > e.clientWidth + 2 && r.width>0;
  }).slice(0,6).map(e=>e.tagName+':'+e.textContent.trim().slice(0,30)+' ('+e.scrollWidth+'>'+e.clientWidth+')');
  // tap targets smaller than 24px
  R.smallTap = [...document.querySelectorAll('button,a,.card,.sp li')].filter(e=>{
    const r=e.getBoundingClientRect(); return r.height>0 && (r.height<24 || r.width<24);
  }).slice(0,6).map(e=>e.tagName+' '+Math.round(e.getBoundingClientRect().width)+'x'+Math.round(e.getBoundingClientRect().height));
  R.fontSizes = [...new Set([...document.querySelectorAll('p,li,span,div')].map(e=>parseFloat(getComputedStyle(e).fontSize)))].filter(n=>n<11).length;
  R.scrollH = document.body.scrollHeight;
  R.counts = {cards:document.querySelectorAll('.card').length, sprint:document.querySelectorAll('.sp li').length, tabs:document.querySelectorAll('.tabs button').length};
  const t=document.body.innerText; R.leaks=['undefined','NaN','${','[object'].filter(k=>t.includes(k));
  const pre=document.createElement('pre'); pre.id='PROBE_RESULT';
  pre.textContent=JSON.stringify(R); document.body.appendChild(pre);
});
</script>
"""

for width in (390, 768):
    print(f"\n===== viewport {width}px =====")
    for d in sorted((ROOT / "sketches").iterdir()):
        if not d.is_dir(): continue
        src = (d / "index.html").read_text(encoding="utf-8").replace("</body>", PROBE + "</body>")
        out = TMP / f"{d.name}.m{width}.html"
        out.write_text(src, encoding="utf-8")
        p = subprocess.run([CH, "--headless=new", "--disable-gpu", "--allow-file-access-from-files",
                            "--virtual-time-budget=4000", f"--window-size={width},900",
                            "--dump-dom", out.as_uri()],
                           capture_output=True, text=True, encoding="utf-8", errors="ignore")
        m = re.search(r'<pre id="PROBE_RESULT">(.*?)</pre>', p.stdout, re.S)
        if not m:
            print(" ", d.name, "PROBE FAILED"); continue
        import html as _h
        r = json.loads(_h.unescape(m.group(1)))
        print(" ", d.name, json.dumps(r, ensure_ascii=False))
