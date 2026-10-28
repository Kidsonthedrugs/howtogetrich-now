import json, os, pathlib, subprocess, sys

TOK = pathlib.Path(os.path.expandvars(r"$LOCALAPPDATA/Temp/gh_tok.txt")).read_text().strip()
PROXY = "socks5h://127.0.0.1:10808"
API = "https://api.github.com"

def gh(method, path, payload=None, raw=False):
    cmd = ["curl", "-s", "-m", "40", "-x", PROXY, "-X", method,
           "-H", f"Authorization: token {TOK}",
           "-H", "Accept: application/vnd.github+json",
           "-H", "X-GitHub-Api-Version: 2022-11-28",
           "-H", "Content-Type: application/json",
           API + path]
    if payload is not None:
        cmd += ["--data-binary", json.dumps(payload)]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    if raw:
        return r.stdout
    try:
        return json.loads(r.stdout)
    except Exception:
        return {"_raw": r.stdout[:600], "_code": r.returncode}

if __name__ == "__main__":
    who = gh("GET", "/user")
    print("auth:", who.get("login"))
    repo = gh("GET", "/repos/Kidsonthedrugs/howtogetrich-now")
    if repo.get("full_name"):
        print("repo exists:", repo["full_name"], repo["html_url"])
    else:
        made = gh("POST", "/user/repos", {
            "name": "howtogetrich-now",
            "description": "howtogetrich.now - single-page playbook: Creator, Clipper, Vibe Coder",
            "private": False,
            "has_issues": True,
            "has_wiki": False,
            "auto_init": False,
        })
        print("create:", made.get("full_name") or made)
