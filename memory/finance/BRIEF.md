# Finance: brief
Updated: 2026-11-18 · Refresh: see end · Contract: `memory/README.md`
Sources: `personal-finance/CLAUDE.md`, `personal-finance/README.md`, `personal-finance/finance-web.service`, wiki `projects/personal-finance`, `memory/finance/<YYYY-MM>.md`. Lab history of this app: none yet (`memory/finance/lab/` empty).

## What it is
Michele's personal finance workspace: a "Ledger" web app over his bank and card transactions (Yuh, Revolut), plus FIRE/investing notes. Lives in Zurich, spends in CHF/EUR/USD. Nobody here is a licensed tax or financial adviser.

## Stack and where the code lives
Repo `/home/beedme/data/workspace/personal-finance`. App in `web/`: Next.js 16 + Tailwind 4 + Recharts, port 3000, public at `https://finance.beedme.online` (Nginx Proxy Manager + Cloudflare). Importer `scripts/normalize_yuh.py`. `app/` and `scripts/build_standalone.py` are the old static page, unused (`CLAUDE.md`).

## Where the data lives
`personal-finance/data/`: `transactions*.csv` (unique `id`, column `account`), `overrides.csv` (manual fixes, win over everything), `merchants.csv` (global rules), `fx_rates.json` (ECB cache), `imports/raw/` (original files). Login secrets only in `web/.env.local` (never read or copy). Raw transactions stay in the app; here only `memory/finance/<YYYY-MM>.md` (generated, no AI, original currencies).

## Current state
About 3,300 moves; accounts Yuh and Revolut. Pages: Dashboard, Cards, Transactions, Categories, Merchants, Analytics, Review, Settings (AI import Beta, default model `claude-opus-5-5`). Test suite: unknown, none documented.

## Decisions that constrain changes
- UI is entirely English; default period "Year to date" (`CLAUDE.md`).
- Multi-currency schema: transaction CSVs persist `amount_chf`, `amount_eur`, `amount_usd`, `fx_rate_applied` (historical ECB day rate with weekend/holiday fallback).
- New data source = new `transactions_*.csv` with the same schema; the loader reads `transactions*.csv`.
- Corrections go to `overrides.csv` / `merchants.csv`; they survive re-imports.
- Anthropic key stays in `web/.env.local`, never sent to the browser.
- Multi-currency conversions use daily ECB rates in `fx_rates.json`.

## Recent work (no Lab keys yet; from the wiki)
- 2026-11-27 MIC-546: Multi-currency transaction schema (CHF, EUR, USD) and historical rate backfill.
- 2026-11-14 Account tabs, chart filter toggles, value labels.
- 2026-11-13 Ledger overhaul, Settings, AI document import, public domain.
- Earlier: Revolut import, systemd unit (`b22d2af`).

## Known pitfalls
- `web/scripts/set-password.mjs` ALWAYS writes the real `web/.env.local`, even when run elsewhere: test credentials/import on a separate copy (`CLAUDE.md`).
- Port 3000 needed a host firewall rule so the proxy container can reach it (wiki 2026-11-13).
- CSV-only changes need no rebuild; code changes do.

## How to verify and restart
After code changes: `cd web && npx next build`, then restart the user service `finance-web.service` (unit in the repo; runs `next start -p 3000`, log `web-server.log`); in a Lab task use `bigmike-restart "Finance app" --task <KEY>`. Check `curl localhost:3000`.

Refresh: after a Lab task of Finance finishes, or on request, update this file from itself (compress, do not restart from zero).
