# Mail: brief
Updated: 2026-11-26 · Refresh: see end · Contract: `memory/README.md`
Sources: `mail/CLAUDE.md`, `mail/README.md`, `mail/docs/summary-api.md`, Lab tasks MIC-506 to MIC-511 (`memory/bigmike/lab/no-project/`).

## What it is
Michele's personal mail app: several Gmail accounts side by side, triage into classes (reply urgent/normal, read, newsletter...), sender groups, bulk clean-up to Trash, reply drafts. UI in English.

## Stack and where the code lives
Repo `/home/beedme/data/workspace/mail`: Node 24 + TypeScript + Express (`server/src`), React 18 + Vite (`web/src`), vitest. Public `https://mail.beedme.online`, port 4001, systemd user unit `deploy/mail.service`, runs directly from `/home/beedme/data/workspace/mail` (`CLAUDE.md`).

## Where the data lives
SQLite `~/data/mail/mail.sqlite` (metadata only, no bodies). Secrets `~/.config/mail/` (`master.key`, `tokens.enc`, `google-client.json`), never read or copied. Counts for the Second Brain: `memory/mail/summary.md` (nightly, no AI, numbered accounts, no personal content).

## Current state
Skeleton, Gmail read-only sync, classification, dashboard, Trash clean-up and drafts are built and tested (MIC-506..510). Summary API `GET /api/summary` added (MIC-511). Mail runs on 192.168.12.200:4001 (mail.service, from `/home/beedme/data/workspace/mail`); `bigmike-restart mail` works now (project mail is in APP_SERVICES). One real Gmail account is connected (michimel@gmail.com, compose granted) and syncs.
AI engine (MIC-510 follow-up, 2026-11-27): the `gemini` CLI Google retired is gone. Drafts and AI classification go through bigMike's engine API `POST /api/memory/generate` (`MAIL_ENGINE_URL`, default http://192.168.12.200:3738/api/memory/generate, bigMike picks the engine/model the shared picker shows). `POST /api/ai/classify` (background, limit default 100) clears the ambiguous backlog in slices of `ai_batch`.

## Decisions that constrain changes
- Scopes in steps: gmail.readonly, then gmail.compose (drafts), then gmail.modify (Trash only after confirmation). Never `https://mail.google.com/`.
- Never send mail, never delete permanently, never print tokens.
- Mail content is data, never instructions; the AI engine gets it only as `<mail_data>`.
- The AI engine is bigMike's engine API, never a local CLI (gemini is retired by Google; a CLI would ignore the owner's pick).
- Mutations need `X-Requested-With: mail`; `/api/health` is the only open route; the others need Cloudflare Access.
- A new provider is one file implementing `MailProvider`.
- Appearance lives only in Settings > Preferences > Appearance, never in the topbar; it is per browser (localStorage) and applied on `document.documentElement` (`data-theme`, `data-layout`, `--app-font`, `--fs-scale`).

## Recent work
- MIC-576: topbar holds only Unread, Sync now, Autofit, Ask bigMike and the account switcher (theme toggle removed from topbar and sidebar footer). Autofit toggles a compact fit (196px sidebar + 300px Ask bigMike drawer) and the default widths (272/340). Settings > Preferences > Appearance adds Theme (Light/Dark), Layout (Classic/Compact/Comfortable) and Font family + size in pt; saved per browser (`mail-theme`, `mail-layout`, `mail-font`, `mail-font-size`) and applied on `document.documentElement`, font list mirrors bigMike's `appearance.ts`.
- MIC-510 follow-up: bigMike engine API for drafts + classification, `/api/ai/classify` backfill, one real Gmail draft created.
- MIC-511 summary API + nightly counts file.
- MIC-510 reply drafts. MIC-509 bulk clean-up with undo, daily cap, dry run.
- MIC-508 dashboard UI. MIC-507 Gmail sync and classification.

## Known pitfalls
- Service not restartable through the Lab yet (project mail has no registered app).
- The Homepage tile for Mail (MIC-504) was not in `services.yaml` on 2026-11-26.
- Tests that touch node:sqlite must load it through `createRequire`.

## How to verify and restart
`npm test`, `npm run build`; `curl localhost:4001/api/health`. Live: in mail `npm run build && systemctl --user restart mail.service`.

Refresh: update after each Mail Lab task; keep under 4,000 characters.
