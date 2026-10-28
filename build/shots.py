import pathlib, subprocess, json

ROOT = pathlib.Path(r"C:/Users/EasyMoneySniper/howtogetrich")
CH = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
SHOTS = ROOT / "shots"
SHOTS.mkdir(exist_ok=True)

V = ["001-terminal-noir", "002-neon-brutalist", "003-quiet-editorial"]
# (suffix, hash, height)
TARGETS = [
    ("hero", "", 1180),
    ("paths", "#paths", 1180),
    ("combo", "#combo", 1180),
    ("warn", "#warn", 900),
]

for name in V:
    url = (ROOT / "sketches" / name / "index.html").as_uri()
    for suffix, h, height in TARGETS:
        out = SHOTS / f"{name}-{suffix}.png"
        subprocess.run([CH, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--allow-file-access-from-files", "--force-device-scale-factor=1",
                        "--virtual-time-budget=3500",
                        f"--window-size=1400,{height}",
                        f"--screenshot={out.as_posix()}",
                        url + h],
                       capture_output=True, text=True)
        print(name, suffix, out.exists(), out.stat().st_size if out.exists() else 0)

# mobile shots
for name in V:
    url = (ROOT / "sketches" / name / "index.html").as_uri()
    out = SHOTS / f"{name}-mobile.png"
    subprocess.run([CH, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--allow-file-access-from-files", "--force-device-scale-factor=2",
                    "--virtual-time-budget=3000", "--window-size=420,900",
                    f"--screenshot={out.as_posix()}", url],
                   capture_output=True, text=True)
    print(name, "mobile", out.exists(), out.stat().st_size if out.exists() else 0)
