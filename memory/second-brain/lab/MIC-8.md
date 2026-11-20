# MIC-8: App phase 5: security review of write paths and Health access

- Project: Second Brain
- Status: done
- Priority: medium
- Agent: Pegasus
- Parent: MIC-5
- Updated: 2026-11-17

## Request

Review the guard (paths, secrets, git commits), the Cloudflare Access check, and what the app can read of Health. Tests plus a written report. Do it before the app writes anything important.

## Last report of the agent

MIC-8 is done: the review report is written, two small fixes are applied, and everything is committed (a1a4c16) and pushed. The full suite passes (65 tests, 9 of them new) and `npm run build` succeeds. I didn't restart or deploy anything.

**What I found**

| Area | Finding | Result |
|---|---|---|
| Guard | Names with a prefix, such as `DB_PASSWORD=`, `MY_API_KEY=` and `GITHUB_TOKEN:`, were not caught. | Fixed, with a test |
| Git | File names go into git commands as pathspecs, so a name like `:(glob)*.md` could be read as a pattern. I could not make it commit other files. | Hardened with `--literal-pathspecs` on add, diff and commit |
| Guard | Images and PDFs stored as they are, file names, and encoded secrets are not scanned. | Open, low risk |
| Deploy | The systemd unit only sets `NoNewPrivileges`, so the service sees the whole home folder. | Open, medium risk |
| Auth | The 4 MB JSON body is parsed before the login check. The Cloudflare token is forwarded to `BIGMIKE_URL`, which is safe only while it stays on loopback. A local user could swap a folder for a symlink between the check and the write. | Open, low risk |

**What holds up**
- **Paths and writes:** traversal, symlinks, hidden or secret-like names, and moving or deleting nested repositories are blocked. Overwriting needs a matching hash, and uploads never overwrite.
- **Git:** each commit contains only the touched paths, with no force-push and no `--no-verify`. On a conflict the commit stays local.
- **Cloudflare Access:** all 13 routes I tested return 401 without a valid token. Writes also need the `X-Second-Brain: 1` header.

**Health access**
- The app cannot reach the Health app or its database. It is confined to the second-brain folder, there are no symlinks out of it, and database and key files are never listed.
- The one real exposure is `memory/bigmike/chats/project_health/`. It holds the full text of your Health chats, and the app shows and searches it. The question box can also send excerpts of it to a model.

**For you to decide**
1. Whether to hide the Health and Finance chats from the app. The alternative is to restrict the Cloudflare Access policy to your email only.
2. Whether to add `ProtectSystem=strict`, `ProtectHome=read-only`, `ReadWritePaths=<second-brain>` and `PrivateTmp=true` to `deploy/second-brain.service`. This needs a restart, which I didn't do.

How to check: read `docs/security-review-phase5.md` in `second-brain-app`, then run `npm test` there and look for `server/tests/security.test.ts` with 9 passing tests.
