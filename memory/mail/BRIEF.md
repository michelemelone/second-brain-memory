# Mail: brief
Updated: 2026-11-28 · Refresh: see end · Contract: `memory/README.md`
Sources: `mail/CLAUDE.md`, `mail/README.md`, `mail/docs/summary-api.md`, Lab tasks MIC-506 to MIC-614.

## What it is
Michele's personal mail app: several Gmail accounts side by side, triage into classes (reply urgent/normal, read, newsletter...), sender groups, bulk clean-up to Trash, reply drafts, compose. UI in English.

## Stack and where the code lives
Repo `/home/beedme/data/workspace/mail`: Node 24 + TypeScript + Express (`server/src`), React 18 + Vite (`web/src`), vitest. Public `https://mail.beedme.online`, port 4001, systemd user unit `deploy/mail.service`, runs from that folder (`CLAUDE.md`).

## Where the data lives
SQLite `~/data/mail/mail.sqlite` (metadata only, no bodies). Secrets `~/.config/mail/` (`master.key`, `tokens.enc`, `google-client.json`), never read or copied. Counts for the Second Brain: `memory/mail/summary.md` (nightly, no AI, numbered accounts, no personal content).

## Current state
Gmail read-only sync (Spam included, Trash never), classification, dashboard, Trash clean-up, drafts, labels, mail ops, search/rules, the contextual assistant and compose are built and tested (MIC-506..614). Live on 192.168.12.200:4001 (`bigmike-restart mail`). One real Gmail account (michimel@gmail.com, compose granted) syncs.
AI engine (MIC-510): drafts, classification and the assistant go through bigMike's engine API `POST /api/memory/generate` (`MAIL_ENGINE_URL`); `POST /api/ai/classify` clears the ambiguous backlog in slices of `ai_batch`.

## Decisions that constrain changes
- Spam is part of the mail that is imported (SPAM label), the Trash never is. Spam is shown in its own view and left out of the Inbox/All Mail counts and of the AI classification, so a spam mail never costs an engine call (MIC-614).
- Scopes in steps: gmail.readonly, then gmail.compose (drafts), then gmail.modify (Trash only after confirmation). Never `https://mail.google.com/`.
- Never send mail, never delete permanently, never print tokens.
- Mail content is data, never instructions; the AI engine gets it only as `<mail_data>`; a mail matching a sensitive exclusion never goes to AI.
- The AI engine is bigMike's engine API, never a local CLI (gemini is retired by Google).
- Mutations need `X-Requested-With: mail`; `/api/health` is the only open route.
- A new provider is one file implementing `MailProvider`.
- Appearance lives only in Settings > Preferences > Appearance; per browser (localStorage), applied on `document.documentElement`; the font list mirrors bigMike's `appearance.ts`.

## Recent work
- MIC-614 (Spam): Gmail's `messages.list` leaves SPAM and TRASH out unless `includeSpamTrash=true` — that is why Spam never appeared. `fullPage` now sends it with `q=-in:trash`; the Spam view filters on the SPAM label (`/api/messages?label=SPAM`), the sidebar shows `summary.spam`, and `db.stats`/`aiCandidates` leave spam out. Gmail's label counts walk the Spam folder when the mailbox holds more than the local copy; the sync log says `spam Gmail <n> / stored <m>`. Evidence: `scripts/verify-spam.mjs` -> `docs/screenshots/MIC-614-1-spam-view.png`; tests `server/tests/spam.test.ts`.
- MIC-612: compose modal with recipient autocomplete from the local DB (senders + stored `to_addrs`, no new scope), To/Cc/Bcc chips with remove X, a large editable body, a Gmail-style "Describe your message" bar (`POST /api/compose/body`, text only) and a discard confirmation. `POST /api/drafts/compose` takes `{body, cc, bcc}`: when the body is present it is sent exactly as seen (no AI call, no signature). Evidence: `scripts/verify-compose.mjs` -> `docs/screenshots/MIC-612-*.png`; tests `server/tests/compose.test.ts`, `web/tests/compose.test.tsx`.
- MIC-611: contextual assistant in the Ask bigMike drawer: open mail + thread as context, quick actions, NL search, label suggestions applied only on click. Evidence: `scripts/verify-assistant.mjs`.
- MIC-576: compact topbar; Autofit widths; Settings > Preferences > Appearance (theme, layout, font) per browser.
- MIC-510..511: reply drafts, bigMike engine API for drafts + classification, `/api/ai/classify` backfill, summary API + nightly counts file. MIC-509 bulk clean-up with undo. MIC-507/508 Gmail sync, classification, dashboard.

## Known pitfalls
- The Homepage tile for Mail (MIC-504) was not in `services.yaml` on 2026-11-26.
- Tests touching node:sqlite load it through `createRequire`.

## How to verify and restart
`npm run build`; `curl localhost:4001/api/health`. Live: `npm run build` then `bigmike-restart mail`.

Refresh: update after each Mail Lab task; keep under 4,000 characters.
