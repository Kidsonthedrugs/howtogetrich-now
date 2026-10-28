import pathlib, shutil, json, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from data import DATA

ROOT = pathlib.Path(r"C:/Users/EasyMoneySniper/howtogetrich")
DEP = ROOT / "deploy"
DEP.mkdir(exist_ok=True)
(DEP / "_headers").write_text("""/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: geolocation=(), microphone=(), camera=()

/og.png
  Cache-Control: public, max-age=31536000, immutable

/index.html
  Cache-Control: public, max-age=0, must-revalidate
""", encoding="utf-8")

shutil.copy(ROOT / "index.html", DEP / "index.html")
if (ROOT / "og.png").exists():
    shutil.copy(ROOT / "og.png", DEP / "og.png")

sitemap = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://howtogetrich.now/</loc>
    <lastmod>2026-10-28</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
"""
(DEP / "sitemap.xml").write_text(sitemap, encoding="utf-8")

# 404 -> redirect to home (SPA-ish, single page)
(DEP / "404.html").write_text("""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Not found — howtogetrich.now</title>
<meta name="robots" content="noindex">
<style>
body{margin:0;min-height:100vh;display:grid;place-items:center;background:#0A0A0A;color:#fff;
 font-family:"Segoe UI",Inter,system-ui,sans-serif;text-align:center;padding:24px}
h1{font-size:clamp(56px,14vw,140px);line-height:.85;margin:0 0 18px;font-weight:900;letter-spacing:-.05em;text-transform:uppercase}
h1 span{color:#FF3B00}
p{color:#A2A2A2;font-family:ui-monospace,Consolas,monospace;font-size:13px;letter-spacing:.12em;text-transform:uppercase}
a{display:inline-block;margin-top:26px;background:#F2FF3B;color:#000;font-family:ui-monospace,Consolas,monospace;
 font-weight:700;font-size:12px;letter-spacing:.14em;text-transform:uppercase;padding:13px 18px;
 border:3px solid #000;box-shadow:6px 6px 0 #fff;text-decoration:none}
</style></head><body><div>
<h1>4<span>0</span>4</h1>
<p>This page doesn't exist. The playbook does.</p>
<a href="/">Back to the playbook</a>
</div></body></html>""", encoding="utf-8")

files = sorted(p.name for p in DEP.iterdir() if p.is_file())
print("deploy/:", files)
for f in files:
    print(f"  {f:16} {(DEP/f).stat().st_size/1024:6.1f} KB")
