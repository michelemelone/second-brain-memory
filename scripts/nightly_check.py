#!/usr/bin/env python3
"""Nightly freshness and health check of the Second Brain (MIC-11).

Standard library only, no model call. Silent (exit 0) when all is well.
Prints one line per problem and exits 1 otherwise.

Checks:
  1. Git: each repo is clean, has a remote, and has nothing unpushed or behind.
  2. Wiki: wiki/ (central) and memory/bigmike/wiki were updated recently.
  3. No secret or database file is inside the folder.
  4. bigMike answers over HTTP.

Env: BIGMIKE_URLS (comma list, default 127.0.0.1 and 192.168.12.200 on port 3738),
     WIKI_MAX_AGE_DAYS (default 3).
"""
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPOS = [ROOT, ROOT / "memory" / "bigmike"]
WIKIS = [ROOT / "memory" / "bigmike" / "wiki"]  # filled by the nightly job
CENTRAL_WIKI = ROOT / "wiki"
MAX_AGE = float(os.environ.get("WIKI_MAX_AGE_DAYS", "3")) * 86400
URLS = os.environ.get(
    "BIGMIKE_URLS", "http://127.0.0.1:3738,http://192.168.12.200:3738"
).split(",")

BAD_NAMES = {".env", "api-keys.json", "login.json", "master.key", "id_rsa", "id_ed25519"}
BAD_SUFFIXES = {".db", ".sqlite", ".sqlite3", ".db-wal", ".db-shm", ".pem", ".key", ".log"}
SKIP_DIRS = {".git", "node_modules"}

problems = []


def git(repo, *args):
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, timeout=60)
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def check_git(repo):
    name = repo.relative_to(ROOT) if repo != ROOT else Path(".")
    if not (repo / ".git").exists():
        problems.append(f"git: {name} is not a git repository")
        return
    _, out, _ = git(repo, "status", "--porcelain")
    if out:
        problems.append(f"git: {name} has {len(out.splitlines())} uncommitted change(s)")
    if not git(repo, "remote")[1]:
        problems.append(f"git: {name} has no remote")
        return
    git(repo, "fetch", "--quiet")
    rc, out, err = git(repo, "rev-list", "--left-right", "--count", "HEAD...@{u}")
    if rc != 0:
        problems.append(f"git: {name} has no upstream branch ({err[:80]})")
        return
    ahead, behind = map(int, out.split())
    if ahead:
        problems.append(f"git: {name} has {ahead} commit(s) not pushed")
    if behind:
        problems.append(f"git: {name} is {behind} commit(s) behind the remote")


def newest_mtime(path):
    newest = 0.0
    for p in path.rglob("*"):
        if p.is_file() and ".git" not in p.parts:
            newest = max(newest, p.stat().st_mtime)
    return newest


def check_wiki(path):
    if not path.is_dir():
        problems.append(f"wiki: {path.relative_to(ROOT)} is missing")
        return
    newest = newest_mtime(path)
    if newest == 0:
        problems.append(f"wiki: {path.relative_to(ROOT)} is empty")
    elif time.time() - newest > MAX_AGE:
        days = (time.time() - newest) / 86400
        problems.append(f"wiki: {path.relative_to(ROOT)} not updated for {days:.1f} days")


def check_forbidden():
    for dirpath, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            low = f.lower()
            if low in BAD_NAMES or any(low.endswith(s) for s in BAD_SUFFIXES) or low.startswith(".env"):
                problems.append(f"secret/db: forbidden file {Path(dirpath, f).relative_to(ROOT)}")


def check_app():
    for url in URLS:
        try:
            urllib.request.urlopen(url.strip(), timeout=10)
            return
        except urllib.error.HTTPError:
            return  # the server answered
        except Exception:
            continue
    problems.append(f"app: bigMike does not answer on {', '.join(u.strip() for u in URLS)}")


for r in REPOS:
    check_git(r)
for w in WIKIS + [CENTRAL_WIKI]:
    check_wiki(w)
check_forbidden()
check_app()

if problems:
    print("Second Brain check: %d problem(s)" % len(problems))
    for p in problems:
        print("- " + p)
    sys.exit(1)
