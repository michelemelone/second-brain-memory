# MIC-11: Nightly freshness and health check of the Second Brain

- Project: Second Brain
- Status: done
- Priority: medium
- Agent: Sirius
- Parent: MIC-5
- Updated: 2026-11-17

## Request

A script that checks the folder is committed and pushed, the wiki was updated, no secret or database file is inside, and the app answers. It reports only when something is wrong.

## Last report of the agent

**Report MIC-11**

**Done**
- I added `scripts/nightly_check.py`. It uses only the Python standard library and makes no model call. It prints nothing and exits 0 when all is well. On a problem it prints one line per issue and exits 1.
- It checks:
  - **Git:** both repos (`second-brain` and `memory/bigmike`) for uncommitted changes, a missing remote, commits not pushed, and being behind the remote.
  - **Wiki:** `wiki/` and `memory/bigmike/wiki` were updated within 3 days. You can change this with `WIKI_MAX_AGE_DAYS`.
  - **Forbidden files:** `.env*`, `master.key`, `api-keys.json`, `login.json`, databases (`.db`, `.sqlite`), keys and `.log` files anywhere in the folder.
  - **App:** bigMike answers over HTTP on port 3738. It tries 127.0.0.1 first, then 192.168.12.200. Any HTTP reply counts as answering.
- I committed and pushed it.

**Result of the first run**
- It found one real problem: `memory/bigmike/wiki` was last updated 3.5 days ago. Its `log.md` was last written on Nov 13.
- The other checks passed: git clean and pushed, no forbidden files, and the app answers.

**Not done**
- **Scheduling:** I did not schedule the script. Nothing runs by itself, and I can't create a cron job or systemd timer from here.
- **Notification:** I did not wire up any notification. Whoever runs it decides how to show the output.

**Assumptions**
- bigMike listens on port 3738. This is the default in its `config.ts`. It is bound to 192.168.12.200, not to 127.0.0.1.
- The central `wiki/` currently holds only `SCHEMA.md`. It counts as fresh because that file was recently touched.

**Left for you**
- Decide how to run it nightly, for example a cron entry that mails or notifies only when output is non-empty.
- Check why the bigMike wiki has not been updated since Nov 13.

How to check: run `python3 -I /home/beedme/data/workspace/second-brain/scripts/nightly_check.py; echo $?`. It should list the stale-wiki line and exit 1. After the wiki is updated, it should print nothing and exit 0.
