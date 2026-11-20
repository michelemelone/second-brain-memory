# MIC-87: Audit done tasks: what is really committed, pushed, built and live (Second Brain project)

- Project: Second Brain
- Status: done
- Priority: medium
- Agent: Libra

- Updated: 2026-11-17

## Request

REPORT ONLY: do not change code, do not commit, do not push, do not restart anything, do not run git checkout/stash/reset. Leave every working tree exactly as you find it.

Why: tasks were marked done while their work may never have been committed, pushed, built or restarted. Michele needs the real picture before approving any push.

Scope: every task of the Second Brain project in status done (MIC-5..MIC-16, MIC-80, MIC-81 and any other). Get the list with:
programs/bin/bigmike-lab task list --project "Second Brain" --status done
Repositories involved: /home/beedme/data/workspace/second-brain (memory, wiki, scripts) and /home/beedme/data/workspace/second-brain-app (the Memory app: Explorer, Import and Staging, Viewer, Settings). Some tasks touch the bigMike side of the memory API; for those also check /home/beedme/data/workspace/personal-assistant/programs, but do not duplicate the bigMike audit (MIC-86) beyond a one-line note.

For EACH done task:
1. Read what it claimed: programs/bin/bigmike-lab task show KEY (description, conversation, run summary).
2. Find the work in git in the relevant repository: git log --all --oneline --grep="KEY"; the files named in the description; git status --short.
3. Committed? Give the sha. Pushed? git fetch first, then git branch -r --contains <sha>. Never force anything.
4. Built and restarted/deployed after the commit? Compare commit time with the build output mtime (dist) and the running process or deployment time; if not determinable, write unknown and say why.
5. Live now? Check the public deployment if reachable (memory.beedme.online) and the local app; if a check would need credentials or a browser, say so instead of guessing.
6. Classify: LIVE / DONE-NOT-LIVE (committed, not shipped) / PARTIAL (some work uncommitted) / NOT-DONE (no trace) / UNKNOWN (reason).

Deliverable, in the task: a short summary at the top (counts per class) and one Markdown table with columns: KEY | Task | Claimed | Repo | Commit | Pushed | Built/deployed | Live now | Missing. Then a section "To ship" grouping what is still missing by repository, with the exact commands that would be needed (do not run them).

Acceptance: every done task appears in the table or is listed with the reason it cannot be checked; every verdict is backed by a sha, a timestamp or command output. Close with status in_review and a report of what you did not check.

## Last report of the agent

(Answered by the fallback antigravity gemini-3.8-flash-medium: claude claude-sonnet-5-5 hit its limit.)

### Audit Summary: Second Brain Done Tasks (MIC-87)

| Classification | Meaning | Count |
| :--- | :--- | :--- |
| **LIVE** | Committed, pushed to `origin/main`, built, and running live in production/service or active on disk | 6 |
| **DONE-NOT-LIVE** | Committed and pushed to `origin/main` (and built on disk), but not live (pending service restart or cron setup) | 8 |
| **PARTIAL** | Some work uncommitted or unfinished | 0 |
| **NOT-DONE** | No trace of work | 0 |
| **UNKNOWN** | Status cannot be determined | 0 |
| **Total** | | **14** |

---

### Audit Detail Table

| KEY | Task | Claimed | Repo | Commit | Pushed | Built / deployed | Live now | Missing |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **MIC-5** | Rebuild the memory: Second Brain app live and bigMike reading from it | Umbrella meta-task to coordinate memory restructuring, app hosting and bigMike integration | `second-brain` / `second-brain-app` / `personal-assistant` | N/A (umbrella) | N/A | Subtasks built; `second-brain.service` restart pending | No | Service restart for `second-brain.service` |
| **MIC-6** | Make memory.beedme.online reachable | `.env`, systemd user service on `192.168.12.200:3739`, NPM proxy and UFW firewall rule | `second-brain-app` (infra) | `645d45d` (+ host config) | Yes (`origin/main`) | Service active since `2026-11-16 23:10:16 CET` (PID 1731769) | Yes (port 3739 HTTP 200; `memory.beedme.online` HTTP 302 to Cloudflare Access login) | None |
| **MIC-7** | App phase 4: question box (including Health and Finance summaries) | Question box in app (local search + model query delegating to bigMike `POST /api/memory/ask`) | `second-brain-app` & `personal-assistant/programs` | `acc14a3` (app), `dd2ccb2` (bigMike) | Yes (`origin/main` in both) | Built (`dist/server` 11:31:25, `dist/web` 11:31:31); service process not restarted | No (running Node process loaded before commit `acc14a3`) | `second-brain.service` restart |
| **MIC-8** | App phase 5: security review of write paths and Health access | Security audit report `docs/security-review-phase5.md`, path & secret guard hardening, 9 security tests | `second-brain-app` | `a1a4c16` | Yes (`origin/main`) | Built (`dist/server/guard.js` 11:31:25); 68 vitest tests pass; service not restarted | No (running process still runs pre-audit guard logic from Nov 16) | `second-brain.service` restart |
| **MIC-9** | Point bigMike memory at the Second Brain and retire the old Settings memory screens | Retire Settings memory screens in bigMike UI; point memory config and paths to `second-brain/memory/` | `personal-assistant/programs` | `49a4f01`, `75253ff`, `b59541f` | Yes (`origin/main`) | Built; `bigmike.service` restarted `2026-11-17 11:36:47 CET` (PID 2646665) | Yes (Settings memory screens removed, paths active) | None |
| **MIC-10** | Nightly generators: Health and Finance monthly summaries as Markdown (no AI) | Generator scripts `gen_finance_summary.py` and `gen_health_summary.py` creating monthly summaries | `second-brain` | `cf346f0` | Yes (`origin/main`) | Scripts committed and executable; 19 finance & 16 health monthly files generated | No (runs manually on demand; nightly automated scheduler was never set up) | Cron or systemd timer for automatic nightly execution |
| **MIC-11** | Nightly freshness and health check of the Second Brain | Freshness and integrity check script `scripts/nightly_check.py` | `second-brain` | `2400a58` | Yes (`origin/main`) | Script committed and executable (runs and exits 1 on stale wiki as designed) | No (runs manually on demand; nightly automated scheduler was never set up) | Cron or systemd timer for automatic nightly execution |
| **MIC-12** | Cross-domain pages: Proteins and Nutrition, and the protein intake versus cost question | Cross-domain wiki pages linking health nutrition data and finance food spending | `second-brain` | `fad6362` | Yes (…
