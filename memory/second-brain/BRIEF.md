# Second Brain: brief
Updated: 2026-11-27 · Refresh: see end · Contract: `memory/README.md`
Sources: `second-brain-app/README.md`, `second-brain-app/deploy/README.md`, `second-brain/README.md`, wiki `projects/second-brain-app`, `topics/memory-wiki`, `decisions/all-application-memory-under-second-brain`, `wiki/gantry-memory-excluded.md`, Lab MIC-269, 272, 283, 303, 304, 320, 324, 341, 413, 524; `agent-skills/doc-ocr/SKILL.md`.

## What it is
Two things: the vault `/home/beedme/data/workspace/second-brain` (Markdown memory + central atomic data warehouse `memory/warehouse/warehouse.sqlite`) and the web app "Memory / Second Brain" that browses, edits, searches, and triggers warehouse syncs, with a chat on the graph view and an Import History tab.

## Stack and where the code lives
App repo `/home/beedme/data/workspace/second-brain-app` (Node API + React/Vite + `node:sqlite` warehouse runner; `npm test`, `npm run build`, `node scripts/warehouse.mjs sync [app]`). Own systemd user unit `second-brain.service`, port 3739, public `memory.beedme.online` behind Cloudflare Access, plus nightly timer `second-brain-warehouse.timer` (03:05). Vault repo `michelemelone/second-brain-memory`; `memory/bigmike/`, `memory/library/`, and `memory/warehouse/` are separate or gitignored.

## Where the data lives
- **Structured atomic data (source for any data question):** `memory/warehouse/warehouse.sqlite` (gitignored; manifest `memory/warehouse/SCHEMA.md`), synced idempotently from every app (read-only on source, no secrets).
- **Markdown only:** `memory/<app>/` (`BRIEF.md`, `lab/`), `memory/bigmike/{chats,wiki,lab}`, `memory/library/` (imports), `wiki/`. Old monthly summary generators (`gen_finance_summary.py`, `gen_health_summary.py`) were removed in MIC-524. Layout and rules: `second-brain/README.md`.

## Current state
Central warehouse framework, `sync_log`, `SCHEMA.md` generator, 10 app adapter skeletons, CLI (`node scripts/warehouse.mjs sync`), UI sync button, and nightly timer live (MIC-524). Per-app Lab history in `memory/<app>/lab/` with `memory/lab-index.md` (MIC-303). Nightly chat sync 03:15, warehouse sync 03:05.

## Decisions that constrain changes
- Gantry never reads the vault; Gantry memory excluded (MIC-13), only `memory/gantry/lab/` allowed (MIC-303).
- The app can reach only the vault root: no `..`, symlinks, dotfiles, credentials, databases; writes need header `X-Second-Brain: 1`; secrets guard rejects keys (422); overwrite needs a content hash (409) (`docs/security-review-phase5.md`).
- Every app write is one git commit, pushed (trailer `Second-Brain-Edit: manual`).
- Agents write only in the wiki and vault folders, never in sources; a chat moved to Trash leaves no trace.
- English only; Markdown views only.

## Recent work
MIC-512 (2026-11-26): Complete architecture review — defined "Second Brain as central authority," GET /api/summary contract, nightly Markdown exports for all apps, cross-domain querying design, phased delivery plan MIC-511–MIC-518 (weekend). MIC-413 the import path runs Office/HTML/CSV/JSON through the `markitdown` skill (doc-ocr/ocr.sh), not raw text; MIC-341 multi-select in the explorer; MIC-324 drag-and-drop moves; MIC-320 chat composer redesign; MIC-304 application briefs.

## Known pitfalls
- Service needs `Environment=PATH` or engines show "NOT INSTALLED" (MIC-195).
- Proxy URL `/api` + `/api/memory/repo` returned 401 (fixed 2026-11-17).
- MIC-283 and MIC-272 were not checked in a browser.
- Document import (MIC-413): only one converter decides per format, `agent-skills/doc-ocr/SKILL.md` — PDF/EPUB/images keep PyMuPDF/Tesseract, DOCX/XLSX/PPTX/HTML/CSV/JSON go to `markitdown/scripts/convert.sh` (venv `~/.venvs/agent-skills`, pinned `markitdown==0.1.9`). `.doc`, `.odt`, `.rtf` are not convertible: no converter supports them.

## How to verify and restart
`cd second-brain-app && npm test && npm run build`; check `curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:3739/api/tree` (401 behind Access). Restart: `bigmike-restart "Second Brain" --task <KEY>`.

Refresh: after a Lab task of Second Brain finishes, or on request, update this file from itself.
