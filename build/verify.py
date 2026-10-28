import pathlib, re, subprocess, json, html as H

ROOT = pathlib.Path(r"C:/Users/EasyMoneySniper/howtogetrich")
CH = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
TMP = ROOT / "shots" / "_probe"
TMP.mkdir(parents=True, exist_ok=True)

PROBE = r"""
<script>
window.addEventListener('load', () => {
  const R = {}, de = document.documentElement, vw = de.clientWidth;
  R.vw = vw; R.overflowX = de.scrollWidth - de.clientWidth;
  R.scrollH = document.body.scrollHeight;
  R.h1 = (()=>{const e=document.querySelector('h1');const r=e.getBoundingClientRect();
    return {fs:getComputedStyle(e).fontSize, w:Math.round(r.width)};})();
  R.wide = [...document.querySelectorAll('body *')].filter(e=>{
    const cs=getComputedStyle(e); if(cs.position==='fixed'||cs.display==='none') return false;
    return e.getBoundingClientRect().width > vw+2;
  }).slice(0,6).map(e=>e.tagName+'.'+String(e.className).slice(0,18));
  R.clipped = [...document.querySelectorAll('h1,h2,h3,h4,p,li,button,span')].filter(e=>
    e.scrollWidth > e.clientWidth+2 && e.getBoundingClientRect().width>0
  ).slice(0,6).map(e=>e.tagName+':'+e.textContent.trim().slice(0,26));
  R.smallTap = [...document.querySelectorAll('button,a,.card,.sp li,.jump a')].filter(e=>{
    const r=e.getBoundingClientRect(); return r.height>0 && (r.height<40);
  }).slice(0,8).map(e=>e.tagName+' '+Math.round(e.getBoundingClientRect().width)+'x'+Math.round(e.getBoundingClientRect().height));
  R.counts = {cards:document.querySelectorAll('.card').length, tabs:document.querySelectorAll('.tabs button').length,
              sprint:document.querySelectorAll('.sp li').length, playbook:document.querySelectorAll('ol.pb li').length,
              money:document.querySelectorAll('.money .mr').length, jump:document.querySelectorAll('.jump a').length};
  // a11y basics
  R.a11y = {
    h1: document.querySelectorAll('h1').length,
    h2: document.querySelectorAll('h2').length,
    imgNoAlt: [...document.querySelectorAll('img')].filter(i=>!i.hasAttribute('alt')).length,
    btnNoLabel: [...document.querySelectorAll('button')].filter(b=>!b.textContent.trim() && !b.getAttribute('aria-label')).length,
    linkNoText: [...document.querySelectorAll('a')].filter(a=>!a.textContent.trim() && !a.getAttribute('aria-label')).length,
    tabsHaveRoles: document.querySelectorAll('[role=tab]').length,
    tabpanel: document.querySelectorAll('[role=tabpanel]').length,
    checkboxes: document.querySelectorAll('[role=checkbox]').length
  };
  // meta
  const g = n => { const m=document.querySelector(`meta[property="${n}"],meta[name="${n}"]`); return m?m.content:null; };
  R.meta = {title:document.title, desc:(g('description')||'').slice(0,60), og:g('og:title'), ogimg:g('og:image'),
            twcard:g('twitter:card'), canonical:(document.querySelector('link[rel=canonical]')||{}).href,
            ldjson:!!document.querySelector('script[type="application/ld+json"]')};
  // interactions
  const t2 = [...document.querySelectorAll('.tabs button')].find(b=>b.dataset.id==='coder');
  if(t2){ t2.click(); R.tabSwitch={title:(document.querySelector('#pathbody .ptitle')||{}).textContent,
            steps:document.querySelectorAll('#pathbody ol.pb li').length,
            aria:t2.getAttribute('aria-selected')}; }
  const li = document.querySelector('.sp li');
  if(li){ li.click(); R.sprint={done:li.classList.contains('done'), aria:li.getAttribute('aria-checked'),
            counter:document.getElementById('sptxt').textContent}; }
  // measure top offsets for nav accuracy
  R.offsets = [...document.querySelectorAll('section[id],#warn')].map(s=>({id:s.id||'warn', top:Math.round(s.offsetTop)}));
  R.leaks = ['undefined','NaN','${','[object Object]'].filter(k=>document.body.innerText.includes(k));
  // reduced motion emulation flag
  R.reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const pre=document.createElement('pre'); pre.id='PROBE_RESULT';
  pre.textContent=JSON.stringify(R); document.body.appendChild(pre);
});
</script>
"""

def run(width, extra_args=None):
    out = {}
    pr = TMP / f"final.m{width}.html"
    src = (ROOT/"index.html").read_text(encoding="utf-8").replace("</body>", PROBE+"</body>")
    pr.write_text(src, encoding="utf-8")
    args = [CH,"--headless=new","--disable-gpu","--allow-file-access-from-files",
            "--virtual-time-budget=4000",f"--window-size={width},900","--dump-dom"]
    if extra_args: args += extra_args
    p = subprocess.run(args+[pr.as_uri()], capture_output=True, text=True, encoding="utf-8", errors="ignore")
    m = re.search(r'<pre id="PROBE_RESULT">(.*?)</pre>', p.stdout, re.S)
    if not m: return {"ERROR":"probe failed","err":p.stderr[-200:]}
    return json.loads(H.unescape(m.group(1)))

for w in (1440, 1024, 768, 430, 390, 360):
    print(f"── {w}px ──")
    print(json.dumps(run(w), ensure_ascii=False, indent=1))
